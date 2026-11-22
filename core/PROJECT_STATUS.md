# LRALM 项目状态

更新日期：2026-11-21。**本文件是当前进度与待办的唯一入口。** 依据 11-21 02:36 的本地源码、`overleaf/main.log`、`memory/notes/project/CITATION_AUDIT.md`、`memory/notes/project/citation-candidates-20261121.md` 和 11-16 至 11-21 的对话记录整理。本次整理没有重新核对数学证明。上一版（10-16 至 11-17 的逐条记录，含 Fast LRALM 重构交接细节、10-26 加速与 Tikhonov 线结论表）见 commit `5c34731` 中的同名文件。

## 1. 当前阶段与范围

- **阶段**：完整初稿已成形（正文 4 节结果加附录 3 节，49 页）。剩下的工作是实验、引用修订、证明核查和叙事统一。
- **标题**：*Accelerated Linearized Augmented Lagrangian Method with a Fixed Penalty for Nonconvex Composite Optimization*（`main.tex` 第 82–83 行）。
- **主线**：(i) LRALM 族 $\mathcal{C}_\theta$ 的紧复杂度，由有效罚参数 $\rho+s$ 决定；(ii) 族外的 Fast LRALM，固定 $\rho$，对偶 Nesterov 外推，达到 $\mathcal{O}(\epsilon^{-5/2})$。
- **投稿**：建议 SIOPT，备选 Mathematical Programming。
- **已关闭**：时变中心步长的下界推广；递增 $s_k$ 的补充上界（旧附录 D、E 已删，可由 `git show b69dee2:overleaf/sections/UpperBound.tex` 取回）；合并推论 `cor:effective-penalty`（已注释）。

## 2. 已写入的结果

1. **`thm:lower-bound`**：$\epsilon(\rho+s)\le c_1$ 时，对所有常数 $(\alpha,\beta)$，族复杂度为 $\Omega(\epsilon^{-4})$；常数 $c_1,c_2$ 只依赖 $(\gamma,\eta,\tau,\Delta)$。**`prop:upper-beta1`**（Smoothed GDA，$\beta=1$，$\alpha=c\epsilon^2$）给出匹配的 $\mathcal{O}(\epsilon^{-4})$，合起来为 $\Theta(\epsilon^{-4})$。
2. **`thm:lower-bound-fixed-rho`**：固定 $\rho$、$s=c_s/\epsilon$ 时为 $\Omega(\epsilon^{-3})$，对任意 $c_s>0$ 成立。**`prop:upper-beta0`**（Perturbed Smoothed GDA，$\beta=0$，$\alpha=c_\alpha\epsilon$）给出 $\mathcal{O}(\epsilon^{-3})$；对该命题中的 $c_s$，族复杂度为 $\Theta(\epsilon^{-3})$。
3. **中心步长阈值**：$\alpha=\Theta(\epsilon^2)$ 与 $\alpha=\Theta(\epsilon)$ 是临界尺度，超过后在问题类内存在 $T_\epsilon=+\infty$ 的实例。困难实例为四个分支：plateau（`lem:main-plateau`）、rotation（`lem:main-rotation`）、Huber（`lem:main-huber`）、radial（`lem:main-radial`），证明在附录 B。
4. **`thm:b2-prime-complexity`（Fast LRALM）**：$s=c_s/\epsilon$、$c_s\ge 12\sqrt{\rho/\tau}\,L_h$ 时为 $\mathcal{O}(\epsilon^{-5/2})$。第 4 节的引理全部带证明，红色占位已回填：残差界、乘子一致有界（改用 Khlebnikov 二次 Lyapunov 函数）、fixed-center contraction、proximal descent、center-update error、sufficient descent 与初值差。

**表述约束**：$\Theta(\epsilon^{-3})$ 只对 $s=c_s/\epsilon$ 这一路径成立，不等于整个 $\rho+s\gt c_1/\epsilon$ 区域的最优阶。$\beta=0$ 固定的是对偶中心，原始中心仍移动。不写 "proximal ALM 不能加速"（族外没有证明）。

## 3. 稿件结构

| 位置 | 文件 | 状态 |
|---|---|---|
| §1 | `sections/Introduction.tex` | 动机例子、Related work、比较表、Organization 已写；引用待修订，见 §4.2 |
| §2 | `sections/Preliminaries.tex` | 问题类、reduced / regularized AL、`prop:curvature-smoothness` |
| §3 | `sections/LRALMFamily.tex` | 族定义、`lem:effective-penalty`、两组上下界、困难实例 |
| §4 | `sections/Acceleration.tex` | Fast LRALM 算法、分析框架、全部引理与主定理；路线图 `fig_roadmap_acceleration.tex` |
| §5 | `sections/Experiments.tex` | **空**，只有 TODO |
| §6 | `sections/Conclusion.tex` | 已按两组 $\Theta$ 结果改写 |
| 附录 A | `appendix/ValueFunctions.tex` | 正则化势函数与值函数性质；前三个子节已注释 |
| 附录 B | `appendix/LowerBoundConstructions.tex` | 下界归约、四个分支、两个下界定理的证明 |
| 附录 C | `appendix/UpperBounds.tex` | 两个上界命题经 `lem:ub-reduction` 换算到 Li26 |

- **编译**：11-23 生成 `main.pdf`，50 页，无错误、无未定义引用。
- **版本**：11-23 提交 `55f0755` 并推送到 GitHub（含论文、实验、`MILESTONES.md`、引用审计）；Overleaf 远端为 `272032f`，与本地 `overleaf/` 的论文源码一致。88M 的 `novelty-check-20261122/` 和 ReasBook 子模块未提交。

## 4. 当前待办

### 4.1 与老师讨论：Fast LRALM 加速（2026-11-17 定）

每次讨论只谈一块。本次只谈加速，下界、arXiv、署名不在议程中。材料由四部分组成。

**1. 加速的本质。** 固定 $\rho$ 后，$\mathcal{D}_\rho$ 关于 $\boldsymbol\lambda$ 是光滑凹函数，梯度 Lipschitz 常数只依赖 $\rho$。按 Lin–Jin–Jordan（COLT 2020）的归约，加以 $\mathbf{0}$ 为中心、系数 $1/s$ 的对偶正则，问题变成 NC-SC。乘子在半径 $L_h$ 的球内，正则偏差为 $\mathcal{O}(L_h/s)$，取 $s=\Theta(\epsilon^{-1})$，对偶条件数 $\kappa=\Theta(\epsilon^{-1})$。NC-SC 下界 $\Omega(\sqrt{\kappa}\,\epsilon^{-2})$（Zhang 等 UAI 2021；Li 等 NeurIPS 2021）代入得 $\epsilon^{-5/2}$。不加速时对 $\kappa$ 一次依赖，$\kappa\,\epsilon^{-2}=\epsilon^{-3}$，即族内的 $\Theta(\epsilon^{-3})$。加速把 $\kappa$ 降为 $\sqrt{\kappa}$；对偶目标在全空间光滑强凹，无需投影，Nesterov 外推直接加在乘子步上。
- 待核：`prop:upper-beta0` 对 $\kappa$ 的一次依赖需从附录 C 的证明中提取。

**2. 讨论提纲。**
- Related work 中的加速：IAIPAL、iALM 多循环，加速在内层（APG 解强凸子问题），带对数因子；本文单循环，加速在外层乘子步。Zhang–Xu 的单循环结果主项无乘性 $\log(1/\epsilon)$，对数只出现在加性的 $\epsilon^{-1/2}$ 预热项中（11-17 对话核对过 Corollary 4.4）。
- 分析难点：(i) 不投影时外推乘子需另证有界（`lem:b2-prime-multiplier-bounds`）；(ii) 外推后单步不单调，收缩的是估计序列，误差放大 $\sqrt{\kappa}$ 倍，势函数加原始跟踪项与增量项。
- 与别人的区别：ALM 方面，核查过的 20 篇内无非凸 ALM 乘子外推的复杂度结果；minimax 方面，Zhang–Xu 已在 $\mathcal{D}_\rho$ 上（对偶球半径 $2L_h$）给出单循环 $\mathcal{O}(\epsilon^{-5/2})$。请老师确认定位：贡献放在族的紧复杂度，加速部分主张算法与分析更简单（梯度步加外推，无投影，无 extragradient）。

**3. 汇报文献。**

| Method | arXiv | 结论 | 备注 |
|---|---|---|---|
| Zhang–Yang–Guzmán–Kiyavash–He, UAI 2021 | 2103.15888 | NC-SC 下界 $\Omega(\sqrt{\kappa}L\Delta\,\epsilon^{-2})$ | 下界中 $\sqrt{\kappa}$ 的来源 |
| Li–Tian–Zhang–Jadbabaie, NeurIPS 2021 | 2104.08708 | 同一下界，确定性 oracle | 与上一篇并列引用 |
| Lin–Jin–Jordan, COLT 2020 | 2002.02417 | Minimax-PPA；NC-C 得 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$ | 对偶正则归约的来源 |
| Kong–Melo–Monteiro, SIOPT 2023 (IAIPAL) | 2008.00562 | 内层 ACG，$\mathcal{O}(\epsilon^{-5/2}\log^2\epsilon^{-1})$ | 加速 ALM |
| Li–Chen–Liu–Lu–Xu, AISTATS 2021 (iALM) | 2007.01284 | 仿射约束 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$，需正则性条件 | 加速 ALM |

另加：Kong–Monteiro 2024（乘子阻尼中心在 $\mathbf{0}$，$\mathcal{O}(\epsilon^{-3})$，最接近 $\beta=0$ 成员）；Zhang–Xu（arXiv:2609.17973，必须汇报）；Ke–Mei–Zhang（arXiv:2609.25752，多层循环 $\mathcal{O}(\epsilon^{-5/2})$）。

**4. 投稿与实验。** 见 4.3。

### 4.2 引用修订（2026-11-21 开始）

材料：`memory/notes/project/CITATION_AUDIT.md`（引用上下文审计，48 个已引条目尚未全部核完）与 `memory/notes/project/citation-candidates-20261121.md`（候选新引用，已读原文，标 SUPPORTS / PARTIAL / DOES NOT FIT，附 BibTeX）。已落盘的只有 `refer.bib` 删 5 条、增 2 条。待用户拍板后执行：

1. **改写或收窄的句子**：Intro 第 70–81 行八篇文献混在一个 $\epsilon^{-1}$ 参数论断下；GDPA 行混合 `luSingleLoopGradientDescent2022` 与 `sun2024dual_descent_alm_admm`；`carmon2020lower` 只能作为无约束子类继承的下界；`xu2026rada` 需注明 Riemannian 设定；Prelim 第 177–198 行的复合 KKT 残差恒等式属于本文结果。
2. **So 组与谱系**：`li2025nonsmooth`（LZS25，bib 中已有，未引）用于 GS/OS 段；`li2020nonconvex`（Li–Zhu–So–Vidal）与 `charisopoulos2021low` 并列；Zhu–Li（arXiv:2607.08954）为 PARTIAL，只放固定罚加局部正则一类。
3. **查源头**：NC-C 多循环 $\epsilon^{-5/2}$ 补 Lin–Jin–Jordan；`moreau1965`、`nesterov2005smooth` 已在 bib 未引。
4. **元数据**：`zhang2022proximal` 实为 SIOPT 2020；`elbourkhissi2025linearized` 为 arXiv:2301.08345（2023 v1）；`zhang2026matching` 作者名 Minghao / Minhao 不一致。
5. **降频**：`li2026smoothing` 正文重复的背景引用合并，附录 19 处定理定位引用保留。
6. **Antigravity 会话（11-21）提出、尚未核对的两条**：比较表把 IAIPAL 并入 iALM 行；`luSingleLoopGradientDescent2022` 被引作 $(\alpha,\beta)=(1,1)$ 的无扰动线性化 ALM 来源。
7. 116 条未引条目投稿前再清理。

### 4.3 实验（§5 为空）

提议实例（待用户确认后再写代码）：robust phase retrieval，$\min_{\mathbf{x}} \frac{1}{m}\sum_i \lvert\langle\mathbf{a}_i,\mathbf{x}\rangle^2-b_i\rvert$，$n=50$、$m=200$；比较 LRALM（$\beta=1$）、LRALM（$\beta=0$，$s=c_s/\epsilon$）、Fast LRALM；记录达到 $\epsilon$-KKT 的迭代数，对数坐标拟合斜率，预期 $-4$、$-3$、$-5/2$；$\epsilon^{-4}$ 一条只取 $\epsilon\in[0.03,0.3]$。

### 4.4 证明核查

1. **附录 B**：11-20 之后大幅重写（约 1800 行改动），重写后没有独立核查记录。重点核对四个分支的覆盖、零初值、实例的问题类成员关系和统一常数。
2. **附录 C**：`lem:ub-reduction` 到 Li26 v2 §4.2 (4.19)–(4.23) 的常数换算尚未逐行核对。
3. **第 4 节**：乘子有界性改用 Lyapunov 证明后，未见用户复核记录。

### 4.5 叙事与零散项

- 摘要、引言贡献段与新标题对齐：标题突出加速与固定罚参数，贡献段需同时交代族的两组 $\Theta$ 结果。
- 标签仍用旧名：`splalm` 出现在 `Acceleration.tex`、`LRALMFamily.tex` 与两个附录中（共 10 处）；`eq:x-weak-convexity-modulus` 名不副实。改名需同步全部引用。
- LRALM 尚未做重名检索。
- `xie2021proximal`（Intro 第 64 行）的 proximal 项作用在原始变量上，引用措辞需与原文一致。
- 附录 A 前三个子节已注释，确认是否删除或恢复。

## 5. 材料使用规则

- 当前定位和任务只在本文件维护。完成任务时更新对应条目，不在文件末尾追加与正文冲突的"最新状态"。
- 历史交接、旧任务表、白板与已完成提示词在 `memory/archive/`，其中的旧标题、章节号和任务不能自动恢复为当前要求。
- `memory/notes/gpt-proofs/` 保存证明来源；`memory/notes/project/` 下的 `literature.md`、`lower-bound-references.md` 分别用于文献总表和下界参考；英文表达在 `core/writing-phrasebook.md`。
- 已撤回判断：不能由任意 oracle 下界推断本文的参数区域下界会被替代；同一问题类与度量下的 oracle 下界能向子族转移，但不增加下界的阶。

## 6. 同步范围

本地论文入口为 `overleaf/main.tex`。`origin` 是 Overleaf，`github` 是 GitHub（`luxuan846-oss/3-DDLALM`），不能混用。推送前用 Git 查询远端实时状态，不沿用历史提交号。
