# LRALM 项目 milestone

本文件只追加，不覆盖。格式见 `~/agent-hub/domains/research/research-workflow.md`「milestone 与会话收尾」。当前进度和待办看 `PROJECT_STATUS.md`。

2026-11-22 之前的条目由 Claude 从项目 memory、`PROJECT_STATUS.md`、git 记录和对话记录补录，可能有遗漏；发现遗漏时按日期补进对应位置。

## 2026-10-25

- [决策] SIOPT 论文之后规划两条后续线：一条投 COLT 2027，研究固定 $\rho$、$s=c/\epsilon$ 时对偶外推对 $\epsilon^{-5/2}$ 是否充分且必要；另一条与 Radu Ioan Boț 合作投期刊，研究 Tikhonov 型对偶正则逐渐消失的情形｜来源：`overleaf/notes/project/next-lines-plan-20261025.md`

## 2026-11-05

- [决策] 算法由 SPLALM 改名为 LRALM（Linearized regularized ALM），算法族记为 $\mathcal{C}_\theta$｜来源：retreat 幻灯片｜影响：全文
- [结果] 族内下界：固定 $\rho$、$s=c_s/\epsilon$ 时，所有 $(\alpha,\beta)\in[0,1]^2$ 都需要 $\Omega(\epsilon^{-3})$ 次迭代，族复杂度为 $\Theta(\epsilon^{-3})$；证明来自 GPT，11-15 写入稿件｜影响：第 3 节

## 2026-11-08

- [撤回] 放弃路线 A（$\rho\sim\epsilon^{-1/2}$、不加动量）｜原因：改走对偶外推路线

## 2026-11-09

- [结果] B2′（$\beta=0$ 的 LRALM 加一次对偶 Nesterov 外推）在笔记层面证得固定 $\rho$ 下 $\mathcal{O}(\epsilon^{-5/2})$，GPT 审核通过；它在族外，和族内 $\Omega(\epsilon^{-3})$ 构成分离｜影响：第 4 节 Fast LRALM

## 2026-11-17

- [导师] 每次讨论只谈一个核心章节；下次只谈加速（Fast LRALM，$\mathcal{O}(\epsilon^{-5/2})$），下界、arXiv、署名不在议程中｜来源：`PROJECT_STATUS.md` §4.1｜影响：第 4 节
- [撤回] 「Pan–Zheng–Li 没有 GS 下界」的判断｜原因：本地全文是 v1；v2 的 Theorem 3.2 给出了 GS 的 $\epsilon^{-5/2}$ 下界

## 2026-11-19

- [决策] Fast LRALM 按 $z\to\lambda\to x$ 自上而下叙述，按 $\bar\lambda\to x\to\lambda\to z$ 执行，分析引理与执行顺序一致｜影响：第 4 节

## 2026-11-20

- [决策] 采用 Palatino arXiv 模板并加行号｜来源：commit `5c34731`
- [决策] 第 3 节重组：删去原 3.1 的小节标题，两个定义直接接在节首说明之后；节首只写结果和卖点，机制解释放到 Corollary 3.1 之后新开的小节｜来源：对话「1120 \| tight \| 逻辑 \| sec3-structure」｜影响：第 3 节
- [吃透] $\mathcal{D}_\rho$ 是对偶侧的 Moreau 包络：固定 $\rho$ 让对偶目标关于 $\lambda$ 变光滑，但不提供强凹性，所以族内复杂度停在无加速的阶｜来源：同上｜影响：第 3 节

## 2026-11-21

- [决策] 引用修订分三项：控制重复引用；补够苏文藻老师谱系和 minimax、ALM、约束优化方向学者的工作；概念引用追到原始出处｜来源：对话「1121 \| all \| 文献 \| so-lineage-cites」｜影响：全文

## 2026-11-22

- [导师] 实验只需要一个小的复合优化例子｜影响：第 5 节
- [决策] 实验实例只要求属于问题类 $\mathcal{I}(C,\Delta)$，不按呈现效果筛选；phase retrieval 的 Jacobian 关于 $x$ 无界，不满足要求｜影响：第 5 节
- [决策] 写作流程固定到 agent-hub：文献准备、GPT Pro 推导、写作循环（你理逻辑、Gemini 起草、Claude 和 Codex 核查）、会话收尾 `/paper-wrap`｜来源：本次对话「反重力 CLI 链接问题」

## 2026-11-23

- [决策] Overleaf 只同步论文；实验代码、笔记和状态文件只推送到 GitHub，供 GPT Pro 读取｜来源：本次对话「反重力 CLI 链接问题」｜影响：`/paper-wrap`
- [决策] 项目瘦身：根目录只留 `overleaf/`、`experiments/`、`slides/`、`core/`、`memory/`；和老大反复一起改的文件集中到 `core/`（状态、milestone、定位、三份清单、phrasebook），novelty-check 和旧讲稿进 `memory/archive/`｜来源：本次对话「反重力 CLI 链接问题」｜影响：全项目与 hub 的路径约定
- [决策] 主卖点定为「分离」：一次对偶 Nesterov 外推让固定罚参数的单循环线性化 ALM 达到 $\mathcal{O}(\epsilon^{-5/2})$，而 LRALM 族内任何方法都做不到｜来源：本次对话定位讨论｜影响：摘要、引言、各节节首
- [灵感] 非光滑非线性复合优化 $\min_{\mathbf{x}} f(\mathbf{x})+h(\mathcal{A}(\mathbf{x}))$ 在分离 oracle 下的两大核心科学问题与正则性子类 $\mathcal{C}_\nu$ 最优复杂度（$\Theta(\mathrm{poly}(1/\nu)\,\epsilon^{-2})$ vs $\Theta(\epsilon^{-5/2})$）｜孵化包：`~/agent-hub/domains/research/ideas/20261119-composite-lower-bound/`｜影响：后续新线
- [判断] 仅在带正则性 $\nu \gt 0$ 的子类 $\mathcal{C}_\nu$ 上做问题类上下界才不易被现有结果覆盖，不加 $\nu$ 的一般类 $\mathcal{C}$ 大概率被 Pan–Zheng–Li 或 Wu–Gu–Yang 的 NC-C 下界直接覆盖｜依据：$\mathcal{A}$ 非线性叠加 $J_{\mathcal{A}}$ 退化才会使复杂度高于 $\epsilon^{-2}$，而一般 NC-C 链式实例若关于 $\mathbf{y}$ 线性即可嵌入 $\mathcal{C}$ 且最小奇异值趋零｜验证：阶段 1 调研，核对两篇困难实例是否关于 $\mathbf{y}$ 线性、耦合矩阵最小奇异值如何随 $\epsilon$ 变化，以及 $\mathcal{C}_\nu$ 上是否已有 $\epsilon^{-2}$ 结果（见 `~/agent-hub/domains/research/ideas/20261119-composite-lower-bound/summary.md`）

- [决策] 投稿目标定为 Mathematical Programming（MP）｜来源：2026-11-23 对话｜影响：篇幅组织、正文与附录结构及模板
- [导师] 六点修改意见：篇幅过长考虑压缩；明确 (2.8) 对 ALM 新、对 minimax 非新并前移至 Q1/表 1 前；§3 交代 $(\alpha,\beta)$ 无法改进阶及数值对照；§4 与徐姿组 $\epsilon^{-5/2}$ 做理论和数值对比；补足 minimax 社区视角；摘要围绕 Q1/Q2 组织｜来源：`memory/dialogue/2026-11-23-200716-comments.txt`｜影响：全文

## 2026-11-24

- [决策] 术语约定写入 `core/writing-phrasebook.md`：class 只用于问题、family 只用于算法；已有算法称 method，不用 scheme；方法 applied to $\mathcal{D}_\rho$、每步为 $\mathcal{P}_s$ 上的 GDA step；参数和统一写 effective penalty（取代 combined penalty）；Table 1 分组为 smooth NC-C minimax 与 equality-constrained optimization，表头 Algorithm｜来源：本次对话｜影响：全文
- [决策] Fast LRALM 初值推广到 $\mathcal{S}_0(\mathbf{C})$、$\boldsymbol{\lambda}^{-1}=\boldsymbol{\lambda}^0$，使族下界与加速上界同口径；Definition 3.2 拆出单成员最坏复杂度，Proposition 3.1、3.2 结论改用单成员记号，Theorem 3.2 后补三种情形并说明对偶中心移动不降阶｜来源：本次对话｜影响：§3、§4
- [判断] Zhang–Xu–So v2 算法未变（MC-EGM），新增 GS 匹配下界，中心步长同为 $\Theta(\epsilon^{1/2})$；本文可主张族内上限 $\alpha\le B\epsilon$ 与单参数 $\omega$ 突破，以及 $\mathcal{D}_\rho$ 结构下无投影、每步 1 次 oracle｜依据：arXiv:2609.17973v2 全文与 `memory/notes/codex-review-c1c6-20261124.md`
- [决策] 改正文流程：用户提修改，agent 先给逻辑，同意后交 Gemini CLI 起草，用户确认后写入｜来源：本次对话｜影响：已写入 agent-hub 科研 STATUS 偏好

