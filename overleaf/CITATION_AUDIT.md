# Citation Audit Report

**Audit mode**: read-only first pass with local context extraction and primary-source checks for high-impact citations  
**Generated**: 2026-11-21T00:57:03.040397+00:00
**Scope**: `overleaf/sections/*.tex`, `overleaf/appendix/*.tex`, `overleaf/tools/refer.bib`

## Overall result

The manuscript has **131 citation commands** containing **135 key mentions**, **48 cited keys**, and **164 bibliography entries**. The active bibliography therefore contains **116 uncited entries**. `latexmk` completed without undefined citation or reference warnings in the existing build.

The audit remains in progress. Several core claims have been checked against primary papers. I found one material attribution problem in the GDPA comparison row, a mixed-method literature sentence, and metadata normalization issues. I have not yet verified all 48 cited sources, so this report does not claim a paper-wide pass.

## Metadata fixes

### `zhang2022proximal`

The cited entry is the paper *A Proximal Alternating Direction Method of Multiplier for Linearly Constrained Nonconvex Minimization*, whose journal record is SIAM Journal on Optimization, volume 30, issue 3, 2272--2302, **2020**. The key `zhang2022proximal` is inconsistent with the record, and `zhang2020proximal` is an uncited duplicate candidate. Canonicalize the record and update the two citations in `sections/Acceleration.tex:342` and `sections/Acceleration.tex:359`.

### `elbourkhissi2025linearized`

The source is arXiv:2301.08345. Its v1 was submitted in 2023 and v2 was revised in 2025. The cited result reports O(sqrt(rho) epsilon^{-2}) Jacobian evaluations and the paper explicitly discusses a local LICQ condition. Record v2 in the bibliography and use a 2023 key/year convention, or state the 2025 revision date consistently. The current 2025 key is ambiguous.

### `zhang2026matching`

The arXiv metadata lists **Minghao Zhang**, whereas the PDF title page and the author email use **Minhao Zhang**. Resolve this discrepancy against the final canonical record before submission. The cited claims at `sections/Introduction.tex:267` and `sections/Introduction.tex:307` are supported by the paper's Algorithm 1 and game-stationarity result.

## Context checks that should be rewritten or narrowed

1. `sections/Introduction.tex:70--81` groups eight papers under one assertion about an $\epsilon^-1$ parameter schedule. These papers mix deterministic and stochastic ALM, penalty, and ADMM settings. Split the claim by method and state the schedule only where the cited theorem gives it.
2. `sections/Introduction.tex:95--98` should state the stationarity notion and the complexity unit for `lin2020gradient`. Its result should not be read as a generic GS bound without that qualification.
3. `sections/Introduction.tex:104--106` should distinguish Euclidean nonconvex-linear minimax results from the Riemannian result `xu2026rada`. Keep the citation, but narrow the sentence.
4. `sections/Introduction.tex:180` should describe `carmon2020lower` as the smooth unconstrained lower bound inherited by the unconstrained subclass. It does not directly prove the manuscript's composite KKT lower bound.
5. The `GDPA` row at `sections/Introduction.tex:253--255` combines `luSingleLoopGradientDescent2022` and `sun2024dual_descent_alm_admm`. Verify the rate, parameter scale, and stationarity certificate separately for each source.
6. `sections/Preliminaries.tex:177--198` may cite smooth NC-C papers for GS/OS terminology and regularization mechanisms. The composite KKT residual identity remains a result of this manuscript and should not be attributed to those sources.

## Repetition triage

| Citation key | Count | Decision |
|---|---:|---|
| `li2026smoothing` | 32 | Keep the 19 appendix pinpoint citations. In the main text, consolidate repeated background statements around the first rate comparison and the table. |
| `zhang2020smoothed` | 10 | Keep the family labels and the value-function lemma citation. Remove only a repeated general-background citation if the same sentence already names Smoothed GDA. |
| `luSingleLoopGradientDescent2022` | 6 | Keep the origin citation and the comparison-table citation. The repeated Introduction/Preliminaries mentions can be reduced to one background citation. |
| `pan2026optimal` | 5 | Keep the theorem-level rate citation and the table row. The adjacent prose can cite it once for both the rate and the multi-loop attainment claim. |
| `nesterov2018lectures` | 4 | Normal foundational usage. No reduction needed. |

The repetition is therefore **concentrated but not structurally excessive**. Appendix citations that point to an algorithm, condition, theorem, or equation should remain.

## Anthony Man-Cho So lineage

The manuscript already cites two directly relevant So-coauthored works. `zheng2023universal` is correctly used for DS-GDA and dual regularization. `xu2026rada` is correctly used for a nonconvex-linear minimax comparison, provided the text identifies its Riemannian setting.

`li2025nonsmooth` is present in `refer.bib` but is uncited. It is the cleanest addition for the paragraph that introduces GS and OS for nonsmooth minimax problems because it explicitly studies the nonsmooth composite setting and gives an algorithm-independent relation between the two notions. It should support the terminology and comparison only. The manuscript's own KKT residual transfer should remain attributed to the present analysis.

Two optional lineage-adjacent additions are technically relevant but not mandatory. Tian--So (2024) can support a general stationarity/oracle-complexity discussion, and Zhu--Li (arXiv:2607.08954) can support a comparison with local-regularity first-order ALM for composite functional constraints. Neither should be added solely for pedigree.

## Uncited bibliography

The 116 uncited entries are a shared bibliography residue. Do not delete them in this pass. Before submission, compare each duplicate family against a canonical record, then prune only entries that are not used by the final manuscript.

## Source records checked

- [Li--Nagarajan--Pan--Zhang, arXiv:2602.14185](https://arxiv.org/abs/2602.14185)
- [Pan--Zheng--Li, arXiv:2609.14235](https://arxiv.org/abs/2609.14235)
- [Zhang--Xu, arXiv:2609.17973](https://arxiv.org/abs/2609.17973)
- [El Bourkhissi--Necoara, arXiv:2301.08345](https://arxiv.org/abs/2301.08345)
- [Li--Zhu--So, Mathematical Programming / arXiv:2209.10825](https://arxiv.org/abs/2209.10825)
- [Zheng--Zhu--So et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/a961dea42c23c3c0d01b79918701fb6e-Paper-Conference.pdf)
- [Xu--Jiang--Liu--So, MOR 2026](https://doi.org/10.1287/moor.2025.1055)
- [Tian--So, Mathematical Programming 2024](https://doi.org/10.1007/s10107-023-02031-6)
- [Li--Chen--Liu--Lu--Xu, AISTATS 2021](https://proceedings.mlr.press/v130/li21d.html)
- [Sun--Sun, SIAM Journal on Optimization 2024](https://doi.org/10.1137/21M1449099)


## Continued source review

### Material attribution and comparison issues

1. `sections/Introduction.tex:73--76` mixes three different literatures in one sentence. `lu2020hybrid` and `xu2023unified` are minimax GDA methods, not ALM or ADMM methods. `alacaoglu2024complexity` and `shi2025momentum` study stochastic constrained optimization, while the surrounding claim reads as a deterministic complexity statement. Separate the smooth minimax perturbation results from deterministic ALM/penalty methods and from stochastic methods. State each method's stationarity measure and oracle unit.
2. The comparison row `sections/Introduction.tex:253--255` labels both `luSingleLoopGradientDescent2022` and `sun2024dual_descent_alm_admm` as `GDPA`. This attributes Sun and Sun's SDD-ADMM method to Lu's algorithm. Split the row. GDPA uses an increasing penalty sequence with `beta_r = Theta(r^{1/3})`, primal step `alpha_r = Theta(r^{-1/3})`, and dual step `gamma_r = Theta(r^{-1/3})`; its O(epsilon^{-3}) result assumes the paper's regularity conditions. SDD-ADMM has a separate O(epsilon^{-3}) guarantee with penalty `rho = Theta(epsilon^{-1})` under Assumption 3.13 and an almost-feasible initialization. Its baseline bound uses `rho = Theta(epsilon^{-2})` for O(epsilon^{-4}), and its O(epsilon^{-2}) result uses `rho = Theta(1)` under the additional assumptions. The table's `Dual reg. s` column does not directly describe either paper's parameter, so do not put `Theta(epsilon^{-1})` there without defining a valid mapping.
3. The sentence at `sections/Introduction.tex:70--81` currently implies that all cited single-loop methods for the manuscript's problem class obtain O(epsilon^{-3}) only through an epsilon-dependent parameter. The cited papers cover nonlinear inequality constraints, stochastic objective/constraints, nonsmooth composite constraints, and minimax problems. Narrow the subject to related constrained methods and distinguish which rate and parameter schedule each theorem proves.
4. `sections/Introduction.tex:95--98` cites Lin--Jin--Jordan for a two-timescale GDA rate of O(epsilon^{-6}). Theorem 4.9 measures stationarity of a Moreau-envelope value function; Proposition 4.13 gives a conversion to game stationarity with O(epsilon^{-2}) additional deterministic gradients. State the source's stationarity criterion when giving the O(epsilon^{-6}) rate.
5. `sections/Introduction.tex:104--106` groups Euclidean nonconvex-linear minimax papers with the Riemannian RADA paper `xu2026rada`. The RADA paper does prove O(epsilon^{-3}) Riemannian game-stationarity complexity, but its manifold setting and residual should be named.
6. In `sections/Introduction.tex:253--255`, Lu's GDPA requires regularity assumptions. The current table's `CQ-free` column says `--`, which is compatible with a non-CQ-free classification, but the relevant condition should be named in a note if readers cannot infer it from the cited paper.

### Citation repetition

The count separates citation commands from individual keys: 131 `\\cite` commands contain 135 key mentions. Repetition is not uniformly excessive. The appendix uses of `li2026smoothing` point to specific algorithms, assumptions, equations, and theorems. Keep those citations. The clearest redundant cluster is in `sections/Acceleration.tex:342` and `sections/Acceleration.tex:359`: the same three papers are cited twice in consecutive discussion of the same Lyapunov construction. Keep the citation with the first attribution and remove the repeated citation from the next sentence if it adds no distinct comparison. The prose citations to `pan2026optimal` around lines 302 and 305 also repeat the same rate result; one citation can support both clauses.

`zhang2022proximal` occurs twice in that same acceleration paragraph and is a duplicate BibTeX record of `zhang2020proximal`. The body key can be canonicalized after the exact duplicate is confirmed. The key suffix does not alter the rendered publication year, which is 2020.

### Anthony Man-Cho So research line

The current draft already cites two relevant So-coauthored works: `zheng2023universal` for DS-GDA and `xu2026rada` for Riemannian NC-linear minimax. Three further papers have plausible, specific roles:

- `li2025nonsmooth` is already in `refer.bib` but uncited. It directly studies nonsmooth composite NC-NC minimax and defines GS and OS, with quantitative relations between stationarity measures. Its measures use a proximal-linear envelope and do not exactly equal this paper's residuals. Cite it when discussing nonsmooth minimax stationarity, with that distinction explicit.
- Zheng--So--Li, *Doubly Smoothed Optimistic Gradients: A Universal Approach for Smooth Minimax Problems*, arXiv:2506.07397 (2025), is absent from `refer.bib`. It is a relevant follow-up to DS-GDA that adds optimistic extrapolation and reports O(epsilon^{-4}) for NC-C and related one-sided KŁ settings. Cite it in the minimax methods discussion if that follow-up is included; it does not establish the present ALM result.
- Zhu--Li, *Nonconvex Composite Functional Constraints via First-Order Augmented Lagrangian Methods under Local Regularity*, arXiv:2607.08954v2 (2026), is absent from `refer.bib`. It is closely relevant to the ALM discussion: a smoothed prox-linear ALM with dual regularization obtains an O(K^{-1/3}) KKT residual rate under local multiplier regularity, and an unregularized O(K^{-1/2}) result under additional local structure. It belongs next to the fixed-penalty/local-regularity comparison, not in the same rate class as this manuscript without qualification.

A further So-coauthored 2025 stochastic PVR-SGDA paper is not a useful citation for the present deterministic results unless the related-work section explicitly covers stochastic minimax methods. The paper should represent this research line through these direct technical connections rather than add every coauthored work.

### Bibliographic corrections

- `shi2025momentum`: use the publisher's official citation year 2025. Keep volume 51, issue 1, pages 92--133; INFORMS lists online publication on 23 January 2025 and cites the article as 2025.
- `elbourkhissi2025linearized`: identify arXiv:2301.08345v2 and reconcile the 2023 first-submission year with the 2025 revision date.
- `zhang2026matching`: arXiv metadata lists Minghao Zhang, while the title page lists Minhao Zhang. Preserve the discrepancy in the audit until an authoritative author record resolves it.
- `zhang2022proximal` and `zhang2020proximal`: exact same 2020 SIAM J. Optim. work appears twice under different keys; retain one canonical bib record after checking references outside this manuscript.

## Current verification boundary

Primary-source checks now cover the central minimax rates, Lin--Jin--Jordan's stationarity measure, GDPA's parameter schedule and regularity assumptions, SDD-ADMM's distinct rates and penalty scales, the two So-coauthored minimax papers already cited, Li--Zhu--So's nonsmooth stationarity definitions, the El Bourkhissi--Necoara version history, and the Shi et al. publication record. The remaining cited sources still need per-entry existence, metadata, and context review. Do not treat this report as a final full-paper pass.
