### 演讲逐字稿（全文连贯版）

**[标题页 & 目录页]**

各位同仁、老师、同学，大家下午好。我是来自北京航空航天大学的李路轩，目前在 Boț 教授这里开展为期一年的交流访学。我的主要研究兴趣是一阶复合优化问题的算法设计与复杂度分析。今天我主要汇报一项关于**固定罚参数的对偶正则增广拉格朗日法（ALM）复杂度紧性估计**的结果。这项工作由我和导师崔春风教授，以及国防科技大学邓康康教授、清华大学胡江教授合作完成。

整个报告围绕一个问题展开：单环线性化 ALM 要达到 $\mathcal{O}(\epsilon^{-3})$ 的迭代复杂度，罚参数是否必须随精度增长。我们先说明这个问题如何从已有结果中产生，再给出我们得到的复杂度下界及其紧性，最后讨论几个关于加速的开放问题。

**[第 1 页：Problem]**

我们考虑非凸复合优化问题 (P)：极小化 $f(\mathbf{x}) + h(\mathcal{A}(\mathbf{x}))$。

这里的假设是标准的：$f$ 和非线性映射 $\mathcal{A}$ 是光滑的，非光滑项 $h$ 是凸且 $L_h$-Lipschitz 连续的函数，并且 $h$ 本身的近端算子 $\mathrm{prox}_{th}$ 容易计算。这一模型涵盖了 spectral risk 学习，其中 $h$ 是排序后样本损失的加权和，CVaR 是它的特例；也涵盖了 worst-group last-layer retraining，其中 $h$ 取各组损失的最大值。我们的目标是：在给定精度 $\epsilon > 0$ 下，刻画一阶方法找到该问题 $\epsilon$-KKT 点所需的迭代复杂度。

**[第 2 页：Handling $h\circ\mathcal{A}$]**

求解该问题的核心难点在于：尽管 $h$ 本身的近端算子好求，但它与非线性映射 $\mathcal{A}$ 复合之后，整体 $h\circ\mathcal{A}$ 的近端算子一般无法得到。

目前主流的处理方法分为四类：
- 次梯度算法，直接对目标函数求次梯度；
- prox-linear 方法，对内层的非线性映射 $\mathcal{A}$ 做线性化，每步求解一个凸复合子问题；
- 变量光滑化方法，用 Moreau 包络对 $h$ 做光滑近似；
- 原始-对偶分裂方法，通过引入辅助变量和乘子将 $h$ 与 $\mathcal{A}$ 解耦，每一步只通过近端算子调用 $h$。

**[第 3 页：Linearized ALM]**

我们重点关注第四类方法，其中最经典的代表是**线性化增广拉格朗日法（Linearized ALM）**。通过引入分裂变量 $\mathbf{y} = \mathcal{A}(\mathbf{x})$，我们将原问题重构为带非线性等式约束 $\mathcal{A}(\mathbf{x}) - \mathbf{y} = \mathbf{0}$ 的优化问题。

在每一轮迭代中，线性化 ALM 对增广拉格朗日函数 $\mathcal{L}_\rho(\mathbf{x},\mathbf{y},\boldsymbol{\lambda})$ 做一步关于 $\mathbf{x}$ 的梯度下降，随后对 $\mathbf{y}$ 做精确极小化，这等价于求一次 $h$ 的近端算子，最后对对偶乘子 $\boldsymbol{\lambda}$ 做一步步长为 $\rho$ 的对偶上升。这里需要注意，为了保证原始下降步的收敛性，$\mathbf{x}$ 的步长 $\eta$ 受到增广拉格朗日函数关于 $\mathbf{x}$ 的光滑常数 $L_{\mathbf{x}}(\rho)$ 的约束，因此步长直接依赖于罚参数 $\rho$。算法输出的精度用 $\epsilon$-KKT 点衡量，要求同时满足原始平稳性与约束可行性。罚参数 $\rho$ 既出现在步长的上界中，也将出现在可行性的估计中，下面的问题正是由此产生的。

**[第 4 页：Existing Nonconvex ALMs: Large Penalty]**

看表 1 中现有的非凸 ALM 工作可以发现：尽管单循环线性化 ALM 已经达到了目前已知最好的 $\mathcal{O}(\epsilon^{-3})$ 复杂度上界，但现有工作都有一个共同限制——需要采用大罚参数，罚参数或者逐步增大，或者取为 $\Theta(\epsilon^{-1})$，与目标精度 $\epsilon$ 相关。

我们可以用**约束可行性与迭代复杂度之间的权衡**来解释这一现象：
- 一方面，由于 $h$ 是 $L_h$-Lipschitz 连续的，乘子序列有界，约束可行性残差受 $2L_h/\rho$ 控制。为了保证可行性达到 $\epsilon$ 精度，就需要将罚参数取为 $\rho = \Theta(\epsilon^{-1})$；
- 但另一方面，关于 $\mathbf{x}$ 的光滑常数 $L_{\mathbf{x}}(\rho)$ 随 $\rho$ 线性增长。增大 $\rho$ 会恶化原始子问题的条件数，使步长 $\eta$ 缩小为 $\Theta(\epsilon)$，进而导致总体迭代复杂度由光滑问题的 $\mathcal{O}(\epsilon^{-2})$ 变为 $\mathcal{O}(\epsilon^{-3})$。

也就是说，已有的 $\mathcal{O}(\epsilon^{-3})$ 结果让罚参数一个量同时承担可行性与步长两方面的要求，而这两方面的要求方向相反。

我们将罚参数固定为常数 $\rho = \Theta(1)$、不依赖于精度 $\epsilon$ 的单循环 ALM 称为**固定罚参数线性化 ALM（fixed-penalty linearized ALM）**。这自然引出一个问题：**当罚参数固定为 $\rho = \Theta(1)$ 时，线性化 ALM 是否仍能达到 $\mathcal{O}(\epsilon^{-3})$ 的迭代复杂度？**

**[第 5 页：Problem (P) as a Minimax Problem]**

罚参数固定之后，可行性估计 $2L_h/\rho$ 只是一个常数，可行性必须由罚参数之外的量来控制。为了找到线性化 ALM 中还有哪些量可以起这个作用，我们先把它的迭代写成只含 $(\mathbf{x},\boldsymbol{\lambda})$ 的形式。

对增广拉格朗日函数 $\mathcal{L}_\rho(\mathbf{x},\mathbf{y},\boldsymbol{\lambda})$ 关于 $\mathbf{y}$ 显式求极小，就可以消去 $\mathbf{y}$，得到只含原始变量 $\mathbf{x}$ 和对偶变量 $\boldsymbol{\lambda}$ 的**约化增广拉格朗日函数** $\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})$，其中极小点 $\mathbf{y}(\mathbf{x},\boldsymbol{\lambda})$ 由步长为 $1/\rho$ 的近端算子给出。

这里有两个核心关系：
1. 对每一个固定的 $\rho > 0$，$\mathcal{D}_\rho$ 关于 $\boldsymbol{\lambda}$ 求极大就等于原目标函数 $F(\mathbf{x})$，因此求解原问题 (P) 等价于求解极小极大问题 $\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})$；
2. 取 $\mathbf{y}=\mathbf{y}(\mathbf{x},\boldsymbol{\lambda})$ 和 $\mathbf{q}=\boldsymbol{\lambda}+\rho(\mathcal{A}(\mathbf{x})-\mathbf{y})\in\partial h(\mathbf{y})$，关于 $\mathbf{x}$ 的梯度恰好是原始平稳性残差，而关于 $\boldsymbol{\lambda}$ 的梯度恰好就是约束可行性 $\mathcal{A}(\mathbf{x}) - \mathbf{y}$。因此该极小极大问题的 **$\epsilon$-博弈平稳点（$\epsilon$-game stationary point）**给出原问题的 $\epsilon$-KKT 点，可行性就是对偶梯度的范数。

`[click]` 因此，**对每一个固定的 $\rho > 0$，原问题 (P) 是一个光滑的非凸-凹极小极大优化问题。**

**[第 6 页：Linearized ALM as GDA]**

相应地，消去 $\mathbf{y}$ 之后，线性化 ALM 的迭代恰好就是在约化增广拉格朗日函数 $\mathcal{D}_\rho$ 上执行的**梯度下降-上升（GDA）算法**：原始变量以步长 $\eta$ 做梯度下降，对偶变量以罚参数 $\rho$ 为步长做梯度上升。这里的 GDA 与线性化 ALM 是同一个迭代的两种写法。

这一写法的作用在于，极小极大优化中改进 GDA 的技巧可以直接用在 ALM 上。对于 $\ell$-光滑的非凸-凹极小极大问题，2020 年 Lin 等人证明了朴素 GDA 的迭代复杂度为 $\mathcal{O}(\epsilon^{-6})$。为了在单循环中加速收敛，现有工作引入了两类正则化：对原始变量 $\mathbf{x}$ 增加围绕中心 $\mathbf{z}$ 的原始光滑项，对对偶变量 $\boldsymbol{\lambda}$ 增加围绕中心 $\boldsymbol{\mu}$、参数为 $s$ 的对偶正则项。把这两项加到 $\mathcal{D}_\rho$ 上，线性化 ALM 就多出了对偶正则参数 $s$ 和两个中心的更新方式这几个可调的量。第 4 页的问题需要一个罚参数之外控制可行性的量，候选就在这里。

**[第 7 页：Single-Loop GDA-Based Methods]**

从表 2 可以看到，引入这两项正则化后，单循环 GDA 的复杂度从最初的 $\mathcal{O}(\epsilon^{-6})$ 改进到了 $\mathcal{O}(\epsilon^{-4})$，并进一步提升到了 $\mathcal{O}(\epsilon^{-3})$。

然而观察表 2 的最后一行可以发现，Perturbed Smoothed GDA 为了达到 $\mathcal{O}(\epsilon^{-3})$ 的复杂度，取对偶正则参数 $s = \Theta(\epsilon^{-1})$，即 $1/s = \Theta(\epsilon)$。

`[click]` 从优化视角来看，这一行与第 4 页有相同的结构，只是承担增长的参数换成了 $s$：
- 一方面，对偶中心固定在零时，对偶正则项引入了量级为 $1/s$ 的对偶残差。为了得到原极小极大问题的 $\epsilon$-博弈平稳点，取 $s = \Theta(\epsilon^{-1})$ 以保证对偶平稳性达到 $\epsilon$ 精度；
- 另一方面，加入对偶正则后，对偶强凹问题的条件数为 $\kappa(s) = \ell s$。取 $s = \Theta(\epsilon^{-1})$ 会恶化对偶问题的条件数，使总体迭代复杂度由 $\mathcal{O}(\epsilon^{-2})$ 变为 $\mathcal{O}(\epsilon^{-3})$。

值得注意的是，这一方法作用在 $\mathcal{D}_\rho$ 上时，罚参数 $\rho$ 保持常数，增长的参数是 $s$。

**[第 8 页：Research Question]**

把这两个 $\mathcal{O}(\epsilon^{-3})$ 结果放在一起看：两者都让一个控制对偶残差的参数取到 $\Theta(\epsilon^{-1})$ 的量级，区别在于增长落在哪个参数上，代价也因此落在不同的地方。在线性化 ALM 中，增长落在罚参数 $\rho$ 上，放大了原始光滑常数 $L_{\mathbf{x}}(\rho)$，使原始步长 $\eta$ 缩小为 $\Theta(\epsilon)$；在 Perturbed Smoothed GDA 中，增长落在对偶正则参数 $s$ 上，原始步长不受影响，代价体现在对偶条件数 $\kappa(s)$ 上，中心步长 $\alpha$ 与 $1/\kappa(s)$ 同阶。

这自然引出我们想要研究的核心问题（Research Question），它包含两层：
**第一，单环线性化 ALM 要达到 $\mathcal{O}(\epsilon^{-3})$ 的迭代复杂度，是否必须让某个参数随 $1/\epsilon$ 增长？第二，如果必须，这一增长是否必须由罚参数 $\rho$ 承担？**

**[第 9–10 页：The LRALM Family & Special Cases]**

为了回答这一问题，我们把上述方法放进同一个单循环算法族——**线性化正则 ALM（LRALM，记作 $\mathcal{C}_\theta$）**。该算法族在约化增广拉格朗日函数 $\mathcal{D}_\rho$ 上同时加入原始光滑项与对偶正则项，参数 $\theta=(\rho,s,\gamma,\eta,\tau)$ 固定，两个正则中心 $\mathbf{z}^k$ 和 $\boldsymbol{\mu}^k$ 分别以常数步长 $(\alpha,\beta)\in[0,1]^2$ 更新。如表 3 所示，当 $(\alpha,\beta)$ 取不同值时，算法族 $\mathcal{C}_\theta$ 可以分别还原线性化 ALM，以及作用在 $\mathcal{D}_\rho$ 上的 Smoothed GDA、DS-GDA 和 Perturbed Smoothed GDA。

因此，第 4 页和第 7 页的方法属于同一个算法族，差别只在参数 $s$ 和中心步长 $(\alpha,\beta)$。研究问题也就可以在族内精确地表述：参数 $\theta$ 固定时，调节中心步长能否弥补参数增长的缺失。

**[第 11 页：Effective Penalty Parameter]**

在这一统一框架下，命题 1 给出了一个关键的结构性质：将正则化目标函数 $\mathcal{P}_s$ 关于对偶变量 $\boldsymbol{\lambda}$ 求极大，得到的结果恰好是罚参数为 **$\rho+s$**、乘子取对偶中心 $\boldsymbol{\mu}$ 的约化增广拉格朗日函数 $\mathcal{D}_{\rho+s}(\mathbf{x},\boldsymbol{\mu})$，再加上原始光滑项。

这一恒等式说明了两点：
1. **对偶正则参数 $s$ 起罚参数的作用，直接叠加在 $\rho$ 上**：对偶变量取最优之后，$\mathbf{x}$ 所面对的是罚参数为 $\rho+s$ 的增广拉格朗日函数，我们称 $\rho+s$ 为有效罚参数；
2. **原始光滑常数只依赖于 $\rho$**：$L_{\mathbf{x}}(\rho)=L_f+L_{\mathcal{A}}L_h+\rho G_{\mathcal{A}}^2$ 与 $s$ 无关，因此增大 $s$ 不会缩减原始步长 $\eta$。

由此可以看到，线性化 ALM 中的 $\rho=\Theta(\epsilon^{-1})$ 与 Perturbed Smoothed GDA 中的 $s=\Theta(\epsilon^{-1})$ 对应的是同一个要求：有效罚参数 $\rho+s$ 达到 $\epsilon^{-1}$ 的量级。这也说明，下界应当用 $\rho+s$ 来刻画。

**[第 12–13 页：Lower Bound & The Critical Order of $\rho+s$]**

基于这一结构，定理 1 给出了算法族 $\mathcal{C}_\theta$ 在标准问题类上的最坏情况复杂度下界：**对任意 $0<\eta\le\gamma$ 和 $\tau>0$，存在与 $(\rho,s,\alpha,\beta)$ 无关的常数 $c_1$，使得对充分小的 $\epsilon$，只要有效罚参数满足 $\rho+s \le c_1/\epsilon$，那么对任意常数中心步长 $(\alpha,\beta)\in[0,1]^2$，族内算法都至少需要 $\Omega(\epsilon^{-4})$ 次迭代。** 由于下确界取在中心步长上，有效罚参数不够大时，中心无论怎样移动都无法弥补。

结合第 13 页的图示，我们可以对前面研究问题的两层分别给出回答：
- **红色区域 I**：当 $\rho+s \le c_1/\epsilon$ 时，族内每一组常数中心步长都需要 $\Omega(\epsilon^{-4})$ 次迭代。罚参数固定时，取 $\beta=1$、$\alpha=\Theta(\epsilon^2)$，即作用在 $\mathcal{D}_\rho$ 上的 Smoothed GDA，可以达到 $\mathcal{O}(\epsilon^{-4})$，所以这一下界在 $\rho$ 固定时是紧的。这回答了第一层问题：在算法族 $\mathcal{C}_\theta$ 中，要突破 $\epsilon^{-4}$，有效罚参数 $\rho+s$ 必须达到 $\Theta(\epsilon^{-1})$ 量级，参数增长不可避免。
- **绿色点 II**：由于有效罚参数是 $\rho+s$，我们可以固定罚参数 $\rho = \Theta(1)$ 以保持原始子问题的良态性，同时取对偶正则参数 $s = c_s/\epsilon$，并取 $\beta=0$、$\alpha=c_\alpha\epsilon$，即作用在 $\mathcal{D}_\rho$ 上的 Perturbed Smoothed GDA，从而在固定罚参数下达到 $\mathcal{O}(\epsilon^{-3})$ 的迭代复杂度。这回答了第二层问题：增长不必由罚参数承担，可以全部由对偶正则参数 $s$ 承担，代价是中心步长取 $\Theta(\epsilon)$，原始步长保持常数。

**[第 14–15 页：Open Question & Acceleration Beyond $\mathcal{C}_\theta$]**

在绿色点 II 的参数尺度上，族内能否快于 $\epsilon^{-3}$，我们目前还没有下界刻画。由此产生最后一个问题：**对问题 (P)，固定罚参数 ALM 的最优迭代复杂度是多少，能否比 $\mathcal{O}(\epsilon^{-3})$ 更快？**

从第 14 页的已知结果来看，光滑非凸优化的一阶通用下界是 $\Omega(\epsilon^{-2})$；而对于对偶域有界的光滑非凸-凹极小极大问题，确定性一阶方法寻找 $\epsilon$-博弈平稳点的最优复杂度是 $\Theta(\epsilon^{-5/2})$。因此，$\mathcal{O}(\epsilon^{-3})$ 与 $\Omega(\epsilon^{-2})$ 之间仍存在明显的改进空间。同时，算法族 $\mathcal{C}_\theta$ 中的方法每步只做一次梯度下降-上升，而已知达到 $\epsilon^{-5/2}$ 的单循环方法使用了族外的更新。

翻到第 15 页，为了跳出 $\mathcal{C}_\theta$ 实现加速，一个重要的观察是：对偶正则项 $-\frac{1}{2s}\lVert\boldsymbol{\lambda}-\boldsymbol{\mu}\rVert^2$ 正是对偶问题上的 **Tikhonov 正则项**，它使对偶问题成为 $\frac{1}{s}$-强凹问题。基于这一视角，我们在两个设定下探讨潜在的加速方向：
1. **有限步复杂度设定（固定 $s = \Theta(\epsilon^{-1})$）**：在极小极大优化中，Zhang 和 Xu 的单循环方法使用同阶的 $s = \Theta(\epsilon^{-1})$，配合对偶动量和移动的近端中心，对博弈平稳性达到了 $\mathcal{O}(\epsilon^{-5/2})$ 复杂度；对于固定罚参数 ALM，设计怎样的更新格式能将复杂度从 $\mathcal{O}(\epsilon^{-3})$ 提升至 $\mathcal{O}(\epsilon^{-5/2})$？
2. **渐近收敛设定（令 $s_k \to \infty$）**：在单调算子问题中，逐渐消失的 Tikhonov 正则不仅能加速残差衰减，还能保证迭代序列强收敛到最小范数解；对于固定罚参数 ALM，当 $s_k \to \infty$ 时，迭代点会收敛到哪一个乘子，其收敛速度又是多少？

我的汇报就到这里，非常感谢大家的聆听，欢迎各位老师提问与指正。
