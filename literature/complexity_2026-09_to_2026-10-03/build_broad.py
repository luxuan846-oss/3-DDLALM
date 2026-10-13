import json,re
from pathlib import Path
ROOT=Path(__file__).parent
src=json.loads((ROOT/'raw/math_oc_new.json').read_text())['rows']
kw={
 '非光滑与复合优化':r'non.?smooth|nonsmooth|weakly convex|prox|composite|subgradient|Moreau|Clarke|directional station',
 '凸优化与加速':r'convex|strongly convex|acceleration|Frank.?Wolfe|linear minimization|first.?order oracle|gradient descent',
 '极小极大与博弈':r'minimax|min.?max|saddle|concave|game|regret|variational inequality|monotone',
 '双层优化':r'bilevel|multilevel|hypergradient',
 '约束与增广拉格朗日':r'constrained|constraint|augmented Lagrangian|penalty|ADMM|primal.?dual|feasibility',
 '随机与机器学习优化':r'stochastic|SGD|AdaGrad|Adam|Muon|learning|federated|reinforcement|policy gradient|bandit',
 '流形与最优传输':r'Riemannian|manifold|Wasserstein|optimal transport|matrix space',
 '变分包含与不动点':r'inclusion|fixed point|operator splitting|extragradient|forward.?backward|Krasnoselskii',
 '控制与动态优化':r'optimal control|stabilization|Lyapunov|MPC|dynamical|Hamilton',
 '组合与离散优化':r'linear programming|integer programming|quadratic programming|QUBO|combinatorial|routing|scheduling|packing|Markov decision',
 '采样与贝叶斯优化':r'Bayesian optimization|Langevin|sampling|trust.?region|zeroth.?order|derivative.?free',
}
out=[]
for p in src:
 s=p['title']+' '+p['abstract']; fields=[f for f,pat in kw.items() if re.search(pat,s,re.I)]
 if not fields: fields=['数学优化相关其他']
 p={**p,'field':'；'.join(fields[:3]),'scope':'math.OC 全量窗口','evidence_level':'arXiv 元数据与摘要级归类','complexity':'摘要未必包含显式复杂度；请按标题、摘要和分区筛选','source_note':'arXiv math.OC；2026-09-01 至 2026-10-03 首次发布'}
 out.append(p)
(ROOT/'broad_math_oc.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('broad',len(out))
