# 01-acceleration-routes

- **Source session**: `6bf893a3 (1/3)`
- **Span (local time)**: 2026-11-08 23:40 to 2026-11-09 00:54
- **User turns**: 51

---

## User (2026-11-08 23:40)

**结论与周报框架**

面向不熟悉鞍点加速文献的合作者或导师，周报应删去所有繁琐的代数细节，只传递**四个核心模块**：
1. **一个拆解公式**：为什么现稿卡在 $\epsilon^{-3}$，以及为什么单循环加速的理论目标是 $\epsilon^{-2.5}$；
2. **一张加速策略分类表**：文献里三种叫“加速”的工具（锚定、外推、动量）分别管什么，为什么只有动量能降下最后这 $0.5$ 阶；
3. **一份对 Zhang–Xu（2026）的去包装解读**：剥掉 4 个外围包装后，他们的核心算法只有 4 行，以及他们真正解决的证明难点是什么；
4. **一张我们的可行方案决策表**：我们自己做 $\epsilon^{-2.5}$ 的三条具体路线（方案 A、方案 B1、方案 B2）各自的改法、计算代价与理论新意。

下面给出可直接用作周报正文的凝练版本。

---

## 一、问题拆解：为什么现稿是 $\epsilon^{-3}$，怎么到 $\epsilon^{-2.5}$？

在现稿中我们已经证明：固定罚参数 $\rho=\Theta(1)$ 时，要保证可行性残差 $\le \epsilon$，对偶正则参数必须取 $s = \Theta(\epsilon^{-1})$。当原始中心 $\mathbf{z}^k$ 固定时，内层正则化目标函数为：

$$
\mathcal{P}_k(\mathbf{x},\boldsymbol{\lambda}) = \mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda}) + \frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}^k\rVert^2 - \frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2
$$

此时内层是一个**强凸–强凹（SC-SC）鞍点问题**，但两侧条件数严重不平衡：
- **原始块 $\mathbf{x}$（不病态）**：由 $\frac{1}{\gamma} > \ell$ 提供强凸模数 $\mu_x = \frac{1}{\gamma}-\ell = \Theta(1)$，光滑常数 $L_x = \Theta(1)$，条件数 $\kappa_x = \Theta(1)$；
- **对偶块 $\boldsymbol{\lambda}$（唯一瓶颈）**：强凹模数仅为 $\mu_\lambda = \frac{1}{s} = \Theta(\epsilon)$，光滑常数为 $\frac{1}{\rho}=\Theta(1)$，条件数 $\kappa_\lambda \sim \frac{s}{\rho} = \Theta(\epsilon^{-1})$。

任何单循环算法的总迭代复杂度都可以拆成两个因子的乘积：

$$
K \asymp \epsilon^{-2} \times \frac{1}{\alpha} \asymp \epsilon^{-2} \times \frac{1}{\delta_{\mathrm{inner}}}
$$

- **第一项 $\epsilon^{-2}$（不可降）**：外层非凸函数寻找 $\epsilon$-驻点的硬下界（Carmon 等，对应我们的平台引理）；
- **第二项 $\frac{1}{\alpha} \asymp \frac{1}{\delta_{\mathrm{inner}}}$（可加速）**：中心移动步长 $\alpha$ 最大只能取到内层子问题的单步收缩率 $\delta_{\mathrm{inner}}$。
  - **现稿状态（不加速）**：普通单步 GDA 的内层收缩率受制于对偶条件数倒数 $\delta_{\mathrm{inner}} \sim \kappa_\lambda^{-1} \sim \frac{\rho}{s} \sim \epsilon$，故 $\alpha\sim\epsilon$，总复杂度为 **$\Theta(\epsilon^{-3})$**。
  - **加速目标（开根号）**：强凸–强凹问题的一阶加速下限是将条件数开根号，使内层收缩率提升至 $\delta_{\mathrm{inner}} \sim \kappa_\lambda^{-1/2} \sim \sqrt{\frac{\rho}{s}} \sim \epsilon^{1/2}$，从而放宽中心步长至 $\alpha\sim\epsilon^{1/2}$，总复杂度降至 **$\mathcal{O}(\epsilon^{-2.5})$**。

---

## 二、策略梳理：文献中的三种“加速”分别管什么？

优化与鞍点文献中常提到的“加速”包含三种完全不同的机制。下表说明它们各自的作用位置，以及为什么从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$ 必须引入动量：

| 加速策略 | 典型操作 | 在鞍点问题中管哪一部分 | 能把内层代价降到多少 | 在我们问题中的结论 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 锚定 / Tikhonov 正则**（Anchoring / Halpern） | 往初始点拉回，或加 $-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$ | 管**无曲率（$\mu_\lambda=0$）**时的单调算子残差，提供 $1/s$ 的人工曲率 | 从 $\epsilon^{-2}$ 降到 $s\sim\epsilon^{-1}$（总复杂度 **$\epsilon^{-4}\to\epsilon^{-3}$**） | **红利已在 $\epsilon^{-3}$ 用完**。当系统已有曲率 $1/s$ 时，锚定不放大步长，无法把 $s$ 开根号 |
| **2. 算子外推 / 乐观修正**（EG / OGDA / PDHG 外推） | 预测–校正双步，或加一步梯度差 $F(\mathbf{w}^k)-F(\mathbf{w}^{k-1})$ | 管**跨块反对称耦合项** $\langle\boldsymbol{\lambda},\mathcal{A}(\mathbf{x})\rangle$，提供超前相位以抵消旋转发散 | **不改变条件数阶数**，在 $1/s$ 强凹下仍需 $s\sim\epsilon^{-1}$ 步（总复杂度仍为 **$\epsilon^{-3}$**） | **单独用不能降阶**，但它是加动量时防止耦合方向振荡发散的**必要稳定器** |
| **3. 惯性动量**（Nesterov / 梯度累加器） | 点外插 $\boldsymbol{\lambda}^k+\theta(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$，或梯度累加 $\mathbf{v}^{k+1}=\omega\mathbf{v}^k+c\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k$ | 管**病态强凹对角块** $-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$，在平缓方向累加约 $\sqrt{s}$ 步同向梯度 | 把条件数 $s$ 开根号为 $\sqrt{s}\sim\epsilon^{-1/2}$（总复杂度 **$\epsilon^{-3}\to\epsilon^{-2.5}$**） | **固定 $\rho=\Theta(1)$ 下突破 $\epsilon^{-3}$ 的核心机制**；且只需加在对偶块上，原始块 $\kappa_x=\Theta(1)$ 无需动量 |

---

## 三、文献解读：Zhang–Xu（2026）的本质是什么？

Zhang–Xu（`arXiv:2609.17973`）在有界对偶域非凸–凹 minimax 问题上做到了单循环 $\mathcal{O}(\epsilon^{-2.5})$。把他们论文中处理有界闭集边界和初值常数的**四个外围包装（球投影 $\Pi_{\mathcal{Y}}$、法锥变量 $\xi_t,n_t$、Warm-up 预热循环、随机采样输出）全部剥除后**，其核心内容浓缩为以下三点：

### 1. 它的核心算法就是“在我们的 $\mathcal{P}_k$ 上做双步 EG + 对偶动量”
固定步长 $h=\Theta(1)$、动量增益 $c=\Theta(1)$，每步更新仅四行：

$$
\tilde{\mathbf{x}}^k = \mathbf{x}^k - h\nabla_{\mathbf{x}}\mathcal{P}_k(\mathbf{x}^k,\boldsymbol{\lambda}^k), \qquad \tilde{\boldsymbol{\lambda}}^k = \boldsymbol{\lambda}^k + h\bigl(\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k(\mathbf{x}^k,\boldsymbol{\lambda}^k) + \mathbf{v}^k\bigr)
$$

$$
\mathbf{x}^{k+1} = \mathbf{x}^k - h\nabla_{\mathbf{x}}\mathcal{P}_k(\tilde{\mathbf{x}}^k,\tilde{\boldsymbol{\lambda}}^k), \qquad \boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + h\bigl((1+c)\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k(\tilde{\mathbf{x}}^k,\tilde{\boldsymbol{\lambda}}^k) + \omega\mathbf{v}^k\bigr)
$$

$$
\mathbf{v}^{k+1} = \omega\mathbf{v}^k + c\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k(\mathbf{x}^{k+1},\boldsymbol{\lambda}^{k+1}), \qquad \mathbf{z}^{k+1} = \mathbf{z}^k + \alpha(\mathbf{x}^{k+1}-\mathbf{z}^k)
$$

其中对偶正则取 $s\asymp\epsilon^{-1}$，动量衰减率取 $\omega = 1-\Theta(\sqrt{1/s}) = 1-\Theta(\epsilon^{1/2})$，中心步长取 $\alpha = \Theta(\sqrt{1/s}) = \Theta(\epsilon^{1/2})$。

### 2. 它为什么能成？（低通滤波机制）
累加器 $\mathbf{v}^k$ 的有效记忆窗口为 $\frac{1}{1-\omega}\asymp\sqrt{s}$ 步。在对偶曲率 $1/s$ 的慢方向上，梯度长期同向，$\mathbf{v}^k$ 的稳态幅值达到 $\frac{c}{1-\omega}\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k \asymp \sqrt{s}\,\nabla_{\boldsymbol{\lambda}}\mathcal{P}_k$，等效于把慢方向步长放大了 $\sqrt{s}$ 倍；而在耦合旋转方向上，梯度正负交替相互抵消，配合双步 EG 保持稳定。

### 3. 它真正攻克的证明难点是什么？（为什么不能直接抄现成的强凸–强凹加速定理）
在单循环中，中心 $\mathbf{z}^k$ 每步都在动，对偶鞍点 $\boldsymbol{\lambda}^\star(\mathbf{z}^k)$ 随中心漂移的敏感度高达 $\lVert\Delta\boldsymbol{\lambda}^\star\rVert \lesssim s\alpha \sim \epsilon^{-1/2}$。如果直接照搬静态强凸–强凹加速算法的欧氏距离势函数 $\lVert\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^\star(\mathbf{z}^k)\rVert^2$，中心漂移误差会直接把步长卡死在 $\alpha\lesssim\epsilon^{3/2}$。Zhang–Xu 的核心证明贡献是构造了**以鞍点值函数间隙 $\mathcal{P}_k-\mathcal{P}_k^\star(\mathbf{z}^k)$ 与交叉项 $\langle\mathbf{v}^k,\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^\star(\mathbf{z}^k)\rangle$ 为主体的 Lyapunov 函数**，利用包络定理避开了对 $\boldsymbol{\lambda}^\star(\mathbf{z}^k)$ 求导。

---

## 四、我们的可行方案对比（三条具体路线）

结合我们 ALM 的独有结构（对偶梯度 $\nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho = \frac{1}{\rho}(\mathbf{q}-\boldsymbol{\lambda})$ 因 $\lVert\mathbf{q}\rVert\le L_h$ 自带向原点的恢复力，**天然无需人工球投影和法锥变量**），我们推进 $\mathcal{O}(\epsilon^{-2.5})$ 有以下三条可行方案：

| 方案名称 | 具体改法（相对现稿 $\beta=0$ 的 SPLALM） | 每步计算量 | 与 Zhang–Xu 的区别及优势 | 当前证明状态与难点 |
| :--- | :--- | :--- | :--- | :--- |
| **方案 A：均衡罚参数版**（无动量、族内直接提速） | **算法公式一字不改**（三行单步更新，$\tau=\rho$）；只把参数从 $\rho=\Theta(1)$ 改为 **$\rho\asymp\epsilon^{-1/2},\ s\asymp\epsilon^{-1}$**，$\eta\asymp\epsilon^{1/2},\ \alpha\asymp\epsilon^{1/2}$ | **1 次梯度 + 1 次 $\mathrm{prox}_h$**（无投影、无额外变量） | **机理完全不同**。利用 $\mathcal{D}_\rho$ 弱凸模数 $\ell=L_f+L_{\mathcal{A}}L_h$ 不随 $\rho$ 增大的性质，直接把对偶步长放大到 $\tau=\rho\sim\epsilon^{-1/2}$ 来把内层收缩率提到 $\frac{\rho}{s}\sim\epsilon^{1/2}$，完全不用动量和 EG | 数值已验证成立；仿射 $\mathcal{A}$ 下可借 PDHG 度量闭合，一般非线性 $\mathcal{A}$ 需补一条利用两次 $\mathrm{prox}$ 增量关联的收缩引理 |
| **方案 B1：固定 $\rho$ 的无投影 EG + 对偶动量版**（稳妥保底） | 保持 $\rho=\Theta(1),\ s\asymp\epsilon^{-1}$，采用上面剥离投影后的 Zhang–Xu 四行格式 | 2 次梯度 + 2 次 $\mathrm{prox}_h$（**无投影、无 Warm-up**） | 利用 ALM 中 $\lVert\mathbf{q}\rVert\le L_h$ 的有界恢复力，砍掉 Zhang–Xu 的球投影、法锥变量和预热循环；配合我们已证的族内 $\Omega(\epsilon^{-3})$ 下界，构成**“固定 $\rho$ 下对偶动量是突破 $\epsilon^{-3}$ 的充要条件”**的分离定理 | **确定性最高**。只需证一条线性递推乘子有界引理（$\sup_k\lVert\boldsymbol{\lambda}^k\rVert=\mathcal{O}(L_h)$），即可直接接入 Zhang–Xu 的 Lyapunov 主不等式 |
| **方案 B2：固定 $\rho$ 的单梯度外推 + 对偶动量版**（最简结构探索） | 保持 $\rho=\Theta(1),\ s\asymp\epsilon^{-1}$，在对偶侧加常数系数 Nesterov 动量 $\theta=1-c\sqrt{\rho/s}$，并用**一步历史差分（OGDA）或原始耦合外推（PDHG）**代替双步 EG | **1 次梯度 + 1 次 $\mathrm{prox}_h$**（计算量比 Zhang–Xu 减半） | 在固定 $\rho=\Theta(1)$ 下把双步 EG 化简为单步更新，每轮少算 1 次梯度和 1 次 $\mathrm{prox}_h$ | **难度最高**。需要把 Zhang–Xu 依赖双步 EG 的值函数型 Lyapunov 证明改写到单步交替/外推格式上，耦合项的稳定性待证 |

---

### 五、周报建议推进顺序（一句话结论）

1. **近期最稳妥的定理产出（保底）**：先写定**方案 B1**（无投影 EG + 对偶动量）与现稿族内 $\Theta(\epsilon^{-3})$ 紧下界的**分离定理**，证明链条只差一条简单的乘子有界引理。
2. **最具区分度的新结果（冲刺）**：并行攻关**方案 A**（$\rho\asymp\epsilon^{-1/2}$ 无动量三行 SPLALM，先从仿射 $\mathcal{A}$ 或加 PDHG 外推写起）或**方案 B2**（单梯度对偶动量版）的固定中心与移动中心 Lyapunov 引理。

**核心要义：向团队汇报时，只需用 $K\asymp\epsilon^{-2}/\delta_{\mathrm{inner}}$ 说明加速核心是把对偶慢块收缩率从 $1/s$ 提到 $1/\sqrt{s}$；用“锚定管 $\epsilon^{-4}\to\epsilon^{-3}$、动量管 $\epsilon^{-3}\to\epsilon^{-2.5}$、外推管旋转稳定”厘清文献策略；最后给出“方案 A（调 $\rho\sim\epsilon^{-1/2}$ 免动量）”与“方案 B（固定 $\rho$ 加对偶动量、免投影）”两条清晰路径供决策。**  我认为这个说的也太啰嗦了 也不清晰

---

## Assistant (2026-11-08 23:41)

读者：不熟悉鞍点加速文献的合作者或导师。

## 改了什么

- **删掉的内容**：Zhang–Xu 的四行算法、"低通滤波"解释、四个外围包装的清单，以及所有中间量级推导。读者做决策用不到这些。
- **改正的两处过度表述**：
  1. 原稿说"固定 $\rho$ 下对偶动量是突破 $\epsilon^{-3}$ 的**充要条件**"，这个说法不成立。族内下界只覆盖现稿的 $(\alpha,\beta)$ 族，推不出动量是必要的。所以改成"与族内下界构成**分离**"。
  2. 原稿说 B1"只需证一条乘子有界引理即可接入 Zhang–Xu 的 Lyapunov 主不等式"。Zhang–Xu 的论证建立在有界对偶域上，换成无界的 $\boldsymbol{\lambda}$ 后是否真的只差这一条，我们还没核对过。所以改写为"主要缺口"。
- **补的一句**：方案 A 改变了 $\rho$，不在族内 $\Theta(\epsilon^{-3})$ 下界的覆盖范围内。不写这句，读者会以为它和下界矛盾。

---

## 周报：单循环 SPLALM 从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$

**本周结论**

- 现稿停在 $\epsilon^{-3}$，原因只在**对偶块**：Tikhonov 正则给 $\boldsymbol{\lambda}$ 的强凹模数只有 $1/s = \Theta(\epsilon)$。
- 要降到 $\epsilon^{-2.5}$，需要把对偶块的内层收缩率从 $1/s$ 提到 $1/\sqrt{s}$。文献中做到这一点的工具是**对偶动量**（Zhang–Xu 2026）。
- 我们有三条路线。建议先做 B1 拿保底定理，同时推进 A。

### 1. 瓶颈

固定 $\rho = \Theta(1)$ 时，可行性残差要做到 $\epsilon$，需取 $s = \Theta(\epsilon^{-1})$。单循环复杂度可以拆成两项的乘积：

$$
K \asymp \epsilon^{-2} \cdot \frac{1}{\delta}
$$

- 第一项 $\epsilon^{-2}$ 是外层非凸问题找驻点的下界，不能再降。
- 第二项中的 $\delta$ 是内层鞍点子问题每步的收缩率，它限制了中心步长 $\alpha$ 的上限。
- 内层子问题中，原始块的条件数是 $\Theta(1)$，对偶块的条件数是 $s/\rho = \Theta(\epsilon^{-1})$。

两种情形的对比：

- **普通 GDA**：$\delta \sim \epsilon$，所以 $K \sim \epsilon^{-3}$。这是现稿的结果，并且已证明在算法族内是紧的。
- **加速后**：$\delta \sim \epsilon^{1/2}$，所以 $K \sim \epsilon^{-2.5}$。

### 2. 文献中三类"加速"分别解决什么

| 工具 | 作用对象 | 效果 |
| :--- | :--- | :--- |
| Tikhonov / 锚定 | 没有曲率的对偶块 | $\epsilon^{-4} \to \epsilon^{-3}$，现稿已用 |
| 外推（EG / OGDA） | $\mathbf{x}$ 与 $\boldsymbol{\lambda}$ 的耦合项引起的旋转 | 本身不改变阶数；加动量后用来保持稳定 |
| 对偶动量 | 曲率只有 $1/s$ 的对偶块 | $\epsilon^{-3} \to \epsilon^{-2.5}$ |

### 3. Zhang–Xu（arXiv:2609.17973）做了什么

- **问题**：对偶域有界的非凸–凹 minimax，单循环复杂度 $\mathcal{O}(\epsilon^{-2.5})$。
- **算法**：在正则化子问题上做 EG，并在对偶侧加一个梯度累加器。累加器的衰减率取 $\omega = 1-\Theta(\epsilon^{1/2})$，中心步长取 $\alpha = \Theta(\epsilon^{1/2})$。
- **证明难点**：中心每步都在移动，鞍点 $\boldsymbol{\lambda}^\star(\mathbf{z})$ 也随之漂移。如果用到鞍点的距离作势函数，漂移误差会把 $\alpha$ 压得过小。他们改用"鞍点值间隙 + 动量交叉项"构造 Lyapunov 函数，从而不需要对 $\boldsymbol{\lambda}^\star(\mathbf{z})$ 求导。

### 4. 我们的三条路线

| 路线 | 相对现稿的改动 | 每步代价 | 主要缺口 |
| :--- | :--- | :--- | :--- |
| A | 算法不变，参数改为 $\rho \sim \epsilon^{-1/2}$、$s \sim \epsilon^{-1}$ | 1 次梯度 + 1 次 prox | 一般非线性 $\mathcal{A}$ 下的收缩引理（仿射 $\mathcal{A}$ 可用 PDHG 度量） |
| B1 | $\rho$ 固定，用 EG + 对偶动量，去掉投影 | 2 次梯度 + 2 次 prox | 证明乘子有界；核对 Zhang–Xu 的 Lyapunov 论证能否接上 |
| B2 | $\rho$ 固定，用单步外推（OGDA / PDHG）+ 对偶动量 | 1 次梯度 + 1 次 prox | 单步格式下要重新构造 Lyapunov 函数，难度最高 |

**B1 可以去掉投影的依据**：我们的对偶梯度满足

$$
\nabla_{\boldsymbol{\lambda}} \mathcal{D}_\rho = \frac{1}{\rho}\left(\mathbf{q}-\boldsymbol{\lambda}\right), \qquad \lVert \mathbf{q} \rVert \le L_h
$$

因此对偶更新自带一个把 $\boldsymbol{\lambda}$ 拉回有界集的项，不需要人工投影。B1 的结论可以和族内 $\Theta(\epsilon^{-3})$ 下界构成**分离结果**。

**A 的价值**：A 不用动量，而是通过增大 $\rho$ 放大对偶步长。它的机理与 Zhang–Xu 不同，区分度最高，数值上已经验证。A 改变了 $\rho$，因此不在族内下界的覆盖范围内。

### 5. 下一步

1. **B1**：证明 $\sup_k \lVert \boldsymbol{\lambda}^k \rVert = \mathcal{O}(L_h)$，并核对 Lyapunov 论证能否接入。
2. **A**：先做仿射 $\mathcal{A}$ 的情形。
3. **B2**：排在 A 之后。

---

**要点**：这一版把篇幅压到原稿的约三分之一。论证主线只剩一条：瓶颈是对偶条件数 $s$，动量把它降到 $\sqrt{s}$，三条路线各有一个待证缺口。

---

## User (2026-11-08 23:43)

B2	$\rho$ 固定，用单步外推（OGDA / PDHG）+ 对偶动量	1 次梯度 + 1 次 prox	单步格式下要重新构造 Lyapunov 函数，难度最高 就是无论怎么样都得加动量对吧？

---

## Assistant (2026-11-08 23:43)

## 结论

**是的。在 $\rho$ 固定的前提下，要做到 $\epsilon^{-2.5}$，必须引入某种形式的动量，也就是让更新用到多步历史信息。** B2 里的 OGDA / PDHG 外推只负责稳定耦合项，本身不降阶。真正把 $s$ 降到 $\sqrt{s}$ 的仍然是对偶动量。B2 和 B1 的区别只在稳定器：B2 用单步外推，B1 用双步 EG。两条路线里动量都不能省。

## 为什么必须有动量

- **我们自己的结果**：族内下界已经表明，在 $s = c_s/\epsilon$ 时，无论 $(\alpha,\beta)$ 怎么取，复杂度都是 $\Omega(\epsilon^{-3})$。所以只调现有参数不够，必须走出这个算法族。
- **一般性结果**：对偶块的条件数是 $\kappa = s/\rho$。如果每步只用当前点、步长固定，这类方法的收缩率最好是 $1/\kappa$。要达到 $1/\sqrt{\kappa}$，迭代必须带至少一步的记忆，典型做法是 heavy-ball 或 Nesterov。参考 Arjevani–Shalev-Shwartz–Shamir（JMLR 2016）的 p-SCLI 框架：lifting factor $p=1$ 的方法不能优于 $\kappa$。这条引用我是凭记忆给的，写进周报前请核对。
- **记忆只是必要条件**：OGDA 也用了两步梯度，但它在强单调问题上的收缩率仍然是 $1/\kappa$。所以要的是专门针对慢方向设计的记忆，也就是动量。

## 例外（"无论怎么样"在这些情形下不成立）

| 做法 | 是否需要动量 | 问题 |
| :--- | :--- | :--- |
| 方案 A：令 $\rho \sim \epsilon^{-1/2}$ | 不需要 | 前提变了。它降低的是条件数 $s/\rho$ 本身，没有对固定的 $\kappa$ 开根号 |
| Chebyshev 变步长 | 不需要 | 在二次问题上可以达到 $\sqrt{\kappa}$，但需要目标在一个长约 $\sqrt{s}$ 的周期内保持不变。中心一冻结，就退回双循环；不冻结，数值上不稳定 |
| Silver stepsize 类长步长 | 不需要 | 只能降到 $\kappa^{0.786}$，对应约 $\epsilon^{-2.79}$，达不到 $\epsilon^{-2.5}$ |
| 双循环 + 加速内层求解器 | 需要（在内层） | 动量藏在内层求解器里，而且不再是单循环 |

**要点**：固定 $\rho$ 的单循环要做到 $\epsilon^{-2.5}$，对偶动量躲不开，外推只是配套的稳定器。唯一真正绕开动量的路线是方案 A，因为它改变了 $\rho$，条件数本身就降下来了。

---

## User (2026-11-08 23:43)

文献中三类"加速"分别解决什么
工具	作用对象	效果
Tikhonov / 锚定	没有曲率的对偶块	$\epsilon^{-4} \to \epsilon^{-3}$，现稿已用
外推（EG / OGDA）	$\mathbf{x}$ 与 $\boldsymbol{\lambda}$ 的耦合项引起的旋转	本身不改变阶数；加动量后用来保持稳定
对偶动量	曲率只有 $1/s$ 的对偶块	$\epsilon^{-3} \to \epsilon^{-2.5}$ 我认为这个很好 但是为啥没有参考问下

---

## Assistant (2026-11-08 23:44)

## 结论

上一版删得太多，把引用也删掉了。这张表的每一格都是在概括文献，所以需要出处。下面是补上引用后的版本。来源分两类：一类已在项目文献笔记 [literature.md](overleaf/notes/project/literature.md) 和 [lit-check-retreat-20261104.md](overleaf/notes/progress/lit-check-retreat-20261104.md) 里对过原文；另一类是我凭记忆给的，下面单独标出，放进周报前需要逐条核对。

## 补引用后的表

| 工具 | 作用对象 | 效果 | 代表文献 |
| :--- | :--- | :--- | :--- |
| Tikhonov / 锚定 | 没有曲率的对偶块 | $\epsilon^{-4} \to \epsilon^{-3}$，现稿已用 | 单调问题：Halpern 1967；Yoon–Ryu 2021；Boț–Chenchene 2026。非凸–凹：Li–Nagarajan–Pan–Zhang 2026；Xu–Zhang–Xu–Lan 2023 |
| 外推（EG / OGDA / PDHG） | $\mathbf{x}$ 与 $\boldsymbol{\lambda}$ 的耦合项引起的旋转 | 本身不改变阶数；加动量后用来保持稳定 | 方法：Korpelevich 1976；Popov 1980；Chambolle–Pock 2011。不改变阶数的证据：Mokhtari–Ozdaglar–Pattathil 2020；Mahdavinia et al. 2022 |
| 对偶动量 | 曲率只有 $1/s$ 的对偶块 | $\epsilon^{-3} \to \epsilon^{-2.5}$ | 强凸–强凹：Zhang–Hong–Zhang 2022（下界）；Kovalev–Gasnikov–Richtárik 2022（单环上界）。非凸–凹：Zhang–Xu 2026（单环）；Lin–Jin–Jordan 2020、Ostrovskii–Lowy–Razaviyayn 2021（多环）；Pan–Zheng–Li 2026（下界） |

## 每行引用支撑的论断

**第一行。** 最直接的证据是 Li–Nagarajan–Pan–Zhang（arXiv:2602.14185），里面有两个结果：

- Smoothed GDA 的算法特定下界是 $\Omega(\epsilon^{-4})$；
- 加入对偶扰动 $r_y = \Theta(\epsilon)$ 后，PSGDA 的 GS 复杂度降到 $\mathcal{O}(\epsilon^{-3})$。

这正是 $\epsilon^{-4} \to \epsilon^{-3}$。Chen（arXiv:2605.30905）说明了锚定可以看作算子侧的 Tikhonov 正则。有了这条，"锚定"和"Tikhonov"合在同一行就有了依据。

**第二行。** Mahdavinia et al.（NeurIPS 2022）在 NC-SC 问题上证明：EG 和 OGDA 无论学习率怎么取，复杂度都有 $\Omega(\kappa \Delta / \epsilon^2)$ 的下界。这个下界对 $\kappa$ 是线性的，说明外推本身不会把 $\kappa$ 降到 $\sqrt{\kappa}$。

**第三行。** 有两点值得写进周报：

- Zhang–Hong–Zhang 证明，强凸–强凹问题的一阶下界是 $\Omega(\sqrt{\kappa_x \kappa_y})$。因此开根号是能达到的最好结果。
- Pan–Zheng–Li（arXiv:2609.14235）对光滑 NC-C 问题、任意确定性一阶方法给出了 GS 下界 $\Omega(\epsilon^{-5/2})$。因此 **$\epsilon^{-2.5}$ 在光滑 NC-C 类上是 oracle 最优的**。我们的问题带 $\mathrm{prox}_h$，这个下界能否迁移过来，还是 open question。

## 核对状态

| 已对过原文或参数（项目笔记中有记录） | 凭记忆给出，待核对 |
| :--- | :--- |
| Li–Nagarajan–Pan–Zhang 2026（2602.14185） | Halpern 1967（Bull. AMS） |
| Mahdavinia et al. 2022（2210.09382） | Yoon–Ryu 2021（ICML） |
| Zhang–Xu 2026（2609.17973），GS 下取 $\tau = \Theta(\epsilon)$ | Korpelevich 1976；Popov 1980 |
| Pan–Zheng–Li 2026（2609.14235） | Chambolle–Pock 2011（JMIV） |
| Boț–Chenchene 2026（SIOPT 36(3)） | Mokhtari–Ozdaglar–Pattathil 2020（AISTATS） |
| Chen 2026（2605.30905） | Zhang–Hong–Zhang 2022（Math. Program.，arXiv:1912.07481） |
| Xu–Zhang–Xu–Lan 2023（MP）：仅为讨论级记录 | Kovalev–Gasnikov–Richtárik 2022（NeurIPS） |
| Ostrovskii–Lowy–Razaviyayn 2021：仅为讨论级记录 | Lin–Jin–Jordan 2020（COLT，Near-optimal algorithms） |

右列都是标准文献，但年份、venue 和定理编号我没有当场核对。如果需要，我可以用 `/citation-audit` 或 arXiv / DBLP 逐条查，再把结果补进 `literature.md`。

**要点**：每一行都有直接文献支撑，其中三条最关键。Li et al. 2026 给出了 $\epsilon^{-4} \to \epsilon^{-3}$ 的直接证据。Mahdavinia et al. 2022 说明外推不能降阶。Pan–Zheng–Li 2026 说明 $\epsilon^{-2.5}$ 已经是光滑 NC-C 类上的下界。

---

## User (2026-11-08 23:44)

我们这种 相当于从Tk正则角度 我记得有Fast Tk bot的工作啊 他们不需要动量

---

## Assistant (2026-11-08 23:45)

## 结论

**你记得没错。Boț–Nguyen（J. Complexity 94, 2026；arXiv:2406.00852）用一阶 Tikhonov 单调算子流，不加惯性，在特定正则函数下就能让残差以 $\mathcal{O}(1/t)$ 衰减。** 但这个提速属于表中第一行：它加速的是没有曲率的单调问题。换算到我们的问题，它对应的正是现稿的 $\epsilon^{-3}$。要到 $\epsilon^{-2.5}$，内层残差速率需要从 $1/k$ 提到 $1/k^2$。Boț 系列里比 $1/k$ 更快的结果都带惯性项，而且只改进到 $o(1/k)$，阶数没有变。

## 速率与复杂度的对应

对偶块的人工曲率是 $1/s$，取 $s \sim \epsilon^{-1}$。内层残差速率与总复杂度的对应如下：

| 内层残差速率 | 内层所需步数 | 总复杂度 | 文献 |
| :--- | :--- | :--- | :--- |
| $1/\sqrt{k}$（无正则的 EG） | $s^2$ | $\epsilon^{-4}$ | Smoothed GDA 型 |
| $1/k$（Tikhonov / 锚定，无惯性） | $s$ | $\epsilon^{-3}$ | Boț–Nguyen 2026；Halpern；我们的 $s_k \asymp k$ |
| $o(1/k)$（带惯性） | $o(s)$ | 仍是 $\epsilon^{-3}$ 量级 | Fast OGDA；Boț–Nguyen–Zong；Li–Xiao 2610.39133 |
| $1/k^2$（对偶动量） | $\sqrt{s}$ | $\epsilon^{-2.5}$ | Zhang–Xu 2026 |

这和 [lit-check-retreat-20261104.md](overleaf/notes/progress/lit-check-retreat-20261104.md) 第 12 行的核对一致：$s_k \asymp k$ 时残差为 $1/k$，要到 $o(1/k)$ 需要惯性或二阶系统。

## 为什么 Tikhonov 视角卡在 $1/k$

- **$1/k$ 在一般单调算子类上已经是最优。** Yoon–Ryu（ICML 2021）证明，对单调 Lipschitz 算子，任何一阶方法的残差下界都是 $\Omega(1/k)$。所以，只要把问题当作一般单调算子 $F$ 来正则化，就不可能超过 $\epsilon^{-3}$。
- **$\epsilon^{-2.5}$ 用到了一般单调算子类不具备的分块结构。** 我们的内层子问题是强凸–强凹问题：$\mu_x = \Theta(1)$，$\mu_\lambda = 1/s$，耦合常数为 $\Theta(1)$。按 Zhang–Hong–Zhang 的下界，这类问题的最优代价是

$$
\sqrt{\frac{L_{x\lambda}^2}{\mu_x \mu_\lambda}} \sim \sqrt{s}
$$

如果把它看成一个强单调模数为 $1/s$ 的一般算子，最优代价只能是 $s$。从 $s$ 降到 $\sqrt{s}$，靠的是区分两个块、在对偶块上利用它是凹函数梯度这一对称结构。对偶动量做的正是这件事。

- **锚定和动量在代数上本来就相通。** Tran-Dinh（COAP 2024）证明，Halpern 迭代经过重新参数化后，就是 Nesterov 型加速。Boț 的 fast 系列算法大多从带消失阻尼的二阶动力系统离散而来，形式上也含惯性项。因此"不需要动量"在很多情形下只是写法上的区别。Boț–Nguyen 的一阶流是真正不带惯性的，它的速率也正好停在 $1/k$。

## 对路线的含义

- 纯 Tikhonov 路线（包括 vanishing Tikhonov 和 anchoring）在一般单调算子框架下，上限就是现稿的 $\epsilon^{-3}$。所以，现稿用 Tikhonov 拿到 $\epsilon^{-3}$，可以引用 Boț–Nguyen 作为单调算子侧的对应结果。
- Boț 合作线上可以追问的问题：**能否在 Tikhonov 动力系统中只对对偶块加惯性，把残差从 $1/k$ 提到 $1/k^2$？** 这正是 B1 / B2 的连续时间版本，也与 [splalm-followup-lines](memory) 记录的 Boț 合作方向吻合。

## 待核对

以下几条凭记忆给出，引用前需要核对：

- Yoon–Ryu 的 $\Omega(1/k)$ 残差下界：适用的算法类，以及残差用平方还是范数；
- Tran-Dinh 的 Halpern–Nesterov 等价，期刊与年份；
- Fast OGDA（Boț–Csetnek–Nguyen）的期刊，我记得是 FoCM。

Boț–Nguyen 2026、Boț–Nguyen–Zong（Numer. Math. 158）和 Li–Xiao 已在项目笔记中核对过。

**要点**：Boț 不加动量的 fast Tikhonov 把一般单调问题加速到 $1/k$，这正是我们 $\epsilon^{-3}$ 的来源，并且在一般单调算子类上已经最优。到 $\epsilon^{-2.5}$ 必须利用对偶块的凹函数结构，目前已知的手段是对偶动量。

---

## User (2026-11-08 23:48)

EXTRA-GRADIENT METHOD WITH FLEXIBLE ANCHORING:
STRONG CONVERGENCE AND FAST RESIDUAL DECAY∗ 但是我接的这篇文章就加速了啊

---

## Assistant (2026-11-08 23:49)

## 结论

**它确实是加速，但加速的是表中第一行。** 我查了原文摘要（arXiv:2410.14369，SIOPT 2026）。Boț–Chenchene 研究的是**单调方程**，即没有强单调性、没有曲率的问题。他们的方法在标准参数下得到的残差速率是 $\mathcal{O}(k^{-1})$。这里"fast residual decay"的比较对象是普通 EG 的 last-iterate 速率 $\mathcal{O}(k^{-1/2})$。换算到我们的问题，这就是 $\epsilon^{-4} \to \epsilon^{-3}$，也就是现稿已经拿到的那一阶。

## 三个速率对照

| 方法 | 单调问题的 last-iterate 残差 | 对应我们的总复杂度 |
| :--- | :--- | :--- |
| 普通 EG | $\mathcal{O}(k^{-1/2})$ | $\epsilon^{-4}$ |
| Boț–Chenchene 锚定 EG | $\mathcal{O}(k^{-1})$ | $\epsilon^{-3}$ |
| 对偶动量（Zhang–Xu） | 需要内层达到 $\sqrt{s}$ 步 | $\epsilon^{-2.5}$ |

- 摘要原话：他们的方法 "recovers the fast residual decay rate $O(k^{-1})$ for standard parameter choices"。
- 方法由 Tikhonov 正则单调流显式离散得到，分析沿用 Boț–Nguyen（arXiv:2406.00852）。所以它和上一条回答里的 Boț–Nguyen 是同一条线：前者是离散算法，后者是连续时间流，速率都是 $1/k$。
- 再快一步做不到。在一般单调 Lipschitz 算子类上，$1/k$ 已经是最优速率（Yoon–Ryu 2021，凭记忆，待核）。因此任何锚定变体在这个类上都不能超过 $1/k$。

## 和我们问题的对应

- 现稿的递增 $s_k$ 分支，就是 Boț–Chenchene 的离散版本：对偶正则的权重 $1/s_k \to 0$，anchor $\boldsymbol{\mu}^k$ 可以移动。项目的 [antigravity-20261026-tikhonov-retreat.md](overleaf/notes/conversations/antigravity-20261026-tikhonov-retreat.md) 第 130–147 行已经做过这个对应，结论相同：锚定把残差从 $1/\sqrt{k}$ 提到 $1/k$；但在强单调问题上，它不改善对 $\kappa$ 的依赖。
- 固定 $s \sim \epsilon^{-1}$ 时，内层已有曲率 $1/s$，锚定给不出额外增益。要从 $s$ 降到 $\sqrt{s}$，必须利用对偶块的凹函数结构，也就是对偶动量。

## 对周报表格的修改建议

第一行的文献列应写上 Boț–Chenchene 2026 和 Boț–Nguyen 2026，效果列写成"单调残差 $1/\sqrt{k} \to 1/k$，对应 $\epsilon^{-4} \to \epsilon^{-3}$"。这样读者会看到，Boț 的加速和对偶动量的加速是两个不同的阶段，不会觉得两者冲突。

**要点**：Boț–Chenchene 的 fast residual decay 把单调问题从 $1/\sqrt{k}$ 加速到 $1/k$，对应我们已有的 $\epsilon^{-3}$。从 $\epsilon^{-3}$ 再到 $\epsilon^{-2.5}$，需要它不涉及的对偶动量。

Sources:
- [arXiv:2410.14369 — Extra-Gradient Method with Flexible Anchoring](https://arxiv.org/abs/2410.14369)
- [HTML version](https://arxiv.org/html/2410.14369)
- [dblp: Enis Chenchene](https://dblp.org/pid/333/2502.html)
- [arXiv:2605.30905 — A Unifying View of Anchoring via Operator-Side Tikhonov Regularization](https://arxiv.org/pdf/2605.30905)

---

## User (2026-11-08 23:51)

zhang用的是是EG+动量？ 我们是不是可以直接借鉴bot的FastOGAD或者Fast系列结合nesterov 进行加速啊

---

## Assistant (2026-11-08 23:52)

## 结论

1. **是的，Zhang–Xu 用的是 EG 加对偶动量。** 项目笔记 [lit-check-retreat-20261104.md](overleaf/notes/progress/lit-check-retreat-20261104.md) 第 23 行记录的是读 arXiv HTML 正文核对过的版本，原话是"projected damped extragradient + 对偶动量 + 移动近端中心"，对偶域有界并做投影。
2. **直接套用 Fast OGDA 到不了 $\epsilon^{-2.5}$。** 它是为一般单调算子设计的，阻尼是消失型的 $\alpha/t$，残差速率 $o(1/k)$，换算到我们的问题仍是 $\epsilon^{-3}$ 量级。它能提供的是**单梯度离散化的技术**和**连续时间 Lyapunov 分析的方法**，这两样正好用于 B2。真正提速的动量要换成**常数阻尼、只加在对偶块上**的强凸型 Nesterov 动量。

## Fast OGDA 本身是什么

我核对了 arXiv:2203.10947（FoCM 2023）的摘要：

- 问题：单调连续算子 $V$ 的零点。
- 连续时间：二阶动力系统，包含消失阻尼项，以及 $V$ 沿轨迹的时间导数。
- 离散：显式算法可以看作 OGDA 的加速版本；$V$ 为 Lipschitz 时，残差和受限 gap 都是 $o(1/k)$。

问题在于，"加速"的含义取决于问题类。在一般单调算子类上，$1/k$ 已经是下界的阶，Fast OGDA 只能把它改进到 $o(1/k)$。我们要的是在固定曲率 $1/s$ 下把 $s$ 降到 $\sqrt{s}$，这和它解决的不是同一个问题。

| | Fast OGDA | 我们需要的 |
| :--- | :--- | :--- |
| 问题类 | 一般单调，无曲率 | 强凸–强凹，$\mu_x = \Theta(1)$，$\mu_\lambda = 1/s$ |
| 阻尼 | 消失型 $\alpha/t$（凸型 Nesterov） | 常数 $\sim 1/\sqrt{s}$（强凸型 Nesterov） |
| 动量加在哪 | 整个算子 $V$，两块对称处理 | 只加在 $\boldsymbol{\lambda}$ 块 |
| 速率 | $o(1/k)$ | 收缩率 $1/\sqrt{s}$ |
| 对应复杂度 | $\epsilon^{-3}$ 量级 | $\epsilon^{-2.5}$ |

## 为什么动量只需加在对偶块

定义对偶函数

$$
\varphi_k(\boldsymbol{\lambda}) = \min_{\mathbf{x}} \mathcal{P}_k(\mathbf{x},\boldsymbol{\lambda})
$$

- 因为原始块强凸且 $\kappa_x = \Theta(1)$，所以 $\varphi_k$ 是光滑的，光滑常数为 $\Theta(1)$；它还是 $1/s$-强凹的。
- 对 $\varphi_k$ 做常数系数的 Nesterov 加速，收缩率是 $1/\sqrt{s}$。这是加速对偶上升的标准结论。
- 单循环中，$\min_{\mathbf{x}}$ 用一步梯度近似。因为 $\kappa_x = \Theta(1)$，一步梯度就有常数比例的收缩，原始块不需要动量。
- 外推（EG / OGDA）的作用是控制"一步近似 $\min_{\mathbf{x}}$"带来的耦合误差，防止动量把旋转方向放大。

所以，正确的模板是"**$\boldsymbol{\lambda}$ 上做强凸型 Nesterov 动量，$\mathbf{x}$ 上做一步梯度，耦合项用外推稳定**"。Fast 系列的消失阻尼模板对应的是 $\mu_\lambda = 0$ 的情形。

## 从 Boț 线上能借什么

1. **单梯度离散化（B2 直接受益）。** Fast OGDA 利用 $V$ 的时间导数项，用"当前梯度 + 历史梯度差"实现每步一次梯度。B2 要把 Zhang–Xu 的双步 EG 换成单步格式，这套离散化技巧可以直接参考。
2. **先连续后离散的 Lyapunov 构造。** 可以先研究一个混合阶的动力系统：$\mathbf{x}$ 一阶，$\boldsymbol{\lambda}$ 二阶，对偶块带常数阻尼 $\sim 2/\sqrt{s}$，再加 Tikhonov 项 $-\boldsymbol{\lambda}/s$ 和中心漂移。在连续时间里找到 Lyapunov 函数后再离散，比直接在离散格式上硬凑更容易。这个题目适合和 Boț 合作，也和 [splalm-followup-lines](memory) 的方向吻合。
3. **可以对照的文献。** 凸最小化中"惯性 + Tikhonov"的组合已有工作，例如 Boț–Sonntag（JMAA 554，项目笔记已列出）和 Attouch–Chbani–Riahi 2018（凭记忆，待核）。鞍点问题上"只对一块加惯性"的连续时间版本，我目前没见过对应结果，需要查新。

## 风险

把常数动量和移动中心、外推放进同一个 Lyapunov 函数，正是 Zhang–Xu 主要的证明工作量。单步格式下不能沿用他们的双步 EG 证明。这仍是 B2"难度最高"的原因，Fast OGDA 的技术不能直接消掉这部分工作。

**要点**：Fast OGDA 是一般单调类上的加速，阻尼消失，速率停在 $o(1/k)$。我们需要的是在对偶块上加常数阻尼的强凸型动量。Boț 线可以借的是单梯度离散化和连续时间 Lyapunov 方法，不能直接借它的速率。

Sources:
- [arXiv:2203.10947 — Fast OGDA in continuous and discrete time](https://arxiv.org/abs/2203.10947)
- [PDF](https://arxiv.org/pdf/2203.10947)
- [arXiv:2510.02951 — Long-Time Analysis of Stochastic Heavy Ball Dynamics](https://arxiv.org/pdf/2510.02951)
- [ResearchGate: Radu Boț](https://www.researchgate.net/profile/Radu-Bot)

---

## User (2026-11-08 23:55)

4. 我们的三条路线
路线	相对现稿的改动	每步代价	主要缺口
A	算法不变，参数改为 $\rho \sim \epsilon^{-1/2}$、$s \sim \epsilon^{-1}$	1 次梯度 + 1 次 prox	一般非线性 $\mathcal{A}$ 下的收缩引理（仿射 $\mathcal{A}$ 可用 PDHG 度量）
B1	$\rho$ 固定，用 EG + 对偶动量，去掉投影	2 次梯度 + 2 次 prox	证明乘子有界；核对 Zhang–Xu 的 Lyapunov 论证能否接上
B2	$\rho$ 固定，用单步外推（OGDA / PDHG）+ 对偶动量	1 次梯度 + 1 次 prox	单步格式下要重新构造 Lyapunov 函数，难度最高

B1 可以去掉投影的依据：我们的对偶梯度满足 zhang是B1？ 我认为A不需要做了 做不了

---

## Assistant (2026-11-08 23:56)

## 结论

1. **是的，B1 基本就是把 Zhang–Xu 搬到我们的 ALM 形式上。** 算法骨架相同，都是 EG、对偶动量、移动近端中心，外加 $s \sim \epsilon^{-1}$。区别只有两处：我们去掉了投影，并把对偶变量换成 ALM 乘子 $\boldsymbol{\lambda}$。
2. **A 按你的判断删掉。** 删掉之后，周报的逻辑反而更统一：固定 $\rho$ 时动量是必需的，两条路线都加对偶动量，差别只在用哪种外推来稳定。
3. **B1 的新意偏薄，比原稿写的更需要警惕。** 理由见下节。

## B1 的风险：Zhang–Xu 几乎可以直接用在我们的问题上

按项目笔记的记录（[literature.md](overleaf/notes/project/literature.md) 第 61 行），我们的证书 $R_k$ 对应下面这个 Lagrangian 的 GS：

$$
L(\mathbf{x},\mathbf{q}) = f(\mathbf{x}) + \langle \mathcal{A}(\mathbf{x}), \mathbf{q} \rangle - h^*(\mathbf{q})
$$

- 因为 $h$ 是 $L_h$-Lipschitz 的，所以 $\mathrm{dom}\, h^*$ 包含在半径为 $L_h$ 的球内。也就是说，在 $\mathbf{q}$ 变量下，对偶域本来就是紧的。
- Zhang–Xu 的设定是光滑 NC-C 加紧对偶域。把他们的投影 $\Pi_{\mathcal{Y}}$ 换成 $\mathrm{prox}_{h^*}$，大概率只是常规推广。
- 因此审稿人可能会说："对 $L(\mathbf{x},\mathbf{q})$ 直接跑 Zhang–Xu，就能得到 GS 的 $\mathcal{O}(\epsilon^{-2.5})$。"

在这个前提下，B1 能站住的贡献只剩三条：

| 贡献 | 分量 |
| :--- | :--- |
| 与族内 $\Theta(\epsilon^{-3})$ 下界构成分离：固定 $\rho$ 时，加对偶动量才能到 $\epsilon^{-2.5}$ | 主要卖点 |
| ALM 形式：乘子 $\boldsymbol{\lambda}$ 无界、不需要投影，靠 $(\mathbf{q}-\boldsymbol{\lambda})/\rho$ 的恢复项保证有界 | 技术细节 |
| 非光滑的 $h^*$：从投影推广到 prox | 偏常规 |

所以 B1 适合定位成**保底的分离结果**，不宜作为独立的主贡献。

## 修改后的路线表

| 路线 | 相对现稿的改动 | 每步代价 | 与 Zhang–Xu 的关系 | 主要缺口 |
| :--- | :--- | :--- | :--- | :--- |
| B1 | $\rho$ 固定，EG + 对偶动量，去掉投影 | 2 次梯度 + 2 次 prox | 同一算法，移到 ALM 形式 | 乘子有界；核对 Lyapunov 论证能否接上 |
| B2 | $\rho$ 固定，单步外推（OGDA / PDHG）+ 常数系数对偶动量 | 1 次梯度 + 1 次 prox | 新格式，每步代价减半 | 单步格式下重新构造 Lyapunov 函数 |

B1 能去掉投影，依据是 $\nabla_{\boldsymbol{\lambda}} \mathcal{D}_\rho = (\mathbf{q}-\boldsymbol{\lambda})/\rho$ 且 $\lVert \mathbf{q} \rVert \le L_h$。不过要注意：动量的累加幅度能到单步梯度的 $\sqrt{s}$ 倍，$\boldsymbol{\lambda}^k$ 可能冲出 $L_h$ 球。所以 $\sup_k \lVert \boldsymbol{\lambda}^k \rVert = \mathcal{O}(L_h)$ 必须真正证出来，不能只靠直觉。

## 对推进顺序的影响

- **B1**：工作量小，先写出来，用来锁定分离定理。
- **B2**：成为唯一有区分度的路线。上一条回答里提到的 Fast OGDA 单梯度离散化和连续时间 Lyapunov 方法，都应投入到这里。

另外，我已把"路线 A 已放弃；B1 在 $\mathbf{q}$ 视角下新意偏薄"记入项目 memory（[acceleration-routes-eps25.md](~/.claude/projects/-Users-liluxuan-Documents-My-Papers-3-DDLALM/memory/acceleration-routes-eps25.md)），后续会话不会再推荐 A。

**要点**：B1 就是 Zhang–Xu 的 ALM 版本。在 $\mathbf{q}$ 视角下 Zhang–Xu 几乎能直接覆盖我们的问题，所以 B1 只能做保底的分离结果。删掉 A 以后，B2 是唯一有区分度的路线。

---

## User (2026-11-08 23:57)

我们刚才一通分析 抛弃了什么思路 因为什么？

---

## Assistant (2026-11-08 23:58)

## 结论

抛弃的思路可以分成三类。**第一类是不能提供 $\epsilon^{-3} \to \epsilon^{-2.5}$ 的加速机制**：纯外推、锚定 / Tikhonov、Fast 系列的速率，以及固定 $\rho$ 下的无动量替代方案。**第二类是路线层面的取舍**：A 被删掉，B1 被降级为保底结果。**第三类是周报里的过度表述**。各项和原因如下。

## 一、加速机制层面

| 抛弃的思路 | 原因 | 保留了什么 |
| :--- | :--- | :--- |
| 只用外推（EG / OGDA / PDHG）降阶 | 外推不改变对 $\kappa$ 的依赖。Mahdavinia et al. 2022 证明 EG / OGDA 在 NC-SC 上有 $\Omega(\kappa\Delta/\epsilon^2)$ 下界 | 作为动量的稳定器，控制耦合项的旋转 |
| 用锚定 / Tikhonov 到 $\epsilon^{-2.5}$（Boț–Chenchene flexible anchoring、Boț–Nguyen fast Tikhonov） | 它们的加速是单调残差 $1/\sqrt{k} \to 1/k$，即 $\epsilon^{-4} \to \epsilon^{-3}$，现稿已用。$1/k$ 在一般单调类上已是最优；固定曲率 $1/s$ 时，锚定没有额外增益 | 作为现稿 $\epsilon^{-3}$ 在单调算子侧的对应文献 |
| 直接拿 Fast OGDA 或 Fast 系列 + Nesterov 来提速 | 阻尼是消失型 $\alpha/t$，只到 $o(1/k)$，仍是 $\epsilon^{-3}$ 量级；而且对两块对称处理，丢掉了对偶块的凹函数结构 | 单梯度离散化技巧和连续时间 Lyapunov 方法，转用到 B2 |
| 固定 $\rho$ 下不加动量的替代方案 | Chebyshev 变步长要求中心冻结约 $\sqrt{s}$ 步，于是退回双循环，否则不稳定；silver 长步长只到约 $\epsilon^{-2.79}$；双循环加速内层求解器不再是单循环 | 无 |

这些合起来得到正面结论：**固定 $\rho$ 时，需要在对偶块上加常数阻尼的强凸型动量。**

## 二、路线层面

| 抛弃或降级 | 原因 |
| :--- | :--- |
| 路线 A（$\rho \sim \epsilon^{-1/2}$，不加动量） | 你判断做不了，因此删除。我没有独立核实这个判断。A 原本是唯一不需要动量的路线，删掉后周报的主线统一为"固定 $\rho$ 必须加对偶动量" |
| B1 作为主贡献 | 在 $\mathbf{q}$ 视角下，$\mathrm{dom}\, h^*$ 包含在半径为 $L_h$ 的球内。把 Zhang–Xu 的投影换成 $\mathrm{prox}_{h^*}$，几乎可以直接覆盖我们的问题。所以 B1 降为保底的分离结果，B2 成为唯一有区分度的路线 |

## 三、表述层面（从周报中删除或改写）

| 原表述 | 原因 | 改为 |
| :--- | :--- | :--- |
| "固定 $\rho$ 下对偶动量是突破 $\epsilon^{-3}$ 的**充要条件**" | 族内下界只覆盖 $(\alpha,\beta)$ 族，推不出动量是必要的 | "与族内下界构成分离" |
| "B1 只需证乘子有界即可接入 Zhang–Xu" | Zhang–Xu 依赖有界对偶域，换成无界 $\boldsymbol{\lambda}$ 后是否只差这一条，还没核对；动量累加还可能让 $\boldsymbol{\lambda}^k$ 冲出 $L_h$ 球 | "主要缺口" |
| 中心漂移的量级："$\Delta\boldsymbol{\lambda}^\star \lesssim s\alpha$，$\alpha \lesssim \epsilon^{3/2}$" | 未经核实，量级推导也不严格 | 删除，只保留定性描述 |
| Zhang–Xu 的四行算法和"低通滤波"解释 | 读者做决策用不到 | 删除 |

## 依据的可靠程度

- **已核对原文或摘要**：Boț–Chenchene（$\mathcal{O}(k^{-1})$）、Fast OGDA（$o(1/k)$，消失阻尼）、Zhang–Xu 的算法结构、Mahdavinia et al.、Li–Nagarajan–Pan–Zhang。
- **凭记忆，待核对**：一般单调类的 $\Omega(1/k)$ 下界（Yoon–Ryu），以及强凸–强凹的 $\sqrt{\kappa_x\kappa_y}$ 下界（Zhang–Hong–Zhang）。"锚定不能超过 $1/k$"和"只需在对偶块开根号"这两个判断依赖这两条。如果下界的适用范围比我记的窄，结论需要重新检查。

**要点**：凡是不区分两块、把问题当作一般单调算子处理的加速手段（外推、锚定、Fast 系列），在一般单调类上都停在 $1/k$，对应现稿的 $\epsilon^{-3}$。剩下的方向是固定 $\rho$、在对偶块上加常数阻尼动量，其中有区分度的路线是 B2。

---

## User (2026-11-08 23:58)

直接拿 Fast OGDA 或 Fast 系列 + Nesterov 来提速	阻尼是消失型 $\alpha/t$，只到 $o(1/k)$，仍是 $\epsilon^{-3}$ 量级；而且对两块对称处理，丢掉了对偶块的凹函数结构	单梯度离散化技巧和连续时间 Lyapunov 方法，转用到 B2 这个没看懂 实际上对应我们的那个参数呢？

---

## Assistant (2026-11-08 23:59)

## 结论

**Fast OGDA 加速的关键是一个动量系数，而我们的算法族里没有这个参数。** 它需要在对偶更新里加一项 $\theta_k(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1})$。两种取法：

- Fast OGDA 取 $\theta_k \approx 1 - \alpha_0/k$，随迭代次数趋于 1，和 $s$ 无关。
- 我们需要取常数 $\theta = 1 - c\sqrt{\tau/s} = 1 - \Theta(\epsilon^{1/2})$，由对偶曲率 $1/s$ 决定。这就是 Zhang–Xu 的 $\omega$。

（这里用 $\alpha_0$ 表示 Fast OGDA 的阻尼常数，以区别于我们的中心步长 $\alpha$。）

Fast OGDA 的另外两个成分在我们的族里都已存在：Tikhonov 权重对应 $s$，anchor 对应 $\boldsymbol{\mu}^k$ 和 $\beta$。族内下界已经覆盖了这两个成分，所以它们帮不上忙。

## 对照我们的参数

现稿的算法族是 $\mathrm{SPLALM}_{\theta,\alpha,\beta}$，其中 $\theta = (\rho, s, \gamma, \eta, \tau)$（[AlgorithmFamily.tex:37-46](overleaf/sections/AlgorithmFamily.tex#L37-L46)）。对偶中心按下式更新：

$$
\boldsymbol{\mu}^{k+1} = \boldsymbol{\mu}^k + \beta\left(\boldsymbol{\lambda}^{k+1} - \boldsymbol{\mu}^k\right)
$$

| Boț 系列的成分 | 我们族里的对应 | 是否被族内下界覆盖 |
| :--- | :--- | :--- |
| Tikhonov 权重 $\varepsilon(t) \to 0$ | $1/s$；递增分支 $s_k \asymp k$ | 是 |
| 可移动的 anchor | $\boldsymbol{\mu}^k$，移动步长 $\beta$ | 是，$\beta \in [0,1]$ 全部覆盖 |
| 惯性项（消失阻尼 $\alpha_0/t$） | **没有对应参数** | 不在族内 |

前两行说明，现稿实际上已经包含了 Boț–Chenchene 的锚定结构，而且已证明它在族内只能到 $\epsilon^{-3}$。

$\boldsymbol{\mu}^k$ 也带历史信息：它是过去各步 $\boldsymbol{\lambda}$ 的指数平均。但它和动量的作用方向相反：

- $\boldsymbol{\mu}^k$ 通过梯度项 $-(\boldsymbol{\lambda}-\boldsymbol{\mu}^k)/s$ **把 $\boldsymbol{\lambda}$ 拉回**历史平均，作用相当于近端点，效果是增加阻尼。
- 动量项 $\theta(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$ **沿上一步的方向继续推**，作用是放大慢方向上的步长。

所以 $\beta$ 取任何值都无法替代动量。

## 为什么消失阻尼不行，要常数阻尼

两种取法写成公式是：

$$
\theta_k^{\mathrm{FastOGDA}} \approx 1 - \frac{\alpha_0}{k}, \qquad \theta^{\mathrm{need}} = 1 - c\sqrt{\frac{\tau}{s}}
$$

单循环证明的核心是 Lyapunov 函数每步有一个**一致的收缩率** $\delta$，中心步长满足 $\alpha \lesssim \delta$。两种取法给出的收缩率不同：

- **常数阻尼**：$\delta \sim \sqrt{\tau/s} \sim \epsilon^{1/2}$，因此 $\alpha \sim \epsilon^{1/2}$，总复杂度 $\epsilon^{-2.5}$。
- **消失阻尼**：收缩只来自从起点算起的多项式速率，不存在一致的 $\delta$，所以中心步长 $\alpha$ 无法取成常数。

**重启也救不回来。** 设每 $T$ 步重启一次 Fast OGDA。它在一般单调类上的残差界是"距离 / $T$"，而强单调模数为 $1/s$ 时，距离最多是 $s$ 倍的残差：

$$
\lVert F(\mathbf{w}^T) \rVert \lesssim \frac{\lVert \mathbf{w}^0 - \mathbf{w}^\star \rVert}{T} \le \frac{s \lVert F(\mathbf{w}^0) \rVert}{T}
$$

所以要让残差减半，需要 $T \sim s$。这给出 $\delta \sim 1/s$，和现稿完全一样。

只对对偶块做 Nesterov 时情况不同。此时可以利用对偶函数的结构：$\varphi_k(\boldsymbol{\lambda}) = \min_{\mathbf{x}} \mathcal{P}_k$ 是凹函数，强凹模数 $1/s$，光滑常数约 $1/\tau$。凸型 Nesterov 加重启，只需 $T \sim \sqrt{s}$ 步就能减半。**$s$ 和 $\sqrt{s}$ 的差别，正好就是"把 $(\mathbf{x},\boldsymbol{\lambda})$ 当一般单调算子处理"和"利用对偶块是凹函数梯度"之间的差别。**

## 对 B2 的含义

B2 需要在现有族之外加一个参数：对偶外推系数 $\theta$，取常数 $1 - c\sqrt{\tau/s}$。可以把它写成：

$$
\boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + \theta\left(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}\right) + \tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s
$$

然后再配一个 OGDA 型的梯度差修正，来稳定耦合项。$\boldsymbol{\mu}^k$ 和 $\beta$ 可以保留，也可以取 $\beta = 0$，它们不是加速的来源。

从 Fast OGDA 能借的只有离散化手法，即如何用"当前梯度 + 历史梯度差"做到每步一次梯度。它的阻尼参数 $\alpha_0/k$ 本身不能用。

**要点**：Fast OGDA 的 Tikhonov 权重和 anchor 分别对应我们的 $s$ 和 $\beta$，已被族内下界覆盖。它的惯性项在我们的族里没有对应参数，而且是消失型，给不出一致的收缩率。B2 需要新增一个常数对偶动量系数 $\theta = 1 - \Theta(\sqrt{\tau/s})$。

---

## User (2026-11-08 23:59)

我现在周报的内容 不是在于 写文章什么主攻线 B1和B2 不要写那么啰嗦

---

## Assistant (2026-11-09 00:00)

读者：不熟悉鞍点加速文献的合作者或导师。

---

## 周报：单循环 SPLALM 从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$ 的加速机制

**本周结论**

- 现稿复杂度是 $\epsilon^{-3}$，瓶颈只在对偶块：Tikhonov 正则给 $\boldsymbol{\lambda}$ 的强凹模数只有 $1/s = \Theta(\epsilon)$。
- 到 $\epsilon^{-2.5}$，需要把对偶块的内层收缩率从 $1/s$ 提到 $1/\sqrt{s}$。
- 文献中有三类"加速"，只有对偶动量能做到这一点。锚定类方法（包括 Boț 的 fast 系列）加速的是 $\epsilon^{-4} \to \epsilon^{-3}$ 这一段，现稿已经用到了。

### 1. 瓶颈

固定 $\rho = \Theta(1)$ 时，可行性要求 $s = \Theta(\epsilon^{-1})$。单循环复杂度可以拆成两项：

$$
K \asymp \epsilon^{-2} \cdot \frac{1}{\delta}
$$

第一项 $\epsilon^{-2}$ 是外层非凸问题的下界，不能再降。$\delta$ 是内层鞍点子问题每步的收缩率。内层原始块的条件数是 $\Theta(1)$，对偶块的条件数是 $s/\rho = \Theta(\epsilon^{-1})$。

- 普通 GDA：$\delta \sim 1/s$，所以 $K \sim \epsilon^{-3}$。这是现稿的结果，并已证明在算法族内是紧的。
- 加速后：$\delta \sim 1/\sqrt{s}$，所以 $K \sim \epsilon^{-2.5}$。光滑 NC-C 问题上，这一阶已经与 oracle 下界吻合（Pan–Zheng–Li 2026）。

### 2. 三类"加速"分别解决什么

| 工具 | 作用对象 | 效果 | 文献 |
| :--- | :--- | :--- | :--- |
| Tikhonov / 锚定 | 没有曲率的对偶块 | 单调残差从 $1/\sqrt{k}$ 到 $1/k$，对应 $\epsilon^{-4} \to \epsilon^{-3}$；现稿已用 | Boț–Chenchene 2026；Boț–Nguyen 2026；Li–Nagarajan–Pan–Zhang 2026 |
| 外推（EG / OGDA） | $\mathbf{x}$ 与 $\boldsymbol{\lambda}$ 的耦合项引起的旋转 | 本身不改变阶数；加动量时用来保持稳定 | Korpelevich 1976；Popov 1980；Mahdavinia et al. 2022 |
| 对偶动量 | 曲率只有 $1/s$ 的对偶块 | $\epsilon^{-3} \to \epsilon^{-2.5}$ | Zhang–Xu 2026 |

**为什么锚定类方法到不了 $\epsilon^{-2.5}$。** 这类方法把 $(\mathbf{x},\boldsymbol{\lambda})$ 当作一般单调算子处理，而在一般单调类上，$1/k$ 已经是最优速率。Fast OGDA（Boț–Csetnek–Nguyen 2023）带惯性，但它的阻尼随迭代消失，系数是 $1 - \Theta(1/k)$，只能把速率改进到 $o(1/k)$。要到 $\epsilon^{-2.5}$，需要两个条件：

- 只在对偶块上加动量，利用对偶函数是凹函数这一结构；
- 动量系数取常数 $1 - \Theta(\sqrt{\tau/s})$，由对偶曲率 $1/s$ 决定。

现稿的算法族里有 Tikhonov 权重 $s$ 和可移动的对偶中心 $\boldsymbol{\mu}^k$，没有动量项，所以停在 $\epsilon^{-3}$。

### 3. Zhang–Xu（arXiv:2609.17973）

- 问题：对偶域有界的光滑 NC-C minimax。复杂度为单循环 GS $\mathcal{O}(\epsilon^{-2.5})$。
- 算法：投影阻尼 EG、对偶动量和移动近端中心三者结合，对偶正则取 $\Theta(\epsilon)$，相当于我们的 $s \sim \epsilon^{-1}$。
- 证明难点：中心每步都在移动，鞍点随之漂移。他们用"鞍点值间隙 + 动量交叉项"构造 Lyapunov 函数，避开了对漂移的鞍点求导。

### 4. 下一步

在固定 $\rho$ 的 SPLALM 中加入常数系数的对偶动量，研究能否得到 $\epsilon^{-2.5}$，并与族内 $\Theta(\epsilon^{-3})$ 构成分离。

### 参考文献

- Boț, Chenchene. Extragradient method with flexible anchoring. SIAM J. Optim. 36(3), 2026.
- Boț, Nguyen. Tikhonov regularization of monotone operator flows... J. Complexity 94, 2026.
- Boț, Csetnek, Nguyen. Fast OGDA in continuous and discrete time. Found. Comput. Math., 2023.
- Li, Nagarajan, Pan, Zhang. Smoothing meets perturbation. arXiv:2602.14185, 2026.
- Mahdavinia, Deng, Li, Mahdavi. Tight analysis of EG and OG for nonconvex minimax. NeurIPS 2022.
- Pan, Zheng, Li. arXiv:2609.14235, 2026.
- Zhang, Xu. Matching multi-loop complexities with a single loop. arXiv:2609.17973, 2026.
- Korpelevich 1976；Popov 1980。

---

还有两点要提醒你：

- 第 2 节"$1/k$ 在一般单调类上已是最优"依据的是 Yoon–Ryu 2021。这条我是凭记忆写的，所以正文没有引用它。你要写上的话，先核对一下。
- Korpelevich 和 Popov 的完整出处我也没有核对。

---

## User (2026-11-09 00:00)

所以我们现在就是要跳出算法族啊

---

## Assistant (2026-11-09 00:00)

**老大，对。固定 $\rho$ 时必须跳出 $\mathcal{C}_\theta$。改动只需一步：在族里加一个常数对偶动量参数，原族就是这个参数取 0 的特例。**

- **依据**：族内下界对 $s = c_s/\epsilon$ 下所有 $(\alpha,\beta) \in [0,1]^2$ 都给出 $\Omega(\epsilon^{-3})$。所以只调 $\alpha$、$\beta$、$s$ 都不够，必须引入族外的自由度。
- **现稿已经留了位置**：[AlgorithmFamily.tex:133-139](overleaf/sections/AlgorithmFamily.tex#L133-L139) 的 Scope remark 写明，$\mathcal{C}_\theta$ 之外的方法可能更快，并把 Zhang–Xu 列为族外方法达到 $\mathcal{O}(\epsilon^{-5/2})$ 的例子。
- **加入后的结果**：设扩展族为 $\mathcal{C}_\theta$ 加上对偶外推系数 $\theta_m = 1 - \Theta(\sqrt{\tau/s})$。如果在扩展族上证出 $\mathcal{O}(\epsilon^{-2.5})$，它和旧族的 $\Theta(\epsilon^{-3})$ 就构成分离：**多出来的阶数恰好来自这一个动量参数**。
- **方向要选对**：只加外推、加变步长或加锚定，同样都在族外，但前面的分析表明它们都停在 $\epsilon^{-3}$。
- **证明之前先做数值检查**：在 [LowerBound.tex](overleaf/sections/LowerBound.tex) 的困难实例上加入对偶动量，看迭代数随 $\epsilon$ 的斜率是否从 $-3$ 降到 $-2.5$。斜率不降，说明动量在这个实例上无效，后面的证明也就不必投入。

---

## User (2026-11-09 00:01)

## 结论

**Fast OGDA 加速的关键是一个动量系数，而我们的算法族里没有这个参数。** 它需要在对偶更新里加一项 $\theta_k(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1})$。两种取法：

- Fast OGDA 取 $\theta_k \approx 1 - \alpha_0/k$，随迭代次数趋于 1，和 $s$ 无关。
- 我们需要取常数 $\theta = 1 - c\sqrt{\tau/s} = 1 - \Theta(\epsilon^{1/2})$，由对偶曲率 $1/s$ 决定。这就是 Zhang–Xu 的 $\omega$。

（这里用 $\alpha_0$ 表示 Fast OGDA 的阻尼常数，以区别于我们的中心步长 $\alpha$。）

Fast OGDA 的另外两个成分在我们的族里都已存在：Tikhonov 权重对应 $s$，anchor 对应 $\boldsymbol{\mu}^k$ 和 $\beta$。族内下界已经覆盖了这两个成分，所以它们帮不上忙。

## 对照我们的参数

现稿的算法族是 $\mathrm{SPLALM}_{\theta,\alpha,\beta}$，其中 $\theta = (\rho, s, \gamma, \eta, \tau)$（[AlgorithmFamily.tex:37-46](overleaf/sections/AlgorithmFamily.tex#L37-L46)）。对偶中心按下式更新：

$$
\boldsymbol{\mu}^{k+1} = \boldsymbol{\mu}^k + \beta\left(\boldsymbol{\lambda}^{k+1} - \boldsymbol{\mu}^k\right)
$$

| Boț 系列的成分 | 我们族里的对应 | 是否被族内下界覆盖 |
| :--- | :--- | :--- |
| Tikhonov 权重 $\varepsilon(t) \to 0$ | $1/s$；递增分支 $s_k \asymp k$ | 是 |
| 可移动的 anchor | $\boldsymbol{\mu}^k$，移动步长 $\beta$ | 是，$\beta \in [0,1]$ 全部覆盖 |
| 惯性项（消失阻尼 $\alpha_0/t$） | **没有对应参数** | 不在族内 |

前两行说明，现稿实际上已经包含了 Boț–Chenchene 的锚定结构，而且已证明它在族内只能到 $\epsilon^{-3}$。

$\boldsymbol{\mu}^k$ 也带历史信息：它是过去各步 $\boldsymbol{\lambda}$ 的指数平均。但它和动量的作用方向相反：

- $\boldsymbol{\mu}^k$ 通过梯度项 $-(\boldsymbol{\lambda}-\boldsymbol{\mu}^k)/s$ **把 $\boldsymbol{\lambda}$ 拉回**历史平均，作用相当于近端点，效果是增加阻尼。
- 动量项 $\theta(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$ **沿上一步的方向继续推**，作用是放大慢方向上的步长。

所以 $\beta$ 取任何值都无法替代动量。

## 为什么消失阻尼不行，要常数阻尼

两种取法写成公式是：

$$
\theta_k^{\mathrm{FastOGDA}} \approx 1 - \frac{\alpha_0}{k}, \qquad \theta^{\mathrm{need}} = 1 - c\sqrt{\frac{\tau}{s}}
$$

单循环证明的核心是 Lyapunov 函数每步有一个**一致的收缩率** $\delta$，中心步长满足 $\alpha \lesssim \delta$。两种取法给出的收缩率不同：

- **常数阻尼**：$\delta \sim \sqrt{\tau/s} \sim \epsilon^{1/2}$，因此 $\alpha \sim \epsilon^{1/2}$，总复杂度 $\epsilon^{-2.5}$。
- **消失阻尼**：收缩只来自从起点算起的多项式速率，不存在一致的 $\delta$，所以中心步长 $\alpha$ 无法取成常数。

**重启也救不回来。** 设每 $T$ 步重启一次 Fast OGDA。它在一般单调类上的残差界是"距离 / $T$"，而强单调模数为 $1/s$ 时，距离最多是 $s$ 倍的残差：

$$
\lVert F(\mathbf{w}^T) \rVert \lesssim \frac{\lVert \mathbf{w}^0 - \mathbf{w}^\star \rVert}{T} \le \frac{s \lVert F(\mathbf{w}^0) \rVert}{T}
$$

所以要让残差减半，需要 $T \sim s$。这给出 $\delta \sim 1/s$，和现稿完全一样。

只对对偶块做 Nesterov 时情况不同。此时可以利用对偶函数的结构：$\varphi_k(\boldsymbol{\lambda}) = \min_{\mathbf{x}} \mathcal{P}_k$ 是凹函数，强凹模数 $1/s$，光滑常数约 $1/\tau$。凸型 Nesterov 加重启，只需 $T \sim \sqrt{s}$ 步就能减半。**$s$ 和 $\sqrt{s}$ 的差别，正好就是"把 $(\mathbf{x},\boldsymbol{\lambda})$ 当一般单调算子处理"和"利用对偶块是凹函数梯度"之间的差别。**

## 对 B2 的含义

B2 需要在现有族之外加一个参数：对偶外推系数 $\theta$，取常数 $1 - c\sqrt{\tau/s}$。可以把它写成：

$$
\boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + \theta\left(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}\right) + \tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s
$$

然后再配一个 OGDA 型的梯度差修正，来稳定耦合项。$\boldsymbol{\mu}^k$ 和 $\beta$ 可以保留，也可以取 $\beta = 0$，它们不是加速的来源。

从 Fast OGDA 能借的只有离散化手法，即如何用"当前梯度 + 历史梯度差"做到每步一次梯度。它的阻尼参数 $\alpha_0/k$ 本身不能用。

**要点**：Fast OGDA 的 Tikhonov 权重和 anchor 分别对应我们的 $s$ 和 $\beta$，已被族内下界覆盖。它的惯性项在我们的族里没有对应参数，而且是消失型，给不出一致的收缩率。B2 需要新增一个常数对偶动量系数 $\theta = 1 - \Theta(\sqrt{\tau/s})$。 我的意思 跳出算法族 的话 这个对一个什么？

---

## Assistant (2026-11-09 00:01)

**老大，跳出算法族之后，新方法就是"乘子更新加常数系数 Nesterov 外推的 SPLALM"。在 ALM 文献里，它对应 accelerated multiplier update；在 minimax 文献里，对应 Zhang–Xu 的 dual momentum；在 Boț 的连续时间框架里，对应 $\boldsymbol{\lambda}$ 方向上常数阻尼的惯性系统。**

## 新方法在三套文献里的位置

新族记为 $\mathrm{SPLALM}_{\theta,\alpha,\beta,\theta_m}$。它比原族多一个参数 $\theta_m$，乘子更新改为：

$$
\boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + \theta_m\left(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}\right) + \tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s
$$

取 $\theta_m = 0$ 就回到原族 $\mathcal{C}_\theta$。

| 文献语言 | 对应对象 | 与我们的差别 |
| :--- | :--- | :--- |
| ALM | 加速乘子法 / accelerated linearized ALM，例如 He–Yuan 2010、Xu 2017 SIOPT（凭记忆，待核） | 它们针对凸问题，系数取 $\theta_k \approx (k-1)/(k+2)$，随迭代消失；我们针对非凸问题，系数取常数 $1-\Theta(\sqrt{\tau/s})$ |
| minimax | Zhang–Xu 的 dual momentum | 它们有投影、有界对偶域、双步 EG；我们用 ALM 乘子，不做投影 |
| Boț 连续时间 | $\boldsymbol{\lambda}$ 方向上带常数阻尼 $\sim 2/\sqrt{s}$ 的 heavy-ball 系统，加 Tikhonov 项 | Fast OGDA 的阻尼是消失型 $\alpha_0/t$，而且作用在整个 $(\mathbf{x},\boldsymbol{\lambda})$ 上 |

论文里的定位可以这样写：**非凸复合问题上，固定罚参数的 accelerated linearized ALM。族内下界说明，从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$ 的提升全部来自 $\theta_m$。**

## 撞车核查

- **Shi–Wang–Wang 的 MLALM**（MOR 51(1), 2026）标题里有"momentum"，但按摘要，它的动量用在随机梯度的 recursive momentum 估计上，属于方差缩减，不是乘子外推。因此和我们不撞车。项目 `literature.md` 第 71 行目前标为"未核对"，可以改成"已读摘要，动量作用在梯度估计上"。
- **待查新**："非凸约束问题 + 固定罚参数 + 乘子 Nesterov 外推 + 复杂度"这个组合，目前没查到。He–Yuan 和 Xu 2017 的凸情形结果需要核对原文，确认它们的外推系数和适用问题类。

Sources:
- [Shi, Wang, Wang — A Momentum-Based Linearized ALM (MOR)](https://pubsonline.informs.org/doi/10.1287/moor.2022.0193)
- [dblp: MOR Volume 51](https://dblp.org/db/journals/mor/mor51.html)
- [arXiv:2604.13272 — Momentum-based stochastic algorithm for linearly constrained nonconvex optimization](https://arxiv.org/pdf/2604.13272)

---

## User (2026-11-09 00:03)

B2的算法是什么 只告诉我算法

---

## Assistant (2026-11-09 00:04)

**老大，B2 的候选形式如下：每步在同一点 $(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k)$ 调用一次 $\mathcal{O}_{f,\mathcal{A}}$ 和一次 $\mathrm{prox}_{h/\rho}$，原始块做 OGDA 修正，对偶块做常数系数 Nesterov 外推。收敛性待证。**

**参数**：$\rho = \Theta(1)$，$s = c_s/\epsilon$，$\gamma$、$\eta$、$\tau$ 取 $\Theta(1)$，$\beta = 0$（即 $\boldsymbol{\mu}^k \equiv \mathbf{0}$），对偶动量系数 $\theta_m = 1 - c_\theta\sqrt{\tau/s}$，中心步长 $\alpha = c_\alpha\sqrt{\tau/s}$。

**初始化**：$\mathbf{x}^0 = \mathbf{z}^0 = \mathbf{0}$，$\boldsymbol{\lambda}^{-1} = \boldsymbol{\lambda}^0 = \mathbf{0}$，并约定 $\mathbf{g}_x^{-1} = \mathbf{g}_x^0$。

**对 $k \ge 0$ 依次执行：**

1. 对偶外推：

$$
\bar{\boldsymbol{\lambda}}^k = \boldsymbol{\lambda}^k + \theta_m\left(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}\right)
$$

2. 调用一次 prox：

$$
\mathbf{y}^k = \mathrm{prox}_{h/\rho}\left(\mathcal{A}(\mathbf{x}^k) + \frac{\bar{\boldsymbol{\lambda}}^k}{\rho}\right), \qquad \mathbf{q}^k = \bar{\boldsymbol{\lambda}}^k + \rho\left(\mathcal{A}(\mathbf{x}^k) - \mathbf{y}^k\right)
$$

3. 在同一点计算两个梯度：

$$
\mathbf{g}_x^k = \nabla f(\mathbf{x}^k) + \nabla\mathcal{A}(\mathbf{x}^k)^{\top}\mathbf{q}^k + \frac{1}{\gamma}\left(\mathbf{x}^k - \mathbf{z}^k\right)
$$

$$
\mathbf{g}_\lambda^k = \mathcal{A}(\mathbf{x}^k) - \mathbf{y}^k - \frac{1}{s}\bar{\boldsymbol{\lambda}}^k
$$

4. 原始步，带 OGDA 修正：

$$
\mathbf{x}^{k+1} = \mathbf{x}^k - \eta\left(2\mathbf{g}_x^k - \mathbf{g}_x^{k-1}\right)
$$

5. 对偶步，从外推点出发：

$$
\boldsymbol{\lambda}^{k+1} = \bar{\boldsymbol{\lambda}}^k + \tau\,\mathbf{g}_\lambda^k
$$

6. 中心更新：

$$
\mathbf{z}^{k+1} = \mathbf{z}^k + \alpha\left(\mathbf{x}^{k+1} - \mathbf{z}^k\right)
$$

取 $\theta_m = 0$ 并去掉 OGDA 修正，得到 Jacobi 型的 SPLALM（$\beta = 0$）。它和现稿的区别在于现稿是交替更新：对偶步使用 $\mathbf{x}^{k+1}$。

Sources（前一轮核查）：[Shi–Wang–Wang MLALM](https://pubsonline.informs.org/doi/10.1287/moor.2022.0193)

---

## User (2026-11-09 00:05)

为什么要额外写这么多 两句话告诉我 和别人加速的区别 zhang的

---

## Assistant (2026-11-09 00:05)

与 Zhang–Xu 相比，B2 用原始块的 OGDA 修正替代双步 EG，用 ALM 乘子的内在恢复项替代对有界对偶域的投影，所以每步只需一次梯度和一次 prox，而 Zhang–Xu 需要两次梯度和两次投影。与 Fast OGDA 和凸情形的 accelerated ALM 相比，B2 的动量只加在对偶块上，系数是由 $1/s$ 决定的常数 $1-\Theta(\sqrt{\tau/s})$，它们的系数则随迭代次数消失、取值与 $s$ 无关。

---

## User (2026-11-09 00:12)

所以加速的motivation其实看到有人做加速我们就去做了 但是不知道选什么技巧 也不知道为什么？1-2句话说清楚

---

## Assistant (2026-11-09 00:12)

动机来自我们自己的族内下界：它指出 $\epsilon^{-3}$ 的唯一来源是对偶块每步只能收缩 $1/s$，而调整族内任何参数 $(\alpha,\beta)$ 都消不掉这个瓶颈，所以要加速，只能针对对偶块引入族外的自由度。选常数系数的对偶动量，是因为对条件数为 $s$ 的强凹块，一阶方法要把收缩率从 $1/s$ 提到最优的 $1/\sqrt{s}$，就必须用带常数阻尼的记忆；外推和锚定都做不到这一点，Zhang–Xu 的结果只说明这条路在单循环里可行。

---

## User (2026-11-09 00:12)

可选的技术有哪些 哪些可能初步可行呢

---

## Assistant (2026-11-09 00:12)

**老大，初步可行的有三项：对偶 Nesterov 外推（B2）、对偶梯度累加器配合 EG（B1），以及先做连续时间常数阻尼系统再离散化，第三项主要作为 B2 的证明工具。其余候选不是只停在 $\epsilon^{-3}$，就是要放弃单循环。**

| 技术 | 能否把 $s$ 降到 $\sqrt{s}$ | 初步判断 |
| :--- | :--- | :--- |
| 对偶块常数系数 Nesterov 外推，原始块加 OGDA / PDHG 修正（B2） | 能，利用对偶函数 $\varphi_k$ 的强凹结构 | **可行**；风险在耦合项的稳定性和移动中心下的 Lyapunov 构造 |
| 对偶梯度累加器配合 EG（B1，Zhang–Xu 形式） | 能，Zhang–Xu 已证 | **可行，确定性最高**；新意偏薄 |
| 连续时间：$\boldsymbol{\lambda}$ 方向带常数阻尼 $\sim 2/\sqrt{s}$ 的惯性系统，再离散化 | 能（推断） | **可行**，作为构造 B2 Lyapunov 函数的方法 |
| 双线性耦合的加速原始–对偶方法（APDG、Lifted PD） | 双线性耦合下能 | **部分可行**：只适用于仿射 $\mathcal{A}$；$\mathcal{D}_\rho$ 中的耦合经过 $h$ 的 Moreau 包络，不是双线性的，需要另作推广 |
| 对偶块 Polyak heavy-ball | 二次函数上能 | 风险较高：非二次强凸函数上，heavy-ball 没有全局加速保证（Lessard–Recht–Packard 2016，凭记忆，待核）；$\varphi_k$ 一般不是二次的 |
| 对偶块的 Catalyst / 加速近端点 | 能 | 舍弃：需要内层循环，不是单循环 |
| Chebyshev 变步长、silver 长步长 | 前者要求冻结中心，后者只到 $\kappa^{0.786}$ | 舍弃 |
| 锚定、Fast OGDA 及其重启 | 不能，停在 $s$ | 舍弃 |
| Anderson 加速 | 没有最坏情形保证 | 舍弃 |

建议的顺序：先在困难实例上数值对比 B2 和 B1 的斜率，B2 斜率达到 $-2.5$，再用连续时间系统构造它的 Lyapunov 函数。

---

## User (2026-11-09 00:13)

对偶块常数系数 Nesterov 外推，原始块加 OGDA / PDHG 修正（B2）	能，利用对偶函数 $\varphi_k$ 的强凹结构	可行；风险在耦合项的稳定性和移动中心下的 Lyapunov 构造
对偶梯度累加器配合 EG（B1，Zhang–Xu 形式） 这个是两种加速技巧吗？

---

## Assistant (2026-11-09 00:14)

**老大，它们是同一种加速技巧：两者都是常数系数为 $1-\Theta(\sqrt{\tau/s})$ 的对偶动量。区别只在动量的写法和配套的稳定器。**

- **动量的写法**：B2 在迭代点上做外推 $\boldsymbol{\lambda}^k+\theta_m(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$，属于 Nesterov 型。B1 维护一个梯度累加器 $\mathbf{v}^{k+1}=\omega\mathbf{v}^k+c\nabla_{\boldsymbol{\lambda}}\mathcal{P}$，也就是对过去的对偶梯度做指数加权求和，属于 heavy-ball 型。两者都在对偶慢方向上累积约 $\sqrt{s}$ 步的同向信息，所以加速来源相同。
- **稳定器**：B1 用双步 EG，每步两次梯度和两次 prox。B2 用原始块的 OGDA 修正，每步一次梯度和一次 prox。
- **待核**：B1 的累加器形式来自你之前那版周报对 Zhang–Xu 的转述，我没有对照原文核对。

---

## User (2026-11-09 00:14)

加速机制 一种是achoring 一种是 momentum动量

---

## Assistant (2026-11-09 00:14)

**老大，对，有两种加速机制，但它们加速的是不同阶段。** 锚定（anchoring / Tikhonov）针对没有曲率的单调问题，把残差从 $1/\sqrt{k}$ 提到 $1/k$，对应 $\epsilon^{-4}\to\epsilon^{-3}$，现稿已经用到。动量针对曲率只有 $1/s$ 的对偶块，把收缩率从 $1/s$ 提到 $1/\sqrt{s}$，对应 $\epsilon^{-3}\to\epsilon^{-2.5}$。外推（EG / OGDA）不单独算一种加速机制，它在加动量时负责稳定耦合项。

---

## User (2026-11-09 00:14)

achoring+外推点

---

## Assistant (2026-11-09 00:15)

**老大，锚定加外推就是 EAG / 锚定 EG（Yoon–Ryu 2021；Boț–Chenchene 2026），它在单调问题上把残差速率做到 $1/k$，对应的仍是 $\epsilon^{-4}\to\epsilon^{-3}$ 这一段。** 两者组合起来并不叠加加速：外推负责稳定耦合项引起的旋转，锚定提供 $1/k$ 的速率，可内层子问题已经带有曲率 $1/s$，这个组合每步的收缩率仍是 $1/s$。要把 $s$ 降到 $\sqrt{s}$，还需要加对偶动量。

---

## User (2026-11-09 00:15)

是他们的

---

## Assistant (2026-11-09 00:15)

**老大，如果"他们"指 Zhang–Xu：他们的算法里确实同时有锚定和外推，但 $\epsilon^{-2.5}$ 来自他们另外加的对偶动量。** 按 [lit-check-retreat-20261104.md](overleaf/notes/progress/lit-check-retreat-20261104.md) 第 23 行的核对，Zhang–Xu 有四个组成部分：以原点为中心的对偶正则（GS 下 $\tau=\Theta(\epsilon)$，作用是锚定）、移动近端中心、extragradient（外推）、对偶动量。Boț–Chenchene 只有锚定和外推，所以停在 $1/k$。两者相差的正是对偶动量，这一项把 $\epsilon^{-3}$ 推到 $\epsilon^{-2.5}$。

---

## User (2026-11-09 00:15)

但是他们没用nesterov

---

## Assistant (2026-11-09 00:15)

**老大，对，Zhang–Xu 用的是对偶梯度累加器，不是 Nesterov 外推。不过 Nesterov、heavy-ball 和梯度累加器都属于动量：它们都用常数系数，在对偶慢方向上累积约 $\sqrt{s}$ 步的历史信息，加速都来自这一点。** 三种形式的区别在于梯度在哪个点计算、历史信息存放在哪里。Nesterov 在外推点计算梯度。heavy-ball 和累加器在当前点计算梯度，把历史信息存在步长差或累加器 $\mathbf{v}^k$ 里。这个区别对证明有影响：对非二次的强凸函数，heavy-ball 型没有全局加速保证（Lessard–Recht–Packard 2016，凭记忆，待核），Nesterov 型有。所以 B2 选 Nesterov 形式有明确理由。Zhang–Xu 的累加器能成立，我推断是配合了 EG 的预测步，这一点需要对照原文核实。

---

## User (2026-11-09 00:15)

他们用的heavybal

---

## Assistant (2026-11-09 00:16)

**老大，从代数形式上看算 heavy-ball 型，但论文自己没有这么叫。我核对了 arXiv HTML 版的 Algorithm 1，论文称之为 "dual momentum"，整个子问题迭代叫 "modified damped extragradient method"。** 动量变量是对偶梯度的指数平均：

$$
\mathbf{v}_{t+1} = \alpha\mathbf{v}_t + (1-\alpha)\gamma\left[\nabla_{\mathbf{y}}G(\mathbf{x}_{t+1},\mathbf{y}_{t+1},\mathbf{z}_t) - \mathbf{n}_{t+1}\right]
$$

校正步是：

$$
\mathbf{y}_{t+1} = \Pi_{\mathcal{Y}}\left(\mathbf{y}_t + h\left[\nabla_{\mathbf{y}}G(\tilde{\mathbf{x}}_t,\tilde{\mathbf{y}}_t,\mathbf{z}_t) + \bar{\mathbf{v}}_t\right]\right)
$$

这里的 $\alpha$ 是他们的动量系数，与我们的中心步长无关；$\mathbf{n}_t$ 是法锥变量。

**为什么算 heavy-ball 型**：展开后，每步位移是过去梯度的指数加权和，heavy-ball 的步长差递推展开后也是这个形式。

**与普通 heavy-ball 的区别**：梯度在 EG 预测点 $(\tilde{\mathbf{x}}_t,\tilde{\mathbf{y}}_t)$ 上计算，外层还套着投影和法锥修正。我上一条推断过，heavy-ball 型能在非二次问题上成立，靠的是 EG 的预测步，原文的结构与这个推断一致。但这个机制是否就是他们证明的关键，需要读完 Section 3.2 之后的证明部分才能确认。

**修正上一条**：之前说 B1 的累加器形式"未核对"，现在已经核对，与 Algorithm 1 一致。

Source: [arXiv:2609.17973 HTML](https://arxiv.org/html/2609.17973)

---

## User (2026-11-09 00:16)

我们的思路来自于对于单调算子还是什么FastOGAD 阻尼什么的可以加速  想到用nesterov 先不用管什么常数补偿数

---

## Assistant (2026-11-09 00:16)

**老大，这条思路链可以成立：Fast OGDA 说明，单调算子上"惯性加 optimistic 修正"是稳定的，而且每步只需一次梯度，这正是 B2 的算法骨架。但有一处不能当作常数细节放掉：阻尼的阶。** Fast OGDA 的动量系数是 $1-\Theta(1/k)$，照搬过来只能到 $\epsilon^{-3}$。换成 $1-\Theta(\sqrt{\tau/s})$ 才是 $\epsilon^{-2.5}$。这两者相差的是 $\epsilon$ 的幂次，只有前面的常数 $c$ 可以暂时不管。所以动机可以这样写：从 Fast OGDA 取"对偶惯性 + OGDA 修正"的结构，把消失阻尼换成由对偶曲率 $1/s$ 决定的常数阻尼，就得到对偶块上的强凸型 Nesterov。

---

## User (2026-11-09 00:17)

我们就想想 阻尼实际上 我们实际上应该写出几个干净的式子 怎么从原来的正则化问题变到用阻尼解释然后再到加2.5

---

## Assistant (2026-11-09 00:18)

**老大，整条链分四步。第一，正则化给对偶块带来曲率 $\mu_\lambda=1/s$。第二，现稿的对偶步是梯度流的离散，每步收缩 $\tau/s$。第三，换成临界阻尼的二阶流，衰减率从 $\mu_\lambda$ 提到 $\sqrt{\mu_\lambda}$，离散后每步收缩 $\sqrt{\tau/s}$。第四，代入单循环复杂度，得到 $\epsilon^{-2.5}$。**

### 1. 正则化后的对偶问题

固定中心 $\mathbf{z}$，取 $\boldsymbol{\mu}=\mathbf{0}$，先把 $\mathbf{x}$ 消去：

$$
\varphi(\boldsymbol{\lambda}) = \min_{\mathbf{x}} \mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\mathbf{0})
$$

$\varphi$ 是 $\mu_\lambda$-强凹且 $L_\varphi$-光滑的函数，其中 $\mu_\lambda = 1/s$，步长取 $\tau \le 1/L_\varphi$。这个曲率全部来自正则项 $-\lVert\boldsymbol{\lambda}\rVert^2/(2s)$。

### 2. 现稿：一阶梯度流

$$
\dot{\boldsymbol{\lambda}} = \nabla\varphi(\boldsymbol{\lambda})
$$

$$
\varphi^\star - \varphi(\boldsymbol{\lambda}(t)) \le e^{-2\mu_\lambda t}\left(\varphi^\star - \varphi(\boldsymbol{\lambda}(0))\right)
$$

以 $\tau$ 为时间步离散，得到现稿的对偶步 $\boldsymbol{\lambda}^{k+1}=\boldsymbol{\lambda}^k+\tau\nabla\varphi(\boldsymbol{\lambda}^k)$。衰减率 $\mu_\lambda$ 乘以时间步 $\tau$，得到每步收缩率：

$$
\delta_{\mathrm{GD}} = \mu_\lambda\tau = \frac{\tau}{s}
$$

### 3. 阻尼解释：二阶流

$$
\ddot{\boldsymbol{\lambda}} + \gamma\dot{\boldsymbol{\lambda}} = \nabla\varphi(\boldsymbol{\lambda})
$$

沿曲率为 $\mu_\lambda$ 的慢方向，特征方程为 $r^2+\gamma r+\mu_\lambda=0$。记最慢的衰减率为 $\nu(\gamma)$，按阻尼大小分两种情形：

- **过阻尼**，$\gamma \ge 2\sqrt{\mu_\lambda}$：此时

$$
\nu(\gamma) = \frac{\gamma - \sqrt{\gamma^2 - 4\mu_\lambda}}{2} \approx \frac{\mu_\lambda}{\gamma}
$$

$\gamma$ 很大时，这个系统退化为梯度流，这就是第 2 步的情形。

- **欠阻尼**，$\gamma \le 2\sqrt{\mu_\lambda}$：$\nu(\gamma) = \gamma/2$。Fast OGDA 取 $\gamma(t)=\alpha_0/t$，迭代后期进入欠阻尼区，$\nu = \alpha_0/(2t) \to 0$，因此没有一致的收缩率。

两种情形在临界阻尼处衔接，衰减率在这里取到最大：

$$
\max_{\gamma \gt 0}\nu(\gamma) = \nu\left(2\sqrt{\mu_\lambda}\right) = \sqrt{\mu_\lambda} = \frac{1}{\sqrt{s}}
$$

### 4. 离散：得到对偶 Nesterov

以 $h=\sqrt{\tau}$ 为时间步，离散临界阻尼方程：

$$
\frac{\boldsymbol{\lambda}^{k+1} - 2\boldsymbol{\lambda}^k + \boldsymbol{\lambda}^{k-1}}{\tau} + 2\sqrt{\mu_\lambda}\,\frac{\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}}{\sqrt{\tau}} = \nabla\varphi(\bar{\boldsymbol{\lambda}}^k)
$$

整理得：

$$
\boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + \left(1 - 2\sqrt{\frac{\tau}{s}}\right)\left(\boldsymbol{\lambda}^k - \boldsymbol{\lambda}^{k-1}\right) + \tau\nabla\varphi(\bar{\boldsymbol{\lambda}}^k)
$$

梯度在外推点 $\bar{\boldsymbol{\lambda}}^k$ 计算，就是 Nesterov；在 $\boldsymbol{\lambda}^k$ 计算，就是 heavy-ball，Zhang–Xu 属于后者。衰减率 $\sqrt{\mu_\lambda}$ 乘以时间步 $\sqrt{\tau}$，得到每步收缩率：

$$
\delta_{\mathrm{damp}} = \sqrt{\mu_\lambda}\cdot\sqrt{\tau} = \sqrt{\frac{\tau}{s}}
$$

### 5. 代入单循环复杂度

单循环分析给出：中心步长满足 $\alpha \lesssim \delta$，复杂度 $K \asymp \epsilon^{-2}/\alpha$。取 $\tau=\Theta(1)$、$s=c_s/\epsilon$：

$$
K_{\mathrm{GD}} \asymp \epsilon^{-2}\cdot\frac{s}{\tau} = \epsilon^{-3}, \qquad K_{\mathrm{damp}} \asymp \epsilon^{-2}\sqrt{\frac{s}{\tau}} = \epsilon^{-2.5}
$$

### 待证

1. 算法中用一步 $\mathbf{x}$ 梯度代替 $\min_{\mathbf{x}}$。这一步依赖 $\kappa_x=\Theta(1)$，由此产生的耦合误差需要 OGDA 修正来控制。
2. 中心 $\mathbf{z}^k$ 移动时，Lyapunov 函数仍要保持每步 $\sqrt{\tau/s}$ 的收缩。
3. 第 3 步的谱分析只对二次方向严格成立。对一般的强凹 $\varphi$，需要用 Lyapunov 函数代替特征根。

---

## User (2026-11-09 00:19)

我的意思是 哪一个式子 怎么对应离散算法 然后 哪些参数需要变

---

## Assistant (2026-11-09 00:20)

**老大，对应关系如下。现稿的对偶步是梯度流 $\dot{\boldsymbol{\lambda}}=\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s$ 以 $\tau$ 为时间步离散得到的。新算法的对偶步是阻尼方程 $\ddot{\boldsymbol{\lambda}}+\gamma_d\dot{\boldsymbol{\lambda}}=\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s$ 以 $\sqrt{\tau}$ 为时间步离散得到的。参数上只需新增一个动量系数 $\theta_{m}$，并调整 $s_k$ 和 $\alpha_k$ 的增长阶。**

这里用 $\gamma_d$ 表示阻尼系数，避免与近端参数 $\gamma$ 混淆。

### 连续方程与离散步的对应

| 连续方程 | 离散步 | 所在位置 |
| :--- | :--- | :--- |
| $\dot{\mathbf{x}} = -\nabla_{\mathbf{x}}\mathcal{P}_s$ | $\mathbf{x}^{k+1}=\mathbf{x}^k-\eta\nabla_{\mathbf{x}}\mathcal{P}_s$ | 现稿与新算法相同 |
| $\dot{\boldsymbol{\lambda}} = \nabla_{\boldsymbol{\lambda}}\mathcal{P}_s$ | $\boldsymbol{\lambda}^{k+1}=\boldsymbol{\lambda}^k+\tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s$ | 现稿 |
| $\ddot{\boldsymbol{\lambda}}+\gamma_d\dot{\boldsymbol{\lambda}} = \nabla_{\boldsymbol{\lambda}}\mathcal{P}_s$ | 见下式 | 新算法 |
| $\dot{\mathbf{z}} = \alpha(\mathbf{x}-\mathbf{z})$ | $\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha_k(\mathbf{x}^{k+1}-\mathbf{z}^k)$ | 两者形式相同，$\alpha_k$ 的阶不同 |

新算法的对偶步：

$$
\boldsymbol{\lambda}^{k+1} = \boldsymbol{\lambda}^k + \theta_{m,k}\left(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}\right) + \tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\boldsymbol{\mu}^k)
$$

动量系数由阻尼和时间步决定，取临界阻尼 $\gamma_d=2/\sqrt{s}$：

$$
\theta_{m} = 1-\gamma_d\sqrt{\tau} = 1-2\sqrt{\frac{\tau}{s}}
$$

### 参数变化

现稿的参数取自 [UpperBound.tex:84-100](overleaf/sections/UpperBound.tex#L84-L100)，按 anytime 形式写。

| 参数 | 现稿 | 新算法 | 是否改变 |
| :--- | :--- | :--- | :--- |
| $\rho$、$\gamma$、$\eta$、$\tau$ | 常数 | 常数 | 不变 |
| $s_k$ | $c_s(k+1)^{1/3}$ | $c_s(k+1)^{2/5}$ | 改变 |
| $\alpha_k$ | $\Theta(\tau/s_k)=\Theta(k^{-1/3})$ | $\Theta(\sqrt{\tau/s_k})=\Theta(k^{-1/5})$ | 改变 |
| $\theta_{m,k}$ | 无，即 $0$ | $1-2\sqrt{\tau/s_k}=1-\Theta(k^{-1/5})$ | 新增 |
| $\beta_k$ | $\theta_\mu/(k+k_0)$ | 可保留，也可取 $0$ | 不是加速的来源 |
| 结构 | 交替更新 | 原始块加 OGDA 修正 | 新增，不含参数 |

$s_k$ 的阶这样确定：单循环下残差约为 $1/s$，复杂度满足

$$
K \asymp \epsilon^{-2}\sqrt{s}
$$

令 $\epsilon \sim 1/s$，得到 $s \sim K^{2/5}$，残差为 $\mathcal{O}(K^{-2/5})$，即复杂度 $\epsilon^{-2.5}$。现稿对应的是 $s\sim K^{1/3}$，即 $\epsilon^{-3}$。

**$\theta_{m,k}$ 与 Fast OGDA 的区别**：$\theta_{m,k}=1-\Theta(k^{-1/5})$ 跟随 $s_k$ 缓慢变化，在每个 $k$ 上都与当前曲率 $1/s_k$ 匹配。Fast OGDA 取 $1-\Theta(k^{-1})$，阻尼下降得更快，很快进入欠阻尼区。

**待证**：$s_k$ 随 $k$ 变化时，当前曲率 $1/s_k$ 也在变，所以要证明动量系数始终跟得上。这一项与中心移动的误差一起，并入 Lyapunov 分析。

---

## User (2026-11-09 00:23)

比 Zhang–Xu 少一半梯度与投影（OGDA 代替 EG，乘子恢复项代替投影）；与 Fast OGDA [9]、凸
accelerated ALM [HeYuan2010AccelALM, Xu2017AccelPD] 不同，系数为常数。 这个本质的区别是什么？
难点是什么 最凝练的语言

---

## Assistant (2026-11-09 00:23)

**本质区别**：我们的阻尼按 Tikhonov 正则提供的对偶曲率 $1/s$ 取临界值，即 $\gamma_d=2/\sqrt{s}$。Fast OGDA 和凸 accelerated ALM 的阻尼按迭代次数衰减，它们是为零曲率问题设计的。与 Zhang–Xu 相比，加速机制相同，区别在于对偶变量是无界的 ALM 乘子，有界性靠恢复项 $(\mathbf{q}-\boldsymbol{\lambda})/\rho$ 保证，而不是靠投影。

**难点**：要构造一个 Lyapunov 函数，同时满足四个要求：

- 在只用一次梯度的 OGDA 格式下，每步按 $\sqrt{\tau/s}$ 收缩；
- 吸收步长为 $\alpha\sim\sqrt{\tau/s}$ 的中心漂移；
- 控制一步 $\mathbf{x}$ 梯度带来的耦合误差；
- 在动量把位移放大到约 $\sqrt{s}$ 倍的情况下，不做投影也能保持 $\boldsymbol{\lambda}^k$ 有界。

**措辞修正**：原句写"系数为常数"，这只对固定 $s=c_s/\epsilon$ 的版本成立。anytime 版本的系数是 $1-\Theta(k^{-1/5})$。建议统一写成"**动量系数由对偶曲率 $1/s$ 决定**"，这样两个版本都适用，也正好把我们和 Fast OGDA 那类按迭代次数衰减的系数区分开。

---

## User (2026-11-09 00:24)

加速机制不一样吧

---

## Assistant (2026-11-09 00:25)

**老大，你说得对，我上一条写"加速机制相同"不准确。更准确的说法是：两者的阻尼阶相同，离散类型不同。Zhang–Xu 是 heavy-ball 加 EG，我们是 Nesterov 加 OGDA。**

我刚核对了 arXiv HTML 版第 4.3 节的式 (4.3)。他们的 $\tau$ 对应我们的 $1/s$，$\beta$ 对应我们的中心步长 $\alpha$。

- **阻尼阶相同**：他们的动量系数满足 $1-\alpha_{\mathrm{ZX}}=\Theta(\sqrt{\tau_{\mathrm{ZX}}/L})$，换成我们的记号是 $\Theta(1/\sqrt{s})$，与临界阻尼 $\gamma_d=2/\sqrt{s}$ 同阶。他们的中心步长 $\beta=\Theta(\sqrt{\tau_{\mathrm{ZX}}/L})$，也与我们的 $\alpha\sim\sqrt{\tau/s}$ 同阶。
- **离散类型不同**：他们在当前点或 EG 预测点计算梯度，再做指数平均，属于 heavy-ball 型。增益 $\gamma_{\mathrm{ZX}}=\Theta(\sqrt{L/\tau_{\mathrm{ZX}}})$ 把累加量放大约 $\sqrt{s}$ 倍。heavy-ball 在非二次问题上没有全局加速保证，所以需要 EG 的预测步来补足（推断，原文没有给出机制解释）。我们在外推点计算梯度，属于 Nesterov 型。外推本身已经起到预测作用，所以只需 OGDA 修正，每步一次梯度。

修正后，与 Zhang–Xu 的本质区别是：**阻尼都按对偶曲率 $1/s$ 取临界值，但他们用 heavy-ball 配 EG，我们用 Nesterov 配 OGDA，后者每步少一次梯度。**

另外，原文没有解释对偶动量为什么带来加速。原文唯一相关的说法是："Positive $\tau$ supplies the dual curvature needed when the original problem is merely concave."

Source: [arXiv:2609.17973 HTML](https://arxiv.org/html/2609.17973)

---

## User (2026-11-09 00:27)

比 Zhang--Xu 少一半梯度与投影（OGDA 代替 EG，乘子恢复项代替投影）；与 Fast OGDA \cite{BotCsetnekNguyen2025FastOGDA}、凸 accelerated ALM \cite{HeYuan2010AccelALM,Xu2017AccelPD} 不同，系数为常数。 这个怎么修改一下叙述

---

## Assistant (2026-11-09 00:27)

**老大，需要改三处。第一，"少一半投影"不准确：我们每步没有投影，只有一次 prox。第二，与 Zhang–Xu 的区别要写成离散类型的区别，因为两者的阻尼阶相同。第三，"系数为常数"改成"由对偶曲率决定"，这样 anytime 版本的 $1-\Theta(k^{-1/5})$ 也能涵盖。**

```latex
与 Zhang--Xu 相同，动量阻尼按对偶曲率 $1/s$ 取临界阶 $1-\Theta(s^{-1/2})$；
不同在离散方式：Zhang--Xu 用 heavy-ball 型对偶动量配 extragradient，
每步两次梯度、两次投影；本文用 Nesterov 型对偶外推配 OGDA 修正，
每步一次梯度、一次 $\mathrm{prox}_h$，乘子有界性由恢复项
$(\mathbf{q}-\boldsymbol{\lambda})/\rho$ 保证，无需投影。
与 Fast OGDA \cite{BotCsetnekNguyen2025FastOGDA} 及凸 accelerated ALM
\cite{HeYuan2010AccelALM,Xu2017AccelPD} 不同，本文的动量系数由对偶曲率
$1/s$ 决定，不随迭代次数衰减。
```

**引用需要核对**：

- `BotCsetnekNguyen2025FastOGDA`：按我核对的结果，Fast OGDA 发表在 FoCM 2023，key 里的年份对不上。
- `HeYuan2010AccelALM` 和 `Xu2017AccelPD`：我还没有核对原文，需要确认它们的外推系数确实随迭代次数衰减。

---

## User (2026-11-09 00:28)

与 Zhang--Xu不同在离散方式：Zhang--Xu 用 heavy-ball 型对偶动量结合 extragradient，
因此每步两次梯度（啥梯度）；如果用用 Nesterov 型对偶外推结合OGDA 修正，
每步一次梯度 ？我只关心这个

---

## Assistant (2026-11-09 00:29)

**老大，这里的"一次梯度"指在一个点上调用一次一阶 oracle，同时得到 $\nabla_{\mathbf{x}}$ 和 $\nabla_{\boldsymbol{\lambda}}$ 两个分量。在我们的问题里，一次调用包含 $\nabla f$、$\mathcal{A}(\mathbf{x})$、$\nabla\mathcal{A}(\mathbf{x})^{\top}\mathbf{q}$，外加一次求 $\mathbf{q}$ 的 $\mathrm{prox}_h$。**

- **Zhang–Xu 每步两次**：预测步在 $(\mathbf{x}_t,\mathbf{y}_t)$ 上算一次 $\nabla G$，校正步在预测点 $(\tilde{\mathbf{x}}_t,\tilde{\mathbf{y}}_t)$ 上再算一次。动量更新要用的 $\nabla_{\mathbf{y}}G(\mathbf{x}_{t+1},\mathbf{y}_{t+1})$ 就是下一步预测点的梯度，可以复用，不额外计数。
- **B2 每步一次**：只在 $(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k)$ 上算一次，得到 $\mathbf{g}_x^k$ 和 $\mathbf{g}_\lambda^k$。OGDA 修正 $2\mathbf{g}_x^k-\mathbf{g}_x^{k-1}$ 中的 $\mathbf{g}_x^{k-1}$ 是上一步存下来的，不需要重新计算。Nesterov 外推 $\bar{\boldsymbol{\lambda}}^k$ 只是迭代点的线性组合，也不需要梯度。

所以这句可以写成："Zhang–Xu 每步在两个点上调用一阶 oracle，B2 每步在一个点上调用一次。"

---

## User (2026-11-09 00:29)

我们只需要改写这句话 不要给我这么多废话

---

## Assistant (2026-11-09 00:29)

```latex
与 Zhang--Xu 不同在离散方式：Zhang--Xu 用 heavy-ball 型对偶动量结合 extragradient，每步需在两个点上调用一阶 oracle；本文用 Nesterov 型对偶外推结合 OGDA 修正，每步只在一个点上调用一次。
```

---

## User (2026-11-09 00:30)

我们可以预见的困难是什么呢？ 最本质的 我们现在s可以是1/k实际上 因为跳出族了吗

---

## Assistant (2026-11-09 00:30)

**老大，两个问题分开答。第一，最本质的困难是：动量会把内层的不精确性放大。第二，$s_k$ 不能取到 $k$ 量级。跳出算法族之后改变的是中心步长 $\alpha$ 的上限，$s_k$ 的增长阶仍由可行性与驻点性之间的平衡决定，从 $k^{1/3}$ 变成 $k^{2/5}$。**

### 最本质的困难

Nesterov 动量要求在 $\varphi_k(\boldsymbol{\lambda})=\min_{\mathbf{x}}\mathcal{P}_s$ 上拿到精确梯度。算法实际给出的是不精确的梯度，误差有两个来源：

- $\mathbf{x}$ 只走一步梯度，没有求解 $\min_{\mathbf{x}}$；
- 中心 $\mathbf{z}^k$ 每步都在移动。

普通梯度法对这类误差不累积，加速方法会在约 $\sqrt{s}$ 步的记忆窗口内把误差累积起来（Devolder–Glineur–Nesterov 2014 的 inexact oracle 结果，凭记忆，待核）。更麻烦的是，$\boldsymbol{\lambda}$ 带上动量后移动得更快，$\mathbf{x}$ 的跟踪误差 $\lVert\mathbf{x}^k-\mathbf{x}^\star(\bar{\boldsymbol{\lambda}}^k)\rVert$ 也随之放大。

因此，Lyapunov 函数必须证明：**这些误差以与加速相同的速率 $\sqrt{\tau/s}$ 被压下去，而不是在动量窗口内累积。** 乘子有界性和耦合稳定性都是这个问题的具体表现。

### $s_k$ 的阶

设 $\alpha\sim\delta$，$K$ 步之后有两个误差：

$$
\text{驻点性}^2 \sim \frac{1}{\alpha K}, \qquad \text{可行性} \sim \frac{1}{s}
$$

令两者平衡：

| 情形 | $\alpha$ | 平衡条件 | $s_K$ | 复杂度 |
| :--- | :--- | :--- | :--- | :--- |
| 现稿 | $1/s$ | $s/K = s^{-2}$ | $K^{1/3}$ | $\epsilon^{-3}$ |
| 加动量 | $1/\sqrt{s}$ | $\sqrt{s}/K = s^{-2}$ | $K^{2/5}$ | $\epsilon^{-2.5}$ |
| 加动量，强取 $s_k\sim k$ | $1/\sqrt{k}$ | 可行性 $1/K$，驻点性 $K^{-1/4}$ | $K$ | $\epsilon^{-4}$ |

如果取 $s_k\sim k$，可行性更好，但 $\alpha$ 降得太快，驻点性反而变差，总体退回 $\epsilon^{-4}$。retreat 笔记里"$s_k\asymp k$ 时残差为 $1/k$"那一条，说的只是乘子残差的渐近速率，不涉及复杂度最优的选择。

---

## User (2026-11-09 00:30)

这个其实也是一个问题

sk 如果类似于1/kq是否还值得分析

---

## Assistant (2026-11-09 00:31)

**老大，单独为一般的 $q$ 写一套分析不值得：在复杂度意义下，最优值只有 $q=2/5$。但证明本来就要对缓变的 $s_k$ 写一般形式，一般 $q$ 的速率可以顺带得到，放进一条 Remark 就够了。**

下面按 Tikhonov 权重 $1/s_k\sim k^{-q}$，即 $s_k=c_sk^q$ 来理解你的问题。

**一般 $q$ 下的速率（推断，待证）。** 加动量后中心步长 $\alpha_k\sim k^{-q/2}$。$K$ 步后，驻点性的平方约为 $1/\sum_k\alpha_k\sim K^{-(1-q/2)}$，可行性约为 $1/s_K\sim K^{-q}$。所以

$$
\epsilon_K \sim K^{-\min\left\{q,\ \frac{1}{2}-\frac{q}{4}\right\}}, \qquad 0 \lt q \lt 2
$$

两项在 $q=2/5$ 时相等，此时 $\epsilon_K\sim K^{-2/5}$，对应复杂度 $\epsilon^{-2.5}$。现稿不带动量的对应式为 $\min\{q,(1-q)/2\}$，最优点 $q=1/3$。

**一般 $q$ 的用处在渐近分析，不在复杂度。**

- $q\lt 2/5$：驻点性更快，可行性受限。
- $q\gt 2/5$：可行性更快，驻点性受限。乘子的 last-iterate 行为，例如是否强收敛到最小范数乘子，需要 $s_k\to\infty$ 足够快。这是 Boț 合作线关心的问题，可以在那里单独研究。

**写法建议。** 定理证明只要求 $s_k$ 单调递增且满足 $s_{k+1}/s_k\to1$，主结果取 $q=2/5$，一般 $q$ 的速率写成推论或 Remark。

---

## User (2026-11-09 00:31)

我热吻及时L杨浦你哦虐函数构造

---

## Assistant (2026-11-09 00:31)

**老大，我把这句理解为"难点其实在 Lyapunov 函数构造"。我同意，而且可以说得更具体：Nesterov 的标准 Lyapunov 函数里含有显式的 $\boldsymbol{\lambda}^\star(\mathbf{z})$，而中心漂移经过这一项时会被放大 $s$ 倍，中心步长因此被压到 $\epsilon^{3/2}$。构造的核心，是把这一项换成不含 $\boldsymbol{\lambda}^\star$ 的形式。**

**放大的来源。** 对偶块的强凹模数是 $1/s$，所以对偶解对中心的敏感度是 $s$：

$$
\lVert\boldsymbol{\lambda}^\star(\mathbf{z}^{k+1})-\boldsymbol{\lambda}^\star(\mathbf{z}^k)\rVert \lesssim s\,\alpha\,\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert
$$

**距离型 Lyapunov 失败。** 强凸 Nesterov 的标准 Lyapunov 函数含有速度项 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}^\star\rVert^2$，其中 $\mathbf{w}^k$ 是迭代点和速度的组合。按收缩率 $\delta$ 用 Young 不等式拆分，漂移带来的额外项是：

$$
\frac{1}{\delta}\cdot\frac{1}{s}\cdot s^2\alpha^2\lVert\mathbf{x}-\mathbf{z}\rVert^2 = \frac{s\alpha^2}{\delta}\lVert\mathbf{x}-\mathbf{z}\rVert^2
$$

外层每步的下降量只有 $\alpha\lVert\mathbf{x}-\mathbf{z}\rVert^2$。要让下降盖过漂移，必须 $\alpha\lesssim\delta/s$。代入 $\delta=s^{-1/2}$，得到 $\alpha\lesssim s^{-3/2}=\epsilon^{3/2}$，复杂度变成 $\epsilon^{-3.5}$，比不加速还差。之前那版周报里的 "$\alpha\lesssim\epsilon^{3/2}$"，正是这样推出来的。我当时以"未核实"为由把它删了，现在看这个推导是对的。

**值函数间隙不放大。** 对 $\varphi_k^\star(\mathbf{z})=\max_{\boldsymbol{\lambda}}\min_{\mathbf{x}}\mathcal{P}_s$ 用包络定理（Danskin）：

$$
\nabla_{\mathbf{z}}\varphi^\star(\mathbf{z}) = \nabla_{\mathbf{z}}\mathcal{P}_s(\mathbf{x}^\star,\boldsymbol{\lambda}^\star;\mathbf{z})
$$

这个梯度不涉及 $\boldsymbol{\lambda}^\star$ 的导数，所以漂移量只有 $\mathcal{O}(\alpha\lVert\mathbf{x}-\mathbf{z}\rVert)$，没有 $s$ 倍的放大。

**真正要解决的问题**：值函数间隙 $\varphi_k^\star-\varphi_k(\boldsymbol{\lambda}^k)$ 可以直接用，但 Nesterov 还需要一个速度项。这个速度项必须写成不含 $\boldsymbol{\lambda}^\star$ 的形式，例如动量与梯度的交叉项，或者 estimate sequence 的写法。按之前那版周报的转述，Zhang–Xu 用的是交叉项 $\langle\mathbf{v}^k,\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^\star\rangle$。这里仍然出现了 $\boldsymbol{\lambda}^\star$，他们怎样避开放大需要读原文证明。这是 B2 构造前要先弄清楚的一件事。

---

## User (2026-11-09 00:32)

太啰嗦了 我就想知道本质的困难

---

## Assistant (2026-11-09 00:32)

**中心每移动一步，对偶解 $\boldsymbol{\lambda}^\star(\mathbf{z})$ 就漂移 $s$ 倍的距离。Nesterov 动量的 Lyapunov 函数需要一个速度项，而标准速度项含有 $\boldsymbol{\lambda}^\star$，漂移正是通过它进入分析，把中心步长压到 $\epsilon^{3/2}$。** 因此，本质困难是构造一个不依赖 $\boldsymbol{\lambda}^\star$ 的速度项。

---

## User (2026-11-09 00:32)

我明天就要干

---

## Assistant (2026-11-09 00:33)

**老大，我要先修正上一条：我说"对偶解漂移 $s$ 倍、中心步长被压到 $\epsilon^{3/2}$"，这是错的。** Zhang–Xu 的式 (8.2) 给出的敏感度是 $\lVert\mathbf{y}^\star(\mathbf{z}')-\mathbf{y}^\star(\mathbf{z})\rVert\le\sqrt{2L/\mu_y}\,\lVert\mathbf{z}'-\mathbf{z}\rVert$，量级是 $\sqrt{s}$。原因是中心 $\mathbf{z}$ 只通过原始块进入问题。代回 Young 不等式，条件变成 $\alpha\lesssim\delta=s^{-1/2}$，正好与加速所需的中心步长相容，所以中心漂移不构成本质障碍。

**本质困难改为固定中心下的单步收缩不等式**，对应 Zhang–Xu 的 Theorem 9.1。要证明的是：在固定中心下，每步只调用一次 oracle 的 B2（对偶 Nesterov 配原始块 OGDA），在一般非线性耦合下仍能以 $\sqrt{\tau/s}$ 的速率收缩。Zhang–Xu 证这一步时靠的是 EG 的预测点。

**明天按顺序做：**

1. 读 Zhang–Xu 的四处：§8.1 式 (8.2)，看敏感度怎么推；式 (9.11)–(9.18)，看 Lyapunov 函数的组成，包括值间隙、$\lVert\mathbf{x}-\mathbf{x}^\star\rVert^2$、$\lVert\mathbf{y}-\mathbf{y}^\star\rVert^2$、动能项 $\lVert\mathbf{v}\rVert^2$ 和交叉项 $\langle\mathbf{v},\mathbf{y}-\mathbf{y}^\star\rangle$；Theorem 9.1 第 3 步，看交叉项怎么用 polarization 消掉；Lemma 9.4，看中心移动误差怎么界。
2. 对 B2 写固定中心不等式。候选 Lyapunov 函数取值间隙、$\lVert\mathbf{x}-\mathbf{x}^\star\rVert^2$、Nesterov 速度项，再加 OGDA 项 $\lVert\mathbf{g}_x^k-\mathbf{g}_x^{k-1}\rVert^2$，目标收缩率 $\sqrt{\tau/s}$。
3. 在困难实例上跑 B2，检查复杂度的斜率是不是 $-2.5$。

Source: [arXiv:2609.17973 HTML](https://arxiv.org/html/2609.17973)

---

## User (2026-11-09 00:33)

Lyapunov 函数必须证明：这些误差以与加速相同的速率 $\sqrt{\tau/s}$ 被压下去，而不是在动量窗口内累积。 乘子有界性和耦合稳定性都是这个问题的具体表 对啊 还是Lypunov构造很难 难在

---

## Assistant (2026-11-09 00:33)

**难在动能几乎不耗散。** 临界阻尼下，速度项 $\lVert\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}\rVert^2$ 每步只耗散 $\sqrt{\tau/s}$ 的比例。单步格式的耦合误差又和这个速度同阶，系数是 $\Theta(1)$ 的耦合常数 $L_{x\lambda}$。所以 Lyapunov 函数要用只有 $\sqrt{\tau/s}$ 的耗散，去吸收 $\Theta(1)$ 系数的误差。

EG 能做到这一点，是因为它在预测点重新计算梯度，误差降成高阶项。OGDA 只有上一步的梯度差，误差和动能同阶，所以必须找到一个交叉项，让这部分误差在相邻两步之间相消，类似 Zhang–Xu 在 Theorem 9.1 第 3 步用 polarization 消掉交叉项的做法。

以上是推断，要在明天的固定中心不等式里验证。

---

## User (2026-11-09 00:34)

原始块 OGDA 修正 [8]，对偶块 Nesterov 外推 为什么呢要用这两个？

---

## Assistant (2026-11-09 00:34)

**对偶块是病态块，原始块是良态块，所以两块分别处理。**

- **对偶块用 Nesterov 外推**：对偶块的条件数是 $s$，只有加速才能把收缩率从 $1/s$ 提到 $1/\sqrt{s}$。选 Nesterov 而不选 heavy-ball，是因为 Nesterov 在外推点计算梯度，对一般的非二次强凹函数有全局加速保证。外推点本身也起到预测作用。
- **原始块用 OGDA 修正**：原始块的条件数是 $\kappa_x=\Theta(1)$，一步梯度就有常数比例的收缩，不需要加速。但 $\mathbf{x}$ 要跟踪一个带动量、移动更快的 $\boldsymbol{\lambda}$，耦合项会引起旋转，所以需要一个预测型修正。
- **OGDA 而不是 EG**：两者都能提供预测。OGDA 用上一步存下的梯度差 $2\mathbf{g}_x^k-\mathbf{g}_x^{k-1}$ 来预测，不需要额外调用 oracle。EG 要在预测点再算一次梯度，每步代价翻倍。

---

## User (2026-11-09 00:35)

有具体的参考文献吗 或者放到我们的语境里呢

---

## Assistant (2026-11-09 00:35)

**老大，两个选择都有经典来源。放到我们的语境里：对偶 Nesterov 就是加速乘子法，因为 ALM 的乘子更新等价于对偶函数上的梯度上升；原始 OGDA 是 PDHG 外推的梯度版本。下面的文献都是凭记忆给出，引用前需要逐条核对。**

| 选择 | 一般来源 | 在我们语境里的对应 |
| :--- | :--- | :--- |
| 对偶块 Nesterov | Nesterov《Lectures on Convex Optimization》中强凸情形的常数步方案；heavy-ball 在非二次函数上可能失去加速：Lessard–Recht–Packard 2016 SIOPT | ALM 是对偶问题上的近端点法（Rockafellar 1976）；加速近端点法见 Güler 1992；凸情形的加速 ALM 见 He–Yuan 2010 和 Xu 2017 SIOPT。我们的 $\tau$ 步就是在 $\varphi_k$ 上做梯度上升，加 Nesterov 后就是这条线上的非凸、固定 $\rho$ 版本 |
| 原始块 OGDA | Popov 1980；Gidel et al. 2019 ICLR 的 extrapolation from the past；Hsieh et al. 2019 NeurIPS 的 single-call EG；Mokhtari–Ozdaglar–Pattathil 2020 把 OGDA 解释为近似近端点 | PDHG（Chambolle–Pock 2011）的外推 $\bar{\mathbf{x}}=2\mathbf{x}^{k+1}-\mathbf{x}^k$；OGDA 的 $2\mathbf{g}^k-\mathbf{g}^{k-1}$ 是同一种预测的梯度形式 |
| 两块非对称处理 | Chambolle–Pock 2011 的 Algorithm 3：两块都强凸时，每步一次调用，线性速率达到 $\sqrt{\mu_x\mu_y}/L$ 阶；Kovalev–Gasnikov–Richtárik 2022 的 APDG；Thekumparampil–He–Oh 2022 的 Lifted PD | 仿射 $\mathcal{A}$ 时，我们的内层子问题属于双线性耦合的强凸–强凹问题，这些结果可以直接对照。非线性 $\mathcal{A}$ 时，耦合经过 $h$ 的 Moreau 包络，没有现成结果 |

**最接近的先例**是 Chambolle–Pock 2011 的 Algorithm 3：它每步只用一次 prox，靠外推达到加速线性速率。B2 可以看作把它推广到两种情形：耦合是非线性的，并且中心在移动。

---

## User (2026-11-09 00:35)

$$x^{k+1}=x^k-\eta\left(2g_x^k-g_x^{k-1}\right)$$ 这个后面的g是啥东西a

---

## Assistant (2026-11-09 00:35)

$\mathbf{g}_x^k$ 是势函数 $\mathcal{P}_s$ 在点 $(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k)$ 处对 $\mathbf{x}$ 的梯度：

$$
\mathbf{g}_x^k = \nabla f(\mathbf{x}^k) + \nabla\mathcal{A}(\mathbf{x}^k)^{\top}\mathbf{q}^k + \frac{1}{\gamma}\left(\mathbf{x}^k-\mathbf{z}^k\right)
$$

其中 $\mathbf{q}^k=\bar{\boldsymbol{\lambda}}^k+\rho(\mathcal{A}(\mathbf{x}^k)-\mathbf{y}^k)$，$\mathbf{y}^k$ 由这一步的 prox 给出。$\mathbf{g}_x^{k-1}$ 是上一步算出并存下来的同一个量，本步不重新计算。

---

## User (2026-11-09 00:36)

那就直接写\nabka_x这个符号啊

---

## Assistant (2026-11-09 00:36)

好，直接用 $\nabla_{\mathbf{x}}\mathcal{P}_s$ 写：

$$
\mathbf{x}^{k+1}=\mathbf{x}^k-\eta\left(2\nabla_{\mathbf{x}}\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\mathbf{0})-\nabla_{\mathbf{x}}\mathcal{P}_s(\mathbf{x}^{k-1},\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^{k-1},\mathbf{0})\right)
$$

对偶步也用同样的记号：

$$
\boldsymbol{\lambda}^{k+1}=\bar{\boldsymbol{\lambda}}^k+\tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\mathbf{0})
$$

---

## User (2026-11-09 00:36)

\textbf{目前想法（B2）.} 原始块 OGDA 修正 \cite{Popov1980OG}，对偶块 Nesterov 外推：
\begin{gather*}
  \bx^{k+1}=\bx^k-\eta\left(2\bm g_x^k-\bm g_x^{k-1}\right),\\
  \blambda^{k+1}=\blambda^k+\theta_{m,k}\left(\blambda^k-\blambda^{k-1}\right)+\tau\nabla_{\blambda}\mathcal P_s(\bx^{k+1},\bar\blambda^k;\bm z^k,\bm\mu^k).
\end{gather*}
动量系数由阻尼和时间步决定，取临界阻尼 $\gamma_d=2/\sqrt{s}$：
\[
  \theta_m=1-\gamma_d\sqrt{\tau}=1-2\sqrt{\frac{\tau}{s}}
\] 四行算法式子是什么

---

## Assistant (2026-11-09 00:37)

下面按 SPLALM 原来的四行结构写，依次是 $\mathbf{x}$、$\boldsymbol{\lambda}$、$\mathbf{z}$、$\boldsymbol{\mu}$，外推点 $\bar{\boldsymbol{\lambda}}^k$ 单独定义：

```latex
\textbf{目前想法（B2）.} 原始块 OGDA 修正 \cite{Popov1980OG}，对偶块 Nesterov 外推。
记 $\bar\blmbd^k=\blmbd^k+\theta_{m,k}(\blmbd^k-\blmbd^{k-1})$，
\begin{gather*}
  \bx^{k+1}=\bx^k-\eta\Bigl(2\nabla_{\bx}\mathcal P_s(\bx^k,\bar\blmbd^k;\bz^k,\bmu^k)
    -\nabla_{\bx}\mathcal P_s(\bx^{k-1},\bar\blmbd^{k-1};\bz^{k-1},\bmu^{k-1})\Bigr),\\
  \blmbd^{k+1}=\bar\blmbd^k+\tau\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar\blmbd^k;\bz^k,\bmu^k),\\
  \bz^{k+1}=\bz^k+\alpha_k(\bx^{k+1}-\bz^k),\\
  \bmu^{k+1}=\bmu^k+\beta_k(\blmbd^{k+1}-\bmu^k).
\end{gather*}
动量系数取临界阻尼 $\gamma_d=2/\sqrt{s}$：
\[
  \theta_{m,k}=1-\gamma_d\sqrt{\tau}=1-2\sqrt{\frac{\tau}{s_k}} .
\]
```

有三点要对一下：

- 正文里 $\boldsymbol{\lambda}$ 的宏是 `\blmbd`，你片段里写的是 `\blambda`，上面已经统一成 `\blmbd`。
- 你原片段的对偶步用的是 $\mathbf{x}^{k+1}$，即交替更新。这样 $\mathbf{x}$ 步和 $\boldsymbol{\lambda}$ 步要在两个不同的点上算 $\mathbf{q}$，每步需要两次 prox，与现稿相同。如果要做到"每步一次调用"，对偶步要改用 $\mathbf{x}^k$。
- 现稿里 $\gamma$ 已经是近端参数，所以阻尼系数用 $\gamma_d$；$\theta$ 已经表示参数组 $(\rho,s,\gamma,\eta,\tau)$，所以动量系数用 $\theta_{m,k}$。

---

## User (2026-11-09 00:38)

病态和两台就很抽象

---

## Assistant (2026-11-09 00:38)

那就直接写条件数，不用"病态"和"良态"：

- **对偶块**：强凹模数是 $1/s$，光滑常数是 $\Theta(1)$，条件数 $\Theta(s)=\Theta(\epsilon^{-1})$。普通梯度步每步只能收缩 $1/s$，所以要用 Nesterov 外推，把收缩率提到 $1/\sqrt{s}$。
- **原始块**：强凸模数 $1/\gamma-\ell$ 和光滑常数都是 $\Theta(1)$，条件数 $\Theta(1)$。一步梯度就有常数比例的收缩，不需要加速。用 OGDA 修正，只是为了让 $\mathbf{x}$ 跟上带动量移动的 $\boldsymbol{\lambda}$。

---

## User (2026-11-09 00:38)

bar 拉面吧你没有单独给我吗？

---

## Assistant (2026-11-09 00:39)

$\bar{\boldsymbol{\lambda}}^k$ 原来写在正文的"记……"里，现在单独列为第一行：

```latex
\begin{gather*}
  \bar\blmbd^k=\blmbd^k+\theta_{m,k}\left(\blmbd^k-\blmbd^{k-1}\right),\\
  \bx^{k+1}=\bx^k-\eta\Bigl(2\nabla_{\bx}\mathcal P_s(\bx^k,\bar\blmbd^k;\bz^k,\bmu^k)
    -\nabla_{\bx}\mathcal P_s(\bx^{k-1},\bar\blmbd^{k-1};\bz^{k-1},\bmu^{k-1})\Bigr),\\
  \blmbd^{k+1}=\bar\blmbd^k+\tau\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar\blmbd^k;\bz^k,\bmu^k),\\
  \bz^{k+1}=\bz^k+\alpha_k\left(\bx^{k+1}-\bz^k\right),\\
  \bmu^{k+1}=\bmu^k+\beta_k\left(\blmbd^{k+1}-\bmu^k\right).
\end{gather*}
```

---

## User (2026-11-09 00:39)

模数是什么东西 很啰嗦

---

## Assistant (2026-11-09 00:40)

- **对偶块**：条件数是 $\Theta(s)$，普通梯度步每步只收缩 $1/s$，所以用 Nesterov 外推把它提到 $1/\sqrt{s}$。
- **原始块**：条件数是 $\Theta(1)$，不需要加速；加 OGDA 修正是为了让 $\mathbf{x}$ 跟上 $\boldsymbol{\lambda}$。

---

## User (2026-11-09 00:40)

条件数是什么

---

## Assistant (2026-11-09 00:40)

条件数是光滑常数 $L$ 与强凸常数 $\mu$ 之比 $\kappa=L/\mu$，梯度法每步大约收缩 $1/\kappa$。对偶块的 $L=\Theta(1)$、$\mu=1/s$，所以 $\kappa=\Theta(s)$；原始块的 $L$ 和 $\mu$ 都是 $\Theta(1)$，所以 $\kappa=\Theta(1)$。

---

## User (2026-11-09 00:40)

太抽象了

---

## Assistant (2026-11-09 00:40)

用一维的例子说明。

**对偶方向**：对 $-\lambda^2/(2s)$ 做梯度上升，步长取 $\tau$：

$$
\lambda^{k+1}=\left(1-\frac{\tau}{s}\right)\lambda^k
$$

每步只缩小 $\tau/s$ 的比例。$s=\epsilon^{-1}$ 时，要走大约 $s/\tau$ 步，误差才减半。

**原始方向**：曲率是 $\Theta(1)$，每步缩小的比例是 $\eta\cdot\Theta(1)$，常数步之内误差就能减半。

所以慢的只有对偶方向，加速也只需要加在对偶块上。

---

## User (2026-11-09 00:42)

原始是theta1????? 不是有ganmma?

---

## Assistant (2026-11-09 00:42)

**老大，有 $\gamma$，但 $\gamma$ 是常数，与 $\epsilon$ 无关，所以原始方向是 $\Theta(1)$。**

- **原始方向的曲率**：近端项 $\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}\rVert^2$ 贡献 $1/\gamma$，减去 $\mathcal{D}_\rho$ 的弱凸常数 $\ell$，得到 $1/\gamma-\ell$。现稿取 $1/\gamma\gt\ell$，二者都是常数，所以这个曲率是 $\Theta(1)$。
- **原始方向的光滑常数** $L_x$ 由 $L_f$、$L_{\mathcal{A}}$、$\rho$、$1/\gamma$ 决定。$\rho$ 固定，所以 $L_x$ 也是 $\Theta(1)$。

两者之比是不依赖 $\epsilon$ 的常数，所以原始方向每步按常数比例收缩。只有对偶方向的曲率 $1/s=\epsilon$ 随 $\epsilon$ 变小。

---

## User (2026-11-09 00:44)

\textbf{下一步.} Lyapunov 函数在 Zhang--Xu 的“鞍点值间隙 + 动量交叉项”上再加 OGDA 项 $\|\bm g_x^k-\bm g_x^{k-1}\|^2$，证明 $s_k$ 变化时 $\theta_{m,k}$ 仍匹配曲率 $1/s_k$。
 这个难点是在函数的构造吧

---

## Assistant (2026-11-09 00:44)

**是的，难点在 Lyapunov 函数的构造。具体是：OGDA 项的系数是 $\Theta(1)$，而动能每步只耗散 $\sqrt{\tau/s}$，要选出各项的权重，让后者能吸收前者。** 相比之下，$s_k$ 变化带来的误差是次要的：$s_{k+1}/s_k-1=\mathcal{O}(1/k)$，远小于收缩率 $\sqrt{\tau/s_k}\sim k^{-1/5}$。因此这句话可以把重点放到构造上：

```latex
\textbf{下一步.} 在 Zhang--Xu 的“鞍点值间隙 + 动量交叉项”上加入 OGDA 项
$\|\nabla_{\bx}\mathcal P_s^{k}-\nabla_{\bx}\mathcal P_s^{k-1}\|^2$，选取各项权重，
使固定中心下每步收缩 $\sqrt{\tau/s}$；$s_k$ 变化带来的误差为 $\mathcal O(1/k)$，
小于收缩率 $\sqrt{\tau/s_k}$。
```

其中 $\nabla_{\mathbf{x}}\mathcal{P}_s^{k}$ 是 $\nabla_{\mathbf{x}}\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\boldsymbol{\mu}^k)$ 的简写，按你前面的要求不再用 $\mathbf{g}_x$。正文里第一次出现时要给出这个定义。

---

## User (2026-11-09 00:45)

与 Zhang--Xu 的区别在离散方式：其用 对偶补heavy-ball 动量结合外推梯度，每步在两点调用 oracle；我们用 对偶步Nesterov 原始变了OGDA，每步在一点调用一次（$\nabla f$、$\mathcal A(\bx)$、$\nabla\mathcal A(\bx)^{\top}\bm q$ 与一次 $\prox_h$）。

---

## Assistant (2026-11-09 00:45)

```latex
与 Zhang--Xu 的区别在离散方式：其对偶块用 heavy-ball 型动量，结合 extragradient，每步在两点调用 oracle；本文对偶块用 Nesterov 外推、原始块用 OGDA 修正，每步在一点调用一次（$\nabla f$、$\mathcal A(\bx)$、$\nabla\mathcal A(\bx)^{\top}\bq$ 与一次 $\prox_h$）。
```

**需要和算法核对一处。** 你现在采用的四行算法里，对偶步用的是 $\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k;\cdot)$。这是交替更新，$\mathbf{x}$ 步和 $\boldsymbol{\lambda}$ 步在两个不同的点上求 $\mathbf{q}$，所以每步要做两次 $\mathrm{prox}_h$，"每步在一点调用一次"并不成立。要让这句话成立，需要把对偶步里的 $\mathbf{x}^{k+1}$ 改成 $\mathbf{x}^k$。

另外，正文里 $\mathbf{q}$ 的宏是 `\bq`，上面已经把 `\bm q` 改成了 `\bq`。

---

## User (2026-11-09 00:53)

不太确定要不要、能不能做出来，因为不知道考虑加这些额外的技巧是否有足够强的动机或者从问题结果本身出发说明加这些技巧是自然的而然的下一步；分析可能在于Lypunov函数构造
 润色一下这个问题

---

## Assistant (2026-11-09 00:53)

```latex
\textbf{待定问题.} 目前有两点不确定。其一是动机：需要说明，加入对偶动量与 OGDA 修正，是从族内下界 $\Theta(\epsilon^{-3})$ 的结构自然得出的下一步，并非额外叠加的技巧。其二是可行性：主要困难在 Lyapunov 函数的构造。
```

动机这一条，周报里可以直接写上现有的依据：族内下界把瓶颈定位在对偶块每步只能收缩 $1/s$，所以对偶动量是针对这个瓶颈的最小改动。这样它就从"待定"变成"已有初步论证"。

---

## User (2026-11-09 00:54)

不要  我觉得我这个语气挺好的

---

## Assistant (2026-11-09 00:54)

```latex
不太确定要不要做、能不能做出来：一方面，不清楚加入这些额外技巧是否有足够强的动机，能否从问题和已有结果本身说明它是自然而然的下一步；另一方面，分析的难点可能在 Lyapunov 函数的构造。
```
