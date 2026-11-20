# SPLALM 项目状态

更新日期：第 1–6 节为 2026-10-16 整理，2026-10-26 更新文件位置；第 7 节为 2026-10-26 新增。**本文件是当前进度与待办的唯一入口。** 依据当前本地源码、已有核查记录及讨论整理。第 1–6 节的更新没有重新核对数学证明，也没有重新编译论文。

历史交接、旧任务表、研究主线和白板用于追溯讨论，不作为当前待办。源码说明已经写入什么；核查记录说明已经核对什么；两者分别记录。

## 1. 当前阶段与范围

- 阶段：完整初稿的完善。算法名为 SPLALM，旧材料中的 DDLALM 指同一项目。
- 主线：单环线性化 ALM 族 $\mathcal C_\theta$ 在指定参数区域内的复杂度下界，以及与已有方法上界的联系。重点说明组合罚参数 $\rho+s$、对偶正则与中心步长各自的作用。
- 新结果重点：对所有常数中心步长一致成立的下界。两个上界分别由 Smoothed GDA、Perturbed Smoothed GDA 的分析换算得到。
- 当前源码标题：*Shrink the Dual Regularization, Keep the Penalty: Tight Complexity of Linearized Augmented Lagrangian Methods*。用户已接受调整标题；新标题尚未确定。
- 评议参照：以 SIOPT 中贡献类型相近的工作为主，再依据成果讨论 Mathematical Programming。旧任务表中的结果与期刊对应关系不作为当前决定。
- 已关闭：把下界推广到时变或单调中心步长，不列入本轮必须完成的工作。

## 2. 已写入的结果与适用范围

1. **下界 `thm:lower-bound`。** 固定 $0<\eta\le\gamma$、$\tau>0$、$\Delta>0$，对充分小的精度、$\rho>0$、$s\ge\tau$ 且 $\epsilon(\rho+s)\le c_1$，每组常数 $(\alpha,\beta)\in[0,1]^2$ 均有从全零初值出发的困难实例，给出 $\Omega(\epsilon^{-4})$。常数 $c_1,c_2$ 不依赖 $\rho,s,\alpha,\beta$，精确量词和常数见定理。平台、旋转、Huber 三分支及主定理证明均已写入；部分核查待完成，见第 4 节。
2. **上界 `thm:upper-beta1`。** 在该定理的步长条件下，取 $\beta=1$、$\alpha=c\epsilon^2$，得到 $O(\epsilon^{-4})$。在同一问题类、固定 $\rho$ 且满足上下界共同条件时，与下界形成族复杂度的紧性结论。不能把该上界常数未经核对地用于随精度增长的 $\rho$。
3. **上界 `thm:upper-beta0`。** 固定 $\rho,\gamma,\eta,\tau$ 并满足 `eq:beta0-stepsizes`，取 $s=c_s/\epsilon$、$\alpha=c_\alpha\epsilon$、$\beta=0$，得到 $O(\epsilon^{-3})$。$c_s$ 足够大、$c_\alpha$ 足够小，参数在单次运行内保持常数。定理、Remark、附录证明均已写入；$C_*$ 的引用换算仍待独立逐行核对。
4. **合并推论 `cor:effective-penalty`。** 已写入上述下界区域与固定 $\rho$ 的充分参数路径。$\rho=c/\epsilon$、$s$ 固定及上侧其他参数路径的族内复杂度尚未由这些结果刻画。
5. **补充上界 `thm:main`。** 递增 $s_k$ 的 accuracy-independent schedule 仍在附录中，使用额外的水平有界假设。它与已经关闭的“时变中心步长下界推广”分别处理。

表述约束：低参数区域内，调节常数中心步长无法突破上述下界；固定 $\rho$ 时，已有一组参数达到较好的上界。不能写“中心步长与复杂度无关”“增大 $\rho$ 在所有区域都无效”或“整个上侧区域只由 $\rho+s$ 决定”。$\beta=0$ 固定的是对偶中心，原始中心仍移动。$O(\epsilon^{-3})$ 的可达性本身不等于该区域的复杂度最优性。

## 3. 当前稿件与产物

| 位置 | 文件 | 状态 |
|---|---|---|
| §1 | `sections/Introduction.tex` | 问题、比较表与贡献已写入；随评议完善定位与措辞 |
| §2 | `sections/Preliminaries.tex` | 问题类、驻点判据与 oracle 定义 |
| §3 | `sections/AlgorithmFamily.tex` | 算法族、复杂度、组合罚参数与特殊情形 |
| §4 | `sections/LowerBound.tex` | 两个上界、下界及合并推论均已写入 |
| §5 | `sections/LowerBoundProof.tex` | GDA 递推对应、三个困难实例分支与主定理证明均已写入 |
| §6 | `sections/Conclusion.tex` | 总结与开放问题已写入 |
| 附录 A | `appendix/LowerBoundRotation.tex` | 已有 10-13 解析核查记录 |
| 附录 B | `appendix/UpperBoundBetaOne.tex` | β=1 上界证明已写入 |
| 附录 C | `appendix/UpperBoundBetaZero.tex` | β=0 上界证明已写入；末尾保留未核对事项 |
| 附录 D、E | `sections/UpperBound.tex`、`appendix/UpperBoundProofs.tex` | 递增参数上界及证明，作为补充 |

- 旋转示意图：`figures/plot_rotation_instance.py` 与 `figures/rotation_instance.pdf` 已存在，不再列为待生成；本次未重跑脚本，也未重新验收图形。
- `sections/RelatedWorkDraft.tex` 和旧独立核查产物已清理；附录 A 的详细核查记录保留。
- `main.pdf` 为已有产物；本次未重新编译，阅读时以源码为准。

## 4. 当前待办

### 与老师讨论：Fast LRALM 加速（2026-11-17 确定的工作内容）

每次讨论只谈一块。本次只谈加速，下界、arXiv、署名不在本次议程中。材料由下面四部分组成。

**1. 加速的本质（一段话）。** 固定 $\rho$ 后，$\mathcal{D}_\rho$ 关于 $\boldsymbol\lambda$ 是光滑凹函数，梯度 Lipschitz 常数只依赖 $\rho$。按 Lin–Jin–Jordan（COLT 2020）的归约，加以 $\mathbf{0}$ 为中心、系数 $1/s$ 的对偶正则，问题变成 NC-SC。乘子在半径 $L_h$ 的球内，正则偏差为 $\mathcal{O}(L_h/s)$，取 $s=\Theta(\epsilon^{-1})$，对偶条件数 $\kappa=\Theta(\epsilon^{-1})$。NC-SC 下界 $\Omega(\sqrt{\kappa}\,\epsilon^{-2})$（Zhang 等 UAI 2021；Li 等 NeurIPS 2021）代入得 $\epsilon^{-5/2}$。不加速时对 $\kappa$ 一次依赖，$\kappa\,\epsilon^{-2}=\epsilon^{-3}$，即 LRALM 族的 $\Theta(\epsilon^{-3})$。加速就是把 $\kappa$ 降为 $\sqrt{\kappa}$；对偶目标在全空间光滑强凹，无需投影，Nesterov 外推直接加在乘子步上。
- 待核：`thm:upper-beta0` 只写了常数 $C'$，对 $\kappa$ 的一次依赖需从附录证明中提取。

**2. 讨论提纲。**
- Related work 中加速的做法：IAIPAL、iALM 多循环，加速在内层（APG 解强凸子问题），带对数因子；本文单循环，加速在外层乘子步。
- 分析难点（算法简单，分析不简单）：(i) 乘子有界性，不投影时外推乘子需另证有界（`lem:b2-prime-multiplier-bounds`，用 $h$ 的 Lipschitz 性）；(ii) Lyapunov 函数构造，外推后单步不单调，收缩的是估计序列 $\mathbf{w}^k$，误差放大 $\sqrt{\kappa}$ 倍，需 $\alpha\le 1/(6\sqrt{\kappa})$，势函数加原始跟踪项与增量项。
- 与别人的区别：ALM 方面，核查过的 20 篇内无非凸 ALM 乘子外推的复杂度结果；minimax 方面绕不开，Zhang–Xu 已在 $\mathcal{D}_\rho$ 上（对偶球半径 $2L_h$）给出 Problem (P) 的单循环 $\mathcal{O}(\epsilon^{-5/2})$。请老师确认定位：贡献放在问题一的族下界，加速部分只主张算法与分析更简单（梯度步加外推，无投影，无 extragradient）。

**3. 汇报文献。**

| Method | arXiv | 结论 | 备注 |
|---|---|---|---|
| Zhang–Yang–Guzmán–Kiyavash–He, UAI 2021 | 2103.15888 | NC-SC 下界 $\Omega(\sqrt{\kappa}L\Delta\,\epsilon^{-2})$；加速框架反复解 SC-SC 子问题，上下界差对数因子 | 下界中 $\sqrt{\kappa}$ 的来源 |
| Li–Tian–Zhang–Jadbabaie, NeurIPS 2021 | 2104.08708 | 同一下界，确定性 oracle；指出 Lin–Jin–Jordan 上界在 $\epsilon$、$\kappa$ 上最优（差对数因子） | 与上一篇并列引用 |
| Lin–Jin–Jordan, COLT 2020 | 2002.02417 | SC-SC 上 $\tilde{\mathcal{O}}(\sqrt{\kappa_x\kappa_y})$；推广到 NC-SC、NC-C（Minimax-PPA） | 加 $\Theta(\epsilon)$ 对偶正则，NC-C 变为 $\kappa=\Theta(\epsilon^{-1})$ 的 NC-SC，得 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$ |
| Kong–Melo–Monteiro, SIOPT 2023 (IAIPAL) | 2008.00562 | 线性约束非凸复合问题，经典 AL；内层 ACG，共 $\mathcal{O}(\epsilon^{-5/2}\log^2\epsilon^{-1})$ | 加速 ALM |
| Li–Chen–Liu–Lu–Xu, AISTATS 2021 (iALM) | 2007.01284 | 仿射等式约束 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$，非凸约束 $\tilde{\mathcal{O}}(\epsilon^{-3})$，$\epsilon$-KKT，需正则性条件 | 加速 ALM |

另加：Kong–Monteiro 2024（单循环，乘子阻尼中心在 $\mathbf{0}$，罚参数 $\Omega(\epsilon^{-1})$，$\mathcal{O}(\epsilon^{-3})$，最接近 $\beta=0$ 成员）；Zhang–Xu（arXiv:2609.17973，最大风险，必须汇报）；Ke–Mei–Zhang（arXiv:2609.25752，经 $h^*$ 多层循环在本文问题类上达到 $\mathcal{O}(\epsilon^{-5/2})$）。

**4. 投稿与实验。** 期刊建议 SIOPT，备选 Math Programming。实验提议（待用户确认实例后再写代码）：robust phase retrieval，$\min_{\mathbf{x}} \frac{1}{m}\sum_i \lvert\langle\mathbf{a}_i,\mathbf{x}\rangle^2-b_i\rvert$，$n=50$、$m=200$；方法为 LRALM（$\beta=1$）、LRALM（$\beta=0$，$s=c_s/\epsilon$）、Fast LRALM；记录达到 $\epsilon$-KKT 的迭代数，对数坐标拟合斜率，预期 $-4$、$-3$、$-5/2$；$\epsilon^{-4}$ 一条只取 $\epsilon\in[0.03,0.3]$。

### 优先完成

1. **β=0 上界引用换算。** 对照 Li26 v2 §4.2 (4.19)–(4.23)，核对 `eq:beta0-gs-rate` 中 $C_*$ 的存在性、参数依赖、精度一致性和平均常数。证明材料见 `notes/gpt-proofs/beta0-upper-check-20261013.md`。写入完成不代表核查完成。
2. **下界证明衔接。** 核对 §5 的 `subsec:lb-huber` 与主定理证明，确认分支覆盖、零初值、实例类成员关系和统一常数。附录 A 的既有通过记录不能替代这些分支的核查。
3. **初稿评议与叙事完善。** 使用 `notes/prompts/gptpro-draft-review-prompt.md`。依据实际定理调整标题、摘要、问题 (Q)、贡献与结论，突出参数区域下界增加的认识。当前摘要仍使用 “$s$ of order $1/\epsilon$” 的简写；需核对其是否应补明充分大的系数与中心步长条件，不能沿用旧记录声称全部措辞已同步。

### 族外加速 B2′（2026-11-09 证明；2026-11-11 更新）

4. **B2′ 的 $O(\epsilon^{-5/2})$ 上界：笔记层面已证，已通过外部审查，尚未写入论文。**
   - **算法**：B2′ 是 LRALM（$\beta=0$）加上对偶 Nesterov 外推，系数为 $(1-\varsigma)/(1+\varsigma)$，其中 $\varsigma=\sqrt{\tau/s}$；中心步长 $\alpha=\varsigma/6$。不需要投影，也不需要 OGDA。
   - **材料**：汇总及查新见 `notes/gpt-proofs/b2-summary-20261109.md`；推导见 `notes/gpt-proofs/b2-G*-20261109.md`；审查见 `notes/progress/b2-review-G*-20261109.md`。
   - **查新**：没有找到完全相同的工作。最接近的是 Pan–Zheng–Li 的 Tracked-FOAM（arXiv:2609.14235），它与本文证明骨架相同，但属于多层循环；其次是 Zhang–Xu（heavy-ball + EG + 投影）。
   - **用户已定（11-10）**：作为主定理写入论文，附录给出完整证明。
   - **待讨论，定下后交 Codex 严格执行**：
     - 新建 `sections/Acceleration.tex`，放在 `LowerBoundProof` 之后、`Conclusion` 之前；另建 `appendix/AccelerationProof.tex`，按 G1→G2→G3 改写。
     - 算法名定为 "Fast LRALM"，不放入 $\mathcal C_\theta$。
     - 定理中直接写外推系数，不引入新符号。
     - Remark 分别对比 Zhang–Xu、Tracked-FOAM 和族内结果。
     - G2 中关于 OGDA 的二次模型分析不写入论文。
   - **悬而未决**：
     - 族内 $\Omega(\epsilon^{-3})$ 是否写入：它决定论文能否称为"分离"。证明不在仓库，由用户主导。
     - 标题三个候选：见 11-10 对话，倾向 "Fixed-Penalty Linearized Augmented Lagrangian Methods: Tight Complexity and Acceleration by Dual Extrapolation"。
     - 用户要改写 (Q)（`sections/Introduction.tex` 第 183–186 行）。
     - B2′ 写入论文前，用户需要复核 G2 的 Lemma G2.1 与定理 G2.4。
     - 含 OGDA 的 B2、anytime 版本 $s_k\sim k^{2/5}$ 仍是待证。

5. **全文改名（2026-11-11 已完成）。** SPLALM 改为 LRALM，"smoothed perturbed linearized ALM" 改为 "linearized regularized ALM"，combined penalty 改为 effective penalty，"smoothed perturbed potential function" 改为 "regularized potential function"，共 9 个文件 62 处。标签 `def:splalm`、`eq:splalm-updates` 未改。在 `/tmp` 下编译通过，没有未定义引用；`main.pdf` 没有重新生成。待定：
   - 是否像 slides 那样改称 "regularized function"；
   - LRALM 尚未做重名检索；
   - 本文件标题和第 1–3 节仍写 SPLALM，属于历史记录。

6. **Fast LRALM 证明重构（2026-11-12 交接，进行中）。** 算法为 `sections/Acceleration.tex` 的 Algorithm 6.1（即 B2′），定理为 `thm:b2-prime-complexity`。（注：重构前的初版 Fast LRALM 与全文 LRALM 改名已推送 Overleaf `origin/master` commit `7e3b129`；以下重构改动均在本地，尚未推送。）
   - **已完成的文件改动**：
     - 删除 `sections/UpperBound.tex`（旧附录 D）和 `appendix/UpperBoundProofs.tex`（旧附录 E），递增 $s_k$ 的结果不再做；旧版本在 git 历史中。
     - 将全局常数 $L_{\mathcal{D},\mathbf{x}}$、$\mu_\gamma$、$L_x$、$L_\lambda:=\rho^{-1}+s^{-1}$（不带括号参数 $s$）、$\nabla\mathcal{D}_\rho$ 公式及曲率光滑性命题 `prop:curvature-smoothness` 从 `appendix/UpperBoundBetaOne.tex` 前移到正文第 3.1 节 `sections/AlgorithmFamily.tex`（紧跟 `eq:potential`、位于 `def:splalm` 之前）；证明仍留在 `appendix/UpperBoundBetaOne.tex` 末尾（`app:curvature-smoothness`）。
     - `sections/Acceleration.tex` 第 32–39 行：用纯算法结构语言改写 Fast LRALM 不属于 $\mathcal{C}_\theta$ 的原因（对偶变量引入 Nesterov 外推并在 $\bar{\boldsymbol{\lambda}}^k$ 而非 $\boldsymbol{\lambda}^k$ 处计算 $\mathcal{P}_s$ 的两块偏梯度，原始步为普通梯度步）。
     - `sections/Acceleration.tex` 第 6.2 节精简与标红占位：开头只对 $\boldsymbol{\mu}=\mathbf{0}$ 引用第 3.1 节的 `prop:curvature-smoothness` 定义单套值函数与唯一鞍点（去掉提前堆砌的 $\mathbf{w}^k,c_e,c_r,\mathcal{E}_k$ 与一般 $\boldsymbol{\mu}$ 重复定义）；`lem:b2-prime-residual-decomposition` 补入 $\mathbf{q}^k\in\partial h(\mathbf{y}^{k+1})$ 并把原始残差系数收紧为 $(\lvert\eta^{-1}-\gamma^{-1}\rvert+L_{\mathcal{D},\mathbf{x}})$；`lem:b2-prime-multiplier-bounds` 条件统一为 $\tau L_\lambda\le 1/2$，$C_\lambda:=\max\{4,\sqrt{8\rho/\tau}\}$；删去旧的绕道 $\mathcal{E}_k$ 的 `lem:b2-prime-residual-bound`，将待顺推构造的势函数 $\mathcal{W}_k$、一步三项步差耗散系数 $(c_1,c_2,c_3)$、初值界 $\Delta_{\mathcal{W}}$ 及 $C_R$ 用红色占位，直接闭合 `thm:b2-prime-complexity` 的证明。
     - 独立 `/private/tmp` 编译通过（36 页，零报错、零未定义引用）；本地 `main.pdf` 未重新生成。2026-11-12 后续：`main.tex` 第 74–76 行暂时注释了附录 A、B、C 的 `\input`，此状态下编译零报错，但有 15 个未定义引用（`app:curvature-smoothness`、`app:upper-beta1`、`app:upper-beta0` 等），恢复这三行后消失。
   - **已验算完毕的常数结论（供下一步顺推写入附录使用）**：
     - 取常数权重 $c_e:=\frac{3}{25}(L_x+\frac{\mu_\gamma}{2})$、$c_r:=\frac{G_{\mathcal{A}}^2}{4\mu_\gamma}$，已用 Python `fractions.Fraction` 对 $\gamma L_{\mathcal{D},\mathbf{x}}\in[0,1/10]$ 精确有理数验算：$c_e/\mu_\gamma\le\frac{31}{150}$ 保持不变，故 `Lemma G3.2`（$C_{\mathbf{z},1},C_{\mathbf{z},2}$）与 `Proposition G3.5`（$\Delta_{\mathcal{W}}$）原常数完全不变；同时 G2.4 + G3.4 在 $\mathcal{W}_{k+1}-\mathcal{W}_k$ 中精确给出三项步差耗散系数 $c_1=\frac{1}{250\gamma}$（精确下界 $\frac{1}{242\gamma}$）、$c_2=\frac{1}{16\tau}$、$c_3=\frac{1}{5\gamma}$。
   - **下一步任务（新对话直接接手）**：
     - 按用户定下的“先顺着推长出势函数，定稿后再浓缩回填正文标红处”的两阶段写法，在 `appendix/AccelerationProof.tex` 中用优化论文风格完整写出 6 步顺推证明（不再拆陈述与证明两个文件）：
       1. `lem:b2-prime-residual-decomposition` 的证明（Moreau 包络梯度加近端项对消）；
       2. `lem:b2-prime-multiplier-bounds` 的证明：**已完成（2026-11-12）**。条件为 $\tau L_\lambda\le 1/2$；外推系数在正文记为 $\omega:=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}$，Algorithm 6.1 与附录统一使用；结论合并为 $\max\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\}\le 3C_\lambda L_h$；证明把乘子写成次梯度的加权和，权重的 $\ell_1$ 界由附录数值引理 `lem:scalar-recursion` 给出；
       3. 值函数正则性、鞍点对中心的灵敏度（含 $\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 的 $\sqrt{s}$ 灵敏度）与外层 $p_s$ 中心步一步下降（吸收原旧附录 D 的 `lem:v2-value-regularity`、`lem:saddle-center-stability`、`lem:z-step-p`，固定 $s$ 与 $\boldsymbol{\mu}=\mathbf{0}$）；
       4. 固定中心部分模型 $\mathcal{P}_s(\mathbf{x}^{k+1},\cdot;\mathbf{z},\mathbf{0})$ 上的对偶 Nesterov 不等式（自然导出 $\mathbf{w}^k$）与原始跟踪收缩（自然导出权重 $c_e,c_r$ 与内层能量 $\mathcal{E}_k$，保留 $-\frac{1}{121\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2$ 与 $-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2$）；
       5. 中心漂移误差（三处 $\sqrt{s}$ 相消）与总势函数 $\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$ 一步下降（证出 `lem:b2-prime-potential-descent`）；
       6. 零初值下 $\mathcal{W}_0-\mathcal{W}_K\le\Delta_{\mathcal{W}}$ 的证明（证出 `lem:b2-prime-initial-gap`）。
     - 附录顺推经用户审定后，将具体的 $\mathcal{W}_k$、$(c_1,c_2,c_3)$、$\Delta_{\mathcal{W}}$ 与 $C_R$ 回填替换 `sections/Acceleration.tex` 中的红色占位块。
   - **编号约定与材料来源（2026-11-12 补记，供新对话对照）**：
     - 正文引理编号：L1 = `lem:b2-prime-residual-decomposition`；L2 = `lem:b2-prime-multiplier-bounds`；L3 = `lem:b2-prime-potential-descent`；L4 = `lem:b2-prime-initial-gap`。
     - 附录每个正文引理占一个子节。只服务于一个引理的辅助引理放在该引理的子节里：数值引理 `lem:scalar-recursion` 在 L2 的子节；A1–A4 在 L3 的子节。L4 的证明引用 A1 中 $p_s$ 的下界，不重复陈述。
     - 状态：L1 陈述已写、证明未写；L2 陈述与证明已写；L3 待写，路线 2 的常数已验算（见上文“已验算完毕的常数结论”），可直接动笔；L4 占位。
     - 旧附录 D、E 的取回命令：`git show b69dee2:overleaf/sections/UpperBound.tex`、`git show b69dee2:overleaf/appendix/UpperBoundProofs.tex`。
     - A1–A4 的来源（G 编号指 `notes/gpt-proofs/b2-G*-20261109.md` 中的引理）：

       | 辅助引理 | 内容 | 来源 |
       |---|---|---|
       | A1 | 值函数正则性，$p_s$ 的下界与光滑性 | 旧附录 D 的 `lem:v2-value-regularity`；G3.1 |
       | A2 | 固定中心一步不等式 | G2.1、G2.3、G2.4，$c_e$ 按路线 2 取常数 |
       | A3 | $p_s$ 的中心步下降 | 旧附录 D 的 `lem:z-step-p`；G3.3 |
       | A4 | 中心移动误差 | 旧附录 D 的 `lem:saddle-center-stability`；G2.7、G3.2 |

   - **外部审核意见（2026-11-12，另一会话给出，尚未采纳）**：
     - 意见：L2 现有证明按特征根与脉冲响应展开，是信号处理的写法，应改成优化论文的写法，即把乘子更新看作受有界次梯度驱动的二阶阻尼系统，用离散能量或 Lyapunov 不等式归纳出界；并提出按 6 步顺推整体重写 `appendix/AccelerationProof.tex`。
     - 需要先核对的一点：G1.5 已证明，只用 $\lVert\mathbf{q}\rVert\le L_h$ 时，最坏半径确实达到 $(\tau L_\lambda)^{-1/2}L_h$ 量级，半径为 $L_h$ 的球不是不变集。所以"一步递推直接归纳"证不出 $L_h$ 量级的界；能量法若可行，得到的常数也必须含 $\sqrt{\rho/\tau}$。能量函数的具体形式尚未给出，属于待证。
     - 用户此前定下的写法是：正文按"乘子是次梯度的带符号加权和"叙述，权重的 $\ell_1$ 估计作为附录辅助引理。两种写法如何取舍由用户决定。

   - **对偶中心与加速的逻辑链（2026-11-12 定）**：近端中心 $\boldsymbol{\mu}=\boldsymbol{\lambda}^k$（$\beta=1$，即 Rockafellar 意义下 ALM 的对偶近端点步）不引入偏差，但对偶目标每步都变，族内得到 $\epsilon^{-4}$（$\beta=1$ 上界，与下界匹配）。固定中心 $\boldsymbol{\mu}=\mathbf{0}$（$\beta=0$）带来 $\lVert\boldsymbol{\lambda}\rVert/s$ 的偏差，需要 $s\sim1/\epsilon$，配合乘子一致有界把偏差压下去；作为交换得到固定的 $\frac{1}{s}$-强凹对偶函数 $d_s$，族内为 $\epsilon^{-3}$，加对偶 Nesterov 外推后为 $\epsilon^{-5/2}$。正文只写 "a fixed dual center makes $d_s$ a fixed strongly concave function, which the dual extrapolation requires"，不写 proximal ALM 不能加速（族外无证明）。`xie2021proximal` 的 proximal 项作用在原始变量上，引用前核对原文。

   - **其余保留小项**：
     - `eq:x-weak-convexity-modulus` 标签名沿用旧名未改（$L_{\mathcal{D},\mathbf{x}}$ 实为 $\nabla_{\mathbf{x}}\mathcal{D}_\rho(\cdot,\boldsymbol{\lambda})$ 的 Lipschitz 常数）；
     - 仓库根目录 `temp/` 下仍有 11-06 至 11-11 留下的历史验算脚本（`lin20a/`、`q3check/`、`rate_check*.py`），未经确认未删。
   - **查新补充（已读原文）**：Chen–Ma–Zhou 的 proximal-AltGDAm（arXiv:2112.11663，全文在 `memory/readings/altgdam-2112.11663/`）没有近端中心，用交替 GDA 加对偶 Nesterov，复杂度 $O(\kappa^{11/6}\epsilon^{-2})$，原始步长须取 $\eta_x\le1/(16L\kappa^{11/6})$。代入 $\kappa\sim\epsilon^{-1}$ 得 $\epsilon^{-23/6}$。这说明去掉 $\mathbf{z}$ 后不能得到 $\epsilon^{-5/2}$，可用来回答"为什么需要近端中心"。SSNAL（arXiv:1607.05428，全文在 `memory/readings/ssnal-1607.05428/`）的牛顿步用在 ALM 子问题上，乘子仍是一阶更新，不属于对偶二阶方法。

### 与定位直接相关的文献核对

- 按 `notes/prompts/gptpro-literature-research-prompt.md` 核对最接近的参数区域下界、组合罚参数恒等式的来源和比较表。
- PPALA：核对问题类、驻点判据、有限步可行性与算法结构；不能预设其与本文在同一问题类上比较。
- LP-ALM、NR-LALM、GDPA：区分问题假设、更新方式和参数条件。LP-ALM 的参数对应目前是待核对的粗对应；固定 $\rho$ 的定量收益需要可比条件下的计算。
- β=1 引用中的 Zhang Lemma B.11 常数依赖，以及 arXiv v3 / NeurIPS 版本编号，仍保留为待核对项。

### 最后处理的编辑项

- `sections/Introduction.tex` 中 “oraccuracy $eps$-dependent” 笔误。
- `tools/refer.bib` 中 `zhang2020single` 与 `zhang2020smoothed` 重复条目，合并时同步实际引用。
- 主体与附录顺序确定后，决定 Organization 是否补充附录说明。
- GS 版本和向一般 Smoothed GDA / DS-GDA 的下界推广为可选事项，不作为当前必做任务。

## 5. 材料使用规则

- 当前定位和任务只在本文件维护。完成任务时更新对应条目，不在文件末尾追加与旧正文冲突的“最新状态”。
- `SESSION_HANDOFF_*.md`、`ddlalm-task-plan.md`、`ddlalm-research-questions.md`、下界讨论记录、Booming 白板与已完成提示词为历史资料，2026-10-26 移至仓库根目录 `memory/archive/notes/`。旧幻灯片、8 月 V2/RouteB 材料与旧版论文在 `memory/archive/` 的其他子目录。里面的旧标题、旧初值、章节号和任务不能自动恢复为当前要求。
- `notes/gpt-proofs/` 保存证明来源；`lb-proof-materials.md` 的 Part I 平台分支仍有用途，Part II 与 Part III 的适用关系按文件顶部说明读取。
- `appendix-a-audit-20261013.md`、`ddlalm-verification-20261001.md` 保存已有核查依据。本次进度整理不新增数学核查结论。
- `literature.md`、`lower-bound-references.md`、`writing-phrasebook.md` 分别用于文献总表、下界参考和英文表达来源。
- `notes/conversations/` 与 `notes/skills/` 按用户要求保留。历史对话与方法副本不自动成为当前执行指令；对话时间覆盖见该目录 README。
- 已撤回判断：不能由任意 oracle 下界推断本文的参数区域下界会被替代。同一问题类与度量下的 oracle 下界能向子族转移，但转移本身不增加下界的阶。

## 6. 同步范围

本地论文入口为 `overleaf/main.tex`；仓库根目录的旧论文副本（10-13 快照）已于 2026-10-26 删除。Overleaf 远端的文件与 `overleaf/` 目录对应（10-26 按文件内容核对）。GitHub 远端是 `github`（`luxuan846-oss/3-DDLALM`）；`origin` 是 Overleaf，不能混用。用户本次授权把笔记更新提交并推送 GitHub。Overleaf 不属于本次推送范围；远端实时状态应通过 Git 查询，不沿用历史交接中的提交号。

## 7. 后续研究线：加速与 Tikhonov（2026-10-25 起）

分工与顺序见 `notes/project/next-lines-plan-20261025.md`；问题表述与 GPT Pro 指令见 `notes/prompts/gptpro-tikhonov-eg-alm-prompt.md`、`notes/prompts/gptpro-acceleration-logic-20261026.md`。下表为 10-26 GPT Pro 第二轮结果经 Gemini 与 Claude 复核后的结论。

| 结论 | 状态 |
|---|---|
| 固定 $\rho>0$ 时 $\nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})=0$ 当且仅当 $\boldsymbol{\lambda}\in\partial h(\mathcal{A}(\mathbf{x}))$，KKT 关系精确。$\mathcal{D}_\rho$ 的对偶 Hessian 为 $-\rho^{-1}J_{\mathrm{prox}_{h/\rho}}$，曲率介于 $0$ 与 $1/\rho$。GPT 所称"固定 $\rho$ 留下 $1/\rho$ 偏差、选最小范数乘子需 $\rho_k\to\infty$"不成立 | 推导 |
| 固定 $s$ 时 Tikhonov 项只提供强单调性；算法 A、B 在有界步长下单步收缩因子为 $1-\Theta(1/s)$ | 已证（直接计算） |
| 不用 momentum，Tikhonov 或 anchoring 不能把中心步长放宽到 $\alpha\sim1/\sqrt{s}$ | 证据充分；针对算法 A、B 的下界待证 |
| Zhang–Xu（arXiv:2609.17973）的 $\sqrt{s}$ 增益来自对偶动量：带衰减的对偶梯度累加，窗口约 $\sqrt{Ls}$ 步；中心步长取 $\propto1/\sqrt{Ls}$ | 原文 (4.3)、(4.26)；纯对偶模态谱隙已数值核对 |
| Zhang–Xu Algorithm 1 直接作用于 $\mathcal{D}_\rho$（定义域 $\mathbb{R}^n\times\mathcal{Y}$，$\mathcal{Y}$ 为半径 $2L_h$ 的球），得到单循环、固定 $\rho$ 的 $O(\epsilon^{-5/2})$ $\epsilon$-KKT 复杂度。依据：附录 C Step 1–2 的约化；$\epsilon<L_h/\rho$ 时 $\epsilon$-GS 点位于 $\mathcal{Y}$ 内部 | 推断；初值量 $\bar\Delta_0$ 在 $\mathcal{I}(\mathbf{C},\Delta)$ 上一致有界待核 |
| Pan–Zheng–Li（arXiv:2609.14235v2）的 GS $\Omega(\epsilon^{-5/2})$ 直接转移到 $\mathcal{I}(\mathbf{C},\Delta)$ | 不成立：$g_3$ 的对偶二次项依赖 $\mathbf{x}$，其 oracle 不含 $\mathrm{prox}_h$ |
| 算法 B 的 Tikhonov 锚点为 $\boldsymbol{\mu}^k$。$\beta_k\equiv0$ 时选择目标为最小范数乘子；现行 $\beta_k=\theta_\mu/(k+k_0)$ 不可和，锚点跟随 $\boldsymbol{\lambda}^k$，没有选择效应 | 推导 |
| 纯 Tikhonov、$s_k\asymp k$、$\boldsymbol{\lambda}^\dagger\neq0$ 时 KKT 残差为 $\Theta(1/k)$；$o(1/k)$ 需要惯性项 | 推断；待对照 arXiv:2406.00852、2410.14369 原文 |

对两条线的影响：

- 线 1：$\epsilon^{-5/2}$ 上界本身接近"Zhang–Xu + 附录 C 约化"的推论。新意转向两处：momentum-free 族 $\Theta(\epsilon^{-3})$ 与对偶动量 $\epsilon^{-5/2}$ 的分离（EG 族不加动量时的下界待证）；带 $\mathrm{prox}_h$ oracle 的 $\Omega(\epsilon^{-5/2})$ 下界构造。
- 线 2：在 $\beta\equiv0$、$s_k\uparrow\infty$ 下提出，目标为局部正则条件下的最小范数乘子与 $O(1/k)$ 残差。Zhang–Xu 的对偶锚点同样固定在 $0$，可作为算法结构的起点。

缺失材料：`ChatGPT-核查算法与下界-20261026-0749.md` 与 `ChatGPT-文献核查与算法加速!-20261026-1052.md` 未入库，待放入 `notes/conversations/`。
