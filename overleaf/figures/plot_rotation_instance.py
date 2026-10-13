import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Parameters from Theorem 4.2 / Appendix A.
rho = s = tau = gamma = eta = 1.0
Delta = 1.0
alpha = beta = 0.5
epsilon = 0.002

# Part III (D1)--(D2).
chi = eta / gamma
sigma = rho + s
Kappa = max(1.0, 4.0 * tau, 4.0 * gamma * tau)
C_chi = 1.0 + 4.0 / chi
A_chi = 1.0 / chi + 1.25
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

# Appendix A, equations (rot-basic)--(rot-shift).
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
kappa = rho * b ** 2 + a
zeta = 1.0 - nu / 2.0 + 1j * math.sqrt(nu - nu ** 2 / 4.0)
nu_complex = zeta - 1.0
Gamma = tau * b * zeta * (nu_complex + beta) / (nu_complex * (nu_complex + V))
X = 1.0 / (3.0 * max(1.0, abs(Gamma)))
Lambda = Gamma * X
Z = alpha * zeta / (nu_complex + alpha) * X
M = beta * zeta / (nu_complex + beta) * Lambda
vartheta = (1.0 - V) * xi
r_x = -((W - 1.0) * nu_complex / (nu_complex + alpha) + xi * zeta / (nu_complex + V)) / (W + xi) * X
omega_x = xi * ((1.0 - alpha) * r_x + (V - alpha) * zeta / (nu_complex + V) * X)
v_x = -D * r_x + omega_x
r_lambda = (chi * (X - Z) + eta * a * r_x - v_x) / (eta * b)
r_z = X - Z + r_x
r_mu = Lambda - M + r_lambda
x_c = -(X + r_x)
lambda_c = -(Lambda + r_lambda)

# The radial smoothing function in Example ex:rotation.
R_star = 1.25 * X

def psi_prime(r):
    if r <= R_star:
        return -kappa * r
    if r <= 3.0 * R_star:
        return kappa * (r - 2.0 * R_star)
    return kappa * R_star


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

# Direct SPLALM recursion from Definition 3.1.
angle = float(np.angle(zeta))
K = int(math.ceil(2.0 * 2.0 * math.pi / angle))
x = lam = z = mu = 0.0j
xs = [x]
residuals = []
ratios = []
for _ in range(K):
    # x-update uses y(x,lambda) and q=lambda+rho(A-y).
    y = prox_h_over_rho(A(x) + lam / rho)
    q = lam + rho * (A(x) - y)
    grad_x_D = f_grad(x) + b * q
    grad_x_P = grad_x_D + (x - z) / gamma
    x_next = x - eta * grad_x_P

    # lambda-update is evaluated at x^{k+1}, lambda^k.
    y_next = prox_h_over_rho(A(x_next) + lam / rho)
    q_next = lam + rho * (A(x_next) - y_next)
    grad_lambda_P = (A(x_next) - y_next) - (lam - mu) / s
    lam_next = lam + tau * grad_lambda_P

    z_next = z + alpha * (x_next - z)
    mu_next = mu + beta * (lam_next - mu)

    # KKT residual at (x^{k+1}, y^{k+1}, q^k), as in the prompt.
    stationarity = abs(f_grad(x_next) + b * q_next)
    feasibility = abs(A(x_next) - y_next)
    Rk = max(stationarity, feasibility)
    residuals.append(Rk)
    ratios.append(Rk / epsilon)
    xs.append(x_next)
    x, lam, z, mu = x_next, lam_next, z_next, mu_next

# Required validity checks; fail without producing a misleading figure.
radii = np.array([abs(xx - x_c) / X for xx in xs])
if radii.min() < 0.75 or radii.max() > 1.25:
    raise RuntimeError("SPLALM trajectory left the prescribed annulus")
if min(ratios) <= 1.0:
    raise RuntimeError("KKT residual reached epsilon")

# Plot.
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "mathtext.fontset": "cm",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(5.1, 2.3), gridspec_kw={"width_ratios": [1.0, 1.08]})
blue = "#1f3b73"
grey = "0.65"
light = "0.92"

# (a) primal plane.
center = np.array([x_c.real, x_c.imag])
theta = np.linspace(0.0, 2.0 * math.pi, 500)
for radius, alpha_fill in [(1.25 * X, 1.0), (0.75 * X, 1.0)]:
    ax0.fill(center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta), color=light, zorder=0)
ax0.plot(center[0] + X * np.cos(theta), center[1] + X * np.sin(theta), "--", color=grey, lw=0.6, zorder=1)
xy = np.array([[xx.real, xx.imag] for xx in xs])
ax0.plot(xy[:, 0], xy[:, 1], color=blue, lw=0.7, zorder=2)
step = max(1, len(xs) // 24)
ax0.plot(xy[::step, 0], xy[::step, 1], ".", color=blue, ms=1.8, zorder=3)
ax0.plot(center[0], center[1], "x", color="black", ms=3.5, mew=0.8, zorder=4)
ax0.annotate(r"$x_c$", center + np.array([0.03 * X, 0.03 * X]), fontsize=8)
ax0.plot(0.0, 0.0, "o", color="black", ms=1.8, zorder=4)
ax0.annotate(r"$x^0=0$", (0.0, 0.0), xytext=(3, 3), textcoords="offset points", fontsize=8)
# Radial labels outside the annulus.
ang = math.radians(35.0)
for rr, label in [(0.75 * X, r"$\frac{3}{4}X"), (1.25 * X, r"$\frac{5}{4}X")]:
    p = center + rr * np.array([math.cos(ang), math.sin(ang)])
    ax0.annotate(label, p, xytext=(3, 1), textcoords="offset points", color="0.25", fontsize=8)
margin = max(0.18 * X, 0.08 * max(1.0, abs(center).max()))
lo = np.minimum(center - 1.25 * X, np.array([0.0, 0.0])) - margin
hi = np.maximum(center + 1.25 * X, np.array([0.0, 0.0])) + margin
ax0.set_xlim(lo[0], hi[0]); ax0.set_ylim(lo[1], hi[1])
ax0.set_aspect("equal", adjustable="box")
ax0.set_xticks([]); ax0.set_yticks([])
for spine in ax0.spines.values(): spine.set_linewidth(0.5)
ax0.text(0.02, 0.96, r"(a)", transform=ax0.transAxes, va="top")

# (b) residual.
ks = np.arange(K)
ax1.plot(ks, ratios, color=blue, lw=0.7)
ax1.axhline(1.0, color="black", lw=0.6)
ax1.axhline(7.0 / 6.0, color=grey, lw=0.6, ls=(0, (2, 2)))
ax1.annotate(r"$\epsilon$", (K * 0.98, 1.0), xytext=(-2, 2), textcoords="offset points", ha="right", fontsize=8)
ax1.annotate(r"$\frac{7}{6}\epsilon$", (K * 0.98, 7.0 / 6.0), xytext=(-2, 2), textcoords="offset points", ha="right", fontsize=8, color="0.25")
ax1.set_xlabel(r"$k$", labelpad=1)
ax1.set_ylabel(r"$R_k/\epsilon$", labelpad=1)
ax1.set_xlim(0, K - 1)
ax1.set_ylim(0.0, max(1.35, float(max(ratios)) * 1.05))
ax1.set_xticks([0, K // 2, K - 1])
ax1.tick_params(axis="both", which="major", length=2.5, width=0.5, pad=2)
for spine in ax1.spines.values(): spine.set_linewidth(0.5)
ax1.text(0.02, 0.96, r"(b)", transform=ax1.transAxes, va="top")

fig.subplots_adjust(left=0.04, right=0.99, bottom=0.18, top=0.98, wspace=0.28)
out = Path(__file__).with_name("rotation_instance.pdf")
fig.savefig(out, bbox_inches="tight", pad_inches=0.02)
plt.close(fig)

print("c1 = {:.12g}".format(c1))
print("c2 = {:.12g}".format(c2))
print("alpha_epsilon = {:.12g}".format(alpha_epsilon))
print("K = {}".format(K))
print("arg(zeta) = {:.12g}".format(angle))
print("min_radius_over_X = {:.12g}".format(radii.min()))
print("max_radius_over_X = {:.12g}".format(radii.max()))
print("min_residual_over_epsilon = {:.12g}".format(min(ratios)))
print("output = {}".format(out))
