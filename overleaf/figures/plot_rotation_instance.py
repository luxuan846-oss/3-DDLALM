import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Parameters from Theorem 3.2 / Appendix A.2 (Example ex:rotation).
rho = s = tau = gamma = eta = 1.0
Delta = 1.0
alpha = beta = 0.5
epsilon = 0.002

# Thresholds c1, c2, alpha_epsilon.
chi = eta / gamma
Kappa = max(1.0, 4.0 * tau, 4.0 * gamma * tau)
C_chi = 1.0 + 4.0 / chi
B_chi = 1.0 / chi + 2.5
c1 = min(
    1.0 / (32.0 * math.sqrt(tau / (eta * C_chi))),
    1.0 / (64.0 * B_chi),
    1.0 / (16.0 * (3.0 + tau ** -1)),
)
c2 = min(
    1.0 / 64.0,
    1.0 / (32.0 * math.sqrt(Kappa)),
    Delta / 12.0,
    math.sqrt(Delta) / 2.0,
    math.sqrt(Delta / (64.0 * gamma)),
)
alpha_epsilon = 1024.0 * Kappa * epsilon ** 2
assert epsilon < c2, (epsilon, c2)
assert epsilon * (rho + s) <= c1, (epsilon * (rho + s), c1)
assert alpha > alpha_epsilon, (alpha, alpha_epsilon)
assert beta > 0.0

# Appendix A.2.1 parameters.
d_tau = tau / s
U = alpha + chi * (1.0 - alpha)
V = beta + d_tau * (1.0 - beta)
b_epsilon = 8.0 * epsilon
nu = eta * tau * b_epsilon ** 2 * alpha * beta / (U * V)
E = alpha ** 2 + (1.0 - alpha) * nu
H = V ** 2 + (1.0 - V) * nu
Ypsilon = beta * V + (1.0 - V) * nu
W = 1.0 + chi * alpha * (1.0 - alpha) / E
D = alpha * W
b = math.sqrt(nu * W * H / (eta * tau * Ypsilon))
xi = eta * tau * b ** 2 * (V - beta) / H
a = nu * (W - 1.0) / (eta * alpha) + xi / eta
c_kappa = rho * b ** 2 + a
zeta = 1.0 - nu / 2.0 + 1j * math.sqrt(nu - nu ** 2 / 4.0)
nu_complex = zeta - 1.0
Gamma = tau * b * zeta * (nu_complex + beta) / (nu_complex * (nu_complex + V))
X = 1.0 / (3.0 * max(1.0, abs(Gamma)))
Lambda = Gamma * X
Z = alpha * zeta / (nu_complex + alpha) * X
M = beta * zeta / (nu_complex + beta) * Lambda
r_x = -(
    (W - 1.0) * nu_complex / (nu_complex + alpha) + xi * zeta / (nu_complex + V)
) / (W + xi) * X
omega_x = xi * ((1.0 - alpha) * r_x + (V - alpha) * zeta / (nu_complex + V) * X)
v_x = -D * r_x + omega_x
r_lambda = (chi * (X - Z) + eta * a * r_x - v_x) / (eta * b)
x_c = -(X + r_x)
lambda_c = -(Lambda + r_lambda)

# Radial smoothing function in Example ex:rotation.
R_star = 1.25 * X


def psi_prime(r):
    if r <= R_star:
        return -c_kappa * r
    if r <= 3.0 * R_star:
        return c_kappa * (r - 2.0 * R_star)
    return c_kappa * R_star


def f_grad(x):
    u = x - x_c
    r = abs(u)
    radial = 0.0j if r == 0.0 else psi_prime(r) * u / r
    return radial - b * lambda_c


def A(x):
    return b * (x - x_c)


def prox_h_over_rho(v):
    nv = abs(v)
    if nv <= 1.0 / rho:
        return 0.0j
    return (1.0 - 1.0 / (rho * nv)) * v


# Direct LRALM recursion.
angle = float(np.angle(zeta))
K_rev = int(math.ceil(2.0 * math.pi / angle))
K = 2 * K_rev
x = lam = z = mu = 0.0j
xs = [x]
ratios = []
for _ in range(K):
    y = prox_h_over_rho(A(x) + lam / rho)
    q = lam + rho * (A(x) - y)
    grad_x_D = f_grad(x) + b * q
    grad_x_P = grad_x_D + (x - z) / gamma
    x_next = x - eta * grad_x_P

    y_next = prox_h_over_rho(A(x_next) + lam / rho)
    q_next = lam + rho * (A(x_next) - y_next)
    grad_lambda_P = (A(x_next) - y_next) - (lam - mu) / s
    lam_next = lam + tau * grad_lambda_P

    z_next = z + alpha * (x_next - z)
    mu_next = mu + beta * (lam_next - mu)

    stationarity = abs(f_grad(x_next) + b * q_next)
    feasibility = abs(A(x_next) - y_next)
    Rk = max(stationarity, feasibility)
    ratios.append(Rk / epsilon)
    xs.append(x_next)
    x, lam, z, mu = x_next, lam_next, z_next, mu_next

radii = np.array([abs(xx - x_c) / X for xx in xs])
if radii.min() < 0.75 or radii.max() > 1.25:
    raise RuntimeError("LRALM trajectory left the prescribed annulus")
if min(ratios) <= 1.0:
    raise RuntimeError("KKT residual reached epsilon")

# Unified publication style matching Figure 1 & plateau_instance.
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9.5,
    "mathtext.fontset": "cm",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

navy = "#204A9E"
slate = "#414E60"
red = "#B23832"
teal = "#14765C"
annulus_fill = "#E7EDF6"
border_gray = "#94A3B8"
muted = "#646E7A"

fig, (ax0, ax1) = plt.subplots(
    1, 2, figsize=(6.6, 2.85), gridspec_kw={"width_ratios": [1.0, 1.28]}
)

# ==================== (a) Primal plane ====================
center = np.array([x_c.real, x_c.imag])
theta = np.linspace(0.0, 2.0 * math.pi, 600)

# Proper annulus shading: outer disk filled, inner disk punched out in white.
ax0.fill(
    center[0] + 1.25 * X * np.cos(theta),
    center[1] + 1.25 * X * np.sin(theta),
    color=annulus_fill,
    zorder=0,
)
ax0.fill(
    center[0] + 0.75 * X * np.cos(theta),
    center[1] + 0.75 * X * np.sin(theta),
    color="white",
    zorder=1,
)
# Outer & inner annulus boundaries + reference circle of radius X.
for rr, ls, col, lw in [
    (1.25 * X, "-", border_gray, 0.8),
    (0.75 * X, "-", border_gray, 0.8),
    (1.00 * X, ":", muted, 0.7),
]:
    ax0.plot(
        center[0] + rr * np.cos(theta),
        center[1] + rr * np.sin(theta),
        ls,
        color=col,
        lw=lw,
        zorder=2,
    )

# Plot trajectory (clean continuous orbit + evenly spaced markers over 1st revolution).
xy = np.array([[xx.real, xx.imag] for xx in xs[: K_rev + 1]])
ax0.plot(xy[:, 0], xy[:, 1], color=navy, lw=1.35, zorder=3)
idx_dots = np.linspace(0, K_rev, 13, endpoint=False, dtype=int)[1:]
ax0.plot(xy[idx_dots, 0], xy[idx_dots, 1], "o", color=navy, ms=2.6, zorder=4)

# Directional arrowhead along the orbit (counterclockwise near ~55 deg).
i_arr = K_rev // 7
ax0.annotate(
    "",
    xy=(xy[i_arr + 4, 0], xy[i_arr + 4, 1]),
    xytext=(xy[i_arr, 0], xy[i_arr, 1]),
    arrowprops=dict(arrowstyle="-|>", color=navy, lw=1.3, mutation_scale=11),
    zorder=5,
)

# Center x_c and initial point x^0 = 0.
ax0.plot(center[0], center[1], "x", color=slate, ms=4.5, mew=1.1, zorder=5)
ax0.annotate(
    r"$x_c$",
    xy=(center[0], center[1]),
    xytext=(4, -10),
    textcoords="offset points",
    fontsize=9.2,
    color=slate,
)
ax0.plot(0.0, 0.0, "o", color=red, ms=4.2, zorder=6)
ax0.annotate(
    r"$x^0=0$",
    xy=(0.0, 0.0),
    xytext=(20, 8),
    textcoords="offset points",
    fontsize=8.8,
    color=red,
    arrowprops=dict(arrowstyle="-", color=red, lw=0.65, shrinkA=1, shrinkB=4),
)

# Clean radial guide arrows & properly closed LaTeX labels for 3/4 X and 5/4 X.
ang_in = math.radians(142.0)
p_in = center + 0.75 * X * np.array([math.cos(ang_in), math.sin(ang_in)])
ax0.annotate(
    "",
    xy=p_in,
    xytext=center,
    arrowprops=dict(arrowstyle="->", color=muted, lw=0.75, shrinkA=2, shrinkB=0),
    zorder=4,
)
p_in_mid = center + 0.42 * X * np.array([math.cos(ang_in), math.sin(ang_in)])
ax0.annotate(
    r"$\frac{3}{4}X$",
    xy=p_in_mid,
    xytext=(2, 8),
    textcoords="offset points",
    color=slate,
    fontsize=8.5,
)

ang_out = math.radians(-128.0)
p_out = center + 1.25 * X * np.array([math.cos(ang_out), math.sin(ang_out)])
ax0.annotate(
    "",
    xy=p_out,
    xytext=center,
    arrowprops=dict(arrowstyle="->", color=muted, lw=0.75, shrinkA=2, shrinkB=0),
    zorder=4,
)
ax0.annotate(
    r"$\frac{5}{4}X$",
    xy=p_out,
    xytext=(-18, -11),
    textcoords="offset points",
    color=slate,
    fontsize=8.5,
)

margin_x_lo = 0.34 * X
margin_x_hi = 0.94 * X
margin_y = 0.34 * X
ax0.set_xlim(center[0] - 1.25 * X - margin_x_lo, max(center[0] + 1.25 * X, 0.0) + margin_x_hi)
ax0.set_ylim(center[1] - 1.25 * X - margin_y, center[1] + 1.25 * X + margin_y)
ax0.set_aspect("equal", adjustable="box")
ax0.set_xticks([])
ax0.set_yticks([])
for spine in ax0.spines.values():
    spine.set_linewidth(0.7)
    spine.set_color(border_gray)
ax0.set_title(r"(a) Primal trajectory in $\mathbb{C}$", fontsize=9.8, color=slate, pad=7)

# ==================== (b) Scaled KKT residual ====================
ks = np.arange(K)
ax1.plot(ks, ratios, color=navy, lw=1.45, label=r"$R_k/\epsilon$", zorder=3)
ax1.axhline(1.0, color=red, lw=0.95, ls="-", zorder=2)
ax1.axhline(7.0 / 6.0, color=teal, lw=0.95, ls="--", zorder=2)

# Non-overlapping labels cleanly placed on opposite sides of the two reference lines
ax1.text(
    K * 0.98,
    7.0 / 6.0 + 0.12,
    r"lower bound $7/6$",
    ha="right",
    va="bottom",
    fontsize=8.4,
    color=teal,
)
ax1.text(
    K * 0.98,
    1.0 - 0.13,
    r"target $R_k/\epsilon = 1$",
    ha="right",
    va="top",
    fontsize=8.4,
    color=red,
)
ax1.text(
    K * 0.03,
    float(ratios[0]) + 0.12,
    r"actual $R_k/\epsilon$",
    ha="left",
    va="bottom",
    fontsize=8.6,
    color=navy,
)

ax1.set_xlabel(r"iteration $k$", labelpad=3, color=slate)
ax1.set_ylabel(r"$R_k/\epsilon$", labelpad=4, color=slate)
ax1.set_xlim(0, K - 1)
ax1.set_ylim(0.0, float(max(ratios)) * 1.26)
ax1.set_xticks([0, K_rev, K - 1])
ax1.set_yticks([0, 1, 2, 3])
ax1.spines[["top", "right"]].set_visible(False)
ax1.spines["left"].set_color(slate)
ax1.spines["bottom"].set_color(slate)
ax1.tick_params(axis="both", which="major", length=3.0, width=0.75, pad=3, colors=slate)
ax1.set_title(r"(b) Scaled KKT residual", fontsize=9.8, color=slate, pad=7)

fig.subplots_adjust(left=0.04, right=0.98, bottom=0.17, top=0.88, wspace=0.26)
out_pdf = Path(__file__).with_name("rotation_instance.pdf")
out_png = Path(__file__).with_name("rotation_instance.png")
fig.savefig(out_pdf, bbox_inches="tight", pad_inches=0.04)
fig.savefig(out_png, dpi=220, bbox_inches="tight", pad_inches=0.04)
plt.close(fig)

print(f"K_rev={K_rev}, K={K}, min_r/X={radii.min():.4f}, max_r/X={radii.max():.4f}, min_Rk/eps={min(ratios):.4f}")
print(f"Saved {out_pdf} and {out_png}")
