# Proof Skeleton

## Main Claim

For the implicit reduced-dual proximal iteration in `PROOF_PACKAGE.md`, choose

$$
s_k=c_s(k+1)^a,
\qquad
\eta_k=\frac{\theta_x}{\rho+s_k},
\qquad
\tau_k=\frac{\theta_\mu s_k}{k+2}.
$$

Under Assumptions 1--5 and the explicit stepsize conditions in Lemma 7, the
choice $a=1/3$ produces one $\epsilon$-split-KKT point in
$O(\epsilon^{-3})$ iterations.

## Dependency DAG

1. Assumptions 1--5 imply bounded subgradients and global smoothness of the
   primal maps.
2. Lemma 0 uses convexity of $h$ and $\rho,s>0$ to construct the unique saddle
   pair and prove the minimax identity.
3. Lemma 1 uses convexity of $h$ and $\rho,s>0$ to derive the implicit update
   and fixed-target contraction.
4. Lemma 2 uses Lemma 1, Lipschitz continuity of $h$, and
   $0<\tau_k/s_k\le1$ to prove bounded multipliers and exact residual bounds.
5. Lemma 3 uses convexity of $h$, nonexpansiveness of proximal maps, the bound
   on $J_A$, and Lemma 2 for the $s$-sensitivity constant.
6. Lemma 4 uses Lemmas 1--3 to prove the scaled moving-target recursion.
7. Lemma 5 uses Lemmas 0, 2, and 3, the Moreau-envelope gradient formula, and
   smoothness of $f,A$ to prove inexact primal descent.
8. Lemma 6 uses Lemma 2 and the direct reduced representation from Lemma 0 to
   prove summable parameter drift and a uniform lower bound.
9. Lemma 7 uses Lemmas 4--6 and explicit choices of $c_T,\theta_x$ to prove a
   joint Lyapunov inequality and weighted finite length.
10. Lemma 8 uses Lemmas 1--2 and Lemma 7 to select one common tail iterate and
   bound all split-KKT residuals.
11. Theorem 1 uses Lemma 8 and balances $a$ with $(1-a)/2$.

The graph is acyclic.

## Assumption Ledger

| Assumption | Type | Used in | Verification status |
|---|---|---|---|
| $h$ is proper, closed, convex, and globally $L_h$-Lipschitz | model | Lemmas 0--3, 5--6, 8 | stated |
| $\rho>0$, $s_k>0$, $\beta\in(0,1)$ | parameter | Lemmas 0--8 | stated |
| $f,A$ are $C^1$ on $\mathbb R^n$ | regularity | Lemmas 3 and 5 | stated |
| $\nabla f,J_A$ are globally Lipschitz and $\|J_A\|\le G_A$ globally | regularity | Lemmas 3, 5, 7--8 | stated |
| $F_{\inf}:=\inf_xF(x)>-\infty$ | lower bound | Lemma 7 | stated |
| initial $y^0$ is consistent with $(x^0,\lambda^0)$ | initialization | algorithm and Lemma 5 at $k=0$ | stated |
| $s_k=c_s(k+1)^a$, $a\in(0,1)$ | schedule | Lemmas 4, 6, 8 | stated |
| $\tau_k=\theta_\mu s_k/(k+2)$, $\theta_\mu\in(0,1]$ | schedule | Lemmas 2, 4, 6 | stated |
| two explicit bounds on $\theta_x$ | stepsize | Lemmas 5 and 7 | stated in Lemma 7 |

## Typed Symbols

| Symbol | Type and meaning |
|---|---|
| $x^k\in\mathbb R^n$ | primal iterate |
| $y^k,\lambda^k,\mu^k,q^k\in\mathbb R^m$ | split variable, reduced-dual multiplier, smoothing center, KKT-aligned subgradient |
| $s_k,\eta_k,\tau_k,\rho,\beta>0$ | scalar algorithm parameters |
| $y_s^\star(x;\mu)\in\mathbb R^m$ | unique minimizer in the exact reduced value |
| $\lambda_s^\star(x;\mu)\in\mathbb R^m$ | unique maximizer of $d_s(x,\cdot;\mu)$ |
| $q_s^\star(x;\mu)\in\partial h(y_s^\star(x;\mu))$ | exact KKT-aligned multiplier |
| $e_k\in\mathbb R^m$ | $\lambda^k-\lambda_{s_k}^\star(x^k;\mu^k)$ |
| $E_k\in\mathbb R_+$ | scaled error $\|e_k\|^2/s_k$ |
| $\psi_s(x;\mu)\in\mathbb R$ | exact reduced value $\max_\lambda d_s(x,\lambda;\mu)$ |
| $p_k,\omega_k\in\mathbb R_+$ | summable parameter-drift sequences |
| $\mathcal V_k\in\mathbb R$ | joint Lyapunov value $\psi_{s_k}+c_TE_k$ |

## Canonical Quantified Statements

1. For every fixed $x,\mu$ and $s>0$, Lemma 0 gives a unique saddle pair and
   equality of the max-min and min-max values.
2. For every fixed $x,\mu,s>0,\lambda$ and $\beta\in(0,1)$, Lemma 1's
   proximal point exists uniquely, has the stated one-prox form, and contracts
   the fixed target by $1-\beta$.
3. For every $k\ge0$, Lemma 2 bounds $\lambda^k,\mu^k,q^k$ by constants that
   depend only on initialization and $L_h$.
4. For every $s>0$, every admissible $x,x',\mu,\mu',s'\ge s$, Lemma 3 gives
   the stated target-sensitivity bounds with constants independent of $k,K$.
5. For every $k\ge0$, Lemma 4 gives the moving-target recursion with constants
   depending only on $\beta,G_A,M$.
6. For every $k\ge0$, Lemma 5 gives primal descent on $\mathbb R^n$.
7. For every $k\ge0$, Lemma 6 gives a one-sided parameter-drift bound whose
   total budget is finite under the polynomial schedule.
8. For every $k\ge0$, Lemma 7 gives the joint descent inequality; its total
   error budget is finite and independent of the terminal horizon $K$.
9. For every integer $K\ge4$, Lemma 8 proves the existence of one
   $\kappa\in\{\lceil K/2\rceil,\ldots,K-1\}$ satisfying all three residual
   bounds with constants independent of $K$. At $a=1/3$, minimizing the
   computable score $\max\{\|g_k\|,\|A(x^k)-y^k\|\}$ over this tail returns an
   iterate with the same rate.
10. For every $\epsilon>0$, Theorem 1 returns an $\epsilon$-split-KKT point by
    horizon

$$
K_\epsilon
=\max\left\{4,
\left\lceil\left(\frac{C}{\epsilon}\right)^3\right\rceil
\right\},
$$

    where $C$ is independent of $\epsilon$. Hence the complexity is
    $O(\epsilon^{-3})$ as $\epsilon\downarrow0$.

## Micro-Claim Inventory

| ID | Goal | Rule | Side conditions |
|---|---|---|---|
| MC-00 | unique saddle pair and minimax identity | direct saddle optimality and strong convexity-concavity | $\rho,s>0$; $h$ proper, closed, convex |
| MC-01 | $d_s(x,\cdot;\mu)$ is $1/s$-strongly concave | infimum of affine functions plus negative quadratic | unique $y$ from $\rho>0$ |
| MC-02 | implicit dual step has one-prox closed form | first-order condition and proximal optimality | $\gamma=\beta s/(1-\beta)$ |
| MC-03 | fixed-target factor is $1-\beta$ | resolvent of a $1/s$-strongly monotone map | $\beta\in(0,1)$ |
| MC-04 | all algorithmic multipliers are bounded | convex-combination induction | bounded subgradients; $0<\tau_k/s_k\le1$ |
| MC-05 | target sensitivity in $x,\mu,s$ | zero perturbation for strongly monotone maps | proximal nonexpansiveness and multiplier bound |
| MC-06 | moving-target recursion contracts $E_k$ | MC-03, MC-05, Young inequality | $s_{k+1}\ge s_k$ |
| MC-07 | $\nabla\psi_s=\nabla f+J_A^\top q_s^\star$ | Moreau-envelope gradient formula and chain rule | global $C^1$ regularity; $h$ proper, closed, convex |
| MC-08 | primal error is at most $G_A\|e_k\|$ | nonexpansiveness of $q(\cdot;x)$ | common $x^k$ |
| MC-09 | primal descent loses only $\theta_xG_A^2E_k$ | descent lemma and Young inequality | first stepsize condition |
| MC-10 | parameter drift is summable | old minimizer as a test point | exact residual $O(1/s_k)$ |
| MC-11 | joint negative coefficients are explicit | choice of $c_T$ and second stepsize condition | $1-Q_\beta>0$ |
| MC-12 | tail average gives one common iterate | finite nonnegative budget | $K\ge4$ |
| MC-13 | feasibility is $O(K^{-a})+O(K^{-(1-a)/2})$ | exact residual plus prox sensitivity | $\rho>0$ |
| MC-14 | $a=1/3$ gives $O(\epsilon^{-3})$ | exponent balance | constants independent of $K,\epsilon$ |

## Counterexample Checklist

1. $h\equiv0$, $A\equiv0$ shows the old explicit dual map expands its
   fixed-target error by $s/\rho$, so it cannot supply the uniform contraction
   used by the present proof.
2. $h\equiv0$ also reduces the implicit update to a scalar linear map with
   contraction factor at most $1-\beta$.
3. Constant $s_k$ leaves the exact feasibility term $C_r/(\rho+s_k)$ bounded
   away from zero, so increasing $s_k$ is necessary for the present argument.
4. The limiting cases $\beta\downarrow0$ and $\beta\uparrow1$ do not violate
   any finite-$\beta$ statement, but the constants are not uniform in
   $\beta$.
5. The proof does not cover indicator-valued $h$ because bounded
   subgradients are used in Lemma 2.

## Uniformity Map

- All $O(\cdot)$ rates are as $K\to\infty$ with
  $f,A,h,\rho,\beta,c_s,\theta_x,\theta_\mu,a,x^0,\lambda^0,\mu^0$ fixed.
- Constants may depend on
  $L_f,L_A,L_h,G_A,M,\rho,\beta,c_s,\theta_x,\theta_\mu,a$ and the initial
  Lyapunov gap.
- Constants do not depend on $K$ or $\epsilon$.
- No claim is uniform as $\beta$ approaches $0$ or $1$, or as $\rho$ approaches
  $0$.

## Acceptance Status

Two independent verifier-style reviews returned PASS. There is no remaining
localization obligation: the stated global smoothness assumptions cover every
descent-lemma and target-sensitivity application. The accepted status is
`accepted_by_review`; the proof has not been machine-checked.
