# 附录 A 解析核对记录

日期：2026-10-13。

范围：`appendix/LowerBoundRotation.tex` 的参数界引理、`lem:rot-estimates` 的 (i) 与 (ii)、`lem:rot-spectral`。同时核对正文旋转实例、迭代矩阵和 `lem:rot-trajectory` 的接口。

方法：逐式解析推导、独立代理审阅、LaTeX 编译。**没有运行数值验证、随机参数扫描或轨迹实验。**

**结论：解析核对通过，独立审阅结论一致。** 已补充谱证明中的稠密性依据；参数、常数、引理和旋转分支结论均保持原样。

## 1. 发现与修正

原谱证明直接写道：

> The excluded root collisions and denominator equalities are algebraic exceptional sets; the nondegenerate parameters are dense.

这个结论成立，但原文省略了例外条件并非恒等成立的理由。已在原位置加入完整的解析依据：

1. 内点参数且 $V\ne\alpha$ 时，$W-1>0$、$\vartheta>0$，两个分母和同步方程的行列式均非零。
2. $Q_{\rm f}(1)=\alpha\beta\eta\tau b^2/\nu>0$，排除了特征值为一导致的分母问题。
3. 快二次因子的判别式是 $\epsilon^2$ 的有理函数。当 $\epsilon\downarrow0$ 时，它趋于 $(U-V)^2$。选择 $U\ne V$ 后，判别式不恒等于零，其零点为孤立点。
4. 在内点，$V=\beta+d_\tau(1-\beta)$ 随 $\beta$ 严格增加，因此可以通过任意小扰动避开 $V=U$ 和 $V=\alpha$。
5. 若 $\epsilon(\rho+s)=c_1$，先略微减少 $\epsilon$，再作端点扰动，整个逼近序列仍满足原参数条件。

修正类型：**ADD_DERIVATION**。属于论证细节补充；没有发现需要加强假设、削弱结论或调整常数的错误。

## 2. 参数界

记 $M=\max\{1,4\tau,4\gamma\tau\}$，此记号只用于本核对记录。原参数条件给出

$$
0<\frac{\nu}{\alpha^2}\le\frac{64\gamma\tau\epsilon^2}{\alpha}<\frac{\gamma\tau}{16M}\le\frac1{64}.
$$

因此 $\zeta$ 非实，所有复分母均非零，且

$$
\frac{64}{65}U\le D\le U\le1,\qquad D\ge\frac\chi2.
$$

先利用 $V\Upsilon-\beta H=(1-V)(V-\beta)\nu\ge0$ 得到 $b\le8\epsilon$。再利用 $0\le\xi\le\eta sb^2$ 与 $c_1$ 的第一项得到

$$
\xi C_{\rm tr}\le\frac{64\eta(1+4/\chi)}\tau(\epsilon s)^2\le\frac1{16}.
$$

由此

$$
\frac{b^2}{64\epsilon^2}=\frac DU\frac{\beta H}{V\Upsilon}
\ge\frac{64}{65}\frac{15}{16}=\frac{12}{13}>\frac{49}{64}.
$$

这条推导先使用上界，再推出下界，没有循环使用 $b$ 的双侧界。

振幅估计使用的实部恒等式为

$$
\operatorname{Re}\bigl((\zeta-1+V)\overline{(\zeta-1+\beta)}\bigr)
=\Upsilon+\frac{V-\beta}{2}\nu.
$$

它与 Cauchy--Schwarz 不等式给出文中的 $a_{\rm p}$ 两个界。加上 $a_{\rm d}\le sb^2$ 后，得到 $aX$ 和 $\kappa X^2$ 的估计。

曲率估计中 $c_1\le1/224$、$\epsilon<1/64$、$M\ge4\tau$ 保证

$$
\kappa\le64c_1\epsilon+\frac\tau{16M}
\le\frac1{224}+\frac1{64}<\frac1{32}.
$$

参数界引理的最后两个不等式均由 $c_1$ 的第二项得到。所有常数的依赖与主定理一致。

## 3. 特征多项式与同步初值

从中心行消元后，特征多项式确为

$$
t^2(t+U)(t+V)-\eta a\,t(t+\alpha)(t+V)
+\eta\tau b^2(t+1)(t+\alpha)(t+\beta).
$$

除正文列出的三个代数恒等式外，参数定义还直接给出

$$
\eta\tau b^2\beta=\nu\bigl(WV-(1-V)\xi\bigr).
$$

用此恒等式逐项比较四次多项式系数，得到

$$
\det((1+t)I-\mathbb T)=(t^2+\nu t+\nu)
\bigl((t+D)(t+V)-\vartheta(t+\alpha)\bigr).
$$

特征向量的两个中心坐标与对偶坐标满足对应矩阵行。将这些表达代入原始坐标行，乘以非零的 $(\zeta-1)(\zeta-1+\alpha)(\zeta-1+V)$，恰好得到上述特征多项式在 $t=\zeta-1$ 的值。因此 $\mathbb T\mathbf v=\zeta\mathbf v$。

同步初值的两条方程乘去分母后，关于 $S_0,S_1$ 的系数矩阵是

$$
\begin{pmatrix}D_{\rm f}&\alpha\\D_{\rm f}-C_{\rm f}+V&-(1-V)\end{pmatrix}.
$$

其行列式确为 $\alpha(1-V)(\alpha-V)(W+\xi)$。解得的 $S_0,S_1$ 与附录给出的 $r_x,r_\lambda$ 完全一致。

补足第 1 节的稠密性论证后，$Q_{\rm f}(\mathbb T)\mathbf r=0$ 覆盖所有允许端点与重根。

## 4. 快子空间与瞬态界

对 $0<D\le1$、$|t|\ge1$，逆三角不等式给出

$$
|t-1+D|\ge |t|-1+D\ge D|t|.
$$

对 $V$ 同理，再用 $2\vartheta/(DV)\le1/8$，可排除 $Q_{\rm f}$ 在单位圆及其外部的根。该论证不要求两个根互异。有限维不变子空间上的矩阵幂因此趋于零，重根产生的 Jordan 项也不影响这一结论。

卷积核为有限几何级数之积的系数。即使 $r_{\rm p}=r_{\rm d}$，仍有

$$
G_j\ge0,\qquad G_j\le D^{-1},\qquad \sum_{j\ge0}G_j=(DV)^{-1}.
$$

原始坐标的上界先对有限 $N$ 推出

$$
\max_{0\le k\le N}|p_k|\le\frac{3X}{16}+\frac14\max_{0\le k\le N}|p_k|.
$$

移项得到 $\max_{0\le k\le N}|p_k|\le X/4$。有限部分和的同类估计给出

$$
\sum_{k\ge0}|p_k|\le\frac{X}{4DV}\le\frac{X}{\chi d_\tau}.
$$

无穷和由非负部分和的单调性与统一上界得到，不需要交换两个极限。

对偶部分先证明差值 $e_k$ 有界，再由 $q_k\to0$ 写成绝对可和的尾和：

$$
q_k=-\frac{\tau b\beta}{V}\sum_{j=k+1}^{\infty}p_j.
$$

利用 $\beta/V\le1$、$\tau/d_\tau=s$，得到 $|q_k|\le sbX/\chi$。与 $|e_k|\le5sbX/4$ 合并，恰好得到正文所用的对偶瞬态界。

**不需要关于全部参数的一致谱间隙。** 每个固定允许参数下的衰减用于尾和恒等式；对所有迭代次数的上界由卷积估计单独证明。

## 5. 类成员证明与下界衔接

分段径向函数在两个接点处函数值和一阶导数匹配。径向与切向 Hessian 特征值的绝对值均不超过 $\kappa$。因此梯度全局 Lipschitz，且范数小于一。仿射映射的 Jacobian 范数为 $b<1$；外函数为凸的 1-Lipschitz 范数函数。

初始差值满足

$$
F(0)-\inf F\le5\epsilon+\frac{100}{9}(\rho+s+2\gamma)\epsilon^2
\le6\epsilon+32\gamma\epsilon^2\le\Delta.
$$

最后一步分别使用 $\epsilon<\Delta/12$ 与 $\epsilon^2<\Delta/(64\gamma)$。实例类的五项常数与初始差值条件均满足。

依赖顺序为：参数界 → 谱结论 → 瞬态界 → 类成员与轨迹归纳。类成员证明中的前向引用不构成循环。

正文归纳先验证 $(x^k,\lambda^k)$ 的 proximal 条件并得到 $x^{k+1}$，再验证 $(x^{k+1},\lambda^k)$ 的条件并完成其余更新。两个 proximal 条件的范数上界均为 $3/4$。最后按 $X$ 与 $|\Lambda|$ 的大小分别使用可行性与驻点残差，得到

$$
R_k\ge\frac b2\max\{X,|\Lambda|\}=\frac b6\ge\frac76\epsilon.
$$

## 6. 解析边界检查

| 情形 | 解析检查 |
|---|---|
| $\alpha=1$ | $W=D=1$，$Q_{\rm f}(t)=t(t-1+V-\vartheta)$；连续延拓合法 |
| $\beta=1$ | $V=1,\xi=\vartheta=0$，$Q_{\rm f}(t)=t(t-1+D)$ |
| $s=\tau$ | $V=1,\vartheta=0$；$\xi$ 可非零，但不影响快因子的形式 |
| $V=\alpha$ 或快根重合 | 由补足的连续延拓处理；卷积核没有根差分母 |
| $\eta=\gamma$ | $\chi=U=1$；内点 $V<1$ 使判别式的极限非零 |
| $\beta\downarrow0$ | $\beta/V\le1$ 与 $\xi C_{\rm tr}\le1/16$ 控制瞬态；$\beta=0$ 本身由另一个实例处理 |
| $\alpha\downarrow\alpha_\epsilon$ | $\nu/\alpha^2<1/64$ 仍由原阈值直接保证 |

以上候选情形均未产生解析反例。

## 7. 审阅与编译状态

独立审阅：**通过**。独立代理 `appendix_a_analytic_review` 从矩阵消元、逐项系数比较、同步方程求解、有限前缀估计等重新推导，确认当前附录及正文旋转分支成立。新增稠密性段落也经独立核对通过。指定的外部 Codex MCP 模型 `gpt-5.5` 返回模型不可用错误，故使用当前会话的独立代理；未将失败调用计作审阅证据。

编译：**通过**。`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/appendix-a-audit-20261013 main.tex` 生成 38 页 PDF；最终日志无未定义引用或 LaTeX 错误。保留的排版警告位于共享导言、Preliminaries 和 LowerBoundProof，新增附录段落没有警告。编译用于发现 LaTeX 语法与引用问题，不构成数学验证。

本次补充为原构造的代数推导，未引入新的文献结论或新的专用术语；原稿中的术语保持原写法。
