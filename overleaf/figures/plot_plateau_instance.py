from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 10.5,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

out = Path(__file__).resolve().parent

eps = 0.1
delta = 1.0
xs = delta / (2.0 * eps) + eps
left = xs - 2.0 * eps
right = xs + 2.0 * eps

navy = "#204A9E"
slate = "#414E60"
orange = "#C46326"
gray = "#646E7A"


def f(x):
    d = np.abs(x - xs)
    return np.where(d <= 2.0 * eps, 0.5 * d * d, 2.0 * eps * d - 2.0 * eps ** 2)


fig, ax = plt.subplots(figsize=(6.8, 3.55))

# Shaded constant-gradient plateau [0, x_* - 2*eps]
ax.axvspan(0.0, left, color=navy, alpha=0.06, zorder=0)

# Piecewise curve
for a, b, col in [(-0.45, left, navy), (left, right, orange), (right, 7.1, navy)]:
    x = np.linspace(a, b, 400)
    ax.plot(x, f(x), color=col, lw=2.1, zorder=2)

# Key points: initial point (0, Delta) and minimizer (x_*, 0)
ax.plot([0.0], [delta], "o", color=navy, ms=4.5, zorder=4)
ax.plot([xs], [0.0], "o", color=orange, ms=4.5, zorder=4)

# Annotations on main plot
ax.annotate(
    r"$(0,\Delta)$",
    xy=(0.0, delta),
    xytext=(0.24, 1.05),
    fontsize=10.5,
    color="black",
)
ax.text(
    1.55,
    0.82,
    r"$f'(x) = -2\epsilon$",
    color=navy,
    fontsize=11.5,
)
ax.text(
    1.55,
    0.70,
    r"(KKT residual $R_k = 2\epsilon > \epsilon$)",
    color=slate,
    fontsize=8.8,
)
ax.text(
    5.92,
    0.34,
    r"$f'(x) = 2\epsilon$",
    color=navy,
    fontsize=11.0,
)

# Horizontal span arrow for the constant-gradient segment
ax.annotate(
    "",
    xy=(0.0, 0.13),
    xytext=(left, 0.13),
    arrowprops=dict(arrowstyle="<->", color=navy, lw=1.0, shrinkA=1, shrinkB=1),
)
ax.text(
    left / 2.0,
    0.175,
    r"$x_\star - 2\epsilon = \Delta/(2\epsilon) - \epsilon$",
    ha="center",
    va="bottom",
    fontsize=10.0,
    color=slate,
)
ax.text(
    left / 2.0,
    0.045,
    r"center drift per step $\leq 2\alpha\gamma\epsilon$",
    ha="center",
    va="bottom",
    fontsize=8.8,
    color=gray,
)

ax.set_xlim(-0.45, 7.1)
ax.set_ylim(-0.08, 1.24)
ax.set_xticks([0.0, xs])
ax.set_xticklabels([r"$0$", r"$x_\star$"])
ax.set_yticks([0.0, delta])
ax.set_yticklabels([r"$0$", r"$\Delta$"])
ax.set_xlabel(r"$x$", loc="right", labelpad=2)
ax.set_ylabel(r"$f(x)$", rotation=0, labelpad=14, va="center")
ax.spines[["top", "right"]].set_visible(False)
ax.spines["left"].set_color(slate)
ax.spines["bottom"].set_color(slate)
ax.tick_params(colors=slate, width=0.8)

# Enlarged quadratic region inset (placed high enough to clear f'(x)=2*eps cleanly)
ins = inset_axes(
    ax,
    width="37%",
    height="41%",
    loc="upper right",
    bbox_to_anchor=(0.0, 0.04, 1.0, 0.96),
    bbox_transform=ax.transAxes,
    borderpad=0.8,
)
xx = np.linspace(xs - 0.5, xs + 0.5, 500)
ins.plot(xx, f(xx), color=navy, lw=1.6, zorder=2)
mid = np.linspace(left, right, 200)
ins.plot(mid, f(mid), color=orange, lw=2.2, zorder=3)
ins.axvspan(left, right, color=orange, alpha=0.09, zorder=0)
ins.plot([xs], [0.0], "o", color=orange, ms=3.5, zorder=4)
ins.set_xticks([left, xs, right])
ins.set_xticklabels(
    [r"$x_\star\!-\!2\epsilon$", r"$x_\star$", r"$x_\star\!+\!2\epsilon$"],
    fontsize=8.2,
)
ins.set_yticks([0.0, 2.0 * eps ** 2])
ins.set_yticklabels([r"$0$", r"$2\epsilon^2$"], fontsize=8.2)
ins.set_ylim(-0.008, 0.092)
ins.set_title("Quadratic region (enlarged)", fontsize=9.0, color=slate, pad=4)
ins.spines[["top", "right"]].set_visible(False)
ins.spines["left"].set_color(slate)
ins.spines["bottom"].set_color(slate)
ins.tick_params(colors=slate, width=0.7, pad=2)

fig.subplots_adjust(left=0.10, right=0.98, bottom=0.15, top=0.96)
fig.savefig(out / "plateau_instance.pdf", bbox_inches="tight", pad_inches=0.04)
fig.savefig(out / "plateau_instance.png", dpi=220, bbox_inches="tight", pad_inches=0.04)
plt.close(fig)
print("Saved plateau_instance.pdf and plateau_instance.png")
