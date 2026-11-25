# LRALM 项目状态

更新日期：2026-11-24。**本文件是当前进度与待办的唯一入口。** 依据 11-21 02:36 的本地源码、`overleaf/main.log`、`memory/notes/project/CITATION_AUDIT.md`、`memory/notes/project/citation-candidates-20261121.md` 和 11-16 至 11-21 的对话记录整理。本次整理没有重新核对数学证明。上一版（10-16 至 11-17 的逐条记录，含 Fast LRALM 重构交接细节、10-26 加速与 Tikhonov 线结论表）见 commit `5c34731` 中的同名文件。

## 1. 当前阶段与范围

- **阶段**：完整初稿已成形（正文 4 节结果加附录 3 节，49 页）。剩下的工作是实验、引用修订、证明核查和叙事统一。
- **标题**：*Accelerated Linearized Augmented Lagrangian Method with a Fixed Penalty for Nonconvex Composite Optimization*（`main.tex` 第 82–83 行）。
- **主线**：(i) LRALM 族 $\mathcal{C}_\theta$ 的紧复杂度，由有效罚参数 $\rho+s$ 决定；(ii) 族外的 Fast LRALM，固定 $\rho$，对偶 Nesterov 外推，达到 $\mathcal{O}(\epsilon^{-5/2})$。
- **投稿**：目标 Mathematical Programming（MP），备选 SIOPT。
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
4. **元数据**：`zhang2022proximal` 实为 SIOPT 2020；`elbourkhissi2025linearized` 为 arXiv:2301.08345（2023 v1）。（已完成：`zhang2026matching` 已更新为 v2，含 Minhao Zhang、Zi Xu、Anthony Man-Cho So、新标题与 `arXiv:2609.17973v2`，Waterbirds 已从 §5 移除，正文引用已对齐 v2。）
5. **降频**：`li2026smoothing` 正文重复的背景引用合并，附录 19 处定理定位引用保留。
6. **Antigravity 会话（11-21）提出、尚未核对的两条**：比较表把 IAIPAL 并入 iALM 行；`luSingleLoopGradientDescent2022` 被引作 $(\alpha,\beta)=(1,1)$ 的无扰动线性化 ALM 来源。
7. 116 条未引条目投稿前再清理。

### 4.3 实验（r6 已完成，结果已写入 §5.2）

- **两个实验**：实验一 IllCondL1（$\sigma_{\min}\in\{10^{-2},10^{-3},10^{-4}\}$，$\epsilon=10^{-5}$，15000 次调用），看加速优势随病态程度的变化；实验二 Waterbirds Group DRO（照搬 Zhang–Xu §6.2，$\epsilon=10^{-3}$，4000 次调用，正则中心放在初始点），看前期下降更快、最终值有竞争力。MNIST mNPC 太简单，已去掉。
- **对比方法**：Smoothed GDA、Perturbed Smoothed GDA、iALM（Sahin et al. 2019 Alg. 1，$\beta_1=1$、$\sigma_1=10$，内层 Nesterov 动量 0.1）、Zhang–Xu Alg. 1。
- **调参口径（MoSSP 式）**：每个关键参数从 4 个候选值中选，在第 1 个初始点上选参，再从 5 个初始点运行，报 mean ± std 与最小–最大带。$\alpha\in\{1/6,0.3,0.5,0.8\}$，不取 1；Fast LRALM 选出的 $\alpha$ 统一给两个 GDA 基线，附录另报基线各自最优 $\alpha$。不改数据、不挑种子、不删基线；合规的取舍只有选实例、正文横轴范围（Waterbirds 前 1000 次）和报告指标。
- **r5 结论**：Fast LRALM 按定理常数取参（$c_s=24L_h$、定理 $\omega$、$\tau=\rho/4$）在三个实例上都输给 Smoothed GDA，原因是 $\kappa=s/\tau\sim10^7$ 使 $\omega\to1$。r6 改为 $c_s/L_h\in\{0.3,1,3,24\}$、$\omega\in\{$定理值$,0.9,0.95,0.98\}$、$\tau/\rho\in\{1/4,1\}$ 也参与选参，Perturbed Smoothed GDA 的 $c_s$ 用同一组候选值；正文须写明定理常数是充分条件、实验按网格选取。
- **r6 结果**：Fast LRALM 在三个 IllCondL1 实例的全部初始点上达到目标阈值。Waterbirds 上两种 GDA 在 1000 和 4000 次 oracle calls 的平均 best-so-far KKT residual 均低于 Fast LRALM。IllCondL1 上两种 GDA 的轨迹近乎重合，图中用菱形标记区分 Smoothed GDA，不偏移坐标。
- **r7（2026-11-24 运行中）**：选参改为按 viol、stat、obj 三个指标分别选，所有方法统一采用有效性规则（不发散且 $F(x_K)\le F(x_0)$），断点续跑按 `{tag}_{metric}` 跳过已存结果。IllCondL1 σ=1e-2 上三个指标 Fast LRALM 均排第一。浏览器 Colab 运行，由 Claude 通过 colab-mcp 读取进度。
- **下一轮提速方案**：(1) 每个运行时只领一个任务（一个 σ 或一个数据集），用一个参数格指定，多个运行时并行；(2) `_select_and_run` 把 5 个初始点放进同一批（B=5）一起跑，轨迹记录改为批量版本，代替逐个初始点串行运行。
- **基线选参（GPT Pro 11-24）**：两个 GDA 基线共用 Fast LRALM 选出的 $\alpha$ 是最强质疑，r7 应给基线单独搜索 $\alpha$；正文写明实验参数在 Theorem 4.1 充分条件之外、Waterbirds 不满足 Jacobian 全局有界。
- **文件**：`experiments/ill/` 和 `experiments/water/` 各有 `colab_runner_r6.ipynb`、`plot.py` 和 `results/`。各实例的 `_r6.npz`、运行后生成的参数 JSON 和单组图归入各自的 `results/`；跨实例合图保留在 `experiments/results/`。原 r6 notebook 归档于 `memory/archive/experiments-r6-original/`。r1–r5 notebook、MNIST notebook 和 r6 之前的旧结果已移到 `memory/archive/experiments-r1-r5/`；r5 的定理常数失败记录是正文「定理常数是充分条件、实验按网格选取」的依据。

### 4.4 证明核查

1. **附录 B**：11-20 之后大幅重写（约 1800 行改动），重写后没有独立核查记录。重点核对四个分支的覆盖、零初值、实例的问题类成员关系和统一常数。
2. **附录 C**：`lem:ub-reduction` 到 Li26 v2 §4.2 (4.19)–(4.23) 的常数换算尚未逐行核对。
3. **第 4 节**：乘子有界性改用 Lyapunov 证明后，未见用户复核记录。
4. **Fast LRALM 初值推广到 $\mathcal{S}_0(\mathbf{C})$（11-24 已通过 Codex 复核）**：`memory/notes/codex-review-init-patch-20261124.md`（`gpt-6.2-astra` high）确认 A/B/D 全 PASS，Lemmas 4.1–4.6、Theorem 4.1、附录依赖与 L909 同口径分离均成立；C 仅查出 Remark 4.1 L167 恢复经典 linearized ALM 缺少 $\mathbf{z}^0=\mathbf{x}^0$，已当场补齐。

### 4.5 叙事与零散项

- **§3.1（11-24 重写，蓝字）待定**：方法定位段按「图已标位置，正文只留引用与成员结论」压成一句（压缩版见 11-24 对话）；节首 "existing GDA methods" 改 "existing single-loop methods"（含线性化 ALM）。（已核实：`zheng2023universal` NeurIPS 2023 原文 Algorithm 1 p.4 与 Prop. 1 p.5 表明，DS-GDA 作用在无约束 $\mathcal{D}_\rho$ 上时与 (3.1) 逐行一致且满足 $0<\eta\le\gamma,0<\tau\le s$，是 $\mathcal{C}_\theta$ 中 $(\alpha,\beta)\in(0,1)^2$ 的严格成员，其 $r_2\ge 2L_y$ 对应 $s\le\rho/2$ 落入 $\Theta(\epsilon^{-4})$ 档位，可与其他方法同列。）
- **卖点与引言（11-24 定）**：族内与加速的联系落在原始中心步长上限，族内 $\alpha\le B\epsilon$（radial 实例）对 Fast LRALM $\alpha=\Theta(\epsilon^{1/2})$（$\kappa^{-1/2}$ 收缩裕量）；不写「族内收缩率 $1-\kappa^{-1}$」。$\Theta(\epsilon^{-3})$ 上界只对 Proposition 3.2 的 $c_s$ 成立，引言需注明。中心步是包络上的非精确梯度步这一观点 Zhang–Xu (3.3) 已写，不作创新点。
- **GPT Pro 审稿（11-24）未处理项**：Remark 3.2 限定为族内最佳最坏复杂度；§5 对两条 GDA 曲线重合的理论解释删去；p.4 两句（固定零对偶中心、已有同阶方法全依赖嵌套循环）；p.13「$f$ 有下界」改为 $F$；p.26 without convexity；Lemma 4.1 补 $\eta\le\gamma$。

- 摘要、引言贡献段与新标题对齐：标题突出加速与固定罚参数，贡献段需同时交代族的两组 $\Theta$ 结果。**摘要（11-25）**：替换稿已定结构（固定罚核心问题 → 族给机制 → 机制引出 Nesterov → 「first」限于加速乘子更新 → 实验句），待老大确认后写入 `main.tex`；机制句「乘子更新是光滑强凹对偶目标上的非精确梯度上升步」需对照 §3、§4 核实；「first」投稿前用 novelty-check 补查。
- §5 实验节缺与理论对照的收束句；lint 提示 12 处缩写首次出现无全称（LSALM、NR-LALM、CQ 等）。
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

## 7. 项目要点（2026-11-24 从 Claude 记忆迁入，三个 agent 共用）

### 7.1 Fast LRALM 一节的叙述顺序（老大要求牢记，2026-11-19）

- **构造按自顶向下讲**：先给 keynote $\min_z \max_\lambda \min_x P_s(x,\lambda;z)$，其中 $P_s = \mathcal{D}_\rho + \lVert x-z\rVert^2/(2\gamma) - \lVert\lambda\rVert^2/(2s)$。
  1. $z$ 更新：$p_s$ 上的非精确梯度步，即 $\varphi_s$ 上的非精确松弛近端点步；PPA 段落和 `eq:minimax-equality` 放在这里。Remark 1：复杂度 $\epsilon^{-2}\sqrt{\kappa}=\epsilon^{-5/2}$，warm start（Catalyst、zhang2021complexity、zhang2026matching 的中心移动拆分、Lin–Jin–Jordan）。
  2. $\lambda$ 更新：只在病态的一层（$\kappa=s/\tau$）对 $d_s$ 做 Nesterov 加速。Remark 2：只加速对偶；$\omega\gt 0$ 是相对 $\mathcal{C}_\theta$ 的唯一改动。
  3. $x$ 更新：一步梯度跟踪 $x_s(\bar\lambda^k;z^k)$。Remark 3：更新顺序和 oracle 计数（与 $\mathcal{C}_\theta$ 相同）。
  4. 四行迭代按执行顺序 $\bar\lambda\to x\to\lambda\to z$，$z$ 放最后，与 `eq:splalm-updates` 和 li2026smoothing 一致。Remark 4：ALM 与 perturbed ALM 的视角；带慢速移动中心的原始近端项不可缺少。
- **四行之前的衔接句**：“Each step uses the estimate produced by the level below it, so each iteration executes them from the innermost level outward:”
- **分析同样自顶向下**：「Iteration complexity analysis」开头一句把 `eq:b2-prime-decomposition` 的三项依次对应到 `lem:b2-prime-z-step-p`、`lem:b2-prime-fixed-center-contraction`（$\lambda$ 与 $x$ 合并处理）、`lem:b2-prime-center-error`。
- 任何改写都保持这个顺序，不把 $z$ 移到最前，不重新编号。

### 7.2 引言动机：精度与步长的权衡

两条文献线都因同一个矛盾停在 $\mathcal{O}(\epsilon^{-3})$：一个参数同时控制精度和步长，方向相反，平衡点在 $\epsilon^{-1}$。

- ALM：可行性误差不超过 $2L_h/\rho$，精度要求 $\rho$ 大；原始步长 $\eta\le 1/L_x(\rho)$ 且 $L_x(\rho)=\Theta(\rho)$，速度要求 $\rho$ 小；因此 $\rho=\Theta(\epsilon^{-1})$，得到 $\mathcal{O}(\epsilon^{-3})$（Lu ’22）。
- GDA 类（Li et al. ’26，arXiv:2602.14185）：对偶扰动 $1/s$ 使对偶梯度偏差 $\mathcal{O}(D_Y/s)$（§2.1），精度要求 $1/s$ 小；带扰动时中心步长可取 $\epsilon/(l D_Y)$，不带扰动的 Smoothed GDA 只能取 $\epsilon^2/(l D_Y^2)$（Remark 3.3(iii)），速度要求 $1/s$ 大；因此 $1/s=\Theta(\epsilon)$。
- 已核对的 $\kappa$ 形式：Lin et al. ’20 Thm 4.4（GDA，NC-SC）为 $\mathcal{O}(\kappa^2 l\Delta\epsilon^{-2})$；Yang et al. ’22（Smoothed AGDA，NC-PL）为 $\mathcal{O}(\kappa\epsilon^{-2})$。用 $\kappa=ls$ 改写 Li ’26 是本文的改写，原文没有这样写。
- 写法：两边各陈述事实再给平衡点，不写 “must”（必要性由本文定理给出）。

### 7.3 Pan–Zheng–Li v2（arXiv:2609.14235v2）

- 光滑 NC-C、紧对偶域、任意确定性一阶算法：OS 度量 Thm 3.1（下界）与 Thm 3.3（Tracked-FOAM 上界），主项 $\ell^2 D_Y\Delta\epsilon^{-3}$；GS 度量 Thm 3.2（下界）与 Thm 3.4（上界），主项为 $\epsilon^{-5/2}$ 阶。
- 本地 `memory/literature/complexity_2026-09_to_2026-10-03/raw/2609.14235v1.txt` 是 v1，只有 OS 下界；不能据此得出「没有 GS 下界」。
- 其他已核对事实：Li et al. NeurIPS 2021 只给 NC-SC 下界，没有算法；Lin–Jin–Jordan 的 NC-C GS 为 $\mathcal{O}(\epsilon^{-5/2}\log^2(1/\epsilon))$（Cor. 13）；Li–Nagarajan–Pan–Zhang 的 Perturbed Smoothed FOAM 带 $\log(1/\epsilon)$。
- 声称 $\epsilon^{-5/2}$ 最优时引 v2 并写定理号；NC-C 下界能否迁移到问题 (P) 是另一个问题。

### 7.4 第 5 节实验的实例判据（2026-11-22）

实例只需属于问题类 $\mathcal{I}(C,\Delta)$：$h$ 凸且 Lipschitz，$f$ 和 $\mathcal{A}$ 的梯度和 Jacobian 全局 Lipschitz 且有界，$\Delta$ 有限。老大原话「只要在我们问题类里就行」。不因展示效果排除实例；Jacobian 关于 $x$ 无界的 phase retrieval 不满足。

### 7.5 后续研究线（2026-10-25）

完整计划在 `memory/notes/project/next-lines-plan-20261025.md`。

- 线 1（先投 COLT 2027，之后加随机版本和 Cooper 实验投 NeurIPS）：固定 $\rho$、$s=c/\epsilon$，单步 ALM 达到 $\epsilon^{-5/2}$ 时外推（PDHG 型对偶步）是否充分且必要。
- 线 2（期刊，与 Radu Ioan Boț 合作）：把 $1/s_k\to 0$ 看作逐渐消失的 Tikhonov 对偶正则，研究最小范数乘子和 $s_k$ 的增长律。Boț 关注渐近性和单调包含，老大关注复杂度。
- 范围：问题类、结论、对比文献和读者都按 ALM 和约束优化定位；minimax、GDA 和单调算子作为分析工具使用。单独的 $\epsilon^{-5/2}$ 不构成新意（Li et al. AISTATS 2021、Zhang–Xu 2026 已有）。

### 7.6 minmax 论文全文位置

- `memory/literature/minmax_papers/` 有 7 篇全文 txt，来自 Zotero 的 minmax 集合，文件名含 Zotero key：Lin–Jin–Jordan COLT 2020、Ke–Mei–Zhang 2026、Zhang et al. UAI 2021、Li–Tian–Zhang–Jadbabaie NeurIPS 2021、Pan–Zheng–Li 2026、Zhang–Xu 2026、Li–Nagarajan–Pan–Zhang 2026。
- 含附录的全文在 `memory/literature/readings/`：`arxiv-2210.09382/`（Mah22，紧性证明在 A.3、B.3、C）和 `arxiv-2609.14233/`（Wu–Gu–Yang，hard instance 在 §3，性质证明在 A.3–A.5）。
- Zotero 接口取到的全文只有前约 10 页，以这些 txt 为准。按需 grep 定位后读相关行段，不整篇载入。
