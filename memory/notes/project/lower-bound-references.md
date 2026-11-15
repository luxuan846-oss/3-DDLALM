# 下界与参数尺度：参考文献清单（2026-10-12 整理）

用途：写第 4 节（困难实例与证明）和第 6 节（上界）时，按这些文献的叙述风格与基本思路组织论证。原文未下载。

元数据核对：arXiv 条目已用 arXiv API 核对标题与作者；期刊条目已用 Crossref 按 DOI 核对。与用户提供列表不一致处已改正，并在"更正"一栏注明。

---

## 阅读顺序

| 轮次 | 文献 | 服务对象 |
|---|---|---|
| 第一轮 | [1] Li et al.；[5] Li–Pan；[2] Pan–Zheng–Li；[3] Wu–Gu–Yang | Theorem 3.1（第 4 节）：困难实例、初始间隙、轨迹区域、谱或链结构、驻点准则、下界量词、参数是否依赖 ε |
| 第二轮 | [4] Zhang–Xu；[6] Zhu–Li；[8] Liu et al. | 第 6 节上界与对照：固定罚参数的正面结果、s = Θ(1/ε) 的作用、局部正则性、显式梯度步与线性系统步的差异 |
| 第三轮 | [7] Deng et al. 综述；[9]–[17] | 引言与 Related Work：术语、ALM 文献谱系、MP/SIOPT 期刊对照 |

若只读三篇：[1]（零初值旋转分支、GS/OS）、[5]（ε⁻⁴ 下界与固定初始间隙）、[4]（s = Θ(1/ε) 的上界对照）。

---

## 每篇统一记录模板

1. 问题模型：是否为 f + h∘A
2. 算法类型：显式梯度、近端步、Gauss–Newton 型或内层求解
3. 罚参数：固定、递增，还是依赖 ε
4. 中心或扰动参数：是否有移动中心、对偶正则、原始光滑
5. 驻点准则：KKT、GS、OS、Moreau 包络或其他
6. 复杂度结果：上界、下界及其精度标准
7. 困难实例机制：谱模态、链结构、误差界失效、初始间隙
8. 对 SPLALM 的作用：可引用、可借证明技术、可作反例、仅作背景

---

## 第一组：下界、参数尺度、GS/OS

### [1] Li, Nagarajan, Pan, Zhang (2026)
*Smoothing Meets Perturbation: Unified and Tight Analysis for Nonconvex-Concave Minimax Optimization.* arXiv:2602.14185 (v2). <https://arxiv.org/abs/2602.14185>
bib key: `li2026smoothing`

已读部分（§1–§3.2）：
1. 模型：光滑 NC-C minimax，Y 紧凸
2. 算法：单循环 GDA 型（Perturbed GDA、Smoothed GDA、Perturbed Smoothed GDA），以及双循环 FOAM 型
3. 罚参数：无
4. 中心/扰动：原始光滑 + 移动中心 z；对偶扰动 r_y‖y‖²/2，中心为 0
5. 准则：GS 与 OS 分开（Definition 2.1）
6. 结果：Perturbed GDA 的 GS 为 Θ(ε⁻⁴)、OS 为 Θ(ε⁻⁶)；Perturbed Smoothed GDA 的 GS 为 Θ(ε⁻³)、OS 为 Θ(ε⁻⁴)；Smoothed GDA 的 GS、OS 均为 Θ(ε⁻⁴)
7. 机制：二次实例上的线性递推；困难实例连同初值一起选取（Theorems 3.2、3.4）
8. 作用：**主要技术来源与写法范本**。§2.1–2.2 "Dual Perturbation / Smoothing" 的写法已用于本文 2.5 节；定理句式 "Consider X run with … Then there exist an ℓ-smooth function and an initialization such that X requires at least T = Ω(·) iterations" 已用于本文 Theorem 3.1

待读：§5 tight analysis（递推矩阵、慢特征值、实例保持在指定区域、初始间隙对 ε 的依赖）

### [2] Pan, Zheng, Li (2026)
*Optimal Deterministic First-Order Oracle Complexity for Nonconvex-Concave Minimax Optimization.* arXiv:2609.14235. <https://arxiv.org/abs/2609.14235>
bib key: `pan2026optimal`

已读部分（§1–§3）：
1. 模型：光滑 NC-C minimax，diam(Y) ≤ D_Y
2. 算法类：确定性一阶算法 A_det（Def 2.5）与 zero-respecting 算法（Def 2.4）
3–4. 不涉及
5. 准则：OS（Def 2.2）
6. 结果：Θ(ℓ²D_YΔ ε⁻³)，下界对 A_det 成立，上界由 TRACKED-FOAM 达到
7. 机制：鞍点 zero-chain + 旋转（resisting oracle），维数随 ε 增长
8. 作用：**第 2 节定义的范本**（函数类 Def 2.1、oracle Def 2.3、复杂度 Def 2.6 的 inf–sup 写法）；本文 Remark 2.9 引用其算法类。不能直接证明 SPLALM 下界：oracle 与准则都不同

### [3] Wu, Gu, Yang (2026)
*Lower Bounds for Nonconvex-Concave Minimax Optimization.* arXiv:2609.14233. <https://arxiv.org/abs/2609.14233>

已读（2026-10-14，arXiv v1 PDF，§1–§2、Thm 4.1）：
1. 模型：光滑 NC-C minimax，f 联合 L-光滑、对 y 凹，diam(Y) ≤ D_Y，初始间隙 Φ(0)−inf Φ ≤ Δ_Φ 或原始–对偶间隙 G_0（Def 2.1）；维数取并集
2. 算法类：确定性 / 随机 zero-respecting 一阶算法（Def 2.6），oracle 返回 (f, ∇_x f, ∇_y f)，允许投影到 X、Y；不含任何 prox；初值 (0,0)
5. 准则：OS，‖∇(Φ+ι_X)_{1/(2L)}(x)‖ ≤ ε（Def 2.3）
6. 结果：Thm 4.1 确定性 Ω(L²D_YΔ_Φ ε⁻³)，ε ≤ c_1 min{√(LΔ_Φ), LD_Y}；Thm 5.5 随机 Ω(L³D_Y²Δ_Φ ε⁻⁶)；Cor 4.2/5.6 换成 G_0 同样成立；与 Lin–Jin–Jordan 的 Õ(ε⁻³)、SAPD+ 的 O(ε⁻⁶) 匹配
7. 机制：有界 zero-chain，原始坐标经对偶块（三对角路径矩阵 B_{α,N}）耦合，信息需穿过对偶块才能传到下一个原始坐标；维数随 ε 增长
8. 作用：§1 把 [Li26]、[Mah22] 归为 "algorithm-specific" 下界，本文属于同一类，但量词覆盖整个参数族。oracle 不含 prox、准则为 OS，与本文结果互不蕴含

### [4] Zhang, Xu (2026)
*Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex–Concave Minimax Optimization.* arXiv:2609.17973. <https://arxiv.org/abs/2609.17973>
bib key: `zhang2026matching`
更正：作者名按 arXiv 记为 Minghao Zhang（论文 PDF 中为 Minhao，bib 中已注明待核）

已读部分（§1–§2）：
1. 模型：光滑 NC-C minimax，Y 紧凸
2. 算法：单循环投影阻尼外梯度 + 对偶动量 + 移动近端中心
3. 罚参数：无
4. 对偶正则 τ：GS 取 τ = ε/(2D_Y)，即 s = Θ(1/ε)
5. 准则：OS（Moreau 包络）与 GS（(2.10)–(2.11)，梯度与法锥距离）
6. 结果：OS 为 O(ε⁻³)（并有匹配下界），GS 为 O(ε⁻⁵ᐟ²)
8. 作用：本文 GS 定义的出处之一；第 6 节 s = Θ(1/ε) 上界的对照；Remark 2.9 中说明它不在 SPLALM 族内

### [5] Li, Pan (2026)
*Optimal Deterministic Oracle Complexity for Weakly Convex Optimization.* arXiv:2608.03246. <https://arxiv.org/abs/2608.03246>

待读。要点：弱凸非光滑优化的确定性 Ω(ε⁻⁴) 下界；Moreau 包络驻点；固定初始间隙；函数类常数与 ε 无关；上下界匹配。作用：核对本文实例类、水平有界性和初始间隙的写法。oracle 模型不同，不能直接作为 SPLALM 下界。

### [6] Zhu, Li (2026)
*Nonconvex Composite Functional Constraints via First-Order Augmented Lagrangian Methods under Local Regularity.* arXiv:2607.08954. <https://arxiv.org/abs/2607.08954>

待读。要点：凸外函数 + 光滑非线性映射；对偶截断与乘子有界；局部锥正则性；对偶正则后的 O(K⁻¹ᐟ³)；分段线性外函数下的 O(K⁻¹ᐟ²)。作用：区分"无额外结构时固定 s 的障碍"与"加入局部正则性后的更快上界"，放在结论的开放问题和 Related Work 中。

---

## 第二组：固定罚 ALM 与综述

### [7] Deng, Wang, Zhu, Zhang, Wen (2026)
*The Augmented Lagrangian Methods: Overview and Recent Advances.* SIAM Review 68(3):471–576, 2026. DOI: [10.1137/24M1706153](https://doi.org/10.1137/24M1706153)
更正：作者为 Kangkang Deng, Rui Wang, Zhenyuan Zhu, Junyu Zhang, Zaiwen Wen（原列表首作者写作 "L. Deng"）

作用：术语统一、ALM 文献谱系、Related Work 组织。不用于核对证明细节。

### [8] Liu, Deng, Wang, Wen (2026)
*A Fixed-Penalty Linearized Augmented Lagrangian Method with Classical Multiplier Updates.* arXiv:2608.19847. <https://arxiv.org/abs/2608.19847>
更正：作者为 Benqi Liu, Kangkang Deng, Zichen Wang, Zaiwen Wen（原列表写作 "L. Deng, Z. Peng, X. Wang, …"）

已知（PROJECT_STATUS §5）：每步解 Jacobian 线性方程组（Gauss–Newton 型），uniform LICQ 下 O(ε⁻²)。作用：说明固定罚参数并不必然导致慢复杂度，改善来自更强的正则性或更强的原始步；论文中需写明它与 SPLALM 的三点差别：线性系统步对显式梯度步；uniform LICQ 不在本文问题类内；乘子由正则性控制。

---

## 第三组：期刊背景（MP / SIOPT）

[9] K. Sun, X. A. Sun. Dual Descent Augmented Lagrangian Method and Alternating Direction Method of Multipliers. *SIAM J. Optim.* 34(2):1679–1707, 2024. DOI: [10.1137/21M1449099](https://doi.org/10.1137/21M1449099)

[10] R. Andreani, K. R. Couto, O. P. Ferreira, G. Haeser. Constraint Qualifications and Strong Global Convergence Properties of an Augmented Lagrangian Method on Riemannian Manifolds. *SIAM J. Optim.* 34(2):1799–1825, 2024. DOI: [10.1137/23M1582382](https://doi.org/10.1137/23M1582382)

[11] W. Kong, J. G. Melo, R. D. C. Monteiro. Iteration Complexity of an Inner Accelerated Inexact Proximal Augmented Lagrangian Method Based on the Classical Lagrangian Function. *SIAM J. Optim.* 33(1):181–210, 2023. DOI: [10.1137/20M136147X](https://doi.org/10.1137/20M136147X)

[12] A. De Marchi, X. Jia, C. Kanzow, P. Mehlitz. Constrained Composite Optimization and Augmented Lagrangian Methods. *Math. Program.* 201:863–896, 2023. DOI: [10.1007/s10107-022-01922-4](https://doi.org/10.1007/s10107-022-01922-4)

[13] D. Boob, Q. Deng, G. Lan. Level Constrained First Order Methods for Function Constrained Optimization. *Math. Program.* 209:1–61, 2025. DOI: [10.1007/s10107-024-02057-4](https://doi.org/10.1007/s10107-024-02057-4)

[14] J. Zhang, Z.-Q. Luo. A Global Dual Error Bound and Its Application to the Analysis of Linearly Constrained Nonconvex Optimization. *SIAM J. Optim.* 32(3):2319–2346, 2022. DOI: [10.1137/20M135474X](https://doi.org/10.1137/20M135474X)

[15] J. Zhang, Z.-Q. Luo. A Proximal Alternating Direction Method of Multiplier for Linearly Constrained Nonconvex Minimization. *SIAM J. Optim.* 30(3):2272–2302, 2020. DOI: [10.1137/19M1242276](https://doi.org/10.1137/19M1242276)

[16] X. Jia, C. Kanzow, P. Mehlitz, G. Wachsmuth. An Augmented Lagrangian Method for Optimization Problems with Structured Geometric Constraints. *Math. Program.* 199:1365–1415, 2023. DOI: [10.1007/s10107-022-01870-z](https://doi.org/10.1007/s10107-022-01870-z)
更正：原列表作者写作 "X. Jia, R. I. Boţ, M. C. Mehlitz"，卷页写作 201:257–288, 2022；以上为 Crossref 记录

[17] G. N. Grapiglia, Y.-X. Yuan. On the Complexity of an Augmented Lagrangian Method for Nonconvex Optimization. arXiv:1906.05622. <https://arxiv.org/abs/1906.05622>
IMA J. Numer. Anal. 正式版本的卷期与年份待核对

---

## 已在本文中使用、但不在上表中的下界文献

- Carmon, Duchi, Hinder, Sidford. Lower Bounds for Finding Stationary Points I. *Math. Program.* 184:71–120, 2020（`carmon2020lower`）：§2.2 算法类、§2.3 式 (7) 的 inf–sup 复杂度
- Mahdavinia, Deng, Li, Mahdavi. Tight Analysis of Extra-gradient and Optimistic Gradient Methods for Nonconvex Minimax Problems. NeurIPS 2022（`mahdavinia2022tight`）：§5 Theorems 5.1–5.2，"对任意学习率"的方法专属下界；二次实例 + 线性时不变递推 + 特征值分析，与本文旋转分支的技术最接近
- Tian, So. No dimension-free deterministic algorithm computes approximate stationarities of Lipschitzians. *Math. Program.* 2024：§2.3 oracle、算法类、函数类的分段写法

---

## 从 GPT Pro 算法类与第 2 节草稿中抽取的文献

以下各条出现在 GPT Pro 给出的"Algorithm class and its scope"与"2. Problem Class and Complexity Model"草稿中。arXiv 条目已用 arXiv API 核对，期刊条目已用 Crossref 核对。

| 文献 | 核对后的元数据 | 草稿中的用途 | 本文中的状态 |
|---|---|---|---|
| Zheng, Zhu, So, Blanchet, Li. Universal Gradient Descent Ascent Method for Nonconvex-Nonconcave Minimax Optimization. NeurIPS 2023 | bib 已有 `zheng2023universal` | DS-GDA 的更新结构（§2, Algorithm 1），$r_1=1/\gamma$，$r_2=1/s$ | 已用于表 `tab:special-cases` |
| Zhang, Xiao, Sun, Luo. A Single-Loop Smoothed Gradient Descent-Ascent Algorithm for Nonconvex-Concave Min-Max Problems. NeurIPS 2020 | bib 已有 `zhang2020smoothed`（另有重复条目 `zhang2020single`，待合并） | Smoothed GDA 与交替 GDA（§3.1, Algorithms 1–2） | 已用于表 `tab:special-cases` |
| Li, Nagarajan, Pan, Zhang. Smoothing Meets Perturbation. arXiv:2602.14185 | 见上文 [1] | PSGDA（§3.1, 式 (3.1), Algorithm 3）；GS 与 OS 的区分（Definition 2.1） | 已用 |
| Carmon, Duchi, Hinder, Sidford. Lower Bounds for Finding Stationary Points I. Math. Program. 184:71–120, 2020 | bib 已有 `carmon2020lower` | 函数类的定义方式（§2.1, Definition 1）；算法类（§2.2）；首次达标时间与 inf–sup（§2.3, 式 (7)） | 已用于 Remark 2.9 |
| Mahdavinia, Deng, Li, Mahdavi. Tight Analysis of Extra-gradient and Optimistic Gradient Methods For Nonconvex Minimax Problems. NeurIPS 35, 2022 | bib 已有 `mahdavinia2022tight`；§5 Theorems 5.1–5.2 已核对原文 | "对任意学习率"的方法专属下界 | 已用于 `rem:lb-initialization` |
| M. Xu, B. Jiang, Y.-F. Liu, A. M.-C. So. A Riemannian Alternating Descent Ascent Algorithmic Framework for Nonconvex-Linear Minimax Problems on Riemannian Manifolds. arXiv:2409.19588 (v2) | 作者已核对；bib 中对应条目为 `xu2026rada`，期刊信息待核对 | RADA：§3.2 Definition 1(b) 对应"存在 KKT 证书"型准则；Definition 1(a) 的 GS 用近端梯度映射，不能直接写成 $R_k$ | 引言比较表已引用 |
| J. Li, L. Zhu, A. M.-C. So. Nonsmooth Nonconvex-Nonconcave Minimax Optimization: Primal-Dual Balancing and Iteration Complexity Analysis. arXiv:2209.10825；Math. Program. 214:591–641, 2025 | 作者已核对；bib 已有 `li2025nonsmooth` | Definition 3.1(b) 的 GS 在原始一侧使用包络残差，**不能作为本文 KKT 证书公式的直接出处** | 已用于 `def:eps-gs` 的引用；按此判断，引用时需写明"本文将其对偶侧的法锥换成 $\partial h^*$" |
| Y. Drori, M. Teboulle. Performance of First-Order Methods for Smooth Convex Minimization: A Novel Approach. Math. Program. 145:451–482, 2014. DOI: [10.1007/s10107-013-0653-0](https://doi.org/10.1007/s10107-013-0653-0) | Crossref 已核对 | 10-01 版证明中提到"把算法最坏表现写成优化问题"的性能估计（PEP）思想 | 未引用；可在第 4 节开头说明证明思路时引用 |
