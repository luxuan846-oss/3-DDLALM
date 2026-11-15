# GPT Pro 指令：路线 A 固定中心收缩引理，补全非线性情形（2026-10-29）

状态：待发送。附件：`overleaf/sections/AlgorithmFamily.tex`、`overleaf/appendix/UpperBoundBetaZero.tex`。本文件第二节是已证的线性化版本，作为模板；任务是把它逐项推广到非线性情形。

---

请只做一件事：在下面的框架内，逐项写出非线性情形的一步收缩证明。每一步给出等号或不等号成立的理由。禁止出现「合并后得到」「整理可得」这类跳步；禁止分块 Young 不等式；禁止把 $\lVert\mathbf G\rVert^2$ 写成含 $G_{\mathcal A}^2\lVert\mathbf e_\lambda\rVert^2$ 的形式；禁止用 $\lVert\widehat{\mathbf r}-\mathbf r\rVert\le\eta\rho G_{\mathcal A}\lVert\mathbf G\rVert$ 一类的粗略范数界（它会产生 $b^2/(\eta\mu_x)$ 量级的系数）。

## 一、设定

固定中心 $\mathbf z$。$\mathcal P(\mathbf x,\boldsymbol\lambda)=\mathcal D_\rho(\mathbf x,\boldsymbol\lambda)+\frac1{2\gamma}\lVert\mathbf x-\mathbf z\rVert^2-\frac1{2s}\lVert\boldsymbol\lambda\rVert^2$。记 $T=\mathrm{prox}_{\rho h^*}$（firmly nonexpansive），
$\mathbf q(\mathbf x,\boldsymbol\lambda)=T(\boldsymbol\lambda+\rho\mathcal A(\mathbf x))$，$J=J_{\mathcal A}$，$\delta=\rho/s$。

一步更新：

$$
\mathbf x^+=\mathbf x-\eta\bigl[\nabla f(\mathbf x)+J(\mathbf x)^\top\mathbf q(\mathbf x,\boldsymbol\lambda)+\tfrac1\gamma(\mathbf x-\mathbf z)\bigr],\qquad
\boldsymbol\lambda^+=\mathbf q(\mathbf x^+,\boldsymbol\lambda)-\delta\boldsymbol\lambda .
$$

鞍点 $(\mathbf x_\star,\boldsymbol\lambda_\star)$，$\mathbf q_\star=(1+\delta)\boldsymbol\lambda_\star$。误差 $\mathbf e_x$、$\mathbf e_\lambda$，
$\mathbf r=\mathbf q(\mathbf x,\boldsymbol\lambda)-\mathbf q_\star$，$\widehat{\mathbf r}=\mathbf q(\mathbf x^+,\boldsymbol\lambda)-\mathbf q_\star$，$\mathbf G=\nabla_{\mathbf x}\mathcal P(\mathbf x,\boldsymbol\lambda)-\nabla_{\mathbf x}\mathcal P(\mathbf x_\star,\boldsymbol\lambda_\star)$。

常数：$\mu_x=\frac1\gamma-(L_f+L_{\mathcal A}L_h)>0$，$a=\eta\mu_x$，$b=\eta\rho G_{\mathcal A}^2\le\frac14$，$\eta\overline L_x\le\frac14$，$\delta\le\frac14$，$\lVert\boldsymbol\lambda\rVert,\lVert\boldsymbol\lambda_\star\rVert\le 2L_h$（已证）。

目标：

$$
\mathcal E^+\le\Bigl(1-c\min\{a,\delta\}\Bigr)\mathcal E,\qquad \mathcal E=\lVert\mathbf e_x\rVert^2+\frac\eta\rho\lVert\mathbf e_\lambda\rVert^2 .
$$

## 二、模板：线性化情形（已证）

$\mathcal A$ 线性（$J$ 常矩阵），$T$ 用同一个对称 $0\preceq B\preceq I$ 线性化。缩放 $\mathbf y=\sqrt{\eta/\rho}\,\mathbf e_\lambda$，$W=\sqrt{\eta\rho}\,J$，$R^2=\eta K\succeq aI$（$K$ 为 $f+\frac1{2\gamma}\lVert\cdot\rVert^2$ 的增量 Hessian）。令 $\mathbf v=W\mathbf e+\mathbf y$。则

$$
\mathbf e^+=(I-R^2)\mathbf e-W^\top B\mathbf v,\qquad \mathbf m:=W\mathbf e^+ +\mathbf y,\qquad \mathbf y^+=B\mathbf m-\delta\mathbf y .
$$

**步 1（关键恒等式，必须保留）：** $W(I-R^2)\mathbf e=\mathbf m-\mathbf y+WW^\top B\mathbf v$。由此

$$
\lVert\mathbf e^+\rVert^2+\lVert\mathbf y^+\rVert^2=\lVert(I-R^2)\mathbf e\rVert^2-\lVert W^\top B\mathbf v\rVert^2+\lVert B\mathbf m\rVert^2-2\langle\mathbf m,B\mathbf v\rangle+2\langle\mathbf y,B\mathbf v\rangle-2\delta\langle B\mathbf m,\mathbf y\rangle+\delta^2\lVert\mathbf y\rVert^2 .
$$

要点：$\lVert W^\top B\mathbf v\rVert^2$ 以负号出现。这是交替更新（对偶在 $\mathbf x^+$ 处求值）带来的，直接代入 firm nonexpansiveness 得不到它。

**步 2：** $\lVert B\mathbf m\rVert^2-2\langle\mathbf m,B\mathbf v\rangle=\langle\mathbf m-\mathbf v,B(\mathbf m-\mathbf v)\rangle-\langle\mathbf v,B\mathbf v\rangle$，其中 $\mathbf m-\mathbf v=-WR^2\mathbf e-WW^\top B\mathbf v$，且 $\lVert B\mathbf m\rVert^2\le\langle\mathbf m,B\mathbf m\rangle$。

**步 3：** $2\langle\mathbf y,B\mathbf v\rangle-\langle\mathbf v,B\mathbf v\rangle=\langle\mathbf y,B\mathbf y\rangle-\langle W\mathbf e,BW\mathbf e\rangle$。

**步 4：** 对偶项合并为 $\langle\mathbf y,[(1-\delta^2)I-(1-2\delta)B]\mathbf y\rangle\ge\delta\lVert\mathbf y\rVert^2$（用 $B\preceq I$）。

**步 5：** 剩余交叉项 $2\delta\langle BW\mathbf e,\mathbf y\rangle$ 与 $2\delta\langle B(\mathbf m-\mathbf y-W\mathbf e),\mathbf y\rangle$ 用 Young 吸收到 $\delta\lVert\mathbf y\rVert^2$、$\langle W\mathbf e,BW\mathbf e\rangle$ 与 $\lVert W^\top B\mathbf v\rVert^2$ 中。结论：

$$
\mathcal E-\mathcal E^+\ \ge\ c\bigl(a\lVert\mathbf e\rVert^2+\delta\lVert\mathbf y\rVert^2\bigr)+\tfrac12\langle W\mathbf e,BW\mathbf e\rangle+(1-2b-8\delta b)\lVert W^\top B\mathbf v\rVert^2 .
$$

## 三、任务：推广到非线性情形

把 $B\mathbf v$ 换成 $T(\mathbf v)-T(\mathbf v_\star)$，$B\mathbf m$ 换成 $T(\mathbf m)-T(\mathbf v_\star)$（即 $\mathbf r$ 与 $\widehat{\mathbf r}$ 的缩放版本），$W\mathbf e$ 换成 $\sqrt{\eta\rho}\,(\mathcal A(\mathbf x)-\mathcal A(\mathbf x_\star))$。可用的工具只有：

1. firm nonexpansiveness 的三条：$\langle\mathbf r,\mathbf v-\mathbf v_\star\rangle\ge\lVert\mathbf r\rVert^2$，$\langle\widehat{\mathbf r},\mathbf m-\mathbf v_\star\rangle\ge\lVert\widehat{\mathbf r}\rVert^2$，$\langle\widehat{\mathbf r}-\mathbf r,\mathbf m-\mathbf v\rangle\ge\lVert\widehat{\mathbf r}-\mathbf r\rVert^2$；
2. $T$ 是凸函数 $\varphi$（Moreau 包络）的梯度，因此有 Bregman 三点恒等式；
3. 原始块：$\langle\mathbf e_x,\mathbf G\rangle\ge\mu_x\lVert\mathbf e_x\rVert^2+\langle\Delta\mathcal A,\mathbf r\rangle$，$\lVert\mathbf G\rVert^2\le C_x\lVert\mathbf e_x\rVert^2+C_qG_{\mathcal A}^2\lVert\mathbf r\rVert^2$；
4. $\mathcal A$ 非线性带来的 Jacobian 余项用 $L_{\mathcal A}$ 和 $\lVert\mathbf e_\lambda\rVert\le4L_h$ 控制，并入 $\mu_x$。

按模板的步 1 到步 5 逐项重做。重点写清两处：

- **步 1 的恒等式在非线性下如何写。** 必须先把原始交叉项 $-2\eta\langle J\mathbf e_x,\mathbf r\rangle$ 用 $\mathbf e_x=\mathbf e_x^+ +\eta\mathbf G$ 改写到 $\mathbf x^+$ 处，再与第 2 条配对。写出改写后每一项。
- **步 2 的非对称项。** 线性情形中 $\langle\mathbf m,B\mathbf v\rangle=\langle\mathbf v,B\mathbf m\rangle$；非线性情形多出 $\langle\mathbf v,T(\mathbf m)\rangle-\langle\mathbf m,T(\mathbf v)\rangle$（均相对 $\mathbf v_\star$ 取增量）。用 $\varphi$ 的 Bregman 不等式把它写成可被步 5 的剩余耗散吸收的形式。写出所用的每一条不等式及其系数。

## 四、交付

1. 完整的一步不等式，形式与模板步 5 一致，所有常数显式。
2. 若某一步做不到，指出具体是哪一项、差多少阶，不要绕过。
3. 最后用一行写出收缩率 $1-c\min\{\eta\mu_x,\rho/s\}$ 中的 $c$ 及其对 $b,\delta,\eta\overline L_x$ 的依赖。

数值参考（供对照，不是证明）：非线性实例（$h=L_h\lVert\cdot\rVert_1$，$\mathcal A$ 含 $\sin$）上一步收缩的实测 $\theta\ge3\min\{\eta\mu_x,\rho/s\}$，说明余量充足。
