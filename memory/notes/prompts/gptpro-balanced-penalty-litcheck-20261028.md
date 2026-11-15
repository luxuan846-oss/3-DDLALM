# GPT Pro 文献调研指令：均衡罚参数的单循环 ALM 是否已有先例（2026-10-28）

状态：待发送。附件：`overleaf/main.tex`、`overleaf/sections/*.tex`、`overleaf/appendix/*.tex`、`overleaf/notes/progress/PROJECT_STATUS.md`（第 7 节）。

---

请作为熟悉非凸约束优化与 ALM 复杂度理论的合作者，核查下面这个算法与参数路径是否已有文献做过。直接给判断，不要加免责说明。讨论用中文，算法与复杂度用 LaTeX。

## 待核查的对象

问题：$\min_{\mathbf{x}} f(\mathbf{x})+h(\mathcal{A}(\mathbf{x}))$，$f$ 与 $\mathcal{A}$ 光滑，$h$ 凸且 $L_h$-Lipschitz；度量为 $\epsilon$-KKT。

算法：论文中的 SPLALM 取 $\beta=0$（对偶中心固定为 $0$）、对偶步长 $\tau=\rho$。每步为

$$
\mathbf{x}^{k+1}=\mathbf{x}^{k}-\eta\Bigl(\nabla_{\mathbf{x}}\mathcal{D}_\rho(\mathbf{x}^{k},\boldsymbol{\lambda}^{k})+\tfrac{1}{\gamma}(\mathbf{x}^{k}-\mathbf{z}^{k})\Bigr),\qquad
\boldsymbol{\lambda}^{k+1}=\Bigl(1-\tfrac{\rho}{s}\Bigr)\boldsymbol{\lambda}^{k}+\rho\bigl(\mathcal{A}(\mathbf{x}^{k+1})-\mathbf{y}^{k+1}\bigr),\qquad
\mathbf{z}^{k+1}=\mathbf{z}^{k}+\alpha(\mathbf{x}^{k+1}-\mathbf{z}^{k}),
$$

其中 $\mathbf{y}^{k+1}=\mathrm{prox}_{h/\rho}(\mathcal{A}(\mathbf{x}^{k+1})+\boldsymbol{\lambda}^{k}/\rho)$。单循环，无动量、无外推、无 anchoring。

参数路径：$\rho\asymp\epsilon^{-1/2}$，$s\asymp\epsilon^{-1}$（阻尼 $\rho/s\asymp\epsilon^{1/2}$），$\eta\asymp1/(L+\rho G_{\mathcal{A}}^2)$，$\alpha\asymp\epsilon^{1/2}$，$\gamma$ 固定。

声称（待验证）：迭代复杂度 $O(\epsilon^{-5/2})$。机制：内层收缩率受 $\tau\lesssim\rho$ 与 $\eta\lesssim1/(\rho G_{\mathcal{A}}^2)$ 两个上限约束，因而不超过 $\min\{\rho/s,1/\rho\}$；在 $\rho+s\gtrsim1/\epsilon$ 的门槛下，$\rho\asymp\epsilon^{-1/2}$ 使之最大。一般地，$K\asymp\epsilon^{-2}\max\{\rho,1/(\epsilon\rho)\}$。

## 任务

1. **查新。** 是否有文献在非凸约束优化、非凸复合优化或非凸–凹 minimax 中，用罚参数（或对偶正则权重）取 $\epsilon^{-1/2}$ 量级、不加动量的单循环方法得到 $\epsilon^{-5/2}$？也包括凸情形下「罚参数与步长平衡」的先例。逐篇给出：算法结构（循环层数、是否加速）、罚参数与对偶步长的尺度、驻点判据、复杂度，以及与上面对象的关系（相同 / 相近 / 无关）。
2. **对照已知的 $\epsilon^{-5/2}$ 结果。** iALM（Li–Chen–Liu–Lu–Xu 2021）、AIDAL（Kong–Monteiro, arXiv:2110.11151）、DPALM（Dahal–Liu–Xu, arXiv:2311.09065）、Zhang–Xu（arXiv:2609.17973）。对每篇写明：罚参数尺度、平方根的来源（内层加速 / 对偶动量 / 其他）、是否单循环。
3. **判断机制。** 「不加速方法的内层收缩率不超过 $\min\{\rho/s,1/\rho\}$」这一说法，在二次模型或已有文献中是否有依据或反例。若有文献对不加速方法给出 $\max\{L_{xx}/\mu_x,L_{yy}/\mu_y,L_{xy}/\sqrt{\mu_x\mu_y}\}$ 型的收缩率，请给出处。
4. **结论。** 用一句话回答：这条参数路径是新的，还是已有文献的特例。若是特例，指明哪篇、哪个定理。

## 交付

- 文献表（中文，附 arXiv 号或 DOI）。
- 任务 2 的对照表。
- 任务 3、4 的判断，各标「已有 / 待证 / 不成立」。
