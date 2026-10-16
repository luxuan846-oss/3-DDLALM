# 会话交接：2026-10-14（定位调整后的全文状态）

新会话先读本文件，再读 `notes/progress/PROJECT_STATUS.md`。`SESSION_HANDOFF_20261013.md` 记录了 10-13 的细节，与本文件冲突时以本文件为准。全文逻辑的最新版在 Obsidian：`/Users/liluxuan/Documents/Obsidian/261003-文章逻辑.md`。

## 1. 论文定位与主结论

- 标题：**Shrink the Dual Regularization, Keep the Penalty: Tight Complexity of Linearized Augmented Lagrangian Methods**；页眉 "Shrink the Dual Regularization, Keep the Penalty"。
- 定位：对单环线性化 ALM 族 $\mathcal C_\theta$ 的紧性分析，不是提出新算法。新的是下界；两个上界是已有方法（Smoothed GDA、Perturbed Smoothed GDA）在本文设定下的改写。
- 主结论：能达到的最好的复杂度阶由有效罚参数 $\rho+s$ 决定；临界尺度的阶为 $1/\epsilon$；这部分增长可以全部由 $s$ 承担，$\rho$ 固定。
- **关键措辞（必须遵守）**：不能写"中心步长不改变复杂度的阶"。实际证明的是：$\rho+s$ 小时任何常数中心步长都只能做到 $\epsilon^{-4}$；$\rho+s$ 足够大时存在一组中心步长（$\beta=0$、$\alpha=\Theta(\epsilon)$）达到 $\epsilon^{-3}$。"不需要移动中心"只对对偶中心成立，原始中心仍要移动。

## 2. 论文结构（`main.tex`）

| 位置 | 文件 | 内容 | 状态 |
|---|---|---|---|
| §1 | `sections/Introduction.tex` | 问题 (Q)、回答段、比较表、三条贡献、Organization | 已按新定位重写；措辞待 Codex 修正（见第 4 节） |
| §2 | `sections/Preliminaries.tex` | 记号、假设、问题类、驻点判据、oracle | 完成 |
| §3 | `sections/AlgorithmFamily.tex` | SPLALM、算法族、复杂度定义、有效罚参数、特殊情形 | 完成 |
| §4 | `sections/LowerBound.tex`（标题 Main Results） | `thm:upper-beta1`、`rem:upper-beta1`、`thm:lower-bound`、`cor:effective-penalty` | β=0 定理与合并推论待 Codex 写入 |
| §5 | `sections/LowerBoundProof.tex` | GDA 对应命题；平台、旋转、β=0 Huber 三分支；定理证明 | β=0 小节与证明小节已由用户写，**未核对** |
| §6 | `sections/Conclusion.tex` | 总结与开放问题 | 已写；第一段措辞待 Codex 修正 |
| 附录 A | `appendix/LowerBoundRotation.tex` | 旋转实例参数与证明 | 已解析核对（`appendix-a-audit-20261013.md`） |
| 附录 B | `appendix/UpperBoundBetaOne.tex` | `thm:upper-beta1` 的证明（引 Zhang et al. 2020 Thm 3.4），开头含 `prop:curvature-smoothness` | 已写 |
| 附录 C | `sections/UpperBound.tex` | 不依赖精度的递增 $s_k$ 参数选择（`thm:main`，需水平有界假设） | 保留为补充 |
| 附录 D | `appendix/UpperBoundProofs.tex` | 附录 C 的证明 | 保留 |

Codex 写入 β=0 证明后，计划在附录 B 之后插入 `appendix/UpperBoundBetaZero.tex`，其后字母顺延。

## 3. 上界的核对结论

- **β=1**（已写入）：β=1 时 SPLALM 即 Smoothed GDA。Zhang Assumption 3.3 只需 $\inf F>-\infty$；参数条件 (3.3) 与 Li26 Condition 3.2（$r_y=0$）相同；初始间隙 $\le\Delta+L_h^2/(2\rho)+(G_f+G_{\mathcal A}L_h)^2/\mu_\gamma$；$R_k\le\frac{11}{10}S_{k+1}$。待验证：Zhang Lemma B.11 中 $\lambda_1$ 的依赖；arXiv v3 与 NeurIPS 版编号。
- **β=0**（GPT Pro 已核对，结果见 `notes/gpt-proofs/beta0-upper-check-20261013.md`）：路线成立，但需两个限定：$s=c_s/\epsilon$ 且 $c_s$ 足够大（如 $c_s\ge\max\{1,16L_h\}$）；$\alpha=\Theta(\epsilon)$（Li26 Condition 3.2(ii) 要求 $\alpha=\Theta(1/(\ell s))$）。初始间隙基准为扰动目标 $\Phi_s=\mathcal D_{\rho+s}(\cdot,0)$；残差换算 $R_k\le\frac{11}{10}S_{k+1}+\frac{L_h}{10s}$。常数 $C_*$ 由 GPT Pro 按 Li26 §4.2 换算，(4.19)–(4.23) 未逐行复核。

## 4. 交给 Codex、尚未完成的任务

任务文件：`notes/prompts/codex-beta0-theorem-and-wording.md`。四项：
1. §4 写入 `thm:upper-beta0` 及 Remark；
2. 附录写入其证明（`appendix/UpperBoundBetaZero.tex`）；
3. 把 `cor:effective-penalty` 改写为合并推论（临界尺度的阶 $1/\epsilon$）；
4. 修正措辞：摘要、(Q) 回答段、贡献 2/3、比较表 β=0 一行、结论第一段中的 "$s$ of order $1/\epsilon$" 与 "the center stepsizes do not change its order"。

Codex 开始前需读最新的 `Introduction.tex`：用户在 Overleaf 上（提交 `66a9ad1`）注释掉了比较表中 `thm:main` 那一行。

## 5. 其余待办

1. 核对 §5 中 β=0 小节（`LowerBoundProof.tex` 约第 614 行起）与定理证明小节（约第 757 行起）。
2. §4、§5 的两个 `\todo`：GS 版本（可选）；把下界推广到 Smoothed GDA / DS-GDA 的推论（保留或删除待用户定）。
3. 引言 Organization 段目前只介绍 §2–§6，未提附录；附录顺序定下后再定是否补。
4. 小项：bib 重复条目 `zhang2020single`；引言第 76 行 "oraccuracy $eps$"；本地 `sections/RelatedWorkDraft.tex` 未被引用（Overleaf 上已删）。
5. Codex 完成后推送 Overleaf。

## 6. 推送方法与状态

- Overleaf 最新提交：`a23c410`（结论一节、比较表、Organization 一句）。之前：`37017fa`、`c5d06e2`、`9bb9c92`。
- 本地 `master` 跟踪 GitHub，含归档提交 `b69dee2`（literature、oldversion 等 280 多个非论文文件），**不要直接推到 Overleaf**。
- 推送步骤：`git fetch origin` → 以 `origin/master` 建临时 worktree → 只放入有改动的论文文件（若远端有用户新改动，在远端版本上做最小修改，不要用本地文件覆盖）→ 编译通过 → 提交并 `git push origin HEAD:master` → 删除 worktree → 把远端版本同步回 `overleaf/` 工作副本。

## 7. 写作规则

- 论文正文用词取自参考文献，见 `CLAUDE.md`「论文正文的用词来源」与 `notes/project/writing-phrasebook.md`。
- 不引入只用一次的符号；正文不出现 $\ell$、$D_{\mathcal Y}$、$\hat\Delta$，常数只写依赖哪些量。
- Future work 中已按用户要求删去"时变或自适应中心步长"和"结构条件"两条。
