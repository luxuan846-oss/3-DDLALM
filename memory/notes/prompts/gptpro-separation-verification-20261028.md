# GPT Pro 指令：两条 $\epsilon^{-5/2}$ 路线的证明（2026-10-28，精简版）

状态：待发送。附件：`overleaf/main.tex`、`overleaf/sections/*.tex`、`overleaf/appendix/*.tex`、`overleaf/notes/progress/PROJECT_STATUS.md`、Zhang–Xu arXiv:2609.17973 全文。文献查新另见 `gptpro-balanced-penalty-litcheck-20261028.md`。

---

请作为熟悉非凸约束优化、ALM 与非凸–凹 minimax 复杂度的合作者，完成下面两个证明任务和一个文献任务。只做离散时间的 Lyapunov 分析，不用连续时间模型。证明沿用附录 C（`appendix/UpperBoundBetaZero.tex`）的框架、记号与宏，用标准技术。讨论用中文；定理、引理、证明用英文 LaTeX。每条结论标「已证 / 待证 / 不成立」。

## 背景

问题 $\min_{\mathbf x}f(\mathbf x)+h(\mathcal A(\mathbf x))$，$h$ 凸且 $L_h$-Lipschitz，度量 $\epsilon$-KKT。论文已证：SPLALM 族在 $\rho+s=O(1)$ 时 $\Theta(\epsilon^{-4})$；$\rho=O(1)$、$s=c_s/\epsilon$、$\beta=0$ 时 $\Theta(\epsilon^{-3})$。$\epsilon^{-3}=\epsilon^{-2}\times\epsilon^{-1}$，其中 $\epsilon^{-2}$ 来自非凸驻点，$\epsilon^{-1}$ 来自固定中心时内层问题的收缩率 $1-\Theta(1/s)$，它决定中心步长 $\alpha\lesssim1/s$。目标：把内层收缩率提到 $1-\Theta(1/\sqrt s)$，使 $\alpha\asymp\sqrt\epsilon$，得到 $\epsilon^{-5/2}$。

两个事实可以直接使用：$\mathcal D_\rho$ 关于 $\mathbf x$ 的弱凸模数为 $L_f+L_{\mathcal A}L_h$，不随 $\rho$ 增大，光滑常数为 $L_x\asymp L_f+L_{\mathcal A}L_h+\rho G_{\mathcal A}^2$；$\lVert\mathbf q(\mathbf x,\boldsymbol\lambda)\rVert\le L_h$ 对所有 $(\mathbf x,\boldsymbol\lambda)$ 成立。

## 任务 A：无动量、均衡罚参数（主任务）

算法为 Definition `def:splalm` 取 $\beta=0$、$\tau=\rho$：

$$
\mathbf x^{k+1}=\mathbf x^k-\eta\bigl(\nabla_{\mathbf x}\mathcal D_\rho(\mathbf x^k,\boldsymbol\lambda^k)+\tfrac1\gamma(\mathbf x^k-\mathbf z^k)\bigr),\qquad
\boldsymbol\lambda^{k+1}=\bigl(1-\tfrac\rho s\bigr)\boldsymbol\lambda^k+\rho\bigl(\mathcal A(\mathbf x^{k+1})-\mathbf y(\mathbf x^{k+1},\boldsymbol\lambda^k)\bigr),\qquad
\mathbf z^{k+1}=\mathbf z^k+\alpha(\mathbf x^{k+1}-\mathbf z^k).
$$

参数：$\rho=c_\rho\epsilon^{-1/2}$，$s=c_s\epsilon^{-1}$，$\eta=c_\eta/L_x$，$\alpha=c_\alpha\epsilon^{1/2}$，$\gamma$ 固定。

证明迭代复杂度 $O(\epsilon^{-5/2})$，或给出断点。证明须含三条引理：
1. 乘子有界（无投影）：$\lVert\boldsymbol\lambda^k\rVert\le L_h/(1-\rho/s)$。
2. 固定中心时内层一步收缩率 $\ge c\min\{\rho/s,\ \eta\mu_x\}$，其中 $\mu_x=1/\gamma-(L_f+L_{\mathcal A}L_h)$。
3. 追踪递推：$\alpha\le c'\min\{\rho/s,\eta\mu_x\}$ 时中心移动误差被吸收。

逐项列出常数对 $\rho$ 的依赖（$L_x$、初值间隙、偏差 $L_h/(\rho+s)$、KKT 转换常数），确认总阶为 $\epsilon^{-5/2}$。并写一句话说明：$\rho=O(1)$ 时同一算法为何停在 $\epsilon^{-3}$。

## 任务 B：固定 $\rho$、EG + 对偶动量、无投影

算法为 Zhang–Xu Algorithm 1 作用于 $\mathcal P_k(\mathbf x,\boldsymbol\lambda)=\mathcal D_\rho(\mathbf x,\boldsymbol\lambda)+\frac1{2\gamma}\lVert\mathbf x-\mathbf z^k\rVert^2-\frac1{2s}\lVert\boldsymbol\lambda\rVert^2$，**保留 EG 预测–校正与对偶动量，去掉投影 $\Pi_{\mathcal Y}$、法锥变量 $\xi_t,n_t$ 与 warm-up**。记 $F_k=(\nabla_{\mathbf x}\mathcal P_k,-\nabla_{\boldsymbol\lambda}\mathcal P_k)$，$h$ 为共同步长：

$$
\tilde{\mathbf x}^k=\mathbf x^k-h\nabla_{\mathbf x}\mathcal P_k(\mathbf x^k,\boldsymbol\lambda^k),\qquad
\tilde{\boldsymbol\lambda}^k=\boldsymbol\lambda^k+h\bigl[\nabla_{\boldsymbol\lambda}\mathcal P_k(\mathbf x^k,\boldsymbol\lambda^k)+\mathbf v^k\bigr],
$$

$$
\bar{\mathbf v}^k=\omega\mathbf v^k+c\,\nabla_{\boldsymbol\lambda}\mathcal P_k(\tilde{\mathbf x}^k,\tilde{\boldsymbol\lambda}^k),\qquad
\mathbf x^{k+1}=\mathbf x^k-h\nabla_{\mathbf x}\mathcal P_k(\tilde{\mathbf x}^k,\tilde{\boldsymbol\lambda}^k),\qquad
\boldsymbol\lambda^{k+1}=\boldsymbol\lambda^k+h\bigl[\nabla_{\boldsymbol\lambda}\mathcal P_k(\tilde{\mathbf x}^k,\tilde{\boldsymbol\lambda}^k)+\bar{\mathbf v}^k\bigr],
$$

$$
\mathbf v^{k+1}=\omega\mathbf v^k+c\,\nabla_{\boldsymbol\lambda}\mathcal P_k(\mathbf x^{k+1},\boldsymbol\lambda^{k+1}),\qquad
\mathbf z^{k+1}=\mathbf z^k+\alpha(\mathbf x^{k+1}-\mathbf z^k).
$$

参数沿用 Zhang–Xu (4.3)：$h=1/(64L_G)$，$1-\omega\asymp h\sqrt{L/s}$，$c\asymp hL$（即 $(1-\alpha_{\rm ZX})\gamma_{\rm ZX}$），$\alpha\asymp h\sqrt{L/s}$；$\rho,\gamma$ 为常数，$s=c_s\epsilon^{-1}$。对应关系：Zhang–Xu 的 $f\leftrightarrow\mathcal D_\rho$，$\lambda_{\rm ZX}\leftrightarrow1/\gamma$，$\tau_{\rm ZX}\leftrightarrow1/s$，$\beta_{\rm ZX}\leftrightarrow\alpha$。

可直接使用的恒等式：

$$
\nabla_{\boldsymbol\lambda}\mathcal P_k(\mathbf x,\boldsymbol\lambda)=\frac1\rho\bigl(\mathbf q(\mathbf x,\boldsymbol\lambda)-\boldsymbol\lambda\bigr)-\frac1s\boldsymbol\lambda,\qquad \lVert\mathbf q(\mathbf x,\boldsymbol\lambda)\rVert\le L_h .
$$

因此 $(\boldsymbol\lambda,\tilde{\boldsymbol\lambda},\mathbf v)$ 的递推是以 $\mathbf q$ 为有界输入的线性系统，系数含 $1/\rho+1/s\ge1/\rho$，$\mathbf x$ 只通过 $\mathbf q$ 进入。

1. **乘子有界性（无投影）**：用上述恒等式证明 $\sup_k(\lVert\boldsymbol\lambda^k\rVert+\lVert\tilde{\boldsymbol\lambda}^k\rVert+\lVert\mathbf v^k\rVert)=O(L_h)$，写出所需的 Jury/Schur 条件，确认它们在 (4.3) 的参数下成立且与 $\epsilon$ 无关。
2. **Lyapunov 证明**：乘子有界后，迭代始终位于半径 $2L_h$ 的球内部，法锥项恒为零。据此逐条说明 Zhang–Xu §4 与附录 9 的 Lyapunov 论证（Theorem 4.1、Lemma 4.1–4.2）在去掉投影后哪些步骤原样成立、哪些需要修改，并给出 $\epsilon$-KKT 复杂度 $O(\epsilon^{-5/2})$ 的完整定理与证明。
3. **初值**：从全零初值出发，不用 warm-up，确认 $\bar\Delta_0$（其 (4.20)）在 $\mathcal I(\mathbf C,\Delta)$ 上一致有界；写出复杂度中 $L$、$L_h$、$\Delta$ 的依赖。
4. **可选（不影响主结论）**：若 EG 预测步只保留对偶块、原始块用单步梯度，上面的证明是否仍成立；给出判断即可，不必证明。

## 任务 C：参考文献（只要最关键的，每类不超过三篇）

对下面三类各给出最直接的出处，写明定理号与结论，用于论文相关工作：
1. 强凸–强凹 minimax 中非加速方法的 $\kappa$ 与加速方法的 $\sqrt{\kappa_x\kappa_y}$（下界与上界各一篇）。
2. 单循环 minimax 的对偶动量或类似机制（Zhang–Xu 之外若有）。
3. Fast-OGDA（Boț–Csetnek–Nguyen）的离散版本：它在强单调情形的速率是 $\kappa$ 还是 $\sqrt\kappa$ 型；它对任务 B 是否有直接用处。

## 交付

1. 任务 A 的定理与完整证明，或断点。
2. 任务 B 的乘子有界引理与 $O(\epsilon^{-5/2})$ 定理及证明，或断点。
3. 任务 C 的文献表（中文，附 arXiv 号）。
4. 一句话总结两条路线各自的代价：A 的 $\rho\asymp\epsilon^{-1/2}$，B 的 EG 预测步与动量变量（每步两次梯度、两次 prox）。
