# 交给 Codex：写入 β=0 上界、合并推论、修正措辞

工作目录：`/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf`。先读 `CLAUDE.md`（尤其「论文正文的用词来源」）、`notes/progress/PROJECT_STATUS.md`、`notes/project/writing-phrasebook.md`。

只做下面四项。不要改动其他内容，不要推送 Overleaf，不要删除文件。

## 材料

- β=0 路线的核对结果与证明原稿：`notes/gpt-proofs/beta0-upper-check-20261013.md`（编号按 Li26 = arXiv:2602.14185v2）。
- 已写好的同类范本：§4 的 `thm:upper-beta1`、Remark `rem:upper-beta1`（`sections/LowerBound.tex`），附录证明 `appendix/UpperBoundBetaOne.tex`。新内容的结构、句式、记号与它们保持一致。
- 写作规则：术语与固定句式取自参考文献，表达库在 `writing-phrasebook.md`；不引入只用一次的符号；正文不出现 \(\ell\)、\(D_{\mathcal Y}\)、\(\hat\Delta\)，常数只写"依赖哪些量"。

## 任务 1：§4 写入 β=0 定理

位置：`sections/LowerBound.tex`，放在 `thm:lower-bound` 及其后的 GS `\todo` 之后、`cor:effective-penalty` 之前。label 用 `thm:upper-beta0`（先全稿检索，确认无冲突）。

陈述要点（按核对结果，不得放宽）：
- 参数：\(\rho,\gamma,\eta,\tau\) 固定并满足附录中的步长条件（正文只引用该条件的公式标签，不写出 \(\ell\)）；\(\beta=0\)；\(s=c_s/\epsilon\)，其中 \(c_s\) 足够大（附录给出 \(c_s=\max\{1,16L_h\}\)）；\(\alpha\) 取 \(\Theta(\epsilon)\)，在一次运行内为常数（附录中 \(\alpha=\kappa/(\ell s)\)）。
- 结论：存在只依赖 \(\rho,\gamma,\eta,\tau,\mathbf C,\Delta\) 的 \(C'>0\)，使对充分小的 \(\epsilon\)，\(T^{\mathrm{KKT}}_\epsilon(\theta,\alpha,0;I)\le C'\epsilon^{-3}\) 对所有 \(I\in\mathcal I(\mathbf C,\Delta)\) 成立。注意这里 \(\theta\) 中的 \(s\) 依赖 \(\epsilon\)，陈述中写清楚。
- 定理后加一个短 Remark（格式同 `rem:upper-beta1`）：(i) β=0 时 SPLALM 退化为作用在 \(\mathcal D_\rho\) 上的 Perturbed Smoothed GDA，类似结果见 \cite[Theorem~3.3]{li2026smoothing}；本文的改写在于初始间隙用类常数控制、乘子不需投影、残差在 \((\bx^{k+1},\blmbd^k)\) 处度量（多一项 \(L_h/(10s)\)）。(ii) \(c_s\) 必须足够大：取 \(s=c/\epsilon\) 且 \(c<c_1\) 时参数落入 `thm:lower-bound` 的范围。(iii) 这里 \(\alpha=\Theta(\epsilon)\)；与精度无关的 \(\alpha\) 能否达到 \(\epsilon^{-3}\)，本文不讨论。

## 任务 2：附录写入证明

新文件 `appendix/UpperBoundBetaZero.tex`，标题 "Proof of Theorem~\ref{thm:upper-beta0}"，label `app:upper-beta0`；在 `main.tex` 中紧接 `appendix/UpperBoundBetaOne` 之后 `\input`。

按核对文件的第 1–8 项和"修订后证明"写成 Step 1–6（结构仿照 `UpperBoundBetaOne.tex`）：算法对应与乘子有界；假设验证与 \(\max_{\lambda\in\mathcal Y}\mathcal D_\rho=F\)；步长条件（写出 Li26 Condition 3.2(ii) 的完整翻译，给一个公式标签供正文引用，并给出核对文件中的数值例子说明条件可同时满足）；初始间隙（扰动基准 \(\Phi_s=\mathcal D_{\rho+s}(\cdot,\zero)\)，用 `eq:effective-penalty`）；复杂度（引用 Li26 Thm 3.3(i) 与 §4.2 (4.19)–(4.23)）；度量换算 \(R_k\le\frac{11}{10}S_{k+1}+\frac{L_h}{10s}\)。注明编号采用 arXiv v2。

核对文件第 7 项中常数 \(C_*\) 的存在与依赖来自对 Li26 §4.2 的换算，未逐行复核。写入时保留这一事实：在文件末尾用 LaTeX 注释标出，不要在正文中声称已复核。

## 任务 3：合并推论

把 `cor:effective-penalty` 改写为合并推论（label 保留 `cor:effective-penalty`，标题改为 "Scale of the effective penalty"）：
- (a) 若 \(\rho=\rho(\epsilon)\)、\(s=s(\epsilon)\ge\tau\) 满足 \(\rho+s\le c_1/\epsilon\)，则复杂度为 \(\Omega(\epsilon^{-4})\)（由 `thm:lower-bound`）；
- (b) \(\rho\) 固定、\(s=c_s/\epsilon\) 时，复杂度为 \(O(\epsilon^{-3})\)（由 `thm:upper-beta0`）；
- 结论句：\(O(\epsilon^{-3})\) 需要 \(\rho+s>c_1/\epsilon\)，并且在 \(\rho\) 固定时由 \(s=c_s/\epsilon\) 达到。说明 \(c_1\) 与 \(c_s\) 不同，因此结论是关于阶 \(1/\epsilon\) 的。

## 任务 4：修正措辞

逐处修改，句子其余部分不动。

1. **"\(s\) of order \(1/\epsilon\)" 改为 "\(s=c_s/\epsilon\) with a sufficiently large constant \(c_s\)"**，并在合适处补上 \(\alpha\) 的取法（\(\alpha\) of order \(\epsilon\)）：
   - `main.tex` 摘要："If $\rho$ is fixed and $s$ is of order $1/\epsilon$, a member of the family …"
   - `sections/Introduction.tex` (Q) 回答段："with $\rho$ fixed, $s$ of order $1/\epsilon$, and the dual center fixed at zero, …"，并把其后的 `\cite[Theorem~3.3]{li2026smoothing}` 换成 `Theorem~\ref{thm:upper-beta0}`，删去紧随的 TODO 注释。
   - 引言贡献 2："with $\rho$ fixed, $s=\Theta(\epsilon^{-1})$, and $\beta=0$"；"The result follows from~\cite[Theorem~3.3]{li2026smoothing} …" 改为指向 `thm:upper-beta0` 并说明是对该定理的改写；删去 TODO 注释。
   - `sections/Conclusion.tex` 第一段："With \(\rho\) fixed and \(s\) of order \(1/\epsilon\), …"；删去其后的 TODO 注释。
   - 引言比较表 β=0 一行：行名的引用换成 `Theorem~\ref{thm:upper-beta0}`；\(s\) 一栏写 \(c_s\epsilon^{-1}\)；删去该行上方的 TODO 注释。
2. **"中心步长不改变复杂度的阶" 改为 "能达到的最好的阶由 \(\rho+s\) 决定"**：
   **（重要，必须做。）** 实际证明的只是：\(\rho+s\) 小时任何常数中心步长都只能做到 \(\epsilon^{-4}\)；\(\rho+s\) 足够大时存在一组合适的中心步长（\(\beta=0\)，\(\alpha=\Theta(\epsilon)\)）达到 \(\epsilon^{-3}\)。不得出现"中心步长不影响/不改变复杂度的阶"或"任意中心步长都可以"之类的说法；全稿检索 "do not change"、"regardless of the center"、"independent of the center" 等表述并逐一修正。
   - 摘要："determined by $\rho+s$ alone; the center stepsizes do not change its order." 改为：最好的可达阶由 \(\rho+s\) 决定；\(\rho+s\) 小时中心步长无法改进，\(\rho+s\) 足够大时取 \(\beta=0\) 并适当选取 \(\alpha\) 即可达到 \(\epsilon^{-3}\)。
   - 引言贡献 3 末句："the order of the iteration complexity is determined by $\rho+s$ alone, and the center stepsizes do not change it." 同样改写。
   - 结论第一段 "These results indicate that the order of the iteration complexity is determined by …" 同样改写。
   - 凡写到"增长后不需要移动中心"的地方，限定为对偶中心（\(\beta=0\)）；原始中心仍按 \(\alpha=\Theta(\epsilon)\) 移动。

## 交付要求

1. `latexmk -pdf main.tex` 编译通过，日志无错误、无未定义引用。
2. 回报：改动清单（文件:行号）；固定表达对照表及出处（找不到出处的单独列出）；所有仍未复核的引用点。
3. 在 `notes/progress/PROJECT_STATUS.md` 第 4 节把待办 1 标为完成，并记录 \(\alpha=\Theta(\epsilon)\)、\(c_s\) 足够大这两个限定。
