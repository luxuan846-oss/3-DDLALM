# 候选引用核查（2026-11-21）

核查方式：arXiv / Optimization Online 全文下载到 `/tmp/citecheck/<id>/`，`pdftotext` 后 grep 定理、算法、假设与度量；元数据取自 Crossref（DBLP API 被 bot 验证拦截）。页码均指 arXiv（或预印本）PDF 页码。经典书籍和老论文只核对元数据与标准归属。未修改任何 `.tex` / `.bib`。

判定记号：**SUPPORTS**（可直接引）/ **PARTIAL**（可引，但须改写措辞）/ **DOES NOT FIT**（不宜放在拟议位置）。

---

## A. So 组相关

### L1 `li2025nonsmooth`（已在 refer.bib，未引用）
- **记录**：J. Li, L. Zhu, A. M.-C. So. Nonsmooth nonconvex–nonconcave minimax optimization: Primal–dual balancing and iteration complexity analysis. *Math. Program.* 214(1–2):591–641, 2025. DOI 10.1007/s10107-025-02197-1；arXiv:2209.10825。bib 条目缺 DOI。
- **内容**：问题为 $\min_{x\in X}\max_{y\in Y}F(x,y)$，其中 $F(\cdot,y)=h_y\circ c_y$，$h_y$ 凸且 Lipschitz，$Y$ 紧凸（Assumption 3.1，p.7）。Def 3.1（p.7–8）定义 $\epsilon$-OS 与 $\epsilon$-GS；其 GS 的 primal 部分用 proximal 度量 $\lVert\nabla_z d_r(y,x)\rVert$，不是梯度范数。Def 7.1（p.27）给出精确 GS/OS；Remark 7.1（p.28–29）在 $F(x,\cdot)$ 凹时由 OS 构造 GS；Thm 7.1（p.29）在凹情形给出 $\epsilon$-GS 推出 $\mathcal O(\epsilon^{1/2})$-OS。Sec. 6 的问题 (22) 为 $\min_x\max_{y\in Y}y^\top G(x)$，$Y$ 为多面体（p.24），即对偶线性的 nonconvex-linear 结构。算法 smoothed PLDA 的复杂度为 $\mathcal O(\epsilon^{-2\max\{2\theta,1\}})$（KŁ 指数 $\theta$）。
- **判定**：**PARTIAL**。
  - Intro 第 90 行：论文没有证明「共轭形式的 GS 点与 KKT 点重合」，这一事实是直接计算。可引 LZS25 作为 GS 概念及其与 OS 关系的来源。
  - Prelim 第 177 行：LZS25 的 $\epsilon$-GS 是 proximal 版本，与本文的梯度范数版本不同；适合写成 "see also"。
- **建议措辞**：`... whose game-stationary (GS) points~\cite{li2025nonsmooth} coincide with the KKT points of Problem~\eqref{prob:main}.`；Prelim：`... \cite{li2026smoothing,pan2026optimal}; see~\cite{li2025nonsmooth} for the relation between game and optimization stationarity.`

### L2 Li–So–Ma, IEEE SPM 2020（新）
- **记录**：J. Li, A. M.-C. So, W.-K. Ma. Understanding notions of stationarity in nonsmooth optimization: A guided tour of various constructions of subdifferential for nonsmooth functions. *IEEE Signal Process. Mag.* 37(5):18–31, 2020. DOI 10.1109/MSP.2020.3003845；arXiv:2006.14901。
- **内容**：综述 Fréchet、limiting、Clarke 次微分及对应的平稳性概念。Fact 4（p.6）给出复合函数链式法则 $\partial(g\circ F)(x)=\nabla F(x)^\top\partial g(F(x))$（正则性条件下）。p.7 把 $g\circ F$（$g$ 凸 Lipschitz、$F$ 光滑）列为 weakly convex 原型，并以 robust low-rank matrix recovery（$\ell_1$ 损失、$UU^\top$ 分解）为例。文中没有 $\epsilon$-KKT 定义。
- **判定**：**PARTIAL**。适合 Prelim 第 66–68 行（$\epsilon=0$ 时的精确平稳条件），不适合作为 $\epsilon$-KKT 残差的出处。
- **建议措辞**：`... the first-order KKT condition of Problem~\eqref{prob:main}; see~\cite{li2020understanding} for the subdifferential calculus behind this condition.`

### L3 Li–Zhu–So–Vidal, SIOPT 2020（新）
- **记录**：X. Li, Z. Zhu, A. M.-C. So, R. Vidal. Nonconvex robust low-rank matrix recovery. *SIAM J. Optim.* 30(1):660–686, 2020. DOI 10.1137/18M1224738；arXiv:1809.09237。
- **内容**：PSD 情形 (1.4) 为 $\min_U \frac1m\lVert y-\mathcal A(UU^\top)\rVert_1$；一般情形 (1.5) 为 $\min_{U,V}\frac1m\lVert y-\mathcal A(UV^\top)\rVert_1+\lambda\lVert U^\top U-V^\top V\rVert_F$（p.4）。在 $\ell_1/\ell_2$-RIP 下，目标函数 sharp 且 weakly convex，SubGM 局部线性收敛（Thm 3，p.15）。
- **判定**：**SUPPORTS**（Intro 第 32 行与 `charisopoulos2021low` 并列）。(1.4) 是 $f\equiv0$ 的 $h\circ\mathcal A$；(1.5) 多一个平衡正则项，本文例子的无正则形式与 Charisopoulos 等一致。
- **建议措辞**：`\textbf{Robust low-rank matrix recovery}~\cite{charisopoulos2021low,li2020nonconvex}.`

### L4 Zhu–Li, arXiv:2607.08954（新）
- **记录**：L. Zhu, J. Li. Nonconvex composite functional constraints via first-order augmented Lagrangian methods under local regularity. arXiv:2607.08954v2, 2026。
- **内容**：问题为 $\min_{x\in X}h_0(c_0(x))$ s.t. $h_i(c_i(x))\le0$，$X$ 紧，$h_i$ 凸 Lipschitz，$c_i$ 光滑非线性（p.1–2）。Algorithm 1 Smoothed Prox-Linear ALM（p.8）：primal 步精确求解一个强凸 prox-linear 子问题（Remark 3.1 明确只计 outer iterations）；dual 在紧集 $Y$ 上投影；需要可行初始点和足够大的固定罚参数。Thm 4.1（p.13）：(i) 对偶正则 $r_y=\Theta(K^{-1/3})$ 时得到 $\mathcal O(K^{-1/3})$-KKT，即 $\mathcal O(\epsilon^{-3})$；(ii) $r_y=0$ 时，在 piecewise linear 外函数、strict complementarity 与 piecewise LICQ 下得到 $\mathcal O(K^{-1/2})$，即 $\mathcal O(\epsilon^{-2})$。
- **判定**：**PARTIAL**。
  - Intro 第 78–81 行：可作为「固定罚参数加局部正则性得到 $\mathcal O(\epsilon^{-2})$」的又一例，但须注明它面向复合不等式约束，且每步要解 prox-linear 子问题。
  - Intro 第 69–77 行：结果 (i) 属于「依赖 $\epsilon$ 的对偶正则」一类，但它不是单步显式梯度的 single-loop 方法，不宜放入那组单循环引用。
- **建议措辞**：`... or local multiplier regularity together with piecewise-linear structure for composite inequality constraints~\cite{zhu2026nonconvex}.`

### L5 Lu–Zhou, SIOPT 2023（新）
- **记录**：Z. Lu, Z. Zhou. Iteration-complexity of first-order augmented Lagrangian methods for convex conic programming. *SIAM J. Optim.* 33(2):1159–1190, 2023. DOI 10.1137/21M1403837；arXiv:1803.09941。
- **内容**：凸锥规划；I-AL 的 $\epsilon$-KKT 复杂度为 $\mathcal O(\epsilon^{-7/4})$（Thm 2–3，p.8–9）；adaptively regularized I-AL 为 $\mathcal O(\epsilon^{-1}\log\epsilon^{-1})$（Thm 5–6，p.10）。两者都是嵌套循环。
- **判定**：**DOES NOT FIT**。Intro 第 62–64 行讨论的是非凸问题的嵌套 ALM，本文是凸问题。只有在另写一句凸 ALM 复杂度背景时才可引。

### L6 So 组其他工作（按强度排序）
1. **Zhu–Ding–Liu–So, arXiv:2604.04130（新，最强）**。L. Zhu, W. Ding, S. Liu, A. M.-C. So. Primal-dual methods for nonsmooth nonconvex optimization with orthogonality constraints. arXiv:2604.04130, 2026。Algorithm 1 LSALM（p.7）是 single-loop、免子问题求解的线性化光滑 ALM，处理非线性等式约束 $X^\top X=I_n$。罚参数 $\rho$ 固定；对偶正则 $\varepsilon=\mathcal O(K^{-1/3})$；dual 投影到紧集。Thm 4.10（p.13）给出 $\mathcal O(K^{-1/3})$-KKT，即 $\mathcal O(\epsilon^{-3})$；另在 KŁ 下证明序列收敛。**SUPPORTS** Intro 第 69–77 行：该方法的 $\epsilon$-依赖由对偶正则承担，罚参数不随 $\epsilon$ 变化。这也直接对应第 186–190 行「罚参数本身是否必须承担增长」的问题。建议并入 `\cite{hajinezhad2019perturbed,...}` 那组，或写 `... and single-loop linearized smoothing ALMs for orthogonality constraints~\cite{zhu2026primal}`。
2. **L4 Zhu–Li 2607.08954**（见上，PARTIAL）。
3. **L1 Li–Zhu–So 2025**（见上，PARTIAL）。已引用的 So 组工作有 `zheng2023universal`、`pan2026optimal`（Taoli Zheng）、`li2026smoothing`（Jiajin Li）。

---

## B. 概念出处

### S1 Nesterov 1983（新）
- **记录**：Yu. E. Nesterov. A method for solving the convex programming problem with convergence rate $O(1/k^2)$. *Dokl. Akad. Nauk SSSR* 269(3):543–547, 1983；英译 *Soviet Math. Dokl.* 27(2):372–376, 1983。只核对了元数据和标准归属。
- **判定**：Intro 第 325–326 行 **SUPPORTS**，作为 Nesterov extrapolation 的原始出处。Acceleration 第 115 行 **PARTIAL**：常数动量 $\omega=(\sqrt\kappa-1)/(\sqrt\kappa+1)$ 属于强凸情形的格式，出自 `nesterov2018lectures` 第 2.2 节，不是 1983 年论文的 $t_k$ 序列。该处主引保持 `nesterov2018lectures`，1983 年论文只作历史出处。
- **建议措辞**：`Fast LRALM applies Nesterov extrapolation~\cite{nesterov1983method} directly to the dual multiplier update ...`

### S2 凸情形对乘子做 Nesterov 加速的 ALM
- **He–Yuan 2010（新）**：B. He, X. Yuan. On the acceleration of augmented Lagrangian method for linearly constrained optimization. Optimization Online 2760, Oct. 2010（全文已读，8 页）。问题为 $\min\{f(x)\mid Ax=b,\ x\in X\}$，$f$ 凸可微。AALM（p.5，(3.4)）的 $x$ 步为精确 ALM 最小化，**只对乘子**做 FISTA 型外推：$\lambda^{k+1}=\tilde\lambda^k+\frac{t_k-1}{t_{k+1}}(\tilde\lambda^k-\tilde\lambda^{k-1})+\frac{t_k}{t_{k+1}}(\tilde\lambda^k-\lambda^k)$。Thm 3.6（p.7）给出 Lagrangian gap 的 $\mathcal O(1/k^2)$。p.2 还写道 ALM 的罚参数可以固定，不必趋于无穷（引 Nocedal–Wright）。**SUPPORTS**，作为「对乘子做 Nesterov 加速」的先例。
- **Kang–Kang–Jung, COAP 2015（新）**：M. Kang, M. Kang, M. Jung. Inexact accelerated augmented Lagrangian methods. *Comput. Optim. Appl.* 62(2):373–404, 2015. DOI 10.1007/s10589-015-9742-8。全文付费，**未读全文**；摘要称 I-AALM 用可执行的子问题停止准则保持 $\mathcal O(1/k^2)$。**PARTIAL**（待核：全文中的外推位置）。
- **Boț–Csetnek–Nguyen, MP 2023（新）**：R. I. Boț, E. R. Csetnek, D.-K. Nguyen. Fast augmented Lagrangian method in the convex regime with convergence guarantees for the iterates. *Math. Program.* 200(1):147–197, 2023. DOI 10.1007/s10107-022-01879-4；arXiv:2111.09370。Algorithm 1（p.13）对 primal（(3.3a) 的 $y_k$）和 dual（(3.3b) 的 $\mu_k$）**同时**做惯性外推；$x$ 步用 $\nabla f(y_k)$ 线性化，但子问题含 $\lVert Ax-\eta_k\rVert^2$ 项。Thm 3.17/3.18/3.20（p.28 起）给出 primal-dual gap、可行性与目标值的 $\mathcal O(1/k^2)$；Thm 4.3/4.4 证明迭代点收敛。**PARTIAL**：它是快速 ALM 的凸情形先例，但动量不只加在乘子上。
- **位置建议**：Intro 第 325–327 行或 Acceleration 第 160–175 行 Remark：`For linearly constrained convex problems, Nesterov extrapolation of the multiplier accelerates the exact and inexact ALM to an $\mathcal O(1/k^2)$ rate~\cite{he2010acceleration,kang2015inexact}, and inertial primal-dual variants further yield convergence of the iterates~\cite{bot2023fast}.`

### S3 Yang–Yuan, Math. Comp. 2013（新）
- **记录**：J. Yang, X. Yuan. Linearized augmented Lagrangian and alternating direction methods for nuclear norm minimization. *Math. Comp.* 82(281):301–329, 2013. DOI 10.1090/S0025-5718-2012-02598-1（预印本 Optimization Online 2534，全文已读）。
- **内容**：LALM (3.7)（预印本 p.8）对 $\min\lVert X\rVert_*$ s.t. $\mathcal AX=b$ 线性化 ALM 子问题中的二次罚项，得到 $X^{k+1}=D_{\tau/\beta}(X^k-\tau g^k)$ 与 $\lambda^{k+1}=\lambda^k+\beta(b-\mathcal AX^{k+1})$。$\beta$ 固定，$\tau\lt 1/\rho(\mathcal A^*\mathcal A)$。Thm 3.3（p.9）证明全局收敛，没有复杂度。
- **判定**：**SUPPORTS**，作为「linearized ALM」这一名称与格式的早期出处（凸、线性约束）。
- **建议措辞**：`By Lemma~\ref{lem:reduced-al}, linearized ALM~\cite{yang2013linearized,luSingleLoopGradientDescent2022}, which replaces ...`

### S4 固定罚参数是 ALM 相对罚函数法的经典优势
- **`bertsekas1982`（已在 bib，未引用）**：全文 PDF（MIT 主页扫描版）已查。§2.2.5 *Comparison with the Penalty Method—Computational Aspects*（p.121）原文："It follows, from Proposition 2.6, that *it is not necessary to increase $c_k$ to infinity in order to induce convergence in the method of multipliers*. This is an important advantage, since it results in elimination or at least moderation of the ill-conditioning problem." **SUPPORTS**，与第 186–187 行的意思一致。
- **`nocedal2006numerical`（已在 bib）**：标准归属为第 2 版 §17.3 *Augmented Lagrangian Method: Equality Constraints*，Theorem 17.5（$\mu$ 超过阈值后 $x^*$ 是 $\mathcal L_A(\cdot,\lambda^*;\mu)$ 的严格局部极小点）。**未对照全文**，按标准归属判 **PARTIAL**。bib 条目格式错误（只有 author = Nocedal，并误用 `journal`），应改为 `@book`，作者 Nocedal, J. and Wright, S. J.，*Numerical Optimization*, 2nd ed., Springer, 2006, DOI 10.1007/978-0-387-40065-5。
- **Birgin–Martínez 2014（新）**：E. G. Birgin, J. M. Martínez. *Practical Augmented Lagrangian Methods for Constrained Optimization*. SIAM, Fundamentals of Algorithms 10, 2014. DOI 10.1137/1.9781611973365。第 7 章为 *Boundedness of the penalty parameters*（目录已核，正文未读）。Algencan 按可行性进展自适应增大罚参数，第 7 章给出其有界的条件。**PARTIAL**：可支持「罚参数保持有界是期望性质」，不支持「保持固定」。
- **补充发现**：K. Deng, R. Wang, Z. Zhu, J. Zhang, Z. Wen. The augmented Lagrangian methods: Overview and recent advances. *SIAM Rev.* 68(3):471–576, 2026. DOI 10.1137/24M1706153；arXiv:2510.16827。结论节（arXiv p.91）把 "convergence analysis with constant penalty parameter in nonconvex case" 列为待研究方向。**SUPPORTS** 第 188–190 行的 "remain open"。
- **建议措辞**：`Keeping the penalty parameter fixed is a classical appeal of ALMs over penalty methods~\cite{bertsekas1982,nocedal2006numerical}, ... remain open~\cite{deng2026augmented}.`

### S5 Variable smoothing 的出处（Intro 第 71 行）
- **`bot2015variable`（已在 bib）**：R. I. Boț, C. Hendrich. A variable smoothing algorithm for solving convex optimization problems. *TOP* 23(1):124–150, 2015. DOI 10.1007/s11750-014-0326-z；arXiv:1207.3254。问题为凸的 $\inf\{f(x)+g(Kx)\}$，用参数变化的 Moreau envelope 光滑后套快速梯度法：variable smoothing 为 $\mathcal O(\ln k/k)$（Thm 1、3，p.6 起），constant smoothing 为 $\mathcal O(1/k)$（Thm 2、4）。**SUPPORTS**，作为 variable smoothing 的出处。bib 作者拼写错误："Hendrick" 应为 "Hendrich"。
- **`boct2020variable`（已在 bib）**：Boț–Böhm, *J. Sci. Comput.* 85(2):33, 2020. DOI 10.1007/s10915-020-01332-8；arXiv:1905.06553。凸、随机梯度版的 variable smoothing。**PARTIAL**（属于随机推广，可选）。
- **`nesterov2005smooth`（已在 bib）**：固定光滑参数、取 $\mu\sim\epsilon$ 的光滑化技术的标准出处。**SUPPORTS**（只核对了元数据）。
- **注意**：`bohm2021variable`（Böhm–Wright, JOTA 2021；arXiv:2003.07612）的问题 (1) 是 $h(x)+g(Ax)$，$A$ 为**矩阵**（p.2）；Thm 4.1（p.11）取 $\mu_k\propto k^{-1/3}$，得 $\mathcal O(\epsilon^{-3})$。本文第 71 行把它放在非线性 $\mathcal A$ 的语境中，需要补一个非线性映射的引用，见 M6 的 `deng2025single`。
- **建议措辞**：`Variable smoothing~\cite{bot2015variable,bohm2021variable,deng2025single} replaces $h$ with its Moreau envelope ...`

### S6 复合问题与 prox-linear 方法
- **Lewis–Wright, MP 2016（新）**：A. S. Lewis, S. J. Wright. A proximal method for composite minimization. *Math. Program.* 158(1–2):501–546, 2016. DOI 10.1007/s10107-015-0943-9；arXiv:0812.0423。问题为 $\min h(c(x))$，$h$ 凸或 prox-regular，$c$ 光滑。ProxDescent（Alg. 1，p.1；Alg. 2）每步求解线性化加正则的子问题；结果为全局收敛与 active manifold identification，没有复杂度。**SUPPORTS** 第 61 行 prox-linear 方法（嵌套）。
- **Burke 1985（新）**：J. V. Burke. Descent methods for composite nondifferentiable optimization problems. *Math. Program.* 33(3):260–279, 1985. DOI 10.1007/BF01584377。只核对元数据与标准归属，Lewis–Wright 在 p.11 把它作为同类复合函数方法的先例。**SUPPORTS**（经典出处）。
- **`Drusvyatskiy2019`** = D. Drusvyatskiy, C. Paquette. Efficiency of minimizing compositions of convex functions and smooth maps. *Math. Program.* 178(1):503–558, 2019. DOI 10.1007/s10107-018-1311-3。现有用法正确。
- **建议措辞**：`Prox-linear methods~\cite{burke1985descent,lewis2016proximal,Drusvyatskiy2019}, ...`

### S7 Nemirovski–Yudin 1983（新）
- **记录**：A. S. Nemirovsky, D. B. Yudin. *Problem Complexity and Method Efficiency in Optimization*. Wiley-Interscience, 1983。只核对元数据。oracle / problem-class 复杂度框架的标准出处。
- **判定**：**SUPPORTS**（Prelim 第 72 行，与 `carmon2020lower` 并列）。
- **建议措辞**：`we specify the problem class and the oracle model~\cite{nemirovski1983problem,carmon2020lower} for Problem~\eqref{prob:main}.`

### S8 Pointwise maximum 与 data subgroups（Intro 第 44 行）
- **`zhang2020smoothed`（已引用）**：arXiv:2010.15768 的 (1.3)（p.2）就是 $\min_x\max_{1\le i\le m}f_i(x)$。Sec. 2（p.4）的 (2.1) 为多分布 robust learning（$f_i$ 是第 $i$ 个分布下的期望损失），(2.2) 为按类别的 fairness 训练。**SUPPORTS**，现有引用成立。
- **Sagawa et al., ICLR 2020（新）**：S. Sagawa, P. W. Koh, T. B. Hashimoto, P. Liang. Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. ICLR 2020；arXiv:1911.08731。(4)（p.3）为最差组经验风险 $\min_\theta\max_g\mathbb E_{\hat P_g}[\ell(\theta;(x,y))]$。**SUPPORTS**，作为 "losses on $m$ data subgroups" 的应用出处。
- **建议措辞**：`\textbf{Minimizing a pointwise maximum}~\cite{zhang2020smoothed}. For smooth losses ..., such as the losses on $m$ data subgroups in group distributionally robust learning~\cite{sagawa2020distributionally}, ...`

### S9 `moreau1965`（已在 bib，未引用）
- J.-J. Moreau. Proximité et dualité dans un espace hilbertien. *Bull. Soc. Math. France* 93:273–299, 1965. DOI 10.24033/bsmf.1625。Moreau envelope 的标准出处。**SUPPORTS**（Intro 第 72 行：`its Moreau envelope~\cite{moreau1965}`）。

### S10–S12 单循环 splitting / ADMM 的 KL 全局收敛
| 文献 | 映射 | 罚参数 | 结果 | 复杂度 |
|---|---|---|---|---|
| Li–Pong, SIOPT 25(4):2434–2460, 2015（新） | 线性满射 $M$ | 固定、足够大 | Thm 1（p.7）聚点平稳；Thm 3（p.13）半代数下全序列收敛 | 无 |
| Hong–Luo–Razaviyayn, SIOPT 26(1):337–364, 2016（新） | 线性约束，consensus/sharing 结构 | 固定、足够大 | Thm 2.4 收敛到平稳集 | Thm 2.5（p.13）：平方残差 $P\le\epsilon$ 需 $\mathcal O(1/\epsilon)$ 步，按范数即 $\mathcal O(\epsilon^{-2})$ |
| `Bolte2018`（BST, MOR 43(4):1210–1232） | **非线性** $F$，$h$ 下半连续 | 自适应，**有限步后稳定**（Sec. 4.2，p.15） | Def 2.3（p.8）uniform regularity，即 $\nabla F(x)$ 一致满射；Thm 3.2（p.13）半代数下有界序列全局收敛 | 无 |
| `bot2019proximal`（BCN, SIOPT 29(2):1300–1328） | $F(Ax)+G(y)+H(x,y)$，$A$ 线性满射 | 固定 | full splitting 单循环；KL 下全局收敛，Łojasiewicz 速率（Thm 14、16，p.20 起） | 无 $\epsilon$ 复杂度 |
| `boct2020proximal` = `bot2020proximal`（BN, MOR 45(2):682–712） | $f+g(Ax)+h$，$A$ 线性满射 | 固定、足够大 | proximal ADMM 与线性化版本；KL 收敛、Łojasiewicz 速率（Thm 14、18、20） | 无 $\epsilon$ 复杂度 |

- **判定**：五篇都没有给出 $\mathcal O(\epsilon^{-3})$ 型复杂度。除 BST18 外都只处理线性映射，且都依赖满射性或一致正则性。因此它们不适合放在第 66–68 行的「单循环 $\mathcal O(\epsilon^{-3})$」语境中。它们适合放在第 78–81 行「固定罚参数依赖结构正则性」的位置。BST18 **SUPPORTS**（非线性 $F$ 加一致正则性）；其余 **PARTIAL**（线性映射加满射性）。
- **重复条目**：`boct2020proximal`（第 453 行）与 `bot2020proximal`（第 1501 行）是同一篇，保留一个即可（建议补 DOI 10.1287/moor.2019.1008）。
- **建议措辞**（接在第 81 行后）：`Under surjectivity of the linear map or uniform regularity of the Jacobian, splitting and ADMM schemes with a fixed, sufficiently large penalty converge globally to critical points under the Kurdyka--{\L}ojasiewicz property~\cite{li2015global,Bolte2018,bot2019proximal,bot2020proximal}, and an $\mathcal O(\epsilon^{-2})$ rate holds for consensus and sharing problems~\cite{hong2016convergence}.`

---

## C. 同方向

### M1 光滑 NC-C minimax 的 $\epsilon^{-5/2}$ 多循环结果（Intro 第 305 行）
| 文献 | GS 型度量？ | 速率 | 位置 |
|---|---|---|---|
| Lin–Jin–Jordan, COLT 2020（新） | 是（Def 5：双侧 gradient mapping） | $\tilde{\mathcal O}(\epsilon^{-2.5})$（含 $\log^2$）；对 $\Phi$ 的平稳性为 $\tilde{\mathcal O}(\epsilon^{-3})$ | Corollary 13；Table 2。Minimax-PPA，三重循环，$X,Y$ 有界 |
| Ostrovskii–Lowy–Razaviyayn, SIOPT 31(4):2508–2538, 2021（新） | 是（$(\epsilon_x,\epsilon_y)$-FNE，比 proximal gradient norm 更强） | $\tilde{\mathcal O}(\epsilon_x^{-2}\epsilon_y^{-1/2})$，即 $\tilde{\mathcal O}(\epsilon^{-2.5})$ | Thm 4.1（p.12）；$Y$ 紧；多循环 |
| `kong2021accelerated`（已引用） | 是（primal-dual stationarity） | $\mathcal O(\rho_x^{-2}\rho_y^{-1/2})$，即 $\epsilon^{-2.5}$ | Table 1.1（arXiv:1905.13433 p.3）；AIPP-S，多循环 |
| Thekumparampil et al., NeurIPS 2019 | 否（Moreau envelope of $\Phi$，OS） | $\tilde{\mathcal O}(\epsilon^{-3})$ | Thm 2（p.8） |
| Nouiehed et al., NeurIPS 2019 | 是（FNE） | $\tilde{\mathcal O}(\epsilon^{-3.5})$ | Thm 4.2（p.7） |

- **判定**：Lin–Jin–Jordan 与 Ostrovskii 等 **SUPPORTS**（需注明 up to logarithmic factors）；Thekumparampil 与 Nouiehed **DOES NOT FIT** $\epsilon^{-5/2}$ 的 GS 句。
- **建议措辞**：`This rate is attained, up to logarithmic factors, by multi-loop schemes~\cite{lin2020near,ostrovskii2021efficient,kong2021accelerated,pan2026optimal} ...`

### M2 单循环 NC-C GDA 的 $\epsilon^{-4}$（Intro 第 95–99 行）
- **Yang–Orvieto–Lucchi–He, AISTATS 2022**（arXiv:2112.05604）：假设对 $y$ 满足 **PL 条件**（NC-PL），不是 NC-C。AGDA 为 $\mathcal O(\kappa^2\epsilon^{-2})$，Smoothed-AGDA 为 $\mathcal O(\kappa\epsilon^{-2})$（摘要；Table 1，p.3）。**DOES NOT FIT**。
- **Boț–Böhm, SIOPT 33(3):1884–1913, 2023**（arXiv:2007.13605）：单循环 alternating proximal-gradient；确定性 NC-C 为 $\mathcal O(\epsilon^{-6})$，随机为 $\mathcal O(\epsilon^{-8})$，度量是 $\max_y\Psi$ 的 Moreau envelope 平稳性（OS）（Table 1，p.4；Thm 3.1）。**DOES NOT FIT** $\epsilon^{-4}$ 句；对第 95–96 行的 $\mathcal O(\epsilon^{-6})$ 句为 **PARTIAL**：`two-timescale GDA and its alternating proximal variant require $\mathcal O(\epsilon^{-6})$ iterations~\cite{lin2020gradient,bot2023alternating}`。
- `xu2023unified` 已引用，不再重复。

### M3 `liu2026lower`（已在 bib，未引用）
- **记录**：W. Liu, Q. Lin, Y. Xu. Lower complexity bounds of first-order methods for affinely constrained composite nonconvex problems. *Math. Oper. Res.* 51(2):1659–1682, 2026. DOI 10.1287/moor.2023.0377；arXiv:2307.07605（arXiv 标题不同：*First-order methods for affinely constrained composite non-convex non-smooth problems: Lower complexity bound and near-optimal methods*）。
- **内容**：问题为 $\min f_0(x)+\bar g(\bar Ax+\bar b)$ s.t. $Ax+b=0$，$\bar g$ 凸、下半连续（Assumption 1，p.2）。算法类为满足 linear-span 型 oracle 假设（Assumption 2/3）的全部 FOM。Thm 2.1（p.18）与 Thm 3.1（分裂形式）的下界为 $\Omega(\kappa([\bar A;A])L_f\Delta\,\epsilon^{-2})$。$\epsilon$-平稳的定义 (1.7)/(1.8)（p.6）就是 KKT 残差。Thm 4.1 的 IPG（嵌套）在对数因子内匹配。
- **判定**：**PARTIAL，与第 186–190 行互补，不矛盾**。它是**算法类**下界，但量级只有 $\epsilon^{-2}$，不刻画单循环 $\epsilon^{-3}$ 或 $\epsilon^{-4}$ 的障碍。因此「超过 $\epsilon^{-2}$ 的单循环下界只针对单个算法」仍然成立。注意：其硬实例含仿射等式约束，相当于 $h$ 含 $\{0\}$ 的指示函数，不满足本文 $h$ 的 Lipschitz 常数 $L_h$，所以不能直接说它属于本文的 problem class。
- **建议措辞**（Figure caption）：`The baseline lower bound $\Omega(\epsilon^{-2})$ is due to~\cite{carmon2020lower}; a lower bound of the same order holds for affinely constrained composite problems~\cite{liu2026lower}.` 也可在第 188 行前加：`Existing algorithm-class lower bounds~\cite{carmon2020lower,liu2026lower} are of order $\epsilon^{-2}$, while ...`

### M4 Li–Xu, INFORMS J. Optim. 2021（新）
- **记录**：Z. Li, Y. Xu. Augmented Lagrangian-based first-order methods for convex-constrained programs with weakly convex objective. *INFORMS J. Optim.* 3(4):373–397, 2021. DOI 10.1287/ijoo.2021.0052；arXiv:2003.08880。
- **内容**：问题为 $\min f_0(x)$ s.t. $Ax=b$、$f(x)\le0$（凸约束），$f_0$ 弱凸复合。方法框架是 proximal point：每个 PP 子问题交替用 iALM 和 penalty（以 iALM 的乘子估计为输入）近似求解，属于多重循环。Thm 7（p.22，非凸情形）在 Slater 条件下给出 $\epsilon$-KKT 的 $\mathcal O(\epsilon^{-5/2}\lvert\log\epsilon\rvert)$。
- **判定**：**SUPPORTS** Intro 第 308–312 行（嵌套的 $\epsilon^{-5/2}$ 阶 ALM）。
- **建议措辞**：`... inexact ALM or penalty methods with accelerated inner solvers~\cite{li2021rate,li2021augmented,lin2022complexity,kong2023iteration}.`

### M5 `grapiglia2021complexity`（已在 bib，未引用）
- G. N. Grapiglia, Y. Yuan. On the complexity of an augmented Lagrangian method for nonconvex optimization. *IMA J. Numer. Anal.* 41(2):1546–1568, 2021；arXiv:1906.05622。非凸约束问题上的 inexact ALM（嵌套）。罚参数有界时需 $\mathcal O(\lvert\log\epsilon\rvert)$ 个外迭代（Thm 2.7，p.9）；无界时为 $\mathcal O(\epsilon^{-2/(\alpha-1)})$（Thm 2.8）；线性约束配一阶内解器时总复杂度为 $\mathcal O(\lvert\log\epsilon\rvert^2\epsilon^{-2})$（Thm 3.4，p.15）。
- **判定**：**SUPPORTS** Intro 第 62–64 行（inexact ALMs）。
- **建议措辞**：`... inexact or proximal augmented Lagrangian methods (ALMs)~\cite{sahin2019inexact,grapiglia2021complexity,li2021rate,xie2021proximal} ...`

### M6 bib 中未引用的条目
| key | 实际内容 | 单循环？ | 罚 / 光滑参数 | 速率 | 判定 |
|---|---|---|---|---|---|
| `deng2025single` | Deng–Peng–Wu, arXiv:2505.09485：紧流形上 $\mathbb E f+h(c(x))$，$c$ **非线性**，$h$ 弱凸 | 是 | 光滑参数 $\mu_k=k^{-1/3}$ | Thm 3.1（p.9）：$\mathcal O(\epsilon^{-3})$ | **PARTIAL**（第 71 行 variable smoothing 的非线性映射例子；注明 stochastic/Riemannian） |
| `berahas2025linearized` | 即 El Bourkhissi–Necoara–Patrinos–Tran-Dinh, arXiv:2503.01056 | 是 | perturbed ALM | $\mathcal O(\epsilon^{-3})$ | **重复条目**：与已引用的 `elbourkhissi2025perturbed` 相同，key 名也错，应删除 |
| `hu2026fixed` | "Workshop presentation"，arXiv 与网络上均未找到公开文本 | — | — | — | **DOES NOT FIT**（无法核实） |
| `jin2022nested` | "Jin, Wang, NeurIPS 2022"，条目自带 "Verify…may be different paper"；arXiv 检索无此文 | — | — | — | **DOES NOT FIT**（疑似虚构） |
| `shi2022linearized` | "arXiv:2211.XXXXX"，占位符；检索无此文 | — | — | — | **DOES NOT FIT**（疑似虚构） |
| `lu2022single` | "Lu, Mei, arXiv preprint"，检索无此文 | — | — | — | **DOES NOT FIT**（疑似虚构；相近的真实工作是已引用的 `luSingleLoopGradientDescent2022` 与 `alacaoglu2024complexity`） |

---

## 汇总表

| id | key / new | verdict | location | evidence |
|---|---|---|---|---|
| L1 | `li2025nonsmooth` | PARTIAL | Intro 90；Prelim 177（see also） | Def 3.1 p.7–8；Def 7.1 p.27；Thm 7.1 p.29；Sec. 6 (22) p.24 |
| L2 | new `li2020understanding` | PARTIAL | Prelim 66–68（精确 KKT 条件） | Fact 4 chain rule p.6；无 $\epsilon$-KKT |
| L3 | new `li2020nonconvex` | SUPPORTS | Intro 32 | (1.4)、(1.5) p.4；Thm 3 p.15 |
| L4 | new `zhu2026nonconvex` | PARTIAL | Intro 78–81 | Alg. 1 p.8（prox-linear 子问题）；Thm 4.1 p.13 |
| L5 | new（Lu–Zhou） | DOES NOT FIT | — | 凸锥规划；Thm 2–6 |
| L6 | new `zhu2026primal` | SUPPORTS | Intro 69–77 | LSALM 单循环、固定 $\rho$、对偶正则 $\mathcal O(K^{-1/3})$；Thm 4.10 p.13 |
| S1 | new `nesterov1983method` | SUPPORTS / PARTIAL | Intro 325–326 / Acc 115（只作历史出处） | 标准归属；常数动量出自 `nesterov2018lectures` |
| S2a | new `he2010acceleration` | SUPPORTS | Intro 325–327；Acc Remark | 只对乘子外推 (3.4) p.5；Thm 3.6 p.7 |
| S2b | new `kang2015inexact` | PARTIAL | 同上 | 仅读摘要 |
| S2c | new `bot2023fast` | PARTIAL | 同上 | primal 与 dual 同时外推 (3.3a–b) p.13；Thm 3.17 p.28 |
| S3 | new `yang2013linearized` | SUPPORTS | Prelim 158 | LALM (3.7) p.8；Thm 3.3 p.9 |
| S4a | `bertsekas1982` | SUPPORTS | Intro 186–187 | §2.2.5 p.121 原文 |
| S4b | `nocedal2006numerical` | PARTIAL | Intro 186–187 | §17.3 Thm 17.5（标准归属，未读全文）；bib 格式需修 |
| S4c | new `birgin2014practical` | PARTIAL | Intro 186–187 | 第 7 章 "Boundedness of the penalty parameters"（目录） |
| S4d | new `deng2026augmented` | SUPPORTS | Intro 188–190 "remain open" | SIAM Rev. 结论节 arXiv p.91 |
| S5a | `bot2015variable` | SUPPORTS | Intro 71 | Thm 1/3 $\mathcal O(\ln k/k)$ p.6；作者拼写需改为 Hendrich |
| S5b | `boct2020variable` | PARTIAL | Intro 71（可选） | 随机凸推广 |
| S5c | `nesterov2005smooth` | SUPPORTS | Intro 71 | 标准归属 |
| S6a | new `lewis2016proximal` | SUPPORTS | Intro 61 | ProxDescent，Alg. 1–2 |
| S6b | new `burke1985descent` | SUPPORTS | Intro 61 | 标准归属 |
| S6c | `Drusvyatskiy2019` | （已引用，正确） | Intro 61 | Drusvyatskiy–Paquette MP 2019 |
| S7 | new `nemirovski1983problem` | SUPPORTS | Prelim 72 | 标准归属 |
| S8a | `zhang2020smoothed` | SUPPORTS | Intro 44 | (1.3) p.2；(2.1)–(2.2) p.4 |
| S8b | new `sagawa2020distributionally` | SUPPORTS | Intro 44 | (4) p.3 |
| S9 | `moreau1965` | SUPPORTS | Intro 72 | 标准归属 |
| S10 | new `li2015global` | PARTIAL | Intro 81 后新句 | Thm 1 p.7；Thm 3 p.13；线性满射 |
| S11 | new `hong2016convergence` | PARTIAL | Intro 81 后新句 | Thm 2.5 p.13（按范数即 $\epsilon^{-2}$） |
| S12a | `Bolte2018` | SUPPORTS | Intro 81 后新句 | 非线性 $F$；Def 2.3 p.8；Thm 3.2 p.13 |
| S12b | `bot2019proximal` | PARTIAL | 同上 | 线性满射 $A$；KL |
| S12c | `bot2020proximal` / `boct2020proximal` | PARTIAL | 同上 | 重复条目，保留一个 |
| M1a | new `lin2020near` | SUPPORTS | Intro 305 | Cor. 13；Def 5 |
| M1b | new `ostrovskii2021efficient` | SUPPORTS | Intro 305 | Thm 4.1 p.12 |
| M1c | Thekumparampil / Nouiehed | DOES NOT FIT | — | 分别为 OS 的 $\epsilon^{-3}$、GS 的 $\epsilon^{-3.5}$ |
| M2a | Yang et al. 2022 | DOES NOT FIT | — | NC-PL，不是 NC-C |
| M2b | new `bot2023alternating` | DOES NOT FIT 95–99 / PARTIAL 95–96 | Intro 96（$\epsilon^{-6}$ 句） | Table 1 p.4：NC-C 确定性 $\mathcal O(\epsilon^{-6})$，OS |
| M3 | `liu2026lower` | PARTIAL（互补） | Figure caption / Intro 188 | Thm 2.1 p.18：$\Omega(\kappa\epsilon^{-2})$，linear-span FOM |
| M4 | new `li2021augmented` | SUPPORTS | Intro 311 | Thm 7 p.22：$\tilde{\mathcal O}(\epsilon^{-5/2})$，多循环 |
| M5 | `grapiglia2021complexity` | SUPPORTS | Intro 63 | Thm 2.7 p.9；Thm 3.4 p.15 |
| M6a | `deng2025single` | PARTIAL | Intro 71 | Thm 3.1 p.9，$\mu_k=k^{-1/3}$ |
| M6b | `berahas2025linearized` | 重复 | 删除 | 与 `elbourkhissi2025perturbed` 相同 |
| M6c | `hu2026fixed`、`jin2022nested`、`shi2022linearized`、`lu2022single` | DOES NOT FIT | — | 无法核实或疑似虚构 |

---

## 新增 BibTeX（SUPPORTS / PARTIAL 且不在 refer.bib 中）

```bibtex
@article{li2020understanding,
  author  = {Li, Jiajin and So, Anthony Man-Cho and Ma, Wing-Kin},
  title   = {Understanding Notions of Stationarity in Nonsmooth Optimization: A Guided Tour of Various Constructions of Subdifferential for Nonsmooth Functions},
  journal = {IEEE Signal Processing Magazine},
  volume  = {37},
  number  = {5},
  pages   = {18--31},
  year    = {2020},
  doi     = {10.1109/MSP.2020.3003845}
}

@article{li2020nonconvex,
  author  = {Li, Xiao and Zhu, Zhihui and So, Anthony Man-Cho and Vidal, Ren{\'e}},
  title   = {Nonconvex Robust Low-Rank Matrix Recovery},
  journal = {SIAM Journal on Optimization},
  volume  = {30},
  number  = {1},
  pages   = {660--686},
  year    = {2020},
  doi     = {10.1137/18M1224738}
}

@misc{zhu2026nonconvex,
  author        = {Zhu, Linglingzhi and Li, Jiajin},
  title         = {Nonconvex Composite Functional Constraints via First-Order Augmented {L}agrangian Methods under Local Regularity},
  year          = {2026},
  howpublished  = {arXiv preprint arXiv:2607.08954},
  eprint        = {2607.08954},
  archivePrefix = {arXiv},
  primaryClass  = {math.OC}
}

@misc{zhu2026primal,
  author        = {Zhu, Linglingzhi and Ding, Wentao and Liu, Shangyuan and So, Anthony Man-Cho},
  title         = {Primal-Dual Methods for Nonsmooth Nonconvex Optimization with Orthogonality Constraints},
  year          = {2026},
  howpublished  = {arXiv preprint arXiv:2604.04130},
  eprint        = {2604.04130},
  archivePrefix = {arXiv},
  primaryClass  = {math.OC}
}

@article{nesterov1983method,
  author  = {Nesterov, Yurii E.},
  title   = {A method for solving the convex programming problem with convergence rate {$O(1/k^2)$}},
  journal = {Soviet Mathematics Doklady},
  volume  = {27},
  number  = {2},
  pages   = {372--376},
  year    = {1983}
}

@misc{he2010acceleration,
  author       = {He, Bingsheng and Yuan, Xiaoming},
  title        = {On the Acceleration of Augmented {L}agrangian Method for Linearly Constrained Optimization},
  year         = {2010},
  howpublished = {Optimization Online, 2760},
  url          = {https://optimization-online.org/2010/10/2760/}
}

@article{kang2015inexact,
  author  = {Kang, Myeongmin and Kang, Myungjoo and Jung, Miyoun},
  title   = {Inexact Accelerated Augmented {L}agrangian Methods},
  journal = {Computational Optimization and Applications},
  volume  = {62},
  number  = {2},
  pages   = {373--404},
  year    = {2015},
  doi     = {10.1007/s10589-015-9742-8}
}

@article{bot2023fast,
  author  = {Bo{\c{t}}, Radu Ioan and Csetnek, Ern{\"o} Robert and Nguyen, Dang-Khoa},
  title   = {Fast Augmented {L}agrangian Method in the Convex Regime with Convergence Guarantees for the Iterates},
  journal = {Mathematical Programming},
  volume  = {200},
  number  = {1},
  pages   = {147--197},
  year    = {2023},
  doi     = {10.1007/s10107-022-01879-4}
}

@article{yang2013linearized,
  author  = {Yang, Junfeng and Yuan, Xiaoming},
  title   = {Linearized Augmented {L}agrangian and Alternating Direction Methods for Nuclear Norm Minimization},
  journal = {Mathematics of Computation},
  volume  = {82},
  number  = {281},
  pages   = {301--329},
  year    = {2013},
  doi     = {10.1090/S0025-5718-2012-02598-1}
}

@book{birgin2014practical,
  author    = {Birgin, Ernesto G. and Mart{\'i}nez, Jos{\'e} Mario},
  title     = {Practical Augmented {L}agrangian Methods for Constrained Optimization},
  series    = {Fundamentals of Algorithms},
  volume    = {10},
  publisher = {SIAM},
  address   = {Philadelphia, PA},
  year      = {2014},
  doi       = {10.1137/1.9781611973365}
}

@article{deng2026augmented,
  author  = {Deng, Kangkang and Wang, Rui and Zhu, Zhenyuan and Zhang, Junyu and Wen, Zaiwen},
  title   = {The Augmented {L}agrangian Methods: Overview and Recent Advances},
  journal = {SIAM Review},
  volume  = {68},
  number  = {3},
  pages   = {471--576},
  year    = {2026},
  doi     = {10.1137/24M1706153}
}

@article{lewis2016proximal,
  author  = {Lewis, Adrian S. and Wright, Stephen J.},
  title   = {A Proximal Method for Composite Minimization},
  journal = {Mathematical Programming},
  volume  = {158},
  number  = {1--2},
  pages   = {501--546},
  year    = {2016},
  doi     = {10.1007/s10107-015-0943-9}
}

@article{burke1985descent,
  author  = {Burke, James V.},
  title   = {Descent Methods for Composite Nondifferentiable Optimization Problems},
  journal = {Mathematical Programming},
  volume  = {33},
  number  = {3},
  pages   = {260--279},
  year    = {1985},
  doi     = {10.1007/BF01584377}
}

@book{nemirovski1983problem,
  author    = {Nemirovsky, Arkadi S. and Yudin, David B.},
  title     = {Problem Complexity and Method Efficiency in Optimization},
  publisher = {Wiley-Interscience},
  address   = {New York},
  year      = {1983}
}

@inproceedings{sagawa2020distributionally,
  author    = {Sagawa, Shiori and Koh, Pang Wei and Hashimoto, Tatsunori B. and Liang, Percy},
  title     = {Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization},
  booktitle = {International Conference on Learning Representations},
  year      = {2020}
}

@article{li2015global,
  author  = {Li, Guoyin and Pong, Ting Kei},
  title   = {Global Convergence of Splitting Methods for Nonconvex Composite Optimization},
  journal = {SIAM Journal on Optimization},
  volume  = {25},
  number  = {4},
  pages   = {2434--2460},
  year    = {2015},
  doi     = {10.1137/140998135}
}

@article{hong2016convergence,
  author  = {Hong, Mingyi and Luo, Zhi-Quan and Razaviyayn, Meisam},
  title   = {Convergence Analysis of Alternating Direction Method of Multipliers for a Family of Nonconvex Problems},
  journal = {SIAM Journal on Optimization},
  volume  = {26},
  number  = {1},
  pages   = {337--364},
  year    = {2016},
  doi     = {10.1137/140990309}
}

@inproceedings{lin2020near,
  author    = {Lin, Tianyi and Jin, Chi and Jordan, Michael I.},
  title     = {Near-Optimal Algorithms for Minimax Optimization},
  booktitle = {Proceedings of the 33rd Conference on Learning Theory},
  series    = {Proceedings of Machine Learning Research},
  volume    = {125},
  pages     = {2738--2779},
  year      = {2020}
}

@article{ostrovskii2021efficient,
  author  = {Ostrovskii, Dmitrii M. and Lowy, Andrew and Razaviyayn, Meisam},
  title   = {Efficient Search of First-Order {N}ash Equilibria in Nonconvex-Concave Smooth Min-Max Problems},
  journal = {SIAM Journal on Optimization},
  volume  = {31},
  number  = {4},
  pages   = {2508--2538},
  year    = {2021},
  doi     = {10.1137/20M1337600}
}

@article{bot2023alternating,
  author  = {Bo{\c{t}}, Radu Ioan and B{\"o}hm, Axel},
  title   = {Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex-Concave Minimax Problems},
  journal = {SIAM Journal on Optimization},
  volume  = {33},
  number  = {3},
  pages   = {1884--1913},
  year    = {2023},
  doi     = {10.1137/21M1465470}
}

@article{li2021augmented,
  author  = {Li, Zichong and Xu, Yangyang},
  title   = {Augmented {L}agrangian-Based First-Order Methods for Convex-Constrained Programs with Weakly Convex Objective},
  journal = {INFORMS Journal on Optimization},
  volume  = {3},
  number  = {4},
  pages   = {373--397},
  year    = {2021},
  doi     = {10.1287/ijoo.2021.0052}
}
```

`lin2020near` 的 PMLR 页码 2738–2779 未经 Crossref 核对（PMLR 不在 Crossref），提交前需在 proceedings.mlr.press 确认一次。

## refer.bib 需修正的已有条目
- `nocedal2006numerical`：改为 `@book{..., author = {Nocedal, Jorge and Wright, Stephen J.}, title = {Numerical Optimization}, edition = {2}, publisher = {Springer}, address = {New York}, year = {2006}, doi = {10.1007/978-0-387-40065-5}}`。
- `bot2015variable`：作者 "C. Hendrick" 改为 "C. Hendrich"；DOI 10.1007/s11750-014-0326-z。
- `li2025nonsmooth`：补 DOI 10.1007/s10107-025-02197-1。
- 重复条目：`berahas2025linearized` 与 `elbourkhissi2025perturbed`；`boct2020proximal` 与 `bot2020proximal`。
- 疑似虚构或无法核实：`jin2022nested`、`shi2022linearized`、`lu2022single`、`hu2026fixed`。
