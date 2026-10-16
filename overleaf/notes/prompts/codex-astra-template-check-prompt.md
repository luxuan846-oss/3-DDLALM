# 任务：核对"统一模板（rho >= 0）"论断与相关文献

> 历史任务草案，状态更新于 2026-10-16。原报告未确认完成，不能标为已完成；正文含旧路径、旧定义和需要重新核对的覆盖关系，不直接执行。当前文献核对任务见 `notes/prompts/gptpro-literature-research-prompt.md`，当前范围见 `notes/progress/PROJECT_STATUS.md`。

> 状态（2026-10-12）：尚未执行，未生成报告。文中路径为旧稿（`sections/Methodology.tex`、`notes/PROJECT_STATUS.md` 等已迁移或删除），执行前需更新。


你在 SPLALM/DDLALM 论文目录中工作。只写报告文件，不修改任何 .tex、.bib、notes/ 文件。

## 0. 先读
1. `CLAUDE.md`（写作规范）。
2. `notes/PROJECT_STATUS.md`（下界定理、机制、待办）。
3. `sections/LowerBound.tex`（实例类、算法族、复杂度定义）、`sections/Methodology.tex`（Algorithm `alg:ddlalm`、式 `eq:explicit-updates`）、`sections/Preliminaries.tex`（`ass:h`）。
4. `notes/literature.md`（已有文献判断及核对状态）、`notes/ddlalm-research-questions.md`。
5. 在 `tmp/`、`notes/`、`sections/` 中查找下界的证明和数值脚本（困难实例：A ≡ 0 的一维平台实例；A(x)=bx、h=||.||_2、f 在半径 r_* 内负曲率的二维实例）。

## 1. 待核对的论断（来自 Claude 的上一轮分析）
- (C1) 由 Moreau 分解，q(x,λ) = λ + ρ[A(x) − y(x,λ)] = prox_{ρh*}(λ + ρA(x))；因此 ALM 的 x 步使用从 λ 出发、步长 ρ 的一次对偶近端上升后的点。
- (C2) max_λ P_s(x,λ;z,μ) = max_q { f(x) + <A(x),q> − h*(q) − ||q−μ||²/(2(ρ+s)) } + ||x−z||²/(2γ)。
- (C3) ∇_x P_s 不含 s；其关于 x 的 Lipschitz 常数约为 L_f + L_A L_h + ρ G_A² + 1/γ，与 s 无关。
- (C4) 在 prox 不激活的区域（h=||.||_2，||λ+ρA(x)|| ≤ 1，y ≡ 0，q = λ+ρA(x)），SPLALM 的更新为
  x+ = x − η[∇f(x) + J_A(x)^T(λ + ρA(x)) + (x−z)/γ]，
  λ+ = λ + τ[A(x+) − (λ−μ)/s]，
  z+ = z + α(x+ − z)，μ+ = μ + β(λ+ − μ)。
  DS-GDA 作用于 L(x,q) = f(x) + <A(x),q> − h*(q)、且投影不激活时，给出 ρ = 0 的同一组式子（r1 = 1/γ，r2 = 1/s）。两者唯一差别是 x 步中的 ρ J_A(x)^T A(x)。
- (C5) 下界常数 K_θ = max{1, 4τ, 4γτ} 不含 ρ，所以下界可能对 ρ ∈ [0, ρ̄] 一致成立；需检查 ε_θ 及证明各步对 ρ 的依赖，以及 ρ = 0、s = ∞ 时证明是否仍成立。
- (C6) Smoothed GDA = (ρ=0, s=∞, 只移动 z)；PSGDA = (ρ=0, s=Θ(D_Y/ε), μ ≡ 0)；DS-GDA = (ρ=0, s 固定, 两个中心常数平均)。

## 2. 任务 A：联网核对文献（必须对照原文，记录定理/算法/式编号与 URL）
- A1. DS-GDA：Zheng, Zhu, So, Blanchet, Li, *Universal Gradient Descent Ascent Method for Nonconvex-Nonconcave Minimax Optimization*, NeurIPS 2023, arXiv:2212.12978。核对 Algorithm 1 的更新顺序（x 步用 y^t 还是 y^{t+1}；y 步用 x^t 还是 x^{t+1}）、投影位置、中心更新用的是哪一步的迭代；参数条件；Theorem 1 在对偶凹情形的速率；是否要求 X、Y 紧。这条决定 (C4) 是否成立，优先完成。
- A2. Smoothed GDA：Zhang, Xiao, Sun, Luo, NeurIPS 2020。核对更新顺序。
- A3. Li, Nagarajan, Pan, Zhang, arXiv:2602.14185：Thm 3.2、Thm 3.4、Cor 3.1 的算法形式（PGDA、SGDA、PSGDA）、下界量词（对哪些参数/步长成立、初值是否由实例选择）、平稳性度量（GS/OS）、困难实例是否属于 f(x) + <A(x),y> − h(y) 形式；是否有任何结果覆盖移动对偶中心（DS-GDA 型）。
- A4. arXiv:2609.17973：标题、作者、算法、GS 速率、参数尺度。
- A5. GDPA：Lu, ICML 2022：问题类、ρ 的尺度、复杂度。
- A6. Pan, Zheng, Li, arXiv:2609.14235：Remark 3.3 中 GS 的 O(ε^{-5/2}) 论断。
- A7. 检索 2023–2026 年是否已有：DS-GDA（固定参数、移动中心）在 NC-C 上的紧性/下界；单循环线性化 ALM 的算法类下界。列出找到的文献；没有找到就写"未找到"及所用检索词。

## 3. 任务 B：数学与证明核对
- B1. 逐条验证 (C1)–(C3)，给出推导。
- B2. 按 A1 核实的 DS-GDA 更新顺序，写出它在投影不激活区域的递推，与 (C4) 逐项比较；列出全部差别。
- B3. 找到下界证明后，逐步标注每一步用到的结构（单循环、Gauss–Seidel 顺序、时不变参数、ρ > 0、s < ∞、prox 不激活等），判断 (C5)：ρ = 0 和 s = ∞ 时哪些步骤需要修改。找不到证明就明确说明。
- B4. 若找到数值脚本或实例参数，在 ρ = 0 与若干 ρ > 0、若干 (α,β) 下运行，报告 R_k 的行为是否与定理一致。

## 4. 交付
写入 `Claude outputs/codex-astra-report.md`，中文，技术术语保留英文，数学用 LaTeX。结构：
1. 结论摘要（C1–C6 各一行：成立 / 不成立 / 需修改，附一句理由）。
2. 任务 A 逐条：结论、原文位置（定理/算法/式编号）、URL、状态（已核对 / 未核对 / 与 notes/literature.md 冲突）。
3. 任务 B 逐条：推导或证明步骤标注。
4. 仍未解决的问题。
无法访问原文的条目标"未核对"，不要凭记忆填写。
