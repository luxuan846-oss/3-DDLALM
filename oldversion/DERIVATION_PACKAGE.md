# Derivation Package

## Target
修正当前 `contrained_format.tex` 中从**等式约束版** Perturbed ALM 过渡到**不等式约束版**时的理论对象，尤其是：
- 乘子更新
- 增广拉格朗日项
- `x` 步中的约束梯度项
- KKT 残差与可行性度量

## Status
COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

当前稿件的问题不是“只差把一个更新式改成投影”。
真正的问题是：**问题定义已经是 equality + inequality，但 KKT、方法和证明主体仍然是 equality-only 版本。**

## Invariant Object
统一对象应当是**分块的 reduced augmented Lagrangian**：
- 等式块：保留你现在的 perturbed ALM 结构
- 不等式块：使用 **nonnegative multiplier maximization** 或等价的 **positive-part reduced AL term**

也就是说，不能继续把所有约束都写成一个无符号的 `\bc(\bx)=0`。

## Assumptions
- \(f\) 可微且随机梯度可得。
- \(\bc_{\calE}\) 与 \(\bc_{\calI}\) 连续可微。
- 不等式乘子满足非负性：\(\blmbd_{\calI} \ge 0\), \(\bmu_{\calI} \ge 0\).
- 若采用
  \[
  \bmu_{\calI}^{k+1} = \bmu_{\calI}^k + \theta_k(\blmbd_{\calI}^k - \bmu_{\calI}^k),
  \]
  则初始化需要 \(\bmu_{\calI}^0 \ge 0\)，这样非负性由凸组合保持。

## Notation
- \(\bc_{\calE}(\bx) \in \RR^{m_E}\): equality constraints
- \(\bc_{\calI}(\bx) \in \RR^{m_I}\): inequality constraints
- \((\blmbd_{\calE}, \bmu_{\calE}) \in \RR^{m_E}\): equality dual variables
- \((\blmbd_{\calI}, \bmu_{\calI}) \in \RR_+^{m_I}\): inequality dual variables
- \([v]_+\): componentwise positive part, i.e. \(([v]_+)_i = \max\{v_i,0\}\)

## Derivation Strategy
先把 equality / inequality 两类约束彻底拆开，再分别写 reduced object。

- 等式块继续沿用你当前的 perturbed ALM
- 不等式块不能用
  \[
  \blmbd^{k+1} = \bmu^{k+1} + \rho \bc(\bx^{k+1})
  \]
  这种**无约束仿射更新**
- 不等式块必须改成**投影后的 dual maximizer**

## Derivation Map
1. 先修正 KKT：不等式必须有 dual feasibility 和 complementarity。
2. 再修正 AL：不等式块不能继续用 equality penalty 形式。
3. 再修正 `x` 步：约束梯度项必须对应新的 inequality reduced term。
4. 最后修正 proof：可行性度量要从 \(\|\bc(\bx)\|^2\) 改成 \(\|[\bc_{\calI}(\bx)]_+\|^2\)。

## Main Derivation
### Step 1. 正确的 KKT 条件
对于
\[
\min_{\bx\in\calX}\ f(\bx)+g(\bx)
\quad\text{s.t.}\quad
\bc_{\calE}(\bx)=0,\qquad \bc_{\calI}(\bx)\le 0,
\]
KKT 条件应写成
\[
\mathbf 0 \in \nabla f(\bx^*) + \partial g(\bx^*)
+ J_{\bc_{\calE}}(\bx^*)^\top \blmbd_{\calE}^*
+ J_{\bc_{\calI}}(\bx^*)^\top \blmbd_{\calI}^*
+ \mathcal N_{\calX}(\bx^*),
\]
\[
\bc_{\calE}(\bx^*) = 0,\qquad
\bc_{\calI}(\bx^*) \le 0,\qquad
\blmbd_{\calI}^* \ge 0,\qquad
\blmbd_{\calI}^* \odot \bc_{\calI}(\bx^*) = 0.
\]

这一步说明：**当前稿件里把 KKT 写成 `\bc(\bx^*)=0` 是根本不对的。**

### Step 2. 等式块保持原结构
等式块可以继续保留你当前写法：
\[
\mathcal L_{\rho_E}^{\calE}(\bx,\blmbd_{\calE},\bmu_{\calE})
=
f(\bx)+g(\bx)
+ \langle \blmbd_{\calE}, \bc_{\calE}(\bx)\rangle
+ \frac{\rho_E}{2}\|\bc_{\calE}(\bx)\|^2
- \frac{1}{2\rho_E}\|\blmbd_{\calE}-\bmu_{\calE}\|^2.
\]
对应更新仍可写成
\[
\blmbd_{\calE}^{k+1} = \bmu_{\calE}^{k+1} + \rho_E \bc_{\calE}(\bx^{k+1}).
\]

### Step 3. 不等式块必须改成 projected dual maximizer
对不等式块，固定 \((\bx,\bmu_{\calI})\) 后，考虑
\[
\psi_{\rho_I}^{\calI}(\bx,\blmbd_{\calI},\bmu_{\calI})
:=
\langle \blmbd_{\calI}, \bc_{\calI}(\bx)\rangle
- \frac{1}{2\rho_I}\|\blmbd_{\calI}-\bmu_{\calI}\|^2,
\qquad \blmbd_{\calI}\ge 0.
\]

对 \(\blmbd_{\calI}\) 做最大化，有闭式解
\[
\blmbd_{\calI}^*(\bx,\bmu_{\calI})
=
\arg\max_{\blmbd_{\calI}\ge 0}
\psi_{\rho_I}^{\calI}(\bx,\blmbd_{\calI},\bmu_{\calI})
=
\big[\bmu_{\calI} + \rho_I \bc_{\calI}(\bx)\big]_+.
\]

因此**不等式乘子更新**应改成
\[
\boxed{
\blmbd_{\calI}^{k+1}
=
\big[\bmu_{\calI}^{k+1} + \rho_I \bc_{\calI}(\bx^{k+1})\big]_+
}
\]
而不是
\[
\blmbd^{k+1} = \bmu^{k+1} + \rho \bc(\bx^{k+1}).
\]

这就是当前算法里最直接的错误。

### Step 4. 不等式块的 reduced AL 项
把 \(\blmbd_{\calI}\) 消掉以后，得到标准的 positive-part reduced term：
\[
\phi_{\rho_I}^{\calI}(\bx,\bmu_{\calI})
=
\frac{1}{2\rho_I}
\left(
\big\|[\bmu_{\calI} + \rho_I \bc_{\calI}(\bx)]_+\big\|^2
- \|\bmu_{\calI}\|^2
\right).
\]

所以总的 reduced object 应该写成
\[
\mathcal L_\rho(\bx,\blmbd_{\calE},\bmu_{\calE},\bmu_{\calI})
=
f(\bx)+g(\bx)
+ \langle \blmbd_{\calE}, \bc_{\calE}(\bx)\rangle
+ \frac{\rho_E}{2}\|\bc_{\calE}(\bx)\|^2
- \frac{1}{2\rho_E}\|\blmbd_{\calE}-\bmu_{\calE}\|^2
+ \phi_{\rho_I}^{\calI}(\bx,\bmu_{\calI}).
\]

### Step 5. `x`-update 里的梯度项也必须变
当前稿件的 `x`-步使用的是
\[
J_{\bc}(\bx^k)^\top \big(\blmbd^k + \rho \bc(\bx^k)\big),
\]
这只对应 equality-only 版本。

若保留“等式块显式、 不等式块 reduced”这种写法，则应改成
\[
\tilde\nabla \psi_\rho(\bx^k)
=
\bd^k
+ J_{\bc_{\calE}}(\bx^k)^\top
\big(\blmbd_{\calE}^k + \rho_E \bc_{\calE}(\bx^k)\big)
+ J_{\bc_{\calI}}(\bx^k)^\top \blmbd_{\calI}^k,
\]
其中
\[
\blmbd_{\calI}^k = [\bmu_{\calI}^k + \rho_I \bc_{\calI}(\bx^k)]_+.
\]

所以 **不等式块在 `x`-步里不是 `\lambda_I + \rho c_I`，而是直接 `\lambda_I`**。

### Step 6. `\mu`-update 可以保留同型，但要分块
等式块：
\[
\bmu_{\calE}^{k+1}
=
\bmu_{\calE}^k + \theta_k^{\calE}(\blmbd_{\calE}^k - \bmu_{\calE}^k).
\]

不等式块可对应写成
\[
\bmu_{\calI}^{k+1}
=
\bmu_{\calI}^k + \theta_k^{\calI}(\blmbd_{\calI}^k - \bmu_{\calI}^k),
\qquad \bmu_{\calI}^0 \ge 0.
\]

因为 \(\blmbd_{\calI}^k,\bmu_{\calI}^k \ge 0\)，若 \(\theta_k^{\calI}\in[0,1]\)，则 \(\bmu_{\calI}^{k+1}\ge 0\) 自动成立。

### Step 7. 可行性残差必须换
当前稿件里大量使用
\[
\|\bc(\bx^{k+1})\|^2
\]
来衡量可行性，这只适合 equality。

对不等式，正确的 primal violation 应改成
\[
\|\bc_{\calE}(\bx)\|^2 + \|[\bc_{\calI}(\bx)]_+\|^2.
\]

并且原来等式版的恒等式
\[
\blmbd^{k+1} - \bmu^{k+1} = \rho\,\bc(\bx^{k+1})
\]
不再成立。

不等式块只能得到
\[
\blmbd_{\calI}^{k+1}
=
[\bmu_{\calI}^{k+1} + \rho_I \bc_{\calI}(\bx^{k+1})]_+,
\]
从而仅有分量级估计
\[
[\,\bc_{\calI}(\bx^{k+1})\,]_+
\le
\frac{1}{\rho_I}
\big|\blmbd_{\calI}^{k+1} - \bmu_{\calI}^{k+1}\big|,
\]
以及
\[
\|[\bc_{\calI}(\bx^{k+1})]_+\|^2
\le
\frac{1}{\rho_I^2}
\|\blmbd_{\calI}^{k+1} - \bmu_{\calI}^{k+1}\|^2.
\]

所以 proof 里原来基于
\[
\|r_{k+1}\|^2 = \rho^2 \|\bc(\bx^{k+1})\|^2
\]
的部分，都要重写成对 \(\|[\bc_{\calI}(\bx^{k+1})]_+\|^2\) 的控制。

## Remarks and Interpretation
- **最小必须修改的地方**不是一个，而是四个：
  1. KKT
  2. reduced AL
  3. `x`-步约束梯度项
  4. dual update / feasibility proof

- 如果你现在只把问题写成 `\bc_{\calI}(\bx)\le 0`，但算法仍然保留
  \[
  \blmbd^{k+1}=\bmu^{k+1}+\rho \bc(\bx^{k+1}),
  \]
  那么算法会允许 \(\blmbd_{\calI}^{k+1}<0\)，这直接违反 dual feasibility。

- 当前草稿中“只改得不多”的根本原因是：你实际上还没有把方法从 equality-only 切换成 mixed-constraint 版本。

## Boundaries and Non-Claims
- 这个修正包只给出**一致的算法对象与公式结构**。
- 还没有把主文中的 descent lemma、smoothness 常数、KKT residual lemma 全部重写。
- 如果要继续推进理论证明，下一步必须把所有 `\bc` / `J_{\bc}` / `\blmbd` 的地方都拆成 `(\calE,\calI)` 两块，并把 violation bound 改为
  \[
  \frac1T\sum_{k=0}^{T-1}\EE\!\left[\|\bc_{\calE}(\bx^{k+1})\|^2 + \|[\bc_{\calI}(\bx^{k+1})]_+\|^2\right].
  \]
