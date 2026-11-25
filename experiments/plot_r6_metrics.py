"""Plot the three metrics in the original paper style.

r6 reads one {tag}_r6.npz for all metrics; r7 reads {tag}_r7_{metric}.npz, whose parameters
were selected by that metric."""

import argparse
from pathlib import Path

import numpy as np

from plot_paper import EXPERIMENTS_DIR, RESULT_DIRS, panel

import matplotlib.pyplot as plt


INSTANCES = (
    ("ill", "illcond_1e-02", r"IllCondL1, $\sigma_{\min}=10^{-2}$", 15000, 1e-5),
    ("ill", "illcond_1e-03", r"IllCondL1, $\sigma_{\min}=10^{-3}$", 15000, 1e-5),
    ("ill", "illcond_1e-04", r"IllCondL1, $\sigma_{\min}=10^{-4}$", 15000, 1e-5),
    ("water", "waterbirds_gdro", "Waterbirds Group DRO", 4000, 1e-3),
)
METRICS = (
    ("stat", "Stationarity residual", "stationarity", True),
    ("viol", "Proximal feasibility residual", "feasibility", True),
    ("obj", "Objective value", "objective", False),
)


def plot_metric(instances, data_dir, out_dir, metric, ylabel, filename, log_scale, round_="r6"):
    fig, axes = plt.subplots(1, len(instances), figsize=(max(6, 3.6 * len(instances)), 3.2), squeeze=False)
    for index, (axis, (group, tag, title, budget, eps)) in enumerate(zip(axes[0], instances)):
        name = f"{tag}_r6.npz" if round_ == "r6" else f"{tag}_{round_}_{metric}.npz"
        with np.load((data_dir or RESULT_DIRS[group]) / name) as data:
            panel(axis, data, metric, budget, eps if log_scale else None, log_scale,
                  ylabel if index == 0 else None)
        axis.set_title(title, fontsize=11)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    legend_columns = 3 if len(instances) == 1 else len(labels)
    fig.legend(handles, labels, loc="upper center", ncols=legend_columns, bbox_to_anchor=(0.5, 1.12))
    fig.tight_layout()
    for extension in ("pdf", "png"):
        fig.savefig(out_dir / f"{filename}.{extension}", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main(group=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--round", dest="round_", default="r6", choices=("r6", "r7"))
    args = parser.parse_args()
    instances = tuple(instance for instance in INSTANCES if group is None or instance[0] == group)
    default_dir = RESULT_DIRS[group] if group is not None else EXPERIMENTS_DIR / "results"
    out_dir = args.out or (args.data or default_dir) / f"{args.round_}_metrics"
    out_dir.mkdir(parents=True, exist_ok=True)
    for metric, ylabel, filename, log_scale in METRICS:
        plot_metric(instances, args.data, out_dir, metric, ylabel, filename, log_scale, args.round_)


if __name__ == "__main__":
    main()
