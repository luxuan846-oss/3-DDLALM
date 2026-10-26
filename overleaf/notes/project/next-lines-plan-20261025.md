# SPLALM 之后的两条线：分工与顺序（2026-10-25）

## 线 0：当前 SIOPT 稿（先收尾）
- 引言与 `rem:family-not-oracle` 补引：Li et al. arXiv:2609.14235（NC-C 的 OS 判据下 $\Theta(\epsilon^{-3})$，对任意确定性一阶算法；OS 与 GS 分离）、Wu–Gu–Yang arXiv:2609.14233、Ramirez–Lacoste-Julien ICLR 2026（dual optimistic ascent = AL-GDA，只有局部结论）、Li–Chen–Liu–Lu–Xu AISTATS 2021。
- 把 GPT 已证的路径紧性（$\alpha=c_\alpha\epsilon,\beta=0,s=c_s/\epsilon$ 时 $\Theta(\epsilon^{-3})$）写成紧跟 `thm:upper-beta0` 的推论；Introduction 表格对应行补下界。
- 核对：`prop:kkt-gs` 下，我们的 $\epsilon$-KKT 落在 GS 一侧还是 OS 一侧。

## 线 1：COLT 2027（约 2027-02 初截稿，按往年推断）/ NeurIPS 2027
核心问题：$\rho$ 固定、$s=c_s/\epsilon$ 时，单步 ALM 中外推对 $\epsilon^{-2.5}$ 是否必要且充分。
1. 数值（1 周）：平台与旋转实例上比较原始 SPLALM、原始 Nesterov 外推、PDHG 型对偶步 $\bar x=2x^{k+1}-x^k$（$\alpha\sim\epsilon^{1/2}$），看迭代数标度。
2. 充分性：PDHG-ALM 的 $O(\epsilon^{-2.5})$ 上界。
3. 必要性：$s=c_s/\epsilon$ 下全族 $\Omega(\epsilon^{-3})$——用户 2026-10-26 告知已证（含 $\alpha>B\epsilon$ 段），待写入正文。
4. NeurIPS 版本另加：随机梯度版本 + Cooper 实验。COLT 版本不需要实验（CFP 核对过）。

## 线 2：与 Boț 合作（期刊）
核心问题：$1/s_k\to0$（消失 Tikhonov 对偶正则）的单循环 ALM 中，$\lambda^k$ 是否强收敛到最小范数乘子；$s_k$ 增长律与 KKT 残差速度的权衡。
1. 二维数值：非凸 $f$、乘子集合非单点的实例，观察 $\lambda^k$ 的极限。
2. 连续时间模型：$x$ 带中心的梯度流 + $\lambda$ 侧 Tikhonov 流（Boț 主导）。
3. 起点：附录递增 $s_k$ 分支；线 1 第 2 步的 Lyapunov 函数复用。
4. 开场材料：retreat 后单独讨论，带第 1 步数值和 "PDHG 卡住的两个控制量就是移动中心和对偶正则" 这一观察。

## 待核清单
- Zhang–Xu arXiv:2609.17973 能否纳入 $h^*$ 的 prox；GS 与 $\epsilon$-KKT 的换算。
- ICLR 2026 的 $\omega$ 与 $\rho+s$ 的精确对应；其非零初值与我们全零初始化的冲突。
- Zhang–Luo 仿射约束单循环 $\epsilon^{-2}$ 的确切条件（目前凭记忆）。
- Boț 单循环 PDHG 具体卡在哪一步（问 Boț）。
