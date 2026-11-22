# Citation audit inventory

This is a read-only inventory of the active manuscript. It does not change `*.tex` or `refer.bib` and does not yet assign source-support verdicts.

## Scope

- Manuscript sources: `sections/*.tex`, `appendix/*.tex`
- Bibliography: `tools/refer.bib`
- Citation occurrences: 131
- Unique cited keys: 48
- Bib entries: 164
- Bib entries not cited in the active manuscript: 116

The 116 uncited entries are a residual of the shared bibliography. They are not evidence of incorrect citations and should be handled separately from the body-citation audit.

## Repetition triage

| Key | Total | Main-text occurrences | Appendix occurrences | Initial assessment |
|---|---:|---:|---:|---|
| `li2026smoothing` | 32 | 13 | 19 | Central source. Appendix pinpoint citations are largely justified; main-text uses should be consolidated where the same rate/role is repeated. |
| `zhang2020smoothed` | 10 | 9 | 1 | Repeated across introduction, family definition, and acceleration comparison. Check whether each use adds a distinct claim. |
| `luSingleLoopGradientDescent2022` | 6 | 6 | 0 | Repeated ALM/GDPA comparison; likely reducible to one origin citation plus one table citation. |
| `pan2026optimal` | 5 | 5 | 0 | Repeated for the same smooth NC-C benchmark; keep theorem-level source uses, remove redundant restatements. |
| `nesterov2018lectures` | 4 | 4 | 0 | Normal for definitions and acceleration background. |

The remaining repeated keys occur at most four times. Repetition alone is not a defect when the citation supports distinct claims or an appendix proof step.

## Exact duplicate or near-duplicate bibliography entries

The active body currently uses one member of several duplicate pairs, so these are bibliography-cleanup candidates rather than body over-citation findings.

- `zhang2022proximal` is cited twice; `zhang2020proximal` has the same title and is uncited.
- `zhang2020smoothed` is cited ten times; `zhang2020single` is uncited and has a related title with an additional coupled-constraint phrase. Verify whether it is a distinct version before merging.
- `trandinh2018smooth` and `tran2018smooth` have the same title and are uncited.
- `boct2020proximal` and `bot2020proximal` have the same title and are uncited.
- `davis2019stochastic` and `davis2019` have the same title and are uncited.
- `liu2019successive` and `pong2019` have the same title and are uncited.
- `karimi2025hingeLogistic` and `karimi2025differences` have the same title and are uncited.
- `Alacaoglu24a` and `alacaoglu2024complexity` have the same title; the latter is uncited while the former is cited once.
- `cui2022complexity` and `lin2022complexity` have the same title; only `lin2022complexity` is cited.

These pairs require canonical-record verification before any merge.

## Anthony Man-Cho So lineage check

The current bibliography contains the following directly So-coauthored works.

| Key | Cited? | Relation to this paper |
|---|---:|---|
| `zheng2023universal` | 3 | Directly relevant smooth NC-NC minimax / DS-GDA family. Keep. |
| `xu2026rada` | 1 | Directly relevant NC-L minimax and ALM-related comparison. Keep if the cited sentence remains specific. |
| `li2025nonsmooth` | 0 | Directly relevant nonsmooth NC-NC minimax and stationarity definitions. Candidate for a focused Related Work or GS/OS paragraph. |

Other current citations involving Jiajin Li, such as `li2026smoothing` and `pan2026optimal`, are relevant to the technical comparison but are not automatically “So lineage” citations. The paper should cite So-coauthored work where it supports a concrete minimax, stationarity, or ALM claim, while avoiding unrelated pedigree-only additions.

The official CUHK profile and publication list identify So's research scope and the relevant coauthored works. Zotero records independently confirm the metadata for `zheng2023universal`, `li2025nonsmooth`, and `xu2026rada`.

## Required source verification passes

1. Verify each cited entry's canonical metadata against arXiv, Crossref/DBLP, or the official proceedings record.
2. Verify each high-impact complexity claim against the theorem/definition in the cited paper, with the stationarity notion and cost unit stated explicitly.
3. Verify the origin of each structural claim in the introduction and related-work paragraphs, especially the transitions between smooth NC-C minimax, ALM, and constrained optimization.
4. Only after these passes decide whether to add So-coauthored work, remove redundant citations, or merge bibliography aliases.

## First source checks completed

The following checks used the cited paper's PDF or an official publisher/arXiv record rather than an abstract-only match.

- `li2026smoothing` supports the manuscript's central benchmark claims. Theorem 3.3 gives Perturbed Smoothed GDA an `O(epsilon^{-3})` GS bound; Theorem 3.4 gives the matching `Omega(epsilon^{-3})` GS lower bound; Corollary 3.1 gives `Theta(epsilon^{-4})` for Smoothed GDA in GS and OS. Theorem B.1 gives the corresponding upper bound.
- `pan2026optimal` v2 supports both the `Omega(epsilon^{-5/2})` GS lower bound and the matching Tracked-FOAM upper bound. The manuscript's GS use is valid for v2, but the bibliography should record the version explicitly because earlier notes described the OS result only.
- `zhang2026matching` supports the `O(epsilon^{-5/2})` GS comparison through Theorem 4.5 and Remark 4.4. Its PDF gives the first author as **Minhao Zhang**, while the arXiv metadata gives **Minghao Zhang**. The current BibTeX entry also has an unrelated `xurl` pointing to `pmlr.press/v267/jin25e.html`; this must be corrected before submission.
- `li2025nonsmooth` directly defines GS and OS for nonsmooth nonconvex-nonconcave minimax problems and gives the algorithm-independent relation between them. It is currently uncited even though the manuscript introduces both stationarity notions and uses a nonsmooth composite minimax framing.
- `elbourkhissi2025linearized` points to arXiv:2301.08345, whose source record is dated 2023 rather than 2025. The PDF does impose LICQ and reports an `O(epsilon^{-2})` first-order complexity in the relevant setting, so the context is plausible but the BibTeX year/key naming is wrong.
- `shi2025momentum` has a final Mathematics of Operations Research record in volume 51 (2026), while the article was published online in 2025. The current year 2026 is defensible for the final citation; the key name should be normalized if the bibliography uses final-publication years.

## Provenance sources used for the So-lineage check

- CUHK faculty profile: <https://www.se.cuhk.edu.hk/people/academic-staff/prof-so-man-cho-anthony/>
- So's publication list: <https://www1.se.cuhk.edu.hk/~manchoso/>
- CUHK research record for Li--Zhu--So (2025): <https://research.cuhk.edu.hk/en/publications/nonsmooth-nonconvexnonconcave-minimax-optimization-primaldual-bal/>
- Zotero local records were queried for `Anthony Man-Cho So`, `Jiajin Li`, and `Linglingzhi Zhu`.
- `lin2020gradient` Theorem 4.9 gives `O(epsilon^{-6})` gradient evaluations for a Moreau-envelope stationarity notion. Proposition 4.13 converts this to an `O(epsilon)` game-stationary pair with `O(epsilon^{-2})` additional gradients. The introduction should state the stationarity measure explicitly if it presents the `O(epsilon^{-6})` number as a GS rate.
