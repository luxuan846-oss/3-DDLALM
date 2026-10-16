# DDLALM / SPLALM 文献库（截至 2026-10-01）

> 另见 `notes/project/lower-bound-references.md`（2026-10-12：下界、参数尺度、固定罚 ALM 的阅读清单与元数据核对）。


说明：
- "bib key" 指 `tools/refer.bib` 中已有的条目；"—" 表示尚未加入 bib。
- 核对状态："原文"＝已对照原文核对；"讨论"＝来自讨论或摘要，细节待核对。
- 记号：GS＝game stationarity（对应我们的 ε-KKT 证书），OS＝optimization stationarity（Moreau 包络平稳）。

---

## A. 与 Q1（固定 s 的下界）直接相关

| bib key | 文献 | 内容 | 与我们的关系 | 核对 |
|---|---|---|---|---|
| `li2026smoothing` | Li, Nagarajan, Pan, Zhang, *Smoothing Meets Perturbation: Unified and Tight Analysis for Nonconvex-Concave Minimax Optimization*, arXiv:2602.14185 (2026) | 统一分析 Perturbed GDA、Smoothed GDA、PSGDA。GS：PSGDA 取 r_y=Θ(ε/D_Y) 得 O(ε^{-3})；OS：r_y=Θ(ε²/(ℓD_Y²))。Thm 3.2/3.4、Cor 3.1 给出算法特定下界（Smoothed GDA 为 Ω(ε^{-4})，PSGDA 的 GS 为 Ω(ε^{-3})）。Remark 3.3(iii)：Smoothed GDA 需 β_t~ε²，PSGDA 只需 ~ε。§5：线性递推 + 谱分析（Lemma 5.1–5.4），Example 5.1/5.2 | 我们的下界是其 Smoothed GDA 现象在"所有常数中心步长 + 移动对偶中心"下的推广；§5 是轨迹/谱部分的写法范本。注意：下界量词只覆盖其参数条件；Example 5.1 在 x=0、y>0 处 x-导数不连续；PSGDA 实例的 Δ=O(ε²/ℓ) | 原文 |
| — | Mahdavinia, Deng, Li, Mahdavi, *Tight Analysis of Extra-gradient and Optimistic Gradient Methods For Nonconvex Minimax Problems*, NeurIPS 2022, arXiv:2210.09382 | NC-SC/NC-C 上 GDA、EG、OGDA 的上界；§5 Thm 5.1/5.2：任意学习率下 NC-SC 的 Ω(κΔ/ε²)，困难实例为二次函数 | "与步长无关的下界"的先例；问题类、算法、阶均与我们不同，不撞车。Li 2026 Example 5.2 改编自其 Appendix B.3.1 | 原文 |
| — | Carmon, Duchi, Hinder, Sidford, *Lower Bounds for Finding Stationary Points I*, Math. Program. (2020) | 函数类、算法类、复杂度 inf_A sup_f 的定义（§2.1–2.3，式 (7)）；zero-chain | 我们第 2 节"定义四件套"的写法来源 | 讨论 |
| — | Tian, So, *No dimension-free deterministic algorithm computes approximate stationarities of Lipschitzians*, Math. Program. 208 (2024) 51–74, arXiv:2210.06907 | 函数类 \(\mathcal F^{\rm Lip}_{C,d}=\{f:\RR^{d'}\to\RR:\ d'\in[d],\ \|f\|_{\rm Lip}\le C,\ f(0)-\inf f\le C\}\)（维数取并集，初始间隙写进类）；Goldstein 近似平稳 (ε,δ)-GAS；局部 oracle；确定性算法类 \(\mathcal A_{\det}\)、确定性 general zero-respecting 类 \(\mathcal A_{\det\text{-}gzr}\subseteq\mathcal A_{\det}\)；复杂度 \(\inf_{A}\sup_{f}\min_{t\le T}\mathrm{dist}(0,\partial_\delta f(x^{A[f],(t)}))\)。结论：确定性算法不存在无维数依赖的多项式 oracle 复杂度，随机算法可以（对照 Zhang et al.） | **"定义四件套"的第二个格式来源**（与 Carmon et al. 并列）：维数并集 + Δ 入类；算法类用"信息结构"定义；复杂度用 min_{t≤T} 覆盖任意输出规则。注意：其算法类是全体确定性局部算法，我们是带参数 (α,β) 的固定算法族，量词更弱（族内下界），不能写成 oracle 下界 | 原文（arXiv PDF 的问题设定部分已核对） |
| — | Li, Pan, *Optimal Deterministic Oracle Complexity for Weakly Convex Optimization*, arXiv:2608.03246 (2026) | ρ-弱凸、G-Lipschitz，全次微分 oracle，Ω(ρG²Δ/ε⁴)（Δ ≤ G²/ρ）；tilted max-affine 块 + 弱凸耦合，对角滤链；结构为"定义 → 显式常数定理 → Condition (C1)–(C4) 归约 → 构造 → 逐条验证 → 推广到确定性算法" | 正文书写格式的范本。oracle 不含 prox，下界不适用于我们 | 原文 |
| — | Pan, Zheng, Li, *Optimal Deterministic First-Order Oracle Complexity for Nonconvex-Concave Minimax Optimization*, arXiv:2609.14235 (2026) | 光滑 NC-C，梯度 oracle，ε-OS 的 Θ(ℓ²D_YΔ/ε³)；saddle zero-chain + resisting oracle；匹配上界 TRACKED-FOAM（嵌套）；此前记录的"Remark 3.3：GS 可达 O(ε^{-5/2})"在 2026-10-01 抓取的原文中未找到，to be verified；GS 的 ε^{-5/2} 改引 arXiv:2609.17973 | 困难实例结构上属于 NC-L，但 oracle 不含 prox_h、度量为 OS，不能移用到我们的 prox + KKT 设定；§2 定义方式可借鉴 | 讨论（已核对内链结构） |
| — | Zhang, Xu, *Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex–Concave Minimax Optimization*, arXiv:2609.17973 (2026) | 单环 NC-C：投影阻尼外梯度 + 对偶动量 + 移动近端中心；OS 的 O(ε^{-3})，GS 的 O(ε^{-5/2})；GS 时对偶正则 τ=min{L, ε/(2D_Y)} | GS 速度标杆；其参数对应 s=Θ(1/ε)，不是固定参数 | 原文（2026-10-01） |
| — | Arjevani, Shamir, *On the Iteration Complexity of Oblivious First-Order Optimization Algorithms*, ICML 2016 | 指定算法结构内，时不变系数是否阻碍加速（§2、§4.2、Cor 1） | "算法结构内某要素是否必要"的研究先例 | 讨论 |
| — | Drori, Teboulle, *Performance of first-order methods for smooth convex minimization: a novel approach*, Math. Program. (2014), DOI 10.1007/s10107-013-0653-0 | PEP：把最坏情形写成优化问题 | 极小极大（两个实例分支对抗同一对步长）的思想来源 | 讨论 |
| — | Taylor, Hendrickx, Glineur, *Exact Worst-Case Performance of First-Order Methods for Composite Convex Optimization*, SIOPT 27 (2017) | 含近端步的一阶方法的精确最坏情形 | PEP 工具；精确最坏情形结果可发 SIOPT 的先例 | 讨论 |
| — | Zamani, Abbaszadehpeivasti, de Klerk, *The exact worst-case convergence rate of the ADMM*, Math. Program. 208 (2024) | ADMM 的精确最坏情形与紧实例 | "重要算法的精确复杂度"进入 MP-A 的先例 | 讨论 |
| — | Liu, Lin, Xu, *Lower Complexity Bounds of First-Order Methods for Affinely Constrained Composite Nonconvex Problems*, MOR 51(2):1659–1682 (2026), DOI 10.1287/moor.2023.0377, arXiv:2502.17770 | 问题 min f_0+g s.t. Ax+b=0，f_0 为 L_f-光滑，g=ḡ(Āx+b̄) 凸 lsc（Problem Class 1）。ORACLE1 给 ∇f_0、Ax、Aᵀz、prox_{ηg}；ORACLE2 给 prox_{ηḡ} 及 Ā、A 的乘积（Algorithm Class 1/2，线性张成）。准则为含可行性残差的 KKT 型 ε-驻点（Def 1）。Thm 1/2：Ω(κ([Ā;A]) L_f Δ_{F_0} ε⁻²)；Class 2 下由 IPG（arXiv:2307.07605）以 Õ(·) 达到，Class 1 的紧性未知。Class 1 包含线性约束下的二次罚与 ALM 方法 | MOR 上"复合非凸 + 下界"的先例。约束为线性、oracle 含 prox，阶为 ε⁻²；我们的族下界 ε⁻⁴ 高于它，说明 ε⁻⁴ 来自算法族的结构，不来自问题本身 | 原文（2026-10-14） |
| — | Güler 1991/1992；Gu, Yang, SIOPT (2020)，DOI 10.1137/19M1299049；Kim (2021) | 近端点法速率 O(1/k)、加速 O(1/k²)；Gu–Yang 的指标是平方固定点残差 | 早期"中心跟踪"启发式的工具；现已不作为证明前提 | 讨论 |
| — | Ouyang, Xu (2021) | 双线性鞍点问题下界 | 乘子部分可能的下界工具（未使用） | 讨论 |

## B. 固定罚参数与正则性（Q3、β=1 端点的对照）

| bib key | 文献 | 内容 | 与我们的关系 | 核对 |
|---|---|---|---|---|
| `liu2026fixed` | Liu, Deng, Wang, Wen, *A Fixed-Penalty Linearized Augmented Lagrangian Method with Classical Multiplier Updates*, arXiv:2608.19847 (2026) | NR-LALM：min f s.t. c(x)=0，光滑。x 步解 (βI+ρ∇c∇cᵀ)p=−∇f−∇c(λ+ρc)（Gauss–Newton 型，只用 ∇f、∇c，不用 Hessian，但不是梯度步）；经典乘子更新。Thm 2.12：区域 U 上局部光滑 + uniform LICQ，固定 β,ρ，O(ε^{-2})；迭代停留在 U 内是证明出来的。Lemma 2.8：‖λ_{k+1}−λ_k‖² ≤ C(‖p_k‖²+‖p_{k−1}‖²)。无下界 | 正则性驱动的固定罚结果（Q3 型），不回答 Q1；步的类型与 SPLALM 不同 | 原文 |
| `zhang2022global` | Zhang, Luo, *A Global Dual Error Bound and Its Application to the Analysis of Linearly Constrained Nonconvex Optimization*, SIOPT (2022), arXiv:2006.16440 | min f s.t. Ax=b, x∈P（多面体）；S-prox-ALM（对偶上升 + 一步投影梯度 + 原始中心平均），步长固定、与 ε 无关，O(ε^{-2})；不需要 A 的秩条件，靠 Hoffman 界 | 与 SPLALM 同类（梯度步、固定参数）的正面结果。推论（inference）：线性 A + 多面体 h 的实例很可能容易，困难实例需非线性 A 或非多面体 h（我们的快分支用 h=‖·‖₂） | 原文（arXiv 版） |
| `zhang2020proximal` | Zhang, Luo, *A Proximal Alternating Direction Method of Multiplier for Linearly Constrained Nonconvex Minimization*, SIOPT (2020), arXiv:1812.10229 | 线性约束，smoothed 原始序列 + 梯度投影步，误差界分析 | Zhang–Luo 路线的前作 | 讨论 |
| — | Zhang, Pu, Luo, *On the Iteration Complexity of Smoothed Proximal ALM for Nonconvex Optimization Problem with Convex Constraints*, arXiv:2207.06304 | Ax=b、x∈X（一般凸），CRCQ + 局部强/弱对偶误差界，O(ε^{-2}) | 非多面体情形的局部正则性路线 | 原文 |
| `zhang2020smoothed`（与 `zhang2020single` 重复） | Zhang, Xiao, Sun, Luo, *A Single-Loop Smoothed Gradient Descent-Ascent Algorithm for Nonconvex-Concave Min-Max Problems*, NeurIPS 2020 | Smoothed GDA；Thm 3.8：有限极大 + 严格互补 ⇒ O(ε^{-2}) | 原始光滑的来源；结构条件提速的先例 | 讨论 |
| `hoffman1952` | Hoffman (1952) | Hoffman 误差界 | Zhang–Luo 全局对偶误差界的基础 | — |
| `sahin2019inexact` | Sahin et al., NeurIPS 2019 | 非线性约束的不精确 ALM，罚参数递增，一致正则性条件 | Q3 正则性条件的对照 | 讨论 |
| `elbourkhissi2025linearized`、`elbourkhissi2025perturbed`（与 `berahas2025linearized` 重复，key 名有误） | El Bourkhissi, Necoara（, Patrinos）, 线性化（扰动）ALM，arXiv:2503.01056 等 | 非线性约束的线性化 / 扰动 ALM 复杂度 | 固定罚线性化 ALM 的相关工作，正文 Related Work 需对比 | 未核对 |
| `hu2026fixed` | Hu, Deng, *Fixed-Penalty Manifold Augmented Lagrangian Methods*（PKU workshop 2026 幻灯片，项目文件 jiang_hu.pdf） | 紧流形、线性 A；固定 ρ，有效罚 ρ+1/μ_k 仍增长；最后一页开放问题：moving-center 正则单环能否 O(ε^{-3})，"still unclear" | Q1 的直接动机来源；范围不同（紧流形、线性 A），不能宣称解决其开放问题 | 原文 |
| — | arXiv:2607.08954, *Nonconvex Composite Functional Constraints via First-Order Augmented Lagrangian Methods under Local Regularity* | 局部正则性下的一阶 ALM | 待读 | 未读 |
| — | arXiv:2502.19764, *Inexact Moreau Envelope Lagrangian Method for Non-Convex Constrained Optimization under Local Error Bound Conditions on Constraint Functions* | 局部误差界下的 Moreau 包络 Lagrangian 法 | 待读（网页限流，未读到） | 未读 |

## C. Minimax 与扰动 / 光滑方法（引言表格中的对照）

| bib key | 文献 | 内容 | 与我们的关系 | 核对 |
|---|---|---|---|---|
| `zheng2023universal` | Zheng, Zhu, So, Blanchet, Li, *Universal Gradient Descent Ascent Method for Nonconvex-Nonconcave Minimax Optimization* (DS-GDA), NeurIPS 2023, arXiv:2212.12978 | F=f+(r₁/2)‖x−z‖²−(r₂/2)‖y−v‖²，参数固定，z、v 平均更新；Thm 1：凹对偶 ε^{-4}，对偶 KŁ θ 时 ε^{-4θ} 或 ε^{-2}；Lyapunov Φ=F−2d+2q；要求 X、Y 紧 | 结构上与 SPLALM 相同（取 f=D_ρ、r₁=1/γ、r₂=1/s）。我们的下界强烈提示 DS-GDA 的 ε^{-4} 是紧的，但需把构造迁移到 DS-GDA 更新上验证 | 原文 |
| — | Zheng et al., *Doubly Smoothed Optimistic Gradients: A Universal Approach for Smooth Minimax Problems*, arXiv (2025)（项目文件） | DS-OGDA | DS-GDA 的后续 | 未核对 |
| `xu2026rada` | Xu, Jiang, Liu, So, *A Riemannian Alternating Descent Ascent Algorithmic Framework for Nonconvex-Linear Minimax Problems* (RADA), MOR (2026), arXiv:2409.19588 | NC-L，正则 −(λ_X/2)‖y‖²−(β_k/2)‖y−y_k‖²，λ_X=ε/(2R)，β_k 可和递减；对偶步一次 prox 精确；GS（RGS 定义）O(ε^{-3})。§5.1：λ_X=0 时与 RALM 重合，但不在其复杂度定理范围内 | 子问题与我们同族；有效罚 →2R/ε，属罚型，合并中心一般非零（不应归入 μ=0 列）。"固定罚 + 复杂度"未被其占据 | 原文 |
| `lu2020hybrid` | Lu, Tsaknakis, Hong, Chen, *Hybrid Block Successive Approximation for One-Sided Non-Convex Min-Max Problems*, IEEE TSP (2020) | Perturbed GDA | 引言表格：μ≡0、s=Θ(1/ε)，ε^{-4} | 讨论 |
| `xu2023unified` | Xu, Zhang, Xu, Lan, *A Unified Single-Loop Alternating Gradient Projection Algorithm for Nonconvex-Concave and Convex-Nonconcave Minimax Problems*, Math. Program. (2023) | AGP，对偶扰动 | 同上 | 讨论 |
| `pan2021efficient` | Pan, Shen, Xu, COAP (2021) | NC-L minimax，O(ε^{-3}) | NC-L 结构下 ε^{-3} 的已有结果 | 讨论 |
| `he2024approximation` | He, Zhang, Xu, J. Global Optim. (2024) | NC-L 近似近端梯度算法 | 同上 | 讨论 |
| `lin2020gradient` | Lin, Jin, Jordan, ICML 2020 | GDA 在 NC-C 上的分析 | 背景 | — |
| — | Ostrovskii, Lowy, Razaviyayn (2021) | 嵌套 + Nesterov，ε^{-2.5} | 加速内层的对照 | 讨论 |
| — | Li, Zhu, So, *Nonsmooth nonconvex–nonconcave minimax optimization: Primal–dual balancing and iteration complexity analysis*, Math. Program. 214 (2025) 591–641（arXiv:2209.10825，早期标题 *Smoothed Proximal Linear Descent-Ascent for ...*） | 结构化非光滑 NC-NC：Smoothed PLDA，对偶 KŁ 指数 θ，复杂度 O(ε^{-2max{2θ,1}})；给出 game stationarity 与 optimization stationarity 的定义及其算法无关的关系（DS-OGDA 文献称 Definition 7.1） | GS/OS 区分的出处：我们的证书 R_k 对应 L(x,q)=f+⟨A(x),q⟩−h*(q) 的 GS；定义四件套的 Remark 中引用它说明证书类型。势函数演化线 | 摘要级（arXiv 摘要已核对；Definition 7.1 的编号来自 DS-OGDA 引用，待核原文） |

## D. 约束优化中的 ALM / 罚方法（引言表格与 Related Work）

| bib key | 文献 | 内容 | 与我们的关系 | 核对 |
|---|---|---|---|---|
| `kim2024fast`（与 `anonymous2026beyond` 重复，作者列表不一致，需统一） | Kim, Chandra, Hashemi et al. / Moon, Kim, Chandra et al., *Beyond Convexity: Proximal-Perturbed Lagrangian Methods for Efficient Functional Constrained Optimization* (PPALA), arXiv:2406.17107 | 固定罚、移动中心，声称 Õ(ε^{-2})。v2：Assumption 6 原始定义域紧，Assumption 7 直接假设乘子在紧集；有限步可行性见 Lemma 18、附录 C.2 式 (53) | 无原始光滑、s 固定的对照；需核查式 (53) 所引速率是否已在前文建立 | 讨论（据 GPT 核对 v2） |
| `luSingleLoopGradientDescent2022` | Lu, *A Single-Loop Gradient Descent and Perturbed Ascent Algorithm for Nonconvex Functional Constrained Optimization* (GDPA), ICML 2022, arXiv:2207.05650 | 单环，O(ε^{-3})；惩罚参数 β_r∼r^{1/3} 递增，τ 固定；r=ε^{-3} 时即 ρ_k=Θ(1/ε) | 引言表格 | 原文（2026-10-01；作者姓名沿用 bib key） |
| — | Deng, Peng, *An inexact augmented Lagrangian method for nonsmooth optimization on Riemannian manifold* (MIALM), arXiv:1911.09900 | A 为线性算子，流形上；用 Moreau 包络得到光滑子问题；双循环，子问题不精确求解；收敛分析同时允许 ρ_k 有界与 ρ_k→∞；乘子更新符号与我们相反 | 不在我们下界的算法类内，理由是双循环与子问题精度趋零（不是罚参数增长）；且它是线性 A | 原文（2026-10-01） |
| `alacaoglu2024complexity` | Alacaoglu, Wright, AISTATS 2024 | 二次罚，ρ_k~k^{1/4}，Õ(ε^{-4}) | 引言表格 | 讨论 |
| `shi2025momentum` | Shi, Wang, Wang, *A Momentum-Based Linearized ALM*, MOR (2025) | 线性化 ALM + 动量 | 相关工作 | 未核对 |
| `hajinezhad2019perturbed` | Hajinezhad, Hong, *Perturbed proximal primal-dual algorithm for nonconvex nonsmooth optimization*, Math. Program. (2019) | 扰动 AL | "Dual-Damping"命名重叠，Related Work 必须对比；阻尼参数与 ε 的关系待核实 | 未核对 |
| — | Kong, Monteiro, SIOPT (2024) | 近端 ADMM，阻尼 / 扰动 AL | 同上 | 未核对 |
| `kong2019complexity` | Kong, Melo, Monteiro, SIOPT (2019) | 二次罚加速不精确近端点法 | 罚方法复杂度背景 | — |
| `lin2022complexity` | Lin, Ma, Xu, COAP (2022) | 不精确近端点罚方法 | 同上 | — |
| `xie2021proximal` | Xie, Wright, J. Sci. Comput. (2021) | 近端 ALM 复杂度 | 同上 | — |
| `grapiglia2021complexity` | Grapiglia, Yuan, IMA J. Numer. Anal. (2021) | ALM 复杂度 | 同上 | — |
| `sun2024dual_descent_alm_admm` | Sun, Sun, SIOPT (2024) | 对偶下降 ALM/ADMM | 同上 | — |
| — | He, Yuan (2010) | 加速 ALM | 类外"加速中心"候选 | 讨论 |

## E. 经典基础

| bib key | 文献 | 用途 |
|---|---|---|
| `hestenes1969multiplier`、`powell1969method` | Hestenes 1969；Powell 1969 | 乘子法起源 |
| `rockafellar1973multiplier`、`rockafellar1976augmented` | Rockafellar 1973/1976 | 凸情形 ALM = 对偶近端点法（Fenchel 视角命题的出处） |
| `bertsekas1982` | Bertsekas 1982 | ALM 教材 |
| `moreau1965` | Moreau 1965 | Moreau 包络 |
| `nesterov2005smooth` | Nesterov 2005 | 光滑化；二次罚 = 中心为 0 |
| `trandinh2018smooth`（与 `tran2018smooth` 重复） | Tran-Dinh, Fercoq, Cevher, SIOPT 2018, arXiv:1507.06243 | 凸情形对偶光滑 + prox-center，光滑参数同伦趋零 |
| `rockafellar2009variational` | Rockafellar, Wets 2009 | 变分分析 |

---

## 待加入 refer.bib
Mahdavinia et al. 2022；Carmon et al. 2020；Tian–So 2024（2210.06907）；Li–Zhu–So 2025（Math. Program. 214）；Li–Pan 2026（2608.03246）；Pan–Zheng–Li 2026（2609.14235）；arXiv:2609.17973；Arjevani–Shamir 2016；Drori–Teboulle 2014；Taylor–Hendrickx–Glineur 2017；Zhang–Pu–Luo（2207.06304）；Zamani et al. 2024；Liu–Lin–Xu 2026；Kong–Monteiro 2024；Zheng et al. 2025（DS-OGDA）。

## refer.bib 中的重复条目
`zhang2020smoothed`/`zhang2020single`；`trandinh2018smooth`/`tran2018smooth`；`kim2024fast`/`anonymous2026beyond`（作者列表不同）；`elbourkhissi2025perturbed`/`berahas2025linearized`（key 名与作者不符）。
