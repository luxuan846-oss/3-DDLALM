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
