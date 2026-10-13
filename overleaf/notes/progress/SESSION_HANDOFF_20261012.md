# 会话交接：2026-10-12（论文重构与下界章节准备）

新会话先读本文件，再读 `notes/progress/PROJECT_STATUS.md` 和 `notes/project/lower-bound-references.md`。

## 1. 论文当前结构（`main.tex`，已推送 Overleaf，提交 8ab1ce6，之后 Overleaf 上删除了 AGENTS.md 等三个非论文文件）

标题：*Growing the Dual Regularization, Not the Penalty: A Fixed-Penalty Single-Loop Augmented Lagrangian Method for Nonconvex Composite Optimization*

| 节 | 文件 | 状态 |
|---|---|---|
| 1 引言 | `sections/Introduction.tex` | 问题 (Q)、三条贡献、比较表、Organization 已重写；研究路线表已删；原 Q2/Q3 留为末尾注释（移到结论） |
| 2 Preliminaries | `sections/Preliminaries.tex` | 完成，见第 2 节 |
| 3 下界陈述 | `sections/LowerBound.tex` | 定理 `thm:lower-bound`、推论 `cor:effective-penalty`、Remark `rem:lb-initialization`、与 GDA 的嵌入（`prop:reduction`、`prop:embedding`） |
| 4 下界证明 | `sections/LowerBoundProof.tex` | **空，下一步要写** |
| 6 上界 | `sections/UpperBound.tex` | 由原 Methodology + Convergence_analysis 合并，重复定义已清理，`\iffalse` 旧稿已删；开头陈述水平有界假设 `ass:level-boundedness` 和待办 TODO |

已删除的旧文件（备份在 `/tmp/deleted_sections/`，重启可能丢失）：Methodology.tex、Convergence_analysis.tex、MainResult.tex。

## 2. 第 2 节的定义（已定稿，写证明时直接引用这些 label）

- `def:problem-class`：$\mathcal I(\mathbf C,\Delta)$，三元组 $(f,\calA,h)$，`ass:smoothness` + `ass:h`（$h$ 实值、凸、$L_h$-Lipschitz）+ $F(\mathbf 0)-\inf F\le\Delta$；水平有界**不在**类内
- `def:eps-kkt`（$\mathcal R_{\rm KKT}$，`eq:kkt-residual`）、`def:eps-gs`（$\calG$）、`prop:kkt-gs`：$\calG=\min_{\by\in\partial h^*(\bq)}\mathcal R_{\rm KKT}$
- `def:oracle-model`：$\mathcal O_{f,\calA}$、$\mathcal O_h$
- `eq:reduced-al`（$\calD_\rho$）、`eq:prox-multiplier`（$\by(\bx,\blmbd)$、$\bq(\bx,\blmbd)$）、`eq:potential`（$\mathcal P_s$）
- `def:splalm`：常数 $(\alpha,\beta)$，**零初值**，四步更新 `eq:splalm-updates`，输出 $(\bx^{k+1},\by^{k+1},\bq^k)$；`def:algorithm-family`：$\calC_\theta$
- `def:complexity-measure`：$T^{\rm KKT}_\epsilon$、$T^{\rm GS}_\epsilon$（用 $K$ 计迭代次数），$\inf_{(\alpha,\beta)}\sup_I$；$T^{\rm GS}\le T^{\rm KKT}$
- `rem:family-not-oracle`：$\calC_\theta\subset\mathcal A_{\det}$，三点：范围、一致性、传递方向
- 2.5 节 `lem:effective-penalty`：$\max_{\blmbd}\mathcal P_s=\calD_{\rho+s}(\bx,\bmu)+\frac1{2\gamma}\|\bx-\bz\|^2$；`tab:special-cases`（$\beta=0$ 二次罚 / PSGDA 型，$0<\beta<1$ DS-GDA 型，$\beta=1$ ALM / Smoothed GDA 型）

## 3. 下一步：写第 4 节（困难实例与证明）

证明材料全部来自 GPT Pro，分三份，最终定理由三块拼成：
1. **平台实例**（小 $\alpha\le1024\varpi\epsilon^2$，$A\equiv0$，零初值）：来自 10-01 版第 2 节
2. **零初值旋转实例**（大 $\alpha$，$\beta>0$）：平移中心 $\bx_c,\blmbd_c$ 使四个初值为零；谱分解 $\mathcal Q(v)=(v^2+\nu v+\nu)[(v+D)(v+V)-\vartheta(v+\alpha)]$；快分量瞬态估计；$R_k\ge\frac76\epsilon$。来自"零初值版本"
3. **$\beta=0$ Huber 实例**（引理 4，$q_h=2s+1$）：来自"零初值版本"
4. **常数与门槛**：$c_1=\min\{\frac1{32}\sqrt{\tau/(\eta C_\chi)},\frac1{64B_\chi},\frac1{16(3+\tau^{-1})}\}$，$c_2(\Delta)=\min\{\frac1{64},\frac1{32\sqrt\varpi},\frac\Delta{12},\frac{\sqrt\Delta}2,\sqrt{\Delta/(64\gamma)}\}$；瞬态常数 $C^\sharp_{\rm tr},C^\sharp_{\rm du},C^\sharp_{\rm res}$。来自"$s$ 一致版本"（ChatGPT 分享 https://chatgpt.com/share/6acd53fb-94ac-83e9-b1c4-1f5d54364aab）

**三份材料已合并存为 `notes/gpt-proofs/lb-proof-materials.md`（Part I：10-01 版；Part II：零初值版；Part III：$s$ 一致版），文件开头说明了三块如何拼成最终定理。**

数值核对已做（2026-10-12，300 组随机参数，从零初值实际运行 SPLALM，$\min_k R_k/\epsilon\ge2.63$，prox 始终取零分支）；用户要求之后不再做数值验证。

写作约定：
- 结构参照 Li et al. 2602.14185 §5 和 Pan et al. 2609.14235 §6：实例条件 → 构造 → 逐条验证，每个分支一小节
- 记号避免冲突：$J\to\Upsilon$，常数 $K\to\varpi:=\max\{1,4\tau,4\gamma\tau\}$，复增益 $L\to\Gamma$，平台中心 $d\to x_\star$，递推矩阵 $\mathbb T$，复数嵌入 $\iota(c)=(\Re c,\Im c)$
- 定理中删去 $\bar\rho$（$c_1$ 不依赖它）
- 用户偏好"先输出看，再写入文件"；改稿前先给方案

## 4. 未决事项

- GS 版本下界依赖"严格凸扰动引理"，尚未写；引言贡献 2 中相应句子带 TODO 注释
- 上界：主上界应为同族常数版本 $s=\Theta(1/\epsilon)$（PROJECT_STATUS 待办 1），证后与 $c_1$ 对照；现有 `thm:main`（递增 $s_k$）作为变体
- 引言 $h:\RR^m\to\RR\cup\{+\infty\}$ 与 Lipschitz 假设冲突，待统一
- `refer.bib`：Zhang–Xiao–Sun–Luo 重复三次；Zhang–Xu 作者名 Minghao/Minhao
- 第 2 节 `def:eps-kkt` 前一句被用户在 Overleaf 上标为 `\red{}`，待处理
- 本地与 Overleaf 的关系：Overleaf 仓库在 `3_DDLALM/`（git 根目录），工作副本在 `3_DDLALM/overleaf/`；推送时把 `main.tex`、`sections/`、`tools/refer.bib`、`tools/shared.tex` 同步到根目录再提交，先 `git pull --ff-only` 并逐行核对远端改动
