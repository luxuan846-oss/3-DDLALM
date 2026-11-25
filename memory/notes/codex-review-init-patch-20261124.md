**A PASS，B PASS，C FAIL，D PASS。** 一般初值补丁的常数正确，Theorem 4.1 的证明和 L909 的分离结论均成立。C 的问题限于 L167 对经典 linearized ALM 的恢复说明，它在第一步隐含使用了初始中心相等。

### A · PASS｜基础步与初始 gap

**Lemma 4.2 的基础步正确。** Algorithm 1 规定初始历史乘子等于当前乘子。由 $$a=(1-t)(1+\omega)$$、$$b=(1-t)\omega$$ 得 $$a-b=1-t$$。代入二次型，利用该引理的条件 $$t=\tau L_\lambda\le 1/2$$ 和初值约束，得到

$$
V_0=(1-a+b)\lVert\lambda^0\rVert^2
=t\lVert\lambda^0\rVert^2
\le \tfrac12 L_h^2.
$$

因此归纳起点满足 $$\sqrt{V_0}\le 2L_h$$。L309–311 的递推保持这个界。L317 在 $$k=0$$ 用到的上一项也受控，因为 $$\lambda^{-1}=\lambda^0$$。[Acceleration.tex L85–91](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:85) · [L237–268](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:237) · [L305–318](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:305)

**初始能量的外层因子 $$1/2$$ 已正确计入。** L352–353 给出 $$w^0=\bar\lambda^{-1}=\lambda^0$$，故第四个能量项为零。展开 L785–788 后，四个非零项及其贡献如下。[Acceleration.tex L339–353](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:339) · [L781–820](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:781)

| 展开后的项 | 对初始能量上界的贡献 |
|---|---|
| $$\tfrac32 p_s(z^0)$$ | $$\tfrac32 F(0)+\tfrac{3}{4\gamma}$$ |
| $$-\tfrac12 d_s(\lambda^0;z^0)$$ | $$-\tfrac12 F(0)+\tfrac{L_h^2}{\rho}+\tfrac{L_h^2}{4s}+\tfrac{G_0^2}{4\mu_\gamma}$$ |
| $$\tfrac{1}{4s}\lVert\lambda^0-\lambda_s^\star(z^0)\rVert^2$$ | $$\tfrac{L_h^2}{s}$$ |
| $$\tfrac{\mu_\gamma}{8}\lVert x_s(\lambda^0;z^0)\rVert^2$$ | $$\tfrac{G_0^2}{8\mu_\gamma}$$ |

第一行在定义 $$p_s(z^0)$$ 的最小化中取试验点 $$x=0$$，因此保留了 $$\lVert z^0\rVert^2/(2\gamma)$$。第二、四行分别用 strong convexity 给出的函数值界和距离界。第三行用到 $$\lambda_s^\star(z^0)=s q^\star/(\rho+s)$$ 和 $$\lVert q^\star\rVert\le L_h$$，故两乘子的距离至多为 $$2L_h$$。[Acceleration.tex L801–820](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:801) · [LRALMFamily.tex L73–92](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex:73) · [ValueFunctions.tex L202–222](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/ValueFunctions.tex:202)

减去 L777–779 的下界，再用 $$F(0)-\inf F\le\Delta$$，恰得

$$
\mathcal W_0-\mathcal W_K
\le \Delta+\frac{3}{4\gamma}
+\frac{L_h^2}{\rho}+\frac{5L_h^2}{4s}
+\frac{L_h^2}{2(\rho+s)}
+\frac{3G_0^2}{8\mu_\gamma}.
$$

其中 $$5/4=1/4+1$$，$$3/8=1/4+1/8$$。最后一步用 $$s\ge4\tau$$ 得 $$5/(4s)\le5/(16\tau)\le1/(2\tau)$$，并用 $$1/\rho+1/[2(\rho+s)]\le3/(2\rho)\le2/\rho$$。其余两项直接放宽。因此 L716–720 定义的 $$\Delta_{\mathcal W}$$ 对全部允许初值一致，且与 $$s$$ 无关。[Acceleration.tex L423–427](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:423) · [L713–721](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:713) · [L758–779](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:758) · [L821–829](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:821)

### B · PASS｜两项初值估计

令 $$r=\lVert\mathcal A(0)-y\rVert$$。由 $$h$$ 的 Lipschitz 条件和 $$\lVert\lambda^0\rVert\le L_h$$，减少至多 $$L_h r$$ 的两项分别来自函数值和乘子内积。因此，对每个 $$y$$ 都有

$$
\mathcal L_\rho(0,y,\lambda^0)
\ge F(0)-2L_h r+\frac{\rho}{2}r^2
\ge F(0)-\frac{2L_h^2}{\rho}.
$$

对 $$y$$ 取最小值得到所需的 $$\mathcal D_\rho$$ 下界。再保留 dual regularizer 的负号，舍去非负的 primal regularizer，即得 L800 的 $$\mathcal P_s$$ 下界。[Preliminaries.tex L39–45](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex:39) · [L105–119](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex:105) · [Acceleration.tex L796–800](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:796)

对梯度，Lemma 2.1(a) 给出 $$q(0,\lambda^0)\in\partial h(y(0,\lambda^0))$$，因此 $$\lVert q(0,\lambda^0)\rVert\le L_h$$。在 $$x=0$$ 处，primal regularizer 的梯度是 $$-z^0/\gamma$$。由 Assumption 2.1 的两个全局界和 $$\lVert z^0\rVert\le1$$，

$$
\bigl\lVert\nabla_x\mathcal P_s(0,\lambda^0;z^0)\bigr\rVert
=\bigl\lVert\nabla f(0)+J_{\mathcal A}(0)^\top q(0,\lambda^0)-z^0/\gamma\bigr\rVert
\le G_f+G_{\mathcal A}L_h+\frac1\gamma=G_0.
$$

[Preliminaries.tex L23–35](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex:23) · [L124–138](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex:124) · [LRALMFamily.tex L189–194](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex:189) · [Acceleration.tex L791–795](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:791)

### C · FAIL｜L167 的首步恢复说明

**L167 声称关闭 extrapolation 和 dual regularization，取 $$\tau=\rho$$、$$\alpha=1$$，即可恢复经典 linearized ALM。** 此时 center update 只保证 $$z^k=x^k$$ 对 $$k\ge1$$ 成立。从相同的 $$(x^0,\lambda^0)$$ 出发，比较两个算法的第一步可得

$$
x^1_{\mathrm{Fast}}-x^1_{\mathrm{ALM}}
=\frac{\eta}{\gamma}(z^0-x^0).
$$

允许的初值中有 $$x^0=0$$、$$z^0\ne0$$，因此整条轨迹从第一步起相同的说法缺少一个条件。**最小修正**是在 L167 的恢复条件中补上 $$z^0=x^0$$。这个条件只加在该 Remark 中。[Acceleration.tex L85–91](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:85) · [L159–168](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:159) · [Preliminaries.tex L175–187](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex:175)

**Lemmas 4.1–4.6、Theorem 4.1 及其附录依赖就初值而言均通过。**

- Lemma 4.1 的 residual 恒等式逐步成立。Lemma 4.2 使用 A 中的基础步。Lemma 4.3 在 $$k=0$$ 用到的 $$\bar\lambda^{-1}$$ 已显式定义为 $$\lambda^0$$，因此 extrapolation 恒等式和 primal tracking 估计在首步均成立。[Acceleration.tex L204–233](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:204) · [L309–318](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:309) · [L346–353](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:346) · [L447–453](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:447) · [L528–550](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:528)
- Lemmas 4.4–4.5 比较任意相邻中心。引用的两个附录引理分别对任意中心、任意一对中心成立。Lemma 4.6 中 $$\mathcal D_{\rho+s}(x,0)$$ 的零来自算法固定的 dual center $$\mu=0$$，与初始乘子无关。[Acceleration.tex L12–19](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:12) · [L611–630](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:611) · [L648–695](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:648) · [L768–779](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:768) · [ValueFunctions.tex L242–303](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/ValueFunctions.tex:242) · [L305–398](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/ValueFunctions.tex:305)
- Theorem 4.1 从 $$k=0$$ 累加 descent。L878–884 选择使**三个非负项之和**不超过平均值的同一个 $$k$$，所以三项估计能同时代入 residual。全节从 L173–178 起已固定任意允许的实例与初值，定理继承这两个量词。[Acceleration.tex L173–178](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:173) · [L867–897](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:867)

### D · PASS｜L909 的同口径分离

固定相同的 $$\mathbf C,\Delta$$，其中 $$L_f,G_f,G_{\mathcal A},L_h\ge1$$。取满足 Theorem 4.1 的参数，并在两个算法中使用同一个 $$\theta(\epsilon)=(\rho,c_s/\epsilon,\gamma,\gamma,\tau)$$。Theorem 3.2 允许 $$\eta=\gamma$$ 和任意固定 $$c_s>0$$，因此两条定理对所有 $$0<\epsilon<\min\{\epsilon_0,c_s/(4\tau)\}$$ 同时适用。两者都用前 $$K$$ 个输出中的最小 KKT residual 衡量迭代次数。[LRALMFamily.tex L195–215](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex:195) · [L305–315](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex:305) · [Acceleration.tex L844–864](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:844)

上界对同一集合中的**每一对** $$(I,u^0)$$ 成立。L899–905 给出的充分迭代次数可以统一取为

$$
K=\left\lceil
4C_R^2\Delta_{\mathcal W}\sqrt{c_s/\tau}\,\epsilon^{-5/2}
\right\rceil .
$$

下界则对**每一组**常数 center stepsizes $$(\alpha,\beta)$$，在同一集合中选取一对 hard instance 与初值。附录的 plateau 分支显式取零初值，radial 分支构造允许的初值并验证其范数。最后先对 $$(I,u^0)$$ 取 supremum，再对 $$(\alpha,\beta)$$ 取 infimum。L909–916 据此比较族的 $$\Omega(\epsilon^{-3})$$ 和 Fast LRALM 的 $$\mathcal O(\epsilon^{-5/2})$$，量词正确。[Acceleration.tex L899–916](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex:899) · [LowerBoundConstructions.tex L1021–1035](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/LowerBoundConstructions.tex:1021) · [L1176–1207](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/LowerBoundConstructions.tex:1176)

这里使用 **$$\Omega(\epsilon^{-3})$$** 有实质意义。Section 3 的 matching upper bound 另外要求 $$\eta<1/(\gamma^{-1}+\ell)<\gamma$$，无法用于 L909 的同一参数组 $$\eta=\gamma$$。L909 引用 Theorem 3.2 的 lower bound 已足以证明分离。[LRALMFamily.tex L322–340](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex:322) · [UpperBounds.tex L237–243](/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/UpperBounds.tex:237)

