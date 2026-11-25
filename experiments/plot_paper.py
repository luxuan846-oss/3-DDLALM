"""Paper figures for Section 5 from the r6 result files.

Usage:  python plot_paper.py [--dir flat_results] [--suffix _r6] [--out results]

Reads the three illcond_*{suffix}.npz files and waterbirds_gdro{suffix}.npz
Writes fig_kkt.pdf      best-so-far R_KKT vs oracle calls, one panel per instance
       fig_obj.pdf      objective vs oracle calls, one panel per instance
Each curve is the mean over the five initial points; the band is the min-max range.
"""
import argparse
import os
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEEDS = [0, 1, 2, 3, 4]
EXPERIMENTS_DIR = Path(__file__).resolve().parent
RESULT_DIRS = {group: EXPERIMENTS_DIR / group / "results" for group in ("ill", "water")}
METHODS = [  # (key in npz, legend label, color, linestyle, linewidth, zorder)
    ("Fast LRALM", "Fast LRALM", "#c0392b", "-", 2.4, 10),
    ("Smoothed GDA", "Smoothed GDA", "#2e7d32", (0, (3.5, 3.5)), 1.8, 7),
    ("Perturbed Smoothed GDA", "Perturbed Smoothed GDA", "#1f4fd6", (3.5, (3.5, 3.5)), 1.8, 6),
    ("iALM", "iALM", "#8e44ad", "-.", 1.6, 4),
    ("Zhang-Xu Alg. 1", "MC-EGM", "#e67e22", (0, (5, 1.5, 1, 1.5)), 1.6, 4),
]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 11,
    "axes.linewidth": 0.8,
    "legend.frameon": True,
    "legend.fancybox": False,
    "legend.edgecolor": "black",
    "legend.fontsize": 11,
})


def curves(D, name, key, xmax, log):
    """Mean and min-max band of the latest available values at each oracle budget."""
    grid = np.arange(1, xmax + 1)
    ys = []
    for sd in SEEDS:
        k = f"{name}|{sd}|{key}"
        if k not in D:
            return None
        x = D[f"{name}|{sd}|calls"]
        y = np.nan_to_num(D[k].astype(float), nan=np.inf, posinf=np.inf)
        if key == "kkt":
            y = np.minimum.accumulate(y)
        indices = np.searchsorted(x, grid, side="right") - 1
        ys.append(np.where(indices >= 0, y[np.maximum(indices, 0)], np.nan))
    ys = np.array(ys)
    if log:
        ys = np.clip(ys, 1e-16, 1e6)
    ok = np.isfinite(ys).all(axis=0)
    return grid[ok], ys.mean(axis=0)[ok], ys.min(axis=0)[ok], ys.max(axis=0)[ok]


def _gda_markers(name, n_points, count=10, size=4.5):
    spacing = max(1, n_points // count)
    if name == "Smoothed GDA":
        return dict(marker="D", markevery=(spacing // 4, spacing),
                    markersize=size, markerfacecolor="white", markeredgewidth=1.1)
    if name == "Perturbed Smoothed GDA":
        return dict(marker="o", markevery=((3 * spacing) // 4, spacing),
                    markersize=size, markerfacecolor="white", markeredgewidth=1.1)
    return {}


def panel(ax, D, key, xmax, eps=None, log=True, ylabel=None):
    span = []
    plotted = []
    for name, label, col, ls, lw, z in METHODS:
        key_name = f"{name} (own alpha)" if f"{name} (own alpha)|{SEEDS[0]}|{key}" in D else name
        c = curves(D, key_name, key, xmax, log)
        if c is None or len(c[0]) == 0:
            continue
        g, m, lo, hi = c
        plotted.append((name, col, ls, lw, z, g, m, lo, hi))
        markers = _gda_markers(name, len(g))
        line_zorder = z + 6 if key == "obj" and name in ("Smoothed GDA", "Perturbed Smoothed GDA") else z
        (ax.semilogy if log else ax.plot)(g, m, color=col, ls=ls, lw=lw, zorder=line_zorder, label=label, **markers)
        ax.fill_between(g, lo, hi, color=col, alpha=0.18 if name == "Fast LRALM" else 0.10, lw=0, zorder=z - 1)
        tail = m[len(m) // 10:]
        if not log and len(tail) and np.max(tail) < 10 * abs(m[0]) + 1:
            span += [tail.min(), tail.max()]
    if not log and span:
        a, b = min(span), max(span)
        pad = 0.06 * (b - a + 1e-12)
        ax.set_ylim(a - pad, b + pad)
    if eps is not None:
        ax.axhline(eps, color="0.45", lw=0.8, ls=(0, (4, 3)), zorder=1)
    ax.set_xlim(0, xmax)
    ax.set_xlabel("Number of oracle calls")
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.grid(True, which="major", ls=":", lw=0.6, color="0.7")
    ax.tick_params(direction="in", top=True, right=True, which="both")
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0), useMathText=True)
    if key == "obj" and not log and xmax >= 5000:
        x_lo = 2500
        inset_vals = []
        for name, col, ls, lw, z, g, m, lo, hi in plotted:
            if name == "Zhang-Xu Alg. 1":
                continue
            mask = g >= x_lo
            if mask.any():
                inset_vals.extend([m[mask].min(), m[mask].max()])
        if inset_vals:
            axins = ax.inset_axes([0.40, 0.37, 0.56, 0.56])
            for name, col, ls, lw, z, g, m, lo, hi in plotted:
                mask = g >= x_lo
                if not mask.any():
                    continue
                sg, sm, slo, shi = g[mask], m[mask], lo[mask], hi[mask]
                markers = _gda_markers(name, len(sg), count=5, size=3.4)
                axins.plot(sg, sm, color=col, ls=ls, lw=max(1.3, lw - 0.4), zorder=z, **markers)
                axins.fill_between(sg, slo, shi, color=col, alpha=0.14 if name == "Fast LRALM" else 0.08, lw=0, zorder=z - 1)
            ya, yb = min(inset_vals), max(inset_vals)
            ypad = 0.10 * (yb - ya + 1e-12)
            axins.set_xlim(x_lo, xmax)
            axins.set_ylim(ya - ypad, yb + ypad)
            axins.set_xticks([5000, 10000, 15000])
            axins.set_xticklabels(["5k", "10k", "15k"], fontsize=7.5)
            axins.yaxis.set_major_locator(plt.MaxNLocator(3))
            axins.yaxis.set_major_formatter(plt.FormatStrFormatter("%.4f"))
            axins.tick_params(axis="both", direction="in", top=True, right=True, labelsize=7.5)
            axins.grid(True, ls=":", lw=0.5, color="0.78")
            for spine in axins.spines.values():
                spine.set_edgecolor("0.45")
                spine.set_linewidth(0.7)
            ax.indicate_inset_zoom(axins, edgecolor="0.45", lw=0.7, alpha=0.75)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", type=Path)
    ap.add_argument("--suffix", default="_r6")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    out = a.out or a.dir or EXPERIMENTS_DIR / "results"
    os.makedirs(out, exist_ok=True)
    sfx = a.suffix
    inst = [  # (file tag, title, eps, budget, x-range of the main-text figure)
        (f"illcond_1e-02{sfx}", r"IllCondL1, $\sigma_{\min}=10^{-2}$", 1e-5, 15000, 15000),
        (f"illcond_1e-03{sfx}", r"IllCondL1, $\sigma_{\min}=10^{-3}$", 1e-5, 15000, 15000),
        (f"illcond_1e-04{sfx}", r"IllCondL1, $\sigma_{\min}=10^{-4}$", 1e-5, 15000, 15000),
        (f"waterbirds_gdro{sfx}", "Waterbirds Group DRO", 1e-3, 4000, 1000),  # early phase in the main text
    ]
    paths = {tag: (a.dir or RESULT_DIRS["ill" if tag.startswith("illcond_") else "water"]) / f"{tag}.npz"
             for tag, *_ in inst}
    data = {tag: np.load(path) for tag, path in paths.items() if path.exists()}
    inst = [i for i in inst if i[0] in data]

    # main-text figures use the x-range of the last column; *_full figures (appendix) use the whole budget
    for full in (False, True):
        for fname, key, log, ylab in (("fig_kkt", "kkt", True, r"$\min_{k'\leq k}\mathcal{R}_{\mathrm{KKT}}$"),
                                      ("fig_obj", "obj", False, "Objective value")):
            fig, axes = plt.subplots(1, len(inst), figsize=(3.6 * len(inst), 3.2), squeeze=False)
            for j, (tag, title, eps, budget, xmain) in enumerate(inst):
                ax = axes[0, j]
                panel(ax, data[tag], key, budget if full else xmain, eps if key == "kkt" else None, log,
                      ylab if j == 0 else None)
                ax.set_title(title, fontsize=11)
            h, l = axes[0, 0].get_legend_handles_labels()
            fig.legend(h, l, loc="upper center", ncol=len(l), bbox_to_anchor=(0.5, 1.08))
            fig.tight_layout()
            name = f"{fname}_full" if full else fname
            fig.savefig(os.path.join(out, f"{name}.pdf"), bbox_inches="tight")
            fig.savefig(os.path.join(out, f"{name}.png"), dpi=160, bbox_inches="tight")
            plt.close(fig)

    print("saved figures to", out)


if __name__ == "__main__":
    main()
