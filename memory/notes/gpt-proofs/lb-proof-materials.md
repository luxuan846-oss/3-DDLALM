# 下界证明材料（GPT Pro，2026-10-01 至 10-12）

**整理方式**：本文件由 Claude 于 2026-10-12 从聊天中整理，公式重新录入，**不是逐字副本**。Part III 与 Part II 的定理、引理及证明按原文完整录入（Part II 引理 1、3 的证明已于 2026-10-13 补全）；Part I §3（初值由实例选取的旋转实例）排版有压缩，公式与结论完整，但该部分已被 Part II 取代。原始对话：Part III 见 ChatGPT 分享 https://chatgpt.com/share/6acd53fb-94ac-83e9-b1c4-1f5d54364aab ；Part I、Part II 无链接，原文在用户的 ChatGPT 记录中。

三份材料依次加强。最终定理（论文 Theorem 3.1，`thm:lower-bound`）由三块拼成：

| 块 | 来源 | 内容 |
|---|---|---|
| 小 $\alpha$ 平台实例 | Part I §2 | $A\equiv0$，零初值，$T_\epsilon\ge\Delta/(32\gamma\alpha\epsilon^2)$ |
| 大 $\alpha$、$\beta>0$ 零初值旋转实例 | Part II §2–§4 | 平移中心 $x_c,\lambda_c$，谱分解，$R_k\ge\frac76\epsilon$ |
| $\beta=0$ Huber 实例 | Part II §5（引理 4） | 可行性残差 $>2\epsilon$ |
| 关于 $s$ 一致的常数与门槛 | Part III | 用 $C^\sharp_{\rm tr},C^\sharp_{\rm du},C^\sharp_{\rm res}$ 替换 Part II 的常数；门槛 $\epsilon(\rho+s)\le c_1$ |

注意：
- Part I 的大 $\alpha$ 旋转实例与 $\beta=0$ 不动点实例**初值由实例选取**，已被 Part II 取代；只保留其平台实例与写法参考。
- Part II 的门槛含 $s^{-3/2}$，已被 Part III 取代；Part II 的构造与代数恒等式保持有效。
- 材料中的 "附件 main.pdf / Algorithm 4.1 / Definition 3.3 / Assumptions 1–3" 指旧稿编号；对应现稿：算法 `def:splalm`，证书 `def:eps-kkt` 与 `def:splalm` 的输出，假设 `ass:smoothness`、`ass:h`（水平有界不在问题类内）。
- 写入论文时的记号替换：$J\to\Upsilon$，$K\to\varpi$，$L$（复增益）$\to\Gamma$，平台中的 $d\to x_\star$，$\mathbb M\to\mathbb T$，$\mathcal V\to\iota$。
- 数值核对已于 2026-10-12 完成（300 组随机参数，从零初值运行，$\min_k R_k/\epsilon\ge2.63$）。

---

# Part I：10-01 版（初值由实例选取）

**下界成立，可以取 $p=4$。** 在"有界初值也由困难实例选择"的常数中心步长子类中，能够证明
$$
\inf_{(\alpha,\beta)\in[0,1]^2}\sup_{I\in\mathcal I_\Delta}T_\epsilon(\theta,\alpha,\beta;I)\ \ge\ c_\theta\Delta\,\epsilon^{-4}.
$$
极小极大形式用**两个不同的实例分支对抗同一对步长**（性能估计思想，Drori–Teboulle, Math. Program. 2014, DOI 10.1007/s10107-013-0653-0）：
$$
\alpha>C_\theta\epsilon^2\ \Longrightarrow\ \text{有界、不衰减的旋转轨道，}R_k>\epsilon\ \forall k;\qquad
0<\alpha\le C_\theta\epsilon^2\ \Longrightarrow\ \text{固定间隙实例需 }\Omega(\Delta/(\alpha\epsilon^2))=\Omega(\Delta\epsilon^{-4}).
$$
快中心分支采用二维 $h(y)=\|y\|_2$。

## 1. 定理

实例类 $\mathcal I_\Delta$：满足 Assumptions 1–3，且 $L_f\le1,G_f\le1,L_A=0,G_A\le1,L_h\le1$，$F(x^0)-\inf F\le\Delta$，$\|x^0\|+\|\lambda^0\|+\|z^0\|+\|\mu^0\|\le1$。初值是实例的一部分。只用一维和二维实例。

**定理。** 固定 $\theta=(\rho,s,\gamma,\eta,\tau)>0$，$\eta\le\gamma$，$\tau\le s$。令 $K_\theta:=\max\{1,4\tau,4\gamma\tau\}$。对每个固定的 $\Delta>0$，存在 $\epsilon_\theta(\Delta)>0$，使得对任意 $0<\epsilon<\epsilon_\theta(\Delta)$、$(\alpha,\beta)\in[0,1]^2$，存在 $I\in\mathcal I_\Delta$ 满足
$$
T_\epsilon(\theta,\alpha,\beta;I)\ge\frac{\Delta}{32768\,\gamma K_\theta}\epsilon^{-4}.\tag{1}
$$

## 2. 小 $\alpha$：固定初始间隙的下降平台（对所有 $\beta$ 有效）

令 $g:=2\epsilon$，$d:=\frac{\Delta}{g}+\frac g2$。取 $A(x)\equiv0$，$h(y)=|y|$，$x^0=z^0=\lambda^0=\mu^0=0$，
$$
f(x)=\begin{cases}\frac12(x-d)^2,&|x-d|\le g,\\ g|x-d|-\frac12g^2,&|x-d|\ge g.\end{cases}\tag{2}
$$
$L_f=1$，$G_f=g$，$\inf f=0$。$\epsilon$ 足够小时 $d\ge g$，于是 $f(0)=gd-\frac12g^2=\Delta$ (3)。$f$ 两端线性增长，水平集紧。

因为 $A=0$ 且两个乘子初值为零，$\lambda^k=\mu^k=y^{k+1}=q^k=0$ 对所有 $k$。记 $\ell:=d-g=\frac\Delta g-\frac g2$。只要 $x^k\le\ell$，有 $f'(x^k)=-g$，递推为
$$
x^{k+1}=x^k+\eta g-\frac\eta\gamma(x^k-z^k),\qquad z^{k+1}=z^k+\alpha(x^{k+1}-z^k).\tag{4}
$$
设 $e^k=x^k-z^k$。由 $\eta\le\gamma$，在平台内 $e^{k+1}=(1-\alpha)[(1-\frac\eta\gamma)e^k+\eta g]$，从 $e^0=0$ 归纳得 $0\le e^k\le\gamma g$ (5)。同时 $0\le z^{k+1}-z^k=\alpha[(1-\frac\eta\gamma)e^k+\eta g]\le\alpha\gamma g$。因此
$$
x^k\le\gamma g(1+\alpha k).\tag{6}
$$
对 $0<\alpha\le1$，取 $N:=\lfloor\frac{\Delta}{4\gamma\alpha g^2}\rfloor$。令 $\epsilon$ 足够小使 $g^2\le\Delta$，$g^2\le\frac{\Delta}{8\gamma}$ (7)。则对 $k\le N$，$x^k\le\gamma g+\frac{\Delta}{4g}\le\frac{\Delta}{2g}\le\ell$。这同时完成"轨迹留在平台"的归纳验证。

所以对 $0\le k<N$，$R_k=|f'(x^{k+1})|=g=2\epsilon>\epsilon$。又因为取整前的数至少为 2，
$$
T_\epsilon\ge N\ge\frac{\Delta}{8\gamma\alpha g^2}=\frac{\Delta}{32\gamma\alpha\epsilon^2}.\tag{8}
$$
（若取整前的数小于 2，(8) 的右端小于 1，而 $T_\epsilon\ge1$ 恒成立。）

当 $\alpha=0$ 时，(6) 给出 $x^k\le\gamma g<\ell$ 对所有 $k$，故 $T_\epsilon=+\infty$ (9)。

## 3. 大 $\alpha$：显式单位模旋转轨道（初值由实例选取；已被 Part II 取代）

处理 $\alpha>K_\theta b_0^2$，$b_0:=32\epsilon$，$0<\beta\le1$ (10)。

### 3.1 参数与实例
$\chi:=\eta/\gamma\in(0,1]$，$d_\tau:=\tau/s\in(0,1]$，$U:=\alpha+\chi(1-\alpha)$，$V:=\beta+d_\tau(1-\beta)$，
$$\nu:=\frac{\eta\tau b_0^2\alpha\beta}{UV},\tag{11}$$
$E:=\alpha^2+(1-\alpha)\nu$，$H:=V^2+(1-V)\nu$，$J:=\beta V+(1-V)\nu$，$W:=1+\frac{\chi\alpha(1-\alpha)}E$，
$$b^2:=\frac{\nu WH}{\eta\tau J},\tag{12}\qquad
\kappa:=\rho b^2+\frac{(1-\alpha)\nu}{\gamma E}+\frac{\tau b^2(V-\beta)}H.\tag{13}$$
令 $\epsilon$ 足够小使 $b_0\le\min\{1,\frac1{\rho+s+\tau},\frac1{2\sqrt{\rho+s}},\frac{d_\tau}{\sqrt{\eta\tau}}\}$ (14)。由 $U\ge\chi$、$V\ge d_\tau$ 和 (10)，$\frac\nu{\alpha^2}\le\frac{\gamma\tau b_0^2}\alpha\le\frac14$，$\frac{\nu}{\beta V}\le\frac{\eta\tau b_0^2}{d_\tau^2}\le1$ (15)。因此 $\frac12\frac U\alpha\le W\le\frac U\alpha$，$\frac12\frac V\beta\le\frac HJ\le\frac V\beta$，得 $\frac{b_0}2\le b\le b_0$ (16)。由 $J\le H$，$\frac{(1-\alpha)\nu}{\gamma E}=\frac{\nu(W-1)}{\eta\alpha}\le\frac{\tau b^2}\alpha$；由 $V\ge d_\tau$，$\frac{\tau(V-\beta)}H\le\frac\tau V\le s$。所以 $0<\kappa\le(\rho+s)b^2+\frac{\tau b^2}\alpha\le\frac14+\frac\tau{K_\theta}\le\frac12$ (17)。

定义 $\omega:=\sqrt{\nu-\nu^2/4}$，$\zeta:=1-\frac\nu2+i\omega$，$u:=\zeta-1$；$|\zeta|=1$，$\omega>0$。取
$$L:=\frac{\tau b\,\zeta(u+\beta)}{u(u+V)},\tag{18}$$
$r_0=1/4$，$X:=\frac{r_0}{\max\{1,|L|\}}$，$\Lambda:=LX$，$Z:=\frac{\alpha\zeta}{u+\alpha}X$，$M:=\frac{\beta\zeta}{u+\beta}\Lambda$ (19)。$\max\{X,|\Lambda|\}=r_0$，$|Z|\le X$，$|M|\le|\Lambda|$ (20)。$\mathcal V(a):=(\Re a,\Im a)$。初值 $(x^0,\lambda^0,z^0,\mu^0)=(\mathcal V(X),\mathcal V(\Lambda),\mathcal V(Z),\mathcal V(M))$ (21)。$A(x)=bx$，$h(y)=\|y\|_2$ (22)。$r_*=X$，$f(x)=\psi_{\kappa,r_*}(\|x\|)$，
$$\psi_{\kappa,r_*}(r)=\begin{cases}-\frac\kappa2r^2,&0\le r\le r_*,\\ \frac\kappa2(r-2r_*)^2-\kappa r_*^2,&r_*\le r\le3r_*,\\ \kappa r_*(r-3r_*)-\frac\kappa2r_*^2,&r\ge3r_*.\end{cases}\tag{23}$$
接点处函数值与一阶导数匹配；径向 Hessian 特征值为 $\psi''(r)$ 与 $\psi'(r)/r$，绝对值不超过 $\kappa$。$f\in C^1$，$L_f\le\kappa\le\frac12$，$G_f\le\kappa r_*\le\frac18$ (24)；线性增长，水平集有界；$\inf f=-\kappa r_*^2$ (25)。$L_A=0$，$G_A=b\le1$，$L_h=1$。

### 3.2 四变量递推与单位模特征值
在 $y=0$、$\nabla f(x)=-\kappa x$ 区域，记 $m:=1+\eta(\kappa-\rho b^2)-\chi$，每个实坐标上
$$
\mathbb M=\begin{pmatrix}m&-\eta b&\chi&0\\ \tau bm&1-d_\tau-\tau\eta b^2&\tau b\chi&d_\tau\\ \alpha m&-\alpha\eta b&1-\alpha+\alpha\chi&0\\ \beta\tau bm&\beta(1-d_\tau-\tau\eta b^2)&\beta\tau b\chi&1-\beta+\beta d_\tau\end{pmatrix}.\tag{26}
$$
传递函数 $\mathsf P(t):=\frac{t-1}\eta+\frac{(1-\alpha)(t-1)}{\gamma(t-1+\alpha)}$，$\mathsf D(t):=\frac{(t-1)(t-1+V)}{\tau(t-1+\beta)}$ (27)。消去两个中心变量后特征模态条件为
$$\kappa-\rho b^2=\mathsf P(t)+b^2\frac{t}{\mathsf D(t)}.\tag{28}$$
由 $\Re u=-\nu/2$、$|u|^2=\nu$：$\Im\mathsf P(\zeta)=\frac{\omega W}\eta$，$\Re\mathsf P(\zeta)=-\frac\nu{2\eta}+\frac{(1-\alpha)\nu(1-\alpha/2)}{\gamma E}$ (29)。$\frac\zeta{\mathsf D(\zeta)}=\tau[\frac\beta V\frac\zeta u+\frac{V-\beta}V\frac\zeta{u+V}]$，$\Im\frac\zeta{\mathsf D(\zeta)}=-\frac{\tau\omega J}{\nu H}$，$\Re\frac\zeta{\mathsf D(\zeta)}=\frac{\tau[J+2(V-\beta)]}{2H}$ (30)。(12) 使 (28) 右端虚部为零，实部等于 $\kappa-\rho b^2$。故 $\zeta$ 是单位模特征值，(19) 是特征向量。

### 3.3 区域验证
候选轨迹 $x^k=\mathcal V(\zeta^kX)$，$\lambda^k=\mathcal V(\zeta^k\Lambda)$，$z^k=\mathcal V(\zeta^kZ)$，$\mu^k=\mathcal V(\zeta^kM)$ (31)。$\|x^k\|=X=r_*$，故 $\nabla f(x^k)=-\kappa x^k$。$\operatorname{prox}_{h/\rho}(v)=0\iff\|\rho v\|\le1$；$\|\lambda^k+\rho bx^k\|,\|\lambda^k+\rho bx^{k+1}\|\le r_0(1+\rho b)\le\frac12$ (32)。由唯一性，(31) 是实际轨迹。

### 3.4 $R_k>\epsilon$
$a:=\kappa-\rho b^2\ge0$。$R_k=\max\{|b\Lambda-a\zeta X|,bX\}=:R$ (33)。由 (18)、(30)，$0\le\Re\Lambda\le b(s+\frac\tau2)X$，$\Im\Lambda<0$ (34)。$|b\Lambda-a\zeta X|\ge b|\Im\Lambda|$，$b|\Lambda|\le b^2(s+\frac\tau2)X+|b\Lambda-a\zeta X|\le bX+|b\Lambda-a\zeta X|\le2R$。故 $R\ge\frac b2\max\{X,|\Lambda|\}=\frac{br_0}2\ge2\epsilon>\epsilon$ (35)，$T_\epsilon=+\infty$ (36)。

### 3.5 初始间隙
$C_\theta:=\rho+s+4\gamma$。$\alpha W\ge\chi/2$ (37)。$\Im\Lambda=-\frac{\omega W}{\eta b}X$ (38)。$\frac{(1-\alpha)\nu}{\gamma E}X^2\le4\gamma b^2|\Lambda|^2$ (39)。$\kappa X^2\le C_\theta b^2r_0^2$ (40)。$F(x^0)-\inf F\le bX+\frac12\kappa X^2\le8\epsilon+32C_\theta\epsilon^2$ (41)；只要 $\epsilon\le\Delta/16$、$\epsilon^2\le\Delta/(64C_\theta)$ (42) 即不超过 $\Delta$。

## 4. 端点与覆盖（Part I 版）
- $\alpha=0$：平台实例，$T_\epsilon=+\infty$。
- $\beta=1$：$V=1$，$M=\Lambda$，$\mu^k=\lambda^k$。$\alpha=1$ 时 $\kappa=\rho b^2$，核心递推 $x^{k+1}=x^k-\eta b\lambda^k$，$\lambda^{k+1}=\lambda^k+\tau bx^{k+1}$，行列式 1，迹 $2-\eta\tau b^2$。
- $\beta=0$（Part I 版，初值非零）：$b=b_0$，$\kappa=(\rho+s)b_0^2$，$r_*=r_0$，$x^0=z^0=r_0e_1$，$\lambda^0=sb_0r_0e_1$，$\mu^0=0$ (43) 是固定点，$R_k=b_0r_0=8\epsilon$ (44)。
- 合并：$0<\alpha\le1024K_\theta\epsilon^2$ 时 $T_\epsilon\ge\frac{\Delta}{32\gamma\alpha\epsilon^2}\ge\frac{\Delta}{32768\gamma K_\theta}\epsilon^{-4}$；$\alpha>K_\theta b_0^2$ 时 $T_\epsilon=+\infty$。
- $B_\theta:=\min\{1,\frac1{\rho+s+\tau},\frac1{2\sqrt{\rho+s}},\frac{\tau/s}{\sqrt{\eta\tau}},\frac1{\sqrt{K_\theta}}\}$，$\epsilon_\theta(\Delta)=\min\{\frac{B_\theta}{32},\frac{\sqrt\Delta}2,\sqrt{\frac\Delta{32\gamma}},\frac\Delta{16},\sqrt{\frac\Delta{64C_\theta}}\}$ (45)。

## 5. 机制
较快的原始中心允许局部负曲率精确抵消耦合阻尼，产生证书始终不合格的有界旋转；为避开这个分支，中心步长必须进入 $O(\epsilon^2)$ 区域，而这一尺度在固定间隙平台上付出四次复杂度。对偶中心步长的任意选择（包括 $\beta=1$）都不能消除最坏情形。慢分支的实际间隙恰为 $\Delta$；快分支间隙为 $O(\epsilon)$ 但 $T_\epsilon=+\infty$，所以下界直接对固定 $\Delta$ 预算类成立。

---

# Part II：零初值版本（大 $\alpha$ 分支，全零初值）

大 $\alpha$ 区域存在从全零初值出发的新实例，仍有 $T_\epsilon=+\infty$。不需要引入段：线性轨迹分成不衰减的旋转分量和衰减分量，后者在初始时刻精确满足两组中心同步条件；再通过问题数据中的平移和线性项，使四个初值都严格为零。更新顺序与后原始步证书不变。

## 1. 定理与常数（本版门槛；常数已被 Part III 替换）
$\chi:=\eta/\gamma$，$d:=\tau/s$，$K_\theta:=\max\{1,4\tau,4\gamma\tau\}$，$\alpha_\epsilon=1024K_\theta\epsilon^2$ (1)。
$C_{\rm tr}:=\frac1d+\frac{2(1+d^{-1})}{\chi d}$，$C_{\rm du}:=\frac\tau\chi+\frac54s$，$C_{\rm res}:=C_{\rm du}+\frac54s$，$C_{\rm gap}:=\rho+s+2\gamma$。
$B_\theta:=\min\{1,\frac1{4\sqrt{K_\theta}},\frac1{4\sqrt{C_{\rm tr}\eta s}},\frac1{8C_{\rm res}},\frac1{2(2C_{\rm du}+5\rho/4)},\frac1{8\sqrt{\rho+s}}\}$ (2)，
$\epsilon_\theta(\Delta):=\min\{\frac{B_\theta}8,\frac\Delta{10},\sqrt{\frac{9\Delta}{200C_{\rm gap}}},\frac1{16(\rho+3s+1)},\frac{\sqrt\Delta}2,\sqrt{\frac\Delta{32\gamma}}\}$ (3)。

**定理。** 对任意 $\Delta>0$、$0<\epsilon<\epsilon_\theta(\Delta)$、$\alpha_\epsilon<\alpha\le1$、$0\le\beta\le1$，存在至多二维实例，满足 Assumptions 1–3、$(L_f,G_f,L_A,G_A,L_h)\le(1,1,0,1,1)$、$F(0)-\inf F\le\Delta$，使从 $x^0=z^0=\lambda^0=\mu^0=0$ 出发 $R_k>\epsilon$ 对所有 $k\ge0$ (4)。$\beta>0$ 时 $R_k\ge7\epsilon/6$，$\beta=0$ 时 $R_k>2\epsilon$。结合小 $\alpha$ 分支，
$$\inf_{(\alpha,\beta)\in[0,1]^2}\sup_{I\in\mathcal I_0(\mathbf C_0,\Delta)}T_\epsilon\ge\frac{\Delta}{32768\gamma K_\theta}\epsilon^{-4}.\tag{5}$$

## 2. $\beta>0$：参数与旋转模态
固定 $\alpha>\alpha_\epsilon$，$0<\beta\le1$。$b_\epsilon:=8\epsilon$，$U$、$V$ 同上，$\nu:=\frac{\eta\tau b_\epsilon^2\alpha\beta}{UV}$ (6)；$E,H,J,W$ 同上；
$$b^2:=\frac{\nu WH}{\eta\tau J},\quad\xi:=\frac{\eta\tau b^2(V-\beta)}H,\quad a:=\frac{\nu(W-1)}{\eta\alpha}+\frac\xi\eta,\quad\kappa:=\rho b^2+a.\tag{7}$$
$\zeta:=1-\frac\nu2+i\sqrt{\nu-\frac{\nu^2}4}$，$u:=\zeta-1$ (8)。
$L:=\frac{\tau b\zeta(u+\beta)}{u(u+V)}$，$X:=\frac1{3\max\{1,|L|\}}$，$\Lambda:=LX$ (9)；$Z:=\frac{\alpha\zeta}{u+\alpha}X$，$M:=\frac{\beta\zeta}{u+\beta}\Lambda$ (10)；$\max\{X,|\Lambda|\}=\frac13$ (11)。

**引理 1（本版）.** $\frac\nu{\alpha^2}\le\frac1{64}$，$7\epsilon\le b\le8\epsilon$，$\frac\chi2\le D:=\alpha W\le1$，$\xi\le\frac1{16C_{\rm tr}}$ (12)；$0<\kappa\le\frac1{32}$ (13)；$aX\le\frac18b|\Lambda|+sb^2X$，$\kappa X^2\le C_{\rm gap}b^2\max\{X^2,|\Lambda|^2\}$ (14)。
*证明.* 因为 $U\ge\chi$、$V\ge\beta$，由分界条件，
$$\frac\nu{\alpha^2}\le\frac{\gamma\tau b_\epsilon^2}\alpha<\frac{\gamma\tau}{16K_\theta}\le\frac1{64}.$$
记 $\delta=\nu/\alpha^2$。由 $W$ 的定义，$D=\alpha+\frac{\chi(1-\alpha)}{1+(1-\alpha)\delta}$，所以 $\frac U{1+\delta}\le D\le U\le1$，$D\ge\chi/2$。

此外，$\frac{b^2}{b_\epsilon^2}=\frac{\alpha W}U\frac{\beta H}{VJ}\le1$，因为两项分别不超过 1。由 $H\ge V^2$、$V-\beta\le V$ 得
$$\xi\le\frac{\eta\tau b^2}V\le\eta sb^2\le\eta sb_\epsilon^2\le\frac1{16C_{\rm tr}}.$$
又有 $\frac{\beta H}{VJ}=1-\frac{(1-V)\xi}{WV}\ge1-\frac\xi d\ge\frac{15}{16}$。因此 $\frac{b^2}{b_\epsilon^2}\ge\frac{64}{65}\frac{15}{16}=\frac{12}{13}>\frac{49}{64}$，证明 $b\ge7\epsilon$。

令 $a_{\rm p}:=\frac{\nu(W-1)}{\eta\alpha}$，$a_{\rm d}:=\frac\xi\eta$。由 $\eta\tau b^2=\nu W+V\xi$ 可得 $a_{\rm p}\le\frac{\tau b^2}\alpha$，$a_{\rm d}\le sb^2$。故
$$\kappa\le(\rho+s)b^2+\frac{\tau b^2}\alpha\le\frac1{64}+\frac1{64}=\frac1{32}.$$
为证明振幅估计，记 $E_\beta:=\beta^2+(1-\beta)\nu$。则 $\frac{|\Lambda|^2}{X^2}=\frac{\tau WE_\beta}{\eta J}$。同时 $J\le\Re\big((u+V)\overline{(u+\beta)}\big)\le\sqrt{HE_\beta}$，从而 $J^2\le HE_\beta$。因此
$$\frac{a_{\rm p}X}{b|\Lambda|}=\frac{\sqrt\nu(W-1)J}{\alpha W\sqrt{HE_\beta}}\le\frac{\sqrt\nu}\alpha\le\frac18,\qquad
\frac{a_{\rm p}X^2}{b^2|\Lambda|^2}=\frac{\eta(W-1)J^2}{\alpha W^2HE_\beta}\le\frac\eta{\alpha W}\le2\gamma.$$
加上 $a_{\rm d}\le sb^2$ 和 $\kappa=\rho b^2+a_{\rm p}+a_{\rm d}$，即得 (14)。∎

## 3. 精确满足标准初始化的谱分解
平移后的四变量递推矩阵
$$\mathbb M=\begin{pmatrix}m&-\eta b&\chi&0\\ \tau bm&1-d-\eta\tau b^2&\tau b\chi&d\\ \alpha m&-\alpha\eta b&1-\alpha+\alpha\chi&0\\ \beta\tau bm&\beta(1-d-\eta\tau b^2)&\beta\tau b\chi&1-\beta+\beta d\end{pmatrix},\qquad m:=1+\eta a-\chi.\tag{15}$$
衰减分量（初始时刻满足 $x=z$、$\lambda=\mu$）：
$$r_x:=-\frac{(W-1)u/(u+\alpha)+\xi\zeta/(u+V)}{W+\xi}X,\tag{16}$$
$$h_x:=\xi\Big[(1-\alpha)r_x+(V-\alpha)\frac\zeta{u+V}X\Big],\qquad v_x:=-Dr_x+h_x,\tag{17}$$
$$r_\lambda:=\frac{\chi(X-Z)+\eta ar_x-v_x}{\eta b},\quad r_z:=X-Z+r_x,\quad r_\mu:=\Lambda-M+r_\lambda.\tag{18}$$
$\mathbf v:=(X,\Lambda,Z,M)^\top$，$\mathbf r:=(r_x,r_\lambda,r_z,r_\mu)^\top$。

**引理 2.** 令 $\vartheta:=(1-V)\xi$，$Q_{\rm f}(t):=(t-1+D)(t-1+V)-\vartheta(t-1+\alpha)$ (19)。则 $\mathbb M\mathbf v=\zeta\mathbf v$，$Q_{\rm f}(\mathbb M)\mathbf r=0$ (20)，且
$$\mathbf v+\mathbf r=(P_0,Q_0,P_0,Q_0)^\top,\qquad P_0:=X+r_x,\ Q_0:=\Lambda+r_\lambda.\tag{21}$$

*证明.* 以 $v=t-1$ 表示，特征多项式
$$\mathcal Q(v)=v^2(v+U)(v+V)-\eta a\,v(v+\alpha)(v+V)+\eta\tau b^2(v+1)(v+\alpha)(v+\beta)=(v^2+\nu v+\nu)\big[(v+D)(v+V)-\vartheta(v+\alpha)\big].\tag{22}$$
消去关系：$\eta a=\frac{\nu(W-1)}\alpha+\xi$，$\eta\tau b^2=\nu W+V\xi$，$U-\alpha W=\frac{(1-\alpha)\nu(W-1)}\alpha$。因 $u^2+\nu u+\nu=0$，(9)–(10) 给出 $\mathbb M\mathbf v=\zeta\mathbf v$。

衰减分量：先在两个快根 $t_1\ne t_2$ 且分母非零的情形推导。特征向量
$$\mathbf v(t)=\Big(1,\ \frac{\tau bt(t-1+\beta)}{(t-1)(t-1+V)},\ \frac{\alpha t}{t-1+\alpha},\ \frac{\beta t}{t-1+\beta}\frac{\tau bt(t-1+\beta)}{(t-1)(t-1+V)}\Big)^\top.$$
快分量 $c_1\mathbf v(t_1)+c_2\mathbf v(t_2)$ 与旋转分量相加后满足两组中心同步条件，当且仅当
$$\sum_jc_j\frac{t_j-1}{t_j-1+\alpha}=-\frac u{u+\alpha}X,\qquad\sum_jc_j\frac{t_j}{t_j-1+V}=-\frac\zeta{u+V}X.\tag{23}$$
记 $S_0=c_1+c_2$，$S_1=(t_1-1)c_1+(t_2-1)c_2$。快根满足 $v^2+C_{\rm f}v+D_{\rm f}=0$，$C_{\rm f}=D+V-\vartheta$，$D_{\rm f}=DV-\alpha\vartheta$。在这些根上 $\frac v{v+\alpha}=\frac{D_{\rm f}+\alpha v}{\alpha^2-C_{\rm f}\alpha+D_{\rm f}}$，$\frac{v+1}{v+V}=\frac{D_{\rm f}-C_{\rm f}+V-(1-V)v}{V^2-C_{\rm f}V+D_{\rm f}}$，分母分别为 $\alpha(W-1)(V-\alpha)$ 与 $\vartheta(V-\alpha)$。解得 $S_0=r_x$，$S_1=v_x$。第一步原始递推给出 $\eta br_\lambda=\chi(X-Z)+\eta ar_x-v_x$；中心分量由同步条件确定，即 (18)。最终公式 (16)–(18) 在参数范围内分母非零且连续，矩阵恒等式延伸到快根重合、$\alpha=1$、$\beta=1$、$d=1$ 等情形。(21) 由 (18) 逐分量成立。∎

**引理 3（本版）.** $\mathbf r^k:=\mathbb M^k\mathbf r\to0$ (24)；$|x_{\rm f}^k|\le\frac X4$，$|\lambda_{\rm f}^k|,|\mu_{\rm f}^k|\le C_{\rm du}bX$ (25)；$\sum_k|x_{\rm f}^k|\le\frac X\chi$ (26)。
*证明.* 令 $r_{\rm p}:=1-D$，$r_{\rm d}:=1-V$，二者均在 $[0,1)$ 内。由 (12) 和常数选择，
$$\frac{2\vartheta}{DV}\le\frac14.\tag{27}$$
若 $|t|\ge1$，则 $|(t-r_{\rm p})(t-r_{\rm d})|\ge|t|^2DV$，$|\vartheta(t-1+\alpha)|\le2\vartheta|t|$。因此 $Q_{\rm f}$ 在 $|t|\ge1$ 上没有零点。结合 $Q_{\rm f}(\mathbb M)\mathbf r=0$，所有快分量都趋于零。

原始快分量满足
$$x_{\rm f}^{k+2}-(r_{\rm p}+r_{\rm d})x_{\rm f}^{k+1}+r_{\rm p}r_{\rm d}x_{\rm f}^k=\vartheta\big[x_{\rm f}^{k+1}-(1-\alpha)x_{\rm f}^k\big],\tag{28}$$
初值为 $x_{\rm f}^0=r_x$，$x_{\rm f}^1-r_{\rm p}x_{\rm f}^0=h_x$。基础递推的卷积核 $G_j=\sum_{i=0}^jr_{\rm p}^{j-i}r_{\rm d}^i$ 非负，且 $\sum_{j\ge0}G_j=\frac1{DV}$。

从 (16)–(17) 可得 $|r_x|\le(\frac18+\frac\xi d)X$，$|h_x|\le\xi(1+d^{-1})X$。故
$$|r_x|+\frac{|h_x|}{DV}\le\Big(\frac18+\xi C_{\rm tr}\Big)X\le\frac{3X}{16}.$$
对 (28) 使用上述卷积核，先在有限前缀上取最大值，再用 (27) 移项，得到
$$\sup_k|x_{\rm f}^k|\le\frac{|r_x|+|h_x|/(DV)}{1-2\vartheta/(DV)}\le\frac X4.$$
同样对绝对值求和，
$$\sum_k|x_{\rm f}^k|\le\frac{|r_x|/D+|h_x|/(DV)}{1-2\vartheta/(DV)}\le\Big(\frac1{2\chi}+\frac1{12}\Big)X\le\frac X\chi.$$
（本版用 $|r_x|+|h_x|/(DV)$ 控制初值项，$C_{\rm tr}$ 因而含 $1/(\chi d)\cdot(1+d^{-1})$，导致 $s^{-3/2}$ 门槛；Part III 改为 $|r_x|+|h_x|/D$。）

为控制对偶快分量，定义 $e^k:=\lambda_{\rm f}^k-\mu_{\rm f}^k$，$v^k:=\frac{\beta(1-d)\lambda_{\rm f}^k+d\mu_{\rm f}^k}V$。由对偶与对偶中心更新，
$$e^{k+1}=(1-V)e^k+\tau b(1-\beta)x_{\rm f}^{k+1},\tag{29}\qquad v^{k+1}=v^k+\frac{\tau b\beta}Vx_{\rm f}^{k+1}.\tag{30}$$
初始中心差 $e^0=-(\Lambda-M)=-\frac{\tau b(1-\beta)\zeta}{u+V}X$。由 $\tau/V\le s$ 和原始快分量界，$|e^k|\le\frac54sbX$。又因 $v^k\to0$，(30) 可从未来求和：$v^k=-\frac{\tau b\beta}V\sum_{j=k+1}^\infty x_{\rm f}^j$，故 $|v^k|\le\frac\tau\chi bX$。最后用 $\lambda_{\rm f}^k=v^k+\frac dVe^k$，$\mu_{\rm f}^k=v^k-\frac{\beta(1-d)}Ve^k$ 即得 (25)。∎

## 4. 新实例、全局假设与证书

### 4.1 显式实例
$$x_c:=-\mathcal V(P_0),\quad\lambda_c:=-\mathcal V(Q_0),\quad R_*:=\frac54X,\tag{31}$$
$$A(x)=b(x-x_c),\qquad h(y)=\|y\|_2,\tag{32}$$
$$f(x)=\psi_{\kappa,R_*}(\|x-x_c\|)-b\langle\lambda_c,x-x_c\rangle,\tag{33}$$
$\psi_{\kappa,R}$ 为 Part I (23) 的三段径向延拓 (34)。**$x_c,\lambda_c$ 是问题数据，算法初值仍为四个零向量。**

### 4.2 全局假设与间隙
$\operatorname{Lip}(\nabla f)\le\kappa$，$\sup\|\nabla f\|\le\kappa R_*+b\|\lambda_c\|$。$\|\lambda_c\|\le|\Lambda|+C_{\rm du}bX\le\frac12$，$R_*\le\frac5{12}$，故 $L_f\le\frac1{32}$，$G_f\le\frac5{384}+\frac12<1$；$L_A=0$，$G_A=b\le1$，$L_h=1$。$\|x-x_c\|\ge3R_*$ 时 $F(x)\ge[\kappa R_*+b(1-\|\lambda_c\|)]\|x-x_c\|-\frac72\kappa R_*^2$，水平集有界。$\inf F\ge-\kappa R_*^2$，$\|P_0\|\le R_*$，
$$F(0)-\inf F\le\frac32bR_*+\kappa R_*^2\le\frac58b+\frac{25}{144}C_{\rm gap}b^2\le5\epsilon+\frac{100}9C_{\rm gap}\epsilon^2\le\Delta.\tag{35}$$

### 4.3 从零出发的实际轨迹
$(p^k,\ell^k,\hat z^k,\hat\mu^k)^\top:=\zeta^k\mathbf v+\mathbf r^k$ (36)。$x^k=x_c+\mathcal V(p^k)$，$z^k=x_c+\mathcal V(\hat z^k)$，$\lambda^k=\lambda_c+\mathcal V(\ell^k)$，$\mu^k=\lambda_c+\mathcal V(\hat\mu^k)$；由 (21)、(31)，$k=0$ 时四者为零。引理 3 给出 $\frac34X\le|p^k|\le\frac54X=R_*$ (37)，故 $\nabla f(x^k)=-\kappa\mathcal V(p^k)-b\lambda_c$。两种 prox 输入
$$\|\lambda^k+\rho A(x^j)\|\le2|\Lambda|+2C_{\rm du}bX+\frac54\rho bX\le\frac13[2+b(2C_{\rm du}+5\rho/4)]\le\frac56<1,\quad j=k,k+1,\tag{38}$$
两次 prox 输出均为 0。由唯一性，(36) 是实际轨迹。

### 4.4 原点不是驻点
$\frac{Q_0}{P_0}=\frac ab-\overline{\frac L\zeta}$ (39)，$\Im\frac L\zeta=-\tau b\omega[\frac\beta{V\nu}+\frac{V-\beta}{VH}]<0$，故 $P_0,Q_0$ 不共线，$P_0\ne0$。$\nabla F(0)=(-\kappa+\frac b{|P_0|})\mathcal V(P_0)+b\mathcal V(Q_0)\ne0$ (40)。

### 4.5 对所有 $k$ 的证书下界
$y^{k+1}=0$，$R_k=\max\{|-ap^{k+1}+b\ell^k|,b|p^{k+1}|\}$ (41)。$b|p^{k+1}|\ge\frac34bX$ (42)。$|-ap^{k+1}+b\ell^k|\ge b|\Lambda|-C_{\rm du}b^2X-\frac54aX\ge\frac{27}{32}b|\Lambda|-C_{\rm res}b^2X$ (43)。$|\Lambda|\ge X$ 时由 $bC_{\rm res}\le\frac18$ 至少为 $\frac{23}{32}b|\Lambda|\ge\frac12b|\Lambda|$；$X\ge|\Lambda|$ 时用 (42)。故
$$R_k\ge\frac b2\max\{X,|\Lambda|\}=\frac b6\ge\frac76\epsilon>\epsilon,\qquad k\ge0.\tag{44}$$
包含 $k=0$ 与全部瞬态阶段。

## 5. $\beta=0$：替代实例
原偏差例子 $f=-cx$，$A=x$，$h=L|\cdot|$ 从零出发时，$R_0=c\max\{|1-\rho\eta|,\eta\}$ 不一定大于 $c/(\rho+s)$（反例：$\rho=s=\frac14$，$\gamma=\frac12$，$\eta=\frac18$，$\tau=\frac1{100}$，$L=1$，$c=\frac14$，$R_0=\frac{31}{32}c<2c$）。

**引理 4.** 令 $\ell_0:=\min\{1,(2\eta)^{-1}\}$，$d_0:=\min\{1,\sqrt\Delta\}$，$q_h:=2s+1$，$Q:=\rho+q_h$，$a_0:=\frac{4\epsilon(Q+s)}{q_h}$。一维实例
$$f(x)=\ell_0\big(\sqrt{1+(x-d_0)^2}-1\big),\qquad A(x)\equiv a_0,\tag{45}$$
$$h(y)=\begin{cases}\frac{q_h}2y^2,&|y|\le q_h^{-1},\\ |y|-\frac1{2q_h},&|y|\ge q_h^{-1}.\end{cases}\tag{46}$$
从四个零初值出发，若 $\beta=0$，则 $R_k>2\epsilon$ 对所有 $k\ge0$ (47)。

*证明.* $L_f,G_f\le1$，$L_A=G_A=0$，$L_h=1$。$F(0)-\inf F=\ell_0(\sqrt{1+d_0^2}-1)\le\Delta/2$；$f$ 向无穷增长，水平集有界；$f'(0)\ne0$。令 $r_\theta:=1-\frac\tau s-\frac\tau Q$，$\lambda_*:=\frac{sq_ha_0}{Q+s}$。因 $Q>2s$、$\tau\le s$，$-\frac sQ\le r_\theta<1$。候选对偶轨迹 $\lambda^k=\lambda_*(1-r_\theta^k)$，$\mu^k=0$ (48)，满足 $0\le\lambda^k\le\frac{sq_ha_0}Q<\frac12q_ha_0$；$q_ha_0\le\frac14$，于是 $y^{k+1}=\frac{\rho a_0+\lambda^k}Q\in[0,a_0]\subset[0,q_h^{-1}]$，位于二次分支。可行性残差
$$A(x^{k+1})-y^{k+1}=\frac{q_ha_0-\lambda^k}Q=\frac{q_ha_0}{Q+s}\Big(1+\frac sQr_\theta^k\Big)=4\epsilon\Big(1+\frac sQr_\theta^k\Big)>2\epsilon.$$
原始轨迹有界：$J_A=0$，原始两步对 $P(x,z):=f(x)+\frac{(x-z)^2}{2\gamma}$ 单调下降（$\eta(\ell_0+1/\gamma)\le\frac32$），故 $f(x^k)\le f(0)$，$x^k\in[0,2d_0]$，$z^k$ 亦然。∎

## 6. 端点、交界与结论（本版）
- $\beta=1$：$V=1$，$\xi=0$，$M=\Lambda$，$r_\mu=r_\lambda$，从零初值始终 $\mu^k=\lambda^k$；$Q_{\rm f}(t)=t(t-1+\alpha W)$。
- $\alpha=1$：$W=1$，(16)–(18) 有定义。
- $\beta=0$：引理 4，对所有 $\alpha$ 有效。
- 分界：大分支 $\alpha>\alpha_\epsilon$，平台分支 $0<\alpha\le\alpha_\epsilon$，$\alpha=0$ 由平台给出 $T_\epsilon=+\infty$。
- 机制：新问题从零出发时就有振幅固定的单位模分量；为满足标准初始化而增加的快分量满足 $|x_{\rm f}^k|\le X/4$、$|\lambda_{\rm f}^k|,|\mu_{\rm f}^k|\le C_{\rm du}bX$，在任何早期迭代都不足以抵消证书。

---

# Part III：关于 $s$ 一致的修订（最终版常数与门槛）

可以改进到 $1/(\rho+s)$：原来的 $s^{-3/2}$ 门槛来自过强的瞬态估计。关键是对初值项使用卷积核的最大值，对持续反馈项仍使用卷积核的绝对和；同时允许原始快分量的绝对和为 $O(s)$。原实例公式、零初始化的代数构造、更新顺序和后原始步证书保持不变。结论：在固定 $(\gamma,\eta,\tau)$ 下，存在不依赖 $s,\rho,\alpha,\beta$ 的 $c_1,c_2(\Delta)$，使 $\epsilon(\rho+s)\le c_1$、$0<\epsilon<c_2(\Delta)$ 时
$$\inf_{(\alpha,\beta)\in[0,1]^2}\sup_{I\in\mathcal I_0(\mathbf C_0,\Delta)}T_\epsilon\ge\frac{\Delta}{32768\gamma K}\epsilon^{-4},\qquad K=\max\{1,4\tau,4\gamma\tau\}.\tag{A}$$

## 1. 常数与门槛
$\chi:=\eta/\gamma$，$\sigma:=\rho+s$，$d:=\tau/s$；$K$，$b_\epsilon:=8\epsilon$，$\alpha_\epsilon:=1024K\epsilon^2$ (B)。
$C_\chi:=1+\frac4\chi$，$A_\chi:=\frac1\chi+\frac54$，$B_\chi:=\frac1\chi+\frac52$。
$$C^\sharp_{\rm tr}(s):=\frac1d+\frac{2(1+d^{-1})}\chi,\tag{C1}\qquad C^\sharp_{\rm du}(s):=sA_\chi,\quad C^\sharp_{\rm res}(s):=sB_\chi,\tag{C2}$$
$C_{\rm gap}=\sigma+2\gamma$ (C3)；$C^\sharp_{\rm tr}\le\frac{C_\chi}d=\frac{C_\chi s}\tau$ (C4)。
$$c_1:=\min\Big\{\frac1{32}\sqrt{\frac\tau{\eta C_\chi}},\ \frac1{64B_\chi},\ \frac1{16(3+\tau^{-1})}\Big\},\tag{D1}$$
$$c_2(\Delta):=\min\Big\{\frac1{64},\ \frac1{32\sqrt K},\ \frac\Delta{12},\ \frac{\sqrt\Delta}2,\ \sqrt{\frac\Delta{64\gamma}}\Big\},\tag{D2}$$
门槛 $\epsilon^\sharp=\min\{c_1/(\rho+s),c_2(\Delta)\}$ (D3)；以下采用 $0<\epsilon<c_2(\Delta)$，$\epsilon\sigma\le c_1$ (D4)。$c_1$ 不依赖 $\bar\rho$。

## 2. 引理 1♯（参数估计）
沿用 Part II (6)–(11) 的构造（$D=\alpha W$）。在 (D4) 下：
$$\frac\nu{\alpha^2}\le\frac1{64},\quad\frac\chi2\le D\le1,\quad7\epsilon\le b\le8\epsilon,\tag{H1}$$
$$\xi C^\sharp_{\rm tr}\le\frac1{16},\tag{H2}\qquad0<\kappa\le\frac1{32},\tag{H3}$$
$$aX\le\frac18b|\Lambda|+sb^2X,\qquad\kappa X^2\le(\sigma+2\gamma)b^2\max\{X^2,|\Lambda|^2\}.\tag{H4}$$
*证明.* $U\ge\chi$、$V\ge\beta$、$\alpha>16Kb_\epsilon^2$ 给出 $\frac\nu{\alpha^2}\le\frac{\gamma\tau b_\epsilon^2}\alpha<\frac{\gamma\tau}{16K}\le\frac1{64}$。$\delta=\nu/\alpha^2$，$D=\alpha+\frac{\chi(1-\alpha)}{1+(1-\alpha)\delta}$，故 $\frac U{1+\delta}\le D\le U\le1$，$D\ge\chi/2$。$\frac{b^2}{b_\epsilon^2}=\frac{\alpha W}U\frac{\beta H}{VJ}\le1$（因 $VJ-\beta H=(1-V)(V-\beta)\nu\ge0$）。由 $H\ge V^2$、$V-\beta\le V$、$V\ge d$：$\xi\le\frac{\eta\tau b^2}V\le\eta sb^2$。结合 (C4) 与 $\epsilon s\le c_1$：
$$\xi C^\sharp_{\rm tr}\le\eta sb_\epsilon^2\frac{C_\chi s}\tau=\frac{64\eta C_\chi}\tau(\epsilon s)^2\le\frac{64\eta C_\chi}\tau c_1^2\le\frac1{16}.\tag{I}$$
因 $C^\sharp_{\rm tr}\ge1/d$，$\xi/d\le1/16$；由 $\frac{\beta H}{VJ}=1-\frac{(1-V)\xi}{WV}$ 得 $\frac{b^2}{b_\epsilon^2}\ge\frac{64}{65}\frac{15}{16}=\frac{12}{13}>\frac{49}{64}$，$b\ge7\epsilon$。分解 $a=a_{\rm p}+a_{\rm d}$，$a_{\rm p}=\frac{\nu(W-1)}{\eta\alpha}$，$a_{\rm d}=\frac\xi\eta$；由 $\eta\tau b^2=\nu W+V\xi$，$a_{\rm p}\le\frac{\tau b^2}\alpha$，$a_{\rm d}\le sb^2$，$\kappa\le\sigma b^2+\frac{\tau b^2}\alpha$ (J)。$B_\chi\ge7/2$ 故 $c_1\le1/224$；$\sigma b^2\le64\epsilon^2\sigma\le64c_1\epsilon\le\frac1{64}$，$\frac{\tau b^2}\alpha<\frac\tau{16K}\le\frac1{64}$，得 $\kappa\le\frac1{32}$。令 $E_\beta=\beta^2+(1-\beta)\nu$，$\frac{|\Lambda|^2}{X^2}=\frac{\tau WE_\beta}{\eta J}$，$J\le\Re((u+V)\overline{(u+\beta)})\le\sqrt{HE_\beta}$；$\frac{a_{\rm p}X}{b|\Lambda|}=\frac{\sqrt\nu(W-1)J}{\alpha W\sqrt{HE_\beta}}\le\frac{\sqrt\nu}\alpha\le\frac18$，$\frac{a_{\rm p}X^2}{b^2|\Lambda|^2}=\frac{\eta(W-1)J^2}{\alpha W^2HE_\beta}\le\frac\eta{\alpha W}\le2\gamma$。加上 $a_{\rm d}\le sb^2$ 得 (H4)。∎

## 3. 引理 3♯（瞬态估计）
$\vartheta=(1-V)\xi$，$r_{\rm p}=1-D$，$r_{\rm d}=1-V$，$Q_{\rm f}(t)=(t-r_{\rm p})(t-r_{\rm d})-\vartheta(t-1+\alpha)$ (K)，来自 Part II (22) 的精确因式分解 (L)。初值 $r_x$、$h_x$ 同 Part II (16)–(17)，记为 (M1)、(M2)。$t_k=x_{\rm f}^k$，$t_0=r_x$，$t_1=r_{\rm p}r_x+h_x$，
$$t_{k+2}-(r_{\rm p}+r_{\rm d})t_{k+1}+r_{\rm p}r_{\rm d}t_k=\vartheta[t_{k+1}-(1-\alpha)t_k].\tag{N}$$
**引理 3♯.** 快分量趋于零，且
$$\sup_{k\ge0}|x_{\rm f}^k|\le\frac X4,\qquad\sum_{k\ge0}|x_{\rm f}^k|\le\frac X{\chi d},\tag{O1}$$
$$|\lambda_{\rm f}^k|,|\mu_{\rm f}^k|\le C^\sharp_{\rm du}bX,\qquad k\ge0.\tag{O2}$$
*3.1 稳定性.* 由 $D\ge\chi/2$、$V\ge d$、$C^\sharp_{\rm tr}\ge2/(\chi d)$：$\frac{2\vartheta}{DV}\le\frac{4\xi}{\chi d}\le2\xi C^\sharp_{\rm tr}\le\frac18$ (P)（下文放宽为 $\le\frac14$）。若 $|t|\ge1$，$|(t-r_{\rm p})(t-r_{\rm d})|\ge DV|t|^2$，$|\vartheta(t-1+\alpha)|\le2\vartheta|t|$，二者不相等，$Q_{\rm f}$ 的根全在单位圆内；由 $Q_{\rm f}(\mathbb M)\mathbf r=0$，快分量趋于零（含快根重合）。
*3.2 核的最大值与绝对和分开.* $G_j=\sum_{i=0}^jr_{\rm p}^{j-i}r_{\rm d}^i$，
$$\sup_jG_j\le\frac1D,\qquad\sum_jG_j=\frac1{DV}.\tag{Q}$$
前者控制初值 $h_x$ 的单次作用，后者控制每步反馈。由 $|u+\alpha|^2=E\ge\alpha^2$、$|u+V|^2=H\ge V^2$ 与 (H1)–(H2)：$|r_x|\le(\frac18+\frac\xi d)X\le\frac{3X}{16}$，$|h_x|\le\xi(1+d^{-1})X$，故
$$|r_x|+\frac{|h_x|}D\le\Big(\frac18+\xi C^\sharp_{\rm tr}\Big)X\le\frac{3X}{16}.\tag{R}$$
（与 Part II 的区别：左边由 $|r_x|+|h_x|/(DV)$ 改为 $|r_x|+|h_x|/D$。）解的表示
$$t_k=r_{\rm p}^kr_x+G_{k-1}h_x+\vartheta\sum_{j=0}^{k-2}G_{k-2-j}[t_{j+1}-(1-\alpha)t_j],\quad k\ge1.\tag{S}$$
$M_N=\max_{0\le k\le N}|t_k|\le|r_x|+\frac{|h_x|}D+\frac{2\vartheta}{DV}M_N$，由 (P)、(R)，$M_N\le\frac{3X/16}{1-1/4}=\frac X4$，对任意 $N$ 成立。
*3.3 绝对和.* $S_N\le\frac{|r_x|}D+\frac{|h_x|}{DV}+\frac{2\vartheta}{DV}S_N$；$A_0:=|r_x|+\frac{|h_x|}D\le\frac{3X}{16}$，$\frac{|r_x|}D+\frac{|h_x|}{DV}\le\frac{A_0}{DV}$，故 $S_N\le\frac{A_0}{DV(1-1/4)}\le\frac X{4DV}\le\frac X{2\chi d}\le\frac X{\chi d}$。（允许绝对和为 $O(s)$，单步振幅仍 $\le X/4$。）
*3.4 对偶快分量.* $e^k:=\lambda_{\rm f}^k-\mu_{\rm f}^k$，$v^k:=\frac{\beta(1-d)\lambda_{\rm f}^k+d\mu_{\rm f}^k}V$，
$$e^{k+1}=(1-V)e^k+\tau b(1-\beta)x_{\rm f}^{k+1},\tag{T1}\qquad v^{k+1}=v^k+\frac{\tau b\beta}Vx_{\rm f}^{k+1}.\tag{T2}$$
$e^0=-\frac{\tau b(1-\beta)\zeta}{u+V}X$，$|e^0|\le sbX$；$|e^k|\le sbX+\frac{\tau b(1-\beta)}V\frac X4\le\frac54sbX$ (U1)。$v^k=-\frac{\tau b\beta}V\sum_{j>k}x_{\rm f}^j$，由 $\beta\le V$ 与 (O1)，$|v^k|\le\tau b\frac X{\chi d}=\frac s\chi bX$ (U2)。$\lambda_{\rm f}^k=v^k+\frac dVe^k$，$\mu_{\rm f}^k=v^k-\frac{\beta(1-d)}Ve^k$，系数不超过 1，得 $|\lambda_{\rm f}^k|,|\mu_{\rm f}^k|\le s(\frac1\chi+\frac54)bX$，即 (O2)。∎

## 4. 下游估计
$p^k=\zeta^kX+x_{\rm f}^k$，$\ell^k=\zeta^k\Lambda+\lambda_{\rm f}^k$；$\frac34X\le|p^k|\le\frac54X$ (V)。实例同 Part II (31)–(34)，$x_c=-\mathcal V(X+r_x)$，$\lambda_c=-\mathcal V(\Lambda+\lambda_{\rm f}^0)$。
*4.1 prox 分支.* $bC^\sharp_{\rm res}\le8\epsilon sB_\chi\le8c_1B_\chi\le\frac18$ (W1)。由 $2A_\chi\ge5/4$：$b(2C^\sharp_{\rm du}+5\rho/4)\le8\epsilon(2A_\chi s+5\rho/4)\le16A_\chi\epsilon\sigma\le16A_\chi c_1\le\frac{A_\chi}{4B_\chi}<\frac14$ (W2)。故
$$\|\lambda^k+\rho A(x^j)\|\le2|\Lambda|+2C^\sharp_{\rm du}bX+\frac54\rho bX\le\frac13[2+b(2C^\sharp_{\rm du}+5\rho/4)]\le\frac34<1,\quad j=k,k+1,\tag{W3}$$
两次 prox 输出从 $k=0$ 起为零；结合 (V)，梯度始终在半径 $R_*$ 的二次区域；候选轨迹即实际轨迹。
*4.2 证书.* $R_k=\max\{|-ap^{k+1}+b\ell^k|,b|p^{k+1}|\}$ (X1)；$b|p^{k+1}|\ge\frac34bX$ (X2)；$|-ap^{k+1}+b\ell^k|\ge b|\Lambda|-C^\sharp_{\rm du}b^2X-\frac54aX\ge\frac{27}{32}b|\Lambda|-C^\sharp_{\rm res}b^2X$ (X3)。$|\Lambda|\ge X$ 时由 (W1) 至少 $\frac{23}{32}b|\Lambda|\ge\frac12b|\Lambda|$；$X\ge|\Lambda|$ 时用 (X2)。故
$$R_k\ge\frac b2\max\{X,|\Lambda|\}=\frac b6\ge\frac76\epsilon>\epsilon,\quad k\ge0;\qquad T_\epsilon=+\infty.\tag{X4}$$
*4.3 全局假设与间隙.* 由 (W1)，$\|\lambda_c\|\le|\Lambda|+C^\sharp_{\rm du}bX\le\frac13(1+\frac{A_\chi}{8B_\chi})<\frac12$；$L_f\le\kappa\le\frac1{32}$，$G_f\le\kappa R_*+b\|\lambda_c\|<1$，$L_A=0$，$G_A=b\le1$，$L_h=1$，均不随 $s,\epsilon,\alpha,\beta$ 恶化；水平集有界。间隙
$$F(0)-\inf F\le5\epsilon+\frac{100}9(\sigma+2\gamma)\epsilon^2\tag{Y1}$$
由 $\epsilon\sigma\le c_1\le1/224$，$\le6\epsilon+32\gamma\epsilon^2$ (Y2)；$c_2$ 中 $\epsilon\le\Delta/12$、$\epsilon^2\le\Delta/(64\gamma)$ 给出 $\le\Delta$ (Y3)。

## 5. 其余分支与门槛核对
*5.1 小 $\alpha$ 不依赖 $s$.* 平台实例 $A\equiv0$，$\lambda^k=\mu^k=0$，原始递推不含 $s$。$T_\epsilon\ge\frac{\Delta}{32\gamma\alpha\epsilon^2}$ 所需条件 $4\epsilon^2\le\Delta$、$4\epsilon^2\le\frac\Delta{8\gamma}$ 由 $c_2$ 保证。$\epsilon<\frac1{32\sqrt K}\Rightarrow\alpha_\epsilon<1$。交界 $\alpha=\alpha_\epsilon$ 由平台分支覆盖。
*5.2 $\beta=0$ 只要求 $\epsilon\sigma$ 小.* 引理 4 的关键条件 $q_ha_0=4\epsilon(\rho+3s+1)\le\frac14$；由 $s\ge\tau$，$\rho+3s+1\le(3+\tau^{-1})(\rho+s)$，故由 $c_1$ 第三项 $q_ha_0\le4c_1(3+\tau^{-1})\le\frac14$ (Z1)。闭式对偶轨迹 $\lambda^k=\lambda_*(1-r_\theta^k)$，$\mu^k=0$，$y^{k+1}\in[0,a_0]\subset[0,q_h^{-1}]$，可行性残差 $4\epsilon(1+\frac sQr_\theta^k)>2\epsilon$ (Z2)，$T_\epsilon=+\infty$。$q_h$ 是局部二次曲率，全局 Lipschitz 常数仍为 1。
*5.3 门槛各项用途.*

| 项 | 控制 |
|---|---|
| $c_1\le\frac1{32}\sqrt{\tau/(\eta C_\chi)}$ | $\xi C^\sharp_{\rm tr}\le1/16$：快模态稳定与瞬态振幅 |
| $c_1\le1/(64B_\chi)$ | $bC^\sharp_{\rm res}\le1/8$：prox 分支与对偶平移量有界 |
| $c_1\le1/[16(3+\tau^{-1})]$ | $\beta=0$ 分支 $q_ha_0\le1/4$ |
| $\epsilon\le1/64$ | 与 $\epsilon\sigma\le c_1$ 合用：$\sigma b^2\le1/64$、$\kappa\le1/32$ |
| $\epsilon\le1/(32\sqrt K)$ | $\alpha_\epsilon\le1$ |
| $\epsilon\le\Delta/12$，$\epsilon^2\le\Delta/(64\gamma)$ | 旋转实例的间隙预算 |
| $\epsilon\le\sqrt\Delta/2$，$\epsilon^2\le\Delta/(64\gamma)$ | 平台实例的有效范围 |

## 6. 定理与推论（最终版）
**定理.** 固定 $0<\eta\le\gamma$，$\tau>0$，$\Delta>0$（原文另列 $\bar\rho$，但 $c_1$ 不依赖它，论文中已删去）。令 $c_1,c_2(\Delta)$ 由 (D1)–(D2) 定义，$\mathbf C_0=(1,1,0,1,1)$，$K=\max\{1,4\tau,4\gamma\tau\}$。对任意 $0<\epsilon<c_2(\Delta)$、$\rho>0$、$s\ge\tau$、$\rho+s\le c_1/\epsilon$ 及任意 $(\alpha,\beta)\in[0,1]^2$，存在至多二维实例 $I\in\mathcal I_0(\mathbf C_0,\Delta)$（全部初值为零）使
$$T_\epsilon(\rho,s,\gamma,\eta,\tau,\alpha,\beta;I)\ge\frac{\Delta}{32768\gamma K}\epsilon^{-4}.\tag{AA}$$
*证明.* $\alpha=0$：平台，$T_\epsilon=+\infty$。$0<\alpha\le\alpha_\epsilon$：$T_\epsilon\ge\frac{\Delta}{32\gamma\alpha\epsilon^2}\ge\frac{\Delta}{32768\gamma K}\epsilon^{-4}$。$\alpha>\alpha_\epsilon$、$\beta>0$：$R_k\ge\frac76\epsilon$，$T_\epsilon=+\infty$（含 $\alpha=1$、$\beta=1$；核估计只要求 $0<D,V\le1$）。$\alpha>\alpha_\epsilon$、$\beta=0$：(Z2)。∎

**推论.** 允许 $\rho=\rho(\epsilon)$、$s=s(\epsilon)\ge\tau$ 随精度选择（每次运行内为常数）。若 $\rho+s=o(\epsilon^{-1})$，则 $\inf_{(\alpha,\beta)}\sup_IT_\epsilon=\omega(\epsilon^{-3})$ (AB)。更强地，该子类在固定 $(\gamma,\eta,\tau)$ 下若有统一的 $O(\epsilon^{-3})$ 保证，则最终必须 $\rho(\epsilon)+s(\epsilon)>c_1/\epsilon$，即 $\rho+s=\Omega(\epsilon^{-1})$；$\rho$ 有界时 $s=\Omega(\epsilon^{-1})$。这只是必要条件：下界覆盖足够小系数的 $c_1/\epsilon$ 以下区域，不是所有 $s=\Theta(1/\epsilon)$。

## 7. 关于 $\gamma$ 的依赖
若 $\gamma$ 随精度增长，$\gamma K\sim4\tau\gamma^2$，下界退化为 $\Omega(\frac\Delta{\tau\gamma^2}\epsilon^{-4})$，且 $\chi=\eta/\gamma$ 影响 $c_1,c_2$。若 $\eta\le\gamma\le\bar\gamma$，用 $\chi_{\min}=\eta/\bar\gamma$、$\bar K=\max\{1,4\tau,4\bar\gamma\tau\}$ 得统一下界 $\frac{\Delta}{32768\bar\gamma\bar K}\epsilon^{-4}$，推论不受影响。

---

# GPT Pro 对整体进度的判断（分享链接最后一条，摘要）

- 主线已收敛到上述定理；它比最初任务多了两点加强：不再依赖对手挑选初值；门槛统一为 $\epsilon(\rho+s)\le c_1$。
- 状态应准确表述为"有证明草稿及修订"，整份证明尚未独立复核。
- 能推出参数尺度的必要性；不能推出四次是紧界（需固定参数下的匹配上界），也不能推出达到该尺度就一定有三次上界（需配套上界）。
- 当务之急：把"平台实例—零初值旋转实例—$\beta=0$ 实例—$s$ 一致估计—主定理"合成同一版本并逐条核验；优先核查零初值旋转分支的谱分解、区域不变性、瞬态不抵消证书。
- 推论措辞：用 "Moreover, Theorem 1 implies"，不用 "Equivalently"。
