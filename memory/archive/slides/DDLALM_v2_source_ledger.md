# DDLALM_v2 Slide Source Ledger

## Candidate Main Deck

| PDF pages | Content | Primary source |
| --- | --- | --- |
| 4--6 | Problem, split-KKT residual, headline result | Local proof Sections 1--2 and Theorem `thm:main` |
| 8 | Reduced-dual formulation and exact certificate | Local proof Lemma `lem:geometry` |
| 10--11 | Four-block algorithm, update order, schedules, oracle cost | Local proof Algorithm 1 and Eqs. `alg:yq`--`alg:mu`, `eq:r-schedule`, `eq:center-schedule` |
| 13--14 | Assumptions, complete parameter domain, tail-best theorem | Local proof Assumptions `ass:h`--`ass:lower`, Eqs. `eq:ellrho`, `eq:rx-cond`--`eq:beta-cond`, Theorem `thm:main` |
| 16--17 | Two-page Proof Sketch with four core modules | Local proof Lemmas `lem:geometry` through `lem:residual-reconstruction` |
| 18--19 | Scope and references | Local proof Sections 11--12 and cited sources |

## Complete-Proof Appendix

| PDF pages | Result | Primary source |
| --- | --- | --- |
| 22--24 | C1: calculus, joint smoothness, exact maximum | Local proof Lemmas `lem:geometry`, `lem:smoothD` |
| 25 | C2: no-projection boundedness | Local proof Lemma `lem:bounded` |
| 26--27 | C3: three value functions and Lyapunov | Local proof Eqs. `eq:surrogate`--`eq:lambda-plus` |
| 28--29 | C4: frozen-center transfer, parameter map, absorption | Local proof Lemma `lem:frozen`; Li et al. (2026), Condition 3.2, Eq. (4.18), Lemmas 4.4--4.5 |
| 30--31 | C5: moving-center transport and perturbation-scale drift | Local proof Lemmas `lem:mu-transport`, `lem:r-drift` |
| 32--34 | C6: one-step inequality, lower bound, finite budget | Local proof Lemmas `lem:master-one`, `lem:lowerV`, Proposition `prop:budget` |
| 35--36 | C7: primal target error and actual dual increment | Local proof Lemma `lem:dlambda` |
| 37--39 | C8: exact certificate, residual reconstruction, common tail index | Local proof Lemma `lem:residual-reconstruction`, Theorem `thm:main` |
| 40--41 | Main Theorem statement and complete proof | Local proof Theorem `thm:main` |

## Independent Proof Gate

A single `gpt-5.6-terra/max` review checked only the load-bearing chain C4--C8 and the Main Theorem. It confirmed the mathematical chain and identified one missing slide-level parameter-domain condition. The deck now explicitly requires `k_0 >= 1`, `c_r > 0`, `0 < theta_mu <= 1`, `theta_z > 0`, and the uniform three-part beta cap.

## External Source

J. Li, M. Nagarajan, S. Pan, and N. Zhang, "Smoothing Meets Perturbation: Unified and Tight Analysis for Nonconvex--Concave Minimax Optimization," arXiv:2602.14185v2, 2026.

