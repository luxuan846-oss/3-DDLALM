# 2026-10-01 核对记录：DS-GDA 对应、文献原文核对、ρ 一致性（Claude 联网 + 本地数值）

状态记号：verified = 对照 arXiv 原文（本轮抓取，经摘要模型转述，关键处建议人工对一眼）；inference = 推导；to be verified = 未核实。

## 1. 文献核对
| 项 | 结论 | 状态 |
|---|---|---|
| DS-GDA（arXiv:2212.12978）Algorithm 1 | x^{t+1}=proj_X(x^t−c∇_xF(x^t,y^t,z^t,v^t))；y^{t+1}=proj_Y(y^t+α∇_yF(x^{t+1},y^t,z^t,v^t))；z^{t+1}=z^t+β(x^{t+1}−z^t)；v^{t+1}=v^t+μ(y^{t+1}−v^t)。Gauss–Seidel，与 SPLALM 四步顺序一致。X、Y 假设为凸紧集。Thm 1：凹对偶时 O(T^{-1/4})-GS，即 ε^{-4} | verified（PDF 与 HTML 两次抓取一致；Li et al. Algorithm 2 的 Smoothed GDA 同一顺序） |
| 记号对照（易混） | DS-GDA 的 (c, α, β, μ) ↔ 我们的 (η, τ, α, β)。DS-GDA 的 α 是对偶步长，不是中心步长 | verified |
| Li–Nagarajan–Pan–Zhang（arXiv:2602.14185） | Thm 3.2（Perturbed GDA）、Thm 3.4（PSGDA：GS Ω(ℓ²D_YΔ/ε³)）、Cor 3.1（Smoothed GDA：GS 与 OS 均 Ω(ℓ³D_Y²Δ/ε⁴)）均限定在各自定理的步长条件（Thm 3.1 / 3.3 / Condition 3.2）之下运行；Remark 3.3(iii)：GS 下 Smoothed GDA 需 β=Θ(ε²/(ℓD_y²))，PSGDA 只需 Θ(ε/(ℓD_y)) | verified。下界不是对所有步长成立 |
| arXiv:2609.17973 | 标题 Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex–Concave Minimax Optimization；作者 Minhao Zhang, Zi Xu；投影阻尼外梯度 + 对偶动量 + 移动近端中心；NC-C：OS O(ε^{-3})，GS O(ε^{-5/2})；对偶正则 τ=min{L, ε/(2D_Y)}（GS） | verified（一次 HTML 抓取 + 搜索标题） |
| Pan–Zheng–Li（arXiv:2609.14235） | 作者 Siyu Pan, Taoli Zheng, Jiajin Li；确定性一阶 oracle，OS，Θ(ℓ²D_YΔ/ε³)，匹配上界 Tracked-FOAM | verified。**笔记里写的"Remark 3.3：GS 可达 O(ε^{-5/2})"本轮没有在抓取文本中找到，to be verified**；GS 的 ε^{-5/2} 改引 2609.17973 |
| GDPA（arXiv:2207.05650，Lu, ICML 2022） | 单环，O(ε^{-3})；惩罚参数 β_r∼r^{1/3} 递增，τ 固定；即 ρ_k=Θ(1/ε)（r=ε^{-3} 时） | verified（作者姓名未在抓取文本中出现，沿用 bib key） |
| MIALM（arXiv:1911.09900） | Kang-Kang Deng, Zheng Peng, *An inexact augmented Lagrangian method for nonsmooth optimization on Riemannian manifold*；**A 为线性算子**（矩阵），流形上；用 Moreau 包络得到光滑子问题；乘子更新 Z^{k+1}=Z^k−ρ_k(AX^{k+1}−Y^{k+1})（符号与我们相反）；收敛定理同时分析 ρ_k 有界与 ρ_k→∞ 两种情形；双循环（子问题不精确求解）。原文未直接使用幻灯片里的 M_h^{1/σ}(Ax−λ/σ)−‖λ‖²/(2σ) 写法 | verified |

## 2. 更正此前表述
1. 此前把 GS 的 ε^{-5/2} 归给 Pan–Zheng–Li 的 Remark 3.3：未核实。可靠出处是 2609.17973。
2. 此前写"MIALM/Hu–Deng：罚参数或精度随迭代变化，因此不在类内"：MIALM 的收敛分析允许 ρ_k 有界；不在常数类内的理由只剩"双循环 + 子问题精度趋零"。且 MIALM 是线性 A，我们的类是非线性 A。

## 3. ρ 一致性：精确约化（推导 + 数值）
在 prox 为零的区域 {(x,λ): λ+ρA(x)∈∂h(0)}（对 h=‖·‖₂ 即 ‖λ+ρA(x)‖≤1，h(0)=0）：
  D_ρ(x,λ) = f(x) + (ρ/2)‖A(x)‖² + ⟨λ,A(x)⟩，且 y(x,λ)=0，q=λ+ρA(x)。
所以 SPLALM_ρ 在该区域内的更新，恰好等于对 f̃ = f + (ρ/2)‖A‖² 的 DS-GDA 更新（对偶步不含 h*，因为 λ 在 ∂h(0) 内部时 h* 为常数）。
推论：DS-GDA（ρ=0）的困难实例 (f̃, A, h)，取 f = f̃ − (ρ/2)‖A‖²，即得 SPLALM_ρ 的同轨迹困难实例；A、h、初值、轨迹均不变。b~ε 时 ρ‖A(x)‖² 的修正是 O(ρ ε²)，只在 ε_θ 中产生对 ρ 的温和依赖，K_θ 不含 ρ。小 α 分支（A≡0）与 ρ 无关。
数值（本地 numpy，标量约化的 4×4 递推：f=−κx²/2，A=bx，b=24ε，ε=1e-3，γ=1，η=τ=0.5，s=1）：
- 对 ρ∈{0,0.5,1,5}、α∈{0.01,0.1,1}、β∈{1e-3,0.1,1} 共 36 组，均存在 κ* 使谱半径恰为 1（一对共轭特征值，|ζ|=1 到 1e-10）。
- κ*=(ρ+c(α,β))·b²，c(α,β) 与 ρ 无关（例：α=0.01,β=0.001 时 c=1.0949，ρ=0,0.5,1,5 分别得 κ*/b²=1.0949,1.5949,2.0949,6.0949）。即 ρ 的作用恰为 κ 平移 ρb²，与上面的恒等式一致。
- 沿单位模轨道（振幅 0.2，约两个周期）：min_k R_k/ε ≥ 1.88，且 ‖ρbx+λ‖≤0.61≤1（轨道不离开 prox 为零区域）。ρ=0 与 ρ=1 的 R_k 数值逐位相同。
- 退化情形：ρ=0、α=β=1 时 κ*=0，即无 f 的双线性博弈上交替 GDA 本身就有单位模特征值。
局限：这是对笔记里二维实例的标量约化重建，未复现 GPT Pro 证明中的二维构造和 R_k≥2ε 的严格论证；它核对的是机制与 ρ 无关，不替代证明。

## 4. 对论文的影响
- 类定义可写成 ρ∈[0,ρ̄] 的统一模板；Smoothed GDA（ρ=0, s=∞）、DS-GDA（ρ=0, s 固定）、SPLALM（ρ>0, s 固定）同属一类，下界定理一次覆盖。
- 在 prox 为零的区域，"ALM = 对 f+ρ/2‖A‖² 的 DS-GDA"，这是模板与 minimax 的精确桥梁，可写成一个 Proposition。
- DS-GDA 的紧性（ε^{-4} 下界）此前无人给出；本定理在常数中心步长类内给出，需注明 Li et al. 2026 对 Smoothed GDA / PSGDA 的结果仅在其步长条件下成立。
