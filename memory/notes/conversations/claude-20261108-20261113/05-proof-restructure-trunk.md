# 05-proof-restructure-trunk

- **Source session**: `2d57d6fc = bcee9312 (shared trunk)`
- **Span (local time)**: 2026-11-12 15:05 to 2026-11-12 17:06
- **User turns**: 67

---

## User (2026-11-12 15:05)

老大，交接内容已写入 [PROJECT_STATUS.md](overleaf/notes/progress/PROJECT_STATUS.md) §4 第 6 条"Fast LRALM 证明重构"，新对话从这一条读起即可。

这一条记了五部分：

- **已做的文件改动**：删除旧附录 D 和 E；`prop:curvature-smoothness` 的证明移到 Appendix B 末尾；在 `sections/Acceleration.tex` 新增残差分解引理，目前只有陈述。
- **你定下的证明结构**：残差分解放最前，拆成四个量，后面的引理各控制一项，证明全部写进 `appendix/AccelerationProof.tex`。
- **路线 2（待落实）**：把 $c_e$ 改成常数，让下降不等式变成步长形式。改完要重新核对 G2.4 的系数。
- **已定的写法和遗留问题**：对偶步长条件统一成 $\tau L_\lambda\le\frac{1}{2}$；乘子有界性按次梯度加权和来讲；常数段落改成五个常数，替换稿还没写进文件；$\gamma$ 有两个条件不一致。
- **查新补充**：proximal-AltGDAm 没有近端中心，代入后是 $\epsilon^{-23/6}$；SSNAL 不属于对偶二阶方法。

有两点和状态文件前几节对不上，新对话里要留意：§2 第 5 条和 §3 的表格仍把旧附录 D、E 列为现有内容，我没有改这两处。 你现在看一下

---

## Assistant (2026-11-12 15:06)

Shell 是 zsh，改用 bash 重跑，同时编译一次查未定义引用。

老大，乘子有界引理的条件可以合并成一条：$\tau L_\lambda\le\frac{1}{2}$，其中 $L_\lambda=\frac{1}{\rho}+\frac{1}{s}$。我已把这个改动写进陈述和证明。交接内容和文件核对过，大体一致。

## 乘子有界引理的参数

**引理只需要 $\nu:=\tau\left(\frac{1}{\rho}+\frac{1}{s}\right)\le\frac{1}{2}$ 这一条。** 我逐个查了证明里用到参数的地方：

- $a=1-\nu\in[\frac{1}{2},1)$ 只依赖 $\nu$。
- 外推系数要落在 $(0,1)$，需要 $s\gt\tau$。这一点由 $\frac{\tau}{s}\le\nu\le\frac{1}{2}$ 推出。
- 常数 $C_\lambda=\max\{4,\sqrt{8\rho/\tau}\}$ 只用到 $\nu\ge\tau/\rho$。
- 三种情形里的估计 $\sin^2\phi\ge\frac{\nu}{2}$、$1-R\ge\frac{\nu}{2}$ 和 $1-R\gt\frac{\sqrt{\nu}}{2}$ 都与 $s\ge4\tau$ 无关。

所以 $s\ge4\tau$ 只在其他地方保证 $\varsigma\le\frac{1}{2}$，这个引理用不到它。

我改了两处：

- [Acceleration.tex:185-186](overleaf/sections/Acceleration.tex#L185-L186)：条件换成 `\tau\left(\frac1\rho+\frac1s\right)\le\frac12`。
- [AccelerationProof.tex:12](overleaf/appendix/AccelerationProof.tex#L12)：相应改成 "By assumption, $0\lt\nu\le1/2$, so $a\in[1/2,1)$."

`eq:b2-prime-stepsizes` 里的 $\tau\le\rho/4$ 和 $s\ge4\tau$ 合起来能推出新条件，所以下游的引用都不受影响。改完之后我没有重新编译。$L_\lambda$ 要等常数段落写好后才有定义，到时可以把条件写成 $\tau L_\lambda\le\frac{1}{2}$。

## 交接内容的核对

- **两条证明核对无误。** 乘子有界引理的证明我逐行推过，三种情形和最后的常数都对。残差分解两个不等式我也独立推了一遍。第一式的系数已经是 $\lvert\frac{1}{\eta}-\frac{1}{\gamma}\rvert+L_{\mathcal{D},\mathbf{x}}$，取 $\eta=\gamma$ 时就等于 $L_{\mathcal{D},\mathbf{x}}$，"收紧系数"这一条在文件里已经落实。
- **删掉附录 D、E 后没有留下悬空引用。** 编译没有报错，也没有未定义引用。旧标签只在 [Preliminaries.tex:97](overleaf/sections/Preliminaries.tex#L97) 的注释里出现一次 `ass:level-boundedness`。
- **交接里没记的两处：**
  - [Acceleration.tex:192](overleaf/sections/Acceleration.tex#L192) 的 `\end{lemma}` 后面多了一个句点。
  - 第 69–72 行仍是草稿文字，其中 `\mu_gamma`、`L\lambda` 写在数学环境外面。这次编译没有报错，但这几行没有出现在 PDF 里，原因我没有查。不管怎样，这几行都要被五个常数的替换稿取代。
- **状态文件过期的位置：** 除了你说的 §2 第 5 条和 §3 表格，§2 第 5 条提到的 `thm:main` 在稿件里也已经不存在。

---

## User (2026-11-12 15:08)

目前是报错的。

---

## Assistant (2026-11-12 15:09)

老大，报错来自旧稿第 69–72 行的草稿文字。你现在的版本已经把这几行换成常数段落，在 `/tmp` 下用干净副本重新编译，**0 个错误，没有未定义的引用或引文**。

- **原因**：旧草稿里的 `\mu_gamma` 和 `L\lambda` 写在数学环境外面，pdflatex 报了 4 处 `Missing $ inserted` 和一处 `Bad math environment delimiter`，都在第 71–73 行。
- **更正**：我上一条说"编译没有报错"是错的。那次用的是 `latexmk`，而副本里带着旧的 `main.pdf` 和辅助文件，所以这次失败没有暴露出来。这一次我先删掉 `aux`、`log`、`pdf`，再用 pdflatex 和 bibtex 从头编译，结果才可靠。
- **没有生效的修改**：我原本想把那几行注释掉，但写入前的匹配检查失败了，因为文件已经被你改过，所以那次修改没有写进去。乘子有界引理那处修改还在当前文件里（第 185–186 行）。
- **如果编辑器还显示报错**：多半是 LaTeX Workshop 留下的旧结果，删掉 `overleaf/` 下的 `main.aux` 后重新编译即可。

当前稿件里有一对 `{\color{red}`（第 154 行）和 `}`（第 183 行），括号配对正确，不影响编译。

---

## User (2026-11-12 15:16)

老大，乘子有界性的证明思路分五步：

1. **把对偶步写成线性递推。** 记 $a=1-\tau L_\lambda$。由 $\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s=\frac{\mathbf{q}-\boldsymbol{\lambda}}{\rho}-\frac{\boldsymbol{\lambda}}{s}$，有 $\boldsymbol{\lambda}^{k+1}=a\bar{\boldsymbol{\lambda}}^k+\frac{\tau}{\rho}\mathbf{q}^k$。再代入外推 $\bar{\boldsymbol{\lambda}}^k=(1+\theta)\boldsymbol{\lambda}^k-\theta\boldsymbol{\lambda}^{k-1}$：

$$
\boldsymbol{\lambda}^{k+1}=a(1+\theta)\boldsymbol{\lambda}^k-a\theta\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k,\qquad\lVert\mathbf{q}^k\rVert\le L_h
$$

2. **展开成次梯度的加权和。** 从零初值出发，

$$
\boldsymbol{\lambda}^k=\frac{\tau}{\rho}\sum_{i=0}^{k-1}c_{k-1-i}\,\mathbf{q}^i
$$

   权重 $c_j$ 满足与第 1 步相同的递推，初值为 $c_{-1}=0$、$c_0=1$。所以 $\lVert\boldsymbol{\lambda}^k\rVert\le\frac{\tau}{\rho}L_h\sum_j\lvert c_j\rvert$。

3. **估计权重的 $\ell_1$ 范数。** 特征多项式 $\zeta^2-a(1+\theta)\zeta+a\theta$ 的根模长不超过 $\sqrt{a}\lt1$。按 $\theta$ 分三段：
   - 实根时权重全为正，和恰为 $\frac{1}{\tau L_\lambda}$；
   - 复根且 $\theta$ 离 1 较远时，用根模长界定；
   - $\theta$ 接近 1 时，用辐角界定。

   三段合起来，当 $\tau L_\lambda\le\frac{1}{2}$ 时，对所有 $\theta\in[0,1]$ 都有

$$
\sum_j\lvert c_j\rvert\le\max\left\{\frac{4}{\tau L_\lambda},\ \frac{2\sqrt{2}}{(\tau L_\lambda)^{3/2}}\right\}
$$

4. **去掉对 $s$ 的依赖。** 代回第 2 步，并用 $\frac{\tau}{\rho}=\frac{s}{\rho+s}\tau L_\lambda$：

$$
\lVert\boldsymbol{\lambda}^k\rVert\le\frac{s}{\rho+s}\max\left\{4,\ \frac{2\sqrt{2}}{\sqrt{\tau L_\lambda}}\right\}L_h\le\max\left\{4,\ \sqrt{\frac{8\rho}{\tau}}\right\}L_h=C_\lambda L_h
$$

   最后一步用了 $\frac{s}{\rho+s}\le1$ 和 $\tau L_\lambda\ge\frac{\tau}{\rho}$。

5. **外推点。** 由 $\theta\le1$，$\lVert\bar{\boldsymbol{\lambda}}^k\rVert\le(1+2\theta)C_\lambda L_h\le3C_\lambda L_h$。
纵观全局 我们先把 
不加外推时（$\theta=0$），权重全为正且总和不超过 $\frac{1}{\tau L_\lambda}$，$\boldsymbol{\lambda}^k$ 就是次梯度的凸组合。加了外推，部分权重变负，所以要估计 $\ell_1$ 范数，常数也因此多出 $\sqrt{\rho/\tau}$。 先输出第一步

---

## Assistant (2026-11-12 15:17)

第一步的 LaTeX 草稿放在下面。证明开头先放你说的"纵观全局"那段，说明没有外推时乘子是次梯度的凸组合。动量系数沿用正文已有的 $\varsigma=\sqrt{\tau/s}$，写成 $\frac{1-\varsigma}{1+\varsigma}$，不用 $\theta$。

另外，你在 [Acceleration.tex:129](overleaf/sections/Acceleration.tex#L129) 写的 `\tauL_\lambda` 会报 `Undefined control sequence`，要在 `\tau` 后面加空格，改成 `\tau L_\lambda`。我还没有动这处。

```latex
\begin{proof}[Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}]
If the extrapolation coefficient were zero, the dual update would read
\(\blmbd^{k+1}=(1-\tau L_\lambda)\blmbd^k+\frac{\tau}{\rho}\bq^k\). Then
\(\blmbd^k\) would be a combination of \(\bq^0,\ldots,\bq^{k-1}\) with
nonnegative weights summing to at most \((\rho L_\lambda)^{-1}\le1\), and
\(\|\blmbd^k\|\le L_h\) would follow. Extrapolation makes some of these
weights negative. We therefore bound the \(\ell_1\)-norm of the weights,
which produces the additional factor \(\sqrt{\rho/\tau}\) in \(C_\lambda\).

\emph{Step 1: a linear recursion.}
Let \(a:=1-\tau L_\lambda\) and \(\varsigma:=\sqrt{\tau/s}\). Since
\(\tau L_\lambda\le\frac12\), we have \(a\in[\frac12,1)\). Moreover,
\(\varsigma^2=\tau/s\le\tau L_\lambda\le\frac12\), so the extrapolation
coefficient \((\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})
=(1-\varsigma)/(1+\varsigma)\) lies in \((0,1)\).
By~\eqref{eq:prox-multiplier},
\(\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
=(\bq^k-\bar{\blmbd}^k)/\rho-\bar{\blmbd}^k/s\). Hence the dual step reads
\[
    \blmbd^{k+1}=a\bar{\blmbd}^k+\frac{\tau}{\rho}\bq^k.
\]
Substituting
\(\bar{\blmbd}^k=\blmbd^k+\frac{1-\varsigma}{1+\varsigma}
(\blmbd^k-\blmbd^{k-1})\) gives
\[
    \blmbd^{k+1}
    =\frac{2a}{1+\varsigma}\blmbd^k
    -\frac{a(1-\varsigma)}{1+\varsigma}\blmbd^{k-1}
    +\frac{\tau}{\rho}\bq^k,
    \qquad
    \|\bq^k\|\le L_h,
\]
where the bound on \(\bq^k\) follows from
\(\bq^k\in\partial h(\by^{k+1})\) and Assumption~\ref{ass:h}.
```

还有一处你的提纲和草稿不一致。提纲里"权重总和不超过 $\frac{1}{\tau L_\lambda}$"指的是系数 $c_j$ 的和。乘上前面的因子 $\frac{\tau}{\rho}$ 之后，实际的总权重是 $\frac{1}{\rho L_\lambda}=\frac{s}{\rho+s}\le1$，也就是草稿第一段用的数。凸组合的说法以后一个数为准。

---

## User (2026-11-12 15:17)

$a$ 没必要，直接写 $1-\tau L_\lambda$ 即可。第 1 步改成：

$$
\boldsymbol{\lambda}^{k+1}=(1-\tau L_\lambda)\bar{\boldsymbol{\lambda}}^k+\frac{\tau}{\rho}\mathbf{q}^k
$$

$$
\boldsymbol{\lambda}^{k+1}=(1-\tau L_\lambda)(1+\theta)\boldsymbol{\lambda}^k-(1-\tau L_\lambda)\theta\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k
$$

第 3 步的特征多项式写成 $\zeta^2-(1-\tau L_\lambda)(1+\theta)\zeta+(1-\tau L_\lambda)\theta$，根的模长不超过 $\sqrt{1-\tau L_\lambda}$。

$\theta$ 作为乘子的动量系数可以保留，但正文里 $\theta$ 已经表示参数组 $(\rho,s,\gamma,\eta,\tau)$，用于 $\mathrm{LRALM}_{\theta,\alpha,\beta}$ 和 $\mathcal{C}_\theta$。写进论文时得换一个字母，或者在证明里直接写 Algorithm 6.1 中的系数 $\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}$。我也没有必要写引出a

动量系数可以直接写成 thta_m????????

---

## Assistant (2026-11-12 15:17)

可以用 $\theta_{\mathrm{m}}$。我检索了全稿，带下标的 $\theta$ 只在 [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex) 出现，就是现在的 `\theta_{\mathrm m}`，和别处没有记号冲突。

- **潜在误读**：正文里 $\theta=(\rho,s,\gamma,\eta,\tau)$ 是一个参数组，读者可能把 $\theta_{\mathrm{m}}$ 读成这个参数组的某个分量。
- **避免误读的写法**：第一次出现时直接写成定义式，如下。

```latex
\theta_{\mathrm m}:=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}\in(0,1)
```

  这样一眼可见它是 Algorithm 6.1 的外推系数。这个记号只在附录证明里使用，正文不出现。
- **取值范围**：由 $\tau L_\lambda\le\frac{1}{2}$ 可得 $\frac{\tau}{s}\le\frac{1}{2}$，所以 $\theta_{\mathrm{m}}\gt0$。第 3 步讨论复根情形时，要用到 $1-\theta_{\mathrm{m}}\lt1$。

照这个写法，第 1 步的递推是

$$
\boldsymbol{\lambda}^{k+1}=(1-\tau L_\lambda)(1+\theta_{\mathrm{m}})\boldsymbol{\lambda}^k-(1-\tau L_\lambda)\theta_{\mathrm{m}}\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k
$$

---

## User (2026-11-12 15:18)

或者换一个符号呢

---

## Assistant (2026-11-12 15:19)

换字母的话，我建议用 $\omega$。备选字母要么已经被占用，要么形状容易混淆，最后剩下的就是 $\omega$ 和"不加新符号"两种写法。我检索了 `sections/`、`appendix/` 和 B2′ 的推导笔记：

| 候选 | 现状 | 问题 |
|---|---|---|
| $\varpi$ | 稿件里没有出现 | G2 笔记里 $\varpi_k$ 是 G2.4 的余量项，移植下降引理时会用到 |
| $\upsilon$ | 稿件里没有出现 | G2 笔记里 $\upsilon=\gamma L_{\mathcal{D},\mathbf{x}}$；形状接近证明里已经用的 $u$ |
| $\iota$、$\varrho$ | 稿件里没有出现 | 分别像 $i$ 和 $\rho$ |
| $\omega$ | 附录 A 用了 $\omega$，附录 C 有 $\omega_s$ | 两处都是局部定义，和本附录不重叠 |

- **推荐用 $\omega$。** Nesterov 动量系数常记作 $\omega$。它在附录 A、C 都是局部记号，在本附录重新定义不会混淆。定义写成：

```latex
\omega:=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}\in(0,1)
```

  第 1 步的递推变成

$$
\boldsymbol{\lambda}^{k+1}=(1-\tau L_\lambda)(1+\omega)\boldsymbol{\lambda}^k-(1-\tau L_\lambda)\omega\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k
$$

- **不加新符号的写法。** 正文已经定义了 $\varsigma=\sqrt{\tau/s}$，系数就是 $\frac{1-\varsigma}{1+\varsigma}$，并且 $1+\frac{1-\varsigma}{1+\varsigma}=\frac{2}{1+\varsigma}$。递推里两个系数分别写成 $\frac{2(1-\tau L_\lambda)}{1+\varsigma}$ 和 $\frac{(1-\tau L_\lambda)(1-\varsigma)}{1+\varsigma}$。这样不增加记号，但第 3 步的三段分析会写长一些：分段阈值要写成 $\frac{2\varsigma}{1+\varsigma}\le\sqrt{\tau L_\lambda}$。

---

## User (2026-11-12 15:19)

\begin{proof}[Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}]
By the update of $\bl$ \eqref{}, we have
$$\boldsymbol{\lambda}^{k+1}=(1-\tau L_\lambda)(1+\theta_{\mathrm{m}})\boldsymbol{\lambda}^k-(1-\tau L_\lambda)\theta_{\mathrm{m}}\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k$$.

By~\eqref{eq:prox-multiplier},
\(\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
=(\bq^k-\bar{\blmbd}^k)/\rho-\bar{\blmbd}^k/s\), so the dual update reads
\[
    \blmbd^{k+1}
    =a\bar{\blmbd}^k+b\bq^k
    =a(1+\theta_{\mathrm m})\blmbd^k-a\theta_{\mathrm m}\blmbd^{k-1}+b\bq^k,
    \qquad \|\bq^k\|\le L_h.
\] ok这个是第一步润色一下  我需要你的输出，把1-5步写到前面，写出我们现在是第几步

---

## Assistant (2026-11-12 15:19)

下面是证明的开头部分，可以替换掉 `\begin{proof}` 到第一个 `\]` 之间的内容。第一段先列出五步，接着写第 1 步。**当前写到第 1 步。**

你的草稿里有两处会出问题：

- `\bl` 在 `tools/shared.tex` 里没有定义，编译会报错，下面改用 `\blmbd`。
- `\eqref{}` 是空引用。Algorithm 6.1 的对偶步没有公式标签，所以下面写成 "the dual step of Algorithm~\ref{alg:b2-prime}"。

另外，`$$...$$` 后面紧跟的句点会单独落到下一行，下面改为 `\[...\]`，句点放进公式内。

```latex
\begin{proof}[Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}]
Let
\(\theta_{\mathrm m}:=(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})\)
denote the extrapolation coefficient in Algorithm~\ref{alg:b2-prime}.
The proof proceeds in five steps.
Step~1 writes the dual step as a linear recursion in \(\blmbd^k\).
Step~2 expands \(\blmbd^k\) as a weighted sum of the subgradients
\(\bq^0,\ldots,\bq^{k-1}\).
Step~3 bounds the \(\ell_1\)-norm of the weights.
Step~4 combines Steps~2 and~3 into a bound on \(\|\blmbd^k\|\) that is
independent of \(s\).
Step~5 transfers the bound to the extrapolated multiplier
\(\bar{\blmbd}^k\).
Without extrapolation, the weights in Step~2 are nonnegative and sum to at
most \((\rho L_\lambda)^{-1}\le1\), so \(\blmbd^k\) is a convex combination
of \(\zero,\bq^0,\ldots,\bq^{k-1}\). Extrapolation makes some weights
negative, which is why Step~3 bounds their \(\ell_1\)-norm. This step is the
source of the factor \(\sqrt{\rho/\tau}\) in \(C_\lambda\).

\emph{Step 1: linear recursion.}
Since \(\tau/s\le\tau L_\lambda\le\frac12\), we have
\(\theta_{\mathrm m}\in(0,1)\) and \(1-\tau L_\lambda\in[\frac12,1)\).
By~\eqref{eq:prox-multiplier},
\[
    \nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
    =\frac{\bq^k-\bar{\blmbd}^k}{\rho}-\frac{\bar{\blmbd}^k}{s},
\]
so the dual step of Algorithm~\ref{alg:b2-prime} reads
\[
    \blmbd^{k+1}=(1-\tau L_\lambda)\bar{\blmbd}^k+\frac{\tau}{\rho}\bq^k.
\]
Substituting
\(\bar{\blmbd}^k=(1+\theta_{\mathrm m})\blmbd^k
-\theta_{\mathrm m}\blmbd^{k-1}\) yields
\[
    \blmbd^{k+1}
    =(1-\tau L_\lambda)(1+\theta_{\mathrm m})\blmbd^k
    -(1-\tau L_\lambda)\theta_{\mathrm m}\blmbd^{k-1}
    +\frac{\tau}{\rho}\bq^k,
    \qquad k\ge0.
\]
Moreover, \(\bq^k\in\partial h(\by^{k+1})\) and \(h\) is \(L_h\)-Lipschitz
by Assumption~\ref{ass:h}, so \(\|\bq^k\|\le L_h\) for every \(k\ge0\).
```

第一段说的"凸组合"指的是 $\theta_{\mathrm{m}}=0$ 时的情形。那时第 $j$ 个权重是 $\frac{\tau}{\rho}(1-\tau L_\lambda)^j$，全部权重的和不超过 $\frac{1}{\rho L_\lambda}=\frac{s}{\rho+s}$。

---

## User (2026-11-12 15:19)

omgea把  $\varsigma=\sqrt{\tau/s}$，这个我怀疑都不需要引入这个符号 这个是条件数吧

---

## Assistant (2026-11-12 15:20)

$\varsigma$ 和条件数相关，但并不就是条件数的倒数。我建议保留这个符号：下降引理的证明里它是 Nesterov 外推的压缩率，G2、G3 笔记中分别用了约 50 次和 45 次。外推系数改用 $\omega$ 没有问题。

**$\varsigma$ 和条件数的关系**

在 $\boldsymbol{\lambda}$ 方向上，$\mathcal{P}_s$ 是 $\frac{1}{s}$-强凹、$L_\lambda$-光滑的，所以对偶条件数是 $\kappa_\lambda=sL_\lambda=1+\frac{s}{\rho}$。

$\varsigma^2=\frac{\tau}{s}$ 等于对偶步长乘以强凹模数，也就是标准 Nesterov 压缩率 $\sqrt{\mu/L}$ 中把 $\frac{1}{L}$ 换成步长 $\tau$。只有取 $\tau=\frac{1}{L_\lambda}$ 时，才有 $\varsigma=\kappa_\lambda^{-1/2}$。在现在的条件 $\tau L_\lambda\le\frac{1}{2}$ 下，只能得到

$$
\varsigma^2=\frac{\tau}{s}\le\frac{1}{2sL_\lambda}=\frac{1}{2\kappa_\lambda}
$$

所以把它写成条件数并不准确，$\varsigma$ 保留了步长 $\tau$ 这个自由度。

**$\varsigma$ 是否需要引入**

- **乘子有界引理的证明里不需要。** 用 $\omega:=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}$ 就够了，证明里只用到 $\omega\in(0,1)$。
- **正文现在用了 8 次。** 位置包括 $\alpha=\kappa_\alpha\varsigma$、定理证明中的 $\sqrt{\Delta_{\mathcal{W}}/(\varsigma K)}$、$\varsigma\le\frac{1}{2}$ 等，都可以改写成 $\sqrt{\tau/s}$。
- **下降引理的证明里需要。** G2.4 移植到附录后，$\mathcal{E}_k$ 每步按 $1-c\varsigma$ 的比例衰减，各处系数核对也都以 $\varsigma$ 为单位。去掉 $\varsigma$ 的话，这几十处都要写成 $\sqrt{\tau/s}$，可读性变差。

两者之间有一个关系，第 3 步分段时可以直接用：

$$
\omega=\frac{1-\varsigma}{1+\varsigma}
$$

---

## User (2026-11-12 15:26)

你没懂我的意思  The function \(\blmbd\mapsto\mathcal P_s(\bx,\blmbd;\bz,\zero)\) is
\(1/s\)-strongly concave. Taking \(\mu=1/s\) and replacing \(1/L\) by the
dual stepsize \(\tau\) gives the extrapolation coefficient
\[
    \omega:= \frac{1-\sqrt{\tau/s}}{1+\sqrt{\tau/s}}
    =\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}.
\]

We refer to the resulting method as Fast LRALM (Algorithm~\ref{alg:b2-prime});
it lies outside \(\calC_\theta\) 
% because it incorporates Nesterov
% extrapolation in the dual variable and evaluates both partial gradients of
% \(\mathcal P_s\) at the extrapolated multiplier \(\bar{\blmbd}^k\), whereas
% every method in \(\calC_\theta\) evaluates \(\nabla\mathcal P_s\) at the
% current multiplier \(\blmbd^k\) without extrapolation. Extrapolation is
% applied only to the multiplier sequence, while the primal variable is updated
% by a plain gradient step.

\begin{algorithm}[H]
    \caption{Fast LRALM}
    \label{alg:b2-prime}
    \small
    \begin{algorithmic}[1]
        \STATE \textbf{Input:} Parameters \(\rho,s,\gamma,\eta,\tau>0\),
        \(\alpha\in(0,1]\); iteration limit \(K\).
        \STATE \textbf{Initialize:} \(\bx^0=\bz^0=\zero\),
        \(\blmbd^{-1}=\blmbd^0=\zero\).
        \FOR{\(k=0,1,\ldots,K-1\)}
            \STATE \(\bar{\blmbd}^{k}=\blmbd^k+
           \omega
            (\blmbd^k-\blmbd^{k-1})\).我现在就这样修改 你看下

---

## Assistant (2026-11-12 15:26)

这个改法可以，$\omega$ 不和稿件里的记号冲突，附录 A 只用了带下标的 $\omega_x$。还有四处要处理：

1. **句子没有结束。** "it lies outside \(\calC_\theta\)" 后面的内容都被注释掉了，这句话缺句点。保留的部分要写成 "...it lies outside \(\calC_\theta\)."，否则编译出来会直接接上算法环境。
2. **附录要同步改。** [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex) 里仍在用 `\theta_{\mathrm m}`，共 15 处，第 10 行还单独定义了一次。这些全部改成 `\omega`，删掉第 10 行的定义，改为引用正文。
3. **$\varsigma$ 可以提前定义。** 正文第 145 行定义了 $\varsigma=\sqrt{\tau/s}$，第 28 行又把同一个式子 $\sqrt{\tau/s}$ 写了两遍。可以在第 28 行就写成下面这样，第 145 行只保留 $\alpha=\kappa_\alpha\varsigma$：

```latex
\omega:=\frac{1-\varsigma}{1+\varsigma}
=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}},
\qquad \varsigma:=\sqrt{\tau/s}.
```

4. **$\mu$ 的含义有重叠。** "Taking \(\mu=1/s\)" 里的 $\mu$ 是 Nesterov 公式中的强凹模数。稿件里同时有对偶中心 $\boldsymbol{\mu}$ 和 $\mu_\gamma$，但一个加粗、一个带下标，读者能区分，这处可以不改。

要不要我把附录里的 $\theta_{\mathrm{m}}$ 全部换成 $\omega$？

---

## User (2026-11-12 15:27)

可以

---

## Assistant (2026-11-12 15:28)

老大，我把附录里的 `\theta_{\mathrm m}` 全部换成了 `\omega`，共 16 处，第 10 行原来的单独定义改成引用正文里的定义。从干净副本编译，**没有报错**，附录里也不再出现 `theta`。

- **改动**：[AccelerationProof.tex:9-10](overleaf/appendix/AccelerationProof.tex#L9-L10) 改为 "Let \(\omega\) be the extrapolation coefficient in Algorithm~\ref{alg:b2-prime}."
- **15 个未定义引用**：原因是 [main.tex:74-76](overleaf/main.tex#L74-L76) 里附录 A、B、C 的 `\input` 现在被注释掉了，`app:curvature-smoothness`、`app:upper-beta1` 等标签都定义在这三个文件中。这次替换不会产生未定义引用；三个文件恢复后，这些引用就会正常解析。
- **还没动的地方**：第 1 步之后的证明仍是旧写法，`a`、`\nu`、`u` 等记号还在，并且有 `\omega` 和 `a` 混用的情况。这部分等改写第 2–5 步时一起处理。

---

## User (2026-11-12 15:31)

你理解错我意思了不是 你在证明里写 而是你输出的时候 写

---

## Assistant (2026-11-12 15:31)

明白了，五步的路线图和"现在是第几步"是写给你看的，不该放进证明。我已经从 [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex) 里删掉了这两部分：一是列出五步的那段，连同"Without extrapolation"那几句；二是 `\emph{Step 1: linear recursion.}` 这个标签。证明现在从 $\omega$ 的取值范围直接写到第 1 步的递推。

**进度：第 1 步已写入证明，共 5 步。**

1. **把对偶步写成线性递推**：已完成。
2. **把 $\boldsymbol{\lambda}^k$ 展开成次梯度的加权和**：下一步。
3. **估计权重的 $\ell_1$ 范数**：分三段讨论。
4. **代回后得到与 $s$ 无关的界**。
5. **推到外推点 $\bar{\boldsymbol{\lambda}}^k$**。

第 1 步后面的内容还是旧写法，用的是 $a$、$\nu$、$u$，后面每写完一步就替换掉对应的旧段落。

---

## User (2026-11-12 15:35)

我们的逻辑不是现有参数范围吧 为什么要这么写呢？

---

## Assistant (2026-11-12 15:35)

你说得对，第 1 步是纯代数推导，用不到任何参数范围，这两句放在开头不合适。

- **$\omega\in(0,1)$ 和 $1-\tau L_\lambda\in[\frac{1}{2},1)$ 都是第 3 步才用到的**：前者用于把外推系数按大小分段，后者用于确定特征根的位置和模长 $\sqrt{1-\tau L_\lambda}\lt1$。
- **放在开头的问题**：读者在第 1 步就看到范围条件，却要到第 3 步才明白它的用途，这样会打断第 1 步"代入化简"的主线。
- **建议**：证明直接从 "By~\eqref{eq:prox-multiplier}" 开始，这两句移到第 3 步开头，写成 "We now bound … Since \(\tau/s\le\tau L_\lambda\le\frac12\), …"。

**进度：第 1 步，共 5 步。** 要不要我现在把这两句删掉，等写第 3 步时再放回去？

---

## User (2026-11-12 15:35)

然后第二步需要写一下

---

## Assistant (2026-11-12 15:36)

你在编辑这个文件，我就不动它了。开头那两句范围条件现在还在第 9–10 行，写第 3 步时移过去。

**进度：第 2 步，共 5 步。** 第 2 步把第 1 步的递推展开成显式的加权和。它要接在第 1 步 "for every \(k\ge0\)." 之后：

```latex
Define the scalar weights \(c_{-1}:=0\), \(c_0:=1\), and
\[
    c_{j+1}:=(1-\tau L_\lambda)(1+\omega)c_j
    -(1-\tau L_\lambda)\omega c_{j-1},
    \qquad j\ge0.
\]
We claim that
\[
    \blmbd^k=\frac{\tau}{\rho}\sum_{i=0}^{k-1}c_{k-1-i}\,\bq^i,
    \qquad k\ge-1,
\]
where an empty sum is zero. For \(k=-1\) and \(k=0\), both sides vanish
because \(\blmbd^{-1}=\blmbd^0=\zero\). Suppose that the claim holds for
\(k-1\) and \(k\) with some \(k\ge0\). Substituting both expressions into
the recursion of Step~1, the coefficient of \(\bq^i\) in \(\blmbd^{k+1}\)
for \(0\le i\le k-1\) is
\[
    \frac{\tau}{\rho}\left[(1-\tau L_\lambda)(1+\omega)c_{k-1-i}
    -(1-\tau L_\lambda)\omega c_{k-2-i}\right]
    =\frac{\tau}{\rho}c_{k-i},
\]
where \(c_{-1}=0\) covers the case \(i=k-1\). The coefficient of
\(\bq^k\) is \(\tau/\rho=(\tau/\rho)c_0\). This proves the claim for
\(k+1\). Since \(\|\bq^i\|\le L_h\) for every \(i\), we obtain
\[
    \|\blmbd^k\|
    \le\frac{\tau}{\rho}L_h\sum_{j=0}^{k-1}\lvert c_j\rvert
    \le\frac{\tau}{\rho}L_h\sum_{j=0}^{\infty}\lvert c_j\rvert,
    \qquad k\ge0.
\]
```

- **为什么只写到这里**：$c_j$ 的通项公式 $\sum_i\zeta_1^i\zeta_2^{j-i}$ 用到特征根，放到第 3 步写。第 2 步只证明加权和的展开式。
- **递推起点为什么取 $k=-1$**：两个初值都为零，所以把 $k=-1$ 和 $k=0$ 都当作归纳基础，从 $k=0$ 起每一步的推导完全相同。这样第一次迭代不需要单独验证。
- **最后的不等式**：右端的无穷级数此时可能取 $+\infty$。它有限，是第 3 步的结论。

---

## User (2026-11-12 15:36)

也不是since 是自然而然的推导你现在写的太差了

---

## Assistant (2026-11-12 15:36)

**进度：第 2 步，共 5 步。** 我按递推直接展开的思路重写了，去掉了"We claim"和归纳法的框架，接在第 1 步的递推之后：

```latex
Unrolling this recursion from \(\blmbd^{-1}=\blmbd^0=\zero\) gives
\[
    \blmbd^k=\frac{\tau}{\rho}\sum_{i=0}^{k-1}c_{k-1-i}\,\bq^i,
\]
where the scalar weights \(c_j\) obey the same recursion,
\[
    c_{j+1}=(1-\tau L_\lambda)(1+\omega)c_j
    -(1-\tau L_\lambda)\omega c_{j-1},
    \qquad c_{-1}=0,\quad c_0=1.
\]
Hence \(\blmbd^k\) is a weighted sum of the subgradients
\(\bq^0,\ldots,\bq^{k-1}\), and \(\|\bq^i\|\le L_h\) yields
\[
    \|\blmbd^k\|\le\frac{\tau}{\rho}L_h\sum_{j\ge0}\lvert c_j\rvert.
\]
```

接下来第 3 步估计 $\sum_{j\ge0}\lvert c_j\rvert$。开头那两句参数范围就放在这里，作为讨论特征根的前提。

---

## User (2026-11-12 15:38)

Then % Since \(\tau/s\le\tau L_\lambda\le\frac12\), we have
% \(\omega\in(0,1)\) and \(1-\tau L_\lambda\in[\frac12,1)\). 这个参数范围应该是从下降量得到的？

---

## Assistant (2026-11-12 15:38)

这两个范围是从引理的假设 $\tau L_\lambda\le\frac{1}{2}$ 直接推出来的，和下降量无关。乘子有界引理本身不依赖任何下降不等式。

- **$\omega\in(0,1)$**：$L_\lambda=\frac{1}{\rho}+\frac{1}{s}$，所以 $\frac{\tau}{s}\le\tau L_\lambda\le\frac{1}{2}$，因此 $\sqrt{\tau/s}\in(0,\frac{1}{\sqrt{2}}]$。再代入 $\omega=\frac{1-\sqrt{\tau/s}}{1+\sqrt{\tau/s}}$，就得到 $\omega\in(0,1)$。
- **$1-\tau L_\lambda\in[\frac{1}{2},1)$**：由假设直接得到。
- **和下降分析的关系**：交接里说 $\tau L_\lambda\le\frac{1}{2}$ 同时服务两处，一处是对偶上升步的充分增量（下降分析要用），一处是这个引理。条件只写一次，两处共用，但这个引理的证明中不用下降量。
- **最弱需要什么**：证明实际上只要求 $\tau L_\lambda\lt1$。取 $\frac{1}{2}$ 是为了和下降分析用同一条条件，由此 $\sqrt{1-\tau L_\lambda}$ 和第 3 步分段中的 $1-R\ge\frac{\tau L_\lambda}{2}$ 等常数也随之确定。

**进度：第 3 步开头，共 5 步。** 所以第 3 步可以这样起句："By the assumption \(\tau L_\lambda\le\frac12\), …"

---

## User (2026-11-12 15:39)

那我们现在有点混乱了 实际上我们 需要多少个引理

---

## Assistant (2026-11-12 15:40)

一共要 **8 个引理**：正文 4 个，附录 4 个。正文 4 个引理加上定理构成复杂度证明的主线，附录 4 个引理只服务于正文的下降引理。这和交接里定下的顺序一致。

## 正文（`sections/Acceleration.tex`）

| 编号 | 引理 | 作用 | 状态 |
|---|---|---|---|
| L1 | `lem:b2-prime-residual-decomposition` | 把 KKT 残差拆成原始步、对偶步、中心步、乘子偏差四项 | 陈述已写，证明是直接计算 |
| L2 | `lem:b2-prime-multiplier-bounds` | 控制乘子偏差 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$ | 证明写到第 2 步 |
| L3 | `lem:b2-prime-potential-descent` | $\mathcal{W}$ 的一步下降，写成步长形式，权重分别为 $c_1$、$c_2$、$c_3\alpha$ | 占位，等路线 2 落实 |
| L4 | `lem:b2-prime-initial-gap` | $\mathcal{W}_0-\mathcal{W}_K\le\Delta_{\mathcal{W}}$ | 占位，对应 G3.5 |

**定理的证明**：把 L3 对 $k$ 求和并用 L4 控制，前三项残差的平方和就被 $\Delta_{\mathcal{W}}$ 控制住；第四项由 L2 控制；最后代入 L1。L3 改成步长形式之后，它的三项和 L1 的前三项一一对应，所以旧的 `lem:b2-prime-residual-bound` 可以删掉。

## 附录（L3 的证明）

| 编号 | 内容 | 来源 |
|---|---|---|
| A1 | 值函数正则性：$p_s$ 的上下估计；$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$、$\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 对中心 $\mathbf{z}$ 的灵敏度 | G3.1 + G2.7 |
| A2 | 固定中心一步不等式：$\mathcal{E}$ 按 $1-\varsigma$ 衰减，并留出余量项 | G2.4，证明内含 G2.1–G2.3 |
| A3 | $p_s$ 在中心步上的下降 | G3.3，即旧 `lem:z-step-p` |
| A4 | 中心移动误差：$\mathbf{z}^k\to\mathbf{z}^{k+1}$ 时 $\mathcal{E}$ 的变化 | G3.2 |

**L3 的证明**：把 A2、A3、A4 组合起来即可，对应 G3.4。路线 2 把 $c_e$ 改成常数，影响的是 A2 的系数核对和 L3 的最终形式，A1、A3、A4 不受影响。

## 当前位置

L2 的证明写到第 2 步，后面还有第 3 步特征根分段、第 4 步去掉对 $s$ 的依赖、第 5 步推到外推点。主要工作量在 A2 和路线 2 的系数重核。

---

## User (2026-11-12 15:40)

虽然现在不是整理结果的最好时机

---

## Assistant (2026-11-12 15:40)

老大，你这句话还没说完。你的意思是先把这份 8 个引理的结构写进 [PROJECT_STATUS.md](overleaf/notes/progress/PROJECT_STATUS.md) §4 第 6 条，作为后续的提纲吗？如果是，我只在"用户定下的证明结构"下面补一张引理表，标出每个引理的状态，其他内容都不改。

---

## User (2026-11-12 15:40)

但是我们不妨先把每个引理需要的条件写一下 最后进行整合

---

## Assistant (2026-11-12 15:41)

下面按引理逐个列出各自原本需要的条件，最后合并成一组。总的结论是：**合并后 $\gamma L_{\mathcal{D},\mathbf{x}}\le\frac{1}{10}$ 取代 $\gamma\lt(2L_{\mathcal{D},\mathbf{x}})^{-1}$**，交接里两个 $\gamma$ 条件不一致的问题由此消失。另外，$s\ge\rho$ 可能可以去掉，这一点还要再核。条件来源是 G2、G3 笔记和当前稿件。

## 各引理的条件

**正文的 4 个引理**

| 引理 | 条件 |
|---|---|
| L1 残差分解 | 只需两条 Assumption 和 $\eta,\gamma,\tau,s\gt0$。$L_{\mathcal{D},\mathbf{x}}$ 是 $\nabla_{\mathbf{x}}\mathcal{D}_\rho(\cdot,\boldsymbol{\lambda})$ 的 Lipschitz 常数，不依赖 $\gamma$ |
| L2 乘子有界 | Assumption `ass:h`，$\tau L_\lambda\le\frac{1}{2}$。证明实际只用到 $\tau L_\lambda\lt1$ |
| L3 $\mathcal{W}$ 下降（G3.4） | A2 的全部条件，加上 $\alpha=\kappa_\alpha\varsigma$、$0\lt\kappa_\alpha\le\frac{1}{6}$ |
| L4 初始间隙（G3.5） | 零初值；$\gamma L_{\mathcal{D},\mathbf{x}}\le\frac{1}{10}$，用来给出 $c_e/\mu_\gamma\le\frac{31}{150}$ |

**附录的 4 个引理**

| 引理 | 条件 |
|---|---|
| A1 值函数正则性（G3.1、G2.7） | $\gamma L_{\mathcal{D},\mathbf{x}}\lt\frac{1}{2}$，$s\gt0$ |
| A2 固定中心一步（G2.4） | 原始条件见下 |
| A3 中心步（G3.3） | $\alpha\in[0,1]$，$\mu_\gamma\gt0$ |
| A4 中心移动误差（G3.2） | $\gamma L_{\mathcal{D},\mathbf{x}}\le\frac{1}{10}$，$s\gt0$ |

A2 的原始条件有三条：

- (a) $0\lt\eta\le\gamma$，并且 $\upsilon^2\le\frac{1}{48\kappa_x+24}$，其中 $\upsilon=1-\eta\mu_\gamma$，$\kappa_x=L_x/\mu_\gamma$；
- (b) $\tau L_\lambda\le\frac{1}{2}$，并且 $\tau\le\frac{\mu_\gamma^2}{8G_{\mathcal{A}}^2(L_x+\mu_\gamma/4)}$；
- (c) $s\ge4\tau$，即 $\varsigma\le\frac{1}{2}$。

G2.5 把 A2 的条件换成显式参数：取 $\eta=\gamma$ 时 $\upsilon=\gamma L_{\mathcal{D},\mathbf{x}}$。这时 $\gamma L_{\mathcal{D},\mathbf{x}}\le\frac{1}{10}$ 推出 (a)，$14\gamma\tau G_{\mathcal{A}}^2\le1$ 推出 (b) 的第二条。

## 合并

所有引理加在一起，需要的条件是

$$
\gamma L_{\mathcal{D},\mathbf{x}}\le\frac{1}{10},\quad \eta=\gamma,\quad \tau L_\lambda\le\frac{1}{2},\quad 14\gamma\tau G_{\mathcal{A}}^2\le1,\quad s\ge4\tau,\quad \alpha=\kappa_\alpha\varsigma,\quad 0\lt\kappa_\alpha\le\frac{1}{6}
$$

和现在的 `eq:b2-prime-stepsizes` 相比有三处不同：

1. **$\gamma$ 只保留一个条件。** $\frac{1}{10}$ 蕴含 A1 需要的 $\frac{1}{2}$，所以常数段落里的 $\gamma\lt(2L_{\mathcal{D},\mathbf{x}})^{-1}$ 可以删掉，或改写成 "under `eq:b2-prime-stepsizes`"。
2. **$\tau\le\rho/4$ 加 $s\ge\rho$ 换成 $\tau L_\lambda\le\frac{1}{2}$。** 在 G2.5 里，$s\ge\rho$ 的作用只是由 $\tau\le\rho/4$ 推出 $\tau L_\lambda\le\frac{1}{2}$。G3.5 用到的 $\rho+s\ge2\rho$ 只改善常数：去掉它之后，$\frac{L_h^2}{2(\rho+s)}\le\frac{L_h^2}{2\rho}$ 照样成立。**推断：$s\ge\rho$ 可以删掉，待核。** 需要逐条检查 G3、G4 有没有其他地方用到 $s\ge\rho$。
3. **定理中仍用不含 $s$ 的充分条件。** $s=c_s/\epsilon$ 随精度变化，而 $\tau L_\lambda\le\frac{1}{2}$ 依赖 $s$。所以定理里写 $\tau\le\rho/4$ 和 $\epsilon\le c_s/(4\tau)$，由此对所有充分小的 $\epsilon$ 都有 $\tau L_\lambda\le\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$，同时 $s\ge4\tau$。

## 待核

- **路线 2 会改变 A2 的条件。** $c_e$ 改成常数 $\frac{3}{25}(L_x+\mu_\gamma/2)$ 以后，(a) 中 $\upsilon^2\le\frac{1}{48\kappa_x+24}$ 这个形式可能变化。L4 用到的 $c_e/\mu_\gamma\le\frac{31}{150}$ 也要重算。上面的合并结果在路线 2 系数核完之前只是暂定。
- **L1 的系数与 $\gamma$ 无关。** L1 中出现的 $L_{\mathcal{D},\mathbf{x}}$ 不受 $\gamma$ 条件限制，所以 L1 可以放在所有参数条件之前陈述。这和你定下的"残差分解放最前"一致。

---

## User (2026-11-12 15:41)

或者 我们把这个条件标红  或者把条件标红？

---

## Assistant (2026-11-12 15:41)

可以标红，**而且应该用宏来标，不要直接写 `\color{red}`。** `tools/shared.tex` 第 240 行已经有 `\red{...}`，可以直接用。

- **标什么**：每个引理陈述中，只把还没整合进 `eq:b2-prime-stepsizes` 的条件写成 `\red{...}`，比如 L2 的 `\red{\(\tau L_\lambda\le\frac12\)}` 和 A1 的 `\red{\(\gamma L_{\calD,\bx}<\frac12\)}`。已经统一的 Assumption 不标。
- **为什么用宏**：最后整合时可以用 `grep -n '\\red{' sections/Acceleration.tex appendix/AccelerationProof.tex` 一次列出所有待整合的条件。逐条替换成 "Suppose that \eqref{eq:b2-prime-stepsizes} holds" 之后，红色标记就清掉了。
- **注意**：当前文件第 154–183 行已经用了一整块 `{\color{red} ... }` 来标记占位内容。为了不混淆，条件标记只用 `\red{}`，整块占位继续用原来的写法。

要不要我按上一条的表格，把 L1、L2 现有陈述里的条件先用 `\red{}` 标出来？

---

## User (2026-11-12 15:42)

先这样\subsection{Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}}
\label{app:b2-prime-multiplier-bounds} 我们把 5步写全

---

## Assistant (2026-11-12 15:43)

先用数值检查一遍第 3 步的界，再把整段证明写进文件。

好，不再做数值检查，直接写证明。

老大，我按五步提纲把证明压缩写进了 [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex)，从约 90 行减到约 45 行。编译没有报错。**进度：5 步全部写完。**

- **结构**：一共三段。第一段做第 1、2 步，从递推展开成加权和，得到 `eq:b2-prime-multiplier-weights`。第二段做第 3 步，三种情形各用一两句写完。第三段做第 4、5 步。
- **记号**：$a$、$\nu$、$u$、$b$ 都已删除，全文只用 $1-\tau L_\lambda$ 和 $\omega$。参数范围 $\omega\in(0,1)$ 放在第 3 步开头，也就是第一次用到它的地方。
- **与提纲的一处差别**：提纲说"根模长不超过 $\sqrt{1-\tau L_\lambda}$"，这只对复根成立。实根时两根之积是 $(1-\tau L_\lambda)\omega$，但较大的根可以超过 $\sqrt{1-\tau L_\lambda}$。所以证明中实根情形只用了"两根落在 $[0,1)$"，没有写这个模长界。

---

## User (2026-11-12 15:46)

这个特征根 可以提取出来一个数值引理吗？ 太啰嗦了

---

## Assistant (2026-11-12 15:47)

老大，特征根的分析已经单独写成数值引理 `lem:scalar-recursion`，放在乘子有界引理的证明之前，乘子引理的证明缩到一段。编译没有报错。

- **数值引理**：设 $t,\omega\in(0,1)$，序列满足 $c_{-1}=0$、$c_0=1$ 和 $c_{j+1}=(1-t)(1+\omega)c_j-(1-t)\omega c_{j-1}$，结论为

$$
\sum_{j\ge0}\lvert c_j\rvert\le\max\left\{\frac{4}{t},\frac{2\sqrt{2}}{t^{3/2}}\right\}
$$

  它的证明就是原来的三种情形，各一句。
- **乘子引理的证明**：先写出对偶步，代入外推，从零初值展开。然后取 $t=\tau L_\lambda$ 调用数值引理，再代入 $\tau/\rho=\tau L_\lambda\cdot\frac{s}{\rho+s}$ 得到 $C_\lambda L_h$，最后一句推到外推点。

拆出来之后可以看清，数值引理只需要 $t\lt1$。所以乘子引理用到的 $\tau L_\lambda\le\frac{1}{2}$，在这里只起两个作用：保证 $t\lt1$，并通过 $\tau/s\lt1$ 保证 $\omega\gt0$。

---

## User (2026-11-12 15:47)

我的理解是 我们现在跟去更新 把两个乘子的范数写出来 ；然后证bpund

---

## Assistant (2026-11-12 15:47)

对，就是这个顺序，只差一点：**真正要证的只有 $\lVert\boldsymbol{\lambda}^k\rVert$**，$\bar{\boldsymbol{\lambda}}^k$ 的界由它直接得到。

1. **从对偶步出发，写出 $\boldsymbol{\lambda}^k$ 的表达式**：

$$
\boldsymbol{\lambda}^k=\frac{\tau}{\rho}\sum_{i=0}^{k-1}c_{k-1-i}\mathbf{q}^i
$$

   由此得到 $\lVert\boldsymbol{\lambda}^k\rVert\le\frac{\tau}{\rho}L_h\sum_j\lvert c_j\rvert$。
2. **证明界**：用数值引理控制 $\sum_j\lvert c_j\rvert$，再代入 $\frac{\tau}{\rho}=\tau L_\lambda\frac{s}{\rho+s}$，得到 $\lVert\boldsymbol{\lambda}^k\rVert\le C_\lambda L_h$。
3. **外推点**：$\bar{\boldsymbol{\lambda}}^k=(1+\omega)\boldsymbol{\lambda}^k-\omega\boldsymbol{\lambda}^{k-1}$。对这个式子用三角不等式，再对 $\boldsymbol{\lambda}^k$ 和 $\boldsymbol{\lambda}^{k-1}$ 用第 2 步的界，就得到 $3C_\lambda L_h$。

现在写进文件的证明就是这个结构。

---

## User (2026-11-12 15:47)

bound用到这个原因是什么

---

## Assistant (2026-11-12 15:48)

这个界只用在一个地方：控制残差分解第二式里的**乘子偏差项** $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$。

- **为什么会出现这一项**：对偶函数里加了 $-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$，所以对偶步的梯度是 $\mathcal{A}(\mathbf{x})-\mathbf{y}-\boldsymbol{\lambda}/s$。由此可行性残差只能写成

$$
\lVert\mathcal{A}(\mathbf{x}^{k+1})-\mathbf{y}^{k+1}\rVert\le\frac{1}{\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert+\frac{1}{s}\lVert\bar{\boldsymbol{\lambda}}^k\rVert
$$

  第一项被下降引理控制，第二项是正则化带来的偏差，下降引理控制不到它。
- **为什么要和 $s$ 无关**：由引理，$\frac{1}{s}\lVert\bar{\boldsymbol{\lambda}}^k\rVert\le\frac{3C_\lambda L_h}{s}$。取 $s=c_s/\epsilon$ 且 $c_s\ge6C_\lambda L_h$，这一项就不超过 $\epsilon/2$。如果 $C_\lambda$ 随 $s$ 增长，偏差项就不再按 $1/s$ 衰减，$s\propto1/\epsilon$ 这个取法不成立，$\epsilon^{-5/2}$ 也随之失效。
- **为什么要对所有 $k$ 一致成立**：Fast LRALM 不对乘子做投影，有界性只能从迭代本身推出。这就是要把 $\boldsymbol{\lambda}^k$ 展开成次梯度加权和的原因。

**这个引理保证的是正则化偏差能被 $s$ 压下去，而且不影响 $s$ 的取法。**

---

## User (2026-11-12 15:48)

不是 我是说为啥用素质引理证明解 是因为加了范数

---

## Assistant (2026-11-12 15:48)

对。用数值引理，是因为三角不等式之后要估计的是**带绝对值的和** $\sum_j\lvert c_j\rvert$，而外推会让一部分 $c_j$ 变成负数。

- **不加外推时**（$\omega=0$）：$c_j=(1-\tau L_\lambda)^j\ge0$，所以 $\sum_j\lvert c_j\rvert=\sum_j c_j$ 是几何级数，和为 $\frac{1}{\tau L_\lambda}$，一行就能写完，不需要引理。
- **加了外推以后**：特征根可能是复根 $Re^{\pm\mathrm{i}\phi}$，这时 $c_j=R^j\frac{\sin((j+1)\phi)}{\sin\phi}$ 正负交替，$\sum_j\lvert c_j\rvert$ 严格大于 $\sum_j c_j$。$\sum_j c_j$ 仍可以用多项式在 $1$ 处的值算出来，但它控制不了 $\sum_j\lvert c_j\rvert$。所以只能分别估计模长 $R$ 和辐角 $\phi$，这就是数值引理里三种情形的来历。
- **常数的代价**：$\omega$ 接近 1 时，$\sin\phi$ 只有 $\sqrt{\tau L_\lambda}$ 量级，于是多出 $(\tau L_\lambda)^{-1/2}$ 这个因子，最后变成 $C_\lambda$ 里的 $\sqrt{8\rho/\tau}$。

---

## User (2026-11-12 15:51)

这个不能合成一个界吗？

---

## Assistant (2026-11-12 15:51)

可以合并。正文只在一处用到这个引理，就是残差里的 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$（第 250 行的 $3C_\lambda L_h/s$），$\lVert\boldsymbol{\lambda}^k\rVert$ 的界只在证明内部用一次。有两种合并写法：

- **只陈述外推点的界（推荐）**：把常数 3 吸收进 $C_\lambda$，引理只写一个界：

$$
\lVert\bar{\boldsymbol{\lambda}}^k\rVert\le C_\lambda L_h,\qquad C_\lambda:=3\max\left\{4,\sqrt{\frac{8\rho}{\tau}}\right\}
$$

  证明里 $\lVert\boldsymbol{\lambda}^k\rVert\le\frac{1}{3}C_\lambda L_h$ 作为中间一步出现。正文要同步改三处：第 197 行改成 $c_s\ge2C_\lambda L_h$，第 250 行改成 $C_\lambda L_h/s$，第 254 行同样改成 $2C_\lambda L_h$。
- **两个一起写成 max**：$\max\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\}\le C_\lambda L_h$，$C_\lambda$ 同上。这样保留了 $\boldsymbol{\lambda}^k$ 的界，但正文用不到它，属于多余的陈述。

推荐第一种，因为引理只陈述正文实际用到的量。要我按第一种改吗？

---

## User (2026-11-12 15:51)

不就是选3C?

---

## Assistant (2026-11-12 15:51)

对，合并后取 $3C_\lambda$ 作为两者共同的界：

$$
\max\left\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\right\}\le3C_\lambda L_h
$$

$C_\lambda$ 的定义和正文其余各处都不用改。第 197、250、254 行原本就用的是 $3C_\lambda$ 和 $6C_\lambda$，和这个界一致。

---

## User (2026-11-12 15:52)

你和一下

---

## Assistant (2026-11-12 15:52)

已经改好了，[Acceleration.tex:131-133](overleaf/sections/Acceleration.tex#L131-L133) 现在只陈述一个界：

$$
\max\left\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\right\}\le3C_\lambda L_h
$$

附录里的证明不用动。证明先得到 $\lVert\boldsymbol{\lambda}^k\rVert\le C_\lambda L_h$，再推出 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert\le3C_\lambda L_h$，这两步已经足以推出这个 max 形式的界。

---

## User (2026-11-12 15:53)

一共要 **8 个引理**：正文 4 个，附录 4 个。正文 4 个引理加上定理构成复杂度证明的主线，附录 4 个引理只服务于正文的下降引理。这和交接里定下的顺序一致。

## 正文（`sections/Acceleration.tex`）

| 编号 | 引理 | 作用 | 状态 |
|---|---|---|---|
| L1 | `lem:b2-prime-residual-decomposition` | 把 KKT 残差拆成原始步、对偶步、中心步、乘子偏差四项 | 陈述已写，证明是直接计算 |
| L2 | `lem:b2-prime-multiplier-bounds` | 控制乘子偏差 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$ | 证明写到第 2 步 |
| L3 | `lem:b2-prime-potential-descent` | $\mathcal{W}$ 的一步下降，写成步长形式，权重分别为 $c_1$、$c_2$、$c_3\alpha$ | 占位，等路线 2 落实 |
| L4 | `lem:b2-prime-initial-gap` | $\mathcal{W}_0-\mathcal{W}_K\le\Delta_{\mathcal{W}}$ | 占位，对应 G3.5 |

**定理的证明**：把 L3 对 $k$ 求和并用 L4 控制，前三项残差的平方和就被 $\Delta_{\mathcal{W}}$ 控制住；第四项由 L2 控制；最后代入 L1。L3 改成步长形式之后，它的三项和 L1 的前三项一一对应，所以旧的 `lem:b2-prime-residual-bound` 可以删掉。

## 附录（L3 的证明）

| 编号 | 内容 | 来源 |
|---|---|---|
| A1 | 值函数正则性：$p_s$ 的上下估计；$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$、$\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 对中心 $\mathbf{z}$ 的灵敏度 | G3.1 + G2.7 |
| A2 | 固定中心一步不等式：$\mathcal{E}$ 按 $1-\varsigma$ 衰减，并留出余量项 | G2.4，证明内含 G2.1–G2.3 |
| A3 | $p_s$ 在中心步上的下降 | G3.3，即旧 `lem:z-step-p` |
| A4 | 中心移动误差：$\mathbf{z}^k\to\mathbf{z}^{k+1}$ 时 $\mathcal{E}$ 的变化 | G3.2 |

**L3 的证明**：把 A2、A3、A4 组合起来即可，对应 G3.4。路线 2 把 $c_e$ 改成常数，影响的是 A2 的系数核对和 L3 的最终形式，A1、A3、A4 不受影响。

## 当前位置

L2 的证明写到第 2 步，后面还有第 3 步特征根分段、第 4 步去掉对 $s$ 的依赖、第 5 步推到外推点。主要工作量在 A2 和路线 2 的系数重核。 我们现在需要更新这个是吗| L3 | `lem:b2-prime-potential-descent` | $\mathcal{W}$ 的一步下降，写成步长形式，权重分别为 $c_1$、$c_2$、$c_3\alpha$ | 占位，等路线 2 落实 | 我们肯呢个需要 \subsection{Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}}新建一个sub？ 然后需要这个引理的引理 放到这个子节里面？是这个意思吗？

---

## Assistant (2026-11-12 15:54)

是这个意思。L2 已经写完，下一个是 L3。L3 的证明新建一个子节，A1–A4 作为辅助引理放在这个子节里面，结构和 L2 的子节一样：先给出辅助引理，再给出主证明。

**更新后的状态**

| 编号 | 状态 |
|---|---|
| L1 | 陈述已写，证明未写 |
| L2 | 陈述和证明都已写完，附带数值引理 `lem:scalar-recursion` |
| L3 | 下一个，等路线 2 落实 |
| L4 | 占位 |

**附录的子节结构**

```latex
\subsection{Proof of Lemma~\ref{lem:b2-prime-residual-decomposition}}  % L1，直接计算
\subsection{Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}}       % L2，已完成
\subsection{Proof of Lemma~\ref{lem:b2-prime-potential-descent}}       % L3
%   A1 值函数正则性 → A2 固定中心一步 → A3 中心步 → A4 中心移动误差 → L3 的证明
\subsection{Proof of Lemma~\ref{lem:b2-prime-initial-gap}}             % L4
```

- **辅助引理放在哪里**：只服务于一个正文引理的，放进该引理的子节，比如数值引理放在 L2 的子节，A1–A4 放在 L3 的子节。
- **一处例外**：L4 的证明要用 A1 中 $p_s$ 的下界，对应 G3.1(i)。A1 已经在 L3 的子节里陈述过，L4 只需引用，不用重复陈述。
- **引理总数**：加上数值引理，一共 9 个。

L1 的证明只有几行，可以先补上，再去写 L3。

---

## User (2026-11-12 15:54)

我的要求是 你是数学家 你是优化数学理论的非常擅长写paper的人 因此 你不能写的像工程技术报告 就很乱

---

## Assistant (2026-11-12 15:55)

老大，明白。后面讨论证明结构和写证明，都围绕"哪个量被哪个不等式控制"来组织，不再用 L1、A1 这类编号、状态表和步骤标签。这条要求已经补进记忆。

按这个标准，整个证明只有一条主线：要控制的量是 KKT 残差。

残差分解把它界定为四个量：原始步 $\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert$、对偶步 $\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert$、中心步 $\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$，以及正则化偏差 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$。

前三个量的平方由势函数 $\mathcal{W}$ 的一步下降量控制：

$$
\mathcal{W}_k-\mathcal{W}_{k+1}\ge c_1\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2+c_2\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2+c_3\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2
$$

对 $k$ 求和后，右端的总和不超过 $\mathcal{W}_0-\inf\mathcal{W}\le\Delta_{\mathcal{W}}$。第四个量不出现在下降量里，由乘子的一致有界性单独控制，得到 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s\le3C_\lambda L_h/s$。

因此定理只依赖三个不等式：残差分解、乘子有界、$\mathcal{W}$ 的下降。乘子有界已经写完。$\mathcal{W}$ 的下降是唯一有实质内容的部分，它由三个估计合成：

- 固定中心时，$\mathcal{E}$ 以比率 $1-\varsigma$ 压缩；
- $p_s$ 沿中心步下降；
- 中心从 $\mathbf{z}^k$ 移到 $\mathbf{z}^{k+1}$ 时，$\mathcal{E}$ 的增量由 $\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$ 控制。

这三个估计都要用到值函数 $p_s$、$d_s$ 关于中心的正则性。附录按这个依赖关系排列。

---

## User (2026-11-12 15:57)

老大，两部分都写进 [PROJECT_STATUS.md](overleaf/notes/progress/PROJECT_STATUS.md) §4 第 6 条了，放在"其余保留小项"之前。

- **编号约定与材料来源**：L1–L4 对应的标签、各自的进度、附录子节的组织规则、取回旧附录 D 和 E 的两条 `git show` 命令，以及 A1–A4 的来源对应表。
- **外部审核意见**：记了对方的两点意见，即 L2 的证明应从特征根写法改成能量或 Lyapunov 写法，以及按 6 步顺推重写附录。我标成了"尚未采纳"。

对方这条意见里有一处我认为站不住，也写进去了：他说可以"直接通过一步递推的不等式归纳出界"。G1.5 已经证明，只用 $\lVert\mathbf{q}\rVert\le L_h$ 时，最坏半径确实能到 $(\tau L_\lambda)^{-1/2}L_h$，半径 $L_h$ 的球不是不变集。所以简单的一步归纳证不出来。能量法也许可行，但常数里必须带 $\sqrt{\rho/\tau}$，而且他没有给出能量函数的具体形式。在看到具体的能量函数之前，我建议不要让他直接重写 L2，L2 现有的证明先留着。 你先看下这个

---

## Assistant (2026-11-12 15:58)

老大，我看过了。那段记录的判断是对的：一步范数归纳证不出界，现有的 L2 证明应当保留。记录里没写的一点是，能量法在原理上可行，得到的常数和现有的同阶。另外，这条状态记录里有三处已经过期。

## 一步归纳为什么失败

记 $t=\tau L_\lambda$，$\mathbf{v}^k=\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}$。递推等价于

$$
\boldsymbol{\lambda}^{k+1}=(1-t)\boldsymbol{\lambda}^k+(1-t)\omega\mathbf{v}^k+\frac{\tau}{\rho}\mathbf{q}^k
$$

$$
\mathbf{v}^{k+1}=-t\boldsymbol{\lambda}^k+(1-t)\omega\mathbf{v}^k+\frac{\tau}{\rho}\mathbf{q}^k
$$

对两式取范数并用三角不等式，$(\lVert\boldsymbol{\lambda}^k\rVert,\lVert\mathbf{v}^k\rVert)$ 的系数矩阵两行分别是 $(1-t,(1-t)\omega)$ 和 $(t,(1-t)\omega)$。当 $\omega\to1$ 时，它的谱半径趋于 $1-t+\sqrt{t(1-t)}$；只要 $t\lt\frac{1}{2}$，这个值就大于 1。三角不等式丢掉了第二式中 $-t\boldsymbol{\lambda}^k$ 的符号，而系统的稳定性正是靠这个符号。所以按范数逐步归纳必然发散，这和 G1.5 的结论一致。

## 能量法是否可行

可行，但不会更短。上面的系统是受迫阻尼振子：恢复力系数为 $t$，阻尼为 $1-(1-t)\omega$，外力不超过 $\frac{\tau}{\rho}L_h\le tL_h$。自然的能量是 $t\lVert\boldsymbol{\lambda}^k\rVert^2+\lVert\mathbf{v}^k\rVert^2$ 加一个交叉项。这个系统的阻尼至少为 $t$，由此得到 $\lVert\boldsymbol{\lambda}^k\rVert\lesssim t^{-1/2}L_h$，和现有的 $\sqrt{\rho/\tau}$ 同阶。

代价是离散情形下交叉项的系数要对所有 $\omega\in(0,1)$ 一致地配出来，这部分计算量和现在的三种情形相当。审核意见没有给出具体的能量函数。上面的阶数估计是我的推断，没有逐项证明。

审核意见批评的"信号处理写法"，在把特征根分析拆成数值引理之后已经大体解决：L2 的证明现在只有一段，内容是"乘子是次梯度的加权和，权重的 $\ell_1$ 范数有界"。我建议维持现状。如果你想要能量写法，我可以把那个能量函数具体推出来，再比较两种写法的长度。

## 记录里过期的地方

- **路线 2 的状态前后矛盾。** 上面"已验算完毕的常数结论"一段说，$c_e=\frac{3}{25}(L_x+\frac{\mu_\gamma}{2})$ 已经验算，并给出 $c_1=\frac{1}{250\gamma}$、$c_2=\frac{1}{16\tau}$、$c_3=\frac{1}{5\gamma}$。下面"编号约定"一段却写"L3 待写，等路线 2 落实"。按前一段，路线 2 已经落实，L3 可以直接写。
- **"下一步任务"第 2 项已经完成。** 动量符号已换成 $\omega$，条件已统一为 $\tau L_\lambda\le\frac{1}{2}$，引理的结论也已合并成 $\max\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\}\le3C_\lambda L_h$。
- **"零未定义引用"现在不成立。** `main.tex` 第 74–76 行把附录 A、B、C 的 `\input` 注释掉了，当前编译有 15 个未定义引用。

要不要我把这三处在状态文件里改掉？

---

## User (2026-11-12 15:59)

重点不是状态文件 是我们现在需要干什么

---

## Assistant (2026-11-12 15:59)

现在要做的只有一件事：**在附录里证明 $\mathcal{W}$ 的一步下降**。定理的证明依赖三个不等式，其中残差分解的证明只是几行计算，乘子有界已经写完，剩下这一个承担全部实质内容。常数 $c_1=\frac{1}{250\gamma}$、$c_2=\frac{1}{16\tau}$、$c_3=\frac{1}{5\gamma}$ 已经在另一个会话里验算过，所以可以直接动笔。

按依赖关系，写作顺序如下：

1. **残差分解的证明。** 从 $\nabla_{\mathbf{x}}\mathcal{D}_\rho$ 的表达式和两个更新式直接算出，先补上。
2. **值函数对中心的正则性。** 包括 $p_s$ 的上下估计，以及 $\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$、$\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 关于 $\mathbf{z}$ 的 Lipschitz 性，后面三个估计都要用。由此直接得到 $p_s$ 沿中心步的下降。
3. **固定中心的一步不等式。** 对偶 Nesterov 步作用在 $d_s(\cdot;\mathbf{z})$ 上，原始梯度步跟踪 $\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k;\mathbf{z})$，两者合起来给出 $\mathcal{E}$ 的压缩，并留下 $\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2$ 和 $\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2$ 两个负项。这一步最长。
4. **中心移动带来的误差。** 中心从 $\mathbf{z}^k$ 移到 $\mathbf{z}^{k+1}$ 时 $\mathcal{E}$ 的增量，由 $\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$ 控制。把第 2、3、4 步合起来就是 $\mathcal{W}$ 的下降。
5. **初值界** $\mathcal{W}_0-\mathcal{W}_K\le\Delta_{\mathcal{W}}$。

附录写完并经你审定后，再把 $\mathcal{W}_k$、$(c_1,c_2,c_3)$、$\Delta_{\mathcal{W}}$、$C_R$ 填回正文的红色占位处。

我先写第 1 步，写完给你看，可以吗？

---

## User (2026-11-12 15:59)

你把过期的改掉就好

---

## Assistant (2026-11-12 16:00)

[PROJECT_STATUS.md](overleaf/notes/progress/PROJECT_STATUS.md) §4 第 6 条里三处过期的内容已经改掉，其他内容没有动。

- **第 84 行**：原来的编译记录保留，后面补了一句当前状态：`main.tex` 注释掉了附录 A、B、C 的 `\input`，所以有 15 个未定义引用，恢复那三行后即消失。
- **第 90 行**：乘子有界引理的证明标为已完成。这一行同时记下四点：条件是 $\tau L_\lambda\le\frac{1}{2}$；外推系数记为 $\omega$；结论合并为 $\max\{\lVert\boldsymbol{\lambda}^k\rVert,\lVert\bar{\boldsymbol{\lambda}}^k\rVert\}\le3C_\lambda L_h$；权重的 $\ell_1$ 界由 `lem:scalar-recursion` 给出。
- **第 99 行**：下降引理的状态改为"路线 2 的常数已验算，可直接动笔"。

---

## User (2026-11-12 16:01)

我的逻辑是 我们证明势函数的一步下降 需要几个引理 但是我们先把这个 一步引理的证明依赖的简单几步写出来 就是几个最本质的不等式 对吧  然后 我们在往回 写这里面不等式的需要的正式引理 不知道你能懂哦的意思吗

---

## Assistant (2026-11-12 16:02)

懂。先把势函数下降的证明本身写出来，其中每个本质的不等式暂时当作已知；主证明定下来之后，再回头把每个不等式写成正式引理并证明。按这个顺序，主证明只依赖一个恒等式和三个不等式。

## 分解

记 $\mathcal{E}_k(\mathbf{z})$ 为以 $\mathbf{z}$ 为中心度量的第 $k$ 步能量，$\mathcal{E}_k=\mathcal{E}_k(\mathbf{z}^k)$，$\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$。一步变化拆成三部分：

$$
\mathcal{W}_{k+1}-\mathcal{W}_k=\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^k)-\mathcal{E}_k\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)\right]
$$

三个括号依次是外层值函数沿中心步的变化、固定中心时内层能量的变化、中心移动引起的能量变化。每个括号对应一个不等式。

## 三个不等式

**固定中心的压缩。** 中心固定在 $\mathbf{z}^k$ 时，一步迭代使能量按比率 $1-\varsigma$ 压缩，并留下三个负项：

$$
\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\frac{1}{121\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

**值函数沿中心步的变化。**

$$
p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\le-\frac{\alpha(1-\alpha)}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2+\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

**中心移动的误差。** 对 $\lVert\mathbf{z}^{k+1}-\mathbf{z}^k\rVert=\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$，存在与 $s$ 无关的常数 $C_1$、$C_2$，使得

$$
\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)\le C_1\alpha\sqrt{\mathcal{E}_{k+1}(\mathbf{z}^k)}\,\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert+C_2\alpha^2\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2
$$

## 合成

主证明只需要处理两个正项。

- **第三式的交叉项**用 Young 不等式分成 $\frac{\varsigma}{2}\mathcal{E}_{k+1}(\mathbf{z}^k)$ 和 $\frac{C_1^2\alpha^2}{2\varsigma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$。前者由压缩吸收，因为 $(1+\frac{\varsigma}{2})(1-\varsigma)\le1-\frac{\varsigma}{2}$。后者在 $\alpha=\kappa_\alpha\varsigma$ 时等于 $\frac{C_1^2\kappa_\alpha}{2}\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$，由第二式的 $-\frac{\alpha(1-\alpha)}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$ 吸收，条件是 $\kappa_\alpha$ 足够小。
- **第二式的正项** $\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2$ 由第一式中的 $\frac{\varsigma\mu_\gamma}{4}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2$ 吸收，同样要求 $\alpha\lesssim\varsigma$。

这两处吸收就是中心步长必须取 $\alpha\propto\varsigma$ 的原因。吸收之后，剩下的负项就是步长形式的三项，系数为 $c_1=\frac{1}{250\gamma}$、$c_2=\frac{1}{16\tau}$、$c_3=\frac{1}{5\gamma}$。

第一式中的 $\frac{1}{121\gamma}$ 取自状态文件里另一个会话的验算记录，我没有独立核对。

下一步我把这部分写进附录，作为下降引理的证明；三个不等式先各用一个带标签的引理陈述占位，证明留空，之后逐个往回补。可以吗？

---

## User (2026-11-12 16:03)

$$\mathcal{W}_{k+1}-\mathcal{W}_k=\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^k)-\mathcal{E}_k\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)\right]$$里面的 epsk=1周卡

---

## Assistant (2026-11-12 16:03)

你问的应该是分解式里的 $\mathcal{E}_{k+1}(\mathbf{z}^k)$。它表示：第 $k$ 步的原始步和对偶步已经做完，但中心还没有更新，这时以旧中心 $\mathbf{z}^k$ 度量的能量。

对任意中心 $\mathbf{z}$，定义

$$
\mathcal{E}_{k+1}(\mathbf{z})=p_s(\mathbf{z})-d_s(\boldsymbol{\lambda}^{k+1};\mathbf{z})+\frac{1}{2s}\lVert\mathbf{w}^{k+1}-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2+c_e\lVert\mathbf{x}^{k+1}-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k;\mathbf{z})\rVert^2+c_r\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2
$$

其中的迭代点 $\mathbf{x}^{k+1}$、$\boldsymbol{\lambda}^{k+1}$、$\bar{\boldsymbol{\lambda}}^k$、$\mathbf{w}^{k+1}$ 都是确定的，中心 $\mathbf{z}$ 只通过 $p_s$、$d_s$、$\boldsymbol{\lambda}_s^\star$、$\mathbf{x}_s$ 这四个与中心有关的量进入。

- **$\mathcal{E}_{k+1}(\mathbf{z}^k)$**：把 $\mathbf{z}=\mathbf{z}^k$ 代入。第 $k$ 步的原始步和对偶步都是针对中心为 $\mathbf{z}^k$ 的鞍点问题做的，所以固定中心的压缩不等式比较的是 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 和 $\mathcal{E}_k=\mathcal{E}_k(\mathbf{z}^k)$。
- **$\mathcal{E}_{k+1}=\mathcal{E}_{k+1}(\mathbf{z}^{k+1})$**：把 $\mathbf{z}=\mathbf{z}^{k+1}$ 代入，这才是 $\mathcal{W}_{k+1}$ 里出现的能量。

两者之差 $\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)$ 中迭代点相同，只有中心不同，所以它只反映中心移动的影响，由第三个不等式控制。分解式就是在 $\mathcal{E}_{k+1}-\mathcal{E}_k$ 中间加减 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 这一项。

---

## User (2026-11-12 16:03)

不就是简写成epsk+1吗？

---

## Assistant (2026-11-12 16:03)

不能。$\mathcal{E}_{k+1}$ 是 $\mathcal{E}_{k+1}(\mathbf{z}^{k+1})$ 的简写，用的是新中心；$\mathcal{E}_{k+1}(\mathbf{z}^k)$ 用的是旧中心。两者是不同的数。

如果把 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 也写成 $\mathcal{E}_{k+1}$，分解式的第三个括号就成了 $\mathcal{E}_{k+1}-\mathcal{E}_{k+1}=0$，中心移动的误差就消失了。$\alpha$ 必须取 $\propto\varsigma$ 的原因正来自这一项。

想让式子短一些，可以给旧中心下的能量一个单独的记号，比如

$$
\widetilde{\mathcal{E}}_{k+1}:=\mathcal{E}_{k+1}(\mathbf{z}^k)
$$

分解式变成

$$
\mathcal{W}_{k+1}-\mathcal{W}_k=\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\widetilde{\mathcal{E}}_{k+1}-\mathcal{E}_k\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}-\widetilde{\mathcal{E}}_{k+1}\right]
$$

这个记号在分解式、压缩不等式和中心移动误差里各出现一次，在合成一步里还要出现两次，所以值得引入。

---

## User (2026-11-12 16:04)

$$\mathcal{W}_{k+1}-\mathcal{W}_k=\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^k)-\mathcal{E}_k\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)\right]$$ 这个啊

---

## Assistant (2026-11-12 16:04)

对，如果你指的是式子里的 $\mathcal{E}_{k+1}(\mathbf{z}^{k+1})$，它就是 $\mathcal{E}_{k+1}$，可以直接简写。我上一条理解成了 $\mathcal{E}_{k+1}(\mathbf{z}^k)$，答偏了。

简写后的分解式是

$$
\mathcal{W}_{k+1}-\mathcal{W}_k=\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^k)-\mathcal{E}_k\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}-\mathcal{E}_{k+1}(\mathbf{z}^k)\right]
$$

只有 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 要把中心写出来，因为它的中心 $\mathbf{z}^k$ 和下标 $k+1$ 不一致。

---

## User (2026-11-12 16:06)

三个不等式对应的引理是和我们的附录D一个框架吗

---

## Assistant (2026-11-12 16:07)

是同一个框架，新的下降证明可以照搬旧附录 D 的组织方式。区别只在内层能量：Nesterov 外推需要的能量比 GDA 的多了两项，所以要多证一个"中心移动误差"的估计。

## 相同之处：三层结构

旧附录 D 用的是 Zhang 等人的三值 Lyapunov 函数：

$$
\Psi_s=\left[\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+\left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+p_s(\mathbf{z})
$$

新的 $\mathcal{W}=p_s+\frac{1}{2}\mathcal{E}$ 和 $\frac{1}{2}\Psi_s$ 的比例完全一样：外层 $p_s$ 的权重为 1，内层间隙的权重为 $\frac{1}{2}$。因此两个证明都分三层：

1. **值函数的正则性。** $\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$ 关于 $\boldsymbol{\lambda}$ 和 $\mathbf{z}$ 都 Lipschitz，$d_s$ 光滑且强凹，$p_s$ 可微。对应旧的 `lem:v2-value-regularity`，固定 $s$、取 $\boldsymbol{\mu}=\mathbf{0}$ 后可以照搬。
2. **外层 $p_s$ 沿中心步的变化。** 对应旧的 `lem:z-step-p`。新的第二个不等式就是它再加一次 Young 不等式，可以原样使用。
3. **内层间隙的一步估计，加上中心移动的修正。** 两个框架的差别全部在这一层。

## 不同之处：内层能量

旧框架里，内层间隙是 $\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k)-d_s(\boldsymbol{\lambda}^k)$ 和 $p_s-d_s(\boldsymbol{\lambda}^k)$。它的一步估计由三个引理拼成：$\mathcal{P}$ 沿 GDA 的下降（`lem:basic-one-step`）、对偶值的增量（`lem:dual-value-gain`），以及两者的合并（`lem:partial-lyapunov-z-step`）。这种估计是加性下降，只能给出 $O(1)$ 的耗散，没有压缩率。

Nesterov 外推的分析需要的是估计序列，所以新的内层能量变成

$$
\mathcal{E}_k=\left[p_s-d_s(\boldsymbol{\lambda}^k)\right]+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2+c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

和旧框架相比，原始间隙 $\mathcal{P}-d$ 换成了跟踪误差 $c_e\lVert\cdot\rVert^2$，并新增了对偶距离 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$。由此产生两个后果。

- **固定中心的估计变成乘性压缩** $\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\cdots$。旧框架的三个引理由 G2.4 这一个估计取代，证明是新写的，篇幅最长。
- **中心移动的误差要单独证明。** 旧框架里中心只通过 $\mathcal{P}$、$d_s$、$p_s$ 进入，`lem:saddle-center-stability` 只需给出 $\mathbf{x}_s$、$\mathbf{x}_s^\star$ 关于 $\mathbf{z}$ 的 Lipschitz 性。新能量还含有 $\boldsymbol{\lambda}_s^\star(\mathbf{z})$，它对中心的灵敏度是

$$
\lVert\boldsymbol{\lambda}_s^\star(\mathbf{z}')-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert\le\frac{\sqrt{s}}{2\gamma\sqrt{\mu_\gamma}}\lVert\mathbf{z}'-\mathbf{z}\rVert
$$

  这里多出的 $\sqrt{s}$ 要和权重 $\frac{1}{2s}$、以及 $\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert\le\sqrt{2s\mathcal{E}_k}$ 抵消，这样常数 $C_1$ 才与 $s$ 无关。这是新框架中唯一需要新思路的估计。所以旧的 `lem:saddle-center-stability` 只要补上 $\boldsymbol{\lambda}_s^\star$ 的这一条灵敏度，就可以作为中心移动误差的基础。

## 落到附录

正则性和外层中心步可以从旧附录 D 直接移植；中心稳定性要补 $\boldsymbol{\lambda}_s^\star$ 的灵敏度；固定中心的压缩和中心移动误差要新写。

---

## User (2026-11-12 16:07)

现在需要你干的第一件事 告诉我 一共写几个引理？按照顺序  然后新增的（）？

---

## Assistant (2026-11-12 16:08)

势函数下降的证明需要 **7 个引理**，按依赖顺序排列。后一个只用到前面的结果，最后的合成用到第 3、6、7 个。

1. **值函数的正则性。** 内容：$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$ 关于 $\boldsymbol{\lambda}$ Lipschitz；$d_s$ 是 $\frac{1}{s}$-强凹且光滑的；$p_s$ 可微，$\nabla p_s(\mathbf{z})=(\mathbf{z}-\mathbf{x}_s^\star(\mathbf{z}))/\gamma$；$p_s$ 有上下估计。移植自 `lem:v2-value-regularity`。其中下界 $p_s\ge\inf F-\frac{L_h^2}{2(\rho+s)}$ 是**新增**的，初值界要用它。
2. **鞍点关于中心的灵敏度。** $\mathbf{x}_s$、$\mathbf{x}_s^\star$ 关于 $\mathbf{z}$ 的 Lipschitz 性，以及误差界 $\lVert\mathbf{x}_s(\boldsymbol{\lambda})-\mathbf{x}_s^\star\rVert^2\le\frac{2}{\mu_\gamma}(p_s-d_s(\boldsymbol{\lambda}))$，都移植自 `lem:saddle-center-stability`。**新增**一条：$\lVert\boldsymbol{\lambda}_s^\star(\mathbf{z}')-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert\le\frac{\sqrt{s}}{2\gamma\sqrt{\mu_\gamma}}\lVert\mathbf{z}'-\mathbf{z}\rVert$。
3. **$p_s$ 沿中心步的变化。** 移植自 `lem:z-step-p`，再加一次 Young 不等式。
4. **对偶 Nesterov 不等式**（**新增**，来自 G2.1）。在部分模型 $\mathcal{P}_s(\mathbf{x}^{k+1},\cdot;\mathbf{z},\mathbf{0})$ 上做估计序列论证，由此引出 $\mathbf{w}^k$。
5. **原始跟踪估计**（**新增**，来自 G2.3）。控制 $\mathbf{x}^{k+1}$ 与 $\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k;\mathbf{z})$ 的距离，由此引出权重 $c_e$、$c_r$。
6. **固定中心的压缩**（**新增**，来自 G2.4）。由第 4、5 个合成 $\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\cdots$。路线 2 改动的常数都在这一个引理里。
7. **中心移动误差**（**新增**，来自 G3.2）。由第 1、2 个得到 $\mathcal{E}_{k+1}-\mathcal{E}_{k+1}(\mathbf{z}^k)\le C_1\alpha\sqrt{\mathcal{E}_{k+1}(\mathbf{z}^k)}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert+C_2\alpha^2\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$，其中三处 $\sqrt{s}$ 相互抵消。

所以 1–3 从旧附录 D 移植，第 1、2 个各补一条新结论；4–7 是新写的。初值界只用到第 1 个的下界，不需要新引理。

第 4、5 个也可以并进第 6 个的证明，这样引理数降到 5 个。但这两个估计的机制不同：前者是对偶估计序列，后者是原始跟踪。分开写，第 6 个的证明就只剩合成。我建议分开。

---

## User (2026-11-12 16:09)

旧附录 D 用的是 Zhang 等人的三值 Lyapunov 函数：

$$\Psi_s=\left[\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+\left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+p_s(\mathbf{z})$$

新的 $\mathcal{W}=p_s+\frac{1}{2}\mathcal{E}$ 和 $\frac{1}{2}\Psi_s$ 的比例完全一样：外层 $p_s$ 的权重为 1，内层间隙的权重为 $\frac{1}{2}$ 我认为的逻辑是 我们需要把目前的函数写成类似于之前的值函数 的分解  你觉得呢？不要啰嗦 直接给我结果

---

## Assistant (2026-11-12 16:09)

同意。按 $\Psi_s$ 的分法，$\mathcal{W}_k$ 写成三层：

$$
\mathcal{W}_k=\frac{1}{2}\underbrace{\left[c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2\right]}_{\text{primal gap}}+\frac{1}{2}\underbrace{\left[p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2\right]}_{\text{dual gap}}+p_s(\mathbf{z}^k)
$$

和 $\frac{1}{2}\Psi_s$ 逐层对应：

- **原始间隙**：$\mathcal{P}_s-d_s$ 换成它的二次替代 $c_e\lVert\mathbf{x}^k-\mathbf{x}_s\rVert^2$。由 $\frac{\mu_\gamma}{2}\lVert\mathbf{x}-\mathbf{x}_s(\boldsymbol{\lambda})\rVert^2\le\mathcal{P}_s-d_s\le\frac{L_x}{2}\lVert\mathbf{x}-\mathbf{x}_s(\boldsymbol{\lambda})\rVert^2$，两者等价；改成在外推点 $\bar{\boldsymbol{\lambda}}^{k-1}$ 处度量。$c_r$ 项是外推带来的修正。
- **对偶间隙**：$p_s-d_s$ 保留，加上 Nesterov 估计序列的距离项 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$。
- **外层**：$p_s(\mathbf{z}^k)$ 不变。

按这个分法，7 个引理也逐层归位：

- 原始间隙由原始跟踪估计控制；
- 对偶间隙由对偶 Nesterov 不等式控制；
- 外层由中心步估计控制；
- 中心移动误差作用在前两层上。

---

## User (2026-11-12 16:10)

primal gap是什么东西 我们之前不是这么写的

---

## Assistant (2026-11-12 16:10)

你说得对，我那里的标签用错了。

旧附录 D 的 `eq:lyapunov-decomposition` 写的是 "primal gap at fixed $\boldsymbol{\lambda}$"，指函数值之差

$$
\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})
$$

新能量里根本没有这一项。我放在第一个括号里的 $c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)\rVert^2$ 是距离的平方，是**跟踪误差**，不是间隙。它和 $\mathcal{P}_s-d_s$ 只是同阶，在旧框架里的位置相同，但两者是不同的量。$c_r$ 项是对偶步长，更不属于原始部分。

照实写，新势函数是

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\left[p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_e}{2}\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

和 $\frac{1}{2}\Psi_s$ 相比，外层项 $p_s$ 和对偶间隙 $p_s-d_s$ 保留不变；原始间隙 $\mathcal{P}_s-d_s$ 换成了跟踪误差；另外新增了对偶估计序列的距离项和外推修正项。

---

## User (2026-11-12 16:11)

不对啊我的意思是写成值函数的分解 而不是一步到位变成跌打差 是必须这么写吗 如果不是那就不要

---

## Assistant (2026-11-12 16:12)

不是每一项都必须写成距离。新势函数有三项不在旧的值函数分解里，三项要分开看：

- **对偶距离项** $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2：必须保留。** 它是 Nesterov 估计序列的一部分，压缩率 $1-\varsigma$ 就是从这一项来的，没有办法写成值函数之差。
- **跟踪项** $c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2：可以不写成距离。** 它可以换成固定 $\bar{\boldsymbol{\lambda}}^{k-1}$ 时的原始间隙 $\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)-d_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)$，也就是旧 $\Psi_s$ 里的第一项，只是改在外推点度量。依据是两者等价：$\frac{\mu_\gamma}{2}\lVert\cdot\rVert^2\le\mathcal{P}_s-d_s\le\frac{L_x}{2}\lVert\cdot\rVert^2$。
- **外推修正项** $c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2：在现在的证明里必须保留。** 跟踪估计中，$\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})$ 漂移到 $\mathbf{x}_s(\boldsymbol{\lambda}^k)$ 产生的误差 $L_\star\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert$ 要由这一项支付。

去掉可以去掉的距离项之后，势函数写成值函数的形式：

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\left[p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{c}{2}\left[\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)-d_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)\right]+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

其中 $c$ 是待定常数。前三项和旧附录 D 的 $\frac{1}{2}\Psi_s$ 同形，后两项是加速带来的。

**代价。** 跟踪引理要从距离收缩改成函数值收缩，对应的不等式是 $\mathcal{P}_s(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k)-d_s(\bar{\boldsymbol{\lambda}}^k)\le\kappa_x\upsilon^2\left[\mathcal{P}_s(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k)-d_s(\bar{\boldsymbol{\lambda}}^k)\right]$。但漂移那一步要比较两个不同 $\boldsymbol{\lambda}$ 处的间隙，三角不等式只对距离成立，所以证明内部仍要先换回距离，再换回间隙。常数会多出因子 $\kappa_x\le\frac{11}{9}$，$c$、$c_e$ 都要重算。

所以值函数写法只改变 $\mathcal{W}$ 的陈述形式，证明的实质不变。我建议在正文和附录开头用上面的值函数形式陈述 $\mathcal{W}$，证明内部仍用距离计算，并在一处写明两者的等价关系。这样常数不用重算，形式上也和旧附录 D 对齐。

---

## User (2026-11-12 16:12)

旧附录 D 用的是 Zhang 等人的三值 Lyapunov 函数：

$$\Psi_s=\left[\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+\left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+p_s(\mathbf{z})$$

新的 $\mathcal{W}=p_s+\frac{1}{2}\mathcal{E}$ 和 $\frac{1}{2}\Psi_s$ 的比例完全一样：外层 $p_s$ 的权重为 1，内层间隙的权重为 $\frac{1}{2}$。 我的意思是 写成类似于原来的三值函数啊

---

## Assistant (2026-11-12 16:12)

懂了，可以直接写成三值函数加上加速修正：

$$
\mathcal{W}_k=\frac{1}{2}\Psi_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

其中 $\Psi_s=\mathcal{P}_s-2d_s+2p_s$ 就是旧附录 D 的三值函数，按原样在当前迭代点上取值。后两项是 Nesterov 外推必需的：第一项是对偶估计序列的距离，第二项支付外推点漂移。

这样写是自然的，因为对偶 Nesterov 不等式（G2.1）本身产生的误差项就是原始间隙 $\mathcal{P}_s(\mathbf{x}^{k+1},\boldsymbol{\lambda}^{k+1})-d_s(\boldsymbol{\lambda}^{k+1})$ 和 $\mathcal{P}_s(\mathbf{x}^{k+1},\boldsymbol{\lambda}^k)-d_s(\boldsymbol{\lambda}^k)$。G2.4 是先把这些间隙换成跟踪距离，才引入 $c_e$ 项；三值写法把它们留在 $\Psi_s$ 里，不做这一步转换。

**待核。** 原始间隙在 $\mathcal{W}$ 中的权重由 $c_e/2$ 变为 $\frac{1}{2}$。等价地，跟踪项的系数从 $c_e$ 变成 $\frac{L_x}{2}$ 量级，比原来大约 $\frac{1}{48\upsilon^2}\ge2$ 倍。所以 G2.4 的四处系数检查要重做，路线 2 已经验算过的 $c_1$、$c_2$、$c_3$ 也会随之改变。

**推断。** 跟踪收缩因子是 $\upsilon^2\le\frac{1}{100}$，余量很大，权重加大应该仍能闭合，代价是 $c_r$ 可能要放大，但这一点还没有证明。

要我先把这组系数检查做完，再决定是否采用这个写法吗？

---

## User (2026-11-12 16:12)

好的 那哪一部分是我们后来引入的1/2 Eps

---

## Assistant (2026-11-12 16:12)

$\frac{1}{2}\mathcal{E}_k$ 就是 $\mathcal{W}_k$ 去掉外层 $p_s(\mathbf{z}^k)$ 后剩下的全部。按三值写法，

$$
\mathcal{E}_k=\underbrace{\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\left[p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]}_{\Psi_s-p_s}+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

所以 $\mathcal{W}_k=p_s+\frac{1}{2}\mathcal{E}_k$ 和 $\mathcal{W}_k=\frac{1}{2}\Psi_s+\frac{1}{4s}\lVert\cdot\rVert^2+\frac{c_r}{2}\lVert\cdot\rVert^2$ 是同一个量。$\mathcal{E}_k$ 的前两项就是 $\Psi_s$ 的两个间隙，后两项是加速带来的修正。

和 G2.4 里原来的 $\mathcal{E}_k$ 相比，唯一的改动是跟踪项 $c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2$ 换成了原始间隙 $\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k)-d_s(\boldsymbol{\lambda}^k)$。对偶间隙、对偶距离项和 $c_r$ 项都不变。

---

## User (2026-11-12 16:13)

你现在的输出有乱码 总结一下我们的势函数 怎么变成三值函数修哼 以及 以及我们的势函数怎么写是最符合直觉和规范的 本质是什么

---

## Assistant (2026-11-12 16:14)

乱码多半是上一条的 `\underbrace` 在 VSCode 里没有渲染出来，下面不再使用。

## 本质

**新势函数就是 Zhang 等人的三值函数，只把其中的对偶间隙换成 Nesterov 对对偶问题的标准 Lyapunov 函数。** 外层值函数和原始间隙原样保留，另外加一个外推修正项。

## 从三值函数到新势函数

旧附录 D 的三值函数取一半，是外层值函数、原始间隙、对偶间隙三项之和：

$$
\frac{1}{2}\Psi_s=p_s(\mathbf{z})+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+\frac{1}{2}\left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]
$$

对偶步不加外推时，对偶间隙 $p_s-d_s$ 本身足以作为对偶部分的 Lyapunov 函数。加入 Nesterov 外推后，这一项不再单调下降。

对最大化 $\frac{1}{s}$-强凹函数 $d_s$ 的 Nesterov 方法，标准 Lyapunov 函数是

$$
\mathcal{V}_k=p_s(\mathbf{z})-d_s(\boldsymbol{\lambda}^k;\mathbf{z})+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2
$$

它每步按 $1-\varsigma$ 压缩。其中 $\mathbf{w}^k$ 是估计序列，满足 $\mathbf{w}^k=\boldsymbol{\lambda}^{k-1}+\varsigma^{-1}(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$。

## 最规范的写法

把对偶间隙换成 $\mathcal{V}_k$，再加上外推修正，就得到

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{1}{2}\mathcal{V}_k+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

四项分别控制四件事：

- **外层值函数** $p_s(\mathbf{z}^k)$：中心 $\mathbf{z}^k$ 的进展，由中心步估计控制。
- **原始间隙** $\mathcal{P}_s-d_s$：$\mathbf{x}^k$ 对内层极小点的跟踪，由原始梯度步的收缩控制。
- **Nesterov 函数** $\mathcal{V}_k$：对偶变量的加速收敛，由对偶 Nesterov 不等式控制。
- **外推修正项**：外推点 $\bar{\boldsymbol{\lambda}}^{k-1}$ 与 $\boldsymbol{\lambda}^k$ 的偏差。它进入跟踪误差，必须单独支付。

$\frac{1}{2}\mathcal{E}_k$ 就是除 $p_s(\mathbf{z}^k)$ 以外的三项之和。

## 待核

这个写法把 G2.4 中的跟踪项 $c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2$ 换成了原始间隙，相当于权重由 $c_e$ 变成 $\frac{L_x}{2}$ 量级。因此 G2.4 的系数检查要重做，$c_1$、$c_2$、$c_3$、$c_r$ 都可能改变。记号检索显示稿件里没有用过 $\mathcal{V}$，可以直接引入。

---

## User (2026-11-12 16:15)

本质逻辑不变就行 我们现在分析的本质 是 xzllbar?

---

## Assistant (2026-11-12 16:15)

对，分析的就是 $\mathbf{x}$、$\mathbf{z}$、$\boldsymbol{\lambda}$、$\bar{\boldsymbol{\lambda}}$ 这四个变量。其中 $\bar{\boldsymbol{\lambda}}$ 不是独立变量：外推使对偶部分多了一步记忆，$\bar{\boldsymbol{\lambda}}$ 就是这份记忆的体现。

$\mathcal{W}_k$ 的每一项对应一个变量：

- **$\mathbf{z}^k$**：外层值函数 $p_s(\mathbf{z}^k)$，衡量中心的进展。
- **$\mathbf{x}^k$**：原始间隙 $\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k)-d_s(\boldsymbol{\lambda}^k)$，衡量 $\mathbf{x}^k$ 离当前乘子下内层极小点的距离。
- **$\boldsymbol{\lambda}^k$ 与 $\boldsymbol{\lambda}^{k-1}$**：Nesterov 函数 $\mathcal{V}_k$。$\mathbf{w}^k$ 同时依赖 $\boldsymbol{\lambda}^k$ 和 $\boldsymbol{\lambda}^{k-1}$，动量带来的记忆就在这里。
- **$\bar{\boldsymbol{\lambda}}^{k-1}$**：修正项 $c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$，即上一步对偶步的长度。原始步是在外推点处计算的，所以 $\mathbf{x}^k$ 跟踪的是 $\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})$，而不是 $\mathbf{x}_s(\boldsymbol{\lambda}^k)$，两者之差由这一项支付。

没有外推时，$\bar{\boldsymbol{\lambda}}=\boldsymbol{\lambda}$，$\mathbf{w}^k=\boldsymbol{\lambda}^k$，后两项退化，$\mathcal{W}$ 就回到三值函数 $\frac{1}{2}\Psi_s$。所以本质逻辑不变：仍是三个变量 $\mathbf{z}$、$\mathbf{x}$、$\boldsymbol{\lambda}$ 各配一个间隙。加速只让对偶部分多出一步记忆。

---

## User (2026-11-12 16:16)

那我们之前附录D在我们目前的讨论 可以承担哪些 比如 我们实际上用附录D的来实现Wk的那部分构造 不要啰嗦

---

## Assistant (2026-11-12 16:17)

旧附录 D 能承担 $\mathcal{W}_k$ 中 $\frac{1}{2}\Psi_s$ 的部分，也就是外层值函数和原始间隙；Nesterov 函数 $\mathcal{V}_k$ 和修正项要新写。移植时固定 $s$、取 $\boldsymbol{\mu}=\mathbf{0}$，并把原始步中的 $\boldsymbol{\lambda}^k$ 换成 $\bar{\boldsymbol{\lambda}}^k$。

**可以直接用的：**

- `lem:v2-value-regularity`：$\mathbf{x}_s$ 关于 $\boldsymbol{\lambda}$ Lipschitz，$d_s$ 光滑强凹，$p_s$ 可微且 $\nabla p_s=(\mathbf{z}-\mathbf{x}_s^\star)/\gamma$。
- `lem:z-step-p`：$p_s(\mathbf{z}^k)$ 沿中心步的变化。
- `lem:saddle-center-stability`：$\mathbf{x}_s$、$\mathbf{x}_s^\star$ 关于 $\mathbf{z}$ Lipschitz，以及误差界 $\lVert\mathbf{x}_s(\boldsymbol{\lambda})-\mathbf{x}_s^\star\rVert^2\le\frac{2}{\mu_\gamma}(p_s-d_s)$。

**改写后可以用的：**

- `lem:basic-one-step`、`lem:partial-lyapunov-z-step` 中只涉及原始步和中心步的部分：给出原始间隙 $\mathcal{P}_s-d_s$ 在 $\mathbf{x}$ 梯度步和中心移动下的变化。原式在 $\boldsymbol{\lambda}^k$ 处做原始步，这里要改成在 $\bar{\boldsymbol{\lambda}}^k$ 处。

**不能用、要新写的：**

- `lem:dual-value-gain`：它给出 $d_s$ 沿普通对偶上升步的增量，现在由对偶 Nesterov 不等式取代，$\mathcal{V}_k$ 的压缩来自后者。
- $\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 关于中心的灵敏度。$\mathcal{V}_k$ 含 $\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2$，这一条要补进 `lem:saddle-center-stability`，其中的 $\sqrt{s}$ 要与权重 $\frac{1}{2s}$ 抵消。
- 外推修正项 $c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$ 及其与原始跟踪的耦合。
- 最后的合成：`lem:moving-three-value-descent` 的骨架可以沿用，但吸收条件变为 $\alpha\propto\varsigma$，所以系数检查要重做。

---

## User (2026-11-12 16:17)

从三值函数到新势函数

旧附录 D 的三值函数取一半，是外层值函数、原始间隙、对偶间隙三项之和：

$$\frac{1}{2}\Psi_s=p_s(\mathbf{z})+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]+\frac{1}{2}\left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right]$$

对偶步不加外推时，对偶间隙 $p_s-d_s$ 本身足以作为对偶部分的 Lyapunov 函数。加入 Nesterov 外推后，这一项不再单调下降。

对最大化 $\frac{1}{s}$-强凹函数 $d_s$ 的 Nesterov 方法，标准 Lyapunov 函数是

$$\mathcal{V}_k=p_s(\mathbf{z})-d_s(\boldsymbol{\lambda}^k;\mathbf{z})+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2$$

它每步按 $1-\varsigma$ 压缩。其中 $\mathbf{w}^k$ 是估计序列，满足 $\mathbf{w}^k=\boldsymbol{\lambda}^{k-1}+\varsigma^{-1}(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$。

最规范的写法

把对偶间隙换成 $\mathcal{V}_k$，再加上外推修正，就得到

$$\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{1}{2}\mathcal{V}_k+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$$ 是否可以写到一块  让我看到和Psi的关系 只保留最有用最本质的

---

## Assistant (2026-11-12 16:17)

可以，合在一起写成

$$
\mathcal{W}_k=\frac{1}{2}\Psi_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

第一项是旧附录 D 的三值函数，原样保留。后两项来自对偶外推，都是二次项：

- **对偶估计序列项**：它和 $\Psi_s$ 中的对偶间隙 $p_s-d_s$ 合起来，正好是 Nesterov 的 Lyapunov 函数 $\mathcal{V}_k$。加速靠的就是这一项。
- **外推修正项**：支付原始步在 $\bar{\boldsymbol{\lambda}}^{k-1}$ 而非 $\boldsymbol{\lambda}^k$ 处计算所产生的偏差。

不加外推时，$\mathbf{w}^k=\boldsymbol{\lambda}^k$，且 $\bar{\boldsymbol{\lambda}}^{k-1}=\boldsymbol{\lambda}^{k-1}$。

---

## User (2026-11-12 16:18)

$$\mathcal{W}_k=\frac{1}{2}\Psi_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$$ =？

---

## Assistant (2026-11-12 16:18)

展开 $\Psi_s=\mathcal{P}_s-2d_s+2p_s$，得到

$$
\mathcal{W}_k=\frac{1}{2}\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+p_s(\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

按间隙分组，它等于

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{1}{2}\mathcal{V}_k+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

其中 $\mathcal{V}_k=p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2$。

两种写法是同一个量。第一种显示 $\mathcal{W}_k$ 是三个值函数 $\mathcal{P}_s$、$d_s$、$p_s$ 的组合加两个二次项；第二种显示它是 $p_s$ 加上两个非负间隙和一个非负修正项，由此直接得到下界 $\mathcal{W}_k\ge p_s(\mathbf{z}^k)$。

---

## User (2026-11-12 16:19)

我们之前有个Ek

---

## Assistant (2026-11-12 16:19)

对，二者的关系是 $\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$，所以

$$
\mathcal{E}_k=\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\mathcal{V}_k+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

用三值函数表示，就是

$$
\mathcal{E}_k=\Psi_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-2p_s(\mathbf{z}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

$\mathcal{E}_k$ 是 $\mathcal{W}_k$ 中除外层 $p_s$ 以外的全部内层误差，四项都非负。

它和 G2.4 原来的 $\mathcal{E}_k$ 只差一项：原来的跟踪项 $c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2$ 换成了原始间隙 $\mathcal{P}_s-d_s$，其余三项都相同。

---

## User (2026-11-12 16:19)

逻辑是 我们现在有好几种写法 写到一起

---

## Assistant (2026-11-12 16:20)

把这几种写法放在一起，它们是同一个量：

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k
$$

$$
=\frac{1}{2}\Psi_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

$$
=p_s(\mathbf{z}^k)+\frac{1}{2}\left[\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\right]+\frac{1}{2}\mathcal{V}_k+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

$$
=\frac{1}{2}\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+p_s(\mathbf{z}^k)+\frac{1}{4s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2+\frac{c_r}{2}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

其中

$$
\mathcal{V}_k=p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z}^k)\rVert^2,\qquad\mathbf{w}^k=\boldsymbol{\lambda}^{k-1}+\varsigma^{-1}(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})
$$

四种写法各有用途：

- **第一种**：外层值函数加内层误差，用于分解 $\mathcal{W}_{k+1}-\mathcal{W}_k$。
- **第二种**：显示与旧附录 D 的三值函数 $\Psi_s$ 的关系。
- **第三种**：每一项都非负，对应一个变量，可直接看出下界 $\mathcal{W}_k\ge p_s(\mathbf{z}^k)$。
- **第四种**：$\mathcal{P}_s$、$d_s$、$p_s$ 三个值函数的线性组合加两个二次项，用于逐项计算一步变化。

---

## User (2026-11-12 16:22)

第二种：显示与旧附录 D 的三值函数 $\Psi_s$ 的关系。 这个并不本质 本质的是和minmax的思路靠拢 知道本质是什么 我们不是为了分析关系 把引理用上来看看到底nest哦到底不同在哪里的 我的理解是第四种：$\mathcal{P}_s$、$d_s$、$p_s$ 三个值函数的线性组合加两个二次项，用于逐项计算一步变化。 这个是一般人的 是吧 然后根据第二章进行分析 但是到nes弄不了 我们得加一个啥 进行化简编程第一种

---

## Assistant (2026-11-12 16:22)

对，你的理解是正确的，只需补充一点：具体是哪一项在 Nesterov 下失效。

**一般的 minimax 路线**（Zhang 等人、旧附录 D）用的是第四种写法 $\mathcal{P}_s-2d_s+2p_s$，对三个值函数逐项计算一步变化：

- $\mathcal{P}_s$ 沿原始梯度步下降；
- $p_s$ 沿中心步下降；
- $-2d_s$ 由对偶值的增量控制，对应 `lem:dual-value-gain`，即 $d_s(\boldsymbol{\lambda}^{k+1})-d_s(\boldsymbol{\lambda}^k)\ge c\lVert\boldsymbol{\lambda}^{k+1}-\boldsymbol{\lambda}^k\rVert^2-\text{误差}$。

**加入 Nesterov 外推后，失效的是第三条。** 对偶步从外推点 $\bar{\boldsymbol{\lambda}}^k$ 出发，$d_s(\boldsymbol{\lambda}^k)$ 不再单调上升，所以 $-2d_s$ 这一项无法逐项控制。加速方法的函数值本来就不单调，Nesterov 的分析也不依赖函数值单调。

**需要加的是估计序列的距离项** $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$。它和对偶间隙合成 $\mathcal{V}_k$ 后，单调性就恢复了，而且变成乘性压缩：

$$
\mathcal{V}_{k+1}\le(1-\varsigma)\mathcal{V}_k+\text{原始间隙误差}
$$

此外，原始步也在 $\bar{\boldsymbol{\lambda}}^k$ 处计算，所以还要加修正项 $c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$ 来支付这个偏差。

**然后化简成第一种写法。** 把原始间隙、$\mathcal{V}_k$ 和修正项合成内层误差 $\mathcal{E}_k$。固定中心时它整体按 $1-\varsigma$ 压缩，于是 $\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$。

**和 minimax 路线相比，本质区别**在于内层的分析方式：minimax 路线对三个值函数逐项做加性下降；Nesterov 路线把内层整体当成一个乘性压缩的量，外层 $p_s$ 仍逐项处理。

---

## User (2026-11-12 16:23)

我们如果按照$\mathcal{P}_s$ 沿原始梯度步下降；
$p_s$ 沿中心步下降；这个 现在是按照这个开始的吗？

---

## Assistant (2026-11-12 16:23)

不完全是。外层 $p_s$ 是这样开始的，原始部分不是。

- **$p_s$ 沿中心步下降：是。** G3.3 就是旧的 `lem:z-step-p` 加一次 Young 不等式，和 minimax 路线一样。
- **$\mathcal{P}_s$ 沿原始梯度步下降：不是。** 现在的证明（G2.3）没有用 $\mathcal{P}_s$ 的函数值下降，用的是距离收缩：

$$
\lVert\mathbf{x}^{k+1}-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k)\rVert\le\upsilon\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k)\rVert
$$

  也就是把原始梯度步看作向内层极小点的压缩。原始间隙 $\mathcal{P}_s-d_s$ 只在对偶 Nesterov 不等式中作为误差出现，随后换成距离来估计。所以现有的证明里，内层整体是 Nesterov 加跟踪收缩，只有外层沿用 minimax 路线。

如果改用三值写法，原始部分就可以回到 minimax 路线：用 $\mathcal{P}_s(\cdot,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k)$ 的下降引理控制原始间隙，对偶部分仍用 Nesterov。这样三层分工最清楚：

- 原始部分用下降引理，与 minimax 路线相同；
- 对偶部分用 Nesterov 估计序列，这是新的；
- 外层用中心步，与 minimax 路线相同。

但这正是前面标了"待核"的那一处。原始步在 $\bar{\boldsymbol{\lambda}}^k$ 处计算，下降引理给出的是 $\bar{\boldsymbol{\lambda}}^k$ 处的间隙，而 $\mathcal{W}$ 里的间隙在 $\boldsymbol{\lambda}^{k+1}$ 处度量。两者之差要由对偶步长 $\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert$ 和修正项支付，系数需要重新检查。

---

## User (2026-11-12 16:24)

本质区别在内层 我们分析外层在分析内层可以吗？

---

## Assistant (2026-11-12 16:24)

可以，而且这个顺序最能说明问题：**先分析外层，就能看清内层必须提供什么**，内层的分析再去满足这些要求。

**外层。** 中心步估计直接沿用 minimax 路线：

$$
p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\le-\frac{\alpha(1-\alpha)}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2+\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

右端第二项是正的，外层自己无法消去，要由内层支付。中心移动还会使内层误差增加 $C_1\alpha\sqrt{\mathcal{E}}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$。由此得到内层必须满足的两个要求：

- **要求一**：提供负项 $-c\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2$，其中 $c\gtrsim\alpha/\gamma$；
- **要求二**：以速率 $\rho_{\mathrm{in}}$ 压缩，并满足 $\rho_{\mathrm{in}}\gtrsim\alpha$。只有这样，交叉项经 Young 不等式分出的 $\frac{\alpha^2}{\rho_{\mathrm{in}}}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$ 才能被外层的 $-\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2$ 吸收。

**内层。** 中心固定在 $\mathbf{z}^k$，这是两种方法唯一不同的地方。

- **GDA**：对偶部分只有加性下降，压缩速率是 $\tau/s$ 量级，所以要求二迫使 $\alpha\lesssim\tau/s\sim1/s$。
- **Nesterov 外推**：$\mathcal{E}$ 按 $1-\varsigma$ 压缩，并提供 $-\frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star\rVert^2$。两个要求在 $\alpha\propto\varsigma=\sqrt{\tau/s}$ 时同时满足。

**结论。** 中心步长从 $1/s$ 提高到 $1/\sqrt{s}$，这就是加速的来源：$\epsilon^{-3}$ 改进为 $\epsilon^{-5/2}$，全部来自内层压缩率从 $1/s$ 提高到 $1/\sqrt{s}$。外层的分析与 minimax 路线完全相同。

因此附录按"外层、内层、耦合"排列：

- **外层**：值函数正则性和中心步估计，从旧附录 D 移植；
- **内层**：对偶 Nesterov 不等式、原始跟踪、固定中心压缩，是新写的；
- **耦合**：中心移动误差和合成。

---

## User (2026-11-12 16:24)

我不知道啊 因为我只熟悉三值的那个 所以 我希望按照我能理解的方式把东西写出来在进行太子恒 你说的外层到底是啥意思

---

## Assistant (2026-11-12 16:25)

这里的"外层"就是三值函数里的 $p_s$ 项。我用你熟悉的 $\Psi_s=\mathcal{P}_s-2d_s+2p_s$ 来说明。

## 三个值函数对应三层问题

$\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})$ 里有三组变量，各自对应一层优化：

$$
p_s(\mathbf{z})=\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z}),\qquad d_s(\boldsymbol{\lambda};\mathbf{z})=\min_{\mathbf{x}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})
$$

- **外层**：关于中心 $\mathbf{z}$ 极小化 $p_s(\mathbf{z})$。算法里对应中心步 $\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha(\mathbf{x}^{k+1}-\mathbf{z}^k)$。
- **内层**：中心 $\mathbf{z}$ 固定时，求鞍点问题 $\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s$ 的解。算法里对应原始梯度步和对偶步。

$\Psi_s$ 的三项正好分属这两层：

$$
\Psi_s=\left[\mathcal{P}_s-d_s\right]+\left[p_s-d_s\right]+p_s
$$

前两项是内层的两个间隙：

- **原始间隙** $\mathcal{P}_s-d_s$：固定 $\boldsymbol{\lambda}$ 时，$\mathbf{x}$ 离内层极小点有多远；
- **对偶间隙** $p_s-d_s$：$\boldsymbol{\lambda}$ 离鞍点有多远。

最后一项 $p_s$ 是外层的目标值。所以"外层"就是 $p_s(\mathbf{z}^k)$ 这一项，"内层"就是两个间隙。

## 旧附录 D 怎么分析，Nesterov 卡在哪里

旧附录 D 逐项计算 $\Psi_s$ 的一步变化：

- $\mathcal{P}_s$ 由 `lem:basic-one-step` 控制；
- $d_s$ 由 `lem:dual-value-gain` 控制；
- $p_s$ 由 `lem:z-step-p` 控制。

换成 Fast LRALM 以后，$\mathcal{P}_s$ 和 $p_s$ 这两项的分析基本照旧，只有 $d_s$ 这一项卡住：对偶步从外推点 $\bar{\boldsymbol{\lambda}}^k$ 出发，$d_s(\boldsymbol{\lambda}^k)$ 不再单调上升，`lem:dual-value-gain` 不成立。

修正的办法是给对偶间隙补一个 Nesterov 距离项 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$，再补一个外推修正项。补完以后，内层两个间隙加上这两项合称 $\mathcal{E}_k$，就得到

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k
$$

这里的外层 $p_s$ 就是 $\Psi_s$ 里原来的 $p_s$，没有任何改动。

## 推导顺序

按你熟悉的方式，接下来这样推：

1. 写出 $\mathcal{W}_k$ 的三值形式：三个值函数的组合，加两个二次项。
2. 逐项计算一步变化，$\mathcal{P}_s$ 和 $p_s$ 两项套用旧附录 D 的引理。
3. 在 $d_s$ 这一项卡住的地方，用 Nesterov 不等式代替 `lem:dual-value-gain`，把距离项引进来。
4. 最后把内层各项合并成 $\mathcal{E}_k$，化简为 $p_s+\frac{1}{2}\mathcal{E}_k$。

这样每一步都能和旧附录 D 逐行对照，不同之处只在第 3 步。

---

## User (2026-11-12 16:26)

三个值函数对应三层问题

$\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})$ 里有三组变量，各自对应一层优化：

$$p_s(\mathbf{z})=\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z}),\qquad d_s(\boldsymbol{\lambda};\mathbf{z})=\min_{\mathbf{x}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z})$$
外层：关于中心 $\mathbf{z}$ 极小化 $p_s(\mathbf{z})$。算法里对应中心步 $\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha(\mathbf{x}^{k+1}-\mathbf{z}^k)$。
内层：中心 $\mathbf{z}$ 固定时，求鞍点问题 $\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s$ 的解。算法里对应原始梯度步和对偶 我问一个很傻的问题 我们我们更新时新x再z但是外层确实先分析z？还是什么？最本质的思路是什么 不要啰嗦

---

## Assistant (2026-11-12 16:26)

这个问题不傻。分析顺序其实和更新顺序一致：先 $(\mathbf{x},\boldsymbol{\lambda})$，后 $\mathbf{z}$。我前面说"先分析外层"，只是讲解时的先后，逻辑上并不是这样。

**最本质的思路**是把一步迭代拆成两个动作，分别计算它们对 $\mathcal{W}$ 的影响：

1. **中心冻结在 $\mathbf{z}^k$，更新 $\mathbf{x}$ 和 $\boldsymbol{\lambda}$。** 此时 $p_s(\mathbf{z}^k)$ 不变，只有内层误差变化，从 $\mathcal{E}_k$ 变为 $\mathcal{E}_{k+1}(\mathbf{z}^k)$。
2. **$\mathbf{x}^{k+1}$、$\boldsymbol{\lambda}^{k+1}$ 不动，中心从 $\mathbf{z}^k$ 移到 $\mathbf{z}^{k+1}$。** 这时外层 $p_s$ 变化，内层误差也随中心变化，从 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 变为 $\mathcal{E}_{k+1}(\mathbf{z}^{k+1})$。

写成式子：

$$
\mathcal{W}_{k+1}-\mathcal{W}_k=\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^k)-\mathcal{E}_k\right]+\left[p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\right]+\frac{1}{2}\left[\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)\right]
$$

第一个括号属于动作 1，后两个括号属于动作 2。Nesterov 和 GDA 的区别全在第一个括号里。

---

## User (2026-11-12 16:27)

中心冻结在 $\mathbf{z}^k$，更新 $\mathbf{x}$ 和 $\boldsymbol{\lambda}$。 此时 $p_s(\mathbf{z}^k)$ 不变，只有内层误差变化，从 $\mathcal{E}_k$ 变为 $\mathcal{E}_{k+1}(\mathbf{z}^k)$ 本质上需要先分析内层 还是不是

---

## Assistant (2026-11-12 16:27)

是的，本质上先分析内层。中心冻结时的一步估计 $\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\cdots$ 是整个证明的核心，Nesterov 和 GDA 的差别全在这一步。中心移动的两项都要用到它的结论：压缩率 $\varsigma$ 用来吸收中心移动误差中的交叉项，负项 $-\frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2$ 用来抵消 $p_s$ 中心步估计里的正项。

---

## User (2026-11-12 16:28)

好多变化 啊 那我们的势函数是什么提取一部分应用到这里呢 不要啰嗦 你的渲染老是出问题

---

## Assistant (2026-11-12 16:28)

势函数是

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k
$$

内层这一步只用 $\mathcal{E}$。中心冻结在 $\mathbf{z}$ 时，$p_s(\mathbf{z})$ 是常数，不参与分析。

$\mathcal{E}_k(\mathbf{z})$ 由四项组成：

$$
A_k=\mathcal{P}_s(\mathbf{x}^k,\boldsymbol{\lambda}^k;\mathbf{z})-d_s(\boldsymbol{\lambda}^k;\mathbf{z})
$$

$$
B_k=p_s(\mathbf{z})-d_s(\boldsymbol{\lambda}^k;\mathbf{z})
$$

$$
C_k=\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2
$$

$$
D_k=c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

$\mathcal{E}_k(\mathbf{z})=A_k+B_k+C_k+D_k$，四项依次是：

- $A_k$：原始间隙；
- $B_k$：对偶间隙；
- $C_k$：Nesterov 距离项；
- $D_k$：外推修正项。

其中 $A_k$、$B_k$ 来自三值函数，$C_k$、$D_k$ 是为外推新加的。

内层要证明的是

$$
\mathcal{E}_{k+1}(\mathbf{z})\le(1-\varsigma)\mathcal{E}_k(\mathbf{z})-\text{负项}
$$

其中 $B_k+C_k$ 正好是 Nesterov 的 Lyapunov 函数 $\mathcal{V}_k$，由对偶 Nesterov 不等式控制；$A_k+D_k$ 由原始梯度步控制。

---

## User (2026-11-12 16:30)

但是我们之前的附录滴 看起来是可以拿过来分析一部分的 但是应该放到哪里 我们就先按照推导的逻辑 写lemma的顺序吧 需要分清楚主次 比如 我们分成几大步 每一步 靠xx到xxlmma得到 然后这几大步得到势函数 然后得到势函数的下降性

---

## Assistant (2026-11-12 16:30)

推导分三大步，前面有一步准备，后面有一个收尾。主线是第一、二步，核心在第一步。

## 准备：值函数的性质

后面每一步都要用到这两个引理。

- **引理 1，值函数正则性。** 内容：$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$ 关于 $\boldsymbol{\lambda}$ Lipschitz；$d_s$ 光滑且 $\frac{1}{s}$-强凹；$p_s$ 可微；$p_s$ 有下界。取自旧附录 D 的 `lem:v2-value-regularity`，下界是新补的。
- **引理 2，鞍点关于中心的灵敏度。** 内容：$\mathbf{x}_s$、$\mathbf{x}_s^\star$ 关于 $\mathbf{z}$ Lipschitz，以及误差界。取自旧附录 D 的 `lem:saddle-center-stability`。新补一条：$\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 的灵敏度，量级为 $\sqrt{s}$。

## 第一步：中心冻结，内层压缩（核心）

目标是

$$
\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\text{负项}
$$

- **引理 3，对偶 Nesterov 不等式（新写）。** 控制 $B_k+C_k=\mathcal{V}_k$：$\mathcal{V}$ 按 $1-\varsigma$ 压缩，代价是若干原始间隙误差。它取代旧附录 D 的 `lem:dual-value-gain`。
- **引理 4，原始步估计。** 控制 $A_k+D_k$，用来支付引理 3 留下的原始间隙误差。改写自旧附录 D `lem:basic-one-step` 的原始部分，要把 $\boldsymbol{\lambda}^k$ 换成 $\bar{\boldsymbol{\lambda}}^k$。
- **引理 5，固定中心压缩。** 由引理 3 和引理 4 合成，路线 2 的系数检查都在这里。

## 第二步：中心移动

- **引理 6，外层中心步。** 估计 $p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)$，取自旧附录 D 的 `lem:z-step-p`。
- **引理 7，中心移动误差（新写）。** 估计 $\mathcal{E}_{k+1}(\mathbf{z}^{k+1})-\mathcal{E}_{k+1}(\mathbf{z}^k)$，由引理 1、2 得到，其中三处 $\sqrt{s}$ 相互抵消。

## 第三步：势函数下降

由引理 5、6、7 合成正文的下降引理。骨架沿用旧附录 D 的 `lem:moving-three-value-descent`，吸收条件改为 $\alpha\propto\varsigma$。

## 收尾：初值与下界

由引理 1 的下界和零初值得到 $\mathcal{W}_0-\mathcal{W}_K\le\Delta_{\mathcal{W}}$。对应旧附录 D `lem:moving-three-value-descent` 的 (a) 部分。

**从旧附录 D 来的有**引理 1、2、4、6 和第三步的骨架；**新写的有**引理 3、5、7。Nesterov 带来的新内容集中在引理 3 和引理 5。

---

## User (2026-11-12 16:30)

然后这个是函数的工作 应该是天眼从 attoch他们的给工作 或者什么最本质的思路和构造 最好是能找出一样的思路和构造 方便我们引用

---

## Assistant (2026-11-12 16:31)

可以直接引用，有现成的同类构造。

## 最接近的构造：Zhang–Xu（arXiv:2609.17973）

它的势函数是 (4.1)：

$$
\mathcal{V}_t=p(z_t)-\inf p+\mathcal{E}_{z_t}(w_t)+c\lVert v_t\rVert^2
$$

- $p$ 是正则化包络，对应我们的 $p_s$；
- $\mathcal{E}_z(w)$ 是以中心 $z$ 度量的内层鞍点跟踪能量，对应我们的 $\mathcal{E}_k(\mathbf{z})$；
- $\lVert v_t\rVert^2$ 是对偶动量项，作用和我们的外推修正项相同。

它的 (9.1)–(9.2) 把一步变化拆成"中心固定的一步变化"加"中心移动引起的变化"，和我们的分解逐项相同。我们的中心移动误差对应它的 Lemma 9.3、9.4。本地全文在 `memory/literature/complexity_2026-09_to_2026-10-03/raw/2609.17973v1.txt`，refer.bib 里已有这一条。

它和我们的区别在于内层能量的具体形式：它用投影外梯度，能量里含外梯度残差和 $\langle v,y-y^\star(z)\rangle$ 这样的交叉项；我们用的是对偶 Nesterov 外推，内层是 Nesterov 的标准 Lyapunov 函数。

## 同一骨架的多循环版本：Pan–Zheng–Li（arXiv:2609.14235）

它的势函数是 $W^t=p_r(\mathbf{z}^t)+2B^t$，其中 $B^t$ 是内层加速求解器 FOAM 的 Lyapunov 函数。每次外层迭代只要求 $B$ 缩小常数倍。我们的 $\mathcal{W}_k=p_s+\frac{1}{2}\mathcal{E}_k$ 和它同形，区别是我们每步都移动中心。

## 组成部分的来源

- **外层包络加内层间隙的三值结构**：Zhang 等人 2020（`zhang2020smoothed`），也就是旧附录 D 的 $\Psi_s$。
- **内层对偶部分** $\mathcal{V}_k=p_s-d_s+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$：Nesterov 估计序列的标准 Lyapunov 函数，引 `nesterov2018lectures`（§2.2 强凸情形）。也可以加引 Wilson、Recht、Jordan 的 *A Lyapunov Analysis of Accelerated Methods in Optimization*（JMLR 2021），它把这个函数写成显式的 Lyapunov 形式。这篇不在 refer.bib 里，卷期和页码要先核对。
- **Attouch**：他的惯性动力系统工作也用"函数值间隙加速度能量"型 Lyapunov 函数，但都是连续时间、凸的情形。我没有找到和本文对应的具体结果，不建议作为构造来源引用。

## 正文可以这样表述（英文）

> Following the potential function of Zhang and Xu [arXiv:2609.17973, (4.1)] and of Pan, Zheng, and Li [arXiv:2609.14235], we couple the envelope \(p_s\) with an inner saddle-tracking energy measured at the current center; for the dual block, the inner energy is the Lyapunov function of Nesterov's method for strongly concave maximization [Nesterov 2018].

这句话说明了 $\mathcal{W}_k$ 的来源。贡献可以落在以下几点：

- 单循环，每步都移动中心；
- 内层只对对偶变量做 Nesterov 外推；
- ALM 形式下乘子不需要投影就有界。

---

## User (2026-11-12 16:34)

Bot的工作 有很多势函数的构造 认为可以从他们的思想里借鉴一些 比如 内层是 Nesterov 的标准 Lyapunov 函数 你说的 为什么标准 最准确的那个参考文献是什么 不在bib你 就要去核对啊 我们可能不是动力系统的工作 数所以可以去看他们的 nesteor的 而不是和我们的竞品 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻 你可能没懂我的意思 你有点傻

---

## Assistant (2026-11-12 16:35)

You've hit your 5-hour limit · resets 8pm (Europe/Vienna)

---

## User (2026-11-12 16:36)

继续继续

---

## Assistant (2026-11-12 16:37)

先说已经核实的部分：**Nesterov 的标准 Lyapunov 函数**，最准确的出处是 Wilson–Recht–Jordan（JMLR 2021）的式 (36)，我已核对原文。下面接着查 Boț 的工作。

**结论**：我们内层对偶部分的 Lyapunov 函数是 Nesterov 强凸加速方法的标准离散 Lyapunov 函数。最准确的出处是 Wilson–Recht–Jordan（JMLR 2021）的式 (36)，我已核对原文。Boț 的工作里最值得借鉴的是 Fast ALM（Math. Program. 2023），它的能量函数和我们的 $\mathcal{V}_k$ 加修正项是同一种构造，而且同样作用在 ALM 的乘子上。两篇都还不在 `refer.bib` 里。

## 1. 为什么称为"标准"

对 $\mu$-强凸、$L$-光滑的 $f$，Nesterov 常动量方法维护两个序列：迭代点 $y_k$ 和估计序列 $z_k$。Wilson–Recht–Jordan 的式 (36) 定义

$$
E_k=A_k\left(\mu D_h(x^\ast,z_k)+f(y_k)-f(x^\ast)\right),\qquad A_k=(1-\sqrt{\mu\delta})^{-k}
$$

取 $h=\frac{1}{2}\lVert\cdot\rVert^2$ 时，括号里就是 $f(y_k)-f^\ast+\frac{\mu}{2}\lVert z_k-x^\ast\rVert^2$。权重 $A_k$ 按几何速度增长，所以括号里的量每步按 $1-\sqrt{\mu\delta}$ 压缩。这一结论见他们的 Proposition 13 和 Corollary 14。原文还说明，取 $\delta\tau=1/\sqrt{\kappa}$ 时，这个格式就是 Nesterov（2004）第 78–79 页的两序列方法。

换到我们的记号：$f\to-d_s$，$\mu\to\frac{1}{s}$，步长 $\delta\to\tau$，$z_k\to\mathbf{w}^k$。括号里的量正好是

$$
\mathcal{V}_k=p_s-d_s(\boldsymbol{\lambda}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2
$$

压缩率是 $\sqrt{\tau/s}=\varsigma$。所以"标准"有确切含义：$\mathcal{V}_k$ 就是 Nesterov 估计序列分析中的 Lyapunov 函数。Wilson–Recht–Jordan 把它写成了显式的形式。

## 2. Boț 的构造：Fast ALM

Boț、Csetnek、Nguyen 的 Fast ALM 讨论凸情形下的线性约束问题。算法对原始变量和乘子都做 Nesterov 外推，见式 (3.3a)、(3.3b)。第 3.2 节的能量函数（式 (3.27) 之后）由三部分组成：

$$
E_k=t_k(t_k-1+\gamma)\left(\mathcal{L}_\beta(x_k,\lambda)-\mathcal{L}_\beta(x,\lambda_k)\right)+\frac{1}{2\rho}\lVert\nu_k-\gamma\lambda\rVert^2+\frac{1-\gamma}{2\rho}(t_k-1)\lVert\lambda_k-\lambda_{k-1}\rVert^2+\cdots
$$

其中乘子的估计序列为

$$
\nu_k=\gamma\lambda_k+(t_k-1)(\lambda_k-\lambda_{k-1})
$$

和我们的构造逐项对应：

- **函数值间隙**：他们用拉格朗日间隙，我们用 $\Psi_s$ 中的原始间隙和对偶间隙。
- **乘子估计序列的距离**：他们的 $\lVert\nu_k-\gamma\lambda\rVert^2$ 对应我们的 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$。两者都是"当前乘子加上动量方向放大若干倍"：他们放大 $t_k-1$ 倍，我们放大 $\varsigma^{-1}$ 倍。
- **乘子速度项**：他们的 $(t_k-1)\lVert\lambda_k-\lambda_{k-1}\rVert^2$ 和我们的修正项 $c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2$ 起同样作用，都用来支付外推产生的偏差。

它的关键一步估计是 Proposition 3.8：$E_{k+1}\le E_k+(\cdots)$ 再减去若干步长平方项。这和我们想要的步长形式下降是同一种写法。

**不同之处**：他们是凸情形，动量 $t_k$ 递增，得到 $O(1/k^2)$；我们的对偶函数 $d_s$ 是 $\frac{1}{s}$-强凹的，动量为常数，得到压缩率 $1-\varsigma$。我们的情形对应 Wilson–Recht–Jordan 的强凸分支。

## 3. 正文可以这样写（英文）

> For the dual block, the inner energy is the discrete Lyapunov function of Nesterov's method for strongly concave maximization [Wilson–Recht–Jordan 2021, (36)], with the multiplier estimate sequence \(\mathbf{w}^k\) playing the role of the auxiliary sequence; a similar energy, combining a Lagrangian gap, the distance of a multiplier estimate sequence and a multiplier-velocity term, is used for the fast ALM of Boț, Csetnek, and Nguyen [Math. Program. 2023].

## 4. 待补的 bib 条目

```bibtex
@article{wilson2021lyapunov,
  author  = {Wilson, Ashia C. and Recht, Benjamin and Jordan, Michael I.},
  title   = {A {L}yapunov Analysis of Accelerated Methods in Optimization},
  journal = {Journal of Machine Learning Research},
  volume  = {22},
  number  = {113},
  pages   = {1--34},
  year    = {2021}
}
@article{bot2023fastalm,
  author  = {Bo{\c{t}}, Radu Ioan and Csetnek, Ern{\"o} Robert and Nguyen, Dang-Khoa},
  title   = {Fast Augmented {L}agrangian Method in the Convex Regime with Convergence Guarantees for the Iterates},
  journal = {Mathematical Programming},
  volume  = {200},
  number  = {1},
  pages   = {147--197},
  year    = {2023},
  doi     = {10.1007/s10107-022-01879-4}
}
```

Fast ALM 的式号和 Proposition 3.8 来自 arXiv:2111.09370 v1，期刊版的编号可能不同，引用前要对照期刊版。要我把这两条写进 `refer.bib` 吗？

Sources:
- [Wilson–Recht–Jordan, JMLR 22(113), 2021](https://jmlr.org/papers/v22/20-195.html)
- [dblp record](https://dblp.org/rec/journals/jmlr/WilsonRJ21.html)
- [Boț–Csetnek–Nguyen, Fast ALM, PMC open access](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10195761/)
- [arXiv:2111.09370](https://arxiv.org/abs/2111.09370)

---

## User (2026-11-12 16:41)

突然想到一个问题 我们实际上和proxiamlALM 就是在对偶子问题上加正则项 不是一一会儿是 我最浅薄的认知是 一个有lambdak一个没有

---

## Assistant (2026-11-12 16:41)

你的理解对了一半。两者在对偶函数上加的是同一个二次项 $-\frac{1}{2s}\lVert\boldsymbol{\lambda}-\boldsymbol{\mu}\rVert^2$，**区别只在中心 $\boldsymbol{\mu}$ 取什么**。在我们的算法族里，这个选择由 $\beta$ 控制：

$$
\boldsymbol{\mu}^{k+1}=\boldsymbol{\mu}^k+\beta(\boldsymbol{\lambda}^{k+1}-\boldsymbol{\mu}^k)
$$

- **$\beta=1$，中心跟着乘子走，即 $\boldsymbol{\mu}^k=\boldsymbol{\lambda}^k$。** 这就是 proximal ALM（Rockafellar 的 proximal method of multipliers），对偶上做的是近端点步。不动点满足 $\boldsymbol{\lambda}=\boldsymbol{\mu}$，所以正则项在极限处消失，不引入偏差。这是"有 $\boldsymbol{\lambda}^k$"的那一种。
- **$\beta=0$，中心固定在 $\boldsymbol{\mu}=\mathbf{0}$。** 这是对偶上的 Tikhonov 正则化，Fast LRALM 用的就是这种。正则项不消失，于是对偶梯度多出 $-\boldsymbol{\lambda}/s$，可行性残差里留下偏差项 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$。所以 $s$ 必须取到 $1/\epsilon$ 量级，乘子有界引理也正是为控制这一项而证的。这是"没有 $\boldsymbol{\lambda}^k$"的那一种。

**两者的代价不同。** 近端版本没有偏差，但对偶函数的强凹性每步都相对于一个移动的中心，没有固定的 $\frac{1}{s}$-强凹目标，Nesterov 的压缩率 $1-\varsigma$ 用不上。固定中心版本以 $1/s$ 的偏差为代价，换来一个固定的、$\frac{1}{s}$-强凹的对偶函数 $d_s$。对偶加速恰好需要这个性质：估计序列的距离项 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$ 必须以一个固定的鞍点 $\boldsymbol{\lambda}_s^\star$ 为参照。

所以 Fast LRALM 取 $\beta=0$，这一选择是加速分析所必需的。族内 $\beta=1$ 的上界 $\epsilon^{-4}$ 与 $\beta=0$ 的上界 $\epsilon^{-3}$ 之差，也反映了这一点。

---

## User (2026-11-12 16:43)

比如我们mu去lambdak 就是proxiamlalm那就是wright他们的工作 或者 是BOt他们的工作 但是因为xx我们不能去 所以我们xx逻辑是这样的吗？

---

## Assistant (2026-11-12 16:44)

逻辑大体是这样，但有两处要说得更准确：引用对象，以及"因为什么不能取"。

**取 $\boldsymbol{\mu}=\boldsymbol{\lambda}^k$ 对应的工作。** 准确的出处是 Rockafellar（1976，`rockafellar1976augmented`）：凸情形下，ALM 的乘子更新本身就是对偶上的近端点步。在我们的算法族里，这对应 $\beta=1$。

Xie–Wright（`xie2021proximal`）的"proximal"指原始变量上的近端项 $\lVert\mathbf{x}-\mathbf{x}^k\rVert^2$，对应我们的中心 $\mathbf{z}$，和对偶中心无关。这一点是我凭记忆说的，引用前要核对原文。Boț 的 Fast ALM 是在凸情形下对乘子做外推，不属于加对偶近端中心的工作。

**不能取的原因。** 加速需要一个固定的强凹对偶函数：

- 取 $\boldsymbol{\mu}=\mathbf{0}$ 时，$d_s(\cdot;\mathbf{z})$ 是固定的 $\frac{1}{s}$-强凹函数，极大点 $\boldsymbol{\lambda}_s^\star$ 也固定。Nesterov 的距离项 $\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star\rVert^2$ 以它为参照，按 $1-\varsigma$ 压缩。
- 取 $\boldsymbol{\mu}=\boldsymbol{\lambda}^k$ 时，对偶目标每步都在变。$\frac{1}{s}$ 的强凹性只相对于一个移动的中心成立，没有固定的极大点可以作为参照，估计序列的论证无从进行。

**完整的逻辑链。** 近端中心 $\boldsymbol{\mu}=\boldsymbol{\lambda}^k$ 不引入偏差，但对偶目标不固定，在我们的族里得到的是 $\epsilon^{-4}$（$\beta=1$ 的上界，与下界匹配）。固定中心 $\boldsymbol{\mu}=\mathbf{0}$ 带来 $\lVert\boldsymbol{\lambda}\rVert/s$ 的偏差，需要 $s\sim1/\epsilon$，再配合乘子一致有界，可以把偏差压下去。作为交换，得到一个固定的强凹对偶函数，族内是 $\epsilon^{-3}$，加上对偶 Nesterov 外推后是 $\epsilon^{-5/2}$。

有一点不要写过头：$\beta=1$ 不能加速，只在我们的算法族内有结论支持，族外没有证明。正文可以写"a fixed dual center makes \(d_s\) a fixed strongly concave function, which the dual extrapolation requires"，不要写成 "proximal ALM cannot be accelerated"。

---

## User (2026-11-12 16:45)

完整的逻辑链。 近端中心 $\boldsymbol{\mu}=\boldsymbol{\lambda}^k$ 不引入偏差，但对偶目标不固定，在我们的族里得到的是 $\epsilon^{-4}$（$\beta=1$ 的上界，与下界匹配）。固定中心 $\boldsymbol{\mu}=\mathbf{0}$ 带来 $\lVert\boldsymbol{\lambda}\rVert/s$ 的偏差，需要 $s\sim1/\epsilon$，再配合乘子一致有界，可以把偏差压下去。作为交换，得到一个固定的强凹对偶函数，族内是 $\epsilon^{-3}$，加上对偶 Nesterov 外推后是 $\epsilon^{-5/2}$。 这个写进到我们的项目里 不要啰嗦

---

## Assistant (2026-11-12 16:46)

这条逻辑链已经写进 [PROJECT_STATUS.md:115](overleaf/notes/progress/PROJECT_STATUS.md#L115)，放在 §4 第 6 条"其余保留小项"之前。同一条里还记了两点：

- 正文只写到"固定的对偶中心让 $d_s$ 成为固定的强凹函数，对偶外推需要这一点"，不写近端 ALM 不能加速，因为族外没有证明。
- `xie2021proximal` 的近端项作用在原始变量上，这是我凭记忆说的，引用前要核对原文。

---

## User (2026-11-12 16:47)

准备：值函数的性质

后面每一步都要用到这两个引理。

引理 1，值函数正则性。 内容：$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})$ 关于 $\boldsymbol{\lambda}$ Lipschitz；$d_s$ 光滑且 $\frac{1}{s}$-强凹；$p_s$ 可微；$p_s$ 有下界。取自旧附录 D 的 lem:v2-value-regularity，下界是新补的。
引理 2，鞍点关于中心的灵敏度。 内容：$\mathbf{x}_s$、$\mathbf{x}_s^\star$ 关于 $\mathbf{z}$ Lipschitz，以及误差界。取自旧附录 D 的 lem:saddle-center-stability。新补一条：$\boldsymbol{\lambda}_s^\star(\mathbf{z})$ 的灵敏度，量级为 $\sqrt{s}$。 这个 我们现在似乎需要写到\subsection{Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}}
\label{app:b2-prime-multiplier-bounds}这个子节后面 直接 这一节就是证明那个引路 然后这个子节有很多小引理 你懂我的意思吗？

---

## Assistant (2026-11-12 16:47)

懂：在乘子有界引理的子节后面新开一个子节，专门证明势函数下降引理，各个小引理按推导顺序放在这个子节里。先写引理 1 和引理 2，我先读旧附录 D、E 和笔记中对应的证明。

两个引理已经写进 [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex)，放在新子节"Proof of Lemma~\ref{lem:b2-prime-potential-descent}"的开头，紧接乘子有界引理的子节。编译没有报错。现有的未定义引用都来自被注释掉的附录 A、B、C，和这次新增的内容无关。

- **`lem:b2-prime-fixed-center-values`，中心固定时的性质。**
  - (i) $\mathbf{x}_s(\cdot;\mathbf{z})$ 是 $G_{\mathcal{A}}/\mu_\gamma$-Lipschitz 的；
  - (ii) 原始间隙夹在两个二次项之间，$\frac{\mu_\gamma}{2}\lVert\mathbf{x}-\mathbf{x}_s\rVert^2\le\mathcal{P}_s-d_s\le\frac{L_x}{2}\lVert\mathbf{x}-\mathbf{x}_s\rVert^2$。这正是三值写法和距离写法之间的桥梁；
  - (iii) 对偶间隙的下界，$p_s-d_s\ge\frac{1}{2s}\lVert\boldsymbol{\lambda}-\boldsymbol{\lambda}_s^\star\rVert^2+\frac{\mu_\gamma}{2}\lVert\mathbf{x}_s(\boldsymbol{\lambda})-\mathbf{x}_s^\star\rVert^2$；
  - (iv) $p_s$ 的下界，$p_s\ge\inf F-\frac{L_h^2}{2(\rho+s)}$。
- **`lem:b2-prime-center-dependence`，对中心的依赖。**
  - $p_s$ 沿中心方向的上估计，中心步估计直接由它得到；
  - $d_s$ 沿中心方向的下估计，中心移动误差要用；
  - $\mathbf{x}_s$、$\mathbf{x}_s^\star$ 的 Lipschitz 常数为 $\frac{1}{\gamma\mu_\gamma}$；
  - $\boldsymbol{\lambda}_s^\star$ 的 Lipschitz 常数为 $\frac{\sqrt{s}}{2\gamma\sqrt{\mu_\gamma}}$。

两个证明都直接从强凸性和强凹性推出，没有用到 $p_s$ 的可微性：中心步只需要上估计，所以旧附录 D 中关于 $\nabla p_s$ 光滑性的那部分没有移植。下一个是对偶 Nesterov 不等式。

---

## User (2026-11-12 16:50)

引理 5，固定中心压缩。 由引理 3 和引理 4 合成，路线 2 的系数检查都在这里。 这个就是$$\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\text{负项}$$形式吗？ 如果是的话 那我们第一步 最好不要写Ak这种 而是写具体的式子，然后不要在lemma中写很多中间结果 只保留 最需要的那个结果 比如 一下子出现好几个不等号 这个这个细节 不需要写 而且不要新引入很多冗余符号 和临时符号 以及  你懂我的意思吗

---

## Assistant (2026-11-12 16:50)

懂，是这个形式。引理 5 的陈述只保留一个不等式，所有量都写成显式表达式：

$$
\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-c_1\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

右端的三个负项，后面的合成都要用到。

按你的要求，写法上遵守三条：

- **$\mathcal{E}_k$ 只在正文定义一次，用显式表达式。** 它在合成中反复出现，所以值得命名。$A_k$、$B_k$ 这类分项名不再引入。
- **陈述里只放最终结果。** 证明里的中间量，比如笔记中的 $e_k$、$r_k$、$\varpi_k$、$\Gamma_k$、$\Gamma_k^+$、$\Gamma_k^\star$，都不引入名字，直接写出范数或函数值之差。实在需要缩写的，只在证明内部局部使用。
- **中间不等式不写进陈述。** 引理 3（对偶 Nesterov）和引理 4（原始步）只在证明引理 5 时用一次，所以不单独陈述，作为引理 5 证明中的两步写出。引理总数由 7 个减到 5 个。

按同样的标准，刚写好的两个引理也要精简：

- `lem:b2-prime-fixed-center-values` 的 (iv)，即 $p_s$ 的下界，只在初值界里用一次，应该移到那里的证明中，不放在这个引理里；
- (ii) 的双边不等式中，两边在引理 5 的证明里都要用到，所以保留。

要我先把 (iv) 移出去，再写引理 5 吗？

---

## User (2026-11-12 16:51)

而且不要过分纠结细节

---

## Assistant (2026-11-12 16:53)

明白，以后不做数值检验，也不再在细节上反复加"待核"。这一条已经记进记忆。

中心固定时的压缩已经写进 [AccelerationProof.tex](overleaf/appendix/AccelerationProof.tex)，编译没有报错。

- **$\mathcal{E}_k(\mathbf{z})$ 的定义**：按显式表达式写，放在引理之前。第二个距离项的权重取 $c_e=\frac{\mu_\gamma}{4}$。
- **`lem:b2-prime-fixed-center-contraction`**：陈述只有一个不等式。

$$
\mathcal{E}_{k+1}(\mathbf{z}^k)\le(1-\varsigma)\mathcal{E}_k-\frac{1}{66\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

- **证明分三段**：
  - **对偶步**：Nesterov 估计序列的计算，留下三个原始间隙；
  - **原始步**：梯度步向 $\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k)$ 压缩，三个原始间隙由此控制；
  - **合并**：$c_e$ 取常数后，$\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2$ 直接出现在右端。

  局部记号只有 $e_k$、$r_k$、$\varpi_k$、$S_k$，都只在证明内部使用。
- **其他改动**：$p_s$ 的下界已经从 `lem:b2-prime-fixed-center-values` 移出，留到初值界里写。`wilson2021lyapunov` 已加入 `refer.bib`。

$c_e$ 现在取 $\frac{\mu_\gamma}{4}$，和正文红色占位块里旧的 $c_e$ 不同。中心移动误差里的常数，按新的 $c_e$ 写就行。下一个是中心移动误差。

---

## User (2026-11-12 17:06)

Lemma A.4. Suppose that Assumptions 2.1 and 2.2 and (6.4) hold. Then, for every k ≥ 0,834
Ek+1(zk) ≤ (1 − ς)Ek − 1
66γ ∥xk+1 − xk∥2 − 1
8τ ∥λk+1 − ¯λk∥2 − ςμγ
2 ∥xk+1 − x⋆
s (zk)∥2. 这个不等式一点都不美 66 可以稍微放缩一下 变成64吗？然后我们的不需要引入kexi吧 我们的动量系数是omga

*[Context was auto-compacted here; the summary repeats the text above and is omitted.]*
