"""Generate experiments/r7_parallel.ipynb from ill/colab_runner_r7.ipynb (run from experiments/).
Each (instance, metric) pair runs as its own background process; the 5 initial points of a method run
in one batch (B=5). Selection rules, grids and the validity filter are unchanged."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
_cells = json.load(open(os.path.join(HERE, "ill", "colab_runner_r7.ipynb")))["cells"]
_code = ["".join(c["source"]) for c in _cells if c["cell_type"] == "code" and "".join(c["source"]).strip()]
_by_head = {s.split("\n", 1)[0][:4]: s for s in _code}
SRC_ENV, SRC_DATA, SRC_PROB, SRC_ALG, SRC_RUN = (_by_head[k] for k in ("# 1.", "# 3.", "# 4.", "# 5.", "# 6."))

CONFIG = '''
DATA_DIR = "/content/data"
EXP_ROOT = "/content/drive/MyDrive/3_DDLALM_exp"
OUT_DIR = os.environ.get("R7_OUT_DIR", os.path.join(EXP_ROOT, "ill", "results"))
WB_CACHE_DIR = EXP_ROOT
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
SEED = 0
SEEDS = [0, 1, 2, 3, 4]
ILL_EPS = 1e-5
ILL_BUDGET = 15000
WB_EPS = 1e-3
WB_BUDGET = 4000
MN_EPS = 1e-4
MN_BUDGET = 4000
BATCH_SIZE = 128 if DEVICE.type == "cuda" else 16
'''


def _patch(src, old, new, count):
    assert src.count(old) == count, (old[:60], src.count(old))
    return src.replace(old, new)


alg = SRC_ALG
alg = _patch(alg, "    x = P.init_x().unsqueeze(0).expand(B, -1).clone()\n",
             "    x = _init_batch(P, B)\n", 3)
alg = _patch(alg, "        assert B == 1\n",
             '        inf_b = torch.full((B,), float("inf"), device=dev, dtype=dt)\n', 3)
alg = _patch(alg, '''        if record_trace:
            _sync(dev)
            ok = bool(_valid(x)[0])
            calls.append(call); stat_l.append(st[0].item() if ok else float("inf")); viol_l.append(vi[0].item() if ok else float("inf"))
            t_l.append(time.perf_counter() - t0)
            ob, cv = P.metrics(x[0]) if ok else (float("inf"), float("inf"))
            obj_l.append(ob); cv_l.append(cv)
''', '''        if record_trace:
            okv = _valid(x)
            calls.append(call)
            stat_l.append(torch.where(okv, st, inf_b)); viol_l.append(torch.where(okv, vi, inf_b))
            obj_l.append(torch.where(okv, _obj_batch(P, x), inf_b))
''', 3)
alg = _patch(alg, '''    if record_trace:
        st_a, vi_a = np.array(stat_l), np.array(viol_l)
        return dict(calls=np.array(calls), stat=st_a, viol=vi_a,
                    kkt=np.maximum(st_a, vi_a), elapsed=np.array(t_l),
                    obj=np.array(obj_l), cviol=np.array(cv_l))
    return _tune_scores(P, x, st, vi, hit_call, best_kkt)
''', '''    if record_trace:
        return _batch_traces(calls, stat_l, viol_l, obj_l, t0, dev)
    return _tune_scores(P, x, st, vi, hit_call, best_kkt)
''', 3)
alg += '''

def _init_batch(P, B):
    X0 = getattr(P, "_x0_batch", None)
    if X0 is not None:
        assert X0.shape[0] == B
        return X0.clone()
    return P.init_x().unsqueeze(0).expand(B, -1).clone()


@torch.no_grad()
def _obj_batch(P, X):
    """Objective of each row of X; same formulas as P.metrics."""
    if isinstance(P, IllCondL1):
        return 0.5 * torch.log1p((X - P.d) ** 2).sum(-1) + (X @ P.B.T - P.c).abs().sum(-1)
    if isinstance(P, WaterbirdsGroupDRO):
        A, _, _ = P.oracle(X)
        return P.lam_reg * (torch.sqrt(1.0 + ((X - P.x0) ** 2).sum(-1)) - 1.0) + A.max(dim=-1).values
    return torch.tensor([P.metrics(x)[0] for x in X], device=X.device, dtype=X.dtype)


def _batch_traces(calls, stat_l, viol_l, obj_l, t0, dev):
    """One trace dict per batch row. elapsed spreads the batch wall time uniformly (not used in figures)."""
    _sync(dev)
    total = time.perf_counter() - t0
    st = torch.stack(stat_l).cpu().numpy()
    vi = torch.stack(viol_l).cpu().numpy()
    ob = torch.stack(obj_l).cpu().numpy()
    c = np.array(calls)
    T = len(calls)
    el = total * np.arange(1, T + 1) / T
    nanv = np.full(T, np.nan)
    return [dict(calls=c, stat=st[:, b], viol=vi[:, b], kkt=np.maximum(st[:, b], vi[:, b]),
                 elapsed=el, obj=ob[:, b], cviol=nanv) for b in range(st.shape[1])]
'''

run = SRC_RUN
run = _patch(run, '''    for sd in seeds:
        P.seed = sd
        tr = _run_best(P, name, best_cfg, budget, eps)
''', '''    traces = _run_best_multi(P, name, best_cfg, budget, eps, seeds)
    for sd, tr in zip(seeds, traces):
''', 1)
run += '''

def _run_best_multi(P, name, cfg, budget, eps, seeds):
    """Run one configuration from all initial points; batched except iALM (data-dependent inner loop)."""
    if name == "iALM":
        out = []
        for sd in seeds:
            P.seed = sd
            out.append(ialm_single(P, budget, eps, cfg, record_trace=True))
        return out
    X0 = []
    for sd in seeds:
        P.seed = sd
        X0.append(P.init_x())
    P._x0_batch = torch.stack(X0)
    cfgs = [cfg] * len(seeds)
    try:
        if name == "Fast LRALM":
            return fast_lralm_run(P, budget, eps, cfgs, record_trace=True)
        if name == "Smoothed GDA":
            return lralm_run(P, budget, eps, cfgs, beta=1.0, record_trace=True)
        if name == "Perturbed Smoothed GDA":
            return lralm_run(P, budget, eps, cfgs, beta=0.0, record_trace=True)
        if name == "Zhang-Xu Alg. 1":
            return zhang_xu_run(P, budget, eps, cfgs, record_trace=True)
        raise ValueError(name)
    finally:
        P._x0_batch = None
'''

LIB = "\n\n".join([SRC_ENV, CONFIG, SRC_DATA, SRC_PROB, alg, run])
JOB_TAIL = '''

import sys
kind, arg, metric = sys.argv[1], sys.argv[2], sys.argv[3]
if kind == "cache":  # build the Waterbirds feature cache once before the water jobs start
    load_waterbirds_features(cache_dir=WB_CACHE_DIR)
    sys.exit(0)
if kind == "check":  # batched rerun of the saved sigma=1e-2 viol-selected configurations vs the serial results
    res = os.path.join(EXP_ROOT, "ill", "results")
    ref = np.load(os.path.join(res, "illcond_1e-02_r7_viol.npz"))
    meta = json.load(open(os.path.join(res, "illcond_1e-02_r7_viol.json")))
    P = IllCondL1(sigma_min=1e-2, seed=SEED)
    for name in ("Fast LRALM", "Smoothed GDA", "Zhang-Xu Alg. 1"):
        t0 = time.time()
        trs = _run_best_multi(P, name, meta[name]["params"], ILL_BUDGET, ILL_EPS, SEEDS)
        abs_err, fin_rel = 0.0, 0.0
        for sd, tr in zip(SEEDS, trs):
            for k in ("stat", "viol", "obj"):
                a, b = tr[k], ref[f"{name}|{sd}|{k}"]
                assert a.shape == b.shape and (np.isfinite(a) == np.isfinite(b)).all(), (name, sd, k)
                m = np.isfinite(b)
                abs_err = max(abs_err, float(np.max(np.abs(a[m] - b[m]))))
                fin_rel = max(fin_rel, abs(a[-1] - b[-1]) / max(abs(b[-1]), 1e-300))
        print(f"{name:24s} max abs diff {abs_err:.2e} | final-value rel diff {fin_rel:.2e} | {time.time() - t0:.1f}s for 5 seeds")
    sys.exit(0)
if kind == "ill":
    sm = float(arg)
    tag = f"illcond_{sm:.0e}_r7"
    P = IllCondL1(sigma_min=sm, seed=SEED)
    verify_oracle(P, f"IllCondL1(sigma_min={sm:g})")
    budget, eps = ILL_BUDGET, ILL_EPS
else:
    tag = "waterbirds_gdro_r7"
    A_wb, b_wb, g_wb = load_waterbirds_features(cache_dir=WB_CACHE_DIR)
    P = WaterbirdsGroupDRO(A_wb, b_wb, g_wb, hidden=4, lam_reg=1e-2, seed=SEED)
    verify_oracle(P, "WaterbirdsGroupDRO")
    budget, eps = WB_BUDGET, WB_EPS
if all(os.path.isfile(os.path.join(OUT_DIR, f"{tag}_{metric}{ext}")) for ext in (".npz", ".json")):
    print(f"Skipping {tag}_{metric}: already saved.")
    sys.exit(0)
run_experiment(tag, P, budget=budget, eps=eps, metrics=(metric,))
print("JOB DONE")
'''
JOB = LIB + JOB_TAIL
compile(JOB, "r7_job.py", "exec")

C_SETUP = '''# 1. 挂载 Drive、确认 GPU
import os, sys, time, subprocess
from google.colab import drive
drive.mount("/content/drive")
print(subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                     capture_output=True, text=True).stdout)
RUN_DIR = "/content/r7_parallel"
os.makedirs(RUN_DIR, exist_ok=True)'''
C_CHECK = '''# 3. 预先建立 Waterbirds 特征缓存；批量版本与已存 σ=1e-2 串行结果逐点比较
def _job(*args):
    r = subprocess.run([sys.executable, "-u", os.path.join(RUN_DIR, "r7_job.py"), *args],
                       capture_output=True, text=True, cwd=RUN_DIR)
    print(r.stdout[-3000:], r.stderr[-3000:])
    assert r.returncode == 0, args

_job("cache", "-", "-")
_job("check", "-", "-")'''
C_START = '''# 4. 启动并行任务（σ=1e-3、1e-4 与 water 各三个指标）：每个 (实例, 指标) 一个后台进程，结果按 {tag}_{metric} 分别存盘
JOBS = ([("ill", sm, m) for sm in ("1e-3", "1e-4") for m in ("viol", "stat", "obj")]
        + [("water", "-", m) for m in ("viol", "stat", "obj")])  # jobs whose results are already saved exit at once
EXP_ROOT = "/content/drive/MyDrive/3_DDLALM_exp"
procs = {}
for kind, arg, metric in JOBS:
    out_dir = os.path.join(EXP_ROOT, "ill" if kind == "ill" else "water", "results")
    name = f"{kind}_{arg}_{metric}"
    log = open(os.path.join(RUN_DIR, f"{name}.log"), "w")
    procs[name] = subprocess.Popen([sys.executable, "-u", os.path.join(RUN_DIR, "r7_job.py"), kind, arg, metric],
                                   stdout=log, stderr=subprocess.STDOUT, cwd=RUN_DIR,
                                   env={**os.environ, "R7_OUT_DIR": out_dir})
print(f"Started {len(procs)} jobs:", ", ".join(procs))'''
C_WATCH = '''# 5. 查看进度（可反复运行）：每个任务的状态和日志最后两行
for name, p in procs.items():
    lines = open(os.path.join(RUN_DIR, f"{name}.log")).read().strip().splitlines()
    state = "running" if p.poll() is None else f"exit {p.returncode}"
    print(f"{name:16s} {state:8s} | " + " || ".join(l.strip() for l in lines[-2:]))'''


def _cell(kind, src):
    lines = src.split("\n")
    c = {"cell_type": kind, "metadata": {}, "source": [l + "\n" for l in lines[:-1]] + [lines[-1]]}
    if kind == "code":
        c.update(execution_count=None, outputs=[])
    return c


nb = {"cells": [
    _cell("markdown", "# r7 并行运行\n\n由 `make_r7_parallel.py` 从 `ill/colab_runner_r7.ipynb` 生成，选参规则不变。"
                      "每个 (实例, 指标) 一个后台进程；同一方法的 5 个初始点放进同一批一起跑（iALM 除外）。"
                      "运行时选 A100，然后全部运行。"),
    _cell("code", C_SETUP),
    _cell("code", "%%writefile /content/r7_parallel/r7_job.py\n" + JOB),
    _cell("code", C_CHECK),
    _cell("code", C_START),
    _cell("code", C_WATCH),
], "metadata": {"accelerator": "GPU", "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
   "nbformat": 4, "nbformat_minor": 5}
out = os.path.join(HERE, "r7_parallel.ipynb")
with open(out, "w") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Wrote", out)
