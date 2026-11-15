# astra 审查指令：B2 的 G2（固定中心收缩引理）

状态：待发送（2026-11-09）。审查对象：`notes/gpt-proofs/b2-G2-20261109.md`。已通过的前置关卡：`notes/gpt-proofs/b2-G0G1-20261109.md`（审查记录见 `notes/progress/b2-review-G0G1-20261109.md`）。

---

你是这份推导的审查人。你的任务是找出错误和缺口，不负责补全证明，也不改写推导。讨论用中文，引用公式时写明对象和条件。这一关是整个 $\epsilon^{-5/2}$ 证明的核心，请从严审查。

## 背景

B2′ 是 B2 去掉原始 OGDA 修正后的版本：中心固定为 $\mathbf z$；对偶块做 Nesterov 外推，$\bar{\boldsymbol\lambda}^k=\boldsymbol\lambda^k+\theta_m(\boldsymbol\lambda^k-\boldsymbol\lambda^{k-1})$；原始步为 $\mathbf x^{k+1}=\mathbf x^k-\eta\nabla_{\mathbf x}\mathcal P_s(\mathbf x^k,\bar{\boldsymbol\lambda}^k)$；对偶步为 $\boldsymbol\lambda^{k+1}=\bar{\boldsymbol\lambda}^k+\tau\nabla_{\boldsymbol\lambda}\mathcal P_s(\mathbf x^{k+1},\bar{\boldsymbol\lambda}^k)$。

推导声称：在 $\gamma L_{\mathcal D,\mathbf x}\le1/10$、$\eta=\gamma$、$\tau\le\min\{\rho/4,1/(14\gamma G_{\mathcal A}^2)\}$、$s\ge\max\{\rho,4\tau\}$、$\theta_m=(1-\varsigma)/(1+\varsigma)$（其中 $\varsigma=\sqrt{\tau/s}$）的条件下，有 $E_{k+1}\le(1-\varsigma)E_k$。Nesterov 模型函数建在 $Q_k=\mathcal P_s(\mathbf x^{k+1},\cdot)$ 上。

## 请逐项审查

1. **二次模型结论**（第 1 节）：根的展开式；$\eta\mu_x\ge1/2$ 的必要性；"OGDA 修正无益、反而缩小稳定区"的论证。请特别注意：对 B2 的窗口结论只覆盖三个参数区域，区域之间的过渡段并未覆盖。
2. **Lemma G2.1**：每一个模型不等式的方向和符号；$Q_k$ 作为对偶目标的凹性与光滑常数是否对所有 $\boldsymbol\lambda$ 成立；$\Gamma_k^+-(1-\varsigma)\Gamma_k$ 的定义及其非负性。
3. **动量位移项**：被 $-\Gamma_k$ 抵消的位移项 $\varpi_k$，是否就是 Lemma G2.3 中推动跟踪误差的那一项；两处的常数是否相容。
4. **原始跟踪收缩** $1-\eta\mu$：前提 $\eta\le2/(\mu+L_x)$ 是否被 $\eta=\gamma$ 和 $\gamma L_{\mathcal D,\mathbf x}\le1/10$ 蕴含。
5. **Theorem G2.4**：四处系数检验；$c_e$、$c_r$ 的取值；收缩因子是否确实为 $1-\varsigma$，并且对所有 $s\ge\max\{\rho,4\tau\}$ 一致成立。
6. **$E_k$ 控制的量**：$\lVert\boldsymbol\lambda^{k+1}-\bar{\boldsymbol\lambda}^k\rVert^2\le8\tau E_k$、原始梯度界、$\lVert\mathbf x^{k+1}-\mathbf x^\star\rVert^2\le20E_k/\mu_\gamma$、$\lVert\boldsymbol\lambda^k-\boldsymbol\lambda^\star\rVert^2\le2sE_k$ 的推导和常数。
7. **中心敏感度**：$\lVert\mathbf x^\star(\mathbf z')-\mathbf x^\star(\mathbf z)\rVert\le\lVert\delta\mathbf z\rVert/(\gamma\mu_\gamma)$ 与 $\lVert\boldsymbol\lambda^\star(\mathbf z')-\boldsymbol\lambda^\star(\mathbf z)\rVert\le\sqrt s\lVert\delta\mathbf z\rVert/(2\gamma\sqrt{\mu_\gamma})$ 是否已证、常数是否正确。
8. **新条件与原稿的关系**：$\gamma L_{\mathcal D,\mathbf x}\le1/10$ 与 $\theta_m=(1-\varsigma)/(1+\varsigma)$ 是否和 G0/G1 的结论相容，尤其是 G1 中 $\theta_m$ 为常数、$\nu=\tau(1/\rho+1/s)\lt1$ 这两个前提。
9. **结论标注**：每条"已证"是否名副其实。

## 输出格式

逐条给出以下内容：

- **判定**：通过 / 缺口 / 不成立；
- **位置**：文件中的小节或公式；
- **理由**：一到三句；
- **影响**：是否会影响 G3–G4。

最后用三行总结：G2 能否放行；必须修改的项；G3 需要从 G2 继承哪些结论。
