# 讨论记录：第 4 节下界证明的思路（2026-10-13）

> 历史记录，状态标记更新于 2026-10-16。下文保留当时的讨论、判断与任务，可能已被后续决定取代；当前进度与待办仅以 `notes/progress/PROJECT_STATUS.md` 为准，不执行本记录中的旧任务。

## 1. 已定的决定

| # | 问题 | 决定 | 理由 |
|---|---|---|---|
| 1 | 量词顺序 | 对任意 $(\alpha,\beta)$，存在实例 $I$；对手先看到步长再出题 | 与 Mahdavinia Theorem 5.1 相同；对应第 2 节的 $\inf_{(\alpha,\beta)}\sup_I$ |
| 2 | 为什么按 $\alpha$ 分支 | $\alpha$ 是原始中心 $z$ 每步的移动比例。$x$ 被近端项拴在 $z$ 附近（距离 $\le\gamma g$），$z$ 每步最多前进 $\alpha\gamma g$，所以 $x^k\le\gamma g(1+\alpha k)$。斜率为 $g=2\epsilon$、高度为 $\Delta$ 的慢坡需要 $\Delta/(\gamma\alpha\epsilon^2)$ 步走完 | 阈值 $\alpha_\epsilon\sim\epsilon^2$ 由慢坡实例反推：要让慢坡给出 $\epsilon^{-4}$，$\alpha$ 必须小到这个量级 |
| 2' | 证明的第一步 | 先写慢坡实例（分支 A），由它定出 $\alpha_\epsilon=1024\varpi\epsilon^2$ | 一维、乘子恒为零，是整份证明最初等的部分；大 $\alpha$ 分支只负责惩罚越过阈值的 $\alpha$ |
| 3 | $\alpha$ 大时出什么题 | 构造模为 1 的特征值 $\zeta$，轨迹有界旋转，$R_k>\epsilon$ 对所有 $k$，$T_\epsilon=+\infty$ | Mahdavinia 用发散；我们不能发散，因为实例只在有界区域内是二次的，且问题类要求梯度有界。模 $<1$ 最终合格，模 $>1$ 跑出二次区域，只有模 $=1$ 可用 |
| 3' | 为什么只有 $\alpha$ 大时能转（推断） | $\alpha$ 大时 $z$ 紧跟 $x$，近端项几乎不产生阻尼，少量负曲率 $\kappa$ 即可精确抵消剩余阻尼；对应引理 1♯ 的条件 $\nu/\alpha^2\le1/64$ | 待写入正文时再核对表述 |
| 4 | 零初值怎样处理 | 零初值写成 $\mathbf v+\mathbf r$：$\mathbf v$ 是旋转特征向量，$\mathbf r$ 取自快根子空间，使 $x=z$、$\lambda=\mu$（同步条件）；再用 $x_c,\lambda_c$ 把同步点平移到原点；引理 3♯ 控制瞬态 $\mathbb T^k\mathbf r$ | 单纯平移不够：$\mathbf v$ 本身不满足同步（$Z=\frac{\alpha\zeta}{u+\alpha}X\ne X$）。保持 `rem:lb-initialization` 的表述：初值固定为零，只有实例依赖参数。这是分支 B 相对文献的技术增量 |

## 2. 为什么要用特征向量

线性系统 $\mathbf w^k=\mathbb T^k\mathbf w^0$。初值是特征向量时，矩阵幂变成数乘 $\mathbf w^k=\lambda^k\mathbf w^0$，整条轨迹由一个数决定，第 0 步算出的证书可以直接推到每一步。

- Mahdavinia：$\lambda=s_1<1$ 贴近 1，$x^T=s_1^Tx^0$ 衰减慢，读出步数下界。
- 我们：$|\zeta|=1$，$|\mathbf w^k|$ 恒定，$R_k$ 始终 $>\epsilon$。
- 我们多一步：零初值不在特征向量上，所以写成 $\mathbf v+\mathbf r$ 并证明 $\mathbf r$ 足够小。

## 3. 文献阅读结论

| 文献 | 可借 | 不适用 |
|---|---|---|
| Mahdavinia et al. NeurIPS 2022 §5、附录 C.1（已读原文） | 二次实例 $f=-\frac{\ell}{2}x^2+bxy-\frac{\mu}{2}y^2$；按步长分情况：步长大时由迹 $\ge0$ 得谱半径 $\ge1$（Prop. C.3），步长小时慢特征值 $s_1$ 贴近 1（Prop. C.2）；定理量词"对任意学习率" | 初值取在特征向量上 |
| Li et al. 2602.14185 §5、附录 A.4–A.5（已读原文） | 2–3 维线性递推，闭式特征值（$3\times3$ 情形用 Mathematica）；区域不变性靠"特征向量初值 + $0<1+\lambda<1$ 单调缩小"；§5.2.2 的比较序列（冻结对偶） | 初值依赖 $\epsilon$，$\Delta_{\Psi_1}=O(\epsilon^2/\ell)$；参数随 $\epsilon$ 选定，只证明给定参数下的紧性，未对步长取下确界 |
| Pan et al. 2609.14235 §4、§6（已读原文） | 小节排列：条件 (C1)–(C4) → 构造 → 逐条验证 → 缩放与定理 | saddle zero-chain + resisting oracle，机制不同 |
| Li–Pan 2608.03246 §3–§5（网页摘要，未读原文） | 同样的"条件 → 构造 → 验证"排列；固定 $\Delta$、类常数与 $\epsilon$ 无关的陈述格式 | zero-chain 构造，非平台实例 |

结论：分支 B 的技术参照是 Mahdavinia 与 Li §5.1；定理量词照 Mahdavinia；小节排列参照 Pan、Li–Pan。零初值谱分解（引理 2）与瞬态估计（引理 3♯）无文献范本。

## 4. 第 4 节结构方案

| 小节 | 内容 | 材料来源 |
|---|---|---|
| 开头段 | 证明思路：Small $\alpha$ / Large $\alpha$ 两段（**已写入并推送**，Overleaf 提交 abc113d） | 本次讨论 |
| 4.2 平台实例 | $0\le\alpha\le\alpha_\epsilon$，$\beta$ 任意；$A\equiv0$；$T_\epsilon\ge\Delta/(32\gamma\alpha\epsilon^2)$ | Part I §2 |
| 4.3 旋转实例 | 4.3.1 实例与参数（引理 1♯）；4.3.2 零初值谱分解（引理 2）；4.3.3 瞬态估计（引理 3♯）；4.3.4 验证（类成员、间隙、$\mathcal R_\rho$、$R_k\ge\frac76\epsilon$） | Part II §2–§4、Part III §2–§4 |
| 4.4 $\beta=0$ 实例 | Huber 外函数 $h$，$q_h=2s+1$；对偶轨迹闭式；可行性残差 $>2\epsilon$ | 引理 4、Part III §5.2 |
| 4.5 定理与推论的证明 | 合并三分支；常数 $c_1,c_2$ 与门槛用途表 | Part III §1、§5.3、§6 |

设计要点：
- 分支 A、B 直接调用 `prop:embedding`（轨迹在 $\mathcal R_\rho$ 内时 SPLALM 等于线性递推 `eq:gda-recursion`）。分支 A 中 $A\equiv0$，条件自动成立。
- 分支 C 中 $\partial h(\mathbf 0)=\{\mathbf 0\}$、$\mathbf y^{k+1}\ne\mathbf 0$，不在 $\mathcal R_\rho$ 内，需直接写出 $\mathbf y^{k+1}$ 的闭式。
- 入手顺序：4.2 → 4.4 → 4.3 → 4.5。

## 5. 待定事项

- 常数 $c_1,c_2$ 与门槛表从 4.1 移到 4.5（建议同意，用户尚未确认）。
- 定理 `thm:lower-bound` 中的 $\max\{1,4\tau,4\gamma\tau\}$ 是否改写为 $\varpi$，写 4.5 时决定。
- Li–Pan 2608.03246 只读了网页摘要，引用其格式前需对照原文。
- 下一步：写 4.2 平台实例。
