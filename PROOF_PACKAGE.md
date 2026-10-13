# Proof Package

## Claim

Consider the composite problem

$$
F(x)=f(x)+h(A(x)),
$$

where $h$ is proper, closed, convex, and globally Lipschitz. For fixed
$\rho>0$, a dual-regularization scale $s>0$, and a moving center $\mu$, define

$$
P_s(x,y,\lambda;\mu)
=f(x)+h(y)+\langle\lambda,A(x)-y\rangle
+\frac{\rho}{2}\|A(x)-y\|^2
-\frac{1}{2s}\|\lambda-\mu\|^2,
$$

and the reduced-dual function

$$
d_s(x,\lambda;\mu):=\min_y P_s(x,y,\lambda;\mu).
$$

The algorithm studied in this package uses only the map

$$
y(\lambda;x)
:=
\operatorname{prox}_{h/\rho}
\left(A(x)+\frac{\lambda}{\rho}\right).
$$

Its three updates are

$$
x^{k+1}
=x^k-\eta_k
\left[
\nabla f(x^k)
+J_A(x^k)^\top
\left(
\lambda^k+\rho\left[A(x^k)-y(\lambda^k;x^k)\right]
\right)
\right],
$$

$$
\lambda^{k+1}
=\lambda^k+\alpha_k
\left[
A(x^{k+1})-y(\lambda^k;x^{k+1})
-\frac{\lambda^k-\mu^k}{s_k}
\right],
$$

and

$$
\mu^{k+1}
=(1-\omega_k)\mu^k+\omega_k\lambda^{k+1}.
$$

The second update is exactly one explicit gradient-ascent step:

$$
\lambda^{k+1}
=\lambda^k+\alpha_k
\nabla_\lambda d_{s_k}(x^{k+1},\lambda^k;\mu^k).
$$

The main parameter candidate is

$$
s_k=c_s(k+1)^a,
\qquad
\eta_k=\frac{\theta_x}{\rho+s_k},
$$

$$
\alpha_k
=\theta_\lambda\frac{\rho s_k}{\rho+s_k},
\qquad
\omega_k=\theta_\mu,
$$

where

$$
a\in(0,1),
\qquad
c_s>0,
\qquad
0<\theta_\lambda\le 1,
\qquad
0<\theta_\mu<1.
$$

The notation

$$
\tau_k:=s_k\omega_k
$$

is only the equivalent stepsize for gradient ascent in the $\mu$ block. It is
not an additional free parameter.

The target claim is that the moving-center dynamics absorb the multiplier
tracking error in the primal descent inequality and yield a single-loop
$O(\epsilon^{-3})$ split-KKT complexity bound when $a=1/3$.

## Status

**NOT CURRENTLY JUSTIFIED.**

The following parts are proved below.

1. Every algorithmic proximal evaluation is a $\rho$-proximal evaluation.
2. The $\lambda$ update is exactly explicit reduced-dual gradient ascent.
3. The main choice of $\alpha_k$ is the reciprocal reduced-dual smoothness
   scale, up to the fixed factor $\theta_\lambda$.
4. The sequences $\{\lambda^k\}$ and $\{\mu^k\}$ are uniformly bounded.
5. The proximal step gives an exact subgradient relation at every iterate.
6. A conditional master descent budget implies the desired
   $O(\epsilon^{-3})$ complexity.
7. The main $\alpha_k,\omega_k$ choice passes the scalar stability test
   $h\equiv0$, $A\equiv0$.

The unresolved point is one coupled Lyapunov inequality. The standard
exact-target tracking estimate loses two powers of $s_k$ when the target moves
with $x^{k+1}-x^k$. The moving-center recursion may cancel that loss, but the
required cancellation does not follow from the assumptions listed below by
the presently available inequalities. Accordingly, this package does not
state the unconditional $O(\epsilon^{-3})$ theorem as proved.

The previous proof for an implicit reduced-dual proximal-point update has been
removed. That proof analyzed a different algorithm whose computed proximal map
depended on $\rho+\beta s_k$.

## Assumptions

1. The function $h:\mathbb R^m\to\mathbb R$ is proper, closed, convex, and
   globally $L_h$-Lipschitz. Consequently,

$$
\|z\|\le L_h
\qquad
\text{for every }z\in\partial h(y).
$$

2. The functions $f:\mathbb R^n\to\mathbb R$ and
   $A:\mathbb R^n\to\mathbb R^m$ are continuously differentiable. There are
   constants $L_f,L_A,G_A\ge0$ such that, for every $x,x'\in\mathbb R^n$,

$$
\|\nabla f(x)-\nabla f(x')\|
\le L_f\|x-x'\|,
$$

$$
\|J_A(x)-J_A(x')\|
\le L_A\|x-x'\|,
\qquad
\|J_A(x)\|\le G_A.
$$

3. The composite objective is bounded below:

$$
F_{\inf}:=\inf_x F(x)>-\infty.
$$

4. The constants $\rho,c_s,a,\theta_x,\theta_\lambda,\theta_\mu$ are fixed
   independently of the terminal horizon $K$ and target accuracy $\epsilon$.

5. The primal stepsize constant is small enough that

$$
\eta_k L_{\psi,k}\le\frac12,
$$

where $L_{\psi,k}$ is the exact-value smoothness constant established below.

## Parameter Design

### Main dual stepsize

The reduced-dual gradient is $L_{\lambda,s}$-Lipschitz with

$$
L_{\lambda,s}
\le
\frac1\rho+\frac1s.
$$

Therefore the main choice is

$$
\alpha_k
=\frac{\theta_\lambda}{1/\rho+1/s_k}
=\theta_\lambda\frac{\rho s_k}{\rho+s_k}.
$$

This is a model-based adaptive stepsize: it changes with $s_k$ but introduces
no new sequence. It also makes the multiplier update a convex combination,
which yields boundedness without projection.

The original PPT update is recovered formally by taking $\alpha_k=s_k$.
That choice is not used in this package because $s_k\uparrow\infty$ eventually
violates the reduced-dual smoothness bound.

### Main center stepsize

The primary candidate uses

$$
\omega_k=\theta_\mu\in(0,1).
$$

Thus $\mu^k$ follows $\lambda^k$ on the same iteration scale. The exact
center-gap recursion is

$$
\lambda^{k+1}-\mu^{k+1}
=(1-\theta_\mu)
\left[
\lambda^k-\mu^k+\lambda^{k+1}-\lambda^k
\right].
$$

### Optional normalized center rule

If the fixed center step cannot be used in a future coupled Lyapunov proof, a
2P-ADMM-inspired alternative is

$$
\omega_k
=\frac{\zeta_k}
{1+\|\lambda^{k+1}-\mu^k\|^2},
\qquad
\zeta_{k+1}=r\zeta_k,
$$

with $0<r<1$ and $0<\zeta_0\le1$. It guarantees

$$
\|\mu^{k+1}-\mu^k\|
\le\frac{\zeta_k}{2},
\qquad
\sum_{k=0}^\infty
\|\mu^{k+1}-\mu^k\|<\infty.
$$

This rule controls center drift, but it gives no positive uniform lower bound
on $\omega_k$. Hence it does not by itself prove that the center gap supplies
the negative term needed to remove the multiplier-tracking bottleneck. It is
retained as a legitimate fallback, not as part of the main claim.

### Optional residual cap

An ARADMM-inspired cap can be imposed by replacing the main $\alpha_k$ with

$$
\alpha_k
=\min\left\{
\theta_\lambda\frac{\rho s_k}{\rho+s_k},
\frac{b_k}
{\|\nabla_\lambda d_{s_k}(x^{k+1},\lambda^k;\mu^k)\|}
\right\},
$$

where the second term is omitted when the gradient is zero. This gives

$$
\|\lambda^{k+1}-\lambda^k\|\le b_k.
$$

A summable choice of $b_k$ controls multiplier drift but may also make the
total dual progress finite before feasibility is reached. Therefore no
specific cap is included in the main algorithm without a matching lower-bound
argument for accumulated dual progress.

## Notation

The following quantities are used only in the proof. They are not additional
algorithmic variables.

For fixed $(x,\lambda)$, define

$$
r(\lambda;x):=A(x)-y(\lambda;x),
$$

$$
q(\lambda;x):=\lambda+\rho r(\lambda;x).
$$

At iteration $k$, write

$$
r^k:=r(\lambda^k;x^k),
\qquad
q^k:=q(\lambda^k;x^k),
$$

and define the post-primal dual gradient

$$
g_\lambda^k
:=
\nabla_\lambda d_{s_k}(x^{k+1},\lambda^k;\mu^k).
$$

Then

$$
\lambda^{k+1}-\lambda^k=\alpha_k g_\lambda^k.
$$

For fixed $(s,x,\mu)$, let

$$
\lambda_s^\star(x;\mu)
:=\arg\max_\lambda d_s(x,\lambda;\mu),
$$

and define

$$
y_s^\star(x;\mu):=y(\lambda_s^\star(x;\mu);x),
$$

$$
r_s^\star(x;\mu)
:=A(x)-y_s^\star(x;\mu),
$$

$$
q_s^\star(x;\mu)
:=\lambda_s^\star(x;\mu)+\rho r_s^\star(x;\mu).
$$

The exact reduced value is

$$
\psi_s(x;\mu)
:=\max_\lambda d_s(x,\lambda;\mu).
$$

The exact-target error and center gap are

$$
e_k
:=\lambda^k-\lambda_{s_k}^\star(x^k;\mu^k),
$$

$$
d_k:=\lambda^k-\mu^k.
$$

The letter $d_k$ denotes the center gap, while $d_s(x,\lambda;\mu)$ denotes
the reduced-dual function; their subscripts and arguments distinguish them.

## Proof Strategy

The intended proof has four components.

1. Establish reduced-dual calculus, exact proximal optimality, and uniform
   multiplier boundedness.
2. Compare the computed primal gradient with $\nabla_x\psi_{s_k}$ and derive
   primal quasi-descent with an $\eta_k\|e_k\|^2$ error.
3. Couple explicit dual-ascent tracking with the center-gap recursion and the
   motion of the exact target in $(x,\mu,s)$.
4. Prove a master finite-budget inequality and convert it to a common
   tail-iterate split-KKT rate.

Steps 1, 2, and the rate conversion in Step 4 are complete below. Step 3 is
reduced to one explicit proof obligation.

## Dependency Map

1. Lemma 1 derives $d_s$, its gradient, strong concavity, and smoothness.
2. Lemma 2 derives the exact subgradient relation and proximal-map
   nonexpansiveness properties.
3. Lemma 3 uses Lemmas 1--2 to derive the explicit ascent update and uniform
   multiplier boundedness.
4. Lemma 4 uses reduced-dual smoothness and the special convex-combination
   form to prove ascent and fixed-target contraction.
5. Lemma 5 constructs the exact target and proves its sensitivity bounds.
6. Lemma 6 uses Lemmas 2 and 5 to prove exact-value smoothness and primal
   quasi-descent.
7. Lemma 7 records the exact tracking and center-gap recursions.
8. Proposition 1 uses a master finite-budget inequality to obtain the
   $O(K^{-1/3})$ residual rate.
9. Proposition 2 identifies the precise coupled Lyapunov estimate still
   required to establish that master budget.

## Proof

### Lemma 1. Reduced-dual calculus

For every $s>0$, $x\in\mathbb R^n$, $\lambda,\mu\in\mathbb R^m$,

$$
d_s(x,\lambda;\mu)
=f(x)
+e_{1/\rho}h
\left(A(x)+\frac{\lambda}{\rho}\right)
-\frac{1}{2\rho}\|\lambda\|^2
-\frac{1}{2s}\|\lambda-\mu\|^2,
$$

where

$$
e_{1/\rho}h(u)
:=\min_y
\left\{
h(y)+\frac{\rho}{2}\|y-u\|^2
\right\}.
$$

The function $d_s(x,\cdot;\mu)$ is continuously differentiable,
$1/s$-strongly concave, and has gradient

$$
\nabla_\lambda d_s(x,\lambda;\mu)
=r(\lambda;x)-\frac{\lambda-\mu}{s}.
$$

Its gradient is Lipschitz with constant

$$
L_{\lambda,s}
\le\frac1\rho+\frac1s.
$$

#### Proof

Completing the square gives

$$
\begin{split}
&h(y)+\langle\lambda,A(x)-y\rangle
+\frac\rho2\|A(x)-y\|^2 \\
&\quad=
h(y)
+\frac\rho2
\left\|y-\left(A(x)+\frac\lambda\rho\right)\right\|^2
-\frac{1}{2\rho}\|\lambda\|^2.
\end{split}
$$

Minimizing over $y$ proves the displayed expression for $d_s$. Since $h$ is
proper, closed, and convex, its Moreau envelope is continuously
differentiable and

$$
\nabla e_{1/\rho}h(u)
=\rho\left[u-\operatorname{prox}_{h/\rho}(u)\right].
$$

The chain rule then gives

$$
\nabla_\lambda d_s(x,\lambda;\mu)
=A(x)-y(\lambda;x)-\frac{\lambda-\mu}{s}.
$$

For fixed $x$, the part of $d_s$ before the last quadratic is the pointwise
infimum over $y$ of functions affine in $\lambda$, and is therefore concave.
Adding $-\|\lambda-\mu\|^2/(2s)$ makes the sum $1/s$-strongly concave.

Lemma 2 below proves that $\lambda\mapsto r(\lambda;x)$ is
$1/\rho$-Lipschitz. Hence

$$
\begin{split}
&\|\nabla_\lambda d_s(x,\lambda;\mu)
-\nabla_\lambda d_s(x,\lambda';\mu)\| \\
&\quad\le
\left(\frac1\rho+\frac1s\right)
\|\lambda-\lambda'\|.
\end{split}
$$

This proves the lemma.

### Lemma 2. Exact subgradient relation and proximal-map bounds

For every $x$ and $\lambda$,

$$
q(\lambda;x)
=\lambda+\rho\left[A(x)-y(\lambda;x)\right]
\in\partial h\bigl(y(\lambda;x)\bigr).
$$

Consequently,

$$
\|q(\lambda;x)\|\le L_h.
$$

For fixed $x$, the map $\lambda\mapsto q(\lambda;x)$ is firmly
nonexpansive, and

$$
\|r(\lambda;x)-r(\lambda';x)\|
\le\frac1\rho\|\lambda-\lambda'\|.
$$

For fixed $\lambda$,

$$
\|r(\lambda;x)-r(\lambda;x')\|
\le\|A(x)-A(x')\|
\le G_A\|x-x'\|.
$$

#### Proof

The optimality condition defining $y(\lambda;x)$ is

$$
0
\in
\partial h(y(\lambda;x))
+\rho\left[
y(\lambda;x)-A(x)-\frac\lambda\rho
\right].
$$

Rearranging gives the exact subgradient relation. The Lipschitz assumption on
$h$ gives the norm bound.

Let $R:=I-\operatorname{prox}_{h/\rho}$. Both the proximal map and $R$ are
firmly nonexpansive. Since

$$
q(\lambda;x)
=\rho R\left(A(x)+\frac\lambda\rho\right),
$$

for fixed $x$ we obtain

$$
\|q(\lambda;x)-q(\lambda';x)\|^2
\le
\langle q(\lambda;x)-q(\lambda';x),\lambda-\lambda'\rangle.
$$

Thus $q(\cdot;x)$ is firmly nonexpansive. Since

$$
r(\lambda;x)
=-\frac1\rho
\left[
(I-q(\cdot;x))(\lambda)
\right],
$$

up to an $x$-dependent constant, and $I-q(\cdot;x)$ is firmly
nonexpansive, the claimed $1/\rho$ Lipschitz bound follows.

For fixed $\lambda$,

$$
r(\lambda;x)
=R\left(A(x)+\frac\lambda\rho\right)-\frac\lambda\rho.
$$

Nonexpansiveness of $R$ gives the first $x$-sensitivity bound. The second
follows from the global Jacobian bound and the mean-value integral formula.
This proves the lemma.

### Lemma 3. Explicit ascent form and uniform multiplier boundedness

Let

$$
\alpha_k
=\theta_\lambda\frac{\rho s_k}{\rho+s_k},
\qquad
0<\theta_\lambda\le1,
$$

and let $0<\omega_k\le1$. Define the proof-only subgradient

$$
\widehat q^{k+1}
:=q(\lambda^k;x^{k+1}).
$$

Then

$$
\lambda^{k+1}
=(1-\theta_\lambda)\lambda^k
+\theta_\lambda\frac{s_k}{\rho+s_k}\widehat q^{k+1}
+\theta_\lambda\frac\rho{\rho+s_k}\mu^k.
$$

Let

$$
M:=\max\{\|\lambda^0\|,\|\mu^0\|,L_h\}.
$$

Then, for every $k\ge0$,

$$
\|\lambda^k\|\le M,
\qquad
\|\mu^k\|\le M,
\qquad
\|q^k\|\le L_h.
$$

#### Proof

Lemma 1 and the algorithm give

$$
\begin{split}
\lambda^{k+1}
&=\lambda^k+\alpha_k
\left[
\frac{\widehat q^{k+1}-\lambda^k}{\rho}
-\frac{\lambda^k-\mu^k}{s_k}
\right].
\end{split}
$$

Substitution of $\alpha_k$ and collection of coefficients give the stated
convex-combination identity. All three coefficients are nonnegative and sum
to one. Lemma 2 gives $\|\widehat q^{k+1}\|\le L_h$. Therefore

$$
\|\lambda^{k+1}\|
\le
\max\{\|\lambda^k\|,\|\mu^k\|,L_h\}.
$$

The center update is also a convex combination, so

$$
\|\mu^{k+1}\|
\le
\max\{\|\mu^k\|,\|\lambda^{k+1}\|\}.
$$

Induction proves the two multiplier bounds. The last bound follows directly
from Lemma 2.

### Lemma 4. Dual ascent and fixed-target contraction

Fix $x,\mu,s$ and let

$$
T:=\lambda_s^\star(x;\mu).
$$

For an input $\lambda$, define

$$
\lambda^+
=\lambda+\alpha\nabla_\lambda d_s(x,\lambda;\mu),
\qquad
\alpha=\theta_\lambda\frac{\rho s}{\rho+s}.
$$

Then

$$
d_s(x,\lambda^+;\mu)
-d_s(x,\lambda;\mu)
\ge
\alpha\left(1-\frac{\theta_\lambda}{2}\right)
\|\nabla_\lambda d_s(x,\lambda;\mu)\|^2,
$$

and

$$
\|\lambda^+-T\|
\le
\chi_s\|\lambda-T\|,
$$

where

$$
\chi_s
:=1-\theta_\lambda\frac\rho{\rho+s}
\in(0,1).
$$

#### Proof

Apply the smoothness inequality to the convex function
$-d_s(x,\cdot;\mu)$. Since

$$
\alpha L_{\lambda,s}\le\theta_\lambda,
$$

the standard gradient-descent estimate for $-d_s$ yields the ascent
inequality.

For the contraction, let

$$
Q_x(\lambda):=q(\lambda;x).
$$

The optimality condition for $T$ is

$$
0
=\frac{Q_x(T)-T}{\rho}-\frac{T-\mu}{s}.
$$

Using this identity and the convex-combination form from Lemma 3 gives

$$
\lambda^+-T
=(1-\theta_\lambda)(\lambda-T)
+\theta_\lambda\frac{s}{\rho+s}
\left[Q_x(\lambda)-Q_x(T)\right].
$$

Lemma 2 gives

$$
\|Q_x(\lambda)-Q_x(T)\|
\le\|\lambda-T\|.
$$

The triangle inequality therefore gives

$$
\begin{split}
\|\lambda^+-T\|
&\le
\left[
1-\theta_\lambda
+\theta_\lambda\frac{s}{\rho+s}
\right]
\|\lambda-T\| \\
&=
\left[1-\theta_\lambda\frac\rho{\rho+s}\right]
\|\lambda-T\|.
\end{split}
$$

This proves the lemma.

### Lemma 5. Exact target representation and sensitivity

For every $x,\mu$ and $s>0$, the exact target exists uniquely. It satisfies

$$
\lambda_s^\star(x;\mu)
=\mu+s r_s^\star(x;\mu),
$$

$$
q_s^\star(x;\mu)
=\mu+(\rho+s)r_s^\star(x;\mu)
\in\partial h(y_s^\star(x;\mu)).
$$

Equivalently,

$$
y_s^\star(x;\mu)
=\operatorname{prox}_{h/(\rho+s)}
\left(A(x)+\frac\mu{\rho+s}\right).
$$

This last formula describes the exact theoretical target. It is not an
algorithmic proximal evaluation.

Under the multiplier bound $\|\mu\|\le M$,

$$
\|\lambda_s^\star(x;\mu)\|\le M,
$$

and

$$
\|r_s^\star(x;\mu)\|
\le\frac{L_h+M}{\rho+s}.
$$

The target satisfies

$$
\|\lambda_s^\star(x;\mu)
-\lambda_s^\star(x';\mu)\|
\le sG_A\|x-x'\|,
$$

$$
\|\lambda_s^\star(x;\mu)
-\lambda_s^\star(x;\mu')\|
\le\|\mu-\mu'\|.
$$

If $s'\ge s$ and both centers are bounded by $M$, then

$$
\|\lambda_{s'}^\star(x;\mu)
-\lambda_s^\star(x;\mu)\|
\le
2M\frac{s'-s}{s}.
$$

#### Proof

Strong concavity from Lemma 1 gives existence and uniqueness once existence
is established. Anti-coercivity follows from

$$
d_s(x,\lambda;\mu)
\le P_s(x,A(x),\lambda;\mu)
=F(x)-\frac{1}{2s}\|\lambda-\mu\|^2.
$$

The first-order condition is

$$
r_s^\star(x;\mu)
-\frac{\lambda_s^\star(x;\mu)-\mu}{s}
=0.
$$

Combining it with Lemma 2 proves the first two identities. Eliminating
$\lambda_s^\star$ from the proximal optimality condition gives the displayed
$(\rho+s)$-prox representation.

Let $q_s^\star:=q(\lambda_s^\star;x)$. Since

$$
\lambda_s^\star
=\frac\rho{\rho+s}\mu
+\frac{s}{\rho+s}q_s^\star,
$$

and $\|q_s^\star\|\le L_h\le M$, the target multiplier is bounded by $M$.
Moreover,

$$
r_s^\star
=\frac{q_s^\star-\mu}{\rho+s},
$$

which proves the residual bound.

For the sensitivity estimates, define

$$
H_{s,x,\mu}(v)
:=-\nabla_\lambda d_s(x,v;\mu).
$$

This operator is $1/s$-strongly monotone. Its unique zero is
$\lambda_s^\star(x;\mu)$. Perturbing $x$ while keeping $(s,\mu)$ fixed and
using Lemma 2 gives

$$
\frac1s
\|\lambda_s^\star(x;\mu)-\lambda_s^\star(x';\mu)\|
\le G_A\|x-x'\|.
$$

Perturbing $\mu$ changes $H$ by $(\mu-\mu')/s$, which gives the unit
Lipschitz bound in $\mu$.

For the $s$ perturbation, let

$$
u:=\lambda_s^\star(x;\mu),
\qquad
u':=\lambda_{s'}^\star(x;\mu).
$$

Strong monotonicity at scale $1/s$ and the two zero equations give

$$
\frac1s\|u-u'\|
\le
\left|\frac1s-\frac1{s'}\right|
\|u'-\mu\|.
$$

The multiplier bounds imply $\|u'-\mu\|\le2M$. Multiplication by $s$ proves
the stated estimate.

### Lemma 6. Exact-value smoothness and primal quasi-descent

The exact value has the representation

$$
\psi_s(x;\mu)
=f(x)+\min_y
\left\{
h(y)+\langle\mu,A(x)-y\rangle
+\frac{\rho+s}{2}\|A(x)-y\|^2
\right\},
$$

and

$$
\nabla_x\psi_s(x;\mu)
=\nabla f(x)+J_A(x)^\top q_s^\star(x;\mu).
$$

On the stated global domain, its gradient is Lipschitz with

$$
L_{\psi,s}
\le
L_f+L_A L_h+(\rho+s)G_A^2.
$$

Suppose $\eta_kL_{\psi,s_k}\le1/2$. Then the algorithm satisfies

$$
\begin{split}
&\psi_{s_k}(x^{k+1};\mu^k)
-\psi_{s_k}(x^k;\mu^k) \\
&\quad\le
-\frac{1}{2\eta_k}\|x^{k+1}-x^k\|^2
+\eta_kG_A^2\|e_k\|^2.
\end{split}
$$

#### Proof

The exact target from Lemma 5 is the unique saddle point of
$P_s(x,\cdot,\cdot;\mu)$. Maximizing first in $\lambda$ gives the displayed
direct representation of $\psi_s$. Danskin's theorem applies because the
target is unique, and gives the gradient formula.

The map

$$
q_s^\star(x;\mu)
=(\rho+s)
\left[I-\operatorname{prox}_{h/(\rho+s)}\right]
\left(A(x)+\frac\mu{\rho+s}\right)
$$

is $(\rho+s)G_A$-Lipschitz in $x$. Combining this with the smoothness of
$f,A$, the bound $\|q_s^\star\|\le L_h$, and $\|J_A\|\le G_A$ gives the
claimed $L_{\psi,s}$.

Let

$$
\Delta x^{k+1}:=x^{k+1}-x^k.
$$

The algorithmic primal gradient is

$$
g_x^k
:=\nabla f(x^k)+J_A(x^k)^\top q^k,
$$

and

$$
\Delta x^{k+1}=-\eta_k g_x^k.
$$

Lemma 2 gives

$$
\|q^k-q_{s_k}^\star(x^k;\mu^k)\|
\le\|e_k\|.
$$

The descent lemma for $\psi_{s_k}$ therefore gives

$$
\begin{split}
&\psi_{s_k}(x^{k+1};\mu^k)
-\psi_{s_k}(x^k;\mu^k) \\
&\quad\le
-\frac1{\eta_k}\|\Delta x^{k+1}\|^2
+\frac{L_{\psi,s_k}}2\|\Delta x^{k+1}\|^2 \\
&\qquad+
G_A\|e_k\|\|\Delta x^{k+1}\|.
\end{split}
$$

The stepsize condition and Young's inequality imply

$$
G_A\|e_k\|\|\Delta x^{k+1}\|
\le
\frac1{4\eta_k}\|\Delta x^{k+1}\|^2
+\eta_kG_A^2\|e_k\|^2.
$$

Combining the last two displays proves the result.

### Lemma 7. Tracking and center-gap recursions

Define the post-primal target

$$
\widehat\lambda_{k+1}^\star
:=\lambda_{s_k}^\star(x^{k+1};\mu^k),
$$

and the post-ascent error before moving the center and $s$:

$$
\bar e_{k+1}
:=\lambda^{k+1}-\widehat\lambda_{k+1}^\star.
$$

Then

$$
\|\bar e_{k+1}\|
\le
\chi_{s_k}
\left[
\|e_k\|+s_kG_A\|\Delta x^{k+1}\|
\right],
$$

where

$$
\chi_{s_k}
=1-\theta_\lambda\frac\rho{\rho+s_k}.
$$

The full moving-target error satisfies

$$
\begin{split}
\|e_{k+1}\|
&\le
\|\bar e_{k+1}\|
+\|\mu^{k+1}-\mu^k\| \\
&\quad+
2M\frac{s_{k+1}-s_k}{s_k}.
\end{split}
$$

The center gap obeys the exact identity

$$
d_{k+1}
=(1-\omega_k)
\left[d_k+\alpha_k g_\lambda^k\right].
$$

For fixed $\omega_k=\theta_\mu$, this implies

$$
\begin{split}
\|d_{k+1}\|^2-\|d_k\|^2
&\le
-\theta_\mu\|d_k\|^2 \\
&\quad+
\frac{(1-\theta_\mu)^2}{\theta_\mu}
\alpha_k^2\|g_\lambda^k\|^2.
\end{split}
$$

#### Proof

Lemma 4 applied at $(s_k,x^{k+1},\mu^k)$ gives

$$
\|\bar e_{k+1}\|
\le
\chi_{s_k}
\|\lambda^k-\widehat\lambda_{k+1}^\star\|.
$$

Add and subtract $\lambda_{s_k}^\star(x^k;\mu^k)$, and apply the
$x$-sensitivity bound from Lemma 5. This proves the first recursion.

Next, add and subtract
$\lambda_{s_k}^\star(x^{k+1};\mu^{k+1})$ in the definition of $e_{k+1}$.
The $\mu$- and $s$-sensitivity bounds in Lemma 5 prove the second recursion.

Finally,

$$
\begin{split}
d_{k+1}
&=\lambda^{k+1}-\mu^{k+1} \\
&=(1-\omega_k)(\lambda^{k+1}-\mu^k) \\
&=(1-\omega_k)
\left[d_k+\lambda^{k+1}-\lambda^k\right].
\end{split}
$$

Use $\lambda^{k+1}-\lambda^k=\alpha_k g_\lambda^k$. For fixed
$\theta_\mu$, the weighted Young inequality

$$
\|u+v\|^2
\le
\frac1{1-\theta_\mu}\|u\|^2
+\frac1{\theta_\mu}\|v\|^2
$$

gives the stated squared recursion.

### Proposition 1. Conditional split-KKT complexity

Assume that the missing coupled Lyapunov argument establishes the master
budget

$$
B
:=\sum_{k=0}^\infty
\left[
s_k\|\Delta x^{k+1}\|^2
+\|g_\lambda^k\|^2
\right]
<\infty.
$$

Then, for every integer $K\ge4$, there exists

$$
\kappa\in
\{\lceil K/2\rceil,\ldots,K-1\}
$$

such that

$$
q^\kappa\in\partial h(y(\lambda^\kappa;x^\kappa)),
$$

$$
\|\nabla f(x^\kappa)+J_A(x^\kappa)^\top q^\kappa\|
=O\left(K^{-(1-a)/2}\right),
$$

and

$$
\|A(x^\kappa)-y(\lambda^\kappa;x^\kappa)\|
=O\left(K^{-a}+K^{-1/2}
+K^{-(1+a)/2}\right).
$$

Consequently, $a=1/3$ yields an $O(K^{-1/3})$ split-KKT residual and a
conditional $O(\epsilon^{-3})$ iteration complexity bound.

#### Proof

Let

$$
I_K:=\{\lceil K/2\rceil,\ldots,K-1\}.
$$

Choose $\kappa\in I_K$ minimizing

$$
s_k\|\Delta x^{k+1}\|^2+\|g_\lambda^k\|^2.
$$

Since $|I_K|\ge K/4$,

$$
s_\kappa\|\Delta x^{\kappa+1}\|^2
+\|g_\lambda^\kappa\|^2
\le\frac{4B}{K}.
$$

The primal update gives

$$
\nabla f(x^\kappa)+J_A(x^\kappa)^\top q^\kappa
=-\frac1{\eta_\kappa}\Delta x^{\kappa+1}.
$$

Because $s_\kappa=\Theta(K^a)$ and
$1/\eta_\kappa=\Theta(s_\kappa)$ on the tail,

$$
\frac1{\eta_\kappa}\|\Delta x^{\kappa+1}\|
=O\left(\sqrt{\frac{s_\kappa}{K}}\right)
=O\left(K^{-(1-a)/2}\right).
$$

Lemma 2 gives the exact subgradient relation.

For feasibility, define the current-point dual gradient

$$
\widetilde g_\lambda^k
:=\nabla_\lambda d_{s_k}(x^k,\lambda^k;\mu^k).
$$

Lemma 2 gives

$$
\|\widetilde g_\lambda^k-g_\lambda^k\|
\le G_A\|\Delta x^{k+1}\|.
$$

The reduced-dual gradient identity gives

$$
r^k
=\widetilde g_\lambda^k+\frac{d_k}{s_k}.
$$

Lemma 3 implies $\|d_k\|\le2M$. Hence

$$
\|r^\kappa\|
\le
\|g_\lambda^\kappa\|
+G_A\|\Delta x^{\kappa+1}\|
+\frac{2M}{s_\kappa}.
$$

The three terms are respectively

$$
O(K^{-1/2}),
\qquad
O(K^{-(1+a)/2}),
\qquad
O(K^{-a}).
$$

This proves the residual estimates. Balancing

$$
a=\frac{1-a}{2}
$$

gives $a=1/3$ and the conditional complexity claim.

### Proposition 2. The remaining coupled Lyapunov obligation

To turn Proposition 1 into an unconditional theorem, it is sufficient to
construct a nonnegative tracking functional $\mathcal T_k$, with a lower
bound independent of the horizon, such that

$$
\begin{split}
&\psi_{s_{k+1}}(x^{k+1};\mu^{k+1})
+\mathcal T_{k+1} \\
&\quad-
\psi_{s_k}(x^k;\mu^k)
-\mathcal T_k \\
&\le
-c_xs_k\|\Delta x^{k+1}\|^2
-c_\lambda\|g_\lambda^k\|^2
+\xi_k,
\end{split}
$$

where $c_x,c_\lambda>0$ are independent of $k$ and

$$
\sum_{k=0}^\infty\xi_k<\infty.
$$

The natural candidate is a coupled function of the exact-target error and
center gap,

$$
\mathcal T_k
=a_k\|e_k\|^2+b_k\|d_k\|^2
+2c_k\langle e_k,d_k\rangle,
$$

with a positive-semidefinite coefficient matrix. A diagonal tracking energy
based only on $\|e_k\|^2$ is insufficient under the estimates currently
available.

#### Reason for the obstruction

For large $s_k$,

$$
1-\chi_{s_k}=\Theta(s_k^{-1}),
$$

while Lemma 5 permits exact-target motion of size

$$
\|\widehat\lambda_{k+1}^\star
-\lambda_{s_k}^\star(x^k;\mu^k)\|
=O\left(s_k\|\Delta x^{k+1}\|\right).
$$

Squaring the first recursion in Lemma 7 with the Young parameter required to
preserve contraction gives an estimate of the form

$$
\|\bar e_{k+1}\|^2
\le
\left(1-\frac{c}{s_k}\right)\|e_k\|^2
+Cs_k^3\|\Delta x^{k+1}\|^2.
$$

On the other hand, Lemma 6 supplies primal descent only at the scales

$$
-\Theta(s_k)\|\Delta x^{k+1}\|^2
+\Theta(s_k^{-1})\|e_k\|^2.
$$

If a scalar weight $w_k\|e_k\|^2$ is used, absorbing the primal tracking
error requires $w_k=\Omega(1)$, while absorbing the target-motion term
requires $w_k=O(s_k^{-2})$. These requirements conflict as
$s_k\to\infty$.

The center-gap recursion in Lemma 7 contributes a useful negative
$-\theta_\mu\|d_k\|^2$ term. Completing the proof therefore requires a
cross-term argument showing that this negative center-gap term cancels the
$s_k^3\|\Delta x^{k+1}\|^2$ loss before separate triangle and Young
inequalities destroy the correlation. No such estimate has yet been derived
from Assumptions 1--5.

This is exactly the mathematical form of the Hu--Jiang question: whether a
moving center can remove the multiplier drift from primal descent while
retaining a single loop.

### Lemma 8. Scalar stability check

For the degenerate test problem

$$
h\equiv0,
\qquad
A\equiv0,
$$

the main dual and center updates are linearly stable for every fixed $s>0$.

#### Proof

Here

$$
y(\lambda;x)=\frac\lambda\rho,
\qquad
q(\lambda;x)=0.
$$

Let

$$
b_s:=\frac\rho{\rho+s}.
$$

The updates reduce to

$$
\lambda^+
=(1-\theta_\lambda)\lambda
+\theta_\lambda b_s\mu,
$$

$$
\mu^+
=(1-\theta_\mu)\mu+\theta_\mu\lambda^+.
$$

Thus

$$
\begin{bmatrix}
\lambda^+\\
\mu^+
\end{bmatrix}
=
\begin{bmatrix}
1-\theta_\lambda & \theta_\lambda b_s\\
\theta_\mu(1-\theta_\lambda)
&1-\theta_\mu+\theta_\mu\theta_\lambda b_s
\end{bmatrix}
\begin{bmatrix}
\lambda\\
\mu
\end{bmatrix}.
$$

The matrix is nonnegative. Its row sums are

$$
1-\theta_\lambda(1-b_s)<1,
$$

and

$$
1-\theta_\mu\theta_\lambda(1-b_s)<1.
$$

Hence its spectral radius is strictly below one. This verifies stability of
the main parameter choice in the required degenerate case. It does not prove
the moving-target Lyapunov estimate in Proposition 2.

## Corrections or Missing Assumptions

The $O(\epsilon^{-3})$ target theorem would become provable if any one of the
following were established.

1. The coupled tracking inequality in Proposition 2 under Assumptions 1--5.
2. A uniform error-bound or PL-type condition for the reduced-dual block that
   replaces the $1/s_k$ contraction scale by a positive constant.
3. A stronger structural assumption on $h$ or $A$ that reduces the
   $O(s_k\|\Delta x\|)$ exact-target sensitivity.

No such condition is silently added in this package.

## Open Risks

1. The fixed $\omega_k=\theta_\mu$ rule keeps the center on the same time
   scale as the multiplier, but its center drift is not summable by itself.
2. The normalized 2P-ADMM-inspired rule makes center drift summable, but may
   weaken center-gap contraction too much to remove the tracking bottleneck.
3. An ARADMM-style residual cap bounds multiplier increments, but a cap that
   decays too quickly can prevent sufficient accumulated dual progress.
4. The displayed algorithm evaluates $y(\lambda^k;x^k)$ and
   $y(\lambda^k;x^{k+1})$. Thus it uses two $\rho$-proximal evaluations per
   iteration, although it has no inner loop.

## Parameter-Design Sources

The adaptive mechanisms above are inspired by the local notes
`2025_nips.md` and `ADMM/full_副本.md`. Their update orders and theorem
assumptions are not imported into this proof. Only the ideas of separating the
dual stepsize from the growing regularization scale, bounding multiplier
increments, and normalizing moving-center drift are used.
