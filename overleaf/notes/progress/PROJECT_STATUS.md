# SPLALM 项目状态

更新日期：第 1–6 节为 2026-10-16 整理，2026-10-26 更新文件位置；第 7 节为 2026-10-26 新增。**本文件是当前进度与待办的唯一入口。** 依据当前本地源码、已有核查记录及讨论整理。第 1–6 节的更新没有重新核对数学证明，也没有重新编译论文。

历史交接、旧任务表、研究主线和白板用于追溯讨论，不作为当前待办。源码说明已经写入什么；核查记录说明已经核对什么；两者分别记录。

## 1. 当前阶段与范围

- 阶段：完整初稿的完善。算法名为 SPLALM，旧材料中的 DDLALM 指同一项目。
- 主线：单环线性化 ALM 族 $\mathcal C_\theta$ 在指定参数区域内的复杂度下界，以及与已有方法上界的联系。重点说明组合罚参数 $\rho+s$、对偶正则与中心步长各自的作用。
- 新结果重点：对所有常数中心步长一致成立的下界。两个上界分别由 Smoothed GDA、Perturbed Smoothed GDA 的分析换算得到。
- 当前源码标题：*Shrink the Dual Regularization, Keep the Penalty: Tight Complexity of Linearized Augmented Lagrangian Methods*。用户已接受调整标题；新标题尚未确定。
- 评议参照：以 SIOPT 中贡献类型相近的工作为主，再依据成果讨论 Mathematical Programming。旧任务表中的结果与期刊对应关系不作为当前决定。
- 已关闭：把下界推广到时变或单调中心步长，不列入本轮必须完成的工作。

## 2. 已写入的结果与适用范围

1. **下界 `thm:lower-bound`。** 固定 $0<\eta\le\gamma$、$\tau>0$、$\Delta>0$，对充分小的精度、$\rho>0$、$s\ge\tau$ 且 $\epsilon(\rho+s)\le c_1$，每组常数 $(\alpha,\beta)\in[0,1]^2$ 均有从全零初值出发的困难实例，给出 $\Omega(\epsilon^{-4})$。常数 $c_1,c_2$ 不依赖 $\rho,s,\alpha,\beta$，精确量词和常数见定理。平台、旋转、Huber 三分支及主定理证明均已写入；部分核查待完成，见第 4 节。
2. **上界 `thm:upper-beta1`。** 在该定理的步长条件下，取 $\beta=1$、$\alpha=c\epsilon^2$，得到 $O(\epsilon^{-4})$。在同一问题类、固定 $\rho$ 且满足上下界共同条件时，与下界形成族复杂度的紧性结论。不能把该上界常数未经核对地用于随精度增长的 $\rho$。
3. **上界 `thm:upper-beta0`。** 固定 $\rho,\gamma,\eta,\tau$ 并满足 `eq:beta0-stepsizes`，取 $s=c_s/\epsilon$、$\alpha=c_\alpha\epsilon$、$\beta=0$，得到 $O(\epsilon^{-3})$。$c_s$ 足够大、$c_\alpha$ 足够小，参数在单次运行内保持常数。定理、Remark、附录证明均已写入；$C_*$ 的引用换算仍待独立逐行核对。
4. **合并推论 `cor:effective-penalty`。** 已写入上述下界区域与固定 $\rho$ 的充分参数路径。$\rho=c/\epsilon$、$s$ 固定及上侧其他参数路径的族内复杂度尚未由这些结果刻画。
5. **补充上界 `thm:main`。** 递增 $s_k$ 的 accuracy-independent schedule 仍在附录中，使用额外的水平有界假设。它与已经关闭的“时变中心步长下界推广”分别处理。

表述约束：低参数区域内，调节常数中心步长无法突破上述下界；固定 $\rho$ 时，已有一组参数达到较好的上界。不能写“中心步长与复杂度无关”“增大 $\rho$ 在所有区域都无效”或“整个上侧区域只由 $\rho+s$ 决定”。$\beta=0$ 固定的是对偶中心，原始中心仍移动。$O(\epsilon^{-3})$ 的可达性本身不等于该区域的复杂度最优性。

## 3. 当前稿件与产物

| 位置 | 文件 | 状态 |
|---|---|---|
| §1 | `sections/Introduction.tex` | 问题、比较表与贡献已写入；随评议完善定位与措辞 |
| §2 | `sections/Preliminaries.tex` | 问题类、驻点判据与 oracle 定义 |
| §3 | `sections/AlgorithmFamily.tex` | 算法族、复杂度、组合罚参数与特殊情形 |
| §4 | `sections/LowerBound.tex` | 两个上界、下界及合并推论均已写入 |
| §5 | `sections/LowerBoundProof.tex` | GDA 递推对应、三个困难实例分支与主定理证明均已写入 |
| §6 | `sections/Conclusion.tex` | 总结与开放问题已写入 |
| 附录 A | `appendix/LowerBoundRotation.tex` | 已有 10-13 解析核查记录 |
| 附录 B | `appendix/UpperBoundBetaOne.tex` | β=1 上界证明已写入 |
| 附录 C | `appendix/UpperBoundBetaZero.tex` | β=0 上界证明已写入；末尾保留未核对事项 |
| 附录 D、E | `sections/UpperBound.tex`、`appendix/UpperBoundProofs.tex` | 递增参数上界及证明，作为补充 |

- 旋转示意图：`figures/plot_rotation_instance.py` 与 `figures/rotation_instance.pdf` 已存在，不再列为待生成；本次未重跑脚本，也未重新验收图形。
- `sections/RelatedWorkDraft.tex` 和旧独立核查产物已清理；附录 A 的详细核查记录保留。
- `main.pdf` 为已有产物；本次未重新编译，阅读时以源码为准。

## 4. 当前待办

### 优先完成

1. **β=0 上界引用换算。** 对照 Li26 v2 §4.2 (4.19)–(4.23)，核对 `eq:beta0-gs-rate` 中 $C_*$ 的存在性、参数依赖、精度一致性和平均常数。证明材料见 `notes/gpt-proofs/beta0-upper-check-20261013.md`。写入完成不代表核查完成。
2. **下界证明衔接。** 核对 §5 的 `subsec:lb-huber` 与主定理证明，确认分支覆盖、零初值、实例类成员关系和统一常数。附录 A 的既有通过记录不能替代这些分支的核查。
3. **初稿评议与叙事完善。** 使用 `notes/prompts/gptpro-draft-review-prompt.md`。依据实际定理调整标题、摘要、问题 (Q)、贡献与结论，突出参数区域下界增加的认识。当前摘要仍使用 “$s$ of order $1/\epsilon$” 的简写；需核对其是否应补明充分大的系数与中心步长条件，不能沿用旧记录声称全部措辞已同步。

### 与定位直接相关的文献核对

- 按 `notes/prompts/gptpro-literature-research-prompt.md` 核对最接近的参数区域下界、组合罚参数恒等式的来源和比较表。
- PPALA：核对问题类、驻点判据、有限步可行性与算法结构；不能预设其与本文在同一问题类上比较。
- LP-ALM、NR-LALM、GDPA：区分问题假设、更新方式和参数条件。LP-ALM 的参数对应目前是待核对的粗对应；固定 $\rho$ 的定量收益需要可比条件下的计算。
- β=1 引用中的 Zhang Lemma B.11 常数依赖，以及 arXiv v3 / NeurIPS 版本编号，仍保留为待核对项。

### 最后处理的编辑项

- `sections/Introduction.tex` 中 “oraccuracy $eps$-dependent” 笔误。
- `tools/refer.bib` 中 `zhang2020single` 与 `zhang2020smoothed` 重复条目，合并时同步实际引用。
- 主体与附录顺序确定后，决定 Organization 是否补充附录说明。
- GS 版本和向一般 Smoothed GDA / DS-GDA 的下界推广为可选事项，不作为当前必做任务。

## 5. 材料使用规则

- 当前定位和任务只在本文件维护。完成任务时更新对应条目，不在文件末尾追加与旧正文冲突的“最新状态”。
- `SESSION_HANDOFF_*.md`、`ddlalm-task-plan.md`、`ddlalm-research-questions.md`、下界讨论记录、Booming 白板与已完成提示词为历史资料，2026-10-26 移至仓库根目录 `memory/archive/notes/`。旧幻灯片、8 月 V2/RouteB 材料与旧版论文在 `memory/archive/` 的其他子目录。里面的旧标题、旧初值、章节号和任务不能自动恢复为当前要求。
- `notes/gpt-proofs/` 保存证明来源；`lb-proof-materials.md` 的 Part I 平台分支仍有用途，Part II 与 Part III 的适用关系按文件顶部说明读取。
- `appendix-a-audit-20261013.md`、`ddlalm-verification-20261001.md` 保存已有核查依据。本次进度整理不新增数学核查结论。
- `literature.md`、`lower-bound-references.md`、`writing-phrasebook.md` 分别用于文献总表、下界参考和英文表达来源。
- `notes/conversations/` 与 `notes/skills/` 按用户要求保留。历史对话与方法副本不自动成为当前执行指令；对话时间覆盖见该目录 README。
- 已撤回判断：不能由任意 oracle 下界推断本文的参数区域下界会被替代。同一问题类与度量下的 oracle 下界能向子族转移，但转移本身不增加下界的阶。

## 6. 同步范围

本地论文入口为 `overleaf/main.tex`；仓库根目录的旧论文副本（10-13 快照）已于 2026-10-26 删除。Overleaf 远端的文件与 `overleaf/` 目录对应（10-26 按文件内容核对）。GitHub 远端是 `github`（`luxuan846-oss/3-DDLALM`）；`origin` 是 Overleaf，不能混用。用户本次授权把笔记更新提交并推送 GitHub。Overleaf 不属于本次推送范围；远端实时状态应通过 Git 查询，不沿用历史交接中的提交号。

## 7. 后续研究线：加速与 Tikhonov（2026-10-25 起）

分工与顺序见 `notes/project/next-lines-plan-20261025.md`；问题表述与 GPT Pro 指令见 `notes/prompts/gptpro-tikhonov-eg-alm-prompt.md`、`notes/prompts/gptpro-acceleration-logic-20261026.md`。下表为 10-26 GPT Pro 第二轮结果经 Gemini 与 Claude 复核后的结论。

| 结论 | 状态 |
|---|---|
| 固定 $\rho>0$ 时 $\nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})=0$ 当且仅当 $\boldsymbol{\lambda}\in\partial h(\mathcal{A}(\mathbf{x}))$，KKT 关系精确。$\mathcal{D}_\rho$ 的对偶 Hessian 为 $-\rho^{-1}J_{\mathrm{prox}_{h/\rho}}$，曲率介于 $0$ 与 $1/\rho$。GPT 所称"固定 $\rho$ 留下 $1/\rho$ 偏差、选最小范数乘子需 $\rho_k\to\infty$"不成立 | 推导 |
| 固定 $s$ 时 Tikhonov 项只提供强单调性；算法 A、B 在有界步长下单步收缩因子为 $1-\Theta(1/s)$ | 已证（直接计算） |
| 不用 momentum，Tikhonov 或 anchoring 不能把中心步长放宽到 $\alpha\sim1/\sqrt{s}$ | 证据充分；针对算法 A、B 的下界待证 |
| Zhang–Xu（arXiv:2609.17973）的 $\sqrt{s}$ 增益来自对偶动量：带衰减的对偶梯度累加，窗口约 $\sqrt{Ls}$ 步；中心步长取 $\propto1/\sqrt{Ls}$ | 原文 (4.3)、(4.26)；纯对偶模态谱隙已数值核对 |
| Zhang–Xu Algorithm 1 直接作用于 $\mathcal{D}_\rho$（定义域 $\mathbb{R}^n\times\mathcal{Y}$，$\mathcal{Y}$ 为半径 $2L_h$ 的球），得到单循环、固定 $\rho$ 的 $O(\epsilon^{-5/2})$ $\epsilon$-KKT 复杂度。依据：附录 C Step 1–2 的约化；$\epsilon<L_h/\rho$ 时 $\epsilon$-GS 点位于 $\mathcal{Y}$ 内部 | 推断；初值量 $\bar\Delta_0$ 在 $\mathcal{I}(\mathbf{C},\Delta)$ 上一致有界待核 |
| Pan–Zheng–Li（arXiv:2609.14235v2）的 GS $\Omega(\epsilon^{-5/2})$ 直接转移到 $\mathcal{I}(\mathbf{C},\Delta)$ | 不成立：$g_3$ 的对偶二次项依赖 $\mathbf{x}$，其 oracle 不含 $\mathrm{prox}_h$ |
| 算法 B 的 Tikhonov 锚点为 $\boldsymbol{\mu}^k$。$\beta_k\equiv0$ 时选择目标为最小范数乘子；现行 $\beta_k=\theta_\mu/(k+k_0)$ 不可和，锚点跟随 $\boldsymbol{\lambda}^k$，没有选择效应 | 推导 |
| 纯 Tikhonov、$s_k\asymp k$、$\boldsymbol{\lambda}^\dagger\neq0$ 时 KKT 残差为 $\Theta(1/k)$；$o(1/k)$ 需要惯性项 | 推断；待对照 arXiv:2406.00852、2410.14369 原文 |

对两条线的影响：

- 线 1：$\epsilon^{-5/2}$ 上界本身接近"Zhang–Xu + 附录 C 约化"的推论。新意转向两处：momentum-free 族 $\Theta(\epsilon^{-3})$ 与对偶动量 $\epsilon^{-5/2}$ 的分离（EG 族不加动量时的下界待证）；带 $\mathrm{prox}_h$ oracle 的 $\Omega(\epsilon^{-5/2})$ 下界构造。
- 线 2：在 $\beta\equiv0$、$s_k\uparrow\infty$ 下提出，目标为局部正则条件下的最小范数乘子与 $O(1/k)$ 残差。Zhang–Xu 的对偶锚点同样固定在 $0$，可作为算法结构的起点。

缺失材料：`ChatGPT-核查算法与下界-20261026-0749.md` 与 `ChatGPT-文献核查与算法加速!-20261026-1052.md` 未入库，待放入 `notes/conversations/`。
