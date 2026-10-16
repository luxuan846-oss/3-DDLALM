# 待查方向：PPALA 靠哪一步逃出 $\mathcal C_\theta$

记录日期：2026-10-16（Booming 草稿体检第 2 轮）

## 问题

PPALA（Kim, Chandra, Hashemi, Brinton, 2024, arXiv:2406.17107）声称在固定参数下，对非凸函数约束问题达到 $\widetilde O(\epsilon^{-2})$。本文 `thm:lower-bound` 说：在 $\mathcal C_\theta$ 内，$\epsilon(\rho+s)\le c_1$ 时任何常数中心步长都需要 $\Omega(\epsilon^{-4})$。

- 若 PPALA 的有限步可行性成立，"参数增长是必要的"只在族内成立。
- 值得提前投入的问题：PPALA 用了哪一步结构（更新顺序、外推、乘子更新方式、问题类假设、驻点判据）逃出 $\mathcal C_\theta$。

## 为什么重要

五年后会被延续的问题，是这个问题类上单环方法的最优复杂度。族内下界一旦遇到 $\mathcal A_{\det}$ 上的 oracle 下界，就会变成推论（`rem:family-not-oracle` (ii)）。弄清 PPALA 逃出族的那一步，可以决定本文的必要性结论该怎样表述，也给出下一篇的题目。

## 要核对的事项

1. PPALA 的问题类：约束是否为函数约束 $g(x)\le0$，是否需要 Slater 条件或其他正则性条件；与 $f+h\circ\mathcal A$ 的对应关系。
2. 驻点判据：是否和本文 $\epsilon$-KKT 一致。
3. 可行性论证：引言（`sections/Introduction.tex` 约 165–170 行）称其依赖渐近论证，需要确认有限步可行性界是否成立。
4. 算法结构：对照 `def:splalm`，找出 PPALA 中不属于 $\mathcal C_\theta$ 的那一步。
5. 若该步可以加进 SPLALM，看本文旋转实例和 Huber 实例在哪一行失效。

## 机制线索（来自本文证明）

对偶最优响应处有

$$
\mathbf q=\boldsymbol\mu+(\rho+s)\bigl(\mathcal A(\mathbf x)-\mathbf y\bigr),\qquad
\lVert\mathcal A(\mathbf x)-\mathbf y\rVert=\frac{\lVert\mathbf q-\boldsymbol\mu\rVert}{\rho+s}.
$$

$\rho+s$ 固定时，可行性只能靠对偶中心 $\boldsymbol\mu$ 追上真乘子。固定参数的方法若要达到 $\epsilon^{-2}$，它的乘子更新必须追得比常数 $\beta$ 的中心平均更快；这是核对第 4 项时首先要看的地方。

## 同时记下的决定

- 标题可以改：现标题 "Keep the Penalty" 与组合罚参数洞察方向相反，阶上看不出 $\rho$ 与 $s$ 的区别。重心移向"组合罚参数的临界阶 $\epsilon^{-1}$"。

## 待定：Keep the Penalty 的定量收益（第 2 轮问题 (a1)）

按 `eq:beta0-stepsizes`，β=0 上界中 $\eta=\Theta(1/\ell)$、$\tau=\Theta(1/\ell)$，与 $\epsilon$ 无关；小步长落在中心步长 $\alpha=\Theta(\epsilon)$。增大 $\rho$ 的方法（GDPA，$\rho_k=\Theta(\epsilon^{-1})$）的小步长落在原始梯度步 $\eta$ 上（待验证）。两者迭代阶都是 $\epsilon^{-3}$。

要做的事：
1. 写一条定理级陈述：步长 $(\eta,\tau)$ 与 $\epsilon$ 无关，$C'$ 对 $\ell$（以及 $G_{\mathcal A}$、$L_h$）的依赖显式写出。
2. 查 GDPA (Lu, ICML 2022) 的步长与常数，逐项对比。
3. 若常数上看不出差别，改用实验展示 $\rho$ 增大时原始子问题的病态。

## 第 4 轮补充：上侧区域与已有方法的对应（2026-10-16 查证）

**LP-ALM**（El Bourkhissi, Necoara, Patrinos, Tran-Dinh, arXiv:2503.01056）。对偶更新为 $y^{k+1}=\tau y^0+(1-\tau)y^k+\rho F(x^{k+1})$，$\tau\in(0,1]$。Theorem 4.16 要求 $\rho\gtrsim\tau/\epsilon$。Remark 4.18：$\tau$ 固定时为 $O(\epsilon^{-3})$；$\tau=O(\epsilon^\eta)$ 时为 $O(\epsilon^{-3-2\eta})$。
- 粗对应（待核对；结构不同：它的原始步是 prox-linear 子问题，非光滑项是 $g(x)$，约束 $F(x)=0$）：取 $y^0=0$ 对应 $\beta=0$；对偶步长取 $\rho$ 时，其 $\tau$ 对应 $\rho/s$，即 $s=\rho/\tau$。
- $\tau$ 固定：$\rho\asymp s\asymp 1/\epsilon$，落在对角线上，不在 $\rho$ 轴上。
- $\tau=\Theta(\epsilon)$、$\rho=O(1)$：$s\asymp 1/\epsilon$，落在本文的 $s$ 轴上，但没有原始中心，复杂度 $O(\epsilon^{-5})$；本文 β=0 加 $\alpha=\Theta(\epsilon)$ 得 $\epsilon^{-3}$。这说明 $s$ 轴上起作用的是原始光滑化。
- $\rho=c/\epsilon$、$s$ 固定对应 $\tau\asymp1/\epsilon>1$，超出 LP-ALM 的参数范围。最接近的是 β=1、α=1 的大罚参数线性化 ALM。

**NR-LALM**（Liu, Deng, Wang, Wen, arXiv:2608.19847, 2026-08-20）。光滑非凸等式约束，固定罚参数，经典乘子更新，确定性 $O(\epsilon^{-2})$。原始步是一次正定线性方程组（Gauss–Newton 型），不在 $\mathcal C_\theta$ 内。与 PPALA 同属"固定参数逃出族"的例子，引言必须讨论。
