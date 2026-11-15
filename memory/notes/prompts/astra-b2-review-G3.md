# astra 审查指令：B2′ 的 G3（中心漂移与总势函数下降）及其复杂度推论

状态：待发送（2026-11-09）。审查对象：`notes/gpt-proofs/b2-G3-20261109.md`。已通过的前置关卡：`notes/gpt-proofs/b2-G0G1-20261109.md`、`notes/gpt-proofs/b2-G2-20261109.md`，审查记录见 `notes/progress/b2-review-G0G1-20261109.md`、`notes/progress/b2-review-G2-20261109.md`。

---

你是这份推导的审查人。你的任务是找出错误和缺口，不负责补全证明，也不改写推导。讨论用中文，引用公式时写明对象和条件。

## 背景

B2′ 的定义：对偶块做 Nesterov 外推，原始块做一步梯度，不含 OGDA 修正；中心步为 $\mathbf z^{k+1}=\mathbf z^k+\alpha(\mathbf x^{k+1}-\mathbf z^k)$，其中 $\alpha=c_\alpha\varsigma$，$\varsigma=\sqrt{\tau/s}$。G2 的定理 G2.4 给出固定中心下的一步收缩 $E_{k+1}\le(1-\varsigma)E_k$。

本关声称的结果如下：

- **总势函数**：$W_k=p_s(\mathbf z^k)+\tfrac12E_k$，其中 $p_s$ 是 $\Phi_s=\mathcal D_{\rho+s}(\cdot,\mathbf 0)$ 的 Moreau 包络。
- **下降不等式**：当 $c_\alpha\le1/6$ 时，

$$
W_{k+1}\le W_k-\frac{\alpha}{5\gamma}\lVert\mathbf x^{k+1}-\mathbf z^k\rVert^2-\frac{\varsigma}{4}E_k-\cdots
$$

- **中心漂移误差**：常数 $C_1$、$C_2$ 都与 $s$ 无关。
- **下界与初值间隙**：都与 $s$ 无关。
- **复杂度（Corollary G3.6）**：取 $s=c_s/\epsilon$、$K\gtrsim\Delta_W\sqrt{c_s/\tau}\,\epsilon^{-5/2}$，则 KKT 残差不超过 $\epsilon$。

## 请逐项审查

1. **Lemma G3.0**：G2.4 是否真的可以当作"任意状态、固定中心"的一步不等式使用？注意 $e_k$ 是在 $\mathbf z^k$ 处度量的，而 $\mathbf x^k$ 来自在 $\mathbf z^{k-1}$ 处的一步。G2.4 的证明有没有用到"历史迭代都在同一中心下生成"这一条件？
2. **$p_s$ 的正则性**：梯度公式 $\nabla p_s(\mathbf z)=(\mathbf z-\mathbf x^\star(\mathbf z))/\gamma$；对所有 $s$ 都有 $1/\gamma$-Lipschitz 性；$p_s$ 与原目标 $F$ 的关系及偏差 $L_h^2/(2(\rho+s))$。
3. **Lemma G3.2**：
   - $E$ 中每一个依赖 $\mathbf z$ 的项都已计入；
   - $\lVert\Delta\mathbf z\rVert^2/(2\gamma)$ 项的精确相消；
   - G2.2(ii) 用于界定值间隙关于 $\mathbf z$ 的梯度差；
   - 对偶距离项中三处 $s$ 的相消是否成立；
   - $C_1^2=10/(3\gamma^2\mu_\gamma)$、$C_2=4/(3\gamma^2\mu_\gamma)$ 是否正确。
4. **Young 不等式的拆分**：用 $(\varsigma/2)E_{k+1}(\mathbf z^k)$ 来吸收交叉项，代价是 $\alpha^2/\varsigma$；条件 (F1)、(F2) 是否只要求 $\alpha\lesssim\varsigma$；数值常数 $31/150$、$b_k\ge1/5$、$1/8$ 是否正确。
5. **总势函数下降**：每个负项的系数和符号；是否有一项被重复使用，例如同一份 $\varsigma E_k$ 既拿去吸收漂移，又拿去提供下降量。
6. **下界与 $W_0$**：$W_k\ge\inf F-L_h^2/(2(\rho+s))$；从零初值出发 $W_0-\inf W$ 不依赖 $s$；$\lVert\boldsymbol\lambda^\star(\mathbf z)\rVert\le sL_h/(\rho+s)$。
7. **Corollary G3.6 与 KKT 合成**：
   - 输出点是 $(\mathbf x^{k+1},\mathbf y(\mathbf x^{k+1},\bar{\boldsymbol\lambda}^k),\mathbf q(\mathbf x^{k+1},\bar{\boldsymbol\lambda}^k))$；
   - 原始 KKT 残差是 $\nabla_{\mathbf x}\mathcal D_\rho$，不是 $\nabla_{\mathbf x}\mathcal P_s$，二者相差 $(\mathbf x-\mathbf z)/\gamma$，这一项是否由 $\lVert\mathbf x^{k+1}-\mathbf z^k\rVert$ 的求和控制（G2 审查第 6 条）；
   - 对偶残差恒等式与偏差 $\bar C_\lambda L_h/s\le\epsilon$ 的条件 $c_s\ge2\bar C_\lambda L_h$；
   - 用"$\min_k$"或"同一指标"取出满足条件的 $k$ 时，两类量是否在同一指标上同时可控；
   - 最终阶是否为 $\epsilon^{-5/2}$，常数是否只依赖类常数和 $\rho,\gamma,\tau$。
8. **与原稿结论的关系**：B2′ 不在 $\mathcal C_\theta$ 中，所以 $\epsilon^{-5/2}$ 与族内 $\Omega(\epsilon^{-3})$ 下界不冲突。请确认这一说法所需的事实是否已经齐备。
9. **结论标注**：每条"已证"是否名副其实。

## 输出格式

逐条给出以下内容：

- **判定**：通过 / 缺口 / 不成立；
- **位置**：文件中的小节或公式；
- **理由**：一到三句；
- **影响**：是否会影响最终的 $\epsilon^{-5/2}$ 结论。

最后用三行总结：G3 能否放行；Corollary G3.6 的 $\epsilon^{-5/2}$ 能否放行；必须修改的项。
