# Proof audit — Appendix A — 2026-10-13

**PASS after one explanatory addition.** Scope is the rotating-instance appendix
and its direct statement/trajectory interfaces, not the entire manuscript.
The executor and an independent reviewer derived the mathematical identities
analytically. No numerical verification was performed.

Full derivations: [Chinese audit record](notes/progress/appendix-a-audit-20261013.md).
Proof obligations: [ledger](PROOF_SKELETON.md).

## Finding A-DENSITY-1

- Original location: `appendix/LowerBoundRotation.tex:329`.
- Status: insufficient explanation of a correct claim; MINOR, UNCLEAR/COSMETIC.
- Category: UNPROVEN_SUBCLAIM; strategy: ADD_DERIVATION.
- Before: algebraic exceptional sets were declared to have dense complement
  without exhibiting a nonzero discriminant or checking admissible perturbations.
- After: positive evaluations exclude eigenvector denominator failures;
  the discriminant has nonzero limit when U differs from V; beta and epsilon
  perturbations avoid the exceptional equalities. Boundary points are approached
  inside the original admissible domain.
- Closure: executor and independent reviewer both verified the new paragraph.
- No counterexample; no hypothesis, constant, construction, or conclusion changed.

## Verified results

Parameter inequalities; smoothness and initial objective gap; characteristic
factorization; synchronized zero initialization; stable invariant subspace,
including repeated roots; uniform transient bounds; both proximal conditions;
the rotating branch's KKT residual bound R_k >= 7 epsilon/6.

The proof uses pointwise spectral decay and separately proves uniform transient
bounds. It does not assume a uniform spectral gap as beta tends to zero.
No circular dependency was found.

## Review provenance and build

The requested external reviewer model gpt-5.5 was unavailable (403 model error).
Independent analytic review was completed by the session agent
`/root/appendix_a_analytic_review`, including review of the added density proof.
An earlier interrupted review provided a partial assessment only and is not
counted as a completed independent review.

`latexmk` completed the manuscript build: 38 pages, no undefined references or
LaTeX errors in the final log. Unrelated existing layout/package warnings remain.
The detailed record lists the build command and output directory.

The prior, unrelated 2026-08-04 audit in PROOF_AUDIT.json is retained in the new
JSON artifact's `prior_audits` field for history; it was not used as evidence.
