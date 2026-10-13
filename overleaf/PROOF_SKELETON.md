# Appendix A proof obligations — 2026-10-13

Scope: `appendix/LowerBoundRotation.tex`, with the statements, instance, matrix,
and trajectory in `sections/LowerBoundProof.tex`. This is not a whole-paper audit.
Verification is analytic only; no numerical experiments or parameter scans.

## Hypotheses and quantifiers

Fix gamma, eta, tau, Delta with 0 < eta <= gamma and tau, Delta > 0.
For every rho > 0, s >= tau, epsilon in (0,c2), alpha in
(1024 max{1,4 tau,4 gamma tau} epsilon^2,1], and beta in (0,1], assume
epsilon(rho+s) <= c1. The appendix constructs one instance for each such tuple.
Every transient inequality holds for all integer k >= 0.
The constants c1 and c2 depend only on the fixed quantities stated in the theorem.

The ambient parameter restrictions come from `def:splalm`,
`thm:lower-bound`, and the opening of the lower-bound proof; `lem:rot-estimates`
adds the large-alpha, positive-beta branch restrictions.

## Dependency graph

Parameter definitions and thresholds
-> parameter bounds
-> spectral identities and stable invariant subspace
-> transient bounds
-> problem-class membership and trajectory induction
-> rotating-branch KKT residual lower bound.

The membership proof appears earlier than the transient proof but uses it only
after the latter has been established algebraically. Neither the parameter,
spectral, nor transient proof assumes problem-class membership. No cycle.

## Types

- chi, d_tau, alpha, beta, U, D, V: positive real scalars, at most one.
- nu: positive real scalar, less than alpha^2/64.
- W >= 1, xi >= 0, vartheta = (1-V)xi >= 0: real scalars.
- b > 0, a >= 0, kappa > 0: real scalars; a may equal zero at endpoints.
- zeta: nonreal complex scalar of modulus one.
- X > 0: real amplitude; Lambda: complex amplitude.
- v, r, w_c: four complex coordinates, each representing a vector in R^2.
- T: real 4-by-4 coefficient matrix acting on C^4, equivalently T tensor I_2.
- Q_f: real monic quadratic polynomial in the eigenvalue variable.
- p_k, ell_k, m_k, e_k, q_k: complex coordinates or linear combinations.
- G_j: nonnegative real convolution kernel.

## Claim ledger

| ID | Obligation | Analytic justification |
|---|---|---|
| A01 | Definitions have nonzero denominators | alpha,beta,V,nu>0; zeta nonreal; Upsilon>0 |
| A02 | nu/alpha^2 < 1/64 | alpha threshold and U>=chi, V>=beta |
| A03 | 64U/65 <= D <= U <= 1 | Substitute W; use A02 |
| A04 | 7 epsilon <= b <= 8 epsilon | Product formula for b^2; small-feedback bound |
| A05 | xi C_tr <= 1/16 | First term of c1; epsilon s <= c1 |
| A06 | Curvature and amplitude bounds | Real-part identity; Cauchy--Schwarz; D>=chi/2 |
| A07 | Characteristic polynomial and T v=zeta v | Eliminate center coordinates; compare coefficients |
| A08 | Synchronized shift lies in ker Q_f(T) | Two-by-two system; nonzero determinant; continuity |
| A09 | Nondegenerate parameters are dense | Positive Q_f(1); nonzero rational discriminant; admissible perturbations |
| A10 | Every fast eigenvalue has modulus <1 | Product lower bound outside the unit circle |
| A11 | Uniform primal transient and absolute summability | Convolution formula; finite-prefix inequalities |
| A12 | Dual transient | Difference recursion; weighted-average tail sum; A10 and A11 |
| A13 | Global smoothness and bounded gradient | Piecewise radial Hessian; matching first derivatives |
| A14 | Initial objective gap <= Delta | Curvature-amplitude estimate and two terms of c2 |
| A15 | Actual SPLALM follows the constructed sequence | Induction verifies both proximal conditions in order |
| A16 | R_k >= 7 epsilon/6 | Two cases for max{X,abs(Lambda)}; A04, A06, A11, A12 |

## Boundary and limit obligations

The annihilator identity extends to alpha=1, beta=1, d_tau=1, V=alpha,
and repeated roots. beta=0 is outside this branch and has its own instance.
No uniform spectral gap as beta tends to zero is asserted or needed.
Pointwise decay for each admissible matrix is used for q_k -> 0;
uniform-in-k transient bounds follow separately from finite-prefix estimates.
The infinite sum is justified by monotonicity of bounded nonnegative partial sums.

## Scope delta

One explanatory derivation was added for density. No hypothesis, construction,
constant, or theorem conclusion was changed. Independent review status is
recorded in `PROOF_AUDIT.md`.
