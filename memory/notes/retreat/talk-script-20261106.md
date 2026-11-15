# Retreat Talk Script (Vienna, Nov 6, 2026)

Slides: `notes/retreat/slides/retreat_talk.tex` (15 numbered pages). Total time: about 20 minutes, followed by 5 minutes of questions.

In each pair, the English line is what you say and the Chinese line is its meaning. `[click]` marks a slide advance inside a page. Lines marked **(key)** carry the argument, so slow down there.

---

## 0. Framework and time allocation

| Part | Pages | Time | Weight | One-sentence message |
|---|---|---|---|---|
| Opening | Title, Outline | 0:40 | light | Four parts, one question |
| I. Problem and large penalty | 1–4 | 5:00 | p4 heavy | $\rho$ controls feasibility and stepsize in opposite directions, so existing ALMs take $\rho\sim\epsilon^{-1}$ |
| II. Linearized ALM as GDA | 5–8 | 5:30 | p5, p8 heavy | For fixed $\rho$, Problem (P) is a minimax problem; GDA methods face the same tension with $s$ |
| III. Lower bounds | 9–13 | 6:00 | p11, p13 heavy | Only $\rho+s$ matters for accuracy; $\rho+s$ must reach $\epsilon^{-1}$, but it can sit on $s$ |
| IV. Open questions | 14–15 | 3:00 | medium | Gap between $\epsilon^{-3}$ and $\epsilon^{-2}$; two settings for acceleration |

Logic chain: $\rho$ (page 4) → $s$ (page 7) → both together (page 8, Research Question) → $\rho+s$ (page 11) → answer (page 13) → beyond the family (pages 14–15).

---

## 1. Symbol reading guide

| Symbol | Read as |
|---|---|
| $\mathcal{O}(\epsilon^{-3})$ | big O of epsilon to the minus three |
| $\Theta(1)$ | big Theta of one |
| $\Omega(\epsilon^{-4})$ | big Omega of epsilon to the minus four |
| $\epsilon^{-5/2}$ | epsilon to the minus five halves |
| $\rho$, $\lambda$, $\mu$, $\eta$, $\kappa$ | rho, lambda, mu, eta, kappa |
| $L_{\mathbf{x}}(\rho)$ | L x of rho, the smoothness constant in x |
| $\kappa(s)=\ell s$ | kappa of s equals ell times s |
| $\nabla_{\mathbf{x}}\mathcal{D}_\rho$ | the gradient of D rho with respect to x |
| $\mathrm{prox}_{h/\rho}$ | the proximal operator of h over rho |
| $M_h^{1/\rho}$ | the Moreau envelope of h with parameter one over rho |
| $\lVert\mathcal{A}(\mathbf{x})-\mathbf{y}\rVert\le 2L_h/\rho$ | the norm of A of x minus y is at most two L h over rho |
| $\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}$ | min over x, max over lambda |
| $\lambda^{k+1}$ | lambda k plus one |
| $\rho+s\le c_1/\epsilon$ | rho plus s is at most c one over epsilon |
| $\mathcal{C}_\theta$ | the family C theta |
| $\tfrac{1}{s}$-strongly concave | one over s strongly concave |
| $s_k\to\infty$ | s k goes to infinity |
| $\epsilon$-KKT point | epsilon KKT point |

---

## 2. Script

### Title page (0:25)

Good morning, everyone. Thank you for the invitation.
大家早上好，感谢邀请。

My name is Luxuan Li, and I am from Beihang University.
我是北京航空航天大学的李路轩。

Today I will talk about augmented Lagrangian methods with a fixed penalty.
今天我讲罚参数有界的增广拉格朗日方法。

This is joint work with Kangkang Deng, Chunfeng Cui, and Jiang Hu.
这是和邓康康、崔春风、胡江老师的合作工作。

### Outline (0:15)

The talk has four parts.
报告分四部分。

First, the problem and existing ALMs. Second, a minimax view of the linearized ALM.
第一部分是问题和已有的 ALM，第二部分从 minimax 的角度看 linearized ALM。

Third, our lower bounds. Finally, some open questions on acceleration.
第三部分是我们的下界，最后是关于加速的开放问题。

### Page 1: Problem (1:00)

We consider a composite problem: minimize f of x plus h of A of x.
我们考虑复合问题：最小化 f(x) 加 h(A(x))。

Here f is smooth, A is a smooth map, and h is convex and Lipschitz.
f 光滑，A 是光滑映射，h 凸且 Lipschitz。

We also assume that the proximal operator of h is easy to compute.
我们还假设 h 的近端算子容易计算。

Here are two examples.
举两个例子。

In spectral risk learning, h is a weighted sum of sorted losses.
在 spectral risk 学习中，h 是排序后损失的加权和。

In worst-group retraining, h is the maximum over group losses.
在 worst-group retraining 中，h 是各组损失的最大值。

Our question is about complexity.
我们关心的是复杂度。

Given epsilon, how many iterations does a first-order method need to find an epsilon-KKT point?
给定 epsilon，一阶方法需要多少次迭代才能找到 epsilon-KKT 点？

### Page 2: Handling the nonsmooth composition (0:50)

The main difficulty is the composition.
主要困难在于复合结构。

The prox of h is easy, but the prox of h composed with A is not.
h 的近端算子好算，但 h 复合 A 的近端算子不好算。

There are four common approaches.
常见的处理方法有四类。

Subgradient methods, prox-linear methods, variable smoothing, and primal-dual methods.
次梯度法、prox-linear 方法、变量光滑化和原始对偶方法。

Today we follow the last one.
今天我们走最后一条路。

We introduce y equals A of x, and we access h only through its prox.
引入 y 等于 A(x)，只通过近端算子调用 h。

### Page 3: Linearized ALM (1:30)

After splitting, we get a problem with an equality constraint.
分裂之后，得到一个带等式约束的问题。

Its augmented Lagrangian has a penalty term with parameter rho.
它的增广拉格朗日函数里有一个罚项，罚参数是 rho。

The linearized ALM is a single-loop method.
linearized ALM 是单环方法。

Each iteration takes one gradient step in x, one prox step in y, and one multiplier step in lambda.
每一步做一次 x 的梯度步、一次 y 的近端步、一次乘子更新。

The x-step uses a stepsize eta, which is at most one over L x of rho.
x 步的步长 eta 不超过 L_x(rho) 分之一。

We measure accuracy by the KKT residual.
我们用 KKT 残差衡量精度。

It has two parts: stationarity, and feasibility, which is the norm of A of x minus y.
它有两部分：平稳性，以及可行性，也就是 A(x) 减 y 的范数。

Please keep feasibility in mind. It drives the rest of the talk.
请记住可行性这一项，后面的内容都围绕它展开。

### Page 4: Existing nonconvex ALMs, large penalty (2:00) (key)

Table 1 lists existing nonconvex ALMs.
表 1 列出了已有的非凸 ALM。

All of them use a large penalty: either increasing, or of order one over epsilon.
它们都用大罚参数：要么递增，要么是 epsilon 分之一的阶。

Why is the penalty large? Let us look at the first formula.
为什么罚参数大？看第一个公式。

In Problem P, the multipliers are bounded by L h, because h is L h Lipschitz.
在问题 (P) 中，因为 h 是 L_h-Lipschitz 的，乘子的范数不超过 L_h。

So feasibility is at most two L h over rho.
所以可行性不超过 2L_h 除以 rho。

To make feasibility below epsilon, we take rho of order one over epsilon.
为了让可行性小于 epsilon，取 rho 为 epsilon 分之一的阶。

However, rho also enters the stepsize.
但是 rho 也影响步长。

The smoothness constant L x of rho grows linearly in rho.
光滑常数 L_x(rho) 随 rho 线性增长。

So the iteration count is L x of rho times Delta over epsilon squared.
所以迭代次数是 L_x(rho) 乘以 Delta 除以 epsilon 平方。

With rho of order one over epsilon, this gives epsilon to the minus three.
rho 取 epsilon 分之一的阶，结果就是 epsilon 的负三次方。

In short, rho controls accuracy and stepsize in opposite directions.
简单说，rho 对精度和步长的作用方向相反。

We call a single-loop ALM with rho of order one a fixed-penalty linearized ALM.
我们把 rho 为常数阶的单环 ALM 称为 fixed-penalty linearized ALM。

Our first question is this: can a fixed-penalty linearized ALM still reach epsilon to the minus three?
第一个问题是：fixed-penalty linearized ALM 还能达到 epsilon 的负三次方吗？

With a fixed penalty, feasibility has to come from somewhere else. To see where, we take a minimax view.
罚参数有界时，可行性要从别处来。为了看清楚，我们换成 minimax 的视角。

### Outline (0:05)

Now, part two.
下面进入第二部分。

### Page 5: Problem (P) as a minimax problem (1:30) (key)

First, we minimize the augmented Lagrangian over y in closed form.
首先，对 y 显式地最小化增广拉格朗日函数。

This gives the reduced augmented Lagrangian D rho, which depends only on x and lambda.
得到约化增广拉格朗日函数 D_rho，它只依赖 x 和 lambda。

Its maximum over lambda is exactly F. So Problem P is equivalent to a minimax problem: min over x, max over lambda of D rho.
它对 lambda 取最大值正好是 F，所以问题 (P) 等价于对 D_rho 的 min-max 问题。

Moreover, the two gradients of D rho are exactly the two KKT residuals.
而且，D_rho 的两个梯度正好就是 KKT 残差的两部分。

The x-gradient is stationarity, and the lambda-gradient is feasibility.
对 x 的梯度对应平稳性，对 lambda 的梯度对应可行性。

So an epsilon-game stationary point of the minimax problem gives an epsilon-KKT point.
所以 minimax 问题的 epsilon 博弈平稳点给出 epsilon-KKT 点。

[click] Therefore, for every fixed rho, Problem P is a smooth nonconvex–concave minimax problem.
[翻页] 因此，对任意固定的 rho，问题 (P) 是一个光滑的非凸-凹 minimax 问题。

### Page 6: Linearized ALM as GDA (1:00)

Now let us look at the algorithm.
现在看算法。

Once we eliminate y, the linearized ALM is exactly gradient descent–ascent on D rho.
消去 y 之后，linearized ALM 就是在 D_rho 上做梯度下降-上升，也就是 GDA。

The primal stepsize is eta, and the dual stepsize is the penalty rho.
原始步长是 eta，对偶步长就是罚参数 rho。

So we can borrow tools from minimax optimization.
所以我们可以借用 minimax 优化的工具。

For smooth nonconvex–concave problems, plain GDA needs epsilon to the minus six iterations.
对光滑非凸-凹问题，普通 GDA 需要 epsilon 负六次方次迭代。

To accelerate, single-loop methods add two regularizations.
为了加速，单环方法加入两种正则。

One is primal smoothing around a center z. The other is dual regularization around a center mu, with parameter s.
一种是围绕中心 z 的原始光滑，另一种是围绕中心 mu、参数为 s 的对偶正则。

### Page 7: Single-loop GDA-based methods (1:30)

Table 2 shows the effect of each tool.
表 2 展示每种工具的效果。

Plain GDA needs epsilon to the minus six. Moving the center z gives epsilon to the minus four.
普通 GDA 是负六次方，让中心 z 移动后是负四次方。

Adding dual regularization with one over s of order epsilon gives epsilon to the minus three.
再加上 s 分之一为 epsilon 阶的对偶正则，就到负三次方。

[click] Here we see the same tension as before, now for s.
[翻页] 这里出现了和前面相同的矛盾，这次是关于 s。

The regularization leaves a dual residual of order D Y over s.
正则化留下的对偶残差是 D_Y 除以 s 的阶。

To make it below epsilon, we take s of order one over epsilon.
为了让它小于 epsilon，取 s 为 epsilon 分之一的阶。

The cost appears in the condition number kappa of s, which equals ell times s.
代价体现在条件数 kappa(s) 上，它等于 ell 乘以 s。

The iteration count is kappa of s times ell Delta over epsilon squared. Again, this is epsilon to the minus three.
迭代次数是 kappa(s) 乘以 ell Delta 除以 epsilon 平方，同样是负三次方。

### Page 8: Research question (1:30) (key)

Let me put the two lines side by side.
把两条线并排放在一起看。

In the ALM, the x-step is limited by one over L x of rho. In GDA, the center step is limited by one over kappa of s.
ALM 里，x 步的步长受 L_x(rho) 分之一限制；GDA 里，中心步的步长受 kappa(s) 分之一限制。

In both lines, one parameter controls the dual part of stationarity. For the ALM it is rho, and for GDA it is s.
两条线里，都是一个参数控制平稳性的对偶部分：ALM 里是 rho，GDA 里是 s。

In both lines, the iteration count grows linearly in this parameter.
两条线里，迭代次数都随这个参数线性增长。

And in both lines, the parameter is of order one over epsilon, which gives epsilon to the minus three.
两条线里，这个参数都取 epsilon 分之一的阶，于是得到负三次方。

This leads to our research question.
由此引出我们的研究问题。

With a fixed penalty, can we also keep s of order one?
罚参数有界时，能否让 s 也保持常数阶？

In other words, can we avoid every parameter of order one over epsilon?
换句话说，能否完全不用 epsilon 分之一阶的参数？

### Outline (0:05)

Part three gives the answer.
第三部分给出答案。

### Page 9: The LRALM family (1:00)

To answer this, we study a family that contains both lines.
为了回答这个问题，我们研究一个同时包含两条线的算法族。

We call it the linearized regularized ALM, or LRALM.
我们称它为 linearized regularized ALM，简称 LRALM。

It takes gradient steps on the regularized function P s: descent in x and z, and ascent in lambda and mu.
它在正则化函数 P_s 上做梯度步：对 x 和 z 下降，对 lambda 和 mu 上升。

The two centers move with stepsizes alpha and beta, both between zero and one.
两个中心分别以步长 alpha 和 beta 移动，取值都在零到一之间。

The family C theta collects all choices of alpha and beta, with the other parameters fixed.
算法族 C_theta 包含 alpha、beta 的所有取法，其他参数固定。

### Page 10: Special cases (0:45)

Different choices of alpha and beta recover known methods.
不同的 alpha、beta 对应已知的方法。

Alpha and beta equal to one give the linearized ALM.
alpha 和 beta 都取一，就是 linearized ALM。

The other rows give smoothed GDA, DS-GDA, and perturbed smoothed GDA, applied to D rho.
其余几行是作用在 D_rho 上的 smoothed GDA、DS-GDA 和 perturbed smoothed GDA。

So a lower bound for this family covers all of them at once.
所以这个族的下界同时覆盖所有这些方法。

### Page 11: Combined penalty parameter (1:30) (key)

Here is the key structural fact.
这是关键的结构性质。

If we maximize P s over lambda, we get D with penalty rho plus s.
把 P_s 对 lambda 取最大，得到罚参数为 rho 加 s 的 D 函数。

So, for accuracy, the dual regularization acts as an extra penalty. Only the sum rho plus s matters.
所以就精度而言，对偶正则相当于额外的罚参数，起作用的只是 rho 加 s 这个和。

However, the primal smoothness depends on rho only.
但是，原始光滑常数只依赖 rho。

So a large s does not shrink the primal stepsize.
所以大的 s 不会缩小原始步长。

The cost of a large s appears elsewhere, through kappa of s, as we saw on page seven.
大 s 的代价出现在别处，即第七页的 kappa(s)。

### Page 12: Worst-case complexity and lower bound (1:30)

We measure the worst case over a problem class.
我们在一个问题类上衡量最坏情形。

The class fixes all smoothness and Lipschitz constants, and also the initial gap Delta.
这个类固定了所有光滑常数、Lipschitz 常数和初始间隙 Delta。

For the family, we take the best choice of alpha and beta, and then the worst instance.
对算法族，我们取最好的 alpha 和 beta，再取最坏的实例。

Theorem 1 says the following.
定理一的内容如下。

If rho plus s is at most c one over epsilon, then the family needs at least order epsilon to the minus four iterations.
如果 rho 加 s 不超过 c_1 除以 epsilon，算法族至少需要 epsilon 负四次方阶的迭代次数。

This holds uniformly in alpha and beta. So no choice of center stepsizes can help.
这个结论对 alpha 和 beta 一致成立，所以中心步长怎么选都没有用。

### Page 13: The critical order of rho plus s (1:30) (key)

This picture summarizes the answer. The horizontal axis is rho plus s.
这张图总结了答案，横轴是 rho 加 s。

In region one, rho plus s is below c one over epsilon.
在区域一，rho 加 s 小于 c_1 除以 epsilon。

Here the tight complexity is epsilon to the minus four, for every alpha and beta. It is attained at beta equal to one and alpha of order epsilon squared.
这里的紧复杂度是负四次方，对所有 alpha、beta 都成立，在 beta 等于一、alpha 为 epsilon 平方阶时达到。

At point two, rho is of order one and s is of order one over epsilon.
在点二，rho 是常数阶，s 是 epsilon 分之一阶。

Here the tight complexity is epsilon to the minus three. It is attained at beta equal to zero and alpha of order epsilon.
这里的紧复杂度是负三次方，在 beta 等于零、alpha 为 epsilon 阶时达到。

[click] So the answer has two parts.
[翻页] 所以答案分两部分。

First, no: rho and s cannot both be of order one.
第一，不能：rho 和 s 不能同时是常数阶。

Second, yes: we can keep rho bounded, and put the large parameter on s.
第二，可以：rho 保持有界，把大参数放在 s 上。

### Outline (0:05)

Finally, some open questions.
最后讲几个开放问题。

### Page 14: Open question, below epsilon to the minus three (1:30)

What is the optimal complexity of fixed-penalty linearized ALMs?
fixed-penalty linearized ALM 的最优复杂度是多少？

Inside the family, we know the answer: epsilon to the minus three. Outside the family, we do not know.
在算法族内，答案是负三次方；在族外，我们还不知道。

Two facts frame the question.
有两个已知事实给出了这个问题的范围。

First, any first-order method needs epsilon to the minus two, already for smooth problems.
第一，任何一阶方法至少需要负二次方，光滑问题就已经如此。

Second, for smooth nonconvex–concave minimax problems, the optimal game-stationarity complexity is epsilon to the minus five halves, and a single-loop method attains it.
第二，对光滑非凸-凹 minimax 问题，博弈平稳性的最优复杂度是负二分之五次方，并且有单环方法达到。

So the open range is between epsilon to the minus three and epsilon to the minus two.
所以开放的区间在负三次方和负二次方之间。

### Page 15: Acceleration beyond the family (1:30)

How can a fixed-penalty linearized ALM leave the family and go below epsilon to the minus three?
fixed-penalty linearized ALM 怎样才能跳出算法族，做到比负三次方更快？

A useful view is that the dual regularization is a Tikhonov term.
一个有用的视角是：对偶正则就是 Tikhonov 项。

It makes the dual problem one over s strongly concave.
它让对偶问题成为 s 分之一强凹。

This view suggests two settings.
这个视角给出两种情形。

In the first setting, the accuracy is fixed, and s is of order one over epsilon.
第一种情形，精度固定，s 是 epsilon 分之一阶。

In minimax optimization, a single-loop method with the same order of s reaches epsilon to the minus five halves.
在 minimax 优化中，用同阶的 s，单环方法达到了负二分之五次方。

So, which updates would do the same for a fixed-penalty linearized ALM?
那么，什么样的更新能让 fixed-penalty linearized ALM 也做到？

In the second setting, there is no fixed accuracy, and we let s k go to infinity.
第二种情形，没有固定的精度，让 s_k 趋于无穷。

For monotone problems, vanishing Tikhonov regularization gives strong convergence to the minimum-norm solution, with fast residual decay.
对单调问题，逐渐消失的 Tikhonov 正则给出到最小范数解的强收敛，残差衰减也快。

For a fixed-penalty linearized ALM, which multiplier do the iterates select, and how fast?
对 fixed-penalty linearized ALM，迭代点会选中哪个乘子，速度有多快？

I would be very happy to hear your thoughts on these questions.
很希望听到大家对这些问题的看法。

### Thank you (0:10)

Thank you for your attention. I am happy to take questions.
感谢大家，欢迎提问。

---

## 3. Questions and answers

### Q1. Your lower bound covers only your family. Could another method avoid a parameter of order one over epsilon?
你的下界只对你的算法族成立，别的方法能否不用 epsilon 分之一阶的参数？

That is right. Theorem 1 is a lower bound inside the family.
对，定理一是族内下界。

It is uniform in the center stepsizes alpha and beta, so the choice of centers cannot help.
它对中心步长 alpha 和 beta 一致成立，所以中心怎么选都没有用。

Outside the family, the only known lower bound is epsilon to the minus two, from Carmon et al.
族外目前已知的下界只有 Carmon 等人的负二次方。

Closing this gap is exactly our open question on page fourteen.
补上这段差距正是第十四页的开放问题。

### Q2. Is a large s just a large penalty in disguise?
大的 s 是不是换了个名字的大罚参数？

For accuracy, yes. Proposition 1 shows that only rho plus s matters.
就精度而言是的，命题一说明起作用的只是 rho 加 s。

For the primal step, no. The smoothness constant depends on rho only, so the x-subproblem stays well conditioned.
就原始步而言不是，光滑常数只依赖 rho，所以 x 子问题的条件数保持良好。

The cost moves to the dual side, through kappa of s.
代价转移到对偶一侧，体现在 kappa(s) 上。

This is useful, because the dual side is where Tikhonov and minimax tools act.
这一点有用，因为 Tikhonov 和 minimax 的工具正是作用在对偶一侧。

### Q3. Why do you measure epsilon-KKT points, and not stationarity of the Moreau envelope?
为什么用 epsilon-KKT 点，而不用 Moreau 包络的平稳性？

The epsilon-KKT residual is the natural measure for ALMs. It contains both stationarity and feasibility.
epsilon-KKT 残差是 ALM 的自然度量，它同时包含平稳性和可行性。

On page five, it equals the game stationarity of D rho.
第五页说明，它就等于 D_rho 的博弈平稳性。

So our results compare directly with game-stationarity results in minimax optimization.
所以我们的结果可以直接和 minimax 优化中的博弈平稳性结果对比。

### Q4. You assume h is Lipschitz. What about indicator functions, that is, hard constraints?
你假设 h 是 Lipschitz 的，那指示函数，也就是硬约束呢？

The Lipschitz constant bounds the multipliers by L h. This bound is used throughout.
Lipschitz 常数把乘子界在 L_h 以内，这个界贯穿整个分析。

For indicator functions, the multipliers are not bounded a priori.
对指示函数，乘子没有先验的界。

Then we need a constraint qualification to bound them. This extension is future work.
这时需要约束规范来控制乘子，这个推广是后续工作。

---

## 4. Practice plan for a first talk

1. Read the symbol table aloud twice. Most hesitation comes from symbols.
2. Learn the first and last sentence of each page by heart. These carry the logic between pages.
3. Slow down on the key pages: 4, 5, 8, 11, 13.
4. If you lose a sentence, read the box or the bold line on the slide, then continue.
5. Rehearse twice with a timer. The checkpoints are page 4 at 6 minutes, page 8 at 12 minutes, page 13 at 18 minutes.
