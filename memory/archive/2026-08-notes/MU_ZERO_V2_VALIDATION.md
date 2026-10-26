# V2 固定零中心特例验证记录

## 结论

本记录将“`mu=0`”解释为固定中心
\(\mu^k\equiv0\)，而不是仅设置初值 \(\mu^0=0\)。在 V2 的原有全局
光滑性、`h` 全局 Lipschitz、下界和参数条件下，固定零中心特例保留

\[
\mathcal R_{\rm split}=O(K^{-1/3}),
\qquad K=O(\varepsilon^{-3}).
\]

该结论针对 V2 的四块 Candidate 去掉最后一个恒等中心块后的特例。它不
自动推广到 `PROOF_PACKAGE.md` 中的三块显式 reduced-dual ascent，也不
覆盖固定正中心或其他 moving-center 规则。

## 1. 专化后的算法

保留 V2 的 \(x\)、\(\lambda\)、\(z\) 更新，并令 \(\mu^k=0\)：

\[
y^k=\operatorname{prox}_{h/\rho}\left(A(x^k)+\lambda^k/\rho\right),
\qquad
q^k=\lambda^k+\rho(A(x^k)-y^k),
\]

\[
x^{k+1}=x^k-c\left[\nabla f(x^k)+J_A(x^k)^\top q^k+r_x(x^k-z^k)\right],
\]

\[
\widehat y^{k+1}=\operatorname{prox}_{h/\rho}
\left(A(x^{k+1})+\lambda^k/\rho\right),
\]

\[
\lambda^{k+1}=\lambda^k+\alpha
\left[A(x^{k+1})-\widehat y^{k+1}-r_k\lambda^k\right],
\]

\[
z^{k+1}=z^k+\beta_k(x^{k+1}-z^k).
\]

这里仍有两次固定参数 \(\operatorname{prox}_{h/\rho}\) 调用。保留
\(r_k=c_r(k+k_0)^{-1/3}\)、\(\beta_k=(\theta_z/\ell_\rho)r_k\)、固定
\(c,\alpha\) 和 V2 的全部正参数条件。为逐字应用 Li--Nagarajan--Pan--Zhang
的 `Condition 3.2`，还要显式取

\[
r_x=\kappa_x\ell_\rho,
\qquad \kappa_x>3
\]

且 \(\kappa_x\) 为固定常数；例如 \(r_x=4\ell_\rho\)。

## 2. 引理逐项核对

| 部分 | 零中心后的结果 | 状态 |
|---|---|---|
| C1.1--C1.3 | prox 最优性、\(q\in\partial h(y)\)、reduced payoff 的梯度和精确最大值不含中心更新假设 | 保持 |
| C2 | 令 \(q_+^{k+1}=\lambda^k+\rho(A(x^{k+1})-\widehat y^{k+1})\)，则 \(\|q_+^{k+1}\|\le L_h\)，且 | 通过 |
|  | \(\lambda^{k+1}=[1-\alpha(\rho^{-1}+r_k)]\lambda^k+(\alpha/\rho)q_+^{k+1}+\alpha r_k\,0\) |  |
| C3--C4 | \(\mathcal F_{r,0}=\mathcal D_\rho+r_x\|x-z\|^2/2-r\|\lambda\|^2/2\)，仍满足 frozen three-value descent 和同一 \(\beta_k\) cap | 保持 |
| C5.1 | \(\mu^{k+1}-\mu^k=0\)，故 moving-center transport 差值严格为零 | 通过 |
| C5.2 | 只剩 \(r\)-漂移，且 \(\sum_k|r_{k+1}-r_k|=r_0<\infty\) | 通过 |
| C6 | master inequality 只含 \(C_r|r_{k+1}-r_k|\)，右端与 \(K,\varepsilon\) 无关 | 通过 |
| C7--C8 | primal target、实际 \(\lambda\) 增量、精确 certificate、共同尾部索引的推导不使用 \(\gamma_k>0\) | 保持 |

### 2.1 Multiplier boundedness

若

\[
0<\alpha\le(\rho^{-1}+r_0)^{-1},
\]

则三个系数

\[
1-\alpha(\rho^{-1}+r_k),
\qquad \alpha/\rho,
\qquad \alpha r_k
\]

非负且和为一。因此 \(\lambda^{k+1}\) 是 \(\lambda^k\)、\(q_+^{k+1}\)
和零向量的凸组合。归纳得到

\[
\|\lambda^k\|\le M_0,
\qquad
M_0:=\max\{\|\lambda^0\|,L_h\}.
\]

证明中的分析球只需取 \(Y=B_R(0)\)，其中 \(R>M_0\)。

### 2.2 Lyapunov 漂移

固定中心势函数为

\[
\Psi_{r,0}(x,\lambda,z)
=\mathcal F_{r,0}(x,\lambda,z)
-2d_{r,0}(\lambda,z)+2p_{r,0}(z).
\]

V2 的 C5.1 差值在 \(\mu'=\mu=0\) 时为零。C5.2 给出

\[
|\Psi_{r_{k+1},0}(u)-\Psi_{r_k,0}(u)|
\le C_r|r_{k+1}-r_k|.
\]

因此 C6 的总预算可写为

\[
B_0\le V_0-\underline V+C_r r_0<\infty,
\]

其中可以取

\[
\underline V=F_{\inf}-\frac{r_0}{2}L_h^2.
\]

该常数不依赖终止步数或目标精度。

### 2.3 C4 外部结果的条件核销

V2 的 C4 使用 Li--Nagarajan--Pan--Zhang 2026 的 `Condition 3.2`、
Lemmas 4.4--4.5。固定零中心下，条件对应如下。

| 外部对象或条件 | V2 固定零中心对应物 | 核销 |
|---|---|---|
| smooth NC-C payoff \(f_{\rm ext}(x,y)\) | \(\mathcal D_\rho(x,\lambda)\) | C1.1--C1.2 给出全局 \(\ell_\rho\)-smooth；C1.3 给出关于 \(\lambda\) 的凹性 |
| closed convex \(X\) | \(\mathbb R^n\) | projection 是恒等映射 |
| compact convex \(Y\) | \(B_R(0)\)，\(R>M_0\) | C2 保证实际 \(\lambda^k\in B_{M_0}\subset\operatorname{int}Y\)；proof-only projection 不激活 |
| dual diameter \(D_Y\) | \(2R\) | 有限且不依赖 \(K,\varepsilon\) |
| surrogate \(F_t\) | \(\mathcal F_{r_k,0}=\mathcal D_\rho+r_x\|x-z\|^2/2-r_k\|\lambda\|^2/2\) | 完全相同 |
| \(r_x=\Theta(\ell),\ r_x>3\ell\) | \(r_x=\kappa_x\ell_\rho,\ \kappa_x>3\) | 显式保留 |
| \(r_y^t>0\) | \(r_k=c_r(k+k_0)^{-1/3}>0\) | 成立 |
| constant primal/dual steps | \(c,\alpha=\Theta(1/\ell_\rho)\) | 保留 V2 的显式上界 |
| center step | \(\beta_k=(\theta_z/\ell_\rho)r_k\) | 取固定且足够小的 \(\theta_z>0\) |

令 \(m(r)=r_x-\ell_\rho-r\) 和

\[
m_0=r_x-\ell_\rho-r_0>0.
\]

因为 \(0<r_k\le r_0\le\ell_\rho\)，V2 的统一条件

\[
c<(r_x+\ell_\rho+r_0)^{-1}
\]

推出外部条件 \(c<(r_x+\ell_\rho+r_k)^{-1}\)。同理，函数

\[
\frac{c^2m(r)^2}
{4(\ell_\rho+r)[1+cm(r)]^2}
\]

关于 \(r\) 递减，所以在 \(r=r_0\) 处施加 V2 的 \(\alpha\) 上界即可
统一满足 `Condition 3.2`。额外条件
\(\alpha\le(\rho^{-1}+r_0)^{-1}\) 用于 C2 的无投影 boundedness。

C4.2 中

\[
\Omega(r)
=\frac{1}{\sqrt r}
\frac{m(r)+\alpha(\ell_\rho+r)(3r_x-2\ell_\rho-2r)}
{\alpha m(r)^{3/2}}
\]

满足 \(\Omega(r)\le C_\Omega/\sqrt r\)，因为括号中的系数在
\(r\in(0,r_0]\) 上连续且一致有界。因此第三个 cap 满足

\[
\frac{1}{384r_x\alpha\Omega(r)^2}
\ge c_\Omega r
\]

其中 \(c_\Omega>0\) 与 \(k,K,\varepsilon\) 无关。前两个 cap 也分别有
正的一致下界。故存在固定 \(\theta_z>0\)，使
\(\beta_k=(\theta_z/\ell_\rho)r_k\) 对所有 \(k\) 满足三个 cap。

外部 Section 4.2 明确允许 adaptive \(r_y^t\)。其 Lemma 4.4 的时变参数
误差也可由本记录 C5.2 的
\(C_r|r_{k+1}-r_k|\) 控制。Lemma 4.5 对每个 \(r_k>0\) 适用。因此 C4
向固定零中心 V2 的迁移所需条件均已核销。

## 3. 残差与复杂度

从 C6 的预算中，在
\(I_K=\{\lceil K/2\rceil,\ldots,K-1\}\) 选择同一个 \(\kappa\)，得到

\[
\|\Delta x^{\kappa+1}\|+e_{\lambda,\kappa}=O(K^{-1/2}),
\qquad
\|z^\kappa-x^{\kappa+1}\|=O(K^{-1/3}).
\]

prox certificate 仍然精确给出

\[
q_\kappa^{\rm out}
\in\partial h(\widehat y^{\kappa+1}).
\]

由于 \(r_\kappa=O(K^{-1/3})\) 且 \(\|\lambda^\kappa\|\le M_0\)，C8.1--C8.2
分别给出

\[
\left\|\nabla f(x^{\kappa+1})
+J_A(x^{\kappa+1})^\top q_\kappa^{\rm out}\right\|
=O(K^{-1/3}),
\]

\[
\|A(x^{\kappa+1})-\widehat y^{\kappa+1}\|
=O(K^{-1/3}).
\]

故固定零中心版本仍满足

\[
\mathcal R_{\rm split}=O(K^{-1/3}),
\qquad
K=O(\varepsilon^{-3}).
\]

相较 moving-\(\mu\) 版本，feasibility 重构中的中心差项由
\(r_k\|\lambda^k-\mu^k\|\le2Mr_k\) 改为更紧的
\(r_k\|\lambda^k\|\le M_0r_k\)。

## 4. 标量 sanity checks

### \(h\equiv0, A\equiv0\)

此时 \(y=\lambda/\rho\)、\(q=0\)，并且

\[
\lambda^{k+1}
=\left[1-\alpha(\rho^{-1}+r_k)\right]\lambda^k.
\]

在上述 \(\alpha\) 条件下，因子属于 \([0,1]\)，所以 multiplier 轨道不扩大。

### \(h(t)=|t|, A(x)=x\)

取 \(\rho=1\)、\(f(x)=0.05x^2\)、\(r_x=4\ell_\rho\)、
\(c=0.04\)、\(\alpha=0.0047502172\)、\(\theta_z=10^{-5}\)。该
\(\theta_z\) 在 \(r_k\in[10^{-8},1]\) 上满足 C4.2 的全部三个 cap。对
central prox 区域和 positive active 区域分别线性化，谱半径在整个网格上均
小于一；谱半径随 \(r_k\to0\) 接近一，但没有出现局部发散。该检查只支持
稳定性判断，不替代复杂度证明。

## 5. 最终判定与边界

**判定：通过，条件为固定 \(\mu^k\equiv0\)，保留 V2 的 varying-\(r_k\)
设计，并将 Li--Nagarajan--Pan--Zhang Lemmas 4.4--4.5 作为已核销条件的
外部结果。**

需要在后续正式文本中明确：

1. 删除 \(\gamma_k\)、\(\theta_\mu\) 和 moving-center transport 项；
2. 将 \(M\) 改为 \(M_0\)，并在 proof-only 分析中取 \(R>M_0\)；
3. 保留 \(r_k\downarrow0\)，不能把“\(\mu=0\)”误写成取消 dual regularization；
4. 结论是 V2 的固定零中心特例，不等同于 `PROOF_PACKAGE.md` 的三块算法。

本结论的证据等级是 `accepted_by_review`。它没有经过 Lean 等 proof
assistant 的机器检查。

本次验证没有修改 V2 源文件、主论文或 PDF。

## 6. 独立审阅记录

第一次独立审阅给出 `WARN`，唯一全局问题是 C4 未在 V2 内逐项核销外部
`Condition 3.2`。本记录 Section 2.3 补齐该映射后，新的独立审阅给出
`PASS`，未发现 FATAL、CRITICAL 或 MAJOR 问题。

最终证据链为：V2 C1--C8 的零中心专化、Li--Nagarajan--Pan--Zhang
Lemmas 4.4--4.5 的条件核销、两个标量 sanity checks，以及一次修复后的独立
验收。该证据支持 `accepted_by_review`，不构成 `machine_checked`。
