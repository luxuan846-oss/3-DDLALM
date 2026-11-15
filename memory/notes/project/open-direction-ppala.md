# 待查方向：PPALA 靠哪一步逃出 $\mathcal C_\theta$

> 待验证的研究方向，2026-10-16 更新。当前任务优先级见 `notes/progress/PROJECT_STATUS.md`。本次修正讨论中的推断范围，未新增文献原文核查。

记录日期：2026-10-16（Booming 草稿体检第 2 轮）

## 问题

PPALA（Kim, Chandra, Hashemi, Brinton, 2024, arXiv:2406.17107）声称在固定参数下，对非凸函数约束问题达到 $\widetilde O(\epsilon^{-2})$。本文 `thm:lower-bound` 说：在 $\mathcal C_\theta$ 内，$\epsilon(\rho+s)\le c_1$ 时任何常数中心步长都需要 $\Omega(\epsilon^{-4})$。

- 本文“参数增长是必要的”始终限定于定理指定的算法族、问题类和步长条件；这一范围不依赖 PPALA 是否成立。
- 值得提前投入的问题：PPALA 用了哪一步结构（更新顺序、外推、乘子更新方式、问题类假设、驻点判据）逃出 $\mathcal C_\theta$。

## 为什么重要

值得继续研究的问题是：不同单环方法通过哪些结构改善复杂度。原判断“族内下界一旦遇到 oracle 下界，就会变成推论”已撤回：同一问题类、同一度量下，oracle 下界虽可向子族转移，但不能因此获得更高阶的参数区域下界。对照 PPALA 的价值在于辨认更新结构、假设或判据带来的差别。

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

该恒等式适用于对偶最优响应处。下一步从 `def:splalm` 推导包含对偶更新增量的实际迭代关系，考察中心跟踪速度与复杂度的联系，以及 PPALA 的更新是否体现这一机制。

## 同时记下的决定

- 用户接受调整标题；重心拟放在参数区域上的必要条件及组合罚参数的作用。$\rho$ 与 $s$ 的迭代复杂度作用不能仅凭恒等式视为相同；大 $\rho$、固定 $s$ 的族内结论尚未确定。新标题待定。

## 待定：Keep the Penalty 的定量收益（第 2 轮问题 (a1)）

按 `eq:beta0-stepsizes`，β=0 上界中 $\eta=\Theta(1/\ell)$、$\tau=\Theta(1/\ell)$，与 $\epsilon$ 无关；小步长落在中心步长 $\alpha=\Theta(\epsilon)$。增大 $\rho$ 的方法（GDPA，$\rho_k=\Theta(\epsilon^{-1})$）的小步长落在原始梯度步 $\eta$ 上（待验证）。两者迭代阶都是 $\epsilon^{-3}$。

要做的事：
1. 写一条定理级陈述：步长 $(\eta,\tau)$ 与 $\epsilon$ 无关，$C'$ 对 $\ell$（以及 $G_{\mathcal A}$、$L_h$）的依赖显式写出。
2. 查 GDPA (Lu, ICML 2022) 的步长与常数，逐项对比。
3. 若需要实验，围绕明确的问题比较不同参数增长方案的实际效率，并解释观察到的差异。

## 第 4 轮补充：上侧区域与已有方法的对应

以下为 2026-10-16 的讨论线索，文献结论、参数映射与跨算法比较待对照原文核实。

**LP-ALM**（El Bourkhissi, Necoara, Patrinos, Tran-Dinh, arXiv:2503.01056）。对偶更新为 $y^{k+1}=\tau y^0+(1-\tau)y^k+\rho F(x^{k+1})$，$\tau\in(0,1]$。Theorem 4.16 要求 $\rho\gtrsim\tau/\epsilon$。Remark 4.18：$\tau$ 固定时为 $O(\epsilon^{-3})$；$\tau=O(\epsilon^\eta)$ 时为 $O(\epsilon^{-3-2\eta})$。
- 粗对应（待核对；结构不同：它的原始步是 prox-linear 子问题，非光滑项是 $g(x)$，约束 $F(x)=0$）：取 $y^0=0$ 对应 $\beta=0$；对偶步长取 $\rho$ 时，其 $\tau$ 对应 $\rho/s$，即 $s=\rho/\tau$。
- $\tau$ 固定：$\rho\asymp s\asymp 1/\epsilon$，落在对角线上，不在 $\rho$ 轴上。
- $\tau=\Theta(\epsilon)$、$\rho=O(1)$：$s\asymp 1/\epsilon$，落在本文的 $s$ 轴上，但没有原始中心，复杂度 $O(\epsilon^{-5})$；本文 β=0 加 $\alpha=\Theta(\epsilon)$ 得 $\epsilon^{-3}$。这提出原始光滑化是否解释速率差异的问题；问题类和更新结构尚未统一，不能由此比较直接得出因果结论。
- $\rho=c/\epsilon$、$s$ 固定对应 $\tau\asymp1/\epsilon>1$，超出 LP-ALM 的参数范围。最接近的是 β=1、α=1 的大罚参数线性化 ALM。

**NR-LALM**（Liu, Deng, Wang, Wen, arXiv:2608.19847, 2026-08-20）。光滑非凸等式约束，固定罚参数，经典乘子更新，确定性 $O(\epsilon^{-2})$。原始步是一次正定线性方程组（Gauss–Newton 型），不在 $\mathcal C_\theta$ 内。作为固定罚参数方法的对照，需核对其问题假设与原始步结构；其与本文的关系不应由参数取值单独判断。
