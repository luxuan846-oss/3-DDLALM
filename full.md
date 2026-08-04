# Complexity of Proximal Augmented Lagrangian for Nonconvex Optimization with Nonlinear Equality Constraints

Yue Xie1 $\textcircled{1}$ ·   2

Received: 11 October 2019 / Revised: 1 September 2020 / Accepted: 15 January 2021 / Published online: 2 February 2021 $\circledcirc$ The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature 2021

# Abstract

We analyze worst-case complexity of a Proximal augmented Lagrangian (Proximal AL) framework for nonconvex optimization with nonlinear equality constraints. When an approximate first-order (second-order) optimal point is obtained in the subproblem, an $\epsilon$ first-order (second-order) optimal point for the original problem can be guaranteed within $\mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ outer iterations (where $\eta$ is a user-defined parameter with $\eta \in [ 0 , 2 ]$ for the first-order result and $\eta \in [ 1 , 2 ]$ for the second-order result) when the proximal term coefficient $\beta$ and penalty parameter $\rho$ satisfy $\beta = \mathcal { O } ( \epsilon ^ { \eta } )$ and $\rho = \varOmega ( 1 / \epsilon ^ { \eta } )$ , respectively. We also investigate the total iteration complexity and operation complexity when a Newton-conjugate-gradient algorithm is used to solve the subproblems. Finally, we discuss an adaptive scheme for determining a value of the parameter $\rho$ that satisfies the requirements of the analysis.

Keywords Optimization with nonlinear equality constraints $\cdot$ Nonconvex optimization $\cdot$ Proximal augmented Lagrangian $\cdot$ Complexity analysis $\cdot$ Newton-conjugate-gradient

Mathematics Subject Classification 68Q25 · 90C06 $\cdot$ 90C26 · 90C30 · 90C60

# 1 Introduction

Nonconvex optimization problems with nonlinear equality constraints are common in some areas, including matrix optimization and machine learning, where such requirements as normalization, orthogonality, or consensus must be satisfied. Relevant problems include dictionary learning [34], distributed optimization [26], and spherical PCA [28]. We consider

the formulation

$$
\operatorname* { m i n } { f ( x ) } \mathrm { s u b j e c t { t o } } c ( x ) = 0 ,
$$

where $f : \mathbb { R } ^ { n } \to \mathbb { R }$ , ${ \boldsymbol { c } } ( { \boldsymbol { x } } ) \triangleq ( c _ { 1 } ( { \boldsymbol { x } } ) , \dots , c _ { m } ( { \boldsymbol { x } } ) ) ^ { T }$ , ${ c _ { i } } : { \mathbb { R } } ^ { n }  { \mathbb { R } } , i = 1 , 2 , \ldots , m$ , and all functions are twice continuously differentiable.

We have the following definitions related to points that satisfy approximate first- and second-order optimality coniditions for (1). (Here and throughout, $\| \cdot \|$ denotes the Euclidean norm of a vector.)

Definition 1 $\epsilon$ -1o) We say that $x$ is an $\epsilon$ -1o solution of (1) if there exists $\lambda \in \mathbb { R } ^ { m }$ such that

$$
\| \nabla f ( x ) + \nabla c ( x ) \lambda \| \leq \epsilon , \quad \| c ( x ) \| \leq \epsilon .
$$

Definition 2 $\epsilon$ -2o) We say that $x$ is an $\epsilon$ -2o solution of (1) if there exists $\lambda \in \mathbb { R } ^ { m }$ such that:

$$
\begin{array} { l } { \| \nabla f ( x ) + \nabla c ( x ) \lambda \| \leq \epsilon , \quad \| c ( x ) \| \leq \epsilon , } \\ { \displaystyle d ^ { T } \left( \nabla ^ { 2 } f ( x ) + \displaystyle \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla ^ { 2 } c _ { i } ( x ) \right) d \geq - \epsilon \| d \| ^ { 2 } , } \end{array}
$$

for any $\begin{array} { r } { d \in S ( x ) \triangleq \{ d \in \mathbb { R } ^ { n } \ | \ \nabla c ( x ) ^ { T } d = 0 \} . } \end{array}$

These definitions are consistent with those of $\epsilon$ -KKT and $\epsilon$ -KKT2 in [11], and similar to those of [23], differing only in choice of norm and use of $\| c ( x ) \| \leq \epsilon$ rather than $c ( x ) = 0$ . The following theorem is implied by several results in [4,11], which consider a larger class of problem than (1). (A proof tailored to (1) is supplied in the “Appendix”.)

Theorem 1 If $x ^ { * }$ is an local minimizer of (1), then there exists $\epsilon _ { k } \to 0 ^ { + }$ and $x _ { k } \to x ^ { * }$ such that $x _ { k }$ is $\epsilon _ { k } { - } 2 o$ , thus $\epsilon _ { k } – I o$ .

Theorem 1 states that being the limit of a sequence of points satisfying Definitions 1 or 2 for a decreasing sequence of $\epsilon$ is a necessary condition of a local minimizer. When certain constraint qualifications hold, a converse of this result is also true: $x ^ { * }$ satisfies firstorder (KKT) conditions when $x _ { k }$ is $\epsilon _ { k }$ -1o and second-order conditions when $x _ { k }$ is $\epsilon _ { k } { - } 2 0$ (See [4,5]). These observations justify our strategy of seeking points that satisfy Definitions 1 or 2.

The augmented Lagrangian (AL) framework is a penalty-type algorithm for solving (1), originating with Hestenes [25] and Powell [31]. Rockafellar proposed in [32] the proximal version of this method, which has both theoretical and practical advantages. The monograph [7] summarizes development of this method during the 1970s, when it was known as the “method of multipliers”. Interest in the algorithm has resurfaced in recent years because of its connection to ADMM [13].

The augmented Lagrangian of (1) is defined as:

$$
\mathcal { L } _ { \rho } ( x , \lambda ) \triangleq f ( x ) + \sum _ { i = 1 } ^ { m } \lambda _ { i } c _ { i } ( x ) + \frac { \rho } { 2 } \sum _ { i = 1 } ^ { m } \vert c _ { i } ( x ) \vert ^ { 2 } = f ( x ) + \lambda ^ { T } c ( x ) + \frac { \rho } { 2 } \| c ( x ) \| ^ { 2 } ,
$$

where $\lambda \triangleq ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { T } .$ . The (ordinary) Lagrangian of (1) is $\mathcal { L } _ { 0 } ( x , \lambda )$ .

# 1.1 Complexity Measures

In this paper, we discuss measures of worst-case complexity for finding points that satisfy Definitions 1 and 2. Since our method has two nested loops — an outer loop for the Proximal AL procedure, and an inner loop for solving the subproblems — we consider the following measures of complexity.

– Outer iteration complexity, which corresponds to the number of outer-loop iterations of Proximal AL or some other framework;   
– Total iteration complexity, which measures the total number of iterations of the innerloop procedure that is required to find points satisfying approximate optimality of the subproblems;   
Operation complexity, which measures the number of some unit operation (in our case, computation of a matrix-vector product involving the Hessian of the Proximal augmented Lagrangian) required to find approximately optimal points.

We also use the term “total iteration complexity” in connection with algorithms that have only one main loop, such as those whose complexities are shown in Table 1.

We prove results for all three types of complexity for the Proximal AL procedure, where the inner-loop procedure is a Newton-conjugate-gradient (Newton-CG) algorithm for the unconstrained nonconvex subproblems. Details are given in Sect. 1.3.

# Algorithm 1 Augmented Lagrangian (AL)

0. Initialize $x _ { 0 }$ , $\lambda _ { 0 }$ and $\rho _ { 0 } > 0$ , $\varLambda \triangleq [ A _ { \mathrm { m i n } }$ , $\varLambda _ { \mathrm { m a x } } ]$ , $\tau \in ( 0 , 1 )$ , $\gamma > 1$ ; Set $k \gets 0$ ;   
1. Update $x _ { k }$ : Find approximate solution $x _ { k + 1 }$ to $\operatorname* { m i n } _ { x }$ $\mathcal { L } _ { \rho _ { k } } ( x , \lambda _ { k } )$ ;   
2. Update $\lambda _ { k } \colon \lambda _ { k + 1 } \gets P _ { \lambda } ( \lambda _ { k } + \rho _ { k } c ( x _ { k + 1 } ) )$ ;   
3. Update $\rho _ { k }$ : if $k = 0$ or $\| c ( x _ { k + 1 } ) \| _ { \infty } \leq \tau \| c ( x _ { k } ) \| _ { \infty }$ , set $\rho _ { k + 1 } = \rho _ { k }$ ; otherwise, set $\rho _ { k + 1 } = \gamma \rho _ { k }$ ;   
4. If termination criterion is satisfied, STOP; otherwise, $k \gets k + 1$ and return to Step 1.

# 1.2 Related Work

AL for nonconvex optimization. We consider first the basic augmented Lagrangian framework outlined in Algorithm 1. When $f$ is a nonconvex function, convergence of the augmented Lagrangian framework has been studied in [9,11], with many variants described in [1–3,6,19]. In [11], Algorithm 1 is investigated and generalized for a larger class of problems, showing in particular that if $x _ { k + 1 }$ is a first-order (second-order) approximate solution of the subproblem, with error driven to 0 as $k  \infty$ , then every feasible limit point is an approximate firstorder (second-order) KKT point of the original problem. In [9], it is shown that when the subproblem in Algorithm 1 is solved to approximate global optimality with error approaching 0, the limit point is feasible and is a global solution of the original problem.

There are few results in the literature on outer iteration complexity in the nonconvex setting. Some quite recent results appear in [12,22]. In [22], the authors apply a general version of augmented Lagrangian to nonconvex optimization with both equality and inequality constraints. With an aggressive updating rule for the penalty parameter, they show that the algorithm obtains an approximate KKT point (whose exact definition is complicated, but similar to our definition of $\epsilon$ -1o optimality when only equality constraints are present) within $\mathcal { O } ( \epsilon ^ { - 2 / ( \alpha - 1 ) } )$ outer-loop iterations, where $\alpha > 1$ is an algorithmic parameter. This complexity is improved to $\mathcal { O } ( | 1 0 \mathrm { g } \epsilon | )$ when boundedness of the sequence of penalty parameters is assumed. Total iteration complexity measures are obtained for the case of linear equality constraints when the subproblem is solved with a $p$ -order method ( $\mathbf { \Phi } _ { p } \geq 2 \mathbf { \varepsilon } ,$ ). In [12], the authors study an augmented Lagrangian framework named ALGENCAN to problems with equality and inequality constraints. An $\epsilon$ -accurate first-order point (whose precise definition is again similar to our $\epsilon$ -1o optimality in the case of equality constraints only) is obtained in $\mathcal { O } ( | 1 0 \mathrm { g } \epsilon | )$ outer iterations when the penalty parameters are bounded. The practicality of the assumption of bounded penalty parameters in these two works [12,22] is open to question, since the use of an increasing sequence of penalty parameters is critical to both approaches, and there is no clear prior reason why the sequence should be bounded1.

Proximal AL for nonconvex optimization: Linear equality constraints. The Proximal augmented Lagrangian framework, with fixed positive parameters $\rho$ and $\beta$ , is shown in Algorithm 2.

# Algorithm 2 Proximal augmented Lagrangian (Proximal AL)

0. Initialize $x _ { 0 }$ , $\lambda _ { 0 }$ and $\rho > 0$ , $\beta > 0$ ; Set $k \gets 0$ ;   
1. Update $x _ { k }$ : Find approximate solution $x _ { k + 1 }$ to $\operatorname* { m i n } _ { x }$ $\begin{array} { r } { \mathcal { L } _ { \rho } ( x , \lambda _ { k } ) + \frac { \beta } { 2 } \| x - x _ { k } \| ^ { 2 } } \end{array}$ ;   
2. Update $\lambda _ { k } \colon \lambda _ { k + 1 } \gets \lambda _ { k } + \rho c ( x _ { k + 1 } )$ ;   
+  +3. If termination criterion is satisfied, STOP; otherwise, $k \gets k + 1$ and return to Step 1.

For this proximal version, in the case of linear constraints $c ( \cdot )$ , outer iteration complexity results become accessible in the nonconvex regime [24,26,27,35]. The paper [26] analyzes the outer iteration complexity of this approach (there named “proximal primal dual algorithm (Prox-PDA)”) to obtain a first-order optimal point, choosing a special proximal term to make each subproblem strongly convex and suitable for distributed implementation. An outer iteration complexity estimate of $\mathcal { O } ( \epsilon ^ { - 1 } )$ is proved for an $\sqrt { \epsilon }$ -1o point. This result is consistent with our results in this paper when the choice of $\beta$ and $\rho$ is independent of $\epsilon$ and $c ( x )$ is linear.

The paper [24] proposes a “perturbed proximal primal dual algorithm,” a variant of Algorithm 2, to obtain outer iteration complexity results for a problem class where the objective function may be nonconvex and nonsmooth. In particular, an outer iteration complexity of $\mathcal { O } ( \epsilon ^ { - 2 } )$ is required to obtain $\epsilon$ -stationary solution, where the latter term is defined in a way that suits that problem class. A modified inexact Proximal AL method is investigated in [35]. Here, an exponentially weighted average of previous updates is used as the anchor point in the proximal term, total iteration complexity of $\mathcal { O } ( \epsilon ^ { - 2 } )$ to locate an $\epsilon$ stationary point similar to $\epsilon$ -1o is derived and a certain kind of linear convergence is proved for quadratic programming (QP). The paper [27] derives outer iteration complexity of $\mathcal { O } ( \epsilon ^ { - 2 } )$ for a proximal ADMM procedure to find an $\epsilon$ stationary solution defined for their problem class.

To our knowledge, outer iteration complexity of Proximal AL in the case of nonlinear $c ( x )$ and its complexity for convergence to second-order optimal points have not yet been studied.

Complexity for constrained nonconvex optimization. For constrained nonconvex optimization, worst-case total iteration complexity results of various algorithms to find $\epsilon$ -perturbed first-order and second-order optimal points have been obtained in recent years. If only firstderivative information is used, total iteration complexity to obtain an $\epsilon$ -accurate first-order optimal point may be $\mathcal { O } ( \epsilon ^ { - 2 } )$ [8,23,29]. If Hessian information is used (either explicitly or via Hessian-vector products), total iteration complexity for an $\epsilon$ -accurate first-order point can be improved to $\mathcal { O } ( \epsilon ^ { - 3 / 2 } )$ [8,23,30], while the total iteration complexity to obtain an $\epsilon$ -accurate second-order point is typically $\mathcal { O } ( \epsilon ^ { - 3 } )$ [8,23,29,30]. More details about these results can be found in Table 1.

Other approaches focus on nonlinear equality constraints and seek evaluation complexity bounds (“Evaluation complexity” refers to the number of evaluations of $f$ and $c$ and their derivatives required, and corresponds roughly to our “total iteration complexity”.) for approximate first-order optimality. An algorithm based on linear approximation of the exact penalty function for (1) is described in [14], and attains a worst-case evaluation complexity of $\mathcal { O } ( \epsilon ^ { - 5 } )$ by using only function and gradient information. Two-phase approaches, which first seek an approximately feasible point by minimizing the nonlinear least-squares objective $\| c ( x ) \| _ { 2 } ^ { 2 }$ (or equivalently $\| c ( x ) \| ,$ ), and then apply a target-chasing method to find an approximate first-order point for (1), are described in [16,17]. (See Table 1.) Extensions of these techniques to approximate second-order optimality is not straightforward; most such efforts focus on special cases such as convex constraints. A recent work that tackles the general case is [18], which again considers the two-phase approach and searches for approximate first-, second-, and third-order critical points. Specific definitions of the critical points are less interpretable; we do not show them in Table 1. They are related to scaled KKT conditions for the first order point, and to local optimality with tolerance of a function of $\epsilon$ for second and third order points.

# 1.3 Contributions

We apply the Proximal AL framework of Algorithm 2 to (1) for nonlinear constraints $c ( x )$ . Recalling Definitions 1 and 2 of approximately optimal points, we show that when approximate first-order (second-order) optimality is attained in the subproblems, the outer iteration complexity to obtain an $\epsilon$ -1o $( \epsilon - 2 0 )$ point is $\mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ if we let $\beta = \mathcal { O } ( \epsilon ^ { \eta } )$ and $\rho = \varOmega ( 1 / \epsilon ^ { \eta } )$ , where $\eta$ is a user-defined parameter with $\eta \in [ 0 , 2 ]$ for the first-order result and $\eta \in [ 1 , 2 ]$ for the second-order result. We require uniform boundedness and full rank of the constraint Jacobian on a certain bounded level set, and show that the primal and dual sequence of Proximal AL is bounded and the limit point satisfies first-order KKT conditions.

We also derive total iteration complexity of the algorithm when the Newton-CG algorithm of [33] is used to solve the subproblem at each iteration of Algorithm 2. The operation complexity for this overall procedure is also described, taking as unit operation the computation of a Hessian-vector product. When $c ( x )$ is linear and $\eta = 2$ , the total iteration complexity matches the known results in literature for second-order algorithms: $\mathcal { O } ( \epsilon ^ { - 3 / 2 } )$ for an $\epsilon$ -1o point and $\mathcal { O } ( \epsilon ^ { - 3 } )$ for an $\epsilon$ -2o point.

Finally, we present a scheme for determining the algorithmic parameter $\rho$ adaptively, by increasing it until convegence to an approximately-optimal point is identified within the expected number of iterations.

# 1.4 Organization

In Sect. 2, we list the notations and main assumptions used in the paper. We discuss outer iteration complexity of Proximal AL in Sect. 3. Total iteration complexity and operation complexity are derived in Sect. 4. A framework for determining the parameter $\rho$ in Proximal AL is proposed in Sect. 5. We summarize the paper and discuss future work in Sect. 6.

Ta ble 1 Total iteration or evaluation complexity estimates for constrained nonconvex optimization procedures   

<table><tr><td>Point type</td><td>Complexity</td><td>Constraint type</td><td>Lit.</td></tr><tr><td colspan="2">{I[XVf(x)il≤∈,if xi &lt;(1-∈/2)bi</td><td>O(ε-2) (gradient) 0≤x≤b</td><td></td><td>[8]</td></tr><tr><td colspan="2">[[Vf(x)li ≤∈，if xi ≥(1-∈/2)bi /Xνf(x)llo ≤∈,xv²f(x)X≥-√∈In</td><td>O(e-3/2) (Hessian)</td><td>x≥0</td><td>[8]</td></tr><tr><td colspan="2">Ax=b,x&gt;0,∀f(x)+ATλ≥-∈1</td><td>O(e-2) (gradient)</td><td>Ax=b,x≥0</td><td></td></tr><tr><td colspan="2">|X(Vf(x)+ATλ)lloo≤∈ [Ax=b,x&gt;0,Vf(x)+ATλ≥-∈1 X(Vf(x)+ATλ)llo≤∈</td><td></td><td></td><td>[23]</td></tr><tr><td colspan="2">dT(xv²f(x)X +√∈I)d ≥0, [∀d ∈ {d|AXd =0} [mins (Vf(x),s) ≤eg s.t.x+s∈F，lsl≤1</td><td>O(e-3/2) (Hessian)</td><td>Ax=b,x≥0</td><td></td></tr><tr><td colspan="2">minddTv² f(x)d s.t.x+d ∈F,Idl≤1, ≤H (Vf(x),d)≤0</td><td>(max1e2,³1） (Hessian)</td><td>x∈F, Fis closed and convex</td><td>[29]</td></tr><tr><td colspan="2">[x &gt;0,∀f(x)≥-∈1,IxVf(x)ll∞≤∈, xv²f（x）x≥-√∈I</td><td>(-3/2) (Hessian)</td><td>x≥0</td><td>[30]</td></tr><tr><td colspan="2">|Vf(x)+Vc(x)λ|≤∈,llc(x)I≤∈,or</td><td>O(ε-5) (gradient)</td><td>c(x)=0</td><td>[14]</td></tr><tr><td colspan="2">xis an approximate critical point ofl (x)ll |lc(x)ll≤∈p，lIVf(x)+∀c(x)λ|≤∈dl(λ,1)l</td><td>(Hessian)</td><td>c(x)=0</td><td>[16]</td></tr></table>

Ta ble 1 continued   

<table><tr><td>Point type</td><td>Complexity</td><td>Constraint type</td><td>Lit.</td></tr><tr><td>IVf(x)+Vc(x)λ|≤∈,llc(x)≤∈,or IVc(x)μl≤∈,llc(x)l≥κ∈.</td><td>O(ε-2) (gradient)</td><td>c(x)=0</td><td>[17]</td></tr><tr><td>x is eapproximate first order critical point of the constrained problem or oflc(x)ll</td><td>O(e-(p+2)/p)</td><td>c(x)=0,x ∈F Fis closed</td><td>[18]</td></tr><tr><td></td><td>(pth derivative)</td><td>and convex</td><td></td></tr><tr><td>x is eapproximateqth order critical point</td><td>O(e-2q-1)</td><td>c(x)=0,x ∈F</td><td></td></tr><tr><td>of the constrained problem or of |lc(x)l</td><td></td><td>Fis closed</td><td>[18]</td></tr><tr><td></td><td>(qth derivative)</td><td></td><td></td></tr><tr><td>q =1,2,3.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>and convex</td><td></td></tr></table>

Here $X = \mathrm { d i a g } ( x )$ and $\bar { X } = \mathrm { d i a g } ( \operatorname* { m i n } \{ x , \mathbf { 1 } \} )$ . $\tilde { \mathcal { O } }$ represents $\scriptscriptstyle \mathcal { O }$ with logarithm factors hidden. Gradient or Hes sian in parenthesis means that the algorithm uses only gradient or both gradient and Hessian information, respectively. $p$ th derivative means that the algorithm needs to evaluate function derivatives up to $p$ th order

Most proofs appear in the main body of the paper; some elementary results are proved in the “Appendix”.

# 2 Preliminaries

Notation. We use $\| \cdot \|$ to denote the Euclidean norm of a vector and $\| \cdot \| _ { 2 }$ to denote the operator 2-norm of a matrix. For a given matrix $H$ , we denote by $\sigma _ { \mathrm { m i n } } ( H )$ its minimal singular value and by $\lambda _ { \operatorname* { m i n } } ( H )$ its minimal eigenvalue. We denote steps in $x$ and $\lambda$ as follows:

$$
\Delta x _ { k + 1 } \triangleq x _ { k + 1 } - x _ { k } , \quad \Delta \lambda _ { k + 1 } \triangleq \lambda _ { k + 1 } - \lambda _ { k } .
$$

In estimating complexities, we use order notation $\mathcal { O } ( \cdot )$ in the usual sense, and $\tilde { \mathcal { O } }$ to hide factors that are logarithmic in the arguments. We use $\beta ( \alpha ) = \Omega ( \gamma ( \alpha ) )$ (where $\beta ( \alpha )$ and $\gamma ( \alpha )$ are both positive) to indicate that $\beta ( \alpha ) / \gamma ( \alpha )$ is bounded below by a positive real number for all $\alpha$ sufficiently small.

Assumptions.

The following assumptions are used throughout this work.

Assumption 1 Suppose that there exists $\rho _ { 0 } \geq 0$ such that $\begin{array} { r } { f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } } \end{array}$ has compact level sets, that is, for all $\alpha \in \mathbb { R }$ , the set

$$
S _ { \alpha } ^ { 0 } \triangleq \left\{ x \Big | f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } \leq \alpha \right\}
$$

is empty or compact.

Assumption 1 holds in any of the following cases:

1. $\begin{array} { r } { f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } } \end{array}$ is coercive for some $\rho _ { 0 } \geq 0$ .   
2. $f ( x )$ is strongly convex.   
3. $f ( x )$ is bounded below and $c ( x ) = x ^ { T } x - 1$ , as occurs in orthonormal dictionary learning applications.   
4. $\begin{array} { r } { \hat { f ( x ) } \triangleq \frac { 1 } { 2 } x ^ { T } Q x - p ^ { T } x , c ( x ) \triangleq A x - b , } \end{array}$ , $Q$ is positive definite on nul $\operatorname { l } ( A ) \triangleq \{ x \mid A x =$ $0 \}$ .

An immediate consequence of this assumption is the following, proof of which appears in the “Appendix”.

Lemma 1 Suppose that Assumption 1 holds, then $\begin{array} { r } { f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } } \end{array}$ is lower bounded.

Therefore, Assumption 1 implies

$$
\bar { L } \triangleq \operatorname* { i n f } _ { x \in \mathbb { R } ^ { n } } \left\{ f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } \right\} > - \infty .
$$

We use this definition of $\bar { L }$ throughout this paper whenever Assumption 1 holds.

The second assumption concerns certain smoothness and nondegeneracy assumptions on $f$ and $c$ over a compact set.

Assumption 2 Given a compact set $S \subseteq \mathbb { R } ^ { n }$ , there exist positive constants $M _ { f } , M _ { c } , \sigma , L _ { c }$ such that the following conditions on functions $f$ and $c$ hold.

(i) $\| \nabla f ( x ) \| \leq M _ { f }$ , $\| \nabla f ( x ) - \nabla f ( y ) \| \leq L _ { f } \| x - y \|$ , for all $x$ , $y \in S$ .   
(ii) $\| \nabla c ( x ) \| _ { 2 } \leq M _ { c }$ , $\sigma _ { \operatorname* { m i n } } ( \nabla c ( x ) ) \geq \sigma > 0$ for all $x \in S$ .   
(iii) $\| \nabla c ( x ) - \nabla c ( y ) \| _ { 2 } \leq L _ { c } \| x - y \|$ , for all $x$ , $y \in S$ .

This assumption may allow a general class of problems; in particular, (i) holds if $f ( x )$ is smooth and $\nabla f ( x )$ is locally Lipschitz continuous on a neighborhood of $s$ . (ii) holds when $c ( x )$ is smooth on a neighborhood of $s$ and satisfies an LICQ condition over $s$ , and (iii) holds if $\nabla c ( x )$ is locally Lipschitz continuous on $s$ .

Assumption 3 Suppose that $f ( x ) \leq { \bar { U } }$ for any $x \in \{ x \mid \| c ( x ) \| \leq 1 \}$ .

A sufficient condition for Assumption 3 to hold is the compactness of $\{ x \mid \| c ( x ) \| \leq 1 \}$ . This assumption is not needed if $c ( x _ { 0 } ) = 0$ , that is, the initial point is feasible.

# 3 Outer Iteration Complexity of Proximal AL

In this section, we derive the outer iteration complexity of Proximal AL (Algorithm 2) when the subproblem is solved inexactly. We assume that $x _ { k + 1 }$ in Step 1 of Algorithm 2 satisfies the following approximate first-order optimality condition:

$$
\begin{array} { r } { \nabla _ { x } \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) + \beta ( x _ { k + 1 } - x _ { k } ) = \tilde { r } _ { k + 1 } , \quad \mathrm { f o r ~ a l l } \ k \geq 0 , } \end{array}
$$

where $\tilde { r } _ { k + 1 }$ is some error vector. We additionally assume that

$$
\mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) + \frac { \beta } { 2 } \| x _ { k + 1 } - x _ { k } \| ^ { 2 } \leq \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) , \mathrm { ~ f o r ~ a l l } \ k \geq 0 .
$$

This condition can be achieved if we choose $x _ { k }$ as the initial point of the subproblem in Step 1 of Algorithm 2, with subsequent iterates decreasing the objective of this subproblem. To analyze convergence, we use a Lyapunov function defined as follows for any $k \geq 1$ , inspired by [26]:

$$
P _ { k } \triangleq \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) + \frac { \beta } { 4 } \| x _ { k } - x _ { k - 1 } \| ^ { 2 } .
$$

For any $k \geq 1$ , we have that

$$
\begin{array} { r l } { P _ { k + 1 } - P _ { k } = \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k + 1 } ) - \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) + \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } - \frac { \beta } { 4 } \| \varDelta x _ { k } \| ^ { 2 } } \\ { = } & { C _ { j } ( x _ { k } ) + \lambda _ { k + 1 } ) - \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) + \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) - \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) } \\ { + \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } - \frac { \beta } { 4 } \| \varDelta x _ { k } \| ^ { 2 } } \\ { = } & { ( \delta _ { k + 1 } - \lambda _ { k } ) ^ { \gamma } C _ { \tau ( x _ { k + 1 } ) } + \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) - \mathcal { L } _ { \rho } ( x _ { 1 } , \lambda _ { k } ) } \\ { + \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } - \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } } \\ { = } & { \frac { 1 } { \rho } \| \varDelta \lambda _ { k + 1 } \| ^ { 2 } + \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) - \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) + \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } - \frac { \beta } { 4 } \| \varDelta x _ { k } \| ^ { 2 } } \\  \overset { ( 2 ) } { \leq } \frac { 1 } { \rho } \| \varDelta x _ { k + 1 } \| ^ { 2 } - \frac { \beta } { 4 } \| \varDelta x _ { k + 1 } \| ^ { 2 } + \frac  \end{array}
$$

where the fourth equality holds because of Step 2 in Algorithm 2. We start with a technical result on bounding $\| \varDelta \lambda _ { k + 1 } \| ^ { 2 } = \| \lambda _ { k + 1 } - \lambda _ { k } \| ^ { 2 }$ .

Lemma 2 (Bound for $\| \lambda _ { k + 1 } - \lambda _ { k } \| ^ { 2 } )$ Consider Algorithm 2 with (6) and (7). Suppose that for a fixed $k \geq 1$ , Assumption 2 holds for some set $s$ and that $\mathfrak { r } _ { k } , \mathfrak { x } _ { k + 1 } \in S$ . Then,

$$
\| \lambda _ { k + 1 } - \lambda _ { k } \| ^ { 2 } \leq C _ { 1 } \| \varDelta x _ { k + 1 } \| ^ { 2 } + C _ { 2 } \| \varDelta x _ { k } \| ^ { 2 } + \frac { 1 6 M _ { c } ^ { 2 } } { \sigma ^ { 4 } } \| \tilde { r } _ { k } \| ^ { 2 } + \frac { 4 } { \sigma ^ { 2 } } \| \tilde { r } _ { k + 1 } - \tilde { r } _ { k } \| ^ { 2 } ,
$$

where $C _ { 1 }$ and $C _ { 2 }$ are defined by

$$
C _ { 1 } \triangleq \frac { 4 } { \sigma ^ { 2 } } \left( L _ { f } + \frac { L _ { c } M _ { f } } { \sigma } + \beta \right) ^ { 2 } , C _ { 2 } \triangleq \frac { 4 } { \sigma ^ { 2 } } \left( \beta + \frac { 2 M _ { c } \beta } { \sigma } \right) ^ { 2 } .
$$

Proof The first-order optimality condition (6) for Step 1 implies that for all $t \geq 0$ , we have

$$
\begin{array} { r l } & { \nabla f ( x _ { t + 1 } ) + \nabla c ( x _ { t + 1 } ) \lambda _ { t } + \rho \nabla c ( x _ { t + 1 } ) c ( x _ { t + 1 } ) + \beta ( x _ { t + 1 } - x _ { t } ) = \tilde { r } _ { t + 1 } . } \\ & { \qquad \Longrightarrow \nabla f ( x _ { t + 1 } ) + \nabla c ( x _ { t + 1 } ) \lambda _ { t + 1 } + \beta ( x _ { t + 1 } - x _ { t } ) = \tilde { r } _ { t + 1 } . } \end{array}
$$

Likewise, by replacing $t$ with $t - 1$ , for $t \geq 1$ , we obtain

$$
\nabla f ( x _ { t } ) + \nabla c ( x _ { t } ) \lambda _ { t } + \beta ( x _ { t } - x _ { t - 1 } ) = \tilde { r } _ { t } .
$$

By combining (12) and (13) and using the notation (3) along with $\Delta \tilde { r } _ { t + 1 } \triangleq \tilde { r } _ { t + 1 } - \tilde { r } _ { t }$ , we have for any $t \geq 1$ that

$$
\begin{array} { r l } & { \nabla f ( x _ { t + 1 } ) - \nabla f ( x _ { t } ) + \nabla c ( x _ { t + 1 } ) \varDelta \lambda _ { t + 1 } } \\ & { \qquad + ( \nabla c ( x _ { t + 1 } ) - \nabla c ( x _ { t } ) ) \lambda _ { t } + \beta ( \varDelta x _ { t + 1 } - \varDelta x _ { t } ) = \varDelta \tilde { r } _ { t + 1 } , } \end{array}
$$

which by rearrangement gives

$$
\begin{array} { r l } & { - \nabla c ( x _ { t + 1 } ) \varDelta \lambda _ { t + 1 } = \nabla f ( x _ { t + 1 } ) - \nabla f ( x _ { t } ) + ( \nabla c ( x _ { t + 1 } ) - \nabla c ( x _ { t } ) ) \lambda _ { t } } \\ & { \qquad + \beta ( \varDelta x _ { t + 1 } - \varDelta x _ { t } ) - \varDelta \tilde { r } _ { t + 1 } . } \end{array}
$$

For the given $k \geq 1$ , since $\sigma$ is a lower bound on the smallest singular value of $\nabla c ( x _ { k + 1 } )$ by Assumption 2, we have that

$$
\begin{array} { r l } & { \| \varDelta \lambda _ { k + 1 } \| \leq \displaystyle \frac { 1 } { \sigma } \Big ( \| \nabla f ( x _ { k + 1 } ) - \nabla f ( x _ { k } ) \| + \| \nabla c ( x _ { k + 1 } ) - \nabla c ( x _ { k } ) \| \| \lambda _ { k } \| } \\ & { \qquad + \beta ( \| \varDelta x _ { k + 1 } \| + \| \varDelta x _ { k } \| ) + \| \varDelta \tilde { r } _ { k + 1 } \| \Big ) . } \end{array}
$$

We have from (13) that

$$
\nabla c ( x _ { k } ) \lambda _ { k } = - \nabla f ( x _ { k } ) - \beta ( x _ { k } - x _ { k - 1 } ) + \tilde { r } _ { k } ,
$$

so that

$$
\| \lambda _ { k } \| \leq { \frac { 1 } { \sigma } } \left( \| \nabla f ( x _ { k } ) \| + \beta \| \varDelta x _ { k } \| + \| \tilde { r } _ { k } \| \right) \leq { \frac { 1 } { \sigma } } \left( M _ { f } + \beta \| \varDelta x _ { k } \| + \| \tilde { r } _ { k } \| \right) .
$$

We also have from Assumption 2 that

$$
\| \nabla c ( x _ { k + 1 } ) - \nabla c ( x _ { k } ) \| \leq L _ { c } \| x _ { k + 1 } - x _ { k } \| , \quad \| \nabla c ( x _ { k + 1 } ) - \nabla c ( x _ { k } ) \| \leq 2 M _ { c } .
$$

By substituting Assumption 2(i), (15), and (16) into (14), we obtain the following for the given $k \geq 1$ .

$$
\begin{array} { l } { \displaystyle \| \varDelta \lambda _ { k + 1 } \| \leq \frac { 1 } { \sigma } \bigg ( L _ { f } \| \varDelta x _ { k + 1 } \| + \beta \| \varDelta x _ { k + 1 } \| + \beta \| \varDelta x _ { k } \| } \\ { \displaystyle \quad + \| \nabla c ( x _ { k + 1 } ) - \nabla c ( x _ { k } ) \| _ { 2 } \bigg ( \frac { 1 } { \sigma } M _ { f } + \frac { \beta } { \sigma } \| \varDelta x _ { k } \| + \frac { 1 } { \sigma } \| \tilde { r } _ { k } \| \bigg ) + \| \varDelta \tilde { r } _ { k + 1 } \| \bigg ) } \end{array}
$$

$$
\begin{array} { r l } & { \leq \cfrac { 1 } { \sigma } \bigg ( L _ { f } \| \Delta x _ { k + 1 } \| + \beta \| \Delta x _ { k + 1 } \| + \beta \| \Delta x _ { k } \| + \frac { L _ { c } M _ { f } } { \sigma } \| \Delta x _ { k + 1 } \| + \frac { 2 M _ { c } \beta } { \sigma } \| \Delta x _ { k } \| } \\ & { ~ + \frac { 2 M _ { c } } { \sigma } \| \widetilde { r } _ { k } \| + \| \Delta \widetilde { r } _ { k + 1 } \| \bigg ) } \\ & { \leq \cfrac { 1 } { \sigma } \bigg ( L _ { f } + \frac { L _ { c } M _ { f } } { \sigma } + \beta \bigg ) \| \Delta x _ { k + 1 } \| + \cfrac { 1 } { \sigma } \bigg ( \beta + \frac { 2 M _ { c } \beta } { \sigma } \bigg ) \| \Delta x _ { k } \| } \\ & { ~ + \frac { 2 M _ { c } } { \sigma ^ { 2 } } \| \widetilde { r } _ { k } \| + \frac { 1 } { \sigma } \| \Delta \widetilde { r } _ { k + 1 } \| . } \end{array}
$$

By using the bound $( a + b + c + d ) ^ { 2 } \leq 4 ( a ^ { 2 } + b ^ { 2 } + c ^ { 2 } + d ^ { 2 } )$ for positive scalars $a , b , c , d$ , and using the definition (11), we obtain the result. □

For the rest of this section, we use the following definitions for $c _ { 1 }$ and $c _ { 2 }$

$$
c _ { 1 } \triangleq \frac { \beta } { 4 } - \frac { C _ { 1 } } { \rho } , c _ { 2 } \triangleq \frac { \beta } { 4 } - \frac { C _ { 2 } } { \rho } ,
$$

where $C _ { 1 }$ and $C _ { 2 }$ are defined in (11). Next we show that sequences $\{ x _ { k } \}$ and $\{ \lambda _ { k } \}$ are bounded and $\{ P _ { k } \} _ { k \ge 1 }$ satisfies certain properties under Assumption 1–3, for suitable choices of the algorithmic parameters.

Lemma 3 Consider Algorithm 2 with conditions (6) and (7). Choose $\{ \tilde { r } _ { k } \} _ { k \ge 1 }$ such that $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \| \tilde { r } _ { k } \| ^ { 2 } \leq R < + \infty } \end{array}$ and $\| \tilde { r } _ { k } \| \ \leq \ 1$ , for all $k \geq 1$ . Let $\{ P _ { k } \} _ { k \ge 1 }$ be defined as in (8). Suppose that Assumptions 1 and 3 hold and define

$$
\hat { \alpha } \triangleq 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } + 2 ,
$$

where $C _ { 0 } > 0$ is any fixed constant. Suppose that Assumption 2 holds with $\boldsymbol { S } = \boldsymbol { S } _ { \hat { \alpha } } ^ { 0 }$ . Choose $\rho$ and $\beta$ such that

$$
\rho \geq \operatorname* { m a x } \left\{ \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } } + \rho _ { 0 } , \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \sigma ^ { 4 } } , 3 \rho _ { 0 } , 1 \right\} ,
$$

where

$$
D _ { S } \triangleq \operatorname* { m a x } \{ \| x - y \| \mid x , y \in S _ { \hat { \alpha } } ^ { 0 } \} ,
$$

and that $c _ { 1 }$ and $c _ { 2 }$ defined in (17) are both positive. Suppose that $x _ { 0 }$ satisfies $\| c ( x _ { 0 } ) \| ^ { 2 } \leq$ $\operatorname* { m i n } \{ C _ { 0 } / \rho , 1 \}$ , where $C _ { 0 }$ is the constant appearing in (18). Then

$$
\{ x _ { k } \} _ { k \geq 0 } \subseteq S _ { \hat { \alpha } } ^ { 0 } a n d \| \lambda _ { k } \| \leq \frac { M _ { f } + \beta D s + 1 } { \sigma } , f o r a l l k \geq 1 .
$$

Furthermore, (10) and the following inequality hold for any $k \geq 1$ ,

$$
P _ { k + 1 } - P _ { k } \leq - c _ { 1 } \| \Delta x _ { k + 1 } \| ^ { 2 } - c _ { 2 } \| \Delta x _ { k } \| ^ { 2 } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \| \tilde { r } _ { k } \| ^ { 2 } + \frac { 4 } { \rho \sigma ^ { 2 } } \| \tilde { r } _ { k + 1 } - \tilde { r } _ { k } \| ^ { 2 } .
$$

Proof Note that Assumption 3 implies that

$$
f ( x _ { 0 } ) \leq { \bar { U } } ,
$$

since $\left\| c ( x _ { 0 } ) \right\| \leq 1$ . Therefore,

$$
\mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 0 } ) = f ( x _ { 0 } ) + \lambda _ { 0 } ^ { T } c ( x _ { 0 } ) + \frac { \rho } { 2 } \| c ( x _ { 0 } ) \| ^ { 2 }
$$

$$
\begin{array} { l } { \displaystyle \le f ( \boldsymbol { x } _ { 0 } ) + \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } + \frac { \rho } { 2 } \| c ( \boldsymbol { x } _ { 0 } ) \| ^ { 2 } + \frac { \rho } { 2 } \| c ( \boldsymbol { x } _ { 0 } ) \| ^ { 2 } } \\ { \displaystyle \overset { ( 2 3 ) } { \le } \bar { U } + \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } . } \end{array}
$$

and

$$
\begin{array} { r l } & { \bar { U } + C _ { 0 } - \bar { L } \overset { ( 2 4 ) } { \geq } f ( x _ { 0 } ) + \lambda _ { 0 } ^ { T } c ( x _ { 0 } ) + \displaystyle \frac { \rho } { 2 } \| c ( x _ { 0 } ) \| ^ { 2 } - \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } - \bar { L } } \\ & { \qquad \overset { ( \rho \geq 3 \rho _ { 0 } ) } { \geq } f ( x _ { 0 } ) + \displaystyle \frac { \rho _ { 0 } } { 2 } \| c ( x _ { 0 } ) \| ^ { 2 } - \bar { L } + \lambda _ { 0 } ^ { T } c ( x _ { 0 } ) + \displaystyle \frac { \rho } { 3 } \| c ( x _ { 0 } ) \| ^ { 2 } - \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } } \\ & { \qquad \geq 0 + \displaystyle \frac { \rho } { 3 } \left\| c ( x _ { 0 } ) + \frac { 3 \lambda _ { 0 } } { 2 \rho } \right\| ^ { 2 } - \displaystyle \frac { 3 } { 4 \rho } \| \lambda _ { 0 } \| ^ { 2 } - \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } } \\ & { \qquad \overset { ( \rho \geq 1 ) } { \geq } - \displaystyle \frac { 5 } { 4 } \| \lambda _ { 0 } \| ^ { 2 } } \end{array}
$$

We prove the theorem by induction. We show that the following bounds hold for all $i \geq 1$

$$
\begin{array} { r } { \begin{array} { r l } & { ~ x _ { i } \in S _ { \hat { \alpha } } ^ { 0 } , } \\ & { \| \lambda _ { i } \| ^ { 2 } \leq \displaystyle \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { \sigma ^ { 2 } } \leq 2 ( \rho - \rho _ { 0 } ) , } \\ & { ~ P _ { i } \leq 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } + \displaystyle \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \displaystyle \sum _ { t = 1 } ^ { i - 1 } \| \tilde { r } _ { t } \| ^ { 2 } + \displaystyle \frac { 4 } { \rho \sigma ^ { 2 } } \sum _ { t = 1 } ^ { i - 1 } \| \tilde { r } _ { t + 1 } - \tilde { r } _ { t } \| ^ { 2 } . } \end{array} } \end{array}
$$

We verify first that (26) holds when $i = 1$ . From (7) we have

$$
\begin{array} { l } { f ( { \boldsymbol x } _ { 1 } ) + \displaystyle \lambda _ { 0 } ^ { T } c ( { \boldsymbol x } _ { 1 } ) + \frac { \rho } { 2 } \| c ( { \boldsymbol x } _ { 1 } ) \| ^ { 2 } + \frac { \beta } { 2 } \| { \boldsymbol x } _ { 1 } - { \boldsymbol x } _ { 0 } \| ^ { 2 } } \\ { \le f ( { \boldsymbol x } _ { 0 } ) + \lambda _ { 0 } ^ { T } c ( { \boldsymbol x } _ { 0 } ) + \displaystyle \frac { \rho } { 2 } \| c ( { \boldsymbol x } _ { 0 } ) \| ^ { 2 } \le \bar { U } + \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } + C _ { 0 } , } \end{array}
$$

so that for $i = 0$ and 1, we have

$$
\begin{array} { l } { f ( x _ { i } ) + \displaystyle \frac { \rho } { 6 } \| \boldsymbol { c } ( x _ { i } ) \| ^ { 2 }  \begin{array} { l l } { ( 4 ; , 0 ; 2 ) } \\ { \leq } & { \bar { U } + \displaystyle \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } + C _ { 0 } - \lambda _ { 0 } ^ { T } c ( x _ { i } ) - \displaystyle \frac { \rho } { 3 } \| \boldsymbol { c } ( x _ { i } ) \| ^ { 2 } } \\ { \qquad \quad } \\ { \quad } \\ { \quad } \end{array}  } \\ { \displaystyle \langle \frac { \rho \geq 3 \rho _ { 0 } } { 2 } \boldsymbol { \Psi } ( x _ { i } ) + \displaystyle \frac { \rho _ { 0 } } { 2 } \| \boldsymbol { c } ( x _ { i } ) \| ^ { 2 } \leq \bar { U } + \displaystyle \frac { 5 \| \lambda _ { 0 } \| ^ { 2 } } { 4 \rho } + C _ { 0 } } \\  \displaystyle  \begin{array} { l l } { ( 2 5 , \rho \geq 1 ) } \\ { \leq } & { \bar { U } + \displaystyle C _ { 0 } + \frac { 5 } { 4 } \| \lambda _ { 0 } \| ^ { 2 } + 6 ( \bar { U } + C _ { 0 } - \bar { L } + \frac { 5 } { 4 } \| \lambda _ { 0 } \| ^ { 2 } ) } \\ { \qquad \quad } \\ { \leq 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + \displaystyle \frac { 3 5 } { 4 } \| \lambda _ { 0 } \| ^ { 2 }  \begin{array} { l l } { ( 1 8 ) } \\ { < \hat { x } _ { i } } \\ { \hat { x } } \end{array}  } \end{array} \end{array}
$$

Thus, $x _ { 0 } , x _ { 1 } \in S _ { \hat { \alpha } } ^ { 0 }$ , verifying that (26a) holds for $i = 1$

ˆ Approximate first-order optimality (6) indicates that

$$
\nabla f ( x _ { 1 } ) + \nabla c ( x _ { 1 } ) \lambda _ { 1 } + \beta ( x _ { 1 } - x _ { 0 } ) = \tilde { r } _ { 1 } .
$$

Since $x _ { 0 } , x _ { 1 } \in S _ { \hat { \alpha } } ^ { 0 }$ , we have by Assumption 2 and (20) that

$$
\begin{array} { r l } & { \sigma \| \lambda _ { 1 } \| \leq \| \nabla c ( x _ { 1 } ) \lambda _ { 1 } \| = \| \nabla f ( x _ { 1 } ) + \beta ( x _ { 1 } - x _ { 0 } ) - \widetilde { r } _ { 1 } \| \leq M _ { f } + \beta D _ { S } + 1 . } \\ & { \qquad \implies \| \lambda _ { 1 } \| ^ { 2 } \leq \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { \sigma ^ { 2 } } \overset { ( 1 9 ) } { \leq } 2 ( \rho - \rho _ { 0 } ) . } \end{array}
$$

Thus, (26b) holds for $i = 1$ .

Next, we verify (26c) when $i = 1$ . Note that

$$
\begin{array} { r l } & { P _ { 1 } = \mathcal { L } _ { \rho } ( x _ { 1 } , \lambda _ { 1 } ) + \frac { \beta } { 4 } \| x _ { 1 } - x _ { 0 } \| ^ { 2 } } \\ & { \quad = \mathcal { L } _ { \rho } ( x _ { 1 } , \lambda _ { 1 } ) - \mathcal { L } _ { \rho } ( x _ { 1 } , \lambda _ { 2 } ) + \mathcal { L } _ { \rho } ( x _ { 1 } , \lambda _ { 3 } ) - \mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 4 } ) + \mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 0 } ) } \\ & { \quad \quad + \frac { \beta } { 4 } \| x _ { 1 } - x _ { 0 } \| ^ { 2 } } \\ & { \quad \stackrel { ( j ) } { \leq } \frac { 1 } { \rho } \| \lambda _ { 1 } - \lambda _ { 0 } \| ^ { 2 } - \frac { \beta } { 2 } \| x _ { 1 } - x _ { 0 } \| ^ { 2 } + \mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 0 } ) + \frac { \beta } { 4 } \| x _ { 1 } - x _ { 0 } \| ^ { 2 } } \\ & { \quad = \rho \| c ( x _ { 1 } ) \| ^ { 2 } - \frac { \beta } { 4 } \| x _ { 1 } - x _ { 0 } \| ^ { 2 } + \mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 0 } ) } \\ & { \quad \stackrel { ( 2 4 ) } { \leq } \rho \| c ( x _ { 1 } ) \| ^ { 2 } + \bar { \mathcal { N } } + \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } , } \\ & { \quad \stackrel { ( \rho \leq 1 ) } { \leq } \rho \| c ( x _ { 1 } ) \| ^ { 2 } + \bar { \mathcal { N } } + \frac { 1 } { 2 } \rho \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } , } \end{array}
$$

In addition, (27) indicates that

$$
\begin{array} { r l } & { \displaystyle \frac { \rho } { 6 } \| c ( x _ { 1 } ) \| ^ { 2 } } \\ & { \displaystyle \quad \leq \bar { U } + \displaystyle \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } - \lambda _ { 0 } ^ { T } c ( x _ { 1 } ) - \displaystyle \frac { \rho } { 6 } \| c ( x _ { 1 } ) \| ^ { 2 } - f ( x _ { 1 } ) - \displaystyle \frac { \rho } { 6 } \| c ( x _ { 1 } ) \| ^ { 2 } } \\ & { \displaystyle \quad = \bar { U } + \displaystyle \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } - \displaystyle \frac { \rho } { 6 } \| c ( x _ { 1 } ) + 3 \lambda _ { 0 } / \rho \| ^ { 2 } + \displaystyle \frac { 3 \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } - f ( x _ { 1 } ) - \displaystyle \frac { \rho } { 6 } \| c ( x _ { 1 } ) \| ^ { 2 } } \\ & { \displaystyle \quad \overset { ( \rho \geq 3 \rho ) } { \leq } \bar { U } + \displaystyle \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } + \displaystyle \frac { 3 \| \lambda _ { 0 } \| ^ { 2 } } { 2 \rho } - f ( x _ { 1 } ) - \displaystyle \frac { \rho _ { 0 } } { 2 } \| c ( x _ { 1 } ) \| ^ { 2 } } \\ & { \displaystyle \quad \leq \bar { U } + \displaystyle \frac { 2 } { \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } - \bar { L } \stackrel { ( \rho \geq 1 ) } { \leq } \bar { U } + 2 \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } - \bar { L } . } \end{array}
$$

By substituting this bound into (28), we have that

$$
P _ { 1 } \leq \bar { U } + \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 } + C _ { 0 } + \rho \| c ( x _ { 1 } ) \| ^ { 2 } \leq 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } ,
$$

so (26c) holds for $i = 1$ also.

We now take the inductive step, supposing that (26) holds when $i = k \ge 1$ , and proving that these three conditions continue to hold for $i = k + 1$ . By inequality (7), we have

$$
\begin{array} { r l r } {  { \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) \le \mathcal { L } _ { \rho } ( x _ { k } , \lambda _ { k } ) \le P _ { k } } } \\ & { \Longrightarrow f ( x _ { k + 1 } ) + \frac { \rho } { 2 } \| c ( x _ { k + 1 } ) \| ^ { 2 } + \lambda _ { k } ^ { T } c ( x _ { k + 1 } ) \le P _ { k } } \\ & { } & { \Longrightarrow f ( x _ { k + 1 } ) + \frac { \rho } { 2 } \| c ( x _ { k + 1 } ) \| ^ { 2 } - \frac { \| \lambda _ { k } \| ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } - \frac { ( \rho - \rho _ { 0 } ) \| c ( x _ { k + 1 } ) \| ^ { 2 } } { 2 } \le P _ { k } } \end{array}
$$

$$
\begin{array} { r l } & { \implies f ( x _ { + + 1 } ) + \frac { \beta \alpha _ { 0 } } { 2 } \lVert c ( x _ { + + 1 } ) \rVert ^ { 2 } \le F _ { k } + \frac { \lVert \lambda _ { k } \rVert ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } \stackrel { \mathrm { O } \mathrm { O } \mathrm { O } \mathrm { B } \mathrm { B } \mathrm { B } } + F _ { k } } \\ & { \overset { ( a \mathrm { E O } ) } { \le } 7 \tilde { U } + 7 C _ { 0 } - 6 \tilde { L } + 1 3 \lVert \lambda _ { 0 } \rVert ^ { 2 } + \frac { 1 6 M _ { e } ^ { 2 } } { \rho \sigma ^ { 4 } } \underset { \longrightarrow } { \lVert \tilde { r } _ { \parallel } \rVert ^ { 2 } } + \frac { 4 } { \rho \sigma ^ { 2 } } \underset { \longrightarrow } { \sum \lVert \tilde { r } _ { \pm 1 } \rVert ^ { 2 } } - \tilde { r } _ { \parallel } \lVert ^ { 2 } + 1 } \\ & { \le 7 \tilde { U } + 7 C _ { 0 } - 6 \tilde { L } + 1 3 \rVert \lambda _ { 0 } \rVert ^ { 2 } + \frac { 1 6 M _ { e } ^ { 2 } } { \rho \sigma ^ { 4 } } \underset { \longrightarrow } { \sum \lVert \tilde { r } _ { \parallel } \rVert ^ { 2 } } + \frac { 8 } { \rho \sigma ^ { 2 } } \underset { \longrightarrow } { \sum \{ - 1 \} } [ \lVert \tilde { r } _ { \pm 1 } \rVert ^ { 2 } + \lVert \tilde { r } _ { \parallel } \rVert ^ { 2 } ) + 1 } \\ & { \le 7 \tilde { U } + 7 C _ { 0 } - 6 \tilde { L } + 1 3 \rVert \lambda _ { 0 } \rVert ^ { 2 } + \frac { 1 6 M _ { e } ^ { 2 } } { \rho \sigma ^ { 4 } } \underset { \longrightarrow } { \sum \lVert \tilde { r } _ { \pm 1 } \rVert ^ { 2 } } + \frac { 1 6 } { \rho \sigma ^ { 2 } } \underset { \longrightarrow } { \sum \{ 1 \} } [ \tilde { r } _ { \parallel } ] ^ { 2 } + 1 } \\ &  \le 7 \tilde { U } + 7 C _ { 0 } - 6 \tilde { L }  \end{array}
$$

where the inequality on the third line holds because of $- \textstyle { \frac { r } { 2 } } \| a \| ^ { 2 } - \frac { 1 } { 2 r } \| b \| ^ { 2 } \leq a ^ { T } b$ , for any $r > 0 , a , b \in \mathbb { R } ^ { m } .$ Therefore, $\boldsymbol { x } _ { k + 1 } \in S _ { \hat { \boldsymbol { \alpha } } } ^ { 0 }$ , so we have proved (26a).

By approximate first-order optimality (6) and the hypothesis $x _ { k } \ \in \ S _ { \hat { \alpha } } ^ { 0 }$ , the argument to establish that λk 12 ≤ (M f +β DS+1)22 is the same as for the case of $i = 1$ , so (26b) holds for $i = k + 1$ .

Since $x _ { k }$ and $x _ { k + 1 }$ both belong to $S _ { \hat { \alpha } } ^ { 0 }$ , Lemma 2 indicates that (10) holds. By combining ˆ (10) with (9), we obtain (22). Therefore,

$$
\begin{array} { r l r } {  { P _ { k + 1 } \stackrel { ( 2 2 ) } { \leq } P _ { k } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \| \tilde { r } _ { k } \| ^ { 2 } + \frac { 4 } { \rho \sigma ^ { 2 } } \| \tilde { r } _ { k + 1 } - \tilde { r } _ { k } \| ^ { 2 } } } \\ & { } & { \stackrel { ( 2 6 ) } { \leq } 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \displaystyle \sum _ { t = 1 } ^ { k } \| \tilde { r } _ { t } \| ^ { 2 } + \frac { 4 } { \rho \sigma ^ { 2 } } \displaystyle \sum _ { t = 1 } ^ { k } \| \tilde { r } _ { t + 1 } - \tilde { r } _ { t } \| ^ { 2 } . } \end{array}
$$

Thus we have established (26c) for $i = k + 1$ . Note that (10) and (22) hold for all $k \geq 1$ , so we have completed the proof. □

First-order complexity. With the properties of $\{ P _ { k } \} _ { k \ge 1 }$ established to this point, we can analyze the complexity of obtaining an $\epsilon$ -1o solution. For any given $\epsilon > 0$ , we define two quantities which will be referred to repeatedly in subsequent sections:

$$
\begin{array} { r l } & { T _ { \epsilon } \triangleq \operatorname* { i n f } \{ t \ge 1 \ | \ \| \nabla _ { x } \mathcal { L } _ { 0 } ( x _ { t } , \lambda _ { t } ) \| \le \epsilon , \| c ( x _ { t } ) \| \le \epsilon \} . } \\ & { \hat { T } _ { \epsilon } \triangleq \operatorname* { i n f } \{ t \ge 1 \ | \ x _ { t } \mathrm { ~ i s ~ a n ~ } \epsilon - \mathrm { 1 o ~ s o l u t i o n ~ o f ~ } ( 1 ) \} . } \end{array}
$$

Note that $\hat { T } _ { \epsilon }$ is independent of the Proximal AL method. Meanwhile, by the definition of $\mathcal { L } _ { 0 } ( x , \lambda )$ , we know that $x _ { T _ { \epsilon } }$ is an $\epsilon$ -1o solution and $\lambda _ { T _ { \epsilon } }$ is the associated multiplier, indicating that $\hat { T } _ { \epsilon } \le T _ { \epsilon }$ . The definition of $T _ { \epsilon }$ also suggests the following stopping criterion for Algorithm 2:

$$
\| \nabla _ { x } { \mathcal { L } } _ { 0 } ( x _ { t } , \lambda _ { t } ) \| \leq \epsilon { \mathrm { ~ a n d ~ } } \| c ( x _ { t } ) \| \leq \epsilon { \mathrm { ~ t h e n ~ } } { \mathrm { S T O P } } .
$$

Under this criterion, Algorithm 2 will stop at iteration $T _ { \epsilon } \mathrm { ~ - ~ } 1$ and output $x _ { T _ { \epsilon } }$ as an $\epsilon$ -1o solution.

Part (i) of the following result shows subsequential convergence of the generated sequence to the first-order optimal point. Part (ii) describes the speed of such convergence by obtaining an estimate of $T _ { \epsilon }$ in terms of $\epsilon$ . In this result, we make a specific choice $\beta = \epsilon ^ { \eta } / 2$ for the proximality parameter. We could choose $\beta$ to be any fixed multiple of this value (the multiple not depending on $\epsilon$ ) and obtain a similar result with only trivial changes to the analysis.

Theorem 2 (First-order complexity) Consider Algorithm 2 with conditions (6) and (7), and let $\{ P _ { k } \} _ { k \ge 1 }$ be defined as in (8). Suppose that Assumptions 1, 3 and 2 hold with $\boldsymbol { S } = \boldsymbol { S } _ { \hat { \alpha } } ^ { 0 }$ (with $\hat { \alpha }$ defined in (18)), and that $\epsilon \in ( 0 , 1 ]$ and $\eta \in [ 0 , 2 ]$ ˆ are given. Suppose that the residual sequence $\{ \tilde { r } _ { k } \} _ { k \ge 1 }$ is chosen such that ${ \textstyle \sum _ { k = 1 } ^ { \infty } \| \tilde { r } _ { k } \| ^ { 2 } \le R \in [ 1 , \infty ) }$ and $\| \tilde { r } _ { k } \| \le \epsilon / 2$ for all $k \geq 1$ .

Define $\beta = \epsilon ^ { \eta } / 2$ and

$$
\rho \geq \operatorname* { m a x } \left\{ \frac { 1 6 \operatorname* { m a x } \{ C _ { 1 } , C _ { 2 } \} } { \epsilon ^ { \eta } } , \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } } + \rho _ { 0 } , \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \sigma ^ { 4 } } , 3 \rho _ { 0 } , 1 \right\} ,
$$

where $C _ { 1 }$ and $C _ { 2 }$ are defined as in (11), and $D _ { S }$ is the diameter of $S _ { \hat { \alpha } } ^ { 0 }$ , as defined in (20). Suppose that $x _ { 0 }$ satisfies $\| c ( x _ { 0 } ) \| ^ { 2 } \leq \operatorname* { m i n } \{ C _ { 0 } / \rho , 1 \}$ , where $C _ { 0 }$ is the constant appearing in (18). Then we have the following.

(i) A subsequence of $\{ ( x _ { k } , \lambda _ { k } ) \} _ { k \geq 1 }$ generated by Algorithm 2 converges to a point $( x ^ { * } , \lambda ^ { * } )$ satisfying first-order optimality conditions for (1), namely,

$$
\nabla f ( x ^ { * } ) + \nabla c ( x ^ { * } ) \lambda ^ { * } = 0 , c ( x ^ { * } ) = 0 .
$$

(ii) For $T _ { \epsilon }$ and $\hat { T } _ { \epsilon }$ defined in (30), we have $\hat { T } _ { \epsilon } \le T _ { \epsilon } = \mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ . In particular, if $\eta = 2$ , then $\hat { T } _ { \epsilon } = \mathcal { O } ( 1 )$ .

Proof We first prove (i). Checking the positivity of $c _ { 1 }$ and $c _ { 2 }$ , given the parameter assignments, we have

$$
\begin{array} { r l } & { c _ { 1 } = \frac { \beta } { 4 } - \cfrac { C _ { 1 } } { \rho } \cfrac { ( 3 2 ) } { 2 } \cfrac { e ^ { \eta } } { 8 } - \cfrac { e ^ { \eta } } { 1 6 } > 0 , \quad c _ { 2 } = \frac { \beta } { 4 } - \cfrac { C _ { 2 } } { \rho } \cfrac { ( 3 2 ) } { 2 } \cfrac { e ^ { \eta } } { 1 6 } > 0 . } \\ & { P _ { k } \succeq f ( x _ { k } ) + \frac { \beta } { 2 } \| c ( x _ { k } ) \| ^ { 2 } + \chi _ { k } ^ { T } c ( x _ { k } ) } \\ & { \quad \succeq f ( x _ { k } ) + \frac { \rho } { 2 } \| c ( x _ { k } ) \| ^ { 2 } - \cfrac { \| \lambda _ { k } \| ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } - \cfrac { ( \rho - \rho _ { 0 } ) \| c ( x _ { k } ) \| ^ { 2 } } { 2 } } \\ & { \quad = f ( x _ { k } ) + \frac { \rho _ { 0 } } { 2 } \| c ( x _ { k } ) \| ^ { 2 } - \cfrac { \| \lambda _ { k } \| ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } } \\ & { \quad \overset { \mathrm { ( L e m a n a 3 ) } } { \underset { { \leq } } { \geq } } f ( x _ { k } ) + \frac { \rho _ { 0 } } { 2 } \| c ( x _ { k } ) \| ^ { 2 } - \cfrac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } ( \rho - \rho _ { 0 } ) } } \\ & { \quad \overset { \mathrm { ( S _ { 1 } , \rho 3 2 ) } } { \underset { { \leq } } { \geq } } \tilde { L } - 1 . } \end{array}
$$

Therefore, using (22) from Lemma 3, we have the following for any $k \geq 1$ :

$$
\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { k } [ c _ { 1 } \| A x _ { i + 1 } \| ^ { 2 } + c _ { 2 } \| A x _ { i } \| ^ { 2 } ] } } \\ & { } & { \leq P _ { 1 } - P _ { k + 1 } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \displaystyle \sum _ { i = 1 } ^ { k } \| \tilde { r } _ { i } \| ^ { 2 } + \frac { 4 } { \rho \sigma ^ { 2 } } \displaystyle \sum _ { i = 1 } ^ { k } \| \tilde { r } _ { i + 1 } - \tilde { r } _ { i } \| ^ { 2 } } \\ & { } & { \leq P _ { 1 } - P _ { k + 1 } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho \sigma ^ { 4 } } \displaystyle \sum _ { i = 1 } ^ { k } \| \tilde { r } _ { i } \| ^ { 2 } + \frac { 8 } { \rho \sigma ^ { 2 } } \displaystyle \sum _ { i = 1 } ^ { k } ( \| \tilde { r } _ { i + 1 } \| ^ { 2 } + \| \tilde { r } _ { i } \| ^ { 2 } ) } \end{array}
$$

$$
\begin{array} { r l } & { \le P _ { 1 } - P _ { k + 1 } + \displaystyle \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) } { \rho \sigma ^ { 4 } } \displaystyle \sum _ { i = 1 } ^ { \infty } \| \tilde { r } _ { i } \| ^ { 2 } } \\ & { \le P _ { 1 } - P _ { k + 1 } + \displaystyle \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \rho \sigma ^ { 4 } } } \\ & { \overset { ( 3 4 ) } { \le } P _ { 1 } - ( \bar { L } - 1 ) + \displaystyle \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \rho \sigma ^ { 4 } } } \\ & { \overset { ( 3 2 ) } { \le } P _ { 1 } - \bar { L } + 2 } \\ & { \overset { ( 2 9 ) } { \le } \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } - \bar { L } + 2 = \hat { \alpha } - \bar { L } . } \end{array}
$$

Because of (21) in Lemma 3 and compactness of $S _ { \hat { \alpha } } ^ { 0 }$ , the sequence $\{ ( x _ { k } , \lambda _ { k } ) \} _ { k \geq 1 }$ is bounded, so there exists a convergent subsequence $\{ ( x _ { k } , \lambda _ { k } ) \} _ { k \in \mathcal { K } }$ with limit $( x ^ { * } , \lambda ^ { * } )$ . Since (36) holds for any $k \geq 1$ and $c _ { 1 } > 0 , c _ { 2 } > 0$ , we have that $\operatorname* { l i m } _ { k \to \infty } \| \varDelta x _ { k } \| = 0$ . Moreover, finiteness of $\scriptstyle \sum _ { k = 1 } ^ { \infty } \| { \tilde { r } } _ { k } \| ^ { 2 }$ implies that $\operatorname* { l i m } _ { k \to \infty } \| \tilde { r } _ { k } \| = 0$ . Therefore, we have

$$
\begin{array} { r l } & { \displaystyle \nabla f ( x ^ { * } ) + \nabla c ( x ^ { * } ) \lambda ^ { * } = \operatorname* { l i m } _ { k \in \mathsf K } ( \nabla f ( x _ { k } ) + \nabla c ( x _ { k } ) \lambda _ { k } ) } \\ & { \quad \quad = \displaystyle \operatorname* { l i m } _ { k \in \mathsf K } ( \nabla f ( x _ { k } ) + \nabla c ( x _ { k } ) ( \lambda _ { k - 1 } + \rho c ( x _ { k } ) ) ) = \operatorname* { l i m } _ { k \in \mathsf K } \nabla _ { x } \mathcal L _ { \rho } ( x _ { k } , \lambda _ { k - 1 } ) } \\ & { \displaystyle \overset { ( 6 ) } { = } \operatorname* { l i m } _ { k \in \mathsf K } ( - \beta \varDelta x _ { k } + \tilde { r } _ { k } ) = 0 . } \end{array}
$$

Since (10) holds for any $k \geq 1$ by Lemma 3, we have

$$
\begin{array} { l } { \displaystyle | c ( \boldsymbol { x } ^ { * } ) | | ^ { 2 } = \operatorname* { l i m } _ { k \in \mathcal K } \| c ( \boldsymbol { x } _ { k } ) \| ^ { 2 } = \operatorname* { l i m } _ { k \in \mathcal K } \| \lambda _ { k } - \lambda _ { k - 1 } \| ^ { 2 } / \rho ^ { 2 } } \\ { \displaystyle \quad \stackrel { ( 1 0 ) } { \leq } \operatorname* { l i m } _ { k \in \mathcal K } \frac { C _ { 1 } } { \rho ^ { 2 } } \| \Delta \boldsymbol { x } _ { k } \| ^ { 2 } + \frac { C _ { 2 } } { \rho ^ { 2 } } \| \Delta x _ { k - 1 } \| ^ { 2 } + \frac { 1 6 M _ { c } ^ { 2 } } { \rho ^ { 2 } \sigma ^ { 4 } } \| \tilde { \boldsymbol { r } } _ { k - 1 } \| ^ { 2 } + \frac { 4 } { \rho ^ { 2 } \sigma ^ { 2 } } \| \tilde { \boldsymbol { r } } _ { k } - \tilde { \boldsymbol { r } } _ { k - 1 } \| ^ { 2 } = 0 . } \end{array}
$$

completing the proof of (i).

We now prove (ii). Define

$$
\begin{array} { l } { { \displaystyle C _ { 1 } ^ { o } \triangleq \frac { 4 } { \sigma ^ { 2 } } \left( L _ { f } + \frac { L _ { c } M _ { f } } { \sigma } \right) ^ { 2 } \le C _ { 1 } , } } \\ { { \displaystyle \hat { \Delta } \triangleq ( \hat { \alpha } - \bar { L } ) \operatorname* { m a x } \left\{ 1 6 , 1 / ( 8 C _ { 1 } ^ { o } ) \right\} . } } \end{array}
$$

We want to show that $T _ { \epsilon } \le \lceil \hat { \Delta } / \epsilon ^ { 2 - \eta } \rceil + 1$ . Let $K \triangleq \lceil \hat { \Delta } / \epsilon ^ { 2 - \eta } \rceil$ , and note that since (36) holds for $k = K$ , we have that there exists some $k ^ { * } \in \{ 1 , 2 , \ldots , K \}$ such that

$$
c _ { 1 } \| x _ { k ^ { * } + 1 } - x _ { k ^ { * } } \| ^ { 2 } + c _ { 2 } \| x _ { k ^ { * } } - x _ { k ^ { * } - 1 } \| ^ { 2 } \leq ( \hat { \alpha } - \bar { L } ) / K .
$$

Thus, we have

$$
\begin{array} { r l } & { \| \nabla { \mathcal L } _ { 0 } ( x _ { k ^ { * } + 1 } , \lambda _ { k ^ { * } + 1 } ) \| = \| \nabla { \mathcal L } _ { \rho } ( x _ { k ^ { * } + 1 } , \lambda _ { k ^ { * } } ) \| \stackrel { ( 6 . ) } \leq \beta \| x _ { k ^ { * } + 1 } - x _ { k ^ { * } } \| + \| \tilde { r } _ { k ^ { * } + 1 } \| } \\ & { \quad \overset { ( 3 8 ) } \leq \beta \sqrt { \frac { ( \hat { \alpha } - \bar { L } ) / c _ { 1 } } { K } } + \frac { \epsilon } { 2 } \overset { ( 3 3 ) } { \leq } \frac { \epsilon ^ { \eta } } { 2 } \sqrt { \frac { ( \hat { \alpha } - \bar { L } ) / ( \epsilon ^ { \eta } / 1 6 ) } { K } } + \frac { \epsilon } { 2 } } \\ & { \quad \leq \frac { \epsilon ^ { \eta } } { 2 } \sqrt { \frac { 1 6 ( \hat { \alpha } - \bar { L } ) / ( \epsilon ^ { \eta } ) } { \hat { \Delta } \epsilon ^ { \eta - 2 } } } + \frac { \epsilon } { 2 } \overset { ( 3 7 b ) } { \leq } \frac { \epsilon ^ { \eta } } { 2 } \sqrt { \frac { 1 6 ( \hat { \alpha } - \bar { L } ) } { 1 6 ( \hat { \alpha } - \bar { L } ) \epsilon ^ { 2 \eta - 2 } } } + \frac { \epsilon } { 2 } = \epsilon . } \end{array}
$$

For the constraint norm, we have

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { i } \frac { \mathrm { d } } { \mathrm { d } t } \mathrm { d } _ { \mathrm { { S } } } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } \\ & { \frac { 1 } { \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } + \frac { 1 } { \mathrm { d } t } \frac { \mathrm { d } _ { \mathrm { S } } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } { \mathrm { d } t } \frac { \mathrm { d } _ { \mathrm { S } } ^ { 2 } } { \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } + \frac { \mathrm { d } _ { \mathrm { S } } ^ { 2 } } { \mathrm { d } t } \frac { \left( \mathrm { d } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } { \mathrm { d } t } \frac { \left( \mathrm { d } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } { \mathrm { d } t ^ { 2 } } + \frac { \mathrm { d } _ { \mathrm { S } } ^ { 2 } } { \mathrm { d } t } \left( \mathrm { R e } ^ { 2 } + \mathrm { b } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } \\ & { \frac { 1 } { \mathrm { d } \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } + \frac { 1 } { \mathrm { d } t } \frac { \mathrm { d } _ { \mathrm { S } } ^ { 2 } } { \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } } \\ &  \frac { 1 } { \mathrm { d } \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } + \frac { 1 } { \mathrm { d } t } \frac { \mathrm { d } _ { \mathrm { S } } ^ { 2 } } { \mathrm { d } t } \left( \mathrm { a } _ { \mathrm { S } } ^ { \dagger } \right) ^ { 2 } \end{array} \end{array}
$$

Therefore, we have

$$
\begin{array} { r } { T _ { \epsilon } \le k ^ { * } + 1 \le K + 1 = \lceil \hat { \Delta } / \epsilon ^ { 2 - \eta } \rceil + 1 . } \end{array}
$$

It follows that $\hat { T } _ { \epsilon } \le T _ { \epsilon } \le \lceil \hat { \Delta } / \epsilon ^ { 2 - \eta } \rceil + 1$ , completing the proof.

Remark 1 (i) The condition $\| c ( x _ { 0 } ) \| ^ { 2 } \leq \operatorname* { m i n } \{ C _ { 0 } / \rho , 1 \}$ is obviously satisfied by a feasible point, for which $c ( x _ { 0 } ) = 0$ . In this case, we do not need Assumption 3 and can prove a result with $\hat { \alpha } = 7 f ( x _ { 0 } ) + 7 C _ { 0 } - 6 \bar { L } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } + 2 .$ . An initial phase can be applied, if necessary, to find a point with small $\| c ( x _ { 0 } ) \|$ ; we discuss this point in a later section.

(ii) When $\eta = 0$ , the complexity result is consistent with that of [26]. However, our parameter choices $\beta = \epsilon ^ { \eta }$ for $\eta > 0$ allows us to choose $\beta$ to be small because, unlike [26], we are not concerned with maintaining strong convexity of the subproblem in Step 1 of Algorithm 2. Another benefit of small $\beta$ is that it allows complexity results to be proved for $\epsilon { - } 2 0$ points, which follows from part (ii) of Theorem 2, as we see next.

Second-order complexity. We further assume that in Step 1 of Algorithm 2, $x _ { k + 1 }$ satisfies the following approximate second-order optimality conditions:

$$
\begin{array} { r } { \nabla _ { x x } ^ { 2 } \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) + \beta I \succeq - \epsilon _ { k + 1 } ^ { H } I , \quad \mathrm { f o r ~ a l l } \ k \geq 0 , } \end{array}
$$

where $\{ \epsilon _ { k + 1 } ^ { H } \} _ { k \geq 0 }$ is a chosen error sequence.

In corresponding fashion to the definition of $\hat { T } _ { \epsilon }$ in (30b), we define $\widetilde { T } _ { \epsilon }$ as follows:

$$
\widetilde { T } _ { \epsilon } \triangleq \operatorname* { i n f } \{ t \geq 1 \ | \ x _ { t } \ \mathrm { i s } \ \mathrm { a n } \epsilon - \ 2 0 \ \mathrm { s o l u t i o n } \ \mathrm { o f } ( 1 ) \} .
$$

We have the following result for complexity of obtaining an $\epsilon { - } 2 0$ stationary point of (1) through Algorithm 2.

Corollary 1 (Second-order complexity) Suppose that all assumptions and settings in Theorem 2 hold. Assume that, in addition, Step 1 of Algorithm 2 satisfies (40), with $\epsilon _ { k } ^ { H } \equiv \epsilon / 2$ for all $k \geq 1$ . Let $\eta \in [ 1 , 2 ]$ . Then for $\widetilde { T } _ { \epsilon }$ defined in (41), we have $\widetilde { T } _ { \epsilon } = \mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ .

Proof Since $\beta = \epsilon ^ { \eta } / 2 \le \epsilon / 2$ and $\epsilon _ { k + 1 } ^ { H } \equiv \epsilon / 2$ , for any $k \geq 0$

$$
\nabla _ { x x } ^ { 2 } \mathcal { L } _ { \rho } ( x _ { k + 1 } , \lambda _ { k } ) \succeq - ( \beta + \epsilon _ { k + 1 } ^ { H } ) I \succeq - \epsilon I .
$$

This fact indicates that

$$
\nabla ^ { 2 } f ( x _ { k + 1 } ) + \sum _ { i = 1 } ^ { m } [ \lambda _ { k + 1 } ] _ { i } \nabla ^ { 2 } c _ { i } ( x _ { k + 1 } ) + \rho \nabla c ( x _ { k + 1 } ) [ \nabla c ( x _ { k + 1 } ) ] ^ { T } \succeq - \epsilon I ,
$$

which implies that

$$
d ^ { T } ( \nabla ^ { 2 } f ( x _ { k + 1 } ) + \sum _ { i = 1 } ^ { m } [ \lambda _ { k + 1 } ] _ { i } \nabla ^ { 2 } c _ { i } ( x _ { k + 1 } ) ) d \geq - \epsilon \| d \| ^ { 2 } ,
$$

for any $d \in S ( x _ { k + 1 } ) \triangleq \{ d \in \mathbb { R } ^ { n } \mid [ \nabla c ( x _ { k + 1 } ) ] ^ { T } d = 0 \}$ . This is exactly condition (2b) of Definition 2. Therefore, we have

$$
\begin{array} { r l } & { \widetilde { I } _ { \epsilon } = \operatorname* { i n f } \{ t \geq 1 \ | \ \exists \lambda \in \mathbb { R } ^ { m } , \| \nabla f ( x _ { t } ) + \nabla c ( x _ { t } ) \lambda | \leq \epsilon , \| c ( x _ { t } ) \| \leq \epsilon , } \\ & { \qquad \quad d ^ { T } ( \nabla ^ { 2 } f ( x _ { t } ) + \displaystyle \sum _ { i = 1 } ^ { m } \lambda _ { i } \nabla ^ { 2 } c _ { i } ( x _ { t } ) ) d \geq - \epsilon \| d \| ^ { 2 } , \quad \mathrm { f o r ~ a l l } \ d \in S ( x _ { t } ) \} } \\ & { \leq \operatorname* { i n f } \{ t \geq 1 \ | \ \| \nabla f ( x _ { t } ) + \nabla c ( x _ { t } ) \lambda _ { t } \| \leq \epsilon , \| c ( x _ { t } ) \| \leq \epsilon , } \\ & { \qquad \quad d ^ { T } ( \nabla ^ { 2 } f ( x _ { t } ) + \displaystyle \sum _ { i = 1 } ^ { m } [ \lambda _ { t } ] _ { i } \nabla ^ { 2 } c _ { i } ( x _ { t } ) ) d \geq - \epsilon \| d \| ^ { 2 } , \quad \mathrm { f o r ~ a l l } \ d \in S ( x _ { t } ) \} } \\ & { = \operatorname* { i n f } \{ t \geq 1 \ | \ \| \nabla f ( x _ { t } ) + \nabla c ( x _ { t } ) \lambda _ { t } \| \leq \epsilon , \| c ( x _ { t } ) \| \leq \epsilon \} = T _ { \epsilon } . } \end{array}
$$

The result now follows from Theorem 2.

# 4 Total Iteration/Operation Complexity of Proximal AL

In this section, we will choose an appropriate method to solve the subproblem and estimate the total iteration and operation complexity of our Proximal AL approach to find an $\epsilon$ -1o or $\epsilon { - } 2 0$ solution. To solve the subproblem at each major iteration of Algorithm 2, we can use methods for unconstrained smooth nonconvex optimization that allow the decrease condition (7) to hold, and approximate optimality conditions (6) or (40) to be enforced in a natural way, finding points that satisfy such conditions within a certain number of iterations that depends on the tolerances [10,15,20,21,33]. Among these, the Newton-CG method described in [33] has good complexity guarantees as well as good practical performance.

To review the properties of the algorithm in [33], we consider the following unconstrained problem:

$$
\operatorname* { m i n } _ { z \in \mathbb { R } ^ { n } } ~ F ( z )
$$

where $F : \mathbb { R } ^ { n }  \mathbb { R }$ is a twice Lipschitz continuously differentiable function. The Newton-CG approach makes use of the following assumption.

Assumption 4 (a) The set $\{ z \mid F ( z ) \leq F ( z _ { 0 } ) \}$ is compact, where $z _ { \mathrm { 0 } }$ is the initial point.

(b) $F$ is twice uniformly Lipschitz continuously differentiable on a neighborhood of $\{ z \mid$ $F ( z ) \leq F ( z _ { 0 } ) \}$ that includes the trial points generated by the algorithm.   
(c) Given $\epsilon _ { H } > 0$ and $0 < \delta \ll 1$ , a procedure called by the algorithm to verify approximate positive definiteness of $\nabla ^ { 2 } F ( z )$ either certifies that $\overline { { \nabla ^ { 2 } F ( z ) } } \succeq - \epsilon _ { H } I$ or finds a direction along which curvature of $\nabla ^ { 2 } F ( z )$ is smaller than $- \epsilon _ { H } / 2$ in at most $N _ { \mathrm { m e o } } \triangleq \operatorname* { m i n } \{ n , 1 +$ $\lceil \mathcal { C } _ { \mathrm { m e o } } \epsilon _ { H } ^ { - 1 / 2 } \rceil \}$ −1/2H } Hessian-vector products, with probability 1 − δ, where Cmeo depends at most logarithmically on $\delta$ and $\epsilon _ { H }$ .

Based on the above assumption, the following iteration complexity is indicated by [33, Theorem 4].

Theorem 3 Suppose that Assumption 4 holds. The Newton-CG terminates at a point satisfying

$$
\| \nabla F ( z ) \| \le \epsilon _ { g } , \quad \lambda _ { \operatorname* { m i n } } ( \nabla ^ { 2 } F ( z ) ) \ge - \epsilon _ { H } ,
$$

in at most $\bar { K }$ iterations with probability at least $( 1 - \delta ) ^ { \bar { K } }$ , where

$$
\bar { K } \triangleq \left\lceil C _ { \mathrm { N C G } } \operatorname* { m a x } \{ L _ { F , H } ^ { 3 } , 1 \} ( F ( z _ { 0 } ) - F _ { \mathrm { l o w } } ) \operatorname* { m a x } \{ \epsilon _ { g } ^ { - 3 } \epsilon _ { H } ^ { 3 } , \epsilon _ { H } ^ { - 3 } \} \right\rceil + 2 .
$$

(With probability at most $1 - ( 1 - \delta ) ^ { \bar { K } }$ , it terminates incorrectly within $\bar { K }$ iterations at $a$ point at which $\| \nabla F ( z ) \| \le \epsilon _ { g }$ but $\lambda _ { \operatorname * { m i n } } ( \nabla ^ { 2 } F ( z ) ) < - \epsilon _ { H } .$ ) Here, $C _ { \mathrm { { N C G } } }$ is a constant that depends on user-defined algorithmic parameters, $L _ { F , H }$ is the Lipschitz constant for $\nabla ^ { 2 } F$ on the neighborhood defined in Assumption $4 ( b )$ , and $F _ { \mathrm { l o w } }$ is the lower bound of $F ( z )$ .

Since in the Newton-CG approach, Hessian-vector products are the fundamental operations, [33] also derives operation complexity results, in which the operations are either evaluations of $\nabla F ( z )$ or evaluations of matrix-vector products involving $\nabla ^ { 2 } F ( z )$ and an arbitrary vector (which can be computed without actually evaluating the Hessian itself).

Corollary 2 Suppose that Assumption 4 holds. Let $\bar { K }$ be defined as in (44). Then with probability at least $( 1 - \delta ) ^ { \bar { K } }$ , Newton-CG terminates at a point satisfying (43) after at most

$$
( \operatorname* { m a x } \{ 2 \operatorname* { m i n } \{ n , J ( U _ { F , H } , \epsilon _ { H } ) \} + 2 , N _ { \mathrm { m e o } } \} ) \bar { K }
$$

Hessian-vector products, where $U _ { F , H }$ is the upper bound for $\nabla ^ { 2 } F ( z )$ on the neighborhood defined in Assumption $4 ( b )$ and $J ( \cdot , \cdot )$ satisfies

$$
J ( U _ { F , H } , \epsilon _ { H } ) \le \operatorname* { m i n } \left\{ n , \left\lceil \left( \sqrt { \kappa } + \frac 1 2 \right) \log \left( \frac { 1 4 4 ( \sqrt { \kappa } + 1 ) ^ { 2 } \kappa ^ { 6 } } { \zeta ^ { 2 } } \right) \right\rceil \right\} ,
$$

where $\begin{array} { r } { \kappa \triangleq \frac { U _ { F , H } + 2 \epsilon _ { H } } { \epsilon _ { H } } } \end{array}$ and $\zeta$ is a user-defined algorithmic parameter. (With probability at most $1 - ( 1 - \delta ) ^ { \bar { K } }$ , it terminates incorrectly within such complexity at a point for which $\lVert \nabla F ( z ) \rVert \leq \epsilon _ { g }$ but $\lambda _ { \operatorname* { m i n } } ( \nabla ^ { 2 } F ( z ) ) < - \epsilon _ { H }$ .)

To get total iteration and operation complexity we can aggregate the cost of applying Newton-CG to each subproblem in Algorithm 2. We present a critical lemma before deriving the total iteration complexity and operation complexity (Theorem 4 and Corollary 3). For these purposes, we denote the objective to be minimized at iteration $k$ of Algorithm 2 as follows:

$$
\psi _ { k } ( x ) \triangleq { \mathcal { L } } _ { \rho } ( x , \lambda _ { k } ) + { \frac { \beta } { 2 } } \| x - x _ { k } \| ^ { 2 } .
$$

Additionally, we recall from Assumption 1 that $\begin{array} { r } { S _ { \alpha } ^ { 0 } \triangleq \{ f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } \leq \alpha \} } \end{array}$ is either empty or compact for all $\alpha$ .

Lemma 4 Suppose that assumptions and parameter settings in Theorem 2 hold. In addition, suppose that $\begin{array} { r } { \bar { \rho } \ge \frac { 1 } { 2 } \| \lambda _ { 0 } \| ^ { 2 } + \bar { \rho _ { 0 } } } \end{array}$ . Then we have

$$
\{ x \mid \psi _ { k } ( x ) \leq \psi _ { k } ( x _ { k } ) \} \subseteq S _ { \hat { \alpha } } ^ { 0 } ,
$$

and

$$
\psi _ { k } ( x _ { k } ) - \psi _ { k } ^ { l o w } \leq \hat { \alpha } - \bar { L } ,
$$

for all $k \geq 0$ , where $\psi _ { k } ^ { l o w } \triangleq \operatorname* { i n f } _ { x \in \mathbb { R } ^ { n } } \psi _ { k } ( x )$ and $\hat { \alpha }$ is defined in (18). Hence $\{ x \mid \psi _ { k } ( x ) \mid $ $\psi _ { k } ( x _ { k } ) \}$ is compact for all $k \geq 0$ .

Proof Because of $c _ { 1 } > 0$ and $c _ { 2 } > 0$ and (35), we have for any $k \geq 1$ that

$$
P _ { k + 1 } \leq P _ { 1 } + \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \rho \sigma ^ { 4 } } \overset { ( 3 2 ) } { \leq } P _ { 1 } + 1 .
$$

Thus for any $k \geq 1$ , we have

$$
\psi _ { k } ( x _ { k } ) = \mathcal L _ { \rho } ( x _ { k } , \lambda _ { k } ) \leq P _ { k } \leq P _ { 1 } + 1 ,
$$

which, using (29) and (18), implies that

$$
\psi _ { k } ( x _ { k } ) \le 7 \bar { U } + 7 C _ { 0 } + 1 3 \| \lambda _ { 0 } \| ^ { 2 } - 6 \bar { L } + 1 = \hat { \alpha } - 1 .
$$

Note that (49) also holds when $k = 0$ since

$$
\begin{array} { l } { \displaystyle \psi _ { 0 } ( x _ { 0 } ) = \mathcal { L } _ { \rho } ( x _ { 0 } , \lambda _ { 0 } ) \overset { ( 2 4 ) } { \leq } \bar { U } + \displaystyle \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } } \\ { \displaystyle \overset { ( 2 5 ) } { \leq } \bar { U } + \displaystyle \frac { 1 } { 2 \rho } \| \lambda _ { 0 } \| ^ { 2 } + C _ { 0 } + 6 ( \bar { U } + C _ { 0 } - \bar { L } + ( 5 / 4 ) \| \lambda _ { 0 } \| ^ { 2 } ) } \\ { \displaystyle \overset { ( \rho \geq 1 ) } { \leq } 7 \bar { U } + 7 C _ { 0 } - 6 \bar { L } + 8 \| \lambda _ { 0 } \| ^ { 2 } < \hat { \alpha } - 1 } \end{array}
$$

Further, for any $k \geq 0$ , we have

$$
\begin{array} { l } { \displaystyle \psi _ { k } ( x ) = \mathcal { L } _ { \rho } ( x , \lambda _ { k } ) + \frac { \beta } { 2 } \| x - x _ { k } \| ^ { 2 } } \\ { \displaystyle \quad = f ( x ) + \frac { \rho } { 2 } \| c ( x ) \| ^ { 2 } + \lambda _ { k } ^ { T } c ( x ) + \frac { \beta } { 2 } \| x - x _ { k } \| ^ { 2 } } \\ { \displaystyle \quad \geq f ( x ) + \frac { \rho } { 2 } \| c ( x ) \| ^ { 2 } - \frac { \| \lambda _ { k } \| ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } - \frac { ( \rho - \rho _ { 0 } ) \| c ( x ) \| ^ { 2 } } { 2 } } \\ { \displaystyle \quad \geq f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } - \frac { 1 } { 2 ( \rho - \rho _ { 0 } ) } \operatorname* { m a x } \left\{ \| \lambda _ { 0 } \| ^ { 2 } , \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { \sigma ^ { 2 } } \right\} } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \begin{array} { l } { { \displaystyle ( 3 2 ) } } \\ { { \displaystyle \geq } \ f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } - \operatorname* { m a x } \left\{ \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 ( \rho - \rho _ { 0 } ) } , 1 \right\} , } \end{array} } } \\ { { \medskip \displaystyle ( 2 ( \rho - \rho _ { \underline { { \theta } } } ) \geq \| \lambda _ { 0 } \| ^ { 2 } ) } \ f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } - 1 . } \end{array}
$$

The second inequality holds because $\| \lambda _ { k } \| \leq ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } / \sigma ^ { 2 } , \forall k \geq 1$ from Lemma 3. Then, for any $k \geq 0$ , we have by combining (49) and (50) that

$$
\psi _ { k } ( x _ { k } ) - \psi _ { k } ( x ) \leq \hat { \alpha } - \left( f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } \right) .
$$

Thus, for any $k \geq 0$ , we have

$$
\psi _ { k } ( x ) \leq \psi _ { k } ( x _ { k } ) \implies \psi _ { k } ( x _ { k } ) - \psi _ { k } ( x ) \geq 0 \ \overset { \mathrm { ( 5 1 ) } } { \Longrightarrow } \ f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } \leq \hat { \alpha } .
$$

Therefore $\{ x \mid \psi _ { k } ( x ) \leq \psi _ { k } ( x _ { k } ) \} \subseteq S _ { \hat { \alpha } } ^ { 0 }$ for all $k \geq 0$ . For the claim (47), note that

$$
\begin{array} { r l r } {  { \psi _ { k } ( x _ { k } ) - \psi _ { k } ^ { l o w } = \operatorname* { s u p } _ { x \in \mathbb { R } ^ { n } } ( \psi _ { k } ( x _ { k } ) - \psi _ { k } ( x ) ) } } \\ & { } & { \overset { \mathrm { ( 5 1 ) } } { \leq } \operatorname* { s u p } _ { x \in \mathbb { R } ^ { n } } ( \hat { \alpha } - ( f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } ) ) \overset { \mathrm { ( 5 ) } } { = } \hat { \alpha } - \bar { L } . } \end{array}
$$

By Lemma 4, we know that if the Newton-CG method of [33] is used to minimize $\psi _ { k } ( x )$ at iteration $k$ of Algorithm 2, Assumption 4(a) is satisfied at the initial point $x _ { k }$ . It also shows that the amount $\psi _ { k } ( x )$ can decrease at iteration $k$ is uniformly bounded for any $k \geq 0$ . This is important in estimating iteration complexity of Newton-CG to solve the subproblem.

The following assumption is needed to prove complexity results about the Newton-CG method. Recall from definition (46) that

$$
\begin{array} { l } { \displaystyle \nabla ^ { 2 } \psi _ { k } ( \boldsymbol { x } ) } \\ { \displaystyle = \nabla ^ { 2 } f ( \boldsymbol { x } ) + \sum _ { i = 1 } ^ { m } [ \lambda _ { k } ] _ { i } \nabla ^ { 2 } c _ { i } ( \boldsymbol { x } ) + \rho \sum _ { i = 1 } ^ { m } c _ { i } ( \boldsymbol { x } ) \nabla ^ { 2 } c _ { i } ( \boldsymbol { x } ) + \rho \nabla c ( \boldsymbol { x } ) \nabla c ( \boldsymbol { x } ) ^ { T } + \beta I . } \end{array}
$$

Assumption 5 (a) There exists a bounded open convex neighborhood $\mathcal { N } _ { \hat { \alpha } }$ of $S _ { \hat { \alpha } } ^ { 0 }$ , where $\hat { \alpha }$ is defined as in (18), such that for any $k \geq 0$ ˆ , the trial points of Newton-CG in iteration $k$ of Algorithm 2 lie in $\mathcal { N } _ { \hat { \alpha } }$ . Suppose that on $\mathcal { N } _ { \hat { \alpha } }$ , the functions $f ( x )$ and $c _ { i } ( x ) , i = 1 , 2 , \ldots , m$ are twice uniformly Lipschitz continuously differentiable.

(b) Given $\epsilon _ { k + 1 } ^ { H } > 0$ and $0 < \delta \ll 1$ at iteration $k \geq 0$ , the procedure called by Newton-CG + to verify sufficient positive definiteness of $\nabla ^ { 2 } \psi _ { k }$ either certifies that $\nabla ^ { 2 } \psi _ { k } ( x ) \succeq - \epsilon _ { k + 1 } ^ { H } I$ or else finds a vector of curvature smaller than $- \epsilon _ { k + 1 } ^ { H } / 2$ in at most

$$
N _ { \mathrm { m e o } } \triangleq \operatorname* { m i n } \{ n , 1 + \lceil \mathcal { C } _ { \mathrm { m e o } } ( \epsilon _ { k + 1 } ^ { H } ) ^ { - 1 / 2 } \rceil \}
$$

Hessian-vector products, with probability $1 - \delta$ , where $\mathcal { C } _ { \mathrm { m e o } }$ depends at most logarithmically on $\delta$ and $\epsilon _ { k + 1 } ^ { H }$ .

Boundedness and convexity of $\mathcal { N } _ { \hat { \alpha } }$ and Assumption 5(a) imply that $\nabla ^ { 2 } \psi _ { k } ( x )$ is Lipschitz continuous on $\mathcal { N } _ { \hat { \alpha } }$ . Thus, Assumption 4(b) holds for each subproblem. Further, if we denote the Lipschitz constant for $\nabla ^ { 2 } \psi _ { k }$ by $L _ { k , H }$ , then there exist $U _ { 1 }$ and $U _ { 2 }$ such that

$$
L _ { k , H } \leq U _ { 1 } \rho + U _ { 2 } , 
$$

where $U _ { 1 }$ and $U _ { 2 }$ depend only on $f$ and $c$ , $\mathcal { N } _ { \hat { \alpha } }$ , and the upper bound for $\| \lambda _ { k } \|$ from Lemma 3.   
Moreover, if $c ( x )$ is linear, then $L _ { k , H } = L _ { H }$ , where $L _ { H }$ is the Lipschitz constant for $\nabla ^ { 2 } f$ .

The next theorem analyzes the total iteration complexity, given the parameter settings in Theorem 2 (with some additional requirements).

Theorem 4 Consider Algorithm 2 with stopping criterion (31), and suppose that the subproblem in Step $^ { l }$ is solved with the Newton-CG procedure such that $x _ { k + 1 }$ satisfies (6), (7) and with high probability satisfies (40). Suppose that Assumptions 1, 2 with $\boldsymbol { S } = \boldsymbol { S } _ { \hat { \alpha } } ^ { 0 }$ (with $\hat { \alpha }$ defined in (18)), Assumptions 3 and 5 hold. $\epsilon \in ( 0 , 1 ]$ and $\eta \in [ 1 , 2 ]$ ˆ are given. In addition, let $\| \tilde { r } _ { k } \| \le \epsilon _ { k } ^ { g } \triangleq \operatorname* { m i n } \{ 1 / k , \epsilon / 2 \}$ , for all $k \geq 1$ (so that $\begin{array} { r } { R = \sum _ { k = 1 } ^ { \infty } 1 / k ^ { 2 } = \pi ^ { 2 } / 6 , } \end{array}$ ). Let $\beta = \epsilon ^ { \eta } / 2$ and assume that $\rho \in [ \rho _ { \eta } , C _ { \rho } \rho _ { \eta } ]$ , where $C _ { \rho } > 1$ is constant and

$$
\begin{array} { l } { \displaystyle \rho _ { \eta } : = \operatorname* { m a x } \left\{ \frac { 1 6 \operatorname* { m a x } \{ C _ { 1 } , C _ { 2 } \} } { \epsilon ^ { \eta } } , \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } } + \rho _ { 0 } , \right. } \\ { \displaystyle \left. \frac { \| \lambda _ { 0 } \| ^ { 2 } } { 2 } + \rho _ { 0 } , \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \sigma ^ { 4 } } , 3 \rho _ { 0 } , 1 \right\} , } \end{array}
$$

where $C _ { 1 }$ and $C _ { 2 }$ are defined in (11) and $D _ { S }$ is the diameter of $S _ { \hat { \alpha } } ^ { 0 }$ (see (20)). Suppose that $x _ { 0 }$ satisfies $\| c ( x _ { 0 } ) \| ^ { 2 } \leq \operatorname* { m i n } \{ C _ { 0 } / \rho , 1 \}$ , where $C _ { 0 }$ is the constant appearing in (18). Then we have the following.

(i) If we set $\epsilon _ { k } ^ { H } \equiv \sqrt { \epsilon } / 2$ , then the total number of iterations of Newton-CG before Algorithm 2 stops and outputs an $\epsilon$ -1o solution is $\mathcal { O } ( \epsilon ^ { - 2 \eta - 7 / 2 } )$ , which is optimized when $\eta = 1$ . When $c ( x )$ is linear, this total iteration complexity is $\mathcal { O } ( \epsilon ^ { \eta - 7 / 2 } )$ , which is optimized when $\eta = 2$ .   
(ii) If we let $\epsilon _ { k } ^ { H } \equiv \epsilon / 2$ , then the total iteration number before Algorithm 2 stops and outputs an $\epsilon$ -1o solution with probability 1 and an $\epsilon$ -2o solution with probability at least $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ is $\mathcal { O } ( \epsilon ^ { - 2 \eta - 5 } )$ , and $\bar { K } _ { T _ { \epsilon } } = \mathcal { O } ( \epsilon ^ { - 3 \eta - 3 } )$ , where $T _ { \epsilon }$ is defined in (30a) and $\bar { K } _ { T _ { \epsilon } }$ is the iteration complexity at iteration $T _ { \epsilon } - 1$ , defined below in (56). This bound is optimized when $\eta = 1$ . When $c ( x )$ is linear, this complexity is $\mathcal { O } ( \epsilon ^ { \eta - 5 } )$ , and $\bar { K } _ { T _ { \epsilon } } = \mathcal { O } ( \epsilon ^ { - 3 } )$ , so the optimal setting for $\eta$ is $\eta = 2$ in this case.

Proof We first prove (i). Note that if we use $x _ { k }$ as the initial point for Newton-CG at iteration $k$ , then (7) will be automatically satisfied because Newton-CG decreases the objective $\psi _ { k }$ at each iteration. Due to Lemma 4 and Assumption 5, we know that Assumption 4 is satisfied for each subproblem. Thus, at iteration $k$ , according to Theorem 3, given positive tolerances $\epsilon _ { g } = \epsilon _ { k + 1 } ^ { g }$ and $\epsilon _ { H } = \epsilon _ { k + 1 } ^ { H }$ , Newton-CG will terminate at a point $x _ { k + 1 }$ that satisfies (6) such that $\| \tilde { r } _ { k + 1 } \| \le \epsilon _ { k + 1 } ^ { g }$ with probability 1, and that satisfies (40) with probability $( 1 - \delta ) ^ { \bar { K } _ { k + 1 } }$ , within

$$
\begin{array} { r l } & { \bar { K } _ { k + 1 } } \\ & { \triangleq \bigg \lceil C _ { \mathrm { N C G } } \operatorname* { m a x } \{ L _ { k , H } ^ { 3 } , 1 \} ( \psi _ { k } ( x _ { k } ) - \psi _ { k } ^ { l o w } ) \operatorname* { m a x } \{ ( \epsilon _ { k + 1 } ^ { g } ) ^ { - 3 } ( \epsilon _ { k + 1 } ^ { H } ) ^ { 3 } , ( \epsilon _ { k + 1 } ^ { H } ) ^ { - 3 } \} \bigg \rceil + 2 . } \end{array}
$$

iterations, where $L _ { k , H }$ is the Lipschitz constant for $\nabla ^ { 2 } \psi _ { k } ( x )$ . By substituting (47) from Lemma 4 into (56), we obtain

$$
\begin{array} { r } { \bar { K } _ { k + 1 } \leq \Big \lceil C _ { \mathrm { N C G } } \operatorname* { m a x } \{ L _ { k , H } ^ { 3 } , 1 \} ( \hat { \alpha } - \bar { L } ) \operatorname* { m a x } \{ ( \epsilon _ { k + 1 } ^ { g } ) ^ { - 3 } ( \epsilon _ { k + 1 } ^ { H } ) ^ { 3 } , ( \epsilon _ { k + 1 } ^ { H } ) ^ { - 3 } \} \Big \rceil + 2 , } \end{array}
$$

for any $k \geq 0$ . From (54) and the conditions on $\rho$ , we have

$$
L _ { k , H } \le U _ { 1 } \rho + U _ { 2 } = \mathcal { O } ( \epsilon ^ { - \eta } ) ,
$$

where $U _ { 1 }$ and $U _ { 2 }$ depend only on $f$ and $c , { \mathcal { N } } _ { \hat { \alpha } }$ , and the upper bound for $\| \lambda _ { k } \|$ from Lemma 3.   
When $c ( x )$ is linear, we have $L _ { k , H } \equiv L _ { H }$ .

Since $\| \tilde { r } _ { k } \| \le \epsilon _ { k } ^ { g } = \operatorname* { m i n } \{ 1 / k , \epsilon / 2 \}$ for all $k \geq 1$ , the definition of $T _ { \epsilon }$ in (30a) and the result of Theorem 2 imply that $T _ { \epsilon } = \mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ . Therefore, for any $k \leq T _ { \epsilon }$ and $\eta \in [ 1 , 2 ]$ , we have

$$
1 / k \geq 1 / T _ { \epsilon } = \Omega ( \epsilon ^ { 2 - \eta } ) \implies \epsilon _ { k } ^ { g } = \varOmega ( \epsilon ) \implies ( \epsilon _ { k } ^ { g } ) ^ { - 1 } = \mathcal { O } ( \epsilon ^ { - 1 } ) .
$$

Thus, when $\epsilon _ { k } ^ { H } \equiv \sqrt { \epsilon } / 2$ , the term involving $\epsilon _ { k + 1 } ^ { g }$ and $\epsilon _ { k + 1 } ^ { H }$ on the right-hand sides of (56) and (57) are $\mathcal { O } ( \epsilon ^ { - 3 / 2 } )$ . Therefore, we have from the bound for $\bar { K } _ { k }$ , the estimate (58), and $T _ { \epsilon } = \mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ that the total iteration complexity to obtain an $\epsilon$ -1o solution is

$$
\sum _ { k = 1 } ^ { T _ { \epsilon } } \bar { K } _ { k } = \sum _ { k = 1 } ^ { T _ { \epsilon } } \operatorname* { m a x } \{ L _ { k - 1 , H } ^ { 3 } , 1 \} \mathcal { O } ( \epsilon ^ { - 3 / 2 } ) = T _ { \epsilon } \mathcal { O } ( \epsilon ^ { - 3 \eta } ) \mathcal { O } ( \epsilon ^ { - 3 / 2 } ) = \mathcal { O } ( \epsilon ^ { - 2 \eta - 7 / 2 } ) .
$$

This bound is optimized when $\eta = 1$ . When $c ( x )$ is linear, we have from $L _ { k , H } = L _ { H } = \mathcal { O } ( 1 )$ that the complexity is

$$
\sum _ { k = 1 } ^ { T _ { \epsilon } } \bar { K } _ { k } = \sum _ { k = 1 } ^ { T _ { \epsilon } } \operatorname* { m a x } \{ L _ { H } ^ { 3 } , 1 \} \mathcal { O } ( \epsilon ^ { - 3 / 2 } ) = T _ { \epsilon } \mathcal { O } ( \epsilon ^ { - 3 / 2 } ) = \mathcal { O } ( \epsilon ^ { \eta - 7 / 2 } ) .
$$

This bound is optimized when $\eta = 2$ .

We turn now to (ii). Since Algorithm 2 stops at iteration $T _ { \epsilon } - 1$ , Newton-CG will stop at Since the point $\epsilon _ { T _ { \epsilon } } ^ { H } = \epsilon / 2$ $x _ { T _ { \epsilon } }$ satisfying (6) with probability 1 and (40) with probability at least , $\eta \in [ 1 , 2 ]$ , and $\beta = \epsilon ^ { \eta } / 2 \le \epsilon / 2$ − , the following conditions are satisfied $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ . with probability at least $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ :

$$
\begin{array} { r l r } {  { \nabla _ { x x } ^ { 2 } \mathcal { L } _ { \rho } ( x _ { T _ { \epsilon } } , \lambda _ { T _ { \epsilon } - 1 } ) \overset { ( 4 0 ) } { \leq } - ( \beta + \epsilon _ { T _ { \epsilon } } ^ { H } ) I \succeq - \epsilon I , } } \\ & { } & { \quad \implies \nabla ^ { 2 } f ( x _ { T _ { \epsilon } } ) + \displaystyle \sum _ { i = 1 } ^ { m } [ \lambda _ { T _ { \epsilon } } ] _ { i } \nabla ^ { 2 } c _ { i } ( x _ { T _ { \epsilon } } ) + \rho \nabla c ( x _ { T _ { \epsilon } } ) \nabla c ( x _ { T _ { \epsilon } } ) ^ { T } \succeq - \epsilon I , } \\ & { } & { \quad \implies d ^ { T } ( \nabla ^ { 2 } f ( x _ { T _ { \epsilon } } ) + \displaystyle \sum _ { i = 1 } ^ { m } [ \lambda _ { T _ { \epsilon } } ] _ { i } \nabla ^ { 2 } c _ { i } ( x _ { T _ { \epsilon } } ) ) d \geq - \epsilon \| d \| ^ { 2 } , } \\ & { } & { \quad \quad \mathrm { f o r ~ a n y ~ } d \in S ( x _ { T _ { \epsilon } } ) \triangleq \{ d \in \mathbb { R } ^ { n } \ | \ [ \nabla c ( x _ { T _ { \epsilon } } ) ] ^ { T } d = 0 \} , } \end{array}
$$

which matches condition (2b) of Definition 2. Therefore, $x _ { T _ { \epsilon } }$ is an $\epsilon$ -1o solution with probability 1 and an $\epsilon$ -2o solution with probability at least $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ . Since we have $( \epsilon _ { k } ^ { g } ) ^ { - 1 } = \mathcal { O } ( \epsilon ^ { - 1 } )$ for $k \leq T _ { \epsilon }$ as in (59), and $\epsilon _ { k } ^ { H } = \epsilon / 2$ , the term involving $\epsilon _ { k + 1 } ^ { g }$ and $\epsilon _ { k + 1 } ^ { H }$ on the right-hand side of (56) and (57) is $\mathcal { O } ( \epsilon ^ { - 3 } )$ . Recalling that $T _ { \epsilon } = \mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ , the total iteration complexity to obtain $x _ { T _ { \epsilon } }$

$$
\sum _ { k = 1 } ^ { T _ { \epsilon } } \bar { K } _ { k } \overset { ( 5 7 ) } { = } \sum _ { k = 1 } ^ { T _ { \epsilon } } \operatorname* { m a x } \{ L _ { k - 1 , H } ^ { 3 } , 1 \} \mathcal { O } ( \epsilon ^ { - 3 } ) \overset { ( 5 8 ) } { = } T _ { \epsilon } \mathcal { O } ( \epsilon ^ { - 3 \eta } ) \mathcal { O } ( \epsilon ^ { - 3 } ) = \mathcal { O } ( \epsilon ^ { - 2 \eta - 5 } ) .
$$

This bound is optimized when $\eta = 1 .$ . Note that

$$
\bar { K } _ { T _ { \epsilon } } \stackrel { ( 5 7 ) } { = } \operatorname * { m a x } \{ L _ { T _ { \epsilon } - 1 , H } ^ { 3 } , 1 \} { \mathcal O } ( \epsilon ^ { - 3 } ) \stackrel { ( 5 8 ) } { = } { \mathcal O } ( \epsilon ^ { - 3 \eta - 3 } ) .
$$

When $c ( x )$ is linear, $L _ { k , H } = L _ { H } = \mathcal { O } ( 1 )$ and the complexity to get $x _ { T _ { \epsilon } }$ is

$$
\sum _ { k = 1 } ^ { T _ { \epsilon } } \bar { K } _ { k } \stackrel { ( 5 7 ) } { = } \sum _ { k = 1 } ^ { T _ { \epsilon } } \operatorname* { m a x } \{ L _ { H } ^ { 3 } , 1 \} \mathcal { O } ( \epsilon ^ { - 3 } ) = T _ { \epsilon } \mathcal { O } ( \epsilon ^ { - 3 } ) = \mathcal { O } ( \epsilon ^ { \eta - 5 } ) ,
$$

which is optimized when $\eta = 2$ . Note that in this case

$$
\bar { K } _ { T _ { \epsilon } } \overset { ( 5 7 ) } { = } \operatorname* { m a x } \{ L _ { H } ^ { 3 } , 1 \} \mathcal { O } ( \epsilon ^ { - 3 } ) = \mathcal { O } ( \epsilon ^ { - 3 } ) .
$$

Remark 2 (i). A feasible point, if available, will satisfy $\| c ( x _ { 0 } ) \| ^ { 2 } \leq \operatorname* { m i n } \{ C _ { 0 } / \rho , 1 \}$ for all $\rho$ . Otherwise, a “Phase I” procedure may be applied to the problem of minimizing $\| c ( x ) \| ^ { 2 }$ . Since $\rho = \mathcal { O } ( \epsilon ^ { - \eta } )$ , we have that $C _ { 0 } / \rho = \varOmega ( \epsilon ^ { \eta } ) , \eta \in [ 1 , 2 ]$ . Thus the Newton-CG algorithm could be use to find an approximate first-order point $\bar { x }$ such that $\| \nabla _ { x } ( \| c ( x ) \| ^ { 2 } ) \ | _ { x = \bar { x } } \ \| =$ $\| 2 \nabla c ( \bar { x } ) c ( \bar { x } ) \| \leq \operatorname* { m i n } \{ \epsilon , \sqrt { C _ { 0 } / \rho } , 1 \} = \varOmega ( \epsilon ) .$ If $\lVert c ( \bar { x } ) \rVert \leq \operatorname* { m i n } \{ \sqrt { C _ { 0 } / \rho } , 1 \}$ , we can set $x _ { 0 } =$ $\bar { x }$ . Otherwise, $\| c ( \bar { x } ) \| > \operatorname* { m i n } \{ \sqrt { C _ { 0 } / \rho } , 1 \} = \varOmega ( \epsilon )$ , and we can terminate at the approximate infeasible critical point of $\| c ( x ) \| ^ { 2 }$ , as in [17]. When Assumption 4 holds for $F ( z ) = \| c ( z ) \| ^ { 2 }$ , Theorem 3 indicates that the iteration complexity of Newton-CG to find $\bar { x }$ is $\mathcal { O } ( \epsilon ^ { - 3 / 2 } )$ (where $\epsilon _ { g } = \operatorname* { m i n } \{ \epsilon , \sqrt { C _ { 0 } / \rho } , 1 \}$ , $\epsilon _ { H } = \sqrt { \epsilon _ { g } } )$ . Thus, the total iteration complexity of Proximal AL is not affected when we account for Phase 1.

(ii). Note that when $c ( x )$ is linear, the optimized total iteration complexity bounds to obtain $\epsilon$ -1o and $\epsilon { - } 2 0$ point are $\mathcal { O } ( \epsilon ^ { - 3 / 2 } )$ and $\bar { \mathcal { O } } ( \epsilon ^ { - 3 } )$ , respectively. These bounds match the best known ones in literature for linear constraints (see Table 1 and corresponding discussion in Sect. 1.2). When $c ( x )$ is nonlinear, the optimized total iteration complexity bounds to locate $\epsilon$ -1o and $\epsilon { - } 2 0$ point are $\mathcal { O } ( \epsilon ^ { - 1 1 / 2 } )$ and $\mathcal { O } ( \epsilon ^ { - 7 } )$ , respectively. These bound are not competitive with the evaluation complexity bounds derived for two-phase second-order methods in [16,18] (see Table 1). These methods require solving a cubic regularization subproblem or minimizing a nonconvex program to global optimality per evaluation, which are potentially expensive computational tasks. The Newton-CG algorithm used for our inner loop has standard iterative linear algebra subproblems, and is equipped with worst-case operation complexity guarantees. We take up the issue of total operation complexity next.

Recalling the formula for $\nabla ^ { 2 } \psi _ { k }$ in (52), we define a constant $U _ { H }$ such that

$$
\| \nabla ^ { 2 } \psi _ { k } ( x ) \| \leq U _ { H } , \forall k \geq 0 , \forall x \in S _ { \hat { \alpha } } .
$$

Since $f ( x )$ and $c _ { i } ( x )$ , $i = 1 , 2 , \ldots , m$ are twice continuously differentiable on a neighborhood $\mathcal { N } _ { \hat { \alpha } } \supseteq \mathcal { S } _ { \hat { \alpha } }$ (by Assumption 5), and $S _ { \hat { \alpha } }$ is compact and $\lambda _ { k }$ is upper bounded (by Lemma 3), then such a $U _ { H } > 0$ exists. Moreover, there exist quantities $\tilde { U } _ { 1 }$ , $\stackrel { \triangledown } { \tilde { U } } _ { 2 }$ such that

$$
U _ { H } \leq \tilde { U } _ { 1 } \rho + \tilde { U } _ { 2 } ,
$$

where $\tilde { U } _ { 1 }$ , $\tilde { U } _ { 2 }$ depend only $f ( \cdot ) , c ( \cdot ) , S _ { \hat { \alpha } } , \beta$ (which is bounded if equals to $\epsilon ^ { \eta } / 2$ for all $\epsilon \leq 1$ and $\eta \geq 0$ ), and the upper bound for $\| \lambda _ { k } \|$ in Lemma 3.

We conclude this section with the result concerning operation complexity of Algorithm 2 in which the subproblems are solved inexactly with Newton-CG.

Corollary 3 Suppose that the setup and assumptions of Theorem 4 are satisfied. $U _ { H }$ is a   
constion satisfying (60) and , respectively. Let $J ( \cdot , \cdot )$ $N _ { \mathrm { m e o } }$ are specified in Corollary 2 and Assump-denote the total iteration complexity for $5 ( b )$ $\bar { K } _ { \mathrm { t o t a l } } \ \triangleq \ \sum _ { k = 1 } ^ { T _ { \epsilon } } \bar { K } _ { k }$   
Algorithm 2 with Newton-CG applied to the subproblems, where $\bar { K } _ { k }$ is defined as in (56).   
Then the following claims are true.

(i) When $\epsilon _ { k } ^ { H } \equiv \sqrt { \epsilon } / 2$ , then the total number of Hessian-vector products before Algorithm 2 stops and outputs an $\epsilon$ -1o solution is bounded by

$$
\operatorname* { m a x } \{ 2 \operatorname* { m i n } \{ n , J ( U _ { H } , \sqrt { \epsilon } / 2 ) \} + 2 , N _ { \mathrm { m e o } } \} \bar { K } _ { \mathrm { t o t a l } } .
$$

For all n sufficiently large, this bound is $\tilde { \mathcal { O } } ( \epsilon ^ { - 5 \eta / 2 - 1 5 / 4 } )$ (which reduces to $\tilde { \mathcal { O } } ( \epsilon ^ { \eta / 2 - 1 5 / 4 } )$ when $c ( x )$ is linear).

(ii) If we let $\epsilon _ { k } ^ { H } \equiv \epsilon / 2$ , then the total number of Hessian-vector products before Algorithm 2 stops and outputs an $\epsilon$ -1o solution with probability 1 and $\epsilon { - } 2 o$ with probability at least $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ is bounded by

$$
\mathrm { m a x } \{ 2 \mathrm { m i n } \{ n , J ( U _ { H } , \epsilon / 2 ) \} + 2 , N _ { \mathrm { m e o } } \} \bar { K } _ { \mathrm { t o t a l } } .
$$

For all n sufficiently large, this bound is $\tilde { \mathcal { O } } ( \epsilon ^ { - 5 \eta / 2 - 1 1 / 2 } )$ (which reduces to $\tilde { \mathcal { O } } ( \epsilon ^ { \eta / 2 - 1 1 / 2 } )$ when $c ( x )$ is linear).

Proof Since $\{ \psi _ { k } ( x ) \ : \leq \ : \psi _ { k } ( x _ { k } ) \} \ : \subseteq \ : S _ { \hat { \alpha } } ^ { 0 }$ (Lemma 4), then $\| \nabla ^ { 2 } \psi _ { k } ( x ) \| \leq U _ { H }$ on $\{ \psi _ { k } ( x ) \ \leq$ $\psi _ { k } ( x _ { k } ) \}$ for each $k \geq 0$ ˆ . Therefore, from Corollary 2, to solve the subproblem in iteration $k - 1$ of Algorithm 2 (for $k \geq 1$ ), Newton-CG requires at most

$$
( \operatorname* { m a x } \{ 2 \sin \{ n , J ( U _ { H } , \epsilon _ { k } ^ { H } ) \} + 2 , N _ { \mathrm { m e o } } \} ) \bar { K } _ { k }
$$

Hessian-vector products, where $\bar { K } _ { k }$ is defined in (56), and $J ( \cdot , \cdot )$ is bounded as in (45). From the latter definition and the fact that $U _ { H } = \mathcal { O } ( \rho ) = \mathcal { O } ( \epsilon ^ { - \eta } )$ , we have for sufficiently large $n$ that

$$
\begin{array} { r } { J ( U _ { H } , \epsilon _ { k } ^ { H } ) \le \operatorname* { m i n } \left( n , \tilde { \mathcal { O } } ( ( U _ { H } / \epsilon _ { k } ^ { H } ) ^ { 1 / 2 } ) \right) = \tilde { \mathcal { O } } \left( ( \epsilon _ { k } ^ { H } ) ^ { - 1 / 2 } \epsilon ^ { - \eta / 2 } \right) . } \end{array}
$$

From (53), we have at iteration $k - 1$ , for sufficiently large $n$ , that

$$
N _ { \mathrm { m e o } } = \operatorname* { m i n } \left( n , \tilde { \mathcal { O } } ( ( \epsilon _ { k } ^ { H } ) ^ { - 1 / 2 } ) \right) = \tilde { \mathcal { O } } ( ( \epsilon _ { k } ^ { H } ) ^ { - 1 / 2 } ) .
$$

By noting that the bound in (63) dominates that of (64), we have from (62) that the number of Hessian-vector products needed at iteration $k - 1$ is bounded by

$$
\tilde { \mathcal { O } } \left( ( \epsilon _ { k } ^ { H } ) ^ { - 1 / 2 } \epsilon ^ { - \eta / 2 } \right) \bar { K } _ { k } .
$$

To prove (i), we have $\epsilon _ { k } ^ { H } = \sqrt { \epsilon } / 2$ , so by substituting into (65) and summing over $k =$ $1 , 2 , \ldots , T _ { \epsilon }$ , we obtain the following bound on the total number of Hessian-vector products before termination:

$$
\tilde { \mathcal { O } } ( \epsilon ^ { - \eta / 2 - 1 / 4 } ) \bar { K } _ { \mathrm { t o t a l } } ,
$$

where $\bar { K } _ { \mathrm { t o t a l } } = \mathcal { O } ( \epsilon ^ { - 2 \eta - 7 / 2 } )$ from Theorem 4(i). By substituting into (66), we prove the result. When $c ( x )$ is linear, we obtain the tighter bound by using the estimate $\bar { K } _ { \mathrm { t o t a l } } = \mathcal { O } ( \epsilon ^ { \eta - 7 / 2 } )$ that pertains to this case.

For (ii), we have from Theorem 4(ii) that $x _ { T _ { \epsilon } }$ is an $\epsilon$ -1o solution with probability 1 and an $\epsilon$ -2o solution with probability at least $( 1 - \delta ) ^ { \bar { K } _ { T _ { \epsilon } } }$ . By substituting $\epsilon _ { k } ^ { H } = \epsilon / 2$ into (65) and summing over $k = 1 , \dots , T _ { \epsilon }$ , we have that the total number of Hessian-vector products before termination is bounded by

$$
\tilde { \mathcal { O } } ( \epsilon ^ { - \eta / 2 - 1 / 2 } ) \bar { K } _ { \mathrm { t o t a l } } ,
$$

where $\bar { K } _ { \mathrm { t o t a l } } = \mathcal { O } ( \epsilon ^ { - 2 \eta - 5 } )$ from Theorem 4(ii), so the result is obtained by substituting into (67). When $c ( x )$ is linear, we obtain the tighter bound by using the estimate $\bar { K } _ { \mathrm { t o t a l } } = \mathcal { O } ( \epsilon ^ { \eta - 5 } )$ that pertains to this case. □

# 5 Determining $\pmb { \rho }$

Our results above on outer iteration complexity, total iteration complexity, and operation complexity for Algorithm 2 are derived under the assumption that $\rho$ is larger than a certain threshold. However, this threshold cannot be determined a priori without knowledge of many parameters related to the functions and the algorithm. In this section, we sketch a framework for determining a sufficiently large value of $\rho$ without knowledge of these parameters. This framework executes Algorithm 2 as an inner loop and increases $\rho$ by a constant multiple in an outer loop whenever convergence of Algorithm 2 has not been attained in a number of iterations set for this outer loop. The framework is specified as Algorithm 3. The next theorem

# Algorithm 3 Proximal AL with trial value of $\rho$

0. Choose initial multiplier $\varLambda _ { 0 }$ , positive sequences $\{ \rho _ { \tau } \} _ { \tau \geq 1 }$ and $\{ T _ { \tau } \} _ { \tau \geq 1 }$ ; set $\tau \gets 1$ .   
1. Call Algorithm 2 with $x _ { 0 } = z _ { \tau }$ , $\lambda _ { 0 } = \varLambda _ { 0 }$ , $\rho = \rho _ { \tau }$ and run Algorithm 2 for $T _ { \tau }$ number of iterations, or until the stopping criteria are satisfied.   
2. If the stopping criterion of Algorithm 2 are satisfied, STOP the entire algorithm and output solutions given by Algorithm 2; otherwise, $\tau  \tau + 1$ and return to Step 1.

shows that $\{ \rho _ { \tau } \} _ { \tau \geq 1 }$ and $\{ T _ { \tau } \} _ { \tau \geq 1 }$ can be defined as geometrically increasing sequences without any dependence on problem-related parameter, and that this choice of sequences leads to an iteration complexity for Algorithm 3 that matches that of Algorithm 2 (from Theorem 2) to within a logarithm factor.

Theorem 5 Suppose that all the assumptions and settings in Theorem 2 for Algorithm 2 hold except for the choice of $\rho$ . In particular, the values of $\epsilon \in ( 0 , 1 )$ , $\eta \in [ 0 , 2 ]$ , $\beta$ and $R$ are the same in each loop of Algorithm 3, and $z _ { \tau }$ satisfies $\| c ( z _ { \tau } ) \| ^ { 2 } \leq \operatorname* { m i n } \{ C _ { 0 } / \rho _ { \tau } , 1 \}$ , where $C _ { 0 }$ is the constant appearing in (18). Suppose that Algorithm 3 terminates when the conditions (31) are satisfied. For user-defined parameters $q > 1$ and $T _ { 0 } \in \mathbb { Z } _ { + + }$ , we define the sequences $\{ \rho _ { \tau } \} _ { \tau \geq 1 }$ and $\{ T _ { \tau } \} _ { \tau \geq 1 }$ as follows:

$$
\left\{ \begin{array} { l l } { \rho _ { \tau } = \operatorname* { m a x } \{ q ^ { \tau } \epsilon ^ { 2 - 2 \eta } , 1 \} , ~ T _ { \tau } = \lceil T _ { 0 } q ^ { \tau } \rceil + 1 , } & { i f \eta \in [ 0 , 1 ) , } \\ { \rho _ { \tau } = q ^ { \tau } , ~ T _ { \tau } = \lceil T _ { 0 } q ^ { \tau } \rceil + 1 , } & { i f \eta = 1 , } \\ { \rho _ { \tau } = q ^ { \tau } , ~ T _ { \tau } = \operatorname* { m a x } \{ \lceil T _ { 0 } q ^ { \tau } \epsilon ^ { 2 \eta - 2 } \rceil + 1 , T _ { 0 } \} , } & { i f \eta \in ( 1 , 2 ] . } \end{array} \right.
$$

Then Algorithm 3 stops within $\log _ { q } \left( { \epsilon } ^ { \operatorname* { m i n } \{ \eta - 2 , - \eta \} } \right) + \mathcal { O } ( 1 )$ iterations. The number of iterations of Algorithm 2 that are performed before Algorithm 3 stops is $\tilde { \mathcal { O } } ( \epsilon ^ { \eta - 2 } )$ .

Proof According to Theorem 2, at iteration $\tau$ , the stopping criterion must be satisfied within $T _ { \tau }$ number of iterations if $\rho$ satisfies (32) and $T _ { \tau }$ is greater than the upper bound for $T _ { \epsilon }$ estimated in Theorem 2 (see (39)). Therefore, Algorithm 3 is guaranteed to stop when $\rho _ { \tau }$ and $T _ { \tau }$ are large enough.

When $\eta \in ( 0 , 1 )$ , $\rho _ { \tau }$ will satisfy (32) if

$$
\begin{array} { r l r } { \left. { q ^ { \tau } \epsilon ^ { 2 - 2 \eta } \geq \operatorname* { m a x } \left\{ \frac { 1 6 \operatorname* { m a x } \{ C _ { 1 } , C _ { 2 } \} } { \epsilon ^ { \eta } } , \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } } + \rho _ { 0 } , \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \sigma ^ { 4 } } , 3 \rho _ { 0 } , 1 \right\} } } \\ & { } & { \Leftrightarrow \tau \geq \operatorname* { m a x } \left\{ \log _ { q } \left( 1 6 \operatorname* { m a x } \{ C _ { 1 } , C _ { 2 } \} \epsilon ^ { \eta - 2 } \right) , \right. } \\ & { } & { \log _ { q } \left( \operatorname* { m a x } \left\{ \frac { ( M _ { f } + \beta D _ { S } + 1 ) ^ { 2 } } { 2 \sigma ^ { 2 } } + \rho _ { 0 } , \frac { 1 6 ( M _ { c } ^ { 2 } + \sigma ^ { 2 } ) R } { \sigma ^ { 4 } } , 3 \rho _ { 0 } , 1 \right\} \epsilon ^ { 2 \eta - 2 } \right) \right\} } \end{array}
$$

$$
= \log _ { q } ( \epsilon ^ { \eta - 2 } ) + \mathcal { O } ( 1 ) .
$$

$T _ { \tau }$ will be larger than the upper bound for $T _ { \epsilon }$ , that is, $\lceil \hat { \varDelta } \epsilon ^ { \eta - 2 } \rceil + 1$ (for $\hat { \varDelta }$ defined in (37b)) if

$$
\begin{array} { r } { T _ { 0 } q ^ { \tau } \geq \hat { \Delta } \epsilon ^ { \eta - 2 } \Leftrightarrow \tau \geq \log _ { q } \left( \hat { \Delta } \epsilon ^ { \eta - 2 } / T _ { 0 } \right) = \log _ { q } ( \epsilon ^ { \eta - 2 } ) + \mathcal { O } ( 1 ) . } \end{array}
$$

Therefore, Algorithm 3 will stop in $\log _ { q } ( \epsilon ^ { \eta - 2 } ) + \mathcal { O } ( 1 )$ number of iterations. Note that $\rho _ { \tau } ~ = ~ \mathcal { O } ( \epsilon ^ { - \eta } )$ , $T _ { \tau } ~ = ~ \mathcal { O } ( \epsilon ^ { \eta - 2 } )$ for any $\tau$ before the algorithm stops. Therefore the total number of iteration of Algorithm 2 is $\bar { \mathcal { O } } ( \epsilon ^ { \eta - 2 } )$ . The same result holds when $\eta \in [ 1 , 2 ]$ and the proof is similar (thus omitted). □

Remark 3 In Theorem 5, we almost recover the iteration complexity of Algorithm 2 derived in Theorem 2, except for a factor of $\log ( 1 / \epsilon )$ . The iteration complexity required to obtain $\epsilon { - } 2 0$ (Corollary 1) is immediate by Algorithm 3 if Step 1 of Algorithm 2 satisfies (40). To recover the iteration complexity of subproblem solver (Newton-CG) derived in Theorem 4, we could use similar approach by setting a limit on the iteration of Newton-CG and increasing this limit geometrically with respect to $\tau$ . The approach and analysis are quite similar to that presented above, so we omit the details.

# 6 Conclusion

We have analyzed complexity of a Proximal AL algorithm to solve smooth nonlinear optimization problems with nonlinear equality constraints. Three types of complexity are discussed: outer iteration complexity, total iteration complexity and operation complexity. In particular, we showed that if the first-order (second-order) stationary point is computed inexactly in each subproblem, then the algorithm outputs an $\epsilon$ -1o $\epsilon$ -2o) solution within $\mathcal { O } ( 1 / \epsilon ^ { 2 - \eta } )$ outer iterations $\beta = \mathcal { O } ( \epsilon ^ { \eta } )$ , $\rho = \varOmega ( 1 / \epsilon ^ { \eta } )$ ; $\eta \in [ 0 , 2 ]$ for first-order case and $\eta \in [ 1 , 2 ]$ for second-order case). We also investigate total iteration complexity and operation complexity when the Newton-CG method of [33] is used to solve the subproblems. A framework for determining the appropriate value of algorithmic parameter $\rho$ is presented, and we show that the iteration complexity increases by only a logarithmic factor for this approach by comparison with the version in which $\rho$ is known in advance.

There are several possible extensions of this work. First, we may consider a framework in which $\rho$ is varied within Algorithm 2. Second, extensions to nonconvex optimization problems with nonlinear inequality constraints remain to be studied.

Acknowledgements Research supported by Award N660011824020 from the DARPA Lagrange Program, NSF Awards 1628384, 1634597, and 1740707; and Subcontract 8F-30039 from Argonne National Laboratory.

# Appendix: Proofs of Elementary Results

Proof of Theorem 1 Since $x ^ { * }$ is a local minimizer of (1), it is the unique global solution of

$$
\operatorname* { m i n } { f ( x ) } + \frac { 1 } { 4 } \| x - x ^ { * } \| ^ { 4 } \mathrm {  ~ \ s u b j e c t { ~ t o ~ } } c ( x ) = 0 , \| x - x ^ { * } \| \leq \delta ,
$$

for $\delta > 0$ sufficiently small. For the same $\delta$ , we define $x _ { k }$ to be the global solution of

$$
\operatorname* { m i n } \quad f ( x ) + { \frac { \rho _ { k } } { 2 } } \| c ( x ) \| ^ { 2 } + { \frac { 1 } { 4 } } \| x - x ^ { * } \| ^ { 4 } \quad { \mathrm { s u b j e c t ~ t o } } \quad \| x - x ^ { * } \| \leq \delta ,
$$

for a given $\rho _ { k }$ , where $\{ \rho _ { k } \} _ { k \ge 1 }$ is a positive sequence such that $\rho _ { k } \to + \infty$ . Note that $x _ { k }$ is well defined because the feasible region is compact and the objective is continuous. Suppose that $z$ is any accumulation point of $\{ x _ { k } \} _ { k \geq 1 }$ , that is, $x _ { k } \to z$ for $k \in \mathcal { K }$ , for some subsequence $\kappa$ . Such a $z$ exists because $\{ x _ { k } \} _ { k \geq 1 }$ lies in a compact set, and moreover, $\| z - x ^ { * } \| \leq \delta$ . We want to show that $z = x ^ { * }$ . By the definition of $x _ { k }$ , we have for any $k \geq 1$ that

$$
\begin{array} { l } { f ( { \boldsymbol x } ^ { * } ) = f ( { \boldsymbol x } ^ { * } ) + \displaystyle \frac { \rho _ { k } } { 2 } \| { \boldsymbol c } ( { \boldsymbol x } ^ { * } ) \| ^ { 2 } + \displaystyle \frac { 1 } { 4 } \| { \boldsymbol x } ^ { * } - { \boldsymbol x } ^ { * } \| ^ { 4 } } \\ { \ge f ( x _ { k } ) + \displaystyle \frac { \rho _ { k } } { 2 } \| { \boldsymbol c } ( x _ { k } ) \| ^ { 2 } + \displaystyle \frac { 1 } { 4 } \| x _ { k } - { \boldsymbol x } ^ { * } \| ^ { 4 } \ge f ( x _ { k } ) + \displaystyle \frac { 1 } { 4 } \| x _ { k } - { \boldsymbol x } ^ { * } \| ^ { 4 } . } \end{array}
$$

By taking the limit over $\kappa$ , we have $\begin{array} { r } { f ( x ^ { * } ) \geq f ( z ) + \frac { 1 } { 4 } \| z - x ^ { * } \| ^ { 4 } } \end{array}$ . From (70), we have

$$
{ \frac { \rho _ { k } } { 2 } } \| c ( x _ { k } ) \| ^ { 2 } \leq f ( x ^ { * } ) - f ( x _ { k } ) \leq f ( x ^ { * } ) - \operatorname* { i n f } _ { k \geq 1 } f ( x _ { k } ) < + \infty .
$$

By taking limits over $\kappa$ , we have that $c ( z ) = 0$ . Therefore, $z$ is the global solution of (68), so that $z = x ^ { * }$ .

Without loss of generality, suppose that $x _ { k } \ \to \ x ^ { * }$ and $\| x _ { k } - x ^ { * } \| < \delta$ . By first and second-order optimality conditions for (69), we have

$$
\begin{array} { c l } { \displaystyle \nabla f ( { \boldsymbol x } _ { k } ) + \rho _ { k } \nabla c ( { \boldsymbol x } _ { k } ) c ( { \boldsymbol x } _ { k } ) + \| { \boldsymbol x } _ { k } - { \boldsymbol x } ^ { * } \| ^ { 2 } ( { \boldsymbol x } _ { k } - { \boldsymbol x } ^ { * } ) = 0 , } \\ { \displaystyle \nabla ^ { 2 } f ( { \boldsymbol x } _ { k } ) + \rho _ { k } \sum _ { i = 1 } ^ { m } c _ { i } ( { \boldsymbol x } _ { k } ) \nabla ^ { 2 } c _ { i } ( { \boldsymbol x } _ { k } ) + \rho _ { k } \nabla c ( { \boldsymbol x } _ { k } ) [ \nabla c ( { \boldsymbol x } _ { k } ) ] ^ { T } } \\ { + 2 ( { \boldsymbol x } _ { k } - { \boldsymbol x } ^ { * } ) ( { \boldsymbol x } _ { k } - { \boldsymbol x } ^ { * } ) ^ { T } + \| { \boldsymbol x } _ { k } - { \boldsymbol x } ^ { * } \| ^ { 2 } I \geq 0 . } \end{array}
$$

Define $\lambda _ { k } \triangleq \rho _ { k } c ( x _ { k } )$ an $\begin{array} { r } { { 1 } \epsilon _ { k } \triangleq \operatorname* { m a x } \{ \| x _ { k } - x ^ { * } \| ^ { 3 } , 3 \| x _ { k } - x ^ { * } \| ^ { 2 } , \sqrt { 2 ( f ( x ^ { * } ) - \operatorname* { i n f } _ { k \geq 1 } f ( x _ { k } ) ) } } \end{array}$ Then by (71), (72), (73) and Definition 2, $x _ { k }$ is $\epsilon _ { k }$ -2o. Note that $x _ { k } \to x ^ { * }$ and $\rho _ { k }  + \infty$ , so $\epsilon _ { k } \to 0 ^ { + }$ . □

Proof of Lemma 1 We prove by contradiction. Otherwise for any $\alpha$ we could select sequence $\{ x _ { k } \} _ { k \ge 1 } \subseteq S _ { \alpha } ^ { 0 }$ such that $f ( x _ { k } ) + { \textstyle \frac { \rho _ { 0 } } { 2 } } \| c ( x _ { k } ) \| ^ { 2 } < - k$ . Let $x ^ { * }$ be an accumulation point of $\{ x _ { k } \} _ { k \geq 1 }$ (which exists by compactness of $S _ { \alpha } ^ { 0 }$ ). Then there exists index $K$ such that $f ( x ^ { * } ) +$ $\begin{array} { r } { \frac { \rho _ { 0 } } { 2 } \| c ( x ^ { * } ) \| ^ { 2 } \geq - K + 1 > f ( x _ { k } ) + \frac { \rho _ { 0 } } { 2 } \| c ( x _ { k } ) \| ^ { 2 } + 1 } \end{array}$ for all $k \geq K$ , which contradicts the continuity of $\begin{array} { r } { f ( x ) + \frac { \rho _ { 0 } } { 2 } \| c ( x ) \| ^ { 2 } } \end{array}$ . □

# References

1. Andreani, R., Birgin, E.G., Martínez, J.M., Schuverdt, M.L.: On augmented Lagrangian methods with general lower-level constraints. SIAM J. Optim. 18(4), 1286–1309 (2008). https://doi.org/10.1137/ 060654797   
2. Andreani, R., Birgin, E.G., Martínez, J.M., Schuverdt, M.L.: Second-order negative-curvature methods for box-constrained and general constrained optimization. Comput. Optim. Appl. 45(2), 209–236 (2010). https://doi.org/10.1007/s10589-009-9240-y   
3. Andreani, R., Fazzio, N., Schuverdt, M., Secchin, L.: A sequential optimality condition related to the quasi-normality constraint qualification and its algorithmic consequences. SIAM J. Optim. 29(1), 743– 766 (2019). https://doi.org/10.1137/17M1147330   
4. Andreani, R., Haeser, G., Ramos, A., Silva, P.J.S.: A second-order sequential optimality condition associated to the convergence of optimization algorithms. IMA J. Numer. Anal. 37(4), 1902–1929 (2017)   
5. Andreani, R., Martínez, J.M., Ramos, A., Silva, P.J.S.: A cone-continuity constraint qualification and algorithmic consequences. SIAM J. Optim. 26(1), 96–110 (2016). https://doi.org/10.1137/15M1008488 6. Andreani, R., Secchin, L., Silva, P.: Convergence properties of a second order augmented Lagrangian method for mathematical programs with complementarity constraints. SIAM J. Optim. 28(3), 2574–2600 (2018). https://doi.org/10.1137/17M1125698 7. Bertsekas, D.P.: Constrained Optimization and Lagrange Multiplier Methods. Academic Press, Cambridge (2014)   
8. Bian, W., Chen, X., Ye, Y.: Complexity analysis of interior point algorithms for non-Lipschitz and nonconvex minimization. Math. Program. 149(1), 301–327 (2015). https://doi.org/10.1007/s10107-014-0753- 5   
9. Birgin, E.G., Floudas, C.A., Martínez, J.M.: Global minimization using an augmented Lagrangian method with variable lower-level constraints. Math. Program. 125(1), 139–162 (2010). https://doi.org/10.1007/ s10107-009-0264-y   
10. Birgin, E.G., Gardenghi, J., Martínez, J.M., Santos, S.A., Toint, P.L.: Worst-case evaluation complexity for unconstrained nonlinear optimization using high-order regularized models. Math. Program. 163(1–2), 359–368 (2017)   
11. Birgin, E.G., Haeser, G., Ramos, A.: Augmented Lagrangians with constrained subproblems and convergence to second-order stationary points. Comput. Optim. Appl. 69(1), 51–75 (2018). https://doi.org/10. 1007/s10589-017-9937-2   
12. Birgin, E.G., Martínez, J.M.: Complexity and performance of an augmented Lagrangian algorithm. Optim. Methods Softw. (2020). https://doi.org/10.1080/10556788.2020.1746962   
13. Boyd, S., Parikh, N., Chu, E., Peleato, B., Eckstein, J.: Distributed optimization and statistical learning via the alternating direction method of multipliers. Found. Trends Mach. Learn. 3(1), 1–122 (2011). https:// doi.org/10.1561/2200000016   
14. Cartis, C., Gould, N., Toint, P.: On the evaluation complexity of composite function minimization with applications to nonconvex nonlinear programming. SIAM J. Optim. 21(4), 1721–1739 (2011)   
15. Cartis, C., Gould, N., Toint, P.: Complexity bounds for second-order optimality in unconstrained optimization. J. Complex. 28(1), 93–108 (2012)   
16. Cartis, C., Gould, N.I.M., Toint, P.L.: On the evaluation complexity of cubic regularization methods for potentially rank-deficient nonlinear least-squares problems and its relevance to constrained nonlinear optimization. SIAM J. Optim. 23(3), 1553–1574 (2013). https://doi.org/10.1137/120869687   
17. Cartis, C., Gould, N.I.M., Toint, P.L.: On the complexity of finding first-order critical points in constrained nonlinear optimization. Math. Program. Ser. A 144, 93–106 (2014)   
18. Cartis, C., Gould, N.I.M., Toint, P.L.: Optimization of orders one to three and beyond: characterization and evaluation complexity in constrained nonconvex optimization. J. Complex. 53, 68–94 (2019)   
19. Curtis, F.E., Jiang, H., Robinson, D.P.: An adaptive augmented Lagrangian method for large-scale constrained optimization. Math. Program. 152(1), 201–245 (2015). https://doi.org/10.1007/s10107-014- 0784-y   
20. Ghadimi, S., Lan, G.: Accelerated gradient methods for nonconvex nonlinear and stochastic programming. Math. Program. 156(1), 59–99 (2016). https://doi.org/10.1007/s10107-015-0871-8   
21. Grapiglia, G.N., Nesterov, Y.: Regularized Newton methods for minimizing functions with Hölder continuous Hessians. SIAM J. Optim. 27(1), 478–506 (2017). https://doi.org/10.1137/16M1087801   
22. Grapiglia, G.N., Yuan, Y.X.: On the complexity of an augmented Lagrangian method for nonconvex optimization. arXiv e-prints arXiv:1906.05622 (2019)   
23. Haeser, G., Liu, H., Ye, Y.: Optimality condition and complexity analysis for linearly-constrained optimization without differentiability on the boundary. Math. Program. (2018). https://doi.org/10.1007/ s10107-018-1290-4   
24. Hajinezhad, D., Hong, M.: Perturbed proximal primal-dual algorithm for nonconvex nonsmooth optimization. Math. Program. (2019). https://doi.org/10.1007/s10107-019-01365-4   
25. Hestenes, M.R.: Multiplier and gradient methods. J. Optim. Theory Appl. 4(5), 303–320 (1969). https:// doi.org/10.1007/BF00927673   
26. Hong, M., Hajinezhad, D., Zhao, M.M.: Prox-PDA: The proximal primal-dual algorithm for fast distributed nonconvex optimization and learning over networks. In: D. Precup, Y.W. Teh (eds.) Proceedings of the 34th International Conference on Machine Learning, Proceedings of Machine Learning Research, vol. 70, pp. 1529–1538. PMLR (2017). http://proceedings.mlr.press/v70/hong17a.html   
27. Jiang, B., Lin, T., Ma, S., Zhang, S.: Structured nonconvex and nonsmooth optimization: algorithms and iteration complexity analysis. Comput. Optim. Appl. 72(1), 115–157 (2019). https://doi.org/10.1007/ s10589-018-0034-y   
28. Liu, K., Li, Q., Wang, H., Tang, G.: Spherical principal component analysis. In: Proceedings of the 2019 SIAM International Conference on Data Mining, pp. 387–395 (2019). https://doi.org/10.1137/1. 9781611975673.44   
29. Nouiehed, M., Lee, J.D., Razaviyayn, M.: Convergence to second-order stationarity for constrained nonconvex optimization. arXiv e-prints arXiv:1810.02024 (2018)   
30. O’Neill, M., Wright, S.J.: A log-barrier Newton-CG method for bound constrained optimization with complexity guarantees. IMA J. Numer. Anal. (2020). https://doi.org/10.1093/imanum/drz074   
31. Powell, M.J.D.: A method for nonlinear constraints in minimization problems. In: Optimization (Sympos., Univ. Keele, Keele, 1968), pp. 283–298. Academic Press, London (1969)   
32. Rockafellar, R.T.: Augmented Lagrangians and applications of the proximal point algorithm in convex programming. Math. Oper. Res. 1(2), 97–116 (1976). https://doi.org/10.1287/moor.1.2.97   
33. Royer, C.W., O’Neill, M., Wright, S.J.: A Newton-CG algorithm with complexity guarantees for smooth unconstrained optimization. Math. Program. (2019)   
34. Sun, J., Qu, Q., Wright, J.: Complete dictionary recovery over the sphere. In: 2015 International Conference on Sampling Theory and Applications (SampTA), pp. 407–410 (2015)   
35. Zhang, J., Luo, Z.Q.: A proximal alternating direction method of multiplier for linearly constrained nonconvex minimization. SIAM J. Optim. 30(3), 2272–2302 (2020). https://doi.org/10.1137/19M1242276