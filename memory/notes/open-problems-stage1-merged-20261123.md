# 非光滑非线性复合优化开放问题：阶段 1 调研的独立复核与合并稿

## 文档头元数据

- **日期**：2026-11-23
- **检索截止日**：2026-11-23。本稿沿用 GPT Pro 两份报告的截止日，本轮没有做新的文献检索。
- **参与模型与分工**：
  1. GPT Pro：撰写阶段 1 的两份调研报告。报告一覆盖大问题一（复杂度定位与下界），报告二覆盖大问题二（可达性、度量换算与 Goldstein 复杂度）。
  2. Codex（`gpt-6.2-sol`，reasoning effort high）：逐行审计 GPT Pro 的 9 项现场推导 `(a)–(i)`，并用 NumPy 做数值检验。
  3. Gemini 4 Neon（High）：全文核查 21 篇文献，补充 6 篇遗漏文献，并核对本稿 `overleaf/sections/Preliminaries.tex` 与用户 6 子问题定稿是否对齐。
  4. Claude（`claude-opus-5-5`，经 `claude-t3-valerie`）：负责独立复核与合并。原计划使用 `--model fable`，因 usage credits 不足，回退至 `claude-opus-5-5`。
- **输入文件**：`gptpro-and-outline-input.md`（GPT Pro 两份报告与用户 6 子问题定稿）、`memory/notes/open-problems-audit-codex-20261123.md`、`memory/notes/open-problems-audit-gemini-20261123.md`、`overleaf/sections/Preliminaries.tex`。
- **Claude 本轮直接核对的原文**：
  - `pzl_v2.txt`：Algorithm 1–3、Proposition 6.2 及其证明、Lemma B.1、Lemma 3.2、inner chain 定义式 (20)–(21)、§5.4 式 (30)、$R_1$ 定义式 (23)。
  - `Preliminaries.tex`：L25–102。
  - 项目笔记 `memory/notes/project/literature.md` 与 `memory/notes/project/lower-bound-references.md`：`2608.19847`、`2607.08954` 与 Tian–So 三个条目。
- **标签约定**：
  - `[已有文献定理]`：原文已证明的定理，原文设定与本线一致，或只差一个显然的嵌入。本稿自身的定理记为 `[已有文献定理·本稿]`。
  - `[已核验归约]`：GPT Pro 的现场推导，已经 Codex 逐行审计、在必要处经 Claude 复核，缺口已补齐。它仍属于本项目的推导，写入论文前需要给出完整证明，引用时不能署名为原文定理。
  - `[有条件成立]`：结论依赖一项尚未核完的条件。该条件随条目一并写明。
  - `[开放空白]`：截至检索截止日，没有检到匹配的上下界。这个标签记录的是检索结果，不构成"不存在"的证明。

---

## 一、Claude 独立复核与三方分歧裁定

### 1.0 总体裁定

1. **Codex 审计的 9 项推导全部成立。** 其中 `(d)` 的修复是必需的。"位精度对 $\kappa$ 指数依赖"这一表述来自一个充分条件，应降级为 `[有条件成立]`，不能写成算法的内在代价。
2. **PZL Algorithm 1 不查询函数值。** Claude 已对照 `pzl_v2.txt` 原文确认，依据见 1.3 节。
3. **本轮新确认两点，均来自 PZL v2 原文。**
   - 半球朝向由 PZL 的构造本身公开。因此 Codex `(b)` 指出的缺口 1 在 PZL 实例上自动满足。
   - 在本稿的完整 Jacobian oracle 下，$K=1$ GS 下界的模拟论证失效。在矩阵–向量积 oracle 下，该论证成立。
   - 后一点决定了「Fast LRALM 在 GS 下 $\epsilon$ 阶最优」能否写进论文。
4. **Gemini 关于 $G_f$ 的捕获成立。** 然而 $G_f$ 消除不了 `(d)` 中对偶初始函数值间隙无界的问题。消除 `(d)` 中有限差分步骤的条件是 oracle 提供 $J_{\mathcal{A}}\mathbf{w}$，与 $G_f$ 无关。
5. **Gemini 对 `2607.08954` 的复杂度与 oracle 层级描述，与项目已有笔记冲突。** 这一条目需要核对原文后才能定稿。

### 1.1 Codex 关键修复的复核

#### (d) $\mathcal{C}_\nu$ 上的 prox-linear 加对偶强凸 APG 上界

**裁定：`[已核验归约]`。Codex 的修复必需；有限差分的位精度表述降为 `[有条件成立]`。**

1. **四条不等式成立。** 本稿采纳 Codex 的显式见证残差定义。OS 界中的系数 $8$ 可收紧为 $2\sqrt{2}$。

2. **对偶初始函数值间隙可以无界，加入 $G_f$ 后仍然如此。** 记当前点的 $\mathbf{g}=\nabla f(\mathbf{x})$、$\mathbf{a}=\mathcal{A}(\mathbf{x})$ 与 Jacobian $J$。线性化子问题的对偶目标为

$$
\psi(\mathbf{q}) = h^\ast(\mathbf{q}) - \langle \mathbf{a},\mathbf{q}\rangle + \frac{1}{2R}\lVert \mathbf{g} + J^\top\mathbf{q}\rVert^2 .
$$

   Codex 的反例成立。Claude 另取满足 $G_f$ 的实例：$h(y)=\lvert y\rvert$、$\mathcal{A}(x)=x$、$f(x)=\cos(x)/2$。此时 $G_f$ 与 $L_f$ 都等于 $1/2$，$R=1/2$。当 $x \gt 3$ 时，对偶最优解为 $q^\star=1$，且

$$
\psi(0)-\psi(1) = x - \frac{2g+1}{2R} = x - 2g - 1 \to +\infty,\qquad g = -\frac{\sin x}{2}.
$$

   **机制**：间隙中含有 $-\langle \mathbf{a},\mathbf{q}\rangle$ 项。本问题类不限制 $\lVert\mathcal{A}(\mathbf{x})\rVert$ 的大小，并且 $h^\ast$ 在其有效域上可以无界。$G_f$ 对这两项都不起控制作用。因此，任何以函数值间隙启动的内层加速法都不可用，必须用距离型初始化。

3. **两种修复都成立。**
   - Codex 的距离型定时重启 FISTA 成立。
   - 另有一个更短的等价修复，Claude 推荐在写作中采用。先从 $\mathbf{q}_0 \in \operatorname{dom} h^\ast$ 出发，做一步步长为 $1/L$ 的近端梯度，得到 $\mathbf{q}_1$。由 Beck–Teboulle（SIIMS 2009）的标准不等式得

$$
\psi(\mathbf{q}_1) - \psi(\mathbf{q}^\star) \le \frac{L}{2}\lVert \mathbf{q}_0 - \mathbf{q}^\star\rVert^2 \le 2LL_h^2 .
$$

   之后接标准的强凸 APG。内层查询次数仍为 $O(\kappa\log(\cdot))$。

4. **有限差分精度。** Codex 给出 $\eta \le LD/(4\cdot 3^M)$。这个界来自逐步 Lipschitz 稳定性：FISTA 单步映射的 Lipschitz 常数不超过 $3$，连乘 $M$ 步得到 $3^M$。它是充分条件，但估计悲观。按 Devolder–Glineur–Nesterov（Math. Program. 2014）的非精确 oracle 框架，快速梯度法的误差随迭代数线性累积，因此 $\eta$ 取多项式小量很可能已经足够。这一判断是 Claude 的推断，常数尚未写出，记为 `[有条件成立]`。在精确实数查询模型下，查询次数不受影响。

5. **与 Gemini 的交叉裁定。**
   - Oracle 一旦提供 $J_{\mathcal{A}}\mathbf{w}$（新线推荐的设定），或提供完整 Jacobian（本稿设定），有限差分模拟就不再需要。
   - 距离型初始化在所有设定下都必须保留，原因见第 2 点。

6. **GS 全精度阈值。** 本稿采纳 Codex 的选取：$r = \min\{\epsilon/(8R), \sqrt{\epsilon/L_{\mathcal{A}}}\}$。

#### (b) 把 PZL 单批次（$K=1$）GS 下界迁入复合类

**裁定：`[已核验归约]`，oracle 层面附带条件。**

1. **Jacobian 的 Lipschitz 常数。** 界 $L_{\mathcal{A}}^{\mathrm{inst}} \le 4\ell/D_Y$ 成立，证明不需要三阶导数假设。

2. **缺口 1（半球朝向）在 PZL 实例上自动满足。**
   - 依据 PZL v2 §5.4 式 (30)，单批次的对偶域为 $\{(u,\mathbf{w}) : u \ge 0,\ \lVert(u,\mathbf{w})\rVert \le D/2\}$。
   - 依据 Lemma 3.2，旋转矩阵 $\operatorname{diag}(I_k, V)$ 只作用于 $(\mathbf{w},\boldsymbol{\eta})$ 块，不旋转 $c$ 块（此处即 $u$ 坐标）。
   - 因此半球朝向 $\mathbf{c}=\mathbf{e}_u$ 由问题类的构造固定，对算法公开，并且 $P_{\mathrm{aux}}\mathbf{c}=0$ 自动成立。
   - 模拟 $J_{\mathcal{A}}^\top\mathbf{v}$ 时，可按已知的 $\langle\mathbf{c},\mathbf{v}\rangle$ 符号取 $\pm\mathbf{v}$，使缩放后的查询点落在半球内。
   - Codex 给出的 $W_\beta$ 一般公式只在构造变体时需要，在本线中作为附注即可。
   - 原文写明辅助梯度为 $(0,-\ell\boldsymbol{\eta})$，可知辅助二次项系数为 $\ell/2$，与 GPT Pro 的写法一致。

3. **缺口 2：同意 Codex 的修正。** 应使用类常数链 $G_{\mathcal{A}}^{\mathrm{inst}} \le \ell_\ast \le L_f \le R$。

4. **缺口 3：同意 Codex。** 题设 GS 只要求见证点存在。若要求算法显式输出对偶点，额外代价为低阶项。

5. **Claude 新增：oracle 依赖性。** PZL 式 (21) 给出：当 $N \ge 2$ 时

$$
I_N(\mathbf{z},t;\mathbf{y}) = \left\langle D_N^\top\mathbf{z} - \frac{t}{\sqrt{N}}\mathbf{e}_N,\ \mathbf{y}\right\rangle ,
$$

   它对原始变量是仿射的。旋转后，$\mathcal{A}$ 分成两部分：一是标量行 $\mathcal{A}_u$，由 $P$ 与常数项构成，对原始变量非线性；二是其余各行，对 $\mathbf{x}$ 仿射。由此得到两个结论。
   - **矩阵–向量积 oracle：下界迁移成立，`[已核验归约]`。** $J_{\mathcal{A}}(\mathbf{x})\mathbf{w}$ 的 $u$ 分量等于 $\langle\nabla\mathcal{A}_u(\mathbf{x}),\mathbf{w}\rangle$，其余分量等于 $\mathcal{A}(\mathbf{x}+\mathbf{w})-\mathcal{A}(\mathbf{x})$ 的对应分量。两者都只需 $O(1)$ 次 saddle 查询。
   - **完整 Jacobian oracle：现有证明失效。** 仿射块是一个与 $\mathbf{x}$ 无关的常数矩阵，含旋转后的整条双线性链。一次完整 Jacobian 查询会揭示整条链，而对偶维数 $MN+1$ 随 $\epsilon$ 增长。因此 PZL 的证明不覆盖本稿 `def:oracle-model`。在本稿 oracle 下，$\Omega(\epsilon^{-5/2})$ 的迁移尚未建立。

6. **Claude 新增：与 $G_f$ 的相容性。** 在对偶原点处只剩状态正则项，所以 $f(\mathbf{x})=\sum_i R_1(s_i)$ 再乘以缩放。$R_1$ 由光滑 ReLU 型函数 $p$ 构成，$p'$ 取值于 $[0,1]$，所以未缩放时梯度有界。缩放后 $\sup\lVert\nabla f\rVert$ 是否与 $\epsilon$ 无关，需要按 PZL 的缩放常数写出。按 Carmon 型尺度推算，该量为 $O(\sqrt{\ell\Delta})$。记为 `[有条件成立]`。

#### (e) $\mathcal{C}_\nu$ 上一维精确 $\epsilon$-KKT 不可达

**裁定：`[已核验归约]`，适用范围比 GPT Pro 原文更宽。**

1. **严格不等号 $0 \lt \nu \lt G_{\mathcal{A}}$ 是必需的。** 在一维情形，若 $\nu = G_{\mathcal{A}}$，连续导数恒为常数，$\mathcal{A}$ 退化为仿射函数，一次查询即可求得零点。本稿采纳 Codex 补出的预算分配、保护点 $x_0$，以及无限 transcript 情形下直至 $j+2$ 阶导数的预算。
2. **Claude 扩展适用范围。** 每个 bump 的支撑避开所有已查询点，所以 $(f,\mathcal{A})$ 在已查询点处的任意阶导数保持不变。由此，下列每一种 oracle 在任意有限 transcript 上都无法区分构造中的实例，结论对它们全部成立：
   - 本稿 oracle：一维时完整 Jacobian 就是 $\mathcal{A}'(x)$，且 $f\equiv 0$；
   - 第 3 层 prox-linear 子问题 oracle：子问题由 $(\mathcal{A}(x),\mathcal{A}'(x))$ 与已知的 $h$ 决定；
   - 任何"回答只由查询点处有限阶 jet 与已知 $h$ 决定"的 oracle。

   用户定稿中「第 3 层可达性开放」一项因此关闭。

#### (f) 满行秩 ODE 流的严格性

**裁定：`[已核验归约]`。论证严格，且只需局部正则性。**

1. **记号与 Lipschitz 性。** 记 $J^+ := J^\top(JJ^\top)^{-1}$。在 $JJ^\top \succeq \nu^2 I_m$ 成立的区域上，$\lVert J^+\rVert \le 1/\nu$，并且 $J^+$ 是 Lipschitz 的：

$$
\lVert J^+(\mathbf{z}) - J^+(\mathbf{z}')\rVert \le \left(\frac{L_{\mathcal{A}}}{\nu^2} + \frac{2G_{\mathcal{A}}^2 L_{\mathcal{A}}}{\nu^4}\right)\lVert\mathbf{z}-\mathbf{z}'\rVert .
$$

2. **局部存在唯一。** 向量场 $-J^+(\mathbf{z})(\mathcal{A}(\mathbf{z})-\mathbf{y})$ 是 Lipschitz 有界算子与 Lipschitz 映射之积，因此局部 Lipschitz。由 Picard–Lindelöf 定理，解局部存在且唯一。
3. **残差与速度。** 由 $JJ^+ = I_m$ 得 $\mathcal{A}(X(s))-\mathbf{y} = e^{-s}(\mathcal{A}(\mathbf{x})-\mathbf{y})$。因此速度满足 $\lVert X'(s)\rVert \le e^{-s}\mu/\nu$，总弧长不超过 $\mu/\nu$。
4. **无爆破与极限点。** 由速度有界，极大解不会在有限时间爆破，所以全局存在。$X(s)$ 是 Cauchy 列，由连续性，其极限 $\mathbf{x}'$ 满足 $\mathcal{A}(\mathbf{x}')=\mathbf{y}$。
5. **局部版本。** 轨迹始终留在闭球 $B(\mathbf{x},\mu/\nu)$ 内。因此只需在该闭球的一个开邻域上有 $JJ^\top \succeq \nu^2 I_m$，再用标准的延拓论证即可。这给出局部正则性的一个可核验的量化版本，见第四节大问题二子问题二。
6. **文献定位。** 该结果是 Lyusternik–Graves 定理的定量形式（见 Dontchev–Rockafellar，*Implicit Functions and Solution Mappings*；定理编号待核）。
7. **后续 OS 界。** 再由 $\nabla F_\lambda$ 的 $2R$-Lipschitz 性得到 $2\eta + 4R\mu/\nu$，验算无误。

#### 其余四项

- **(c)：同意 Codex。** 全链非零要求每个次对角元非零。PZL 与 WGY 的 OS 三对角块是否满足这一条件，需对照式 (9)–(10) 与 WGY 式 (16)–(17) 确认，记为待补核项。
- **(g)：同意 Codex。** 两个平方根反例在固定类常数下成立。
- **(h)：同意 Codex。** 在含 $G_f$ 的本稿问题类中，"无需全局梯度界"这一附注不再必要，但仍然成立。
- **(i)：同意 Codex。** 该上界只计 oracle 调用次数，椭球法每步 $O(d^2)$ 的算术量不计入。

### 1.2 Gemini 文献与稿件对齐捕获的裁定

| 捕获项 | Gemini 结论 | Claude 裁定 |
|---|---|---|
| `ass:smoothness` 含 $G_f$ | 本稿类中 $F$ 全局 Lipschitz | 成立。已核 L25–39，常数 $G_F$ 定义见 2.1 节。该条不消除 `(d)` 的初始间隙问题 |
| `def:oracle-model` 给出完整 Jacobian 与 $f(\mathbf{x})$ | 完整 Jacobian 会破坏 zero-chain 下界 | 成立。已核 L86–102。Claude 已在 PZL $K=1$ 实例上确认失效机制，见 1.1 (b) 第 5 点 |
| 定稿行号错位 | 列出当前行号；L7–22 的 $\nu$ 假设已删除 | 成立。Claude 读到的行号与 Gemini 一致 |
| DP 2019 Appendix C | 去对数的总复杂度在 pp. 57–58 的推导段，不在 Theorem C.1 | Gemini 单方核实；只涉及定位，不影响内容 |
| PZL 记号 $B_N$ | 原文中 $B_N$ 指 $M_N$ 的逆，GPT Pro 误作耦合块 | Gemini 单方核实；新线应另取记号表示耦合块 |
| Kornowski–Shamir（2209.10346）Theorem 3 | 适用于随机算法、受限的 $\delta$ 与维数 | Gemini 单方核实；条件原式待核 |
| `2608.19847` | 一致 LICQ 下 $O(\epsilon^{-2})$；每步解线性方程组 | 成立。项目笔记已核原文。需补充一点：该文处理等式约束，即 $h=\delta_{\{0\}}$，不在 Lipschitz 外函数类内 |
| `2607.08954` | 局部锥正则加分段线性 $h$ 时，一阶 ALM 达 $O(\epsilon^{-2})$ | **存在冲突。** 项目笔记 `literature.md` 记为：问题形式为函数约束，$X$ 紧；每步解 prox-linear 子问题；一般情形残差为 $O(K^{-1/3})$；`lower-bound-references.md` 记分段线性情形为 $O(K^{-1/2})$。按此，$O(\epsilon^{-2})$ 计的是第 3 层外层迭代数，不是第 2 层 oracle 次数。记为 `[待核原文]` |
| Tian–So（Math. Program. 2024） | 补列为确定性局部 oracle 的核心文献 | 补列成立。该文的结论是 Goldstein 驻点没有维数无关的确定性算法。用户定稿把它列为"精确驻点不可达"的出处，属于归属错位 |
| Zhang–Xu、Ke–Mei–Zhang、Liao–Zheng、Zhang–Luo、De Marchi 等 | 补列 | 补列合理；复杂度数值为 Gemini 单方核实 |
| PZL Algorithm 1 不用函数值 | Codex 报告称已由 Gemini 报告确认 | Gemini 报告中没有这一核查。现由 Claude 完成，见 1.3 节 |

### 1.3 PZL Algorithm 1 是否依赖函数值

**裁定：不依赖。`[已有文献定理]`（核对来源为 PZL v2 原文）。**

1. **主循环（Algorithm 1，`pzl_v2.txt` L2082–2126）。** 只执行三类操作：调用 saddle 梯度，调用 $\operatorname{proj}_X$，以及更新可计算量 $Q_t$ 与 $B_t$。
2. **初值 $B_0$ 的来源。** $B_0 = 15(\Delta + r_y D_Y^2)$ 中，$\Delta$ 作为已知的类参数进入，算法不对它做查询。
3. **子程序。** FOAM 单步（Algorithm 2）与非精确近端步（Algorithm 3）只使用梯度与投影。Lemma B.1 明确写明 "evaluates gradients only in $X\times Y$"。
4. **warm-start 初始化。** Proposition 6.2 的证明中，$\Delta$ 只出现在误差界里。
5. **对本线的含义。** 归约所需的已知参数是 $(\ell, D_Y, \Delta)$。经 $\mathcal{D}_\rho$ 的值函数恰为 $F$，因此 $\Delta$ 就是 $F(\mathbf{0})-\inf F$ 的上界，与本线的问题类一致。

### 1.4 剩余风险

1. **Oracle 一致性风险。** 本稿 oracle 含完整 Jacobian，问题类下界只在矩阵–向量积 oracle 下成立。若要在本稿中声称 Fast LRALM 在 GS 下 $\epsilon$ 阶最优，需同时满足三个条件：oracle 定义收窄；Fast LRALM 的分析只用到 $J_{\mathcal{A}}^\top\mathbf{q}$（目前为 Gemini 单方核实）；PZL 实例满足 $G_f$。
2. **$G_f$ 相容性风险。** 前提是 PZL $K=1$ 实例的梯度界与 $\epsilon$ 无关，见 1.1 (b) 第 6 点。
3. **归属风险。** 所有 `[已核验归约]` 都是本项目的现场推导。引用时必须写成「PZL 构造加本文归约」这类表述，不能写成文献定理。
4. **常数风险。**
   - 上下界的常数依赖没有联合匹配。
   - 当 $L_{\mathcal{A}}=0$ 时 $\ell_\ast=0$，$C_\ast$ 下界不适用。仿射子类需要另行分析。
5. **文献风险。** `2607.08954` 的内容存在冲突；另有若干条目只经 Gemini 单方核实。

---

## 二、统一后的问题类、Oracle 与度量设定

### 2.1 本稿设定：$\mathcal{I}(\mathbf{C},\Delta)$

1. **问题类。** 常数向量为 $\mathbf{C}=(L_f,G_f,L_{\mathcal{A}},G_{\mathcal{A}},L_h)$，维数取所有 $n,m$ 的并集，并要求 $F(\mathbf{0})-\inf F \le \Delta$。$\nabla f$ 满足 $L_f$-Lipschitz 且有界 $G_f$；$J_{\mathcal{A}}$ 满足 $L_{\mathcal{A}}$-Lipschitz 且有界 $G_{\mathcal{A}}$；$h$ 全域有限、凸，且 $L_h$-Lipschitz。

2. **推论。** $F$ 是 $R$-弱凸函数，并且全局 Lipschitz：

$$
R = \rho_F := L_f + L_h L_{\mathcal{A}},\qquad G_F := G_f + L_h G_{\mathcal{A}} .
$$

3. **Oracle。** 本稿 oracle 返回 $(f(\mathbf{x}),\nabla f(\mathbf{x}),\mathcal{A}(\mathbf{x}),J_{\mathcal{A}}(\mathbf{x}))$ 与 $\operatorname{prox}_{th}$。其中返回的是完整 Jacobian 矩阵。
4. **度量。** 本稿使用 `def:eps-kkt`，即 GS。
5. **对现有定理的影响。** 本稿现有定理（LRALM 族内下界与 Fast LRALM 上界）不受上述 oracle 问题影响。受影响的只是与问题类下界做比较的陈述。

### 2.2 新线推荐设定

1. **问题类 $\mathcal{C}$：保留 $G_f$，其余与 $\mathcal{I}(\mathbf{C},\Delta)$ 相同。** 理由有三条。
   - 与本稿及 Fast LRALM 的分析保持一致。
   - 第 1 层黑盒基准（Li–Pan）需要全局 Lipschitz 常数 $G_F$。
   - 所有已核验的上界都不依赖 $G_f$。

   下界实例必须满足 $\sup\lVert\nabla f\rVert \le G_f$。
   - Carmon 实例的梯度界为 $O(\sqrt{L_f\Delta})$ 量级。这一量级由该文的 $\ell_\infty$ 梯度界推算，常数待核。
   - PZL 实例的梯度界见 1.1 (b) 第 6 点。

   因此，下界陈述需附加 $G_f \ge c_0\sqrt{L_f\Delta}$ 型的相容条件，记为 `[有条件成立]`。若新线删去 $G_f$，上界与下界都不变，但需要重新核对 Fast LRALM 的分析和第 1 层基准。

2. **全局满行秩子类 $\mathcal{C}_\nu$。** 要求 $m \le n$，并且

$$
J_{\mathcal{A}}(\mathbf{x})J_{\mathcal{A}}(\mathbf{x})^\top \succeq \nu^2 I_m\quad \forall\,\mathbf{x}\in\mathbb{R}^n,\qquad 0 \lt \nu \lt G_{\mathcal{A}} .
$$

   这一条件等价于对一切 $\mathbf{q}$ 有 $\lVert J_{\mathcal{A}}^\top\mathbf{q}\rVert \ge \nu\lVert\mathbf{q}\rVert$。"最小非零奇异值有下界"不能替代它。严格不等号是不可达性构造所必需的，见 1.1 (e)。记 $\kappa := G_{\mathcal{A}}/\nu$。

3. **Oracle：矩阵–向量积加精确 prox。**

$$
\mathcal{O}_{f,\mathcal{A}}(\mathbf{x};\mathbf{w},\mathbf{v}) := \left(f(\mathbf{x}),\ \nabla f(\mathbf{x}),\ \mathcal{A}(\mathbf{x}),\ J_{\mathcal{A}}(\mathbf{x})\mathbf{w},\ J_{\mathcal{A}}(\mathbf{x})^\top\mathbf{v}\right),\qquad \mathcal{O}_h(\mathbf{z},t) := \operatorname{prox}_{th}(\mathbf{z}),\quad t \gt 0 .
$$

   选择这一 oracle 的依据有四条。
   - 它与 Drusvyatskiy–Paquette（Math. Program. 2019）使用的原语一致。
   - PZL $K=1$ 实例可用 $O(1)$ 次 saddle 查询模拟它，所以 GS 下界可以迁移。
   - $\mathcal{C}_\nu$ 上界不再需要有限差分。
   - 保留 $f(\mathbf{x})$ 会使下界结论更强，而所有上界都不使用它。

   GPT Pro 采用的较弱 oracle 不含 $f(\mathbf{x})$ 与 $J_{\mathcal{A}}\mathbf{w}$。在这一 oracle 下，下界同样成立；上界在精确实数模型中借助有限差分也成立。

4. **计数与算法类。**
   - 算法类为全体确定性算法。
   - 每次调用计一次。
   - 类常数与 $\epsilon$ 及维数无关，困难实例的维数可以随 $\epsilon$ 增长。
   - 采用精确实数模型，不计位复杂度。
   - 要求 $R \gt 0$。
   - 凡结论含显式维数因子，均在条目中单独注明。

### 2.3 度量定义

取 $\lambda = 1/(2R)$。记 $F_\lambda$ 为 $F$ 的 Moreau 包络。各度量定义如下：

$$
E_\epsilon(\mathbf{x}):\ \operatorname{dist}(\mathbf{0},\partial F(\mathbf{x})) \le \epsilon ;\qquad \mathrm{OS}_\epsilon(\mathbf{x}):\ \lVert\nabla F_\lambda(\mathbf{x})\rVert \le \epsilon ;
$$

$$
V_{\mu,\eta}(\mathbf{x}):\ \exists\,\mathbf{y},\ \mathbf{q}\in\partial h(\mathbf{y}),\quad \lVert\nabla f(\mathbf{x}) + J_{\mathcal{A}}(\mathbf{x})^\top\mathbf{q}\rVert \le \eta,\quad \lVert\mathcal{A}(\mathbf{x})-\mathbf{y}\rVert \le \mu ;
$$

$$
\mathrm{GS}_\epsilon := V_{\epsilon,\epsilon};\qquad G_{\delta,\eta}(\mathbf{x}):\ \operatorname{dist}\left(\mathbf{0},\ \operatorname{cl\,conv}\bigcup_{\lVert\mathbf{z}-\mathbf{x}\rVert\le\delta}\partial F(\mathbf{z})\right) \le \eta .
$$

由于 $h$ 全域有限且凸，链式法则 $\partial F(\mathbf{x}) = \nabla f(\mathbf{x}) + J_{\mathcal{A}}(\mathbf{x})^\top\partial h(\mathcal{A}(\mathbf{x}))$ 成立。因此 $E_\epsilon$ 与 $V_{0,\epsilon}$ 等价。

---

## 三、已核验的四格复杂度表与五类度量总表

### 3.1 记号

$$
B := L_h G_{\mathcal{A}},\qquad S := \max\{R,\ G_{\mathcal{A}}\},\qquad \kappa := \frac{G_{\mathcal{A}}}{\nu},
$$

$$
\ell_\ast := \min\left\{L_f,\ G_{\mathcal{A}},\ \frac{L_h L_{\mathcal{A}}}{2}\right\},\qquad D_\ast := 2L_h,\qquad \Delta_\ast := \min\{\Delta,\ c_5\ell_\ast D_\ast^2\},\qquad C_\ast := \ell_\ast^{3/2}D_\ast^{1/2}\Delta_\ast ,
$$

其中 $c_5$ 是 PZL Theorem 3.2 证明中的数值常数。

### 3.2 四格表（$\mathcal{C}$ / $\mathcal{C}_\nu$ × OS / GS）

| 问题类与度量 | 算法无关下界 | 确定性上界 | $\epsilon$ 指数状态 |
|---|---|---|---|
| $\mathcal{C}$，OS | $\Omega(C_\ast\epsilon^{-5/2})$ `[已核验归约]`：由 PZL $K=1$ 实例、分离 oracle 模拟，再经 OS 到 GS 的换算得到 | $O(RB\Delta\epsilon^{-3})$ `[已核验归约]`：由 $\mathcal{D}_\rho$ 结合 PZL Theorem 3.3 得到 | 下界指数 $5/2$，上界指数 $3$：`[开放空白]` |
| $\mathcal{C}$，GS | $\Omega(C_\ast\epsilon^{-5/2})$ `[已核验归约]` | $O(S\sqrt{B}\Delta\epsilon^{-5/2})$ `[已核验归约]`：由 PZL Theorem 3.4 得到；Fast LRALM 的 $O(\epsilon^{-5/2})$ 为 `[已有文献定理·本稿]`，在本稿 oracle 下成立 | 指数 $5/2$ 已匹配；常数依赖为 `[开放空白]` |
| $\mathcal{C}_\nu$，OS | $\Omega(L_f\Delta\epsilon^{-2})$ `[已有文献定理]`：由 Carmon et al. 2020 经 $h=0$ 与 $\mathcal{A}(\mathbf{x})=\nu\mathbf{x}$ 嵌入得到 | $\widetilde{O}(\kappa R\Delta\epsilon^{-2})$ `[已核验归约]` | 指数 $2$ 已匹配；$\kappa$ 的幂次与对数因子为 `[开放空白]` |
| $\mathcal{C}_\nu$，GS | 同上 | 同上 | 同上 |

**表注。**

1. **$\mathcal{C}$ 行下界的条件。** 该下界在以下条件下成立：
   - $\ell_\ast \gt 0$；
   - $\epsilon \le c\min\{\ell_\ast D_\ast, \Delta_\ast/D_\ast\}$；
   - oracle 取 2.2 节的设定；
   - $G_f$ 满足相容条件，此项为 `[有条件成立]`。

   在本稿的完整 Jacobian oracle 下，该下界尚未建立。
2. **全参数上界。** 与上表对应的全参数上界为

$$
T_{\mathcal{C},\mathrm{OS}} = O\left(\left(1+\frac{R\Delta}{\epsilon^2}\right)\left(1+\frac{B}{\epsilon}\right)\right),\qquad T_{\mathcal{C},\mathrm{GS}} = O\left(\sqrt{\left(1+\frac{S\Delta}{\epsilon^2}\right)\left(1+\frac{B}{\epsilon}\right)\left(1+\frac{S\Delta}{\epsilon^2}+\frac{B}{\epsilon}\right)}\right),
$$

$$
T_{\mathcal{C}_\nu} = O\left(\kappa\left(1+\frac{R\Delta}{\epsilon^2}\right)\log\left(2+\frac{\kappa B^2}{\epsilon^2}\right)\right).
$$

3. **单次梯度的查询代价。** 经 $\mathcal{D}_\rho$ 计算一次梯度，所需查询次数随 oracle 而定：本稿 oracle 需 $2$ 次，2.2 节 oracle 需至多 $3$ 次。

### 3.3 五类度量总表

| 度量 | 一般类 $\mathcal{C}$ | 满行秩子类 $\mathcal{C}_\nu$ |
|---|---|---|
| 精确 $\epsilon$-KKT（$E_\epsilon$） | 没有有限的最坏情形查询界 `[已核验归约]` | 同左。对 $0\lt\nu\lt G_{\mathcal{A}}$ 与 $\epsilon \lt L_h\nu$ 成立，一维多面体 $h$ 已足够构造；覆盖第 2、3 层 oracle `[已核验归约]` |
| OS | 下界 $\Omega(\epsilon^{-5/2})$，上界 $O(\epsilon^{-3})$ | 下界 $\Omega(\epsilon^{-2})$，上界 $\widetilde{O}(\kappa\epsilon^{-2})$ |
| GS | 下界与上界均为 $\Theta(\epsilon^{-5/2})$ 阶 | 下界与上界的指数均为 $2$ |
| $V_{\mu,\epsilon}$（固定 $\mu \gt 0$） | 上界为下式的 $N_V$，指数 $2$ `[已核验归约]`；下界 $\Omega(L_f\Delta\epsilon^{-2})$，由光滑基准嵌入得到 | 同左，不需要 $\nu$ |
| Goldstein（固定 $\delta \gt 0$） | 上界经 OS 转移得 $\widetilde{O}(\epsilon^{-3})$ `[已核验归约]`；允许显式维数时为 $\widetilde{O}(d^2\epsilon^{-2})$ `[已核验归约]`；维数无关的匹配下界为 `[开放空白]` | 上界 $\widetilde{O}(\epsilon^{-2})$ `[已核验归约]`；匹配下界为 `[开放空白]` |

$$
N_V(\mu,\epsilon) = \widetilde{O}\left(\left(1+\frac{R\Delta_\mu}{\epsilon^2}\right)\sqrt{1+\frac{L_h G_{\mathcal{A}}^2}{R\mu}}\right),\qquad \Delta_\mu := \Delta + \frac{L_h\mu}{2};\qquad N_G(\delta,\epsilon) \le N_{\mathrm{OS}}\left(\min\{\epsilon,\ 2R\delta\}\right).
$$

**表注。**

1. **固定 $\delta$ 的 Goldstein 格不能填入 $\Omega(\epsilon^{-2})$。** 对光滑函数，Goldstein 只保证梯度不超过 $\epsilon + L_f\delta$。固定 $\delta$ 后，由此得到的界不含 $\epsilon$ 的负幂。
2. **一般 Lipschitz 类的 Goldstein 下界不能直接转入。** Kornowski 2026 与 Ding–Yuan 2026 的困难实例不属于固定 $R$ 的复合类。在含 $G_f$ 的类中 $F$ 虽然 $G_F$-Lipschitz，这些下界仍不能转入。
3. **DP prox-linear 映射。** 作为一个点性质，它与 OS 在常数意义下等价，属于 `[已有文献定理]`（DP 2019 Theorem 4.5，式 (4.8)），复杂度与 OS 同阶。

### 3.4 度量换算一览

1. **OS 推出同阶的 GS 与 Goldstein，`[已核验归约]`。** 若 $\mathrm{OS}_\eta(\mathbf{x})$ 成立，则 $V_{\mu',3\eta/2}(\mathbf{x})$ 与 $G_{\eta/(2R),\eta}(\mathbf{x})$ 成立，其中 $\mu' = G_{\mathcal{A}}\eta/(2R)$。$E_\eta$ 推出 $\mathrm{OS}_{2\eta}$，且因子 $2$ 是紧的。
2. **无满秩时 GS 推出 OS，损失为平方根，`[已核验归约]`。**

$$
V_{\mu,\eta}(\mathbf{x}) \Longrightarrow \lVert\nabla F_\lambda(\mathbf{x})\rVert \le \eta + \sqrt{\eta^2 + 8RL_h\mu}.
$$

   反例一在固定类常数（$L_f$、$L_h$、$G_{\mathcal{A}}$、$L_{\mathcal{A}}$ 均为 $1$，$R=2$，$\Delta\le 4$）下取到 $\Theta(\sqrt{\mu})$。因此平方根损失在最坏情形下是必要的。半径固定为 $1$ 的 Goldstein 同样出现这一损失。
3. **满秩时 GS 推出 OS，损失为线性，`[已核验归约]`。** 只要在 $B(\mathbf{x},\mu/\nu)$ 上满秩，就有

$$
V_{\mu,\eta}(\mathbf{x}) \Longrightarrow E_{\eta+R\mu/\nu}(\mathbf{x}'),\qquad \lVert\nabla F_\lambda(\mathbf{x})\rVert \le 2\eta + \frac{4R\mu}{\nu}.
$$

4. **满秩不能把 Goldstein 到 OS 的损失线性化，`[已核验归约]`。** 反例二满足 $\nu = 1$、$L_{\mathcal{A}}=0$，损失仍为 $\sqrt{\delta}$。
5. **Goldstein 推出 OS，`[已核验归约]`。** 该换算不需要 $F$ 全局 Lipschitz。记 $a = \eta + R\delta$，则 $\lVert\nabla F_\lambda(\mathbf{x})\rVert \le a + \sqrt{a^2 + 8RB\delta}$。

---

## 四、6 个子问题终审记分卡

### 大问题一 · 子问题一：分离 oracle 下的最优阶数

- **`[已有文献定理]`**
  - 第 1 层黑盒 oracle：$\Omega(RG_F^2\Delta\epsilon^{-4})$（Li–Pan v3，Theorem 2）。
  - 光滑基准：$\Omega(L_f\Delta\epsilon^{-2})$（Carmon et al. 2020，Theorem 1）。
  - PZL Theorems 3.1–3.4：光滑 NC-C 问题上 OS 与 GS 的紧界。
  - Fast LRALM：GS 上界 $O(\epsilon^{-5/2})$，为 `[已有文献定理·本稿]`。
- **`[已核验归约]`**
  - 经 $\mathcal{D}_\rho$ 归约的 OS 与 GS 上界，见 3.2 节。
  - 在 2.2 节 oracle 下，$\mathcal{C}$ 上 OS 与 GS 都有 $\Omega(C_\ast\epsilon^{-5/2})$ 下界，其中 $G_f$ 相容性为 `[有条件成立]`。
  - 因此 GS 的 $\epsilon$ 指数为 $5/2$。
- **`[开放空白]`**：确定下式中的 OS 最优指数：

$$
p^\ast_{\mathrm{OS}} := \inf\left\{p \ge 0 :\ \exists\ \text{deterministic } \mathsf{A},\ T_{\mathrm{OS}}(\mathsf{A},\mathcal{C},\epsilon) = O(\epsilon^{-p})\right\},\qquad \frac{5}{2} \le p^\ast_{\mathrm{OS}} \le 3 .
$$

  另一个开放问题是 GS 的常数依赖，即 $S\sqrt{B}\Delta$ 与 $C_\ast$ 之间的差距。

### 大问题一 · 子问题二：minimax 下界能否在复合类内实现

- **`[已有文献定理]`**
  - PZL：对一般确定性算法，OS 下界 $\Omega(\ell^2 D_Y\Delta\epsilon^{-3})$，GS 下界 $\Omega(\ell^{3/2}D_Y^{1/2}\Delta\epsilon^{-5/2})$。
  - WGY：只对 zero-respecting 算法给出 OS 下界。
- **`[已核验归约]`：GS 方向可以实现。** 依据如下。
  - PZL $K=1$ 实例可写成 $f(\mathbf{x}) + h(\mathcal{A}(\mathbf{x}))$，其中 $h = H^\ast$。
  - 在 2.2 节 oracle 下，精确 prox 与矩阵–向量积都可由 $O(1)$ 次 saddle 查询模拟。
  - 在本稿的完整 Jacobian oracle 下，这一论证失效。
- **`[已核验归约]`：OS 方向的现有构造不可迁移。**
  - PZL §4.3 与 WGY 式 (16)–(17) 的对偶三对角二次项使 prox 恢复 $(I+\gamma M_N)^{-1}\mathbf{e}_1$。当次对角元全部非零时，这个向量覆盖整条链。
  - 耦合块的满行秩最小奇异值为 $0$。
- **`[开放空白]`**：在 2.2 节 oracle 下，是否存在 OS 困难实例族给出 $\Omega(\epsilon^{-3})$，或存在 $o(\epsilon^{-3})$ 的 OS 算法？
  - 必要条件（`[已核验归约]`）：若实例族满足 $JJ^\top \succeq \nu_\epsilon^2 I$，则复杂度不超过 $\widetilde{O}(\kappa_\epsilon\epsilon^{-2})$，其中 $\kappa_\epsilon$ 是以 $\nu_\epsilon$ 代入的条件数。因此一个 $\Omega(\epsilon^{-3})$ 实例必须秩亏，或者满足 $\nu_\epsilon = \widetilde{O}(\epsilon)$。
  - 在任意确定性算法下，支撑函数子类（$h = \sigma_Y$）的下界同样为 `[开放空白]`。原因是 PZL 的确定性扩展引入了辅助二次项，此时 $h$ 不再是支撑函数。

### 大问题一 · 子问题三：结构参数如何决定阶数

- **`[已有文献定理]`**
  - 外函数光滑时的 NC-SC 紧界：$\Theta(\sqrt{\kappa_y}\,\ell\Delta\epsilon^{-2})$。
  - 满行秩仿射复合：上界 $\widetilde{O}(\kappa L_f\Delta\epsilon^{-2})$（Zhu–Chen–Zhang–Wen）。
  - 带条件数的下界（Zhu–Chen–Zhang–Wen、Liu–Lin–Xu、Shi–Wang）都要求 $h=\delta_{\{0\}}$、linear-span 算法限制或完整 Jacobian 中的至少一项。
- **`[已核验归约]`**
  - $\mathcal{C}_\nu$ 上 OS 与 GS 都有 $\widetilde{O}(\kappa R\Delta\epsilon^{-2})$，对一般 $L_h$-Lipschitz 凸 $h$ 成立。机制是：线性化子问题对偶目标中的二次项 $\lVert\mathbf{g}+J^\top\mathbf{q}\rVert^2/(2R)$ 关于 $\mathbf{q}$ 是 $\nu^2/R$ 强凸的。因此 $h^\ast$ 自身是否强凸不影响结论。
  - 若 $h$ 有 Lipschitz 梯度，$F$ 是光滑函数，梯度法直接给出 $O(\epsilon^{-2})$。
- **`[开放空白]`**
  1. 对一般 Lipschitz 凸 $h$ 与任意确定性算法，求 $\kappa$ 的紧指数。已知 $\alpha^\ast \in [0,1]$，目标是使复杂度主项为

$$
\Theta\left(\kappa^{\alpha^\ast}R\Delta\epsilon^{-2}\right).
$$

  2. 能否去掉对数因子。
  3. 当 $\nu = 0$ 时，$h$ 的锐度或多面体误差界常数能否恢复指数 $2$。
  4. 局部正则性的可核验定义，以及在该定义下的复杂度。

### 大问题二 · 子问题一：可达性边界

- **`[已有文献定理]`**
  - 黑盒 Lipschitz 类上，精确驻点有限步不可达：Zhang et al.（ICML 2020，Theorem 5）；Kornowski–Shamir（JMLR 2022）。
  - 当 $\mathcal{A} = I$ 时，近端梯度在 $O(L_f\Delta\epsilon^{-2})$ 步内达到 $E_\epsilon$。
  - 满行秩仿射且矩阵可用时，Böhm–Wright（JOTA 2021）式 (25) 的修正点给出 $E_\epsilon$。
- **`[已核验归约]`**
  - 对 $0\lt\nu\lt G_{\mathcal{A}}$ 与 $\epsilon \lt L_h\nu$，$\mathcal{C}_\nu$ 上的 $E_\epsilon$ 没有有限的最坏情形查询界。
  - 该结论覆盖精确 prox、本稿 oracle、第 3 层 prox-linear oracle，以及任何只依赖查询点有限阶 jet 的 oracle，见 1.1 (e)。
  - 对未知的满行秩仿射 $\mathcal{A}$，可用 $m$ 次矩阵–向量积恢复矩阵，再做 Böhm–Wright 修正，即可达到 $E_\epsilon$。这一做法带有显式维数代价。
- **`[开放空白]`**
  - 若 $\mathcal{A}(\mathbf{x}) = M\mathbf{x} + \mathbf{b}$ 未知且 $MM^\top \succeq \nu^2 I$，在 2.2 节 oracle 下，是否存在与维数无关的有限查询界来输出 $E_\epsilon$ 点？
  - 对非线性 $\mathcal{A}$，什么样的附加可计算结构能恢复 $E_\epsilon$ 的可达性？已知 Bareilles–Iutzeler–Malick 的流形识别还不够。

### 大问题二 · 子问题二：GS 与 OS 的换算

- **`[已有文献定理]`**
  - Moreau 包络的基本关系：Davis–Drusvyatskiy（SIOPT 2019），Lemma 2.2。
  - Lyusternik–Graves 型度量正则性：Dontchev–Rockafellar。
  - 带统一邻域的外 Lipschitz 条件下，Goldstein 推出邻近驻点：Tian–Zhou–So（ICML 2022），Theorem 4.4。
- **`[已核验归约]`**：3.4 节的五条换算与两个反例全部成立。
  - 无满秩时的紧换算率为 $\Theta(\sqrt{RL_h\epsilon})$。
  - 满秩时为线性换算，只需在 $B(\mathbf{x},\mu/\nu)$ 上满秩。
  - 两分支在 $\nu \asymp \sqrt{\epsilon}$ 处衔接。
- **`[开放空白]`**
  - 正则性能否进一步弱化：例如只沿算法轨迹成立，或只在水平集上成立。
  - $\nu = 0$ 时，多面体或锐度结构能否维持同阶换算。

### 大问题二 · 子问题三：各度量下的问题类紧下界

- **`[已有文献定理]`**：光滑 NC-C 上存在 OS 与 GS 的半阶分离，即 OS 为 $\Theta(\epsilon^{-3})$，GS 为 $\Theta(\epsilon^{-5/2})$（PZL）。
- **`[已核验归约]`**
  - 在 $\mathcal{C}$ 上，GS 的指数为 $5/2$。
  - 在 $\mathcal{C}_\nu$ 上，OS 与 GS 的指数都是 $2$，所以固定 $\nu$ 时两类度量在指数层面归并。
  - 若取 $\nu = \Theta(\epsilon^{a})$ 且 $0 \le a \le 1$，上界为 $\widetilde{O}(\epsilon^{-2-a})$。当 $a = 1$ 时，它与无正则的 $O(\epsilon^{-3})$ 重合。
  - PZL OS 实例在 $N \gt 2$ 时秩亏，两个非零奇异值为 $\Theta(\sqrt{\ell\epsilon/D_Y})$。
- **`[开放空白]`**
  1. $\mathcal{C}$ 上 OS 的紧指数，与大问题一子问题一相同。
  2. 关于 $(\nu,\epsilon)$ 的联合下界：当 $\nu = \Theta(\epsilon^{a})$ 时，是否需要 $\Omega(\epsilon^{-2-a})$？

---

## 五、核心文献索引与定位切割

| 文献 | 设定与 oracle | 本线用途 | 核实状态 |
|---|---|---|---|
| Pan–Zheng–Li，arXiv:2609.14235v2 | 联合光滑 NC-C；返回函数值与双侧梯度；一般确定性算法 | $\mathcal{C}$ 的上界归约与 $K=1$ GS 下界迁移 | Gemini 全文核实；Claude 已核 Algorithm 1–3、Prop 6.2、式 (21)、(30)、Lemma 3.2 |
| Wu–Gu–Yang，arXiv:2609.14233v1 | 联合光滑 NC-C；zero-respecting 算法 | OS 构造对照；§6 公开问题 | Gemini 核实 |
| Zhang–Xu，arXiv:2609.17973；Ke–Mei–Zhang，arXiv:2609.25752 | NC-C 单循环与多层循环上界 | 与 PZL Tracked-FOAM 并列，作为上界对照 | Gemini 单方 |
| Lin–Jin–Jordan，COLT 2020；Kovalev–Gasnikov，NeurIPS 2022 | 先行上界；FOAM 的内层来源 | 上界谱系 | Gemini 核实 |
| Li–Pan，arXiv:2608.03246v3 | 弱凸、$G$-Lipschitz；完整次微分 oracle | 第 1 层黑盒基准，取 $G = G_F$ | Gemini 核实 |
| Liao–Zheng，arXiv:2509.02804 | 确定性弱凸 $O(\epsilon^{-4})$ 上界 | 与 Li–Pan 配对 | Gemini 单方 |
| Carmon–Duchi–Hinder–Sidford，Math. Program. 2020 | 光滑非凸；任意确定性算法 | 四格表中的光滑基准 | Gemini 核实；梯度界常数待核 |
| Drusvyatskiy–Paquette，Math. Program. 2019 | 凸复合；原语为 $J_c\mathbf{v}$、$J_c^\top\mathbf{w}$ 与 prox | 第 3 层基准；映射度量等价于 OS | Gemini 核实；Appendix C 的定位已修正 |
| Zhu–Chen–Zhang–Wen，arXiv:2308.06470v1 | 满行秩仿射复合；下界需 $h=\delta_{\{0\}}$ 与 linear-span | 仿射基准；$\kappa$ 下界路径 | Gemini 核实；§2.2 的笔误属实 |
| Liu–Lin–Xu，arXiv:2307.07605 与 MOR 2026 | 仿射约束复合；linear-span 算法 | $\kappa$ 下界路径；更强 oracle 下的紧性问题 | Gemini 核实 |
| Shi–Wang，Optimization Online 2026 | 光滑等式约束；完整 Jacobian | 正则性常数进入下界的先例 | Gemini 核实 |
| Liu–Deng–Wang–Wen，arXiv:2608.19847 | 光滑等式约束；Gauss–Newton 线性方程组步；一致 LICQ | 立项切割对象 | 项目笔记已核原文 |
| Zhu–Li，arXiv:2607.08954 | 函数约束复合；$X$ 紧；每步解 prox-linear 子问题；局部正则 | 立项切割对象 | `[待核原文]`；笔记与 Gemini 冲突 |
| Zhang–Luo，SIOPT 2020/2022；De Marchi–Jia–Kanzow–Mehlitz，Math. Program. 2023 | 线性约束的全局对偶误差界；非线性复合约束 ALM | 子问题三的第一步 | Gemini 单方 |
| Zhang–Lin–Jegelka–Sra–Jadbabaie，ICML 2020 | 黑盒 Lipschitz；精确驻点不可达 | 可达性的出处 | Gemini 核实 |
| Kornowski–Shamir，JMLR 2022 与 arXiv:2209.10346 | 局部 oracle；邻近驻点与小次梯度 | 可达性与凸 Goldstein | Gemini 核实；Theorem 3 的条件待核 |
| Tian–So，Math. Program. 2024（arXiv:2210.06907） | Goldstein 驻点不存在维数无关的确定性算法 | Goldstein 维数依赖；"定义四件套"的格式参照 | 项目笔记已核问题设定 |
| Tian–Zhou–So，ICML 2022 | Goldstein 与 NAS 的区分；外 Lipschitz 条件 | 换算的正则条件 | Gemini 核实 |
| Böhm–Wright，JOTA 2021；Bareilles–Iutzeler–Malick，SIOPT 2023；Davis–Drusvyatskiy，SIOPT 2019 | 满秩仿射修正；流形识别；Moreau 关系 | 大问题二 | Gemini 核实 |
| Davis et al.，NeurIPS 2022；Jordan et al.，COLT 2023；Kong–Lewis，MOR 2024；Kornowski，arXiv:2609.17780 与 arXiv:2609.23837；Ding–Yuan，arXiv:2609.38082v2 | 一般 Lipschitz 类的 Goldstein 复杂度 | 邻近基准，不进入四格表 | Gemini 核实 |
| Beck–Teboulle，SIIMS 2009；Devolder–Glineur–Nesterov，Math. Program. 2014；Dontchev–Rockafellar（专著） | 近端梯度单步界；非精确 oracle；Lyusternik–Graves | 补充 `(d)` 与 `(f)` | Claude 引入；定理编号待核 |

**立项切割。**

1. **与 `2608.19847` 的区别有三点。**
   - 该文处理等式约束 $c(\mathbf{x}) = 0$，相当于 $h = \delta_{\{0\}}$，不在 $L_h$-Lipschitz 外函数类内。
   - 该文每步求解 $(\beta I + \rho\nabla c\nabla c^\top)\mathbf{p} = \cdots$，这是线性方程组原语，强于本线的矩阵–向量积 oracle。
   - 该文的 $O(\epsilon^{-2})$ 是迭代数，不是 oracle 次数。

   本线 $\mathcal{C}_\nu$ 上界的新内容在于：对一般 Lipschitz 凸 $h$，只用矩阵–向量积与精确 prox，就能在 oracle 次数意义下达到 $\widetilde{O}(\kappa\epsilon^{-2})$。
2. **与 `2607.08954` 的区别（待核原文后定稿）。**
   - 该文是函数约束形式，且 $X$ 紧。
   - 每步解 prox-linear 子问题，属于第 3 层原语。
   - 采用局部正则性。
   - $O(\epsilon^{-2})$ 只在分段线性外函数下成立。

   本线的区别在于：第 2 层 oracle 计数、全局满行秩，以及一般 Lipschitz 凸 $h$。
3. **与带条件数下界文献的区别。** Zhu–Chen–Zhang–Wen、Liu–Lin–Xu 与 Shi–Wang 的条件数下界，分别依赖 $h = \delta_{\{0\}}$、linear-span 算法限制或完整 Jacobian 中的至少一项。本线要求的下界针对 Lipschitz 凸 $h$ 与任意确定性算法。

---

## 六、下一步立项与核查行动清单

### 6.1 优先攻克方向

1. **首选方向：一般类 $\mathcal{C}$ 上 OS 的 $\epsilon$ 指数（$5/2$ 至 $3$）。**
   - **理由**：这是四格表中唯一在指数层面没有闭合的格子，正反两个方向的结论都是实质定理。
   - **第一步，构造方向**：设计与精确 prox 相容的 OS 困难实例。按 `(c)` 的判据，对偶 Hessian 中带非零次对角元的三对角块会被一次 prox 暴露。候选做法有两种：一是把链式耦合移入 $\mathcal{A}$ 的非线性部分，二是使对偶二次项在隐藏基下坐标可分。无论哪种做法，实例都必须秩亏，或满足 $\nu_\epsilon = \widetilde{O}(\epsilon)$。
   - **第一步，算法方向**：检验精确 $\operatorname{prox}_{th}$ 能否把 GS 的 $\epsilon^{-5/2}$ 算法提升为 OS 的 $o(\epsilon^{-3})$ 算法。静态换算只给出 $\sqrt{\epsilon}$，因此需要动态论证。
2. **次选方向：$\mathcal{C}_\nu$ 上 $\kappa$ 的紧幂次。** 这是 Claude 提出的候选路径，尚未验证。
   - 用精确罚函数把 Zhu–Chen–Zhang–Wen 的 $h=\delta_{\{0\}}$ 条件数链换成 $h = L_h\lVert\cdot\rVert$。这需要乘子有界，并且 $L_h$ 大于乘子界。
   - 再用 PZL 型正交旋转去掉 linear-span 限制。
3. **并行的低风险工作。**
   - 把 `[已核验归约]` 整理成自包含证明：度量换算、不可达性、$\mathcal{C}_\nu$ 上界、GS 下界迁移。
   - 交 Codex 复核后，可作为新线的第一批引理。
4. **与本稿相关。** 若要在本稿写「Fast LRALM 在 GS 下 $\epsilon$ 阶最优」，需先完成 6.2 节第 1、2 项，并把 `def:oracle-model` 收窄为矩阵–向量积形式。本轮只提出建议，不修改 `.tex` 文件。

### 6.2 待补核项

1. **Fast LRALM 的 oracle 用量。** 核对 `LRALMFamily.tex` 与 `Acceleration.tex` 的分析是否只用到 $J_{\mathcal{A}}^\top\mathbf{q}$、不用 $f(\mathbf{x})$。目前只有 Gemini 单方核实。
2. **PZL $K=1$ 实例的梯度界。** 写出缩放后的 $\sup\lVert\nabla f\rVert$，确认它与 $\epsilon$ 无关。同时核对 Carmon 实例的梯度界常数。
3. **`2607.08954` 全文。** 需确认四件事：问题形式、每步原语的层级、局部锥正则的量化条件、$O(K^{-1/3})$ 与 $O(K^{-1/2})$ 各自成立的条件。
4. **原 `[判断]` 条目对照。** 对 GPT Pro 报告与用户定稿中的判断性陈述，逐条给出"保留、修订或删除"。已知需处理的条目如下：
   - 用户定稿把 Tian–So 列为"精确驻点不可达"的出处，需修订；
   - 「第 3 层可达性开放」已关闭；
   - 「仅凭 $\nu \gt 0$ 未必足够」已解决；
   - 对 OS 实例 $\sigma_{\min} = \Theta(\epsilon)$ 的预期与原文不符；
   - OS 下界应由 $\Omega(\epsilon^{-2})$ 升级为 $\Omega(\epsilon^{-5/2})$；
   - GPT Pro「$F$ 未必全局 Lipschitz」的结论，在含 $G_f$ 的类中已不适用；
   - DP 2019 Theorem C.1 的定位需修正。
5. **有限差分精度。** 若保留 GPT Pro 的弱 oracle，需按 Devolder–Glineur–Nesterov 写出 $\eta$ 的多项式界。
6. **Gemini 单方核实的条目。** 包括：DP 2019 pp. 57–58；PZL 中 $B_N$ 的定义；Kornowski–Shamir Theorem 3 的条件；Tian–So 与 Ding–Yuan 的 oracle 定义关系；Zhang–Xu、Ke–Mei–Zhang 与 Liao–Zheng 的复杂度。
7. **PZL OS 实例的次对角元。** 确认 PZL 式 (9)–(10) 与 WGY 式 (16)–(17) 中三对角块的次对角元全部非零。
8. **引用编号。** 核对 Lyusternik–Graves 定理在 Dontchev–Rockafellar 中的编号，以及 Beck–Teboulle 单步界的引理编号。
9. **项目笔记同步。** `memory/notes/project/lower-bound-references.md` 需更新到 PZL v2 与 Li–Pan v3；该文件把 `2607.08954` 标为"待读"，与 `literature.md` 的已核标记不一致，需要统一。

### 6.3 对用户 6 子问题定稿的修订要点

1. **§0.2 Oracle 层级。**
   - 第 2 层改为 2.2 节的矩阵–向量积 oracle。
   - 注明完整 Jacobian 会使 PZL 下界的模拟论证失效。
   - 第 1 层基准写成 $\Theta(RG_F^2\Delta\epsilon^{-4})$。
2. **§0.4 计算一次 $\nabla\mathcal{D}_\rho$ 的查询次数。** 在 2.2 节 oracle 下改为"至多 3 次"；本稿 oracle 下为 2 次。
3. **大问题一子问题一。**
   - Insight 与已知结果中，OS 与 GS 的下界都由 $\Omega(\epsilon^{-2})$ 升级为 $\Omega(\epsilon^{-5/2})$。
   - 「全算法类紧阶数（开放）」缩小为只针对 OS。
   - 「常数幂次待核」替换为 3.2 节给出的显式上界。
4. **大问题一子问题二。**
   - 「GS 下界（开放）」改为 `[已核验归约]`，并附 oracle 条件与 $G_f$ 条件。
   - 思路中「$h = L_h\lVert\cdot\rVert_2$ 的旋转不变性」应换成"对偶耦合与 prox 相容"。原因是 $K=1$ 实例的半球朝向不参与旋转，GS 方向已经解决；OS 方向的障碍来自三对角对偶二次项。
5. **大问题一子问题三。**
   - 删除「仅凭 $\nu \gt 0$ 未必消除 $h^\ast$ 非强凸性」的推测，代以对偶二次项 $\nu^2/R$-强凸的机制。
   - 把对 `2607.08954` 的描述修订为第 3 层原语下的迭代数，并标注待核。
   - 开放问题收窄为 $\kappa$ 的紧指数与对数因子。
6. **大问题二子问题一。**
   - 一维构造需写明严格的 $0\lt\nu\lt G_{\mathcal{A}}$ 与 $\epsilon \lt L_h\nu$。
   - 「第 3 层可达性开放」改为已核验。
   - 新开放问题换成"未知满行秩仿射 $\mathcal{A}$ 下的维数无关可达性"。
   - 黑盒不可达性的出处改为 Zhang et al. 2020 与 Kornowski–Shamir 2022。Tian–So 2024 移到 Goldstein 维数依赖处。
7. **大问题二子问题二。**
   - 原反例中 $\mathcal{A}(x) = \epsilon - \sqrt{\epsilon}x - x^2/2$ 的导数无界，违反 $G_{\mathcal{A}}$ 有界的假设。应换成反例一：$\mathcal{A}(x) = \sqrt{1+x^2} - 1$，在固定类常数下成立。
   - 无 $\nu$ 时的换算式采用 $\eta + \sqrt{\eta^2 + 8RL_h\mu}$。
   - 有 $\nu$ 时注明只需在 $B(\mathbf{x},\mu/\nu)$ 上满秩。
   - 删除对 `Preliminaries.tex#L7-L22` 的引用。
8. **大问题二子问题三。**
   - $O((1+\rho_F/\nu)^{5/2}\epsilon^{-5/2})$ 已被 $\widetilde{O}(\kappa\epsilon^{-2})$ 取代。
   - 「OS 实例 $\sigma_{\min} = \Theta(\epsilon)$」应改为：$N \gt 2$ 时实例秩亏，两个非零奇异值为 $\Theta(\sqrt{\ell\epsilon/D_Y})$。按此重新设计"按 $\nu$ 截断链长"的思路。
9. **全稿行号。** 按当前 `Preliminaries.tex` 更新：
   - `ass:smoothness`：L25–39
   - `ass:h`：L41–48
   - `def:eps-kkt`：L52–66
   - `def:problem-class`：L73–84
   - `def:oracle-model`：L86–102
