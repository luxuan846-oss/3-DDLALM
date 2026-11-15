# astra 审查指令：B2 的 G0（设定）与 G1（乘子有界性）

状态：待发送（2026-11-09）。审查对象：`notes/gpt-proofs/b2-G0G1-20261109.md`。

---

你是这份推导的审查人。你的任务是找出错误和缺口，不负责补全证明，也不改写推导。讨论用中文，引用公式时写明对象和条件。

## 背景

问题是 $\min_{\mathbf x} f(\mathbf x)+h(\mathcal A(\mathbf x))$。SPLALM 的定义见 `sections/AlgorithmFamily.tex` 第 1–62 行；$\beta=0$、$s=c_s/\epsilon$ 时的 $O(\epsilon^{-3})$ 证明见 `appendix/UpperBoundBetaZero.tex`。该证明的 Step 1 把 SPLALM 约化为 Li et al.（arXiv:2602.14185v2）的 Perturbed Smoothed GDA，作用在 $\mathcal D_\rho$ 和 $\mathcal Y=\{\lVert\boldsymbol\lambda\rVert\le2L_h\}$ 上。

B2 在这个设定上做了三处改动：对偶块加 Nesterov 外推 $\bar{\boldsymbol\lambda}^k=\boldsymbol\lambda^k+\theta_m(\boldsymbol\lambda^k-\boldsymbol\lambda^{k-1})$；原始块加 OGDA 修正；保持交替顺序，即对偶步使用 $\mathbf x^{k+1}$。目标参数为 $\theta_m=1-c\sqrt{\tau/s}$，$\alpha=c_\alpha\sqrt{\tau/s}$。

## 请逐项审查

1. **G0 的算法定义**：与 `def:splalm` 的记号、更新顺序、初始化是否一致；OGDA 项在 $k=0$ 时的约定是否良定。
2. **oracle 计数**：每步一次 $\mathcal O_{f,\mathcal A}$ 和两次 $\mathrm{prox}_h$ 是否正确，与 `def:splalm` 之后的缓存说明是否一致。
3. **常数表**：每个常数，包括原始光滑常数、原始强凸模数、对偶光滑常数、对偶强凹模数和耦合常数，是否与文中的定义和标签一致；有没有把 $\rho$ 或 $s$ 的依赖写错。
4. **G1 的对偶递推**：$\boldsymbol\lambda^{k+1}=a(1+\theta_m)\boldsymbol\lambda^k-a\theta_m\boldsymbol\lambda^{k-1}+b\mathbf q^k$ 这个恒等式是否成立，$a$ 和 $b$ 是否算对。
5. **G1 的 BIBO 界**：
   - 脉冲响应的 $\ell_1$ 界是否对所有 $\theta_m\in[0,1)$ 一致成立；
   - 实根情形和复根情形是否都覆盖了，$a$ 接近 $0$ 或 $1$ 的端点是否处理了；
   - 常数 $C$ 是否真的不依赖 $s$ 和 $\theta_m$；
   - 初值 $\boldsymbol\lambda^{-1}=\boldsymbol\lambda^0=\mathbf 0$ 是否用对。
6. **约化是否仍然成立**：把 $\mathcal Y$ 放大到半径 $CL_h$ 之后，附录 C 里依赖半径的常数（例如 $D_{\mathcal Y}$）是否仍然是 $\Theta(1)$；外推点 $\bar{\boldsymbol\lambda}^k$ 越出 $\mathcal Y$ 会不会影响约化。
7. **结论标注**：每条"已证"是否名副其实，有没有把"待证"写成了"已证"。

## 输出格式

逐条给出以下内容：

- **判定**：通过 / 缺口 / 不成立；
- **位置**：文件中的小节或公式；
- **理由**：一到三句；
- **影响**：是否会影响 G2–G4。

最后用三行总结：G0 能否放行；G1 能否放行；必须修改的项。
