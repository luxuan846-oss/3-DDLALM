# DDLALM / SPLALM 项目状态（从 Cowork 项目导出，2026-10-01；第 1–4 节于 2026-10-13 更新）

> **最新进度（2026-10-13）：先读 `notes/progress/SESSION_HANDOFF_20261013.md`**（论文定位调整、全文逻辑、第 4 节与附录进度、待办），再读 `SESSION_HANDOFF_20261012.md`（第 2 节定义）。文献清单见 `notes/project/lower-bound-references.md`，正文用词见 `notes/project/writing-phrasebook.md`。


本文件供 Claude Code 读取。完整研究主线见同目录 `notes/project/ddlalm-research-questions.md`（第八版 + 第 7 节最新结果）。
**当前任务清单以同目录 `notes/project/ddlalm-task-plan.md`（2026-10-01 更新）为准**；10-01 的文献核对与 ρ 一致性推导见 `notes/progress/ddlalm-verification-20261001.md`。两者中出现的 `claude/...` 路径指 Cowork 项目里的同名文件，本地副本在 `notes/`。

## 1. 论文与定位（2026-10-13 调整）
- 稿子：`main.tex`（SIAM 模板）。当前标题（2026-10-13 改）："Shrink the Dual Regularization, Keep the Penalty: Tight Complexity of Linearized Augmented Lagrangian Methods"；页眉 "Shrink the Dual Regularization, Keep the Penalty"。摘要已按新定位重写（其中 β=0 的 O(ε^{-3}) 与"order attained within the family"两句依赖待完成的两个上界）。原标题 "Growing the Dual Regularization, Not the Penalty: A Fixed-Penalty Single-Loop ALM for Nonconvex Composite Optimization"。
- **定位调整**：论文不再以"提出一种固定罚 ALM 算法"为主线，改为对单环 ALM 族 $\mathcal C_\theta$ 的**紧性分析**。主体是下界；两个上界通过退化为已有方法（Smoothed GDA、Perturbed Smoothed GDA）引用并改写。
- 改标题的理由：引言把对偶正则系数写成 1/s，原 "Growing" 方向易读反；原副标题是算法论文写法。标题中的 "Tight" 依赖下界证明与 β=1 上界，二者完成前此词超前于已证内容。
- 算法名：SPLALM；旧笔记中的 DDLALM 指同一方法。
- 时变线已删除（2026-10-13）：第 5 节 `TimeVarying.tex` 已删。`thm:main`（s_k=Θ(k^{1/3})，α_k、β_k 时变，O(ε^{-3})，需水平有界假设）已移到附录 B（accuracy-independent schedule，`sections/UpperBound.tex` 路径未变，\input 移到 \appendix 之后），其证明为附录 C；正文第 6 节已不存在。

## 2. 核心问题
- 单环 ALM 固定罚参数 ρ 时，能否只靠增长 s，把复杂度从 ε^{-4} 降到 ε^{-3}？复杂度由中心步长决定，还是由有效罚参数 ρ+s 决定？
- 导师意见（2026-09-29）：Q1 第一优先；Q2（原始光滑的作用）、Q3（结构条件）放到结论的开放问题。

## 3. 全文逻辑与结果（2026-10-13）
主结论：在常数参数族 $\mathcal C_\theta$ 内，复杂度的阶由有效罚参数 ρ+s 决定，与中心步长无关；临界尺度为 ρ+s=Θ(1/ε)，增长可全部由 s 承担（ρ 固定）。

| 紧性 | 结论 | 依据 | 状态 |
|---|---|---|---|
| 复杂度紧 | ε(ρ+s)≤c_1 时复杂度为 Θ(ε^{-4}) | 下界 `thm:lower-bound`（所有常数 (α,β)）+ β=1 上界 O(ε^{-4}) | 下界证明未完成；β=1 上界未写 |
| 参数紧 | 低于 c_1/ε 为 ε^{-4}；ρ 固定、s=Θ(1/ε) 为 ε^{-3} | 下界 + β=0 上界 O(ε^{-3}) | β=0 上界未写 |
| 中心与参数 | 移动中心代替不了 ρ+s 的增长；增长后也不需要移动中心 | 下界覆盖所有 β；ε^{-3} 在 β=0 达到 | 同上 |

- 下界定理（`thm:lower-bound`）：固定 0<η≤γ、τ>0、Δ>0，存在 c_1(γ,η,τ)、c_2(γ,τ,Δ)，使对所有 ε<c_2、ρ>0、s≥τ 且 ε(ρ+s)≤c_1、(α,β)∈[0,1]²，存在**从全零初值出发**的实例 I∈I(C_0,Δ)，T_ε ≥ Δε^{-4}/(16384γ max{1,4τ,4γτ})。三块构造：小 α 平台实例；大 α、β>0 旋转实例（R_k≥7ε/6）；β=0 Huber 实例（可行性残差 >2ε）。
- β=1 上界：β=1 时 μ^k=λ^k，SPLALM 即作用在 D_ρ 上的 Smoothed GDA，引用 Li et al. 2026 Thm B.1（及 Zhang et al. 2020）。已核对：ℓ=max{L_{D,x}, G_A, 1/ρ}；Li Condition 3.2（r_y=0）逐项对应；初始间隙 ≤ Δ + L_h²/(2ρ) + (G_f+G_A L_h)²/μ_γ；R_k ≤ (11/10)·S_{k+1}；乘子 ‖λ^k‖≤L_h，对偶投影不触发；上界的 α=O(10^{-8}ε²) 落在下界平台区间内，与旋转实例相容。2026-10-13 补核：可直接引用 Zhang–Xiao–Sun–Luo (NeurIPS 2020, arXiv:2010.15768v3) Theorem 3.4。其 Assumption 3.3 只要求 ψ=max_{y∈Y} f 有有限下界（inf F>−∞ 即可，min/inf 问题消除；φ^t≥下界见其附录）；参数条件 (3.3) 与 Li Condition 3.2（r_y=0）逐字相同；驻点定义（其 Def 3.1）与 Li 的 ε-GS 相同，度量点同为 (x^{t+1},y^{t+1})。其光滑常数 L 取联合 Euclid 范数，可取 L=√2ℓ。证明两种情形：(i) 残差 ≤ λ√β，(ii) 残差 ≤ λ̄√((φ^0−inf F)/(Tβ))，取 α=cε²（c≤1/λ²）与 T≥λ̄²Δ̂/(cε⁴) 即得，c 不依赖 Δ。Zhang 的 Prop 4.1、Lemma B.11、B.12 本身未逐行复核（已发表结果，按引用处理）。NeurIPS 版的定理编号待对照。
- β=0 上界（推断，待核对）：β=0 时 SPLALM 即 r_y=1/s 的 Perturbed Smoothed GDA，Li Thm 3.3(i) 在 r_y=Θ(ε/D_Y)（s=Θ(L_h/ε)）下给出 O(ε^{-3})。需逐项核对 Condition 3.2(ii)、初始间隙、残差换算（多一项 τL_h/s=O(ε)）。相容性：上界需 s≳4L_h/ε，下界只覆盖 ρ+s≤c_1/ε（c_1≤1/224），不重叠。
- 数值核对：零初值旋转实例 300 组随机参数 min_k R_k/ε ≥ 2.63（10-12）；附录 A 谱分解、衰减子空间、瞬态界、(i) 中五个不等式在 20000 组参数下成立（10-13，数值证据，非证明）。
- 统一模板（ρ∈[0,ρ̄] 覆盖 ρ=0 的 GDA 型方法）仍只有推导和数值；论文中以 `rem:family-not-oracle` 与第 3 节嵌入小节处理。

## 4. 待办（2026-10-13 更新，按优先级）
1. **下界证明补全**：附录 A 已完成解析核对（2026-10-13，独立审阅一致；参数界引理、(i)、谱分解、瞬态界均成立；补了非退化参数稠密性的论证，见 `notes/progress/appendix-a-audit-20261013.md`）；写 4.3（β=0 Huber 实例）、4.4（合并三分支，c_1、c_2 已在附录 A 给出）。
2. **β=0 常数参数上界 O(ε^{-3})**：ρ 固定、s=Θ(1/ε)，引用 Li Thm 3.3(i) 并做换算。核心问题与"参数紧""中心与参数"都依赖它。
3. **β=1 上界 O(ε^{-4})**：已写入（2026-10-13）。陈述 `thm:upper-beta1` 与 Remark `rem:upper-beta1` 在第 3 节、下界定理之前；证明 `appendix/UpperBoundBetaOne.tex`（附录 B，引用 Zhang et al. 2020 Thm 3.4）。待验证：Zhang Lemma B.11 中 λ_1 的依赖、NeurIPS 版编号。附录顺序现为 A 旋转实例、B β=1 证明、C 不依赖精度的参数选择、D 其证明。
4. **结构调整**：第 3 节改为主结果（β=1 上界、下界、β=0 上界、合并推论，`cor:effective-penalty` 并入）；两个上界的证明放附录（新的一节，字母待定）；`prop:curvature-smoothness`（现位于附录 B）是否移到第 2 节待定；`thm:main` 已移入附录 B。
5. **引言与标题**：按新定位改写贡献列表；贡献 3 的"necessary scale"限定为常数参数；GS 下界一句在严格凸扰动引理证出前删除；标题见第 1 节。
6. 结论一节：开放问题（s=Θ(1/ε) 时 ε^{-3} 是否紧；β>0 能否改进常数；GS 版本下界；原始光滑的作用；结构条件）。
7. 可选：严格凸扰动引理（KKT 下界转 GS 下界）。

已完成：ε_θ 对 s 的一致性（门槛 ε(ρ+s)≤c_1）；零初值；第 4 节开头、4.1、4.2 草稿；附录 A 参数精简；时变线删除。

## 5. 已确认的文献判断
- Liu–Deng–Wang–Wen（arXiv:2608.19847，NR-LALM）：每步解 Jacobian 线性方程组（Gauss–Newton 型），不是梯度步；在 uniform LICQ 下 O(ε^{-2})，属于正则性驱动的结果。
- 与 SPLALM 同类（梯度步、固定参数）的参照：Zhang–Luo（SIOPT 2022，线性约束 + 多面体，Hoffman，O(ε^{-2})，不需要 A 满秩）；Zhang–Pu–Luo（arXiv:2207.06304，凸约束，局部误差界 + CRCQ）。
- 投稿定位：常数步长子类紧性 → SIOPT；全步长规则下的分离 → Mathematical Programming, Series A；固定参数达到 O(ε^{-3}) → MOR。
- 2026-10-01 更正：(1) GS 的 O(ε^{-5/2}) 应引 arXiv:2609.17973（Zhang, Xu），不是 Pan–Zheng–Li 的 Remark 3.3（该说法未在原文中找到，to be verified）；`notes/project/ddlalm-research-questions.md` §1.10 仍是旧说法。(2) Li et al. 2026 的下界只在其各定理的步长条件下成立，不是对所有步长。(3) MIALM（arXiv:1911.09900）是线性 A，收敛分析允许 ρ_k 有界；它不在我们算法类内的理由是双循环与子问题精度趋零。
- 快于 ε^{-4} 的路线（2026-10-13 定）：族内取 s=Θ(1/ε)、β=0，即 Perturbed Smoothed GDA（Li et al. 2026 Thm 3.3(i)），见第 3 节。

## 6. Cowork 项目中的其他记录（未导出，需要时在 claude.ai 项目 "Valerie-DDLALM" 中查看）
- `claude/gptpro-q1-step4-prompt.md`：交给 GPT Pro 的第 4 步任务说明
- `DDLALM_Q1_lower_bound_完整聊天记录_2026-09-29 (1).md`：与 GPT 的完整讨论
- `claude/ddlalm-fenchel-view-and-literature.md`、`claude/ddlalm-vs-rada.md`、`claude/ddlalm-dsgda-analysis.md`：文献与结构对照
- `claude/ddlalm-session-20260927*.md`：早期讨论记录（部分结论已被后续版本取代）
- 已导出到 `notes/`：`notes/project/ddlalm-task-plan.md`（2026-10-01 更新版）、`notes/progress/ddlalm-verification-20261001.md`

文献库：`notes/project/literature.md`（按 Q1 下界、固定罚与正则性、minimax、ALM、经典基础分类；含 bib key、核对状态、待加入与重复条目）。
