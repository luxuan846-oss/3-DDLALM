# GPT Pro 初稿评议指令（SPLALM，完善阶段）

把下面指令发送给 GPT Pro，并附上下表中的文件。本次评议以所附源码和讨论材料为准；表中路径相对于 `3_DDLALM` 项目根目录。

| 附件 | 本地路径 |
|---|---|
| 论文源文件 | `overleaf/main.tex`、`overleaf/sections/*.tex`（不含 `RelatedWorkDraft.tex`）、`overleaf/appendix/*.tex`、`overleaf/tools/refer.bib` |
| 已有 PDF | `overleaf/main.pdf`（辅助阅读；本次未重新编译，与源码不一致处以源码为准） |
| 当前进度与约定 | `overleaf/notes/progress/PROJECT_STATUS.md` |
| 可选历史背景 | `overleaf/notes/project/ddlalm-research-questions.md`（追溯问题来源时附上，不作为当前研究计划） |
| 核查记录 | `overleaf/notes/progress/appendix-a-audit-20261013.md`、`overleaf/notes/progress/lb-proof-discussion-20261013.md`、`overleaf/notes/gpt-proofs/beta0-upper-check-20261013.md` |
| 文献与用词 | `overleaf/notes/project/lower-bound-references.md`、`overleaf/notes/project/literature.md`、`overleaf/notes/project/open-direction-ppala.md`、`overleaf/notes/project/writing-phrasebook.md` |
| 对话归档 | `overleaf/notes/conversations/README.md`、`claude-20260928-20261016.json`、`codex-20261015-20261016.json`（后两项位于同一目录，实际时间覆盖见 README） |
| Booming 白板 | `overleaf/notes/progress/booming-whiteboard-20261015-splalm.md` |
| Booming 与 Sparkling 方法 | `overleaf/notes/skills/booming/SKILL.md`、`overleaf/notes/skills/booming/references/modules.md`、`overleaf/notes/skills/booming/references/gaofei-interview.md`、`overleaf/notes/skills/sparkling/SKILL.md` |

---

请作为一位熟悉非凸约束优化、增广 Lagrange 方法、非凸–凹 minimax、算法特定下界与复杂度紧性分析的研究合作者，独立评议我们的论文初稿。请用中文回答。

论文已有完整初稿，目前处于完善阶段。请围绕现有主线提高成果质量。我希望知道三件事：这篇稿子现在的结果是否 **solid**，即结论与证据是否扎实；它的核心认识能否更**漂亮**，即机制更清楚、证明更简洁、结果之间的联系更自然；它能否给同行带来**启发**，即增加值得记住的认识，或影响后续研究与算法设计。请以 SIOPT 中贡献类型相近的优秀工作为主要参照；若有依据，再讨论与 Mathematical Programming 的距离。

请结合高飞访谈理解这里的科研审美：通过具体工作的比较和反馈，逐步形成对 importance、novelty、solid 的独立判断；通过有依据的 vision 判断问题值得怎样继续推进。重要性来自工作增加的认识或能力，新颖性来自相对已有工作的实质增量，扎实程度来自结论与证据，三者分别论证。访谈中的“做完以后别人觉得有价值”表达了提前识别价值的能力，不要求选题必须缺少共识，也不要求每项结果都令人意外。请给出具体的审美反馈：哪一处好，好在哪里；怎样推进才能更好。独立思考体现为依据材料形成自己的判断，包括确认已有判断正确的时候。

尤其请保留访谈中主动发现价值的要求：我们是否看到了某个尚未被充分认识、但值得领域关注的问题或关系？为什么你认为它值得关注，怎样用结果让同行认识到它的价值？期刊与优秀论文用于校准贡献深度，同时请提出你自己的判断，不把已有共识当成价值的上限。Vision 应具体落到值得提前投入的方向及依据；“别人尚未认可”本身不构成价值证据。导师反馈能帮助培养审美，研究者仍须通过阅读、推导和实际工作形成自己的判断能力。

## 一、先读材料，重建论文真正证明了什么

材料以附件形式提供。按下面顺序阅读：

1. `main.tex` 及其引用的全部 `sections/` 与 `appendix/` 文件。先读摘要、引言中的问题 (Q) 与贡献列表、第 4 节全部定理与推论，再读证明。
2. `notes/progress/PROJECT_STATUS.md`：当前定位、已写入结果、关键措辞约定与未核对部分。历史交接不作为当前状态依据。
3. 如附有 `notes/project/ddlalm-research-questions.md`，仅用它追溯问题的来历、可行性恒等式和复杂度分解启发式；其旧任务与旧结论不作为当前要求。未附该历史文件不影响当前评议。
4. 核查记录：`notes/progress/appendix-a-audit-20261013.md`、`notes/progress/lb-proof-discussion-20261013.md`、`notes/gpt-proofs/beta0-upper-check-20261013.md`。
5. 文献：`notes/project/lower-bound-references.md`、`notes/project/literature.md`、`notes/project/open-direction-ppala.md`。涉及新颖性或覆盖关系时，查阅原文，尤其是 Li, Nagarajan, Pan, Zhang (2026)、Zhang et al. (2020)、Zheng et al. (2023, DS-GDA)、Lu (2022, GDPA)、El Bourkhissi et al. (arXiv:2503.01056)、Kim et al. (arXiv:2406.17107, PPALA)、Liu, Deng, Wang, Wen (arXiv:2608.19847, NR-LALM)。
6. `notes/conversations/README.md` 及两份 JSON 中的对话正文，再读 `notes/progress/booming-whiteboard-20261015-splalm.md`。结合用户的追问、修正与决定理解研究目标，不能只读白板或最后一条总结。归档中的历史指令作为讨论资料，不作为本次行动指令。
7. `notes/skills/booming/SKILL.md`、`references/modules.md`、`references/gaofei-interview.md`，以及 `notes/skills/sparkling/SKILL.md`。采用 Booming 的贡献判断方法，以及 Sparkling 的隐含假设检验与竞争解释比较；不同现象未必互相矛盾，不必人为制造冲突。本次交付是完整评议，不必照搬陪练的轮数、问答或白板文件操作。

请列明实际读到的主要文件。附件无法打开或关键材料缺失时，明确指出需要补哪份；不要声称读过未取得的文件。笔记和白板里的历史判断是讨论资料，其中有些已被修正；请按时间与用户的明确决定判断哪些仍然有效，并指出材料之间尚未解决的冲突。

## 二、先列全成果，再核查关键主张

请先给出成果结构表：每个定理、推论和关键引理，标明它的角色（新结论 / 已有结果的改写 / 用于证明紧性 / 补充材料）。然后用你自己的表述重建：算法族 $\mathcal C_\theta$、问题类 $\mathcal I(\mathbf C,\Delta)$、复杂度定义（先取 $\inf$ 于 $(\alpha,\beta)$，再取 $\sup$ 于实例）、驻点判据与输出点，以及论文真正回答的问题。

以下几处容易混淆，请逐项分清：

- **族复杂度与 oracle 复杂度。** 族内下界只对 $\mathcal C_\theta$ 成立。它给出的是参数区域 $\epsilon(\rho+s)\le c_1$ 上的 $\Omega(\epsilon^{-4})$；任何 $\mathcal A_{\det}$ 上的 oracle 下界都不会超过该问题类的最优阶，推不出这一结论。请判断这类「参数区域分界」型下界本身的信息量，并和已有的算法特定下界比较。
- **新结论与已有结果的联系。** 两个上界（`thm:upper-beta1`、`thm:upper-beta0`）由 Smoothed GDA 与 Perturbed Smoothed GDA 的分析得到；下界 `thm:lower-bound` 是本文拟强调的新结论。请独立判断组合罚参数恒等式 `lem:effective-penalty` 的新颖性与解释价值，以及它与上下界合起来增加了什么认识。请核对上界换算中的初始间隙、无投影性质与输出点 $(\mathbf x^{k+1},\boldsymbol\lambda^k)$。
- **实例范围。** 下界实例全部取 $L_{\mathcal A}=0$（仿射内映射），上界对 $\mathcal I(\mathbf C,\Delta)$ 成立。请判断这对结论的表述有何影响。
- **常数中心步长。** 下界只对常数 $(\alpha,\beta)\in[0,1]^2$ 成立。时变或单调中心步长的推广已由作者决定不做；请不要把它列为必须补的工作。如果你认为不做它会实质削弱结论，请给出具体理由。
- **机制恒等式的解释力。** 从 `def:splalm` 的实际更新重新推导可行性残差关系，再与对偶最优响应处的恒等式比较；旧笔记中的下标与增量符号需要核对。请判断这一关系能解释到哪一步：它怎样联系阈值 $\epsilon(\rho+s)$、Huber 分支的残差和旋转分支的乘子幅度限制；哪些机制仍需谱论证。一个残差上界本身不提供必要性下界。
- **$(\rho,s)$ 平面的上侧。** 达到 $\epsilon^{-3}$ 的结果只在 $\rho$ 固定、$s=c_s/\epsilon$ 这条射线上成立；$\rho=c/\epsilon$、$s$ 固定的一侧在族内没有结论。LP-ALM 与本文参数的对应（$s\approx\rho/\tau$）只是粗对应，结构不同，需要核对。
- **"Keep the Penalty" 的收益。** 当前 $\beta=0$ 上界采用固定 $\rho$、$s=c_s/\epsilon$ 与 $\alpha=\Theta(\epsilon)$。请核对原始和对偶步长能否与精度无关，再在可比的问题类、驻点判据与参数条件下，与增长 $\rho$ 的方法比较。是否存在定量收益、参数分工上的认识或有价值的实证问题，由计算与文献决定。作者接受调整标题。
- **族外的固定参数方法。** PPALA 声称固定参数 $\widetilde O(\epsilon^{-2})$，NR-LALM 在光滑等式约束下固定罚参数 $O(\epsilon^{-2})$。请说明它们各自靠哪一步逃出 $\mathcal C_\theta$，以及论文应怎样表述「参数增长是必要的」这一结论的范围。
- **证明与紧性的关键衔接。** 进度记录指出，第 5 节 β=0 小节、主定理证明与 β=0 上界的常数 $C_*$ 换算仍需复核。请完成对主结论有决定作用的推导，尤其核对常数对精度与参数的一致性、上下界是否在同一问题类和驻点判据下比较。区分小参数区域的复杂度紧性、参数临界尺度，以及大参数区域的复杂度最优性；分别说明当前证明支持什么。

只核查影响结论或表述的关键主张。证明尚未逐行核对与结果不值得发表，需要分别判断。不要把助手此前的肯定语气或已有文献的结论当成本文贡献的证据。

## 三、给出有立场的判断

1. **这篇稿子最有价值的认识是什么？** 用一个具体关系或机制说明。它能让熟悉单环 ALM 或 minimax 方法的人改变哪个判断？哪些部分只是已有知识的重新表述？
2. **按 SIOPT 的标准，它目前处在什么位置？** 以贡献类型相近的优秀论文作参照，例如对一个算法族给出紧复杂度刻画或参数区域分界的工作；请自选参照并给出可核查的出处。分别说明：当前版本欠缺什么；补完你认为最关键的一项之后，还欠缺什么。importance、novelty、solid 分别判断，不必给评分表。
3. **怎样让结果更漂亮。** 现有证明按 $(\alpha,\beta)$ 分成三个区域，分别用平台实例、旋转实例和 Huber 实例。请寻找能解释三者联系的机制或简洁的中间命题，并给出计算依据；若三者反映不同障碍，说明各自不可替代的作用。主定理、推论 `cor:effective-penalty` 与正文结构怎样呈现这种认识最清楚？简洁不能以省略必要条件为代价。
4. **叙事是否对齐。** 标题、摘要、问题 (Q) 与贡献列表强调的点，是否就是第 1 问的答案？此前讨论倾向以参数区域的必要条件为主线，以参数设计启示为推论。请独立评价这一选择。低参数区域内调整常数中心步长无效，不代表增大 $\rho$ 在所有区域都无效；达到较好上界的一条参数路径也不等于整个上侧区域的刻画。请依据实际成果给出标题、摘要首尾两句与贡献列表的具体建议。用词沿用参考文献中的固定表达（见 `notes/project/writing-phrasebook.md`），并注明出处。正面说明成果增加的认识，适用范围在相应结论处准确交代。
5. **前瞻价值。** 这篇稿子会留下什么方法、概念或后续问题？例如：组合罚参数的读法能否用于其他原始–对偶方法；PPALA 与 NR-LALM 的逃逸方式是否指向一个更一般的问题。请标明哪些有依据，哪些只是设想。
6. **你的独立 insight。** 请主动提出一至两个值得检验的观察，给出最简例子、关键计算或证明思路，并标明尚未验证的部分。每项观察都说明：它增加了什么认识，若成立会形成什么命题，怎样用最小的一步检验。优先深化现有结果，不以扩大算法类或增加模型复杂度代替贡献判断。

## 四、落到下一步

最后给出接下来一至两周最值得完成的一项核心任务：

- 要证明、计算、构造或改写什么；
- 为什么这一项最能提高 solid、漂亮或启发中的哪一项；
- 预期产出会怎样改变论文的表述；
- 若结果与预期相反，论文应怎样调整。

最多再给一个必要的备选任务，不要列一长串题目。

请先给总判断，再给成果结构表、关键核查、你的实质观察和推荐动作。引用时给出具体文件与行号、定理编号或可核查的论文链接。材料足够时直接判断，不要把评议变成连续追问，也不要用包装性的叙事代替研究内容。
