# 会话交接：2026-10-13（第 4 节下界证明：开头、4.1、4.2、附录 A）

## 附录 A 核对更新

2026-10-13 已完成附录 A 的逐式解析核对和独立代理审阅，包括参数界引理、实例类成员证明、谱分解、瞬态估计及正文旋转轨迹的接口。结论通过。已补足谱证明中非退化参数稠密性的依据，覆盖端点与重根；没有调整假设、参数和下界常数。全程未做数值验证。论文编译通过。详细记录见 `notes/progress/appendix-a-audit-20261013.md`。本更新优先于下文有关附录 A「未核对」的旧状态。

新会话先读本文件，再读 `notes/progress/PROJECT_STATUS.md`、`notes/progress/lb-proof-discussion-20261013.md`（本次讨论记录）和 `notes/gpt-proofs/lb-proof-materials.md`（GPT Pro 证明材料，三部分合一）。上一份交接 `SESSION_HANDOFF_20261012.md` 仍有效，本文件只记新进展。

## 0. 本日后半段的决定（优先于下文第 1–6 节中与之冲突的内容）

- **附录 A 已解析核对**（2026-10-13 晚）：参数界、(i)、谱分解、瞬态界成立；补充稠密性论证（`LowerBoundRotation.tex` 约第 329 行）；记录见 `appendix-a-audit-20261013.md`。下界只剩 §5 中 4.3、4.4（用户在写）。
- **当前结构（2026-10-13 晚，另一会话调整）**：§2 Preliminaries（记号、假设、问题类、驻点判据、oracle）；§3 Algorithm Family and Effective Penalty（`sections/AlgorithmFamily.tex`）；§4 主结果（`LowerBound.tex`，含 `thm:upper-beta1` 与 `thm:lower-bound`）；§5 下界证明（开头为 GDA 对应命题）；附录 A 旋转实例、B β=1 证明（开头为 `prop:curvature-smoothness`）、C 不依赖精度的参数选择（`thm:main`）、D 其证明。下文中的节号按此换算。

- **定位调整**：论文改为对单环 ALM 族 $\mathcal C_\theta$ 的紧性分析，不再以"提出固定罚 ALM 算法"为主线。全文逻辑、三个紧性结论、待办见 `PROJECT_STATUS.md` 第 1–4 节。
- **上界改为常数参数、两条引用路线**：$\beta=1$ 即 Smoothed GDA（Li Thm B.1，$O(\epsilon^{-4})$，换算已核对）；$\beta=0$、$s=\Theta(1/\epsilon)$ 即 Perturbed Smoothed GDA（Li Thm 3.3(i)，$O(\epsilon^{-3})$，待核对）。定理陈述计划放第 3 节，证明放附录 B；正文不出现 $\ell$、$\hat\Delta$、$D_{\mathcal Y}$，常数只写依赖哪些量。
- **时变线删除**：`sections/TimeVarying.tex` 已删，`main.tex` 的 `\input` 与引言 Organization 中的引用已删；笔记中相应任务已删。`thm:main` 去留待定。
- **4.2 开头已按 Li §5.1.1 的叙述重写**：先说明二次区域内更新线性、按谱分析；再说明为何取模为 1 的非实特征值；再说明零初值的分解。$\mathbb T$ 显式写在正文 `eq:rot-matrix`（不用 $\chi,d_\tau,m$）；Remark `rem:rotation` 删去两句重复，改为"two respects"。
- **附录 A**：A.1 参数从 34 个符号减到约 9 个（$\chi,d_\tau,U,E,H,\Upsilon,\xi,D,u,\Gamma,Z,M$ 等内联或移入证明）；新旧公式数值比对一致。此后 Codex 写入了 $c_1,c_2$（`eq:rot-thresholds`）、参数界引理与谱分解证明，**未核对**。
- **记号**：$\mathbb R^2\cong\mathbb C$ 的约定移入 Preliminaries 的 Notation 段。
- **写作规则**：`CLAUDE.md` 新增「论文正文的用词来源」；固定表达库 `notes/project/writing-phrasebook.md`（目前收 Li 2026、Mahdavinia 2022）。记忆新增"不引入只用一次的符号"。
- **初始化 Remark**：已由另一会话移到算法族定义之后（`Preliminaries.tex`），用户决定不写局限句。
- **引言**：第 159 行 "genius" 改为 "genuine"。
- **推送补充**：`Preliminaries.tex`、`Introduction.tex` 现有正文改动，需要推送；`TimeVarying.tex` 需 `git rm`。

## 1. 第 4 节当前状态（`sections/LowerBoundProof.tex`）

| 部分 | 状态 | 要点 |
|---|---|---|
| 开头 | 已写 | 用户改写的 Li 风格开头；量词式 $\forall(\alpha,\beta)\ \exists I$；阈值 $\alpha_\epsilon:=1024\max\{1,4\tau,4\gamma\tau\}\epsilon^2$ 在第一次划分时直接定义（不用 $\varpi$）；三块划分；与 Li/Mahdavinia 比较段与旧的 Small/Large 概述段目前为注释 |
| 4.1 `subsec:lb-plateau` | 已写 | Example `ex:plateau`（plateau Huber，$x_\star=\Delta/(2\epsilon)+\epsilon$，无 $g$、无 $N$）→ Remark `rem:plateau`（$\inf f=0$、$f(0)=\Delta$，间隙恰为 $\Delta$）→ 说明段 → Lemma `lem:plateau` (i) 乘子恒零、$R_k=\|\nabla f(x^{k+1})\|$ (ii) 位移界 (iii) $T>\Delta/(16\gamma\alpha\epsilon^2)$，$\alpha=0$ 时 $+\infty$ → 一行不等式换算成 $\Delta\epsilon^{-4}/(16384\gamma\max\{\cdot\})$。原 Proposition 已并入 Lemma (iii)。plateau 图已注释（决定不放） |
| 4.2 `subsec:lb-rotation` | 已写（草稿版） | Example `ex:rotation`（$\mathbb R^2\cong\mathbb C$，$f=\psi(\|x-x_c\|)-b\langle\lambda_c,x-x_c\rangle$，$\mathcal A=b(x-x_c)$，$h=\|\cdot\|_2$）→ Remark `rem:rotation`（与 Li Ex. 5.1 同形式；两处适配、三处新论证）→ 机制段 → Lemma `lem:rot-spectral` → Lemma `lem:rot-estimates`（(i) 参数估计 (ii) 类成员 (iii)(iv) 瞬态界，证明在附录）→ Lemma `lem:rot-trajectory`（先定义候选轨迹 $\tilde w^k$，验证满足 SPLALM 每步更新，再得实际轨迹；$R_k\ge\frac76\epsilon$） |
| 4.3 `subsec:lb-huber`（$\beta=0$） | 已写 | Example `ex:huber`：复用 plateau $f$（用户要求实例不过度退化；间隙恰为 $\Delta$），$\mathcal A\equiv a_0$，Huber $h$（$q_h=2s+1$）→ 机制段 → Lemma `lem:huber`（(i) $\lambda^k=\bar\lambda(1-\varphi^k)$ 闭式 (ii) 可行性残差 $>3\epsilon$，$T=+\infty$，对任意 $\alpha$）。不写 Remark（用户决定）。数值核对：2000 组参数 $\min_k$ 残差$/\epsilon\ge3.12$ |
| 4.4 `subsec:lb-combine` | 已写 | $c_1,c_2$ 仍引用附录 A `eq:rot-thresholds`；合并证明按三种情形逐一核对条件；无门槛用途表；推论 `cor:effective-penalty` 的证明未写。$R_k$ 定义已加入（现位于 `Preliminaries.tex` 的 `subsec:gda-embedding` 开头） |

## 2. 附录（Codex 已完成，本次又补了内容）

- `main.tex`：`\input{sections/UpperBound}` 后加 `\appendix`、`\input{appendix/LowerBoundRotation}`、`\input{appendix/UpperBoundProofs}`。
- `appendix/UpperBoundProofs.tex`（Appendix B）：第 6 节辅助证明原样搬入（逐字节核对通过），`UpperBound.tex` 中原 `\appendix` 已删。
- `appendix/LowerBoundRotation.tex`（Appendix A）：七组参数定义 `eq:rot-basic`…`eq:rot-constants`，本次补 `eq:rot-shift`（$\mathbf v,\mathbf r,x_c,\lambda_c,\mathbf w_c$）；三个证明小节只有 `\todo`：Lemma `lem:rot-estimates` (i)–(ii)、`lem:rot-spectral`、`lem:rot-estimates` (iii)–(iv)。
- 记号替换：$J\to\Upsilon$，$L\to\Gamma$，$\mathbb M\to\mathbb T$，$h_x\to\omega_x$，$d\to d_\tau$；**不用 `\iota`**（`LowerBound.tex:164` 已作指示函数）。
- `appendix/complexity_analysis.tex` 为旧文件，未被引用，未处理。

## 3. 其他改动

- 定理 `thm:lower-bound` 常数 32768 → **16384**（$2^{14}$），全稿统一。
- `tools/shared.tex` 新增 `example` 环境（已推送）。
- 用户偏好：一维实例也用范数 $\|\cdot\|$、$\nabla f$ 表达；中文回复中领域术语用英文原词（已存入记忆）；措辞平实、不要 AI 腔。

## 4. 推送状态

- Overleaf 最新提交 `0f7c0d0`（开头 + 4.1 + example 环境）。
- **未推送**：`main.tex`、`sections/LowerBound.tex`、`sections/LowerBoundProof.tex`、`sections/UpperBound.tex`、新目录 `appendix/`（根目录尚无此目录，推送时需 `git add appendix/LowerBoundRotation.tex appendix/UpperBoundProofs.tex`）。
- `sections/Preliminaries.tex` 本地与 Overleaf 只差首行 `% !TEX root` 注释，不推。
- 推送流程同 10-12 交接第 4 节最后一条：先 `git fetch` 核对远端，再复制到根目录提交。

## 5. 待办（按优先级）

1. **核对并写附录 A 的三个证明**（引理 1♯、2、3♯）。它们仍是 GPT Pro 草稿，未独立复核；GPT Pro 建议优先查谱分解、区域不变性、瞬态估计。Remark `rem:rotation` 中"新论证"的主张依赖这三个证明。
2. 写 4.3（$\beta=0$ Huber 实例），格式同 4.1/4.2：Example → Remark → Lemma。
3. 写 4.4：$c_1,c_2$ 定义、门槛用途表、合并证明、推论 `cor:effective-penalty` 的证明。
4. 画旋转实例图：任务说明在 `notes/prompts/codex-rotation-figure.md`（两子图：圆环轨迹 + $R_k/\epsilon$；示意用，不做验证）。待交给 Codex。
5. 结构调整（待用户确认）：把 `prop:reduction`、`prop:embedding`、`eq:gda-recursion`、`rem:embedding-scope` (i)–(iii) 从 3.2 节移到第 4 节开头的新小节，3.2 节只留两三句与 (iv)、待写推论；label 不变。
6. 开头的量词式右端仍写 $\ge\Omega(\Delta\epsilon^{-4})$，建议改为显式常数或 $=\Omega(\cdot)$。
7. `rem:lb-initialization`（3 节）与第 4 节开头的比较段内容重叠，比较段目前是注释，需定去留。
8. 可选：在 4.4 或推论处加入"plateau 实例给出 $\alpha=\Omega(\epsilon)$ 的必要尺度，且不依赖 $\rho+s$"（与上界计划 $\alpha=\Theta(\epsilon)$ 对应，上界未证，待验证）。

## 6. 已定的写作判断

- 证明顺序先按 $\alpha$ 分是写作选择，不具必然性；先按 $\beta$ 分同样可行（$\beta=0$ 实例对任意 $\alpha$ 成立）。
- $\alpha_\epsilon$ 是充分条件：使 plateau 下界达到 $\epsilon^{-4}$，并使旋转实例估计成立；不称"最小可行步长"或"实例失效边界"。
- 与文献的区别：主结论是"调整常数中心步长不能替代有效罚参数的必要增长"；零初值是第二层区别；三个实例是证明安排，不是贡献。与 Mahdavinia 的量词比较需写明出处是其附录 C.1（固定 $\eta_y=\Theta(1/\ell)$）。
- 每小节格式：Example → Remark → 说明段 → Lemma（复杂度结论并入最后一个 Lemma，不单列 Proposition）。
