# SPLALM 之后的加速问题：梳理与 GPT Pro 核验指令

状态：第一部分为当前逻辑（2026-10-26 讨论结论）；第二部分待发送给 GPT Pro。

---

# 第一部分：当前逻辑

## 1. 已证结果

- 族 $\mathcal C_\theta$：$s$ 为常数，中心步长 $(\alpha,\beta)\in[0,1]^2$ 为常数，单步 GDA。
- 要突破 $\epsilon^{-4}$，组合罚参数需满足 $\rho+s\gtrsim1/\epsilon$。罚参数 $\rho$ 固定时，$s\sim1/\epsilon$。
- 取 $s=c_s/\epsilon$ 时，全族复杂度为 $\Theta(\epsilon^{-3})$，对所有中心步长成立。

## 2. $\epsilon^{-3}$ 的机制

- 平台引理：原始中心 $z$ 每步最多前进 $\alpha\epsilon$，平台长度约 $\Delta/\epsilon$，所以 $K\gtrsim1/(\alpha\epsilon^2)$。
- 追踪约束：中心步长受内层追踪速度限制，$\alpha\lesssim1/s$。附录 `eq:ddlalm-parameter-schedule` 取 $\alpha_k=c/s_k$，用的就是这个约束。
- 两者合起来：$s\sim1/\epsilon$，$\alpha\sim\epsilon$，$K\sim\epsilon^{-3}$。
- 要得到 $\epsilon^{-2.5}$，需要把追踪约束放宽到 $\alpha\sim1/\sqrt{s}$。

## 3. 跳出族：两种加速

族内已经没有余地，下一步让 $\alpha_k,\beta_k,s_k$ 随迭代变化，并改变更新结构。

| 加速 | 效果 | 前提 | 代表 |
|---|---|---|---|
| momentum | 条件数 $\kappa\to\sqrt{\kappa}$ | 无 | Zhang–Xu 2026（单循环，dual momentum，GS $\epsilon^{-2.5}$） |
| Tikhonov / anchoring | 单调问题残差 $1/\sqrt{k}\to1/k$ | 权重 $1/s_k\to0$ | Boț–Nguyen 2024；Boț–Chenchene 2026 |

- 对偶正则 $-\frac{1}{2s}\lVert\lambda-\mu\rVert^2$ 就是以 $\mu$ 为 anchor、权重 $1/s$ 的 Tikhonov 项。$\mathcal P_s$ 加原始近端项后，固定中心的子问题是强凸–强凹的。
- $s$ 固定时，Tikhonov 权重不衰减，只提供强单调性。$s_k\uparrow\infty$ 时，进入 Boț 的设定。
- 我们想要的是第二种：不用 momentum，算法式子干净。

## 4. 速率天花板

一致（best-iterate）速率与复杂度的对应：

| 复杂度 | 一致速率 | 状态 |
|---|---|---|
| $\epsilon^{-4}$ | $k^{-1/4}$ | 族内低参数区域 |
| $\epsilon^{-3}$ | $k^{-1/3}$ | 当前（族内紧；附录 $s_k\sim k^{1/3}$） |
| $\epsilon^{-2.5}$ | $k^{-2/5}$ | 目标 |
| $\epsilon^{-2}$ | $k^{-1/2}$ | 天花板（Carmon 等人下界），在我们问题类上是否可达未知 |

last-iterate 是另一回事：
- 非凸问题不加结构时，last iterate 没有一般速率；已有非凸结果多为 best-iterate 或 running-best。
- KL 性质下有渐近 last-iterate 速率：$\theta\le1/2$ 线性，$\theta>1/2$ 为 $k^{-(1-\theta)/(2\theta-1)}$。
- 单调问题：EG 的 last iterate 为 $O(1/\sqrt{k})$；anchoring（EAG、FEG、Boț–Chenchene）为 $O(1/k)$，最优。
- 附录 `thm:main` 用的是 tail-best，不是 last-iterate。

## 5. 两个核心问题

**问题 1（有限时间）**：单循环、$\rho$ 固定、$s_k$ 可变，用 Tikhonov / anchoring（不用 momentum），能否把追踪约束从 $\alpha\sim1/s$ 放宽到 $\alpha\sim1/\sqrt{s}$，从而达到 $\epsilon^{-2.5}$，即一致速率 $k^{-2/5}$？

**问题 2（无穷时间）**：$s_k\to\infty$ 时，
- last-iterate 的 KKT 残差速率是多少？
- $\lambda^k$ 是否收敛到最小范数乘子？
- 对偶与可行性部分能否达到 $1/k$？

## 6. 讲给 Boț 的对应

| ALM 语言 | 他的语言 |
|---|---|
| 对偶正则 $-\frac{1}{2s}\lVert\lambda-\mu\rVert^2$ | 以 $\mu$ 为 anchor、权重 $1/s$ 的 Tikhonov 项 |
| $s_k\uparrow\infty$ | vanishing Tikhonov 权重 |
| 中心步长受 $\alpha\lesssim1/s$ 限制 | 漂移的强单调算子上的追踪速度 |
| 问题 1 | Tikhonov / anchoring 能否给出 $\sqrt{\kappa}$ 型加速 |
| 问题 2 | primal 块弱单调时，能否强收敛到最小范数零点、残差快速衰减 |

---

# 第二部分：发给 GPT Pro 的指令

请作为熟悉非凸约束优化、ALM、非凸–凹 minimax、单调算子与 anchoring / Tikhonov 加速的研究合作者，完成下面四项任务。讨论用中文；算法、命题、定理用英文 LaTeX，格式与所附论文一致（沿用论文的宏、环境、术语：SPLALM、center stepsize、combined penalty、$\epsilon$-KKT point、problem class $\mathcal I(\mathbf C,\Delta)$）。每项结论标「已证 / 待证 / 不成立」。证明多用标准技术和标准框架；可以简化，不要另辟蹊径。

附件：`overleaf/main.tex`、`overleaf/sections/*.tex`、`overleaf/appendix/*.tex`、`overleaf/notes/progress/PROJECT_STATUS.md`，以及本文件第一部分。上一轮核对记录：`ChatGPT-核查算法与下界-20261026-0749.md`。

## 背景

- 问题：$\min_{\bx}f(\bx)+h(\calA(\bx))$，$f,\calA$ 光滑，$h$ 凸且 $L_h$-Lipschitz；度量为 $\epsilon$-KKT。
- 已证：$\mathcal C_\theta$ 中突破 $\epsilon^{-4}$ 需 $\rho+s\gtrsim1/\epsilon$；$\rho$ 固定、$s=c_s/\epsilon$ 时全族 $\Theta(\epsilon^{-3})$。
- 允许跳出族：$\alpha_k,\beta_k,s_k$ 随迭代变化；更新结构可改为 EG 或 anchoring；保持单循环、$\rho$ 固定。

记 $\bw=(\bx,\blmbd)$，$\bc=(\bz,\bmu)$，
$$
F_0(\bw)=\bigl(\nabla_{\bx}\calD_\rho(\bx,\blmbd),\,-\nabla_{\blmbd}\calD_\rho(\bx,\blmbd)\bigr),\qquad
F_k(\bw)=F_0(\bw)+\Lambda_k(\bw-\bc^k),\qquad
\Lambda_k=\operatorname{diag}(\gamma^{-1}I_n,\,s_k^{-1}I_m).
$$
SPLALM 是 $F_k$ 上的交替 forward step。候选算法（$H=\operatorname{diag}(\eta I_n,\tau I_m)$）：

- 算法 A（显式 Tikhonov-EG）：$\hat\bw^k=\bw^k-HF_k(\bw^k)$，$\bw^{k+1}=\bw^k-HF_k(\hat\bw^k)$。
- 算法 B（按 Boț–Chenchene 对齐）：$\hat\bw^k=\bw^k-HF_k(\bw^k)$，$(I+H\Lambda_k)\bw^{k+1}=\bw^k-HF_0(\hat\bw^k)+H\Lambda_k\bc^k$。
- 两者的中心更新：$\bc^{k+1}=\bc^k+\operatorname{diag}(\alpha_kI_n,\beta_kI_m)(\bw^{k+1}-\bc^k)$。

## 任务一：文献核查（问题 1）

是否已有工作用 Halpern、anchoring、Tikhonov、对偶扰动或对偶阻尼，对非凸复合问题 $f+h(\calA(\bx))$、非凸约束问题的 ALM，或非凸–凹 minimax 实现加速？单循环、多循环都算。逐篇给出：算法结构（循环层数、momentum、EG、anchor、参数是否随精度或迭代变化）、问题类、驻点判据（OS / GS / $\epsilon$-KKT）、复杂度、加速来源，以及与问题 1 的关系（覆盖 / 部分覆盖 / 不覆盖）。

待核清单（可补充）：Li–Chen–Liu–Lu–Xu iALM（AISTATS 2021）；Kong–Monteiro AIDAL（arXiv:2110.11151）；LP-ALM / LIPAL（arXiv:2503.01056）；Zhang–Xu（arXiv:2609.17973）；Xu–Zhang–Xu–Lan AGP；Zheng et al. DS-GDA（arXiv:2212.12978）；Lee–Kim FEG（arXiv:2106.02326）与 SA-MGDA（arXiv:2105.15042）；Cai–Oikonomou–Zheng composite-EAG（arXiv:2206.05248）；Boț–Nguyen（arXiv:2406.00852）；Boț–Chenchene（arXiv:2410.14369）；Chen（arXiv:2605.30905）；Tikhonov primal–dual dynamics（arXiv:2609.06420、arXiv:2409.05301、arXiv:2411.17656）；Ramirez–Lacoste-Julien（arXiv:2509.22500）；NR-LALM（arXiv:2608.19847）；PPALA（arXiv:2406.17107）。

## 任务二：速率基准（问题 2）

1. 区分 best-iterate 与 last-iterate。给出我们问题类上 best-iterate 的已知上下界：Carmon 等人 $\Omega(\epsilon^{-2})$；Liu–Lin–Xu（MOR 2025，arXiv:2502.17770）的阶数及其问题类与我们的关系；Li et al.（arXiv:2609.14235v2）GS $\Omega(\epsilon^{-5/2})$ 能否转移到 $\mathcal I(\mathbf C,\Delta)$。
2. last-iterate 的现状：非凸 ALM、ADMM、NC-C 中已有的 last-iterate 结果（是否只有 KL 下的渐近速率，DS-GDA 等是否只有收敛无速率）；单调与 comonotone 情形的 last-iterate 基准（EG、EAG、FEG、composite-EAG）。
3. 结论：问题 2 的合理目标速率是什么。

## 任务三：Tikhonov 能否给出 $\sqrt{\kappa}$（问题 1 的核心）

1. $s$ 固定（可依赖 $\epsilon$）时，Tikhonov 项是否产生任何加速，还是只提供强单调性？给出判断与依据。
2. $s_k\uparrow$、配合 EG 或 anchoring 时，追踪约束能否从 $\alpha_k\lesssim1/s_k$ 放宽到 $\alpha_k\sim1/\sqrt{s_k}$？先在二次模型 $\frac{p}{2}x^2+ax\lambda-\frac{q_k}{2}\lambda^2$（$q_k=1/s_k$，中心移动）上推导，再说明一般问题类中对偶块曲率 $1/\rho$ 的影响。
3. 若能，给出 $s_k,\alpha_k,\beta_k,\eta,\tau$ 的取法与 $\epsilon^{-2.5}$ 的证明框架（Lyapunov 函数、追踪递推、KKT 转换）。若不能，给出反例或障碍，并说明 momentum 在该障碍处起的作用。

## 任务四：无穷时间（问题 2 的核心）

对算法 B 取 $s_k\uparrow\infty$：
1. $\lambda^k$ 收敛到最小范数乘子需要什么条件（KL、Hölderian error bound、局部正则解）？
2. last-iterate 的 KKT 残差能达到什么速率；对偶与可行性部分能否达到 $1/k$ 或 $o(1/k)$？
3. 写出对应的连续时间模型和 Lyapunov 函数草案。

## 交付

1. 文献核查表（中文，附可核实出处）。
2. 四项任务各自的结论段，标「已证 / 待证 / 不成立」。
3. 英文 LaTeX：算法定义、关键引理、目标定理或反例命题，论文格式。
