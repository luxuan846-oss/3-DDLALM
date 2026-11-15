# Retreat slides 文献核查（2026-11-04）

目的：核对 `notes/retreat/slides/retreat_talk.tex` 中文献现状的说法在 2026-11-04 是否成立。检索窗口以 2026-08-01 至 2026-11-04 为主，另补检索中发现的 5–7 月相关文章。外部检索人的结果回来后在本文件第 5 节对照。

## 1. 结论

| slides 位置 | 原说法 | 核查结果 | 处理 |
|---|---|---|---|
| p6 红框 | 表中所有单环 $O(\epsilon^{-3})$ 结果都让罚参数或对偶正则随 $1/\epsilon$ 增长 | 成立。新增的单环结果都有一个参数随 $1/\epsilon$ 增长：Zhang–Xu 的对偶正则 $\tau=\Theta(\epsilon)$；ALDER 的罚参数 $\gamma_\epsilon=C/\epsilon$；Zhu–Li 的对偶正则 $r_y=\Theta(K^{-1/3})$ | 保留；表中可补 Zhang–Xu 一行 |
| p12 红框 | Known lower bounds treat one method at a time | 不准确。Pan–Zheng–Li 对任意确定性一阶方法给出 $\Omega(\epsilon^{-3})$ OS 与 $\Omega(\epsilon^{-5/2})$ GS 下界；Wu–Gu–Yang 对 zero-respecting 方法给出 $\Omega(\epsilon^{-3})$ OS 下界。这些下界不涉及哪个参数必须增长 | 改写，见第 4 节 |
| p11/p15 Theorem 3 的定位 | 固定 $\rho$、$s=\Theta(1/\epsilon)$ 达到 $O(\epsilon^{-3})$ | Zhu–Li（arXiv:2607.08954）在 prox-linear ALM 中得到同类结构：$\rho$ 固定且充分大，对偶正则 $r_y=\Theta(K^{-1/3})$，KKT 残差 $O(K^{-1/3})$。问题类、子问题、假设与本文不同 | slides 与论文引言都应引用并区分，见第 3 节 |
| p18 预期 | $s_k\asymp k$ 时残差 $1/k$；$o(1/k)$ 需要惯性 | 与 Boț–Nguyen（J. Complexity 2026）一致：一阶 Tikhonov 单调算子流的残差在特定正则函数下可达 $O(1/t)$；$o(1/k)$ 的结果来自带惯性或二阶的系统（fast OGDA；Li–Xiao 2610.39133） | 补引 Boț–Nguyen 2026 |
| p20 | 对偶动量给出 GS $O(\epsilon^{-5/2})$ | 成立。Zhang–Xu 的 GS 结果同时用了对偶动量、移动近端中心和 $\tau=\Theta(\epsilon)$ 的对偶正则，对偶域有界并做投影 | 可补"with $s=\Theta(\epsilon^{-1})$" |
| footnote | Boț–Chenchene, SIAM J. Optim., to appear | 已发表：SIAM J. Optim. 36(3), 1420–1445, 2026 | 更新 |

## 2. 相关文献表

列：标题 | 作者 | arXiv/期刊 | 日期 | 问题类与假设 | 单环/双环 | 随 $1/\epsilon$ 增长的参数 | 复杂度与驻点度量 | 类别（1 上界、2 下界、3 Tikhonov/加速、4 听众近作）

| 标题 | 作者 | 来源 | 日期 | 问题类与假设 | 结构 | 增长参数 | 复杂度 | 类别 |
|---|---|---|---|---|---|---|---|---|
| ALDER: A single-loop augmented-Lagrangian damped extragradient method for NC–C minimax problems with nonlinear coupled constraints | H. Zhang, M. Zhang, Z. Xu, Y.-H. Dai | arXiv:2611.00691 | 2026-10-31 | 光滑 NC–C minimax，耦合不等式约束 $c(x,y)\le0$，扩展 MFCQ | 单环 | 罚参数 $\gamma_\epsilon=C/\epsilon$（Thm 16–17）；凹情形对偶正则 $\rho_\epsilon=\Theta(\epsilon)$ | $\epsilon$-KKT：凹 $O(\epsilon^{-4})$，强凹 $O(\epsilon^{-7/2})$ | 1 |
| Matching multi-loop complexities with a single loop | M. Zhang, Z. Xu | arXiv:2609.17973 | 2026-09-16 | 光滑 NC–C，紧对偶域并投影 | 单环；对偶动量 + 移动近端中心 + extragradient | 以原点为中心的对偶正则：OS 取 $\tau=\Theta(\epsilon^2)$，GS 取 $\tau=\Theta(\epsilon)$（Thm 4.4、4.5） | OS $O(\epsilon^{-3})$，GS $O(\epsilon^{-5/2})$；projected zero-respecting 类 OS 下界 $\Omega(\epsilon^{-3})$ | 1、2、3 |
| Optimal deterministic first-order oracle complexity for NC–C minimax optimization (v2) | S. Pan, T. Zheng, J. Li | arXiv:2609.14235 | 2026-09-13 | 光滑 NC–C，有界凸对偶域 | Tracked-FOAM | — | 任意确定性一阶方法：OS $\Theta(\epsilon^{-3})$，GS $\Theta(\epsilon^{-5/2})$ | 2 |
| Lower bounds for NC–C minimax optimization | Q. Wu, Z. Gu, J. Yang | arXiv:2609.14233 | 2026-09-13 | 联合 $L$-光滑，有界对偶域 | — | — | zero-respecting：确定性 $\Omega(\epsilon^{-3})$，随机 $\Omega(\epsilon^{-6})$（Moreau 包络梯度） | 2 |
| Lower bounds for stochastic first-order algorithms with variance reduction in NC–C | J. Song, Z. Xu | arXiv:2610.01662 | 2026-10-01 | 随机 NC–C，紧对偶域 | — | — | $\Omega(\epsilon^{-3}+\sigma^2\epsilon^{-6})$，允许方差缩减 | 2 |
| Matching randomized bounds for finite-sum NC–C optimization | W. Wu et al. | arXiv:2610.16991 | 2026-10-12 | 有限和 NC–C，有界对偶域 | — | — | 随机分量 oracle 复杂度的上下界匹配 | 2 |
| Nonconvex composite functional constraints via first-order ALMs under local regularity | L. Zhu, J. Li | arXiv:2607.08954 (v2) | 2026-07-09 | $\min h_0(c_0(x))$ s.t. $h_i(c_i(x))\le0$，$X$ 紧，局部乘子正则，可行初值；不含等式约束 | 每步解强凸 prox-linear 子问题（按精确解计） | $\rho$ 固定且充分大；对偶正则 $r_y=\Theta(K^{-1/3})$，依赖 horizon | KKT 残差 $O(K^{-1/3})$；无正则时在分片线性外层函数与局部对偶误差界下为 $O(K^{-1/2})$ | 1 |
| A fixed-penalty linearized ALM with classical multiplier updates (NR-LALM) | B. Liu, K. Deng, Z. Wang, Z. Wen | arXiv:2608.19847 | 2026-08-20 | 光滑非凸目标，光滑等式约束，局部正则 | 单环 | 无 | 确定性 $O(\epsilon^{-2})$ | 1（已引） |
| Efficient parameter-free first-order methods for nonsmooth composite minimax optimization | S. Ke, S. Mei, J. Zhang | arXiv:2609.25752 | 2026-09-22 | 非光滑复合 NC–C | 多环（近端点外层） | — | $O(\epsilon^{-5/2})$ operation complexity | 1 |
| Single-loop stochastic projected damped extragradient methods for NC–(S)C | H. Zhang, M. Zhang, Z. Xu, Y.-H. Dai | arXiv:2609.21747 | 2026-09-18 | 随机 NC–(S)C | 单环 | 同 Zhang–Xu 的阻尼 | NC–C GS：SPDE $O(\epsilon^{-5})$，VR-SPDE $O(\epsilon^{-9/2})$ | 1 |
| Tikhonov regularization of monotone operator flows ... speeds up the vanishing of the residuals | R. I. Boț, D.-K. Nguyen | J. Complexity 94 (2026), 102029；arXiv:2406.00852 | 2026 | 单调连续算子方程，Hilbert 空间 | 连续时间加 Halpern 型离散 | — | 强收敛到最小范数解；残差在特定正则函数下可达 $O(1/t)$ | 3、4 |
| Extragradient method with flexible anchoring | R. I. Boț, E. Chenchene | SIAM J. Optim. 36(3), 1420–1445 (2026) | 2026 | 单调问题 | — | — | 强收敛与快速残差衰减 | 3、4（已引，更新出处） |
| Regularized extragradient method for structured bilevel optimization in continuous and discrete time | R. I. Boț, E. Chenchene, D. A. Hulett | arXiv:2608.29181 | 2026-08-29 | 凸外层 + 极大单调算子零点集 | 动态正则化算子的 proximal-extragradient | — | outer/inner 残差的 last-iterate 速率；迭代弱收敛 | 3、4 |
| Tikhonov-regularized dynamics and inexact algorithms for nonlinear saddle-point problems | H.-L. Li, Y.-B. Xiao | arXiv:2610.39133 | 2026-10-29 | 光滑凸–凹鞍点 | 二阶动力系统 + 非精确算法 | — | 强收敛到最小范数鞍点；gap $o(t^{-2})$、$o(k^{-2})$ | 3 |
| A unifying view of anchoring via operator-side Tikhonov regularization | Z. Chen | arXiv:2605.30905 | 2026-05-29 | 单调 Lipschitz 方程 | Halpern、EG、PEG 的 Tikhonov 版本 | — | 残差 $O(1/k)$（EG、PEG） | 3 |
| On the regularization of primal-dual dynamics in time-dependent nonconvex optimization | M. Vaquero, J. Cortés | arXiv:2610.19916 | 2026-10-14 | 时变约束优化；非凸时局部 | 连续时间 | 对偶 Tikhonov 正则 | 跟踪误差界 | 3 |

听众近作（arXiv 与 Boț 主页，2026）：
- Boț 主页 2026 年条目与本报告相关的有：Boț–Chenchene（SIOPT 36(3)）、Boț–Nguyen（J. Complexity 94）、Boț–Sonntag（vanishing Tikhonov 惯性动力系统，JMAA 554）、Boț–Nguyen–Zong（fast forward-backward 的 $o(1/k)$，Numer. Math. 158）、Boț–Nenov–Tao（结构化 DC full splitting，Appl. Numer. Math. 225），以及 to appear 的 Boț–Chenchene–Csetnek–Hulett（bilevel 的加速 diagonal 方法，MP）。
- Malitsky：arXiv:2608.22834（mirror descent with logarithmic barriers），与本报告无直接关联。
- Böhm、Csetnek、A. Daniilidis：检索窗口内没有 arXiv 新文。Ziyuan Wang 同名作者较多，未找到 Boț 组 Wang 在窗口内的新文。

## 3. 需要讨论的事项

1. **Zhu–Li 2607.08954 与 Theorem 3 的关系。** 两者都是固定 $\rho$、对偶正则约为 $\epsilon$ 量级、得到 $\epsilon^{-3}$。区别：
   - Zhu–Li 每步解 prox-linear 子问题，SPLALM 每步只做一次显式梯度步与 prox；
   - Zhu–Li 需要局部乘子正则、可行初值和紧的 $X$，处理不等式约束，并对对偶变量截断；
   - Zhu–Li 没有下界。

   本文的 "dual regularization alone can carry the growth" 应写成在显式单环族内成立，并引用 Zhu–Li 作为 prox-linear 情形的同类现象。论文引言与 `literature.md` 第 45 行同步处理。
2. **线性 $\mathcal{A}$ 的固定参数 $O(\epsilon^{-2})$ 结果。** Zhang–Luo（SIOPT 2022）在多面体约束下用固定步长达到 $O(\epsilon^{-2})$；Kim（arXiv:2306.11299，"false penalty"）对线性约束复合问题声称单环 $O(\epsilon^{-2})$。听众可能问：下界实例的 $\mathcal{A}$ 是仿射的，为什么这些结果不适用？可能的回答：Zhang–Luo 需要多面体结构，而困难实例的 $h$ 不是多面体函数。这一点依据 `literature.md` 第 37 行的推断，需逐个分支核对；Kim 2023 的假设与参数也待核。
3. **ALDER 的措辞。** 摘要称罚参数 "fixed throughout each run"，定理中取 $\gamma_\epsilon=C/\epsilon$。slides 可用它说明"在一次运行内固定"与"不依赖精度"的区别。

## 4. 建议的 slides 修改（对照外部检索后再改）

- p6 表增加一行：Zhang–Xu '26，对偶动量，$s=\Theta(\epsilon^{-1})$，GS $O(\epsilon^{-5/2})$。
- p12 红框改为两句："Parameter-uniform lower bounds exist for SGDA in NC–PŁ games [Ha '26]. Oracle lower bounds for NC–C [Pan–Zheng–Li '26] do not tell which parameter must grow."
- p15 或 p16 加一条 footnote：prox-linear ALM 中的同类现象 [Zhu–Li '26]。
- p18 第一条补引 Boț–Nguyen, J. Complexity, 2026。
- Boț–Chenchene footnote 与参考文献页改为 SIAM J. Optim. 36(3), 2026。
- p21 "Beyond the family" 可补："GS lower bound $\Omega(\epsilon^{-5/2})$ is known for smooth NC–C [Pan–Zheng–Li '26]; does it transfer to the class with $\mathrm{prox}_h$?"
- p21 或 p6 可补一句："Black-box weakly convex optimization needs $\Theta(\epsilon^{-4})$ [Li–Pan '26]; access to $\mathrm{prox}_h$ and $\mathcal{A}$ separately allows $\epsilon^{-3}$." 族内下界区域 $\rho+s\le c_1/\epsilon$ 的阶与黑箱阶相同，这一点只作为现象陈述。

## 5. 与外部检索对照

外部材料是检索人的推理过程记录，未附最终表。下面按记录中出现的条目对照，外部新增的条目已用 arXiv API 逐篇核对摘要。

**两边一致**：ALDER（两边都发现 $\gamma_\epsilon=\Theta(1/\epsilon)$）、Zhang–Xu、Pan–Zheng–Li v2、Song–Xu、Wu et al.（有限和 NC–C）、Zhu–Li、Ke–Mei–Zhang、SPDE/VR-SPDE、Boț–Chenchene–Hulett、Boț 主页 2026 条目、Li–Xiao、Liu–O'Neill。

**外部新增，已核实，影响 slides**：

| 标题 | 作者 | 来源 | 内容 | 影响 |
|---|---|---|---|---|
| Optimal deterministic oracle complexity for weakly convex optimization | J. Li, S. Pan | arXiv:2608.03246 (2026-08-04) | $\rho$-weakly convex、$G$-Lipschitz，oracle 返回函数值与完整次微分；任意确定性一阶方法需要 $\Omega(\rho G^2\Delta\epsilon^{-4})$，与上界匹配 | 黑箱下界为 $\epsilon^{-4}$；利用复合结构的方法可达 $\epsilon^{-3}$。可用于 p6 或 p21 |
| Stochastic gradient descent ascent is suboptimal for nonconvex-PŁ min-max games | J. Ha | arXiv:2610.07814 (2026-10-06) | 对固定时间尺度比、非增步长的 SGDA 给出紧下界 $\Omega(\kappa^2\ell\epsilon^{-2}+\kappa^4\ell\sigma^2\epsilon^{-4})$，对参数选择一致 | 与 Theorem 1 同类的"对参数一致"的算法族下界；p12 红框需引用 |

**外部新增，已核实，影响小**：
- Xu, Jiang, Zhang, Liu, So, *Riemannian DC optimization for K-means*（arXiv:2609.34310）：RADA-DC 用对偶正则，$O(\epsilon^{-3})$。与 p6 红框一致。
- Zhang–Wu–Yang（arXiv:2609.35206）、Wu et al.（arXiv:2610.00229）：随机 NC–SC 下界。问题类为强凹，不进 slides。
- Zhou–Chen–Luo–Liu（arXiv:2610.20345）：NC–SC 二阶方法，不相关。
- Liu–O'Neill（arXiv:2608.27676）：自适应罚参数的双环 ALM，确定性 $\widetilde O(\epsilon^{-3})$。不进单环表。

**外部提及但未能核实或不相关**：
- Malitsky 2026 年关于 Halpern anchoring、分布式 min-max 的工作：arXiv 2026 年只查到 arXiv:2608.22834（mirror descent with logarithmic barriers）。需看外部最终表的出处。
- 一篇 NC–PŁ 确定性下界 $\Omega(\ell\Delta\kappa\epsilon^{-2})$、匹配 AGDA 的文章：记录未给编号，待外部最终表。
- arXiv:2610.21026（clipped SGD 的 last-iterate）：不相关。

**判断差异**：
- Zhu–Li：外部记录称其为固定罚参数的单环方法。核对 Algorithm 1 与 Remark 3.1，每步要精确求解 prox-linear 子问题，"单环"只按外层迭代计数。两边一致的部分：$\rho$ 固定，$r_y=\Theta(K^{-1/3})$。

## 6. 检索记录

- arXiv API，时间窗 `submittedDate:[202608010000 TO 202611042359]`，共 43 条查询：ALM 与单环、fixed penalty、linearized ALM、nonconvex-concave、GDA、primal-dual nonconvex、lower bound（minimax、NC–C、GDA）、Tikhonov、anchoring/Halpern、dual momentum、dual regularization、smoothed GDA、ADMM nonconvex、proximal ALM、game stationarity、extragradient nonconvex、variable smoothing，以及听众作者查询。去重后约 300 条，按标题与摘要筛选。
- Web 检索：fixed-penalty 单环 ALM（2026）；Li–Nagarajan–Pan–Zhang 发表状态（Jiajin Li 主页列为 under revision）；Boț–Chenchene 发表状态（dblp `journals/siamjo/BotC26`）；Boț 个人主页 2026 条目；El Bourkhissi–Necoara 2301.08345 发表状态（未找到期刊信息）。
- 参数核对：Zhang–Xu 与 ALDER 读 arXiv HTML 正文的定理参数；Zhu–Li 读 Algorithm 1 与 Theorem 4.1。
