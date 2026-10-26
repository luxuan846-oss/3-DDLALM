# Booming 白板：SPLALM 草稿（Shrink the Dual Regularization, Keep the Penalty）

> 历史记录，状态标记更新于 2026-10-16。下文保留当时的讨论、判断与任务，可能已被后续决定取代；当前进度与待办仅以 `notes/progress/PROJECT_STATUS.md` 为准，不执行本记录中的旧任务。

草稿目录：`~/Documents/My_Papers/3_DDLALM/overleaf/`
开始：2026-10-15（Booming 测试用例 #1，源自 sparkling 研讨）

## 1. 议题与交付目标
- 议题：这篇作品真正的洞察是什么，下界的边界在哪里，叙事重心是否放对。
- 交付：出口 B 草稿体检（尚未交付；用户 10-15 决定论文先放一放）。
- 10-16 重启：用户按 Taste / Insight / Vision / 顶刊顶会 四问请求判断。草稿模式预算 6 轮，已用 5 轮，候选 0。下一轮（第 6 轮）交出口 B。用户第 3 轮选 (b)：重要性主线为参数区域上的分界（oracle 下界给不出），设计规则作推论。用户决定：标题可以改；PPALA 方向记入 `notes/project/open-direction-ppala.md`，用户自己去读。venue 推定 SIOPT（siamart 模板），待用户确认。

## 2. 硬事实
- `lem:effective-penalty`：$\max_{\lambda}\mathcal P_s=\mathcal D_{\rho+s}$，族内每个成员的有效罚参数为 $\rho+s$。
- `thm:lower-bound`：$\epsilon(\rho+s)\le c_1$ 时，所有常数 $(\alpha,\beta)\in[0,1]^2$ 需要 $\Omega(\epsilon^{-4})$；三区间构造（平台 $\alpha\le\alpha_\epsilon$ / 旋转 $\alpha>\alpha_\epsilon,\beta>0$ / Huber $\beta=0$），见 `sections/LowerBoundProof.tex` 第 27–35 行。
- 平台引理的界为 $\Delta/(16\gamma\alpha\epsilon^2)$（`sections/LowerBoundProof.tex` 第 139–190 行）。
- 旋转实例依赖固定迭代矩阵 $\mathbb T$ 的谱半径与不变子空间（`appendix/LowerBoundRotation.tex` 第 34–35、365 行）。
- `thm:upper-beta0`：$\rho$ 固定、$s=c_s/\epsilon$、$\beta=0$、$\alpha=\Theta(\epsilon)$ 时 $O(\epsilon^{-3})$。
- 比较表中 GDPA 以 $\rho_k=\Theta(1/\epsilon)$ 同样得 $O(\epsilon^{-3})$。
- 附录 `thm:main`：递增 $s_k=\Theta(k^{1/3})$ 的与精度无关方案，$O(\epsilon^{-3})$，需水平有界假设。

## 3. 成果清单
| 成果 | 位置 | 角色 |
|---|---|---|
| 组合罚参数引理 | `lem:effective-penalty` | 刻画用的参数；连接 ALM 罚参数与 minimax 对偶正则 |
| 与中心步长无关的下界 | `thm:lower-bound` | 新结论 |
| β=1 上界 | `thm:upper-beta1` | 改写已有结果，证明下界紧 |
| β=0 上界 | `thm:upper-beta0` | 改写已有结果，增长可由 s 单独承担 |
| 临界尺度推论 | `cor:effective-penalty` | 合并上下界 |
| 递增 $s_k$ 方案 | 附录 `thm:main` | 补充，独立 Lyapunov 分析 |

- `li2026smoothing` 为 Li J., Nagarajan, Pan, Zhang (2026)，非本文作者；其中已有 Smoothed GDA 的 $\Omega(\epsilon^{-4})$ 与 Perturbed Smoothed GDA（$s=\Theta(1/\epsilon)$）的 $O(\epsilon^{-3})$ 及匹配下界。本文两个上界均为其改写（`rem:upper-beta1`、`rem:upper-beta0`）。
- 引言称增大 $\rho$ 会压小原始步长、代价高（`sections/Introduction.tex` 约 180–185 行）；同一比较表中 GDPA 以 $\rho_k=\Theta(1/\epsilon)$ 也得 $O(\epsilon^{-3})$。
- 下界实例全部取 $L_{\mathcal A}=0$（仿射内映射，`sections/LowerBound.tex` 第 9–11 行）。
- PPALA（Kim et al. 2024, arXiv:2406.17107）声称固定参数 $\widetilde O(\epsilon^{-2})$，引言称其可行性论证为渐近，待核对。

- LP-ALM（arXiv:2503.01056）Thm 4.16：$\rho\gtrsim\tau/\epsilon$；$\tau$ 固定得 $O(\epsilon^{-3})$，$\tau=O(\epsilon^\eta)$ 得 $O(\epsilon^{-3-2\eta})$。粗对应 $s=\rho/\tau$，落在对角线。
- NR-LALM（Liu, Deng, Wang, Wen, arXiv:2608.19847）：光滑等式约束、固定罚参数、$O(\epsilon^{-2})$，Gauss–Newton 型原始步，族外。作者含本文合作者 Kangkang Deng。

## 4. 已关闭分支
- 把作品概括为"只有下界"或"乘子更新换不来阶的改进"：用户纠正，作品是罚参数、对偶正则与中心更新作用的完整刻画。
- 时变中心步长推广、单调步长序列推广：用户决定不做（只放宽范围、无新机制）。论文只写清下界适用于常数中心步长，不声称覆盖单调序列。

- 第 2 轮旧判断「族内下界会成为 $\mathcal A_{\det}$ oracle 下界的推论、方向寿命短」错误：oracle 下界至多是该类最优阶（$\le\epsilon^{-3}$，因 $s=\Theta(1/\epsilon)$ 已达 $\epsilon^{-3}$），推不出参数区间 $\epsilon(\rho+s)\le c_1$ 上的 $\Omega(\epsilon^{-4})$。族内参数区间下界与 oracle 下界不可互相替代。

## 5. 领先判断
- 10-16 第 3 轮：重要性应写成参数区间的分界（哪组参数无望），这是 oracle 下界给不出的信息；与 Li et al. 2026 的区别在于对 $(\alpha,\beta)$ 与 $\epsilon(\rho+s)\le c_1$ 的整个区域均匀成立。用户认为 importance 写得不够，判断一致：引言缺少『这条下界改变谁的哪个设计决定』。
- 一句话概括取自结论第二段：这些结果说明了罚参数、对偶正则和中心更新各自的作用；$\rho+s$ 的临界阶为 $1/\epsilon$，增长可由 $s$ 单独承担。
- 用户直觉：固定 $\rho+s$、中心步长随 $k$ 变化仍逃不出 $\epsilon^{-4}$；技术障碍在旋转实例的谱论证。

- 10-16 第 1 轮判断：洞察 $\max_\lambda\mathcal P_s=\mathcal D_{\rho+s}$ 与标题 "Keep the Penalty" 方向相反——前者说 $\rho$ 与 $s$ 对复杂度是同一个量，后者强调二者有别；而阶上看不出区别（GDPA 同阶）。下一单点：Keep the Penalty 换来了什么。

- 10-16 第 2 轮：用户选 (a)，收益为可量化的（原始步长与 $\epsilon$ 无关）。机制行：对偶最优响应处 $\mathbf q=\boldsymbol\mu+(\rho+s)(\mathcal A(\mathbf x)-\mathbf y)$，故 $\lVert\mathcal A(\mathbf x)-\mathbf y\rVert=\lVert\mathbf q-\boldsymbol\mu\rVert/(\rho+s)\le 2L_h/(\rho+s)$。对应：Huber 分支残差 $=q_ha_0/(\rho+q_h+s)=4\epsilon$；上界 `eq:beta0-residual-transfer` 的 $L_h/(10s)$；旋转分支 $b\in[7\epsilon,8\epsilon]$ 与 $bs,b\rho\lesssim c_1$（`appendix/LowerBoundRotation.tex` 125、172–179 行）。该行解释阈值 $\epsilon(\rho+s)$，不解释旋转分支的循环本身。代价位置：增大 $\rho$ 时小步长落在 $\eta$；增大 $s$ 时落在 $\alpha=\Theta(\epsilon)$。

- 第 4 轮单点：分界的上侧只在一条射线上有上界（$\rho$ 固定、$s=c_s/\epsilon$）；$\rho=\Theta(1/\epsilon)$、$s$ 固定一侧在族内无结论。『分界只依赖 $\rho+s$』在上侧尚未证明。

## 6. 证据缺口与下一单点
- 补证：GDPA (Lu 2022) 的原始步长是否 $\Theta(\epsilon)$、常数如何依赖 $G_{\mathcal A}$；SPLALM β=0 的 $C'$ 对 $\ell$ 的依赖。
- 补证：PPALA 固定参数 $\epsilon^{-2}$ 结论的有限步可行性是否成立；若成立，必要性结论只是族内结论，需在引言正面说明 PPALA 逃出族的那一步。
- 叙事对齐（P5）尚未讨论：标题强调 "Keep the Penalty"，而组合罚参数 $\rho+s$ 仍按 $1/\epsilon$ 增长，审稿人可能读成换个名字；引言中"增大 $\rho$ 会压小原始步长"的理由，与 $\beta=0$ 上界要求 $\alpha=\Theta(\epsilon)$ 之间的关系需要说清。
- 用户提到"我还有其他的"，尚未补充是否有成果清单之外的内容（例如覆盖 $\rho=0$ 的统一模板）。
