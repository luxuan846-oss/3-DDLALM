# 2026 年论文查新报告（LRALM 族、族内紧复杂度与 Fast LRALM）

- **查新日期**：2026-11-22
- **检索时间窗**：2026-01 至 2026-11（另单列 10 篇 2025 年底或更早初版、2026 年修订或见刊的边界时间候选）
- **待查新本文**：LRALM 族 $\mathcal{C}_\theta$、族内紧复杂度与 Fast LRALM（`overleaf/sections/Preliminaries.tex`、`LRALMFamily.tex`、`Acceleration.tex`）
- **终审依据**：Claude Opus 5.5 原文终审（`stage3/opus-final-verdict.md`）

## 核心结论

**2026-01 至 2026-11 期间不存在撞车论文。** 本次合并去重后共获 48 篇 2026 主候选（46 篇可读全文，2 篇因付费墙无法读取而未评级）与 10 篇边界时间候选（全部可读）；经双模型独立全文核对及 Opus 5.5 原文终审，56 篇已读全文中撞车为 0 篇。2026 主范围内最接近的 3 篇均属「部分重合」，按接近度排序如下：**`C14`**（Zhang–Zhang–Xu–Dai，经本文约化 AL 函数 $\mathcal{D}_\rho$ 转化并令 $\sigma=0$ 可推得确定性单循环 $O(\epsilon^{-5/2})$，但原文仅陈述随机 $O(\epsilon^{-5})$，且采用每步三次梯度评估的投影阻尼 extragradient 加 normal-cone 修正，无 ALM 罚参数）、**`C06`**（Ke–Mei–Zhang，在本文完整问题类加最优解存在性下显式给出确定性 $O(\epsilon^{-5/2})$，但采用五层嵌套近端点求解器，无 ALM 框架）与 **`C07`**（Zhu–Ding–Liu–So，固定罚参数单循环线性化、移动原始中心加零中心对偶扰动得 $O(\epsilon^{-3})$，但仅限 Stiefel 正交等式约束，对偶中心固定在 $\mathbf{0}$，无有效罚参数 $\rho+s$ 机制，无相变与匹配下界）。Opus 5.5 直读本文 `Preliminaries.tex` 确认，`Assumption \ref{ass:h}`（编号 2.2）规定 $h\colon\mathbb{R}^m\to\mathbb{R}$ 为有限值凸且 $L_h$-Lipschitz 函数，对偶域 $\operatorname{dom} h^*\subseteq B(0,L_h)$ 有界，本文问题类不含 indicator 与等式约束 $c(x)=0$。据此，**创新点 1 与创新点 2 保持新颖**；**创新点 3 的 $O(\epsilon^{-5/2})$ 速率在本文完整问题类上已有先例**（`C06` 显式多层、`C14` 经 $\mathcal{D}_\rho$ 退化单循环、已引种子文献 Zhang–Xu `arXiv:2609.17973` 单循环）。正文不主张「首个 $O(\epsilon^{-5/2})$」。创新点 3 的贡献定位在算法结构与分析简洁性：固定罚参数 $\rho$ 的 ALM 单步梯度更新加乘子 Nesterov 外推，单循环，无 extragradient 预测步，无内层求解器。

### 本文核定设定与最终分档统计

1. **本文真实设定**：`Assumption \ref{ass:h}` 要求 $h$ 为有限值凸且 $L_h$-Lipschitz，故 $\operatorname{dom} h^*\subseteq B(0,L_h)$ 有界，不含 indicator；`Assumption \ref{ass:smoothness}` 要求 $\nabla f$ 与 $J_{\mathcal{A}}$ 全局有界（常数 $G_f$ 与 $G_{\mathcal{A}}$）；问题类 $\mathcal{I}(\mathbf{C},\Delta)$ 见 `Definition \ref{def:problem-class}`；oracle 为确定性一阶 oracle 加精确 $\operatorname{prox}_{th}$（`Definition \ref{def:oracle-model}`）；度量为 `Definition \ref{def:eps-kkt}` 的 $\epsilon$-KKT 残差。Fast LRALM（`Algorithm \ref{alg:b2-prime}`）以 $\mathbf{0}$ 为中心施加强度 $1/s$ 的对偶正则，取 $s=c_s/\epsilon$、中心步长 $\alpha=c_\alpha/\sqrt{\kappa}=\Theta(\epsilon^{1/2})$、乘子 Nesterov 外推系数 $\omega=(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$，`thm:b2-prime-complexity` 给出 $O(\epsilon^{-5/2})$ 迭代复杂度。
2. **正文定位校正**：阶段 2 以「不覆盖无界对偶域 indicator」区分 `C06` 与 `C14` 对本文无效；「无对偶投影」区分力弱（向球 $B(0,2L_h)$ 的投影具闭式解）。Related Work 需正面列出 `C06`、`C14`、Zhang–Xu（`arXiv:2609.17973`）以及 `C01`、`C05`、`C07`。
3. **主范围之外需留意的近邻**：
   - **Zhang–Xu（`arXiv:2609.17973`，已引种子文献）**：已在 $\mathcal{D}_\rho$ 上（对偶球半径 $2L_h$）给出确定性单循环 $O(\epsilon^{-5/2})$，是创新点 3 的真实最近邻；`C14` 为同课题组随机推广。
   - **Kong–Monteiro（2024）**：乘子阻尼中心在 $\mathbf{0}$，给出 $O(\epsilon^{-3})$，为族内 $\beta=0$ 成员的最近先例；创新点 2 的新意在于紧性与下界。
   - **`B10`（Maia–Gutman–Monteiro–Silva，*Math. Program.* 2026）**：FP-ADMM 在固定 $c=\Theta(\eta^{-1})$ 下，因初值可行性不同呈现 $\epsilon^{-4}$ 与 $\epsilon^{-3}$ 两档（`Theorem 3.2` 后讨论）；本文正文需写明相变源于 $(\rho+s)$ 尺度与中心步长，与初值可行性无关。
   - **`B08`（Zhou et al.，*IEEE TAC* 2026）**：线性约束加零中心对偶阻尼；其 `Theorem 1` 第二部分证明存在参数尺度缺陷，引用时仅引第一部分 $\epsilon$-AKKT 结论。
   - **`B09`（Deng et al.，*SIAM Rev.* 2026）**：`Table 2` 与 §6.3 对 IAIPAL（文献 `[136]`）复杂度记载矛盾，引用 IAIPAL 以原文为准。

| 候选集合 | 篇数 | 撞车 | 部分重合 | 相关 | 无关（排除） | 不可读 |
|---|---:|---:|---:|---:|---:|---:|
| **2026-01 至 2026-11 主候选（`C01`–`C46` 可读全文）** | 46 | **0** | **3**（`C14`, `C06`, `C07`） | **30** | **13** | — |
| 主候选不可读（`C47`, `C48`） | 2 | — | — | — | — | **2** |
| **边界时间候选（`B01`–`B10`）** | 10 | **0** | **0** | **8** | **2**（`B01`, `B07`） | 0 |

---

## 一、撞车（0 篇）

无。

---

## 二、部分重合（3 篇）

按与本文接近度从高到低排序。

### 1. `[C14]` Single-Loop Stochastic Projected Damped Extragradient Methods for Nonconvex–(Strongly) Concave Minimax Optimization

- **作者**：Huiling Zhang, Minhao Zhang, Zi Xu, Yu-Hong Dai
- **年份与出处**：2026（2026-09-18，v2 2026-10-12），`arXiv:2609.21747v2`（`math.OC`）
- **链接**：<https://arxiv.org/abs/2609.21747>
- **问题设定四项差异**：
  1. **约束**：原文为紧凸对偶域 $Y$ 上的光滑 NC-C 极小极大，无显式约束；借由本文 $\mathcal{D}_\rho$ 并取 $Y=B(0,2L_h)$ 可覆盖本文非线性复合问题类，原文无此陈述。
  2. **$h$ 结构**：无 indicator 型 $h$；直接 Fenchel 转化仅覆盖 support function，经 $\mathcal{D}_\rho$ 转化可覆盖全部 $L_h$-Lipschitz 凸 $h$。
  3. **内层求解器**：无，单循环，每步三次梯度评估。
  4. **罚参数**：无 AL 罚参数；采用以 $\mathbf{0}$ 为中心的对偶 Tikhonov 正则 $\tau=\min\{L,\epsilon/(2D_Y)\}$（对应 $1/s=\Theta(\epsilon)$）、移动原始中心步长 $\beta=\Theta(\epsilon^{1/2})$、对偶动量与每步投影到 $Y$；无 CQ。
- **重合创新点**：创新点 3
- **结论原文位置**：`Assumptions 1–2`、`Algorithm 1`、`(7)`、`Theorem 3` 式 `(94)–(96)`、`Remark 2`
- **差异要点**：原文显式结论为随机 $O(\epsilon^{-5})$（`Remark 2`），输出为随机下标；令 $\sigma=0$ 由 `Theorem 3` 式 `(95)–(96)` 可推得确定性单循环 $O(\epsilon^{-5/2})$（确定性选点需逐步算残差，阶不变）。更新形式为 projected damped extragradient 加 normal-cone 修正，每步三次梯度评估并带对偶投影；本文为固定 $\rho$ 的 ALM 一次梯度步加乘子 Nesterov 外推，无投影。无下界。其确定性版本已由同课题组种子文献 Zhang–Xu（`arXiv:2609.17973`）给出。

### 2. `[C06]` Efficient Parameter-Free First-Order Methods for Nonsmooth Composite Minimax Optimization

- **作者**：Shaozhe Ke, Sanyou Mei, Jiheng Zhang
- **年份与出处**：2026（2026-09-22），`arXiv:2609.25752v1`（`math.OC`）
- **链接**：<https://arxiv.org/abs/2609.25752>
- **问题设定四项差异**：
  1. **约束**：复合 NC-C 极小极大 $\min\max\{h(x,y)+p(x)-q(y)\}$（对 $x$ 取极小、对 $y$ 取极大），取 $H(x,y)=f(x)+\langle\mathcal{A}(x),y\rangle$、$p=0$、$q=h^*$ 覆盖本文完整问题类。
  2. **$h$ 结构**：$p$ 与 $q$ 为一般凸函数，要求 $\operatorname{dom} q$ 有界（`Assumption 1(ii)`），不含无界对偶域 indicator；本文 `Assumption \ref{ass:h}` 下自动满足，$\operatorname{prox}_q$ 由 Moreau 恒等式经一次 $\operatorname{prox}_h$ 得到。
  3. **内层求解器**：需要，五层嵌套：`Algorithm 5`（半径倍增）调用 `Algorithm 4`（非精确近端点 trial），再调用 `Algorithm 2`（累积正则）、`Algorithm 1`（加速非精确近端），最内层为单调包含子求解器 $\mathcal{A}$（EAG 或 past-EAG，`Remark 2`）。
  4. **罚参数**：无 ALM 罚参数；对偶正则 $\mu=\epsilon/(32D)$ 固定，对偶中心固定在 $y^0$，原始中心 $x^t$ 在接受 trial 后更新；无 CQ，额外要求最优解存在（`Assumption 1(iv)`）。
- **重合创新点**：创新点 3
- **结论原文位置**：`Assumption 1`、`Definition 1`、`Assumption 3`、`Remark 2`、`Algorithms 1, 2, 4, 5`、`Theorems 4–5`、`Remark 8`
- **差异要点**：在本文完整问题类（加最优解存在性）上显式给出确定性、无对数因子的 $O(\epsilon^{-5/2})$，参数无关且具可验证终止准则；与本文的区分在算法结构（五层嵌套近端点对固定 $\rho$ 单循环 ALM 加 Nesterov 外推）。无下界。

### 3. `[C07]` Primal-Dual Methods for Nonsmooth Nonconvex Optimization with Orthogonality Constraints

- **作者**：Linglingzhi Zhu, Wentao Ding, Shangyuan Liu, Anthony Man-Cho So
- **年份与出处**：2026（2026-04-05），`arXiv:2604.04130v1`（`math.OC`）
- **链接**：<https://arxiv.org/abs/2604.04130>
- **问题设定四项差异**：
  1. **约束**：Stiefel 正交非线性等式约束 $X^\top X=I_n$，位于本文问题类之外。
  2. **$h$ 结构**：是，约束为 indicator $\delta_{\{0\}}$，另有作用在 $X$ 上的弱凸项 $g$。
  3. **内层求解器**：当组合项 $g+\iota_{\mathcal{X}}$ 的近端映射可算时无内层求解器（`Remarks 3.6–3.7`）。
  4. **罚参数**：固定且充分大（`Proposition 4.7`）；利用 Stiefel 约束在可行集邻域自带的局部一致 CQ（`Remark 4.6`），要求可行初值（`Algorithm 1`、`Remark 3.7(iii)`）、紧原始集 $\mathcal{X}$（`Assumption 3.5`）与紧对偶集 $\mathcal{Y}$ 投影（`Assumption 3.4`）。
- **重合创新点**：创新点 1, 2
- **结论原文位置**：`Assumptions 3.2, 3.4, 3.5`、`Algorithm 1`、`Remarks 3.6–3.7`、`Remark 4.6`、`Proposition 4.7`、`Theorem 4.10`
- **差异要点**：对偶扰动 $\varepsilon=O(K^{-1/3})$（对应 $s=\Theta(\epsilon^{-1})$）与中心步长 $\beta=O(K^{-1/3})$（对应临界中心步长 $\Theta(\epsilon)$）给出一阶 $O(\epsilon^{-3})$ 上界；但对偶中心固定在 $\mathbf{0}$，无有效罚参数 $\rho+s$ 抬高机制，仅有上界而无 $\Theta(\epsilon^{-4})$ 分支、无相变、无匹配下界，也无 $O(\epsilon^{-5/2})$ 加速。

---

## 三、相关（30 篇）

下表涵盖全部 30 篇 2026-01 至 2026-11 可读全文「相关」论文。四项设定差异依次为：① 约束线性或非线性；② $h$ 是否为 indicator；③ 是否需要内层求解器；④ 罚参数是否固定（及附加假设）。

| ID | 标题 | 作者 | 年份 / 出处 / 链接 | ① 约束 | ② $h$ 与 indicator | ③ 内层求解器 | ④ 罚参数与附加假设 | 重合创新点 | 原文位置 |
|---|---|---|---|---|---|---|---|---|---|
| C01 | Nonconvex Composite Functional Constraints via First-Order Augmented Lagrangian Methods under Local Regularity | Linglingzhi Zhu, Jiajin Li | 2026-07-09（v2 10-14），[arXiv:2607.08954](https://arxiv.org/abs/2607.08954) | 非线性复合函数不等式，紧凸集 | 外函数有限值凸 Lipschitz；可行性为 indicator | 需要（精确复合子问题，凸分裂求解；仅计外层步数） | 固定充分大；局部正则、可行初值、截断对偶投影、零中心对偶正则 | 1, 2 | Alg 1, Remark 3.1, Ass 2.2, Prop 4.6, Thm 4.1, Remarks 4.3–4.4 |
| C05 | A Fixed-Penalty Linearized Augmented Lagrangian Method with Classical Multiplier Updates | Benqi Liu, Kangkang Deng, Zichen Wang, Zaiwen Wen | 2026-08-20，[arXiv:2608.19847](https://arxiv.org/abs/2608.19847) | 光滑非线性等式 | 是 | 无非线性子问题，每步一次 SPD 线性方程组 | 固定，与精度无关；uniform LICQ、小初始残差；无对偶正则与中心 | 1 | Alg 2.1, Ass 2.1/2.3/2.5, Thm 2.12 |
| C02 | ALDER: A Single-Loop Augmented-Lagrangian Damped Extragradient Method for Nonconvex–Concave Minimax Problems with Nonlinear Coupled Constraints | Huiling Zhang, Minhao Zhang, Zi Xu, Yu-Hong Dai | 2026-10-31，[arXiv:2611.00691](https://arxiv.org/abs/2611.00691) | 极小极大内层非线性耦合不等式 | 无一般复合项，集合约束为 indicator | 无，单循环 | 运行内固定，取 $\Theta(\epsilon^{-1})$；扩展 MFCQ、可行初值 | 1 | Alg 1, Lemma 5, Thms 16–17 |
| C40 | Improved Analysis of Restarted Accelerated Gradient and Augmented Lagrangian Methods via Inexact Proximal Point Frameworks | Matthew X. Burns, Jiaming Liang | 2026-02-19，[arXiv:2602.17878](https://arxiv.org/abs/2602.17878) | 线性等式，凸复合 | 是 | 需要（ACG） | I-FALM 固定 $\rho$，零中心对偶正则加外层对偶加速 | 1, 3 | Alg 3–4, Thm 3.1, 3.4, Cor 3.2, 3.5 |
| C33 | Augmented Lagrangian methods with Nesterov acceleration for convex optimization with nonlinear inequality constraints | Xin He | 2026-11-15，[arXiv:2611.20134](https://arxiv.org/abs/2611.20134) | 凸非线性不等式 | 是 | 需要（FISTA 类） | 递增，PHR 等效罚 $\Theta(k^2)$ | 3 | Alg 1, Remarks 2.1–2.2, Thms 3.1, 3.4 |
| C39 | Accelerated Implicit GDA Schemes: Theoretical Guarantees and Application to Proximal Augmented Lagrangian Methods | Jiaqi Liu, Bin Shi | 2026-06-10，[arXiv:2606.11800](https://arxiv.org/abs/2606.11800) | 线性等式（凸） | 是 | 隐式版需解子问题，另有显式变体 | 随步长变化；外层 Nesterov 加速 | 3 | Thms 2.2, 3.2, 4.2 |
| C36 | A Momentum-based Stochastic Algorithm for Linearly Constrained Nonconvex Optimization | Chenyang Qiu, Mihitha Maithripala, Zongli Lin | 2026-04-14，[arXiv:2604.13272](https://arxiv.org/abs/2604.13272) | 线性等式 $Ax=b$，随机目标 | 是 | 无，单循环 | 运行内固定，$\beta=\Theta(\epsilon^{-2})$；式 `(22)` 隐含近可行初值 | 1 | Alg 1, Lemma 7, 式 (22), Thm 1 |
| C04 | Lower Bounds for Feasibility and Stationarity in First-Order Nonconvex Constrained Optimization | Qiankun Shi, Xiao Wang | 2026-06-28，[OptOnline ?p=35411](https://optimization-online.org/?p=35411) | 光滑非线性等式 | 是 | 下界针对一般一阶算法类 | 下界不指定罚参数 | 2 | Defs 1–4, Thms 1–5, Cor 1 |
| C11 | Optimal Oracle Complexity for Weakly Convex Optimization | Jiajin Li, Siyu Pan | 2026-08-04（v3 11-13），[arXiv:2608.03246](https://arxiv.org/abs/2608.03246) | 无约束弱凸 Lipschitz（含本文 $F$） | 无复合分解 | 下界针对 oracle 算法类 | 无罚参数；oracle 不含 prox | 2 | Def 2.3, Thm 3.1, Lemma 3.2, Prop 3.3 |
| C21 | Complexity of quadratic penalty methods with adaptive accuracy under a PL condition for the constraints | Florentin Goyens, Geovani N. Grapiglia | 2026-01-05，[arXiv:2601.02134](https://arxiv.org/abs/2601.02134) | 光滑非线性等式 | 是 | 需要（一阶或二阶内层） | 几何递增，预选 $\beta_0$ 可消对数；约束 PŁ 产生 $\epsilon^{-4}$ 与 $\epsilon^{-3}$ 分界 | 2（机制对照） | Thms 5.3–5.4, 6.3–6.4 |
| C24 | Lower Bounds for Nonconvex-PŁ Minimax Optimization | Siyu Pan, Jiajin Li | 2026-08-27，[arXiv:2608.26799](https://arxiv.org/abs/2608.26799) | 无约束光滑极小极大，对偶 PŁ | 无 | 下界针对任意确定性一阶方法 | 无罚参数；说明 $\sqrt{\kappa}$ 加速依赖对偶强凹 | 3 | Thms 3.1–3.2 |
| C08 | Envelopt: Constrained Convex Composite Optimization | Alberto De Marchi, Dominique Orban | 2026-08-25，[arXiv:2609.29521](https://arxiv.org/abs/2609.29521) | 一般复合 $f+h(c(x))$，可加 $c(x)\in C$ | 一般 proper lsc 凸，含 indicator | 需要（外部光滑约束求解器） | envelope 参数自适应；仅外层步数与渐近平稳性 | 无 | Alg 4.1, Thms 4.1, 4.4–4.6 |
| C03 | First-order smoothed exact-penalty methods for equality-constrained regularized nonconvex optimization | Shiji Zuo, Qihang Lin, Wei Liu, Yangyang Xu | 2026-11-15，[arXiv:2611.19887](https://arxiv.org/abs/2611.19887) | 非线性等式加凸正则 | 是 | 需要（APG 或对偶割平面） | exact penalty 自适应有界 | 无 | Alg 3.1, 4.1, B.1, Thms 3.5, 4.2, 4.7 |
| C09 | An Adaptive Augmented Lagrangian Method for Deterministic and Stochastic Nonconvex Optimization | Tianzhu Liu, Michael J. O'Neill | 2026-08-27，[arXiv:2608.27676](https://arxiv.org/abs/2608.27676) | 非线性等式加凸正则 | 是 | 需要（双循环） | 残差触发几何增长 | 无 | Alg 1–2, Thms 5.3, 5.8, 5.13 |
| C10 | A smoothing extended sequential quadratic method for difference-of-convex optimization over a convex composite inequality constraint | Jiefeng Xu, Ting Kei Pong, Yongle Zhang | 2026-06-11，[arXiv:2606.13343](https://arxiv.org/abs/2606.13343) | 单个凸复合不等式，DC 目标 | $h$ 有限值凸 Lipschitz，集合用 indicator | 无嵌套，每步 prox 加回溯 | 自适应，最终为常数 | 无 | Alg 1, Thms 3.1–3.2, Cor 3.1, Thms 4.1–4.2 |
| C12 | A Proximal Augmented Lagrangian Method Based on Quadratic Approximations for Weakly Convex Optimization | Yule Zhang, Benqi Liu, Xiantao Xiao, Liwei Zhang | 2026-05-05，[arXiv:2605.03415](https://arxiv.org/abs/2605.03415) | 光滑弱凸不等式 | 是 | 需要（强凸二次约束子问题） | 运行内固定；隐含条件 `(B5)`，带符号均值界，未平方精度 $O(\epsilon^{-6})$ | 无 | Thm 3.2, Lemma 2.6, (B5) |
| C13 | A Single-Loop Penalty-based Algorithm for Stochastic Minimax Optimization with Nonlinear Coupled Constraints | Qichao Cao, Shangzhi Zeng, Jin Zhang, Yuxuan Zhou | 2026-05-02（v3 06-08），[arXiv:2605.01246](https://arxiv.org/abs/2605.01246) | 极小极大内层非线性耦合不等式 | 是 | 无，单循环 | 二次罚递增至无穷，无乘子；GPLCQ | 无 | Alg 1, Remark 3.16, Thms 4.10–4.11 |
| C15 | MoSSP: A Momentum-Based Single-Loop Stochastic Penalty Method for Nonconvex Constrained DC-Regularized Optimization | Luxuan Li, Chunfeng Cui, Xiao Wang | 2026-05-28，ICML 2026，[arXiv:2605.29635](https://arxiv.org/abs/2605.29635) | 确定性非线性等式，随机 DC 目标 | 是 | 无，单循环 | 运行内固定，随预算增长；近可行初值、`Ass 2.3`（作者 Luxuan Li 与本文研究者同名，按自引处理） | 无 | Thms 3.1–3.2, Cors 3.1–3.2, Remark 3.2 |
| C16 | A Fletcher's Augmented Lagrangian-Based Stochastic First-Order Method for Nonconvex Equality-Constrained Optimization | Yawen Cui, Qiankun Shi, Xiao Wang, Xiantao Xiao | 2026-06-26，[arXiv:2606.28230](https://arxiv.org/abs/2606.28230) | 随机非线性等式 | 是 | 单循环，含线性代数求解 | Fletcher 参数自适应有界 | 无 | Alg 2.1, Thms 4.1–4.2 |
| C18 | Primal-Dual Halpern-PAGE Algorithm for Constrained Stochastic Weakly Convex Optimization（v2 已撤稿） | Lixin Tang, Xingyu Wang, Liwei Zhang | 2026-06-24 v1（08-10 v2 撤稿），[arXiv:2606.25355v1](https://arxiv.org/abs/2606.25355v1) | 随机混合约束 | 是 | 单循环，原始与对偶投影 | 无 AL 罚，乘子盒约束；v1 式 `(3.12)` 证明有缺陷，已撤稿不构成有效在先文献 | 无 | Lemma 3.2 式 (3.12), Thm 3.1, Cor 3.1 |
| C19 | Elastically safeguarded augmented Lagrangian methods | Ernesto G. Birgin, Alberto De Marchi, Patrick Mehlitz | 2026-07-02，[arXiv:2607.02697](https://arxiv.org/abs/2607.02697) | 非线性等式与不等式 | 是 | 需要（双层） | 自适应 safeguard | 无 | Alg 2.2, Thms 3.3, 3.6, 4.1, 4.2 |
| C20 | Proximal-Linearized NEP Method for Composite Optimization with Set-Inclusion and Manifold Constraints | Hao He, Ruyu Liu, Shaohua Pan | 2026-09-13（v3 10-26），[arXiv:2609.14564](https://arxiv.org/abs/2609.14564) | 集合包含与流形约束，DC 目标 | 是 | 需要（双层与步长接受检验） | exact penalty 自适应 | 无 | Alg 1, Thms 4.1–4.3, Cors 4.1–4.3, Thms 5.1–5.2 |
| C25 | Prox-PEP: A Proximal Partial Exact Penalty Algorithm for Weakly Convex Stochastic Nonlinear Programming | Lixin Tang, Xingyu Wang, Liwei Zhang | 2026-05-08，[arXiv:2605.07165](https://arxiv.org/abs/2605.07165) | 非线性等式与不等式，随机弱凸 | 是，另有 slack 罚 | 每次抽样解联合子问题 | 等式 exact penalty 先增后固定；未平方梯度 $O(\epsilon^{-8})$，带符号均值 | 无 | Thm 3.2 式 (3.38)–(3.41) |
| C26 | First-Order Methods for Solving Convex (Strongly) Concave Minimax Problems with Functional Constraints | Yangyang Xu, Xinhao Ying | 2026-06-17，[arXiv:2606.19050](https://arxiv.org/abs/2606.19050) | 两侧凸函数不等式（凸-凹） | 加性凸项一般 | 需要（iAPG 与辅助最大化） | 一侧几何增长，一侧固定；经典 Rockafellar 近端 ALM | 无 | 式 (2.3)–(2.4), Alg 1–2, Thms 3.6, 3.8–3.10 |
| C30 | A Proximal Approach for Nonsmooth Composite-Constrained Optimization | Wim van Ackooij, Yi Chu, Welington de Oliveira, Pedro Pérez-Aros | 2026-09-11，[OptOnline ?p=36714](https://optimization-online.org/?p=36714) | 非光滑复合不等式加闭集 | 可行性为 indicator | 需要（每次 trial 解 master problem） | improvement function 权重固定 | 无 | Alg 1, Ass 1, Thm 8 |
| C31 | A Parallel Adaptive Proximal ADMM for Linearly Constrained Separable Composite Optimization Problems | Leandro F. Maia, Renato D. C. Monteiro, Gilson N. Silva | 2026-10-31，[arXiv:2611.00570](https://arxiv.org/abs/2611.00570) | 多块线性等式 | 是 | 多 stage 并行块迭代 | 每 stage 倍增，得 $O(\epsilon^{-3})$，无下界 | 无 | Thm 3.2, Cor 3.3 |
| C32 | A Bregman proximal linearized ADMM for fractional programming with nonlinear coupling constraints | Pengjie Liu, Jinhu Chen, Minh N. Dao, Hu Shao, Jinbao Jian | 2026-10-08，[arXiv:2610.11961](https://arxiv.org/abs/2610.11961) | 非线性耦合等式，分式目标 | 是 | 每轮两个 argmin | 固定超阈值；满列秩，无 $\epsilon$ 阶复杂度 | 无 | Alg 3.1, Ass 3.2(vi), Thms 3.13, 3.14, 3.18 |
| C34 | Optimal Nonergodic Primal-Dual Complexity of Efficient Inexact Parameter-Free Augmented Lagrangian Methods | Arnesh Sujanani, Saeed Ghadimi, Henry Wołkowicz | 2026-08-04（v2 08-10），[arXiv:2608.03170](https://arxiv.org/abs/2608.03170) | 线性等式，凸复合 | 是 | 需要（加速内层） | $c=1/\hat\epsilon$ 或几何增长 | 无 | Thms 2.8, 2.13, 2.20, 3.5, 3.7 |
| C35 | A conditional-gradient-based single-loop augmented Lagrangian method for inequality constrained optimization | Xiaozhou Wang, Ting Kei Pong, Zev Woodstock | 2026-05-21，[arXiv:2605.22539](https://arxiv.org/abs/2605.22539) | 凸非线性不等式 | 加性项一般 | 无，单循环，每轮一次 LMO | 递增至无穷 | 无 | Alg 1, Thms 3.1–3.2, 4.1–4.2 |
| C46 | An augmented Lagrangian method with exact multipliers for non-separable composite $\ell_0$-$\ell_2$ regularization | Huan Ren, Guiyun Xiao | 2026-07-06，[arXiv:2607.05073](https://arxiv.org/abs/2607.05073) | 线性分裂等式 $Wu=y$ | 是，另有非凸 $\ell_0$ 项 | 交替精确子问题 | 固定，有下界要求；无复杂度界 | 无 | Alg 2.1–2.2, Thms 3.1–3.2, 3.11–3.12, 3.16 |

---

## 四、边界时间候选（`B01`–`B10`）与已核查排除项简表

以下两张附表均独立于 2026-01 至 2026-11 有效主清单。

### 4.1 边界时间候选（10 篇：相关 8 篇，无关排除 2 篇）

该组论文初版发布于 2025 年底或更早、2026 年修订或期刊见刊，全部已读全文，无撞车与部分重合。

| 等级 | ID | 标题 | 作者 | 日期 / 出处 / 链接 | ① 约束 | ② $h$ 与 indicator | ③ 内层求解器 | ④ 罚参数与附加假设 | 重合创新点 | 原文位置 |
|---|---|---|---|---|---|---|---|---|---|---|
| 相关 | B08 | Perturbed Proximal Gradient ADMM for Nonconvex Composite Optimization | Yuan Zhou, Xinli Shi, Luyao Guo, Jinde Cao, Mahmoud Abdel-Aty | v1 2025-04-17，*IEEE TAC* 2026-06-04，[arXiv:2504.12759](https://arxiv.org/abs/2504.12759) | 两块线性等式 | 是，各块可含弱凸项 | 无，单层两次 prox | 固定 $\rho$；KKT 分支取 $\beta=1/K$，证明不完整 | 1 | Alg 1, Ass 3 式 (37a)–(37e), Thm 1 式 (42)–(47) |
| 相关 | B10 | An adaptive proximal ADMM for nonconvex linearly constrained composite programs | Leandro F. Maia, David H. Gutman, Renato D. C. Monteiro, Gilson N. Silva | v1 2024-07-12，*Math. Program.* 2026-06-05，[arXiv:2407.09927](https://arxiv.org/abs/2407.09927) | 多块线性等式 | 是，$h$ 块可分凸 | 两个主循环，块内可调 solver | FP 固定 $c=\Theta(\eta^{-1})$，VP 与 Adapt 分阶段加倍 | 2（机制对照） | Algs 1–3, Thm 3.2, Thm 5.2, Thm 6.3 |
| 相关 | B02 | The Güler-type acceleration for proximal gradient, linearized augmented Lagrangian and linearized alternating direction method of multipliers | Bin Zhou, Liusheng Hou, Xingju Cai, Hailin Sun | 2025-11-21，[arXiv:2511.17157](https://arxiv.org/abs/2511.17157) | 线性等式（凸） | 是，$g$ 一般凸 | 每步二次复合 argmin，一般需内层求解 | 线性增长 $\kappa_k=\Theta(k)$ | 3 | Alg 2 式 (4.1), Thm 4.1 式 (4.10) |
| 相关 | B03 | Augmented Lagrangian methods for fully convex composite optimization | Alberto De Marchi, Tim Hoheisel, Patrick Mehlitz | v1 2025-11-10（v3 2026-10-06），[arXiv:2511.07117](https://arxiv.org/abs/2511.07117) | 允许非线性 $c$，整体凸 | $g$ 一般凸 | 需要（非精确极小化） | 固定、递增或按残差调整 | 无 | Algs 4.1, 5.1, 6.1, Thms 4.2, 4.4, 5.3, 5.8, 6.2, 6.3 |
| 相关 | B04 | A first-order method for nonconvex-strongly-concave constrained minimax optimization | Zhaosong Lu, Sanyou Mei | v1 2025-12-28，*Optim. Methods Softw.* 2026-01-02，[arXiv:2512.22909](https://arxiv.org/abs/2512.22909) | 两侧不等式，允许耦合 | $p,q$ 一般凸 | 需要（嵌套极小极大求解器） | 几何递增 | 无 | Algs 1–3, Thms 1–2 |
| 相关 | B05 | Adaptive directional decomposition methods for nonconvex constrained optimization | Qiankun Shi, Xiao Wang | 2025-11-05（v2 11-07），[arXiv:2511.03210](https://arxiv.org/abs/2511.03210) | 非线性等式与不等式 | 是 | 等式版投影方向，混合版每步两个 QP | 自适应 merit 参数；强 LICQ 特例 | 无 | 式 (18)–(19), Algs 1–3, Thms 1–7 |
| 相关 | B06 | A proximal augmented Lagrangian method for nonconvex optimization with equality and inequality constraints | Adeyemi D. Adeoye, Puya Latafat, Alberto Bemporad | v1 2025-09-03，*COAP* 2026-10-12，[arXiv:2509.02894](https://arxiv.org/abs/2509.02894) | 非线性等式与不等式 | 是，另有凸 $f_2$ | 需要（非精确近端 AL 子问题） | 按残差自适应增长；可行初值 | 无 | 式 (1.4), Algs 1–2, Thm 3.1, Cor 5.2 |
| 相关 | B09 | The Augmented Lagrangian Methods: Overview and Recent Advances | Kangkang Deng, Rui Wang, Zhenyuan Zhu, Junyu Zhang, Zaiwen Wen | v1 2025-10-19，*SIAM Rev.* 2026-08-06，[arXiv:2510.16827](https://arxiv.org/abs/2510.16827) | 多类模型 | 一般复合与 indicator 均讨论 | 依具体方法 | 固定与自适应均讨论 | 无 | Table 2, §6.1–6.3 |
| 排除 | B01 | A first-order method for constrained nonconvex-nonconcave minimax optimization | Zhaosong Lu, Xiangyuan Wang | v1 2025-10，*Math. Program.* 2026-08-25，[arXiv:2510.01168](https://arxiv.org/abs/2510.01168) | 最大化侧非线性不等式（NC-NC） | $p,q$ 一般凸 | 需要（SCP 内含回溯） | 无 AL 罚；局部 KL | 无 | Algs 1–2, Thms 1–7 |
| 排除 | B07 | A Minimization Approach for Minimax Optimization with Coupled Constraints | Xiaoyin Hu, Kim-Chuan Toh, Shiwei Wang, Nachuan Xiao | v1 2024-08-30，*SIOPT* 2026-05-06，[arXiv:2408.17213](https://arxiv.org/abs/2408.17213) | 强凹内层，耦合锥约束 | 锥约束，另有两个凸正则项 | 转化后单层迭代 | 固定 envelope 参数，无 AL 罚 | 无 | Props 4.4, Thms 3.14, 4.6, 4.7, 4.14 |

### 4.2 2026 主候选已核查无关（排除）项简表（13 篇）

| ID | 标题 | 作者 | 日期 / 出处 / 链接 | ① 约束 | ② $h$ 与 indicator | ③ 内层求解器 | ④ 罚参数 | 创新点 | 原文位置 | 排除理由 |
|---|---|---|---|---|---|---|---|---|---|---|
| C17 | Lower Bounds for Stochastic First-Order Algorithms with Variance Reduction in Nonconvex–Concave Minimax Optimization | Jiayi Song, Zi Xu | 2026-10-01（v2 11-01），[arXiv:2610.01662](https://arxiv.org/abs/2610.01662) | 极小极大域约束 | 只有域限制 | 下界，不限定循环 | 无 | 无 | Def 2.4, Thm 4.4, Thms 5.3, 5.7 | 随机方差缩减下界；确定性项借用已引种子文献 |
| C22 | Constraint Qualifications and Regularity Conditions for Nonlinear Constraint Systems | Shiji Zuo, Qihang Lin, Wei Liu, Yangyang Xu | 2026-10-31，[arXiv:2611.00526](https://arxiv.org/abs/2611.00526) | 非线性约束系统 | 只研究可行性 | 无算法 | 无 | 无 | Props 3.1–3.4, 3.6, 4.1 | 静态 CQ 性质 |
| C23 | Deterministic Oracle Complexity for Goldstein Stationarity in Nonsmooth Nonconvex Optimization with Constraints | Yixi Ding, Ya-xiang Yuan | 2026-11-04（v2 11-16），[arXiv:2611.06739](https://arxiv.org/abs/2611.06739) | 集合或凸函数约束 | 可写为 indicator | 下界，不限定循环 | 无 | 无 | Thms 3.1, 4.1, Cors 4.2, 4.7, Thm 5.1 | 非弱凸 Goldstein 平稳性 |
| C27 | Nonsmooth Nonconvex-Concave Minimax Optimization: Convergence Criteria and Algorithms | Jinyang Shi, Luo Luo | 2026-04-23，[arXiv:2604.21371](https://arxiv.org/abs/2604.21371) | 两个凸域 | 可写为 indicator | 主循环加子程序 | 无 | 无 | Algs 1–3, Thm 2, Cor 3, Thm 4, Cor 5 | 随机零阶 Goldstein 平稳性 |
| C28 | On the Convergence of Proximal Algorithms for Weakly-convex Min-max Optimization | Guido Tapia-Riera, Camille Castera, Nicolas Papadakis | 2026-03-30，[arXiv:2603.28484](https://arxiv.org/abs/2603.28484) | 无显式约束，弱凸-强凹 | 最大化侧一般凸正则 | 交替单循环 | 无 | 无 | Thm 3.2, Prop 3.3, Thms 4.1–4.2 | 天然强凹的无约束极小极大 |
| C29 | Obtaining Game-Stationary Points for Smooth Nonconvex-Nonconcave Minimax Problems via First-Order Methods | Mengxuan Dong, Yao Yao, Jiawei Zhang | 2026-09-26（v2 09-29），[arXiv:2609.32970](https://arxiv.org/abs/2609.32970) | 无约束 NC-NC | 无 | 外层 GD，内层 best response | 固定 gap 罚参数 | 无 | Algs 1–2, Thm 3.1, Thms 3.4–3.5, Cor 3.6 | NC-NC 局部正则，无 ALM |
| C37 | Accelerated primal-dual dynamical systems for convex optimization with nonlinear inequality constraints | Xin He | 2026-09-01（v3 11-09），[arXiv:2609.01415](https://arxiv.org/abs/2609.01415) | 凸非线性不等式 | 是 | 连续时间 | 固定 $\beta$ | 无 | Thm 2.2, Thms 3.1, 3.4 | 连续时间 ODE，无离散复杂度 |
| C38 | Restarted Reflected Halpern Acceleration for Augmented Primal-Dual Methods | Benqi Liu, Ju Cao, Wotao Yin, Zaiwen Wen | 2026-06-15，[arXiv:2606.16552](https://arxiv.org/abs/2606.16552) | 线性等式（凸） | 是 | 精确或线性化映射，可加重启外循环 | 固定 $\sigma\ge0$ | 无 | Algs 1–3, Thms 1–7 | 纯凸单调算子 Halpern 框架 |
| C41 | A Nesterov-Accelerated Primal-Dual Splitting Algorithm for Convex Nonsmooth Optimization | Laurent Condat, Abdurakhmon Sadiev, Peter Richtárik | 2026-04-10，[OptOnline ?p=34422](https://optimization-online.org/?p=34422) | 线性算子复合（凸） | 一般 $h$，含 indicator | 无，单循环分裂 | 无 ALM 罚 | 无 | Alg 1, Thms 3.1, 3.3, 3.8, 3.11 | 纯凸原始-对偶分裂，无 ALM 罚项，需强凸 |
| C42 | Matching Randomized Bounds for Finite-Sum Nonconvex-Concave Optimization | Wendao Wu, Haihan Zhang, Qian Chen, Chenheng Zhang, Chunyuan Zheng, Cong Fang, Haoxuan Li, Zhouchen Lin | 2026-10-12，[arXiv:2610.16991](https://arxiv.org/abs/2610.16991) | 紧对偶域 | 可写为 indicator | 多循环 | 无 | 无 | Alg 1, Thms 3.1–3.3 | 随机化有限和 oracle |
| C43 | On the Complexity of Finite-Sum Nonconvex-Strongly-Concave Minimax Optimization with Exact Proximal Oracles | Yuxing Peng, Zhiqing Tang, Weijia Jia | 2026-11-03（v2 11-14），[arXiv:2611.04806](https://arxiv.org/abs/2611.04806) | 无约束 | 无 | warm start 加 refinement | 无 | 无 | Thms 1–3, Cor 4 | 有限和、天然强凹 |
| C44 | How to Make the Gradient Mapping Small for Constrained Stochastic Min-Max Problems and Beyond | Ahmet Alacaoglu | 2026-09-08，[arXiv:2609.08380](https://arxiv.org/abs/2609.08380) | 凸-凹或单调包含 | 一般凸，可为 indicator | 多循环递归正则 | 无 | 无 | Algs 1–3, Thms 4.3, 4.5, 5.2 | 随机单调 VI |
| C45 | Feedback control of Lagrange multipliers for non-smooth constrained optimization | V. Cerone, S. M. Fosson, S. Pirrera, A. Re, D. Regruto | 2026-04-07（v2 05-02），[arXiv:2604.06511](https://arxiv.org/abs/2604.06511) | 一般模型含非线性等式，稳定性定理用仿射等式 | 是 | 连续时间反馈 | 固定 Moreau 参数 | 无 | Thms 1–3 | 强凸连续时间反馈，无非凸复杂度 |

---

## 五、阶段 2 分歧与阶段 3 终审裁决摘要

阶段 2 双模型（Gemini 4 Carbon High 与 GPT 6.2 Astra High）对 56 篇全文共产生 38 项分歧，Opus 5.5 逐篇直读 `papers/*.txt` 原文给出终审裁定，另按统一口径调整阶段 2 一致条目 `C21` 1 处（创新点由「无」调为 `2` 机制对照，等级不变）。

### 5.1 高优先级等级分歧：部分重合 vs 相关（3 篇）

| ID | Carbon | Astra | 原文核查核心依据 | 终审裁定 |
|---|---|---|---|---|
| C01 | 部分重合（1, 2） | 相关（1, 2） | `Remark 3.1` 写明速率仅计精确复合子问题外层步数，不匹配本文一阶 oracle 计量；另需 `Assumption 2.2` 局部正则、可行初值与截断对偶投影，对偶中心固定为 $\mathbf{0}$，无下界 | **相关（1, 2）** |
| C05 | 相关（1） | 部分重合（1） | 光滑等式 $h=\delta_{\{0\}}$ 在本文问题类之外；无对偶正则与移动中心；`Theorem 2.12` 的 $O(\epsilon^{-2})$ 依赖 `Assumption 2.1(iii)` uniform LICQ、小初始残差及每步 SPD 线性方程组求解 | **相关（1）** |
| C14 | 相关（1） | 部分重合（3） | `Assumption 2` 允许 $\sigma=0$，`Theorem 3` 式 `(94)–(96)` 在 $\sigma=0$ 时退化得 $m=1$ 与 $N=O(\epsilon^{-5/2})$；取 $F=\mathcal{D}_\rho$ 与 $Y=B(0,2L_h)$ 满足 `Assumption 1`，且 $\epsilon\lt L_h/\rho$ 时平稳点位于球内即本文 $\epsilon$-KKT 点 | **部分重合（3）**，第 1 名 |

`C14` 退化与 $\mathcal{D}_\rho$ 球内验证的关键关系（`Theorem 3` 式 `(95)–(96)`）：

$$
T=\max\Bigl\{1,\Bigl\lceil\frac{256LB}{\beta\epsilon^{2}}\Bigr\rceil\Bigr\},\qquad m=\max\Bigl\{1,\Bigl\lceil\frac{76800\sigma^{2}}{\beta\epsilon^{2}}\Bigr\rceil\Bigr\},\qquad \beta^{-1}=\Theta\bigl(\sqrt{K_\epsilon}\bigr),\qquad K_\epsilon=\max\Bigl\{1,\frac{2LD_Y}{\epsilon}\Bigr\},\qquad N\le 3mT.
$$

令 $\sigma=0$ 得 $m=1$ 与 $N=O(\epsilon^{-5/2})$；若 $\lVert\lambda\rVert=2L_h$ 且 $\epsilon\lt L_h/\rho$，则存在 $t\ge0$ 与 $\lVert e\rVert\le\epsilon$ 使 $q=\lambda+\rho(\mathcal{A}(x)-y)\in\partial h(y)$ 满足

$$
\lVert q\rVert\ge(1+\rho t)\,2L_h-\rho\epsilon\gt L_h,
$$

与 $\lVert q\rVert\le L_h$ 矛盾，故 $\lambda$ 必在球内。

### 5.2 边界归类分歧：相关 vs 无关（11 篇）

| ID | Carbon | Astra | 原文核查核心依据 | 终审裁定 |
|---|---|---|---|---|
| C11 | 相关（2） | 排除 | `Theorem 3.1` 给出弱凸 Lipschitz 类确定性/随机下界 $\Omega(\rho G^2\Delta/\epsilon^4)$；函数类含本文 $F$，oracle 无 prox，用于对照本文 $\Theta(\epsilon^{-4})$ 档 | **相关（2）** |
| C17 | 相关（2） | 排除 | `Theorems 4.4, 5.3, 5.7` 为随机方差缩减下界，确定性项借用已引种子文献 Zhang–Xu（2026） | **无关（排除）** |
| C24 | 相关（2） | 排除 | `Theorem 3.1` 给出确定性一阶 NC-PŁ 下界 $\Omega(\ell\Delta\kappa/\epsilon^2)$，对照 Fast LRALM 依赖对偶强凹取得 $\sqrt{\kappa}$ 加速 | **相关（3）** |
| C29 | 排除 | 相关 | 无约束光滑 NC-NC，依赖局部 inverse-Lipschitz 正则与内层 best response，无 ALM | **无关（排除）** |
| C37 | 排除 | 相关（3） | 凸不等式连续时间惯性原始-对偶 ODE，无离散 oracle 复杂度（离散版见 `C33`） | **无关（排除）** |
| C38 | 排除 | 相关（1, 3） | 纯凸单调算子 reflected Halpern 锚定框架，与非凸 LRALM 与乘子 Nesterov 外推无对应 | **无关（排除）** |
| C39 | 排除 | 相关（3） | 凸线性等式近端 ALM 等价于隐式 GDA，`Theorems 2.2, 3.2, 4.2` 给出 Nesterov 外层加速，与 `C33`/`C40`/`B02` 同谱系 | **相关（3）** |
| C41 | 排除 | 相关（3） | 纯凸原始-对偶分裂 APAPC，无 ALM 罚项且需 $g$ 强凸 | **无关（排除）** |
| C42 | 排除 | 相关（2, 3） | 随机化有限和 component oracle 复杂度；$n=1$ 退化为已引 Pan–Zheng–Li | **无关（排除）** |
| C45 | 排除 | 相关（1） | 强凸假设下的连续时间乘子反馈控制，无非凸复杂度 | **无关（排除）** |
| B01 | 相关 | 排除 | 约束 NC-NC 加局部 KL，多循环 SCP，无 ALM 罚项 | **无关（排除）** |

### 5.3 创新点归属分歧（12 篇，等级均为「相关」）

| ID | Carbon | Astra | 原文核查核心依据 | 终审创新点 |
|---|---|---|---|---|
| C13 | 1 | 无 | `Remark 3.16` 弃用 AL、`Theorem 4.11` 用递增二次罚 $\rho_k\to\infty$，无乘子 | **无** |
| C26 | 无 | 1 | 式 `(2.3)–(2.4)` 为经典 Rockafellar 近端 ALM，中心为上一迭代点，凸设定多循环 | **无** |
| C31 | 无 | 2 | 多块线性约束每 stage 罚参数倍增得 $O(\epsilon^{-3})$，无下界 | **无** |
| C32 | 无 | 1 | `Assumption 3.2(vi)` 满列秩固定罚线性化 ADMM，`Theorems 3.13, 3.14, 3.18` 无 $\epsilon$ 阶复杂度 | **无** |
| C34 | 无 | 2 | `Theorem 2.13` 取 $c=1/\hat\epsilon$ 属凸 ALM 标准尺度，与族内相变无关 | **无** |
| C35 | 无 | 1 | 凸不等式单循环 LMO，罚参数递增至无穷 | **无** |
| C40 | 3 | 1, 3 | `Algorithm 4` 与 `Theorem 3.4` 固定 $\rho=L_f/\lVert A\rVert^2$、零中心对偶正则加外层对偶加速，内层 ACG | **1, 3** |
| C46 | 无 | 1 | $\ell_0$-$\ell_2$ 特化问题，伪逆求精确乘子，无复杂度界 | **无** |
| B05 | 无 | 1 | 式 `(18)–(19)` 为强 LICQ 下的经典线性化 ALM 特例，无对偶正则与中心 | **无** |
| B06 | 无 | 1 | 式 `(1.4)` 仅含原始近端项，$-\frac{1}{2\nu}\lVert\mu\rVert^2$ 属 PHR 标准项（纠正 Carbon），罚参数自适应增长 | **无** |
| B09 | 无 | 1, 3 | 综述属背景文献；核实 `Table 2` 与 §6.3 对 IAIPAL `[136]` 记载存在 $O(\epsilon^{-3})$ 与 $O(\epsilon^{-5/2})$ 矛盾 | **无** |
| B10 | 无 | 2 | `Theorem 3.2` 后讨论：$c=\Theta(\eta^{-1})$ 时由初值可行性产生 $\epsilon^{-4}$ 与 $\epsilon^{-3}$ 分界，无下界 | **2（机制对照）** |

按同一口径，终审将 `C21` 的创新点由「无」调整为 **2（机制对照）**，等级保持「相关」。

### 5.4 技术细节、定理编号与证明缺陷出入（12 篇）

| ID | 争议点 | 原文核查裁定 | 终审等级与创新点 |
|---|---|---|---|
| C06 | 嵌套层级 | 实际调用链为 `Alg 5 → Alg 4 → Alg 2 → Alg 1 → 子求解器 A`（EAG / past-EAG）；`Alg 3` 为 SCSC 包装不在调用链中，纠正双方对 `Alg 2`/`Alg 3` 的误述；`Theorems 4–5` 给出确定性 $O(\epsilon^{-5/2})$ | 部分重合（3） |
| C07 | 单循环前提与步长 | `Remarks 3.6–3.7` 确认 $g+\iota_{\mathcal{X}}$ 近端映射可算时单循环；`Remark 4.6` 给出 Stiefel 局部一致 CQ；`Proposition 4.7` 要求罚参数充分大；`Theorem 4.10` 在 $\varepsilon=O(K^{-1/3})$ 与 $\beta=O(K^{-1/3})$ 下得 $O(K^{-1/3})$-KKT；两方互补均成立 | 部分重合（1, 2） |
| C08 | 定理编号 | `Theorem 4.4` 为 $\mu h_\mu$ 的 epi-limit 结论，`Theorem 4.5` 为 $O(\log(1/\epsilon))$ 外层步数，`Theorem 4.6` 含不可行分支；Astra 编号准确，纠正 Carbon | 相关（无） |
| C12 | 复杂度与 `(B5)` | `Theorem 3.2` 式 `(3.31)` 未平方精度对应 $O(\epsilon^{-6})$；式 `(3.32)–(3.33)` 为带符号均值，无单点 $\epsilon$-KKT；`Lemma 2.6` 隐含依赖 `(B5)` 严格正则；两方观察均成立 | 相关（无） |
| C15 | 定理与推论区分 | `Theorems 3.1–3.2` 对应 Polyak 与递归两种动量，均需近可行初值（纠正 Carbon「确定性 vs 随机约束」及 Astra 的区分表述）；`Corollaries 3.1–3.2` 给出 $O(\epsilon^{-5})$ 与 $O(\epsilon^{-4})$ | 相关（无） |
| C18 | 证明缺陷（v2 已撤稿） | v1 `Lemma 3.2` 式 `(3.12)` 后将随 $t$ 变化的参考点 $\hat y_t$ 当作可伸缩求和项，能量收缩不成立；Carbon 提及的 `(3.55)` 在 v1 中不存在；`Corollary 3.1` 证书针对近端点 | 相关（无） |
| C21 | 对数因子与二阶结果 | `Theorem 5.3` 与 `5.4` 预选 $\beta_0$ 后分别化为 $O(\epsilon^{-4})$ 与 $O(\epsilon^{-3})$（一般 $\beta_0$ 含对数）；`Theorem 6.3` 为二阶 oracle 下 $O(\epsilon^{-5/2})$，不可与一阶比较 | 相关（2） |
| C25 | 式 `(3.38)–(3.41)` | `Theorem 3.2` 平均平方梯度 $O(T^{-1/4})$ 对应未平方 $O(\epsilon^{-8})$；不等式违反与互补性为带符号均值，不控制单点可行性 | 相关（无） |
| C33 | 罚参数阶数 | `Algorithm 1` 中 $c_{k+1}=\Theta(k)$，`Remark 2.1` 识别 PHR 子问题等效罚参数为 $\Theta(k^2)$，`Remark 2.2` 用 FISTA 类内层求解；Astra 准确，纠正 Carbon | 相关（3） |
| C36 | 初始能量 | `Lemma 7` 取 $\beta=C_\beta K^{1/2}$；式 `(22)` 含 $\frac{\beta}{2}\lVert Ax^0-b\rVert^2$ 却直接断言右端 $O(1)$，隐含近可行初值前提；Astra 指出的问题成立 | 相关（1） |
| B02 | 式 `(4.1)` 线性化 | `Algorithm 2` 仅线性化 $f$，未线性化 $\frac{\kappa_k}{2}\lVert Ax-b\rVert^2$，一般 $A$ 与 $g$ 下无法由一次 $\operatorname{prox}_g$ 求解；`Theorem 4.1` 取 $\kappa_k=\Theta(k)$；Astra 准确 | 相关（3） |
| B08 | `Theorem 1` 尺度缺陷 | `Theorem 1` 第二部分取 $\beta=1/K$ 时，由 `Assumption 3` 式 `(37a)–(37c)` 推出 $d$、$\tau_F$ 与 $\tau_H$ 至少 $\Theta(K)$，原文将 $\zeta$ 与 $\hat P$ 视作 $K$-无关常数，证明不完整；第一部分 $\epsilon$-AKKT 不受影响 | 相关（1） |

`C18` 式 `(3.12)` 处无法跨步抵消的项与 `B08` 式 `(37a)–(37c)` 参数尺度条件：

$$
\lVert\hat y_t-y_t\rVert^2-\lVert\hat y_t-\tilde y_{t+1}\rVert^2,\qquad \hat y_t\in\arg\max_{y} L(\hat x_t,y);
$$

$$
d\gt\frac{(1-\rho\beta)(2-\rho\beta)}{4\rho\beta},\qquad \tau_F I\succ 2d\rho A^\top A+\bigl[(4d+3)L_F+(4d+1)\gamma_F\bigr]I.
$$

---

## 六、模型调用路线与失败记录

| 阶段 | 执行角色 | 模型与推理档位 | 首选路线与结果 | 失败记录 | 实际完成路线与产出 | 日志文件 |
|---|---|---|---|---|---|---|
| Stage 1 | `search-neon` | Gemini 4 Neon High | Swarm 内置直接执行，成功 | 无 | Swarm 内置；产出 43 篇 2026 主候选、10 篇 2026 顶刊旧预印本基准与 6 篇边界附注 | `stage1/neon-candidates.md` |
| Stage 1 | `search-gpt-sol` | GPT 6.2 Sol（`gpt-6.2-sol`, `reasoning_effort="high"`, `web_search="live"`） | `codex-cli 0.171.0` 官方 OpenAI provider（本地 OAuth），一次通过，未触发 `yxai` 降级 | 外部 API 限流：Semantic Scholar 主题搜索 HTTP 429，DBLP 返回非 JSON | 官方 OpenAI provider（`exit code 0`，281,306 tokens）；产出 22 篇候选，22/22 元数据复核通过 | `stage1/gpt-sol-route.log` |
| Stage 2 前置 | `merger` | Gemini 4 Neon High | Swarm 内置直接执行，成功 | 无 | Swarm 内置；合并去重 48 篇主候选与 10 篇边界候选，下载提取 56 篇全文 | `stage2/merged-candidates.md` |
| Stage 2 | `verify-carbon` | Gemini 4 Carbon High | Swarm 内置直接执行，成功 | 无 | Swarm 内置；独立完成 56 篇全文核对 | `stage2/carbon-verification.md` |
| Stage 2 | `verify-gpt-astra` | GPT 6.2 Astra（`gpt-6.2-astra`, `reasoning_effort="high"`） | `codex-cli 0.171.0` 官方 OpenAI provider：Probe 1 成功（27s，`exit code 0`），正式 Batch 1 与 Batch 2 失败 | 1. 官方 OpenAI provider 在 Batch 1（303s）与 Batch 2（301s）均报 `ERROR: You’ve hit your usage limit`（`exit code 1`）；2. 切换 `yxai` 后首次探测 `-m "yxai/gpt-6.2-astra"` 报 `403 Forbidden: 模型不存在或未启用`（66s，`exit code 1`） | 降级至 `yxai` provider（`https://yxai.chat/v1`），使用 `-m "gpt-6.2-astra"` 探测通过（43s）后，5 批共 56 篇全部 `exit code 0` 完成（耗时 614s、1023s、757s、619s、830s，有效总计 2,039,467 tokens） | `stage2/gpt-astra-route.log` |
| Stage 3 | `judge-opus` | Claude Opus 5.5（`claude-opus-5-5`, `effort="high"`） | 路线 1（Swarm 内置）与路线 2（直接 `/opt/homebrew/bin/claude`）均失败 | 1. Swarm 内置 `claude-opus-5-5-high` 余量 `0%`（重置时间 `2026-11-25T13:00:13Z`）；2. 直接调用 `/opt/homebrew/bin/claude`（v2.1.326，尝试 `--model opus` 与 `--model claude-opus-5-5`）绕过 `claude-wrapper` 落至满额旧账号，均触发 HTTP 429 `rate_limit_error` / `usage_limit_reached`（周限额，重置 `Nov 24 at 11am Europe/Vienna`） | 经 `$HOME/.local/bin/claude-wrapper /opt/homebrew/bin/claude --model opus --effort high` 走 `claude-switch` 活跃第一方 OAuth 账号；探测通过（4.2s，`$0.16`），正式终审 146 轮完成（`exit code 0`，墙钟 1,469s / API 1,458.7s，输出 116,355 tokens 含 49,410 thinking tokens，缓存读取 20,102,539 tokens，账单 `$9.26`，session `d67382ec-45d5-4372-b8c8-21492b7773d6`） | `stage3/opus-route.log` |
| Stage 4 | `polish-neon` | Gemini 4 Neon High | Swarm 内置直接执行，成功 | 无 | Swarm 内置；完成中文终稿初版起草 | `stage4/neon-draft.md` |
| Stage 4 | `polish-argon` | Gemini 4 Argon High | Swarm 内置直接执行，成功 | 无 | Swarm 内置；完成逐项事实保真复核与最终报告定稿 | `stage4/argon-audit.md` |

---

## 七、读不到全文的论文（2 篇）

全部 48 篇 2026 主候选中，以下 2 篇因期刊付费墙无法获取公开全文且无 arXiv 预印本，依规范不绕过付费墙、不予评级。全部 10 篇边界时间候选均已获取全文。

| ID | 标题 | 作者 | 日期与出处 | 链接 | 无法读取原因 |
|---|---|---|---|---|---|
| C47 | A Proximal-Perturbed Bregman ADMM for Solving Nonsmooth and Nonconvex Composite Optimization | Jianchao Bai, Xu Cui, Zhie Wu | 2026-05-07，*Numerical Mathematics: Theory, Methods and Applications* (NMTMA), Global Science Press | DOI: [10.4208/nmtma.oa-2025-0066](https://doi.org/10.4208/nmtma.oa-2025-0066) / [期刊页](https://www.global-sci.com/nmtma/article/view/24096) | Global Science Press 付费墙（下载链接返回 HTML 订阅页）；OpenAlex 原链接失效；无 arXiv 预印本 |
| C48 | An Accelerated Preconditioned Primal-Dual Gradient Algorithm for Nonconvex Composite Optimization Problems with Applications | Xian-Jun Long, Jia-Lin Nie, Gao-Xi Li, Zai-Yun Peng | 2026-05-14，*Journal of Computational Mathematics* (JCM), Global Science Press | DOI: [10.4208/jcm.2512-m2024-0107](https://doi.org/10.4208/jcm.2512-m2024-0107) / [期刊页](https://www.global-sci.com/JCM/article/view/24201) | Global Science Press 付费墙（下载链接返回 HTML 订阅页）；OpenAlex 原链接返回 HTML；无 arXiv 预印本 |

按标题与出处判断，`C48` 涉及非凸复合问题的加速原始-对偶梯度算法，与创新点 3 主题相近，获取全文后建议补核。

**特殊状态附注**：`C18`（`arXiv:2606.25355`）最新 `v2` 版已于 2026-08-10 撤稿（作者备注 *"I found some critical problems which should be reconsidered"*），当前 PDF 链接返回 HTTP 404；其公开归档初版 `v1`（2026-06-24）全文已下载核实并确认证明缺陷（见 5.4 `C18`），因撤稿不构成有效在先文献。
