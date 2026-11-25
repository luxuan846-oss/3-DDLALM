# 开放问题调研数学推导与反例核查报告（Codex）

- **核查日期**：2026-11-23
- **核查工具与模型**：本地 Codex CLI（`/opt/homebrew/bin/codex exec`，`gpt-6.2-sol`，`reasoning effort = high`，经已配置的 `yxai` provider 运行；默认 `manypapers` 返回 `429 Too Many Requests`，`codexbar.openai-oauth` 触发用量上限）＋ Python 数值检验（NumPy）
- **核查范围**：GPT Pro 两份调研报告中全部标记为「本次推导 / 本次构造」的 9 项数学论证 `(a)–(i)`
- **配套文献核查**：见同目录 `open-problems-audit-gemini-20261123.md`

---

## 一、总览表

**核心结论**：9 项推导与构造无一 `[不成立]`——**`(f)` 与 `(g)` 直接 `[通过]`，其余 7 项均为 `[有缺口可补]`**（主结论与阶数成立，但原报告省去了关键前提、精确误差控制或无函数值下降证明，必须补齐后方可写入论文）。

| 编号 | 核查对象 | 结论 | 捕获的核心缺口 / 关键发现 |
|---|---|---|---|
| **(a)** | $\mathcal{D}_\rho$ 归约到 PZL OS/GS 上界 | `[有缺口可补]` | 光滑常数 $\lt 3R$（精确 $(3+\sqrt{5})R/2$ ）与法锥不降残差均通过；无缓存时计算一次 $\nabla \mathcal{D}_\rho$ 需至多 **3 次**（非 1–2 次）分离 oracle 查询；PZL Alg 1 是否无需函数值需对照原文（见文献核查报告）。 |
| **(b)** | PZL $K=1$ GS 下界迁入 $\mathcal{C}$ | `[有缺口可补]` | 联合光滑性加仿射结构确可推出 $L_{\mathcal{A}}^{\mathrm{inst}} \le 4\ell/D_Y$ ；**捕获三处缺口**：(1) 半球朝向 $\mathbf{c}$ 必须公开或允许空间外查询（隐藏时梯度差不泄露 $\langle \mathbf{c}, \mathbf{z}\rangle$ ），且 $P_{\mathrm{aux}}\mathbf{c} \ne 0$ 时三分量公式失效；(2) OS $\to$ GS 处不能由共同上界推出 $G_{\mathcal{A}}^{\mathrm{inst}} \le L_f^{\mathrm{inst}}$ ，应直接用类常数 $R$ ；(3) 若下界要求显式输出对偶点 $\mathbf{q}$ 需补 $\mathcal{O}(\epsilon^{-1})$ 恢复归约。 |
| **(c)** | PZL/WGY OS 三对角二次项与精确 prox 障碍 | `[有缺口可补]` | 全链非零需**每个次对角元非零**（反例：$M_N = I$ 三对角正定但仅首分量非零）；若有仿射平移且无约束解落在球外，小输入仍触发球约束；耦合块 $N \gt 2$ 确无正满行秩下界。 |
| **(d)** | $\mathcal{C}_\nu$ prox-linear ＋ 对偶强凸 APG 上界 | `[有缺口可补]` | 四条不等式在显式见证残差 $\lVert \mathbf{y} - (\mathbf{a} + J\mathbf{d})\rVert \le \zeta$ 下全成立（OS 常数 $8$ 可收紧为 $2\sqrt{2}$ ）；**捕获重大缺口**：无全局 $\lVert \nabla f\rVert$ 界时，**对偶初始函数值间隙 $\psi(\mathbf{q}_0) - \psi(\mathbf{q}^\star)$ 可无界**（已给反例），必须改用基于初始距离 $\le 2L_h$ 的**定时重启 FISTA**，且有限差分精度 $\eta$ 需按 $3^{-M}$ 指数缩小（精确查询次数仍为 $O(1)$ 但位精度指数依赖 $\kappa_{\mathcal{A}}$ ）；全范围 GS 还需取 $r = \min\{\epsilon/(8R), \sqrt{\epsilon/L_{\mathcal{A}}}\}$ 。 |
| **(e)** | $\mathcal{C}_\nu$ 一维精确 $\epsilon$-KKT 不可达性 | `[有缺口可补]` | 构造成立且覆盖精确软阈值 prox；需补齐三处细节：(1) 严格不等号 $0 \lt \nu \lt G_{\mathcal{A}}$ 必需（一维 $\nu = G_{\mathcal{A}}$ 退化为仿射，一次查询即得根）；(2) 显式给出 $2^{-j}$ 可求和导数预算与保护点 $x_0$ 以固定类常数和 $\Delta$ ；(3) 若排除逐实例有限终止需控制至 $j+2$ 阶导数。 |
| **(f)** | 第 3.1–3.2 节六条度量换算 | `[通过]` | 六条换算常数全部严格成立：包括 $E_\eta \to$ OS 的紧因子 $2$ 、$V_{\mu,\eta} \to$ OS 与 Goldstein 的 $2L_h\mu$ 支撑项、Goldstein $\to$ OS 无需 $F$ 全局 Lipschitz、以及用常微分方程流 $X'(s) = -J_{\mathcal{A}}(X(s))^+(\mathcal{A}(X(s))-\mathbf{y})$ 全局证明 $\lVert \mathbf{x}' - \mathbf{x}\rVert \le \mu/\nu$ （无需额外 $L_{\mathcal{A}}$ 限制）。 |
| **(g)** | 两个平方根损失反例 | `[通过]` | 反例一（GS $\to$ OS 与固定半径 $\delta=1$ Goldstein 均损失 $\Theta(\sqrt{\mu_t})$ ）与反例二（$\nu=1, L_{\mathcal{A}}=0$ 下 Goldstein $\to$ OS 仍损失 $\sqrt{\delta}$ ）在解析与数值上全部成立。 |
| **(h)** | $V_{\mu,\epsilon}$ Moreau 光滑化 ＋ 近端点 ＋ APG 上界 | `[有缺口可补]` | 光滑常数 $H = R + L_h G_{\mathcal{A}}^2/\mu$ 与主阶成立；原报告缺少无函数值 oracle 的外层下降证明，已补齐（内层停在 $\lVert \nabla \phi_k(\mathbf{z}_k)\rVert \le \epsilon/4$ 即可保证所有继续步严格下降 $> 7\epsilon^2/(64R)$ ，且对数项仅依赖 $\Delta_\mu$ 无需全局梯度界）。 |
| **(i)** | 梯度型椭球法 $\widetilde{\mathcal{O}}(d^2 \epsilon^{-2})$ 上界 | `[有缺口可补]` | 主阶成立；已补齐缺失的初始球半径 $D_0 + r$ （$D_0 = \sqrt{2\Delta_\mu/R}, r = \sigma/(2L)$ ）、无函数值中心切割保球证明 $B_r(\mathbf{p}_k)$ 与体积收缩界。 |

---

## 二、报告一推导审查：`(a)–(d)`

### (a) `[有缺口可补]` $\mathcal{D}_\rho$ 归约到 PZL OS/GS 上界

1. **梯度与最大值恒等式（通过）**：由近端最优性得 $\mathbf{q} = \boldsymbol{\lambda} + \rho(\mathcal{A}(\mathbf{x}) - \mathbf{y}) \in \partial h(\mathbf{y})$ ，故 $\lVert \mathbf{q}\rVert \le L_h$ 。写为共轭形式
   $$
   \mathcal{D}_\rho(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \max_{\mathbf{q}}\left\{\langle \mathcal{A}(\mathbf{x}), \mathbf{q}\rangle - h^\ast(\mathbf{q}) - \frac{1}{2\rho}\lVert \mathbf{q} - \boldsymbol{\lambda}\rVert^2\right\},
   $$
   内层唯一最大化解即 $\mathbf{q} = \operatorname{prox}_{\rho h^\ast}(\rho\mathcal{A}(\mathbf{x}) + \boldsymbol{\lambda})$ ，求导得两项梯度公式；取 $\boldsymbol{\lambda} \in \partial h(\mathcal{A}(\mathbf{x})) \subseteq B(\mathbf{0}, L_h)$ 即取到最大值 $F(\mathbf{x})$ 。
2. **联合光滑常数 $\lt 3R$（通过）**：记 $P \in \{R, S\}$ ，缩放 $\boldsymbol{\lambda} = c\mathbf{u}$ 、$c = P/G_{\mathcal{A}}$ 、$\rho = P/G_{\mathcal{A}}^2$ 。利用 $I - \operatorname{prox}_{\rho h^\ast}$ 非扩张性，缩放后四块梯度 Lipschitz 界为 $(R+P, P, P, P)$ ，对称块界矩阵谱范数为 $\frac{1}{2}(R + 2P + \sqrt{R^2 + 4P^2})$ 。当 $P = R$ 时上界为 $\frac{3+\sqrt{5}}{2}R \approx 2.618 R \lt 3R$ ；当 $P = S$ 时严格小于 $3S$ 。无需假设 Hessian 处处存在。特例 $G_{\mathcal{A}} = 0$ 时 $\mathcal{A}$ 为常值，退化为光滑优化。
3. **边界法锥不抵消 GS 残差与原坐标换算（通过）**：令 $U = \{\mathbf{u} : \lVert \mathbf{u}\rVert \le L_h/c\}$ 。因 $\mathbf{q}/c \in U$ ，有 $\nabla_{\mathbf{u}}\mathcal{D}_\rho = P(\mathbf{q}/c - \mathbf{u})$ ，对任意 $\theta \in [0, 1/P]$ 均有 $\mathbf{u} + \theta \nabla_{\mathbf{u}}\mathcal{D}_\rho \in U$ ，故对一切 $\mathbf{n} \in N_U(\mathbf{u})$ 有 $\langle \mathbf{n}, \nabla_{\mathbf{u}}\mathcal{D}_\rho\rangle \le 0$ ，从而 $\operatorname{dist}(\nabla_{\mathbf{u}}\mathcal{D}_\rho, N_U(\mathbf{u})) = \lVert \nabla_{\mathbf{u}}\mathcal{D}_\rho\rVert$ 。换回原坐标时 $\lVert \mathcal{A}(\mathbf{x}) - \mathbf{y}\rVert = (G_{\mathcal{A}}/S)\lVert \nabla_{\mathbf{u}}\mathcal{D}_\rho\rVert \le \lVert \nabla_{\mathbf{u}}\mathcal{D}_\rho\rVert$ ，精度只增不减。
4. **OS Moreau 参数换算（通过）**：$t = 1/(6R)$ 与 $s = 1/(2R)$ 之间，由 $F + \frac{R}{2}\lVert \cdot\rVert^2$ 的次梯度单调性得 $\frac{1}{3}\lVert \nabla F_t(\mathbf{x})\rVert \le \lVert \nabla F_s(\mathbf{x})\rVert \le \frac{5}{3}\lVert \nabla F_t(\mathbf{x})\rVert$ ，只差常数因子。
5. **缺口与修复**：无缓存情形下求 $\nabla \mathcal{D}_\rho(\mathbf{x}, \boldsymbol{\lambda})$ 须按 $\mathcal{A}(\mathbf{x}) \to \operatorname{prox}_{h/\rho} \to J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{q}$ 执行**至多 3 次**分离 oracle 调用（仍为常数因子）；另外需对照 PZL 原文确认 Algorithm 1 不依赖函数值查询（已由文献核查报告确认）。

### (b) `[有缺口可补]` PZL 单批次（$K=1$）GS 下界迁入一般类 $\mathcal{C}$

1. **共轭构造与 Jacobian Lipschitz 常数（通过）**：取闭半球 $Y = \{\mathbf{q} : \lVert \mathbf{q}\rVert \le D_Y/2, \langle \mathbf{c}, \mathbf{q}\rangle \ge 0\}$ ，$h = H^\ast$ 确为全域有限、闭凸、$(D_Y/2)$-Lipschitz。关于 $L_{\mathcal{A}}^{\mathrm{inst}} \le 4\ell / D_Y$ ，利用 $\phi$ 关于 $\mathbf{q}$ 仿射，在 $\mathbf{q}$ 与 $\mathbf{0}$ 两切片应用 $\mathbf{x}$ 方向 $\ell$-光滑性相减得 $\lVert (J_{\mathcal{A}}(\mathbf{x}) - J_{\mathcal{A}}(\mathbf{x}'))^\top \mathbf{q}\rVert \le 2\ell \lVert \mathbf{x} - \mathbf{x}'\rVert$ ；对任一单位向量 $\mathbf{v}$ ，$\pm (D_Y/2)\mathbf{v}$ 至少其一属于 $Y$ ，直接推出 $L_{\mathcal{A}}^{\mathrm{inst}} \le 4\ell / D_Y$ ，**无需额外三阶导数假设**。
2. **缺口 1（半球朝向 $\mathbf{c}$ 与 $P_{\mathrm{aux}}\mathbf{c}$ 正交性）**：
   - 若 $\mathbf{c}$ 隐藏且 saddle oracle 限制查询必须落在 $Y$ 内，梯度差不提供 $\langle \mathbf{c}, \mathbf{z}\rangle$（反例：$P_{\mathrm{aux}} = 0$ 时 $\pm \mathbf{c}$ 梯度完全一致但半球投影不同），首次查询 $J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{v}$ 亦无法保证 $\alpha\mathbf{v} \in Y$ 。**修复**：须将半球朝向 $\mathbf{c}$ 作为公开信息，或明确 saddle oracle 允许在整个空间查询仿射扩展。
   - 仅当 $P_{\mathrm{aux}}\mathbf{c} = \mathbf{0}$ 时三正交分量闭式公式成立；若 $P_{\mathrm{aux}}\mathbf{c} \ne \mathbf{0}$ ，须改用 $W_\beta = ((1+\beta)I + \gamma\ell P_{\mathrm{aux}})^{-1}$ ，先解无半空间约束 $W_\beta \mathbf{z}$ ，再沿 $W_\beta \mathbf{c}$ 补项 $\max\{0, -\langle \mathbf{c}, W_\beta \mathbf{z}\rangle / \langle \mathbf{c}, W_\beta \mathbf{c}\rangle\}$ （初始化时一次查询得 $P_{\mathrm{aux}}\mathbf{c}$ ）。
3. **缺口 2（OS $\to$ GS 常数论证笔误）**：原报告写 $G_{\mathcal{A}}^{\mathrm{inst}} \le L_f^{\mathrm{inst}} \le R$ ，但共同上界 $\le \ell_\ast$ 推不出 $G_{\mathcal{A}}^{\mathrm{inst}} \le L_f^{\mathrm{inst}}$ 。**修复**：直接用 $G_{\mathcal{A}}^{\mathrm{inst}} \le \ell_\ast \le L_f \le R$ （其中 $R$ 为类参数），即可把第二项残差控在 $\epsilon/2$ 。
4. **缺口 3（若下界要求显式输出对偶点 $\mathbf{q}$ ）**：存在性证人可经一次额外查询归约补成显式输出——在 OS 点 $\mathbf{x}$ 处解二次系数 $2R$ 的 prox-linear 子问题，对偶 gap 控至 $\mathcal{O}(\epsilon^2/R)$ 后做一步近端梯度，距离型 FISTA 仅需 $\mathcal{O}(1 + L_h G_{\mathcal{A}}^{\mathrm{inst}} / \epsilon)$ 次查询，远低于 $\epsilon^{-5/2}$ 。

### (c) `[有缺口可补]` PZL/WGY OS 构造的三对角二次项与精确 prox 障碍

1. **全链非零的条件（缺口与修复）**：令 $T = I + \gamma M_N$ 、次对角元 $b_i = T_{i+1,i}$ 。由余子式公式
   $$
   (T^{-1}\mathbf{e}_1)_i = (-1)^{i-1} b_1 \cdots b_{i-1} \frac{\det(T_{i+1:N, i+1:N})}{\det(T)},
   $$
   正定性保证各主子式为正，因此全分量非零**严格要求每个次对角元 $b_i \ne 0$**（如离散拉普拉斯）；反例 $M_N = I$ 满足三对角正定但仅第一分量非零。
2. **球约束与仿射平移（缺口与修复）**：无平移中心球时，取 $0 \lt \lvert \alpha\rvert \lt$ 球半径即可使球约束不活跃，一次 prox 查询即可通过 $T^{-1}\mathbf{e}_1 = [\tau\alpha\mathbf{e}_1 - \operatorname{prox}_{\tau h}(\tau\alpha\mathbf{e}_1)]/(\tau\alpha)$ 恢复逆矩阵首列（且即便中心球活跃，KKT 只在 $T$ 对角线加 $\beta I$ ，仍保持全链非零）。但若加入线性项 $\langle \mathbf{b}, \mathbf{q}\rangle$ 使零输入的无约束解落在球外，小输入仍会触发球约束；若有未知平移且处于不活跃区间，需两次查询相减消去偏移。
3. **耦合块行秩（通过）**：$N \gt 2$ 时 $N \times 2$ 耦合块秩至多 2 ，满行秩最小奇异值为 $0$ ；两个非零奇异值在 $k_N = \Theta(N), N = \Theta(\ell D_Y/\epsilon)$ 下为 $\Theta(\sqrt{\ell\epsilon/D_Y})$ 。

### (d) `[有缺口可补]` $\mathcal{C}_\nu$ 全局满行秩 prox-linear ＋ 对偶强凸 APG 上界

1. **四条不等式与残差定义（通过，常数可收紧）**：统一采用显式见证残差——存在 $\mathbf{y} \in \partial h^\ast(\mathbf{q})$ 使 $\lVert \mathbf{y} - (\mathbf{a} + J\mathbf{d})\rVert \le \zeta$ （因 $\nabla s(\mathbf{q}) = -(\mathbf{a} + J\mathbf{d})$ ，等价于显式 $\operatorname{dist}(\mathbf{0}, \partial\psi(\mathbf{q})) \le \zeta$ ）。在此定义下：
   - 下降 $F(\mathbf{x}) - F(\mathbf{x}+\mathbf{d}) \ge \frac{R}{2}\lVert \mathbf{d}\rVert^2 - 2L_h\zeta$ 、原始残差 $\le 2R\lVert \mathbf{d}\rVert$ 、可行性 $\le \frac{L_{\mathcal{A}}}{2}\lVert \mathbf{d}\rVert^2 + \zeta$ 全部成立；
   - OS 界中由 $P(\mathbf{v}) = F(\mathbf{x}+\mathbf{v}) + R\lVert \mathbf{v}\rVert^2$ 的 $R$-强凸性得 $\lVert \mathbf{v}^\star - \mathbf{d}\rVert^2 \le \lVert \mathbf{d}\rVert^2 + 2L_h\zeta/R$ ，故 $\lVert \nabla F_{1/(2R)}(\mathbf{x})\rVert \le 4R\lVert \mathbf{d}\rVert + 2\sqrt{2RL_h\zeta}$ （原报告系数 $8$ 成立并可收紧为 $2\sqrt{2}$ ）。
2. **重大缺口与修复（无全局梯度界时对偶初始 gap 无界）**：
   - **反例**：取 $h(y) = \lvert y\rvert$ 、$A(x) = x$ 、$f(x) = x^2/8 + \cos(x)/2$ （$L_f = R = 1, L_{\mathcal{A}} = 0$ ）。当 $x \to +\infty$ 时 $q^\star = 1$ ，从 $q_0 = 0$ 出发虽有 $\lvert q_0 - q^\star\rvert = 1$ ，但初始对偶函数值间隙 $\psi(0) - \psi(1) = x - g - 1/2 \to +\infty$ ！因此不能直接用函数值间隙启动内层加速法。
   - **修复方案（距离型定时重启 FISTA ＋ 误差控制）**：每段运行 $M = \lceil 4\sqrt{L/\mu}\rceil$ 步 FISTA，利用距离界 $\psi(\mathbf{q}_M) - \psi^\star \le 2L\lVert \mathbf{q}_0 - \mathbf{q}^\star\rVert^2/(M+1)^2$ 使段末距离减半，首段仅需 $\mathbf{q}_0 \in \operatorname{dom} h^\ast$ 保证 $\lVert \mathbf{q}_0 - \mathbf{q}^\star\rVert \le 2L_h$ 。若单步差分梯度误差至多 $\eta$ ，轨迹偏差至多 $3^M \eta / L$ ；令 $D = \zeta/(8L)$ 、取 $\eta \le L D / (4 \cdot 3^M)$ ，并按当前精确 $\mathbf{w} = \mathbf{g} + J^\top \mathbf{v}$ 选前向差分步长 $0 \lt \delta \le 2R\eta / (L_{\mathcal{A}}\lVert \mathbf{w}\rVert^2)$ ，经 $\mathcal{O}(1 + \log_+(L L_h / \zeta))$ 段即得 $\lVert \mathbf{v} - \mathbf{q}^\star\rVert \le D$ ，最后补一步近端梯度 $\mathbf{q} = \operatorname{prox}_{h^\ast/L}(\mathbf{v} - \widetilde{\nabla}s(\mathbf{v})/L)$ 构造显式见证 $\mathbf{y}$ 。**注**：$\lVert \mathbf{g}\rVert$ 与 $3^M$ 仅影响 $\delta$ 的数值尺度，精确实数查询模型下内层迭代界不依赖全局梯度界，但位复杂度对 $\kappa_{\mathcal{A}}$ 呈指数敏感。
3. **全精度范围的 GS 阈值修复**：取 $r = \epsilon/(8R)$ 、$\zeta = R r^2/(8L_h)$ 对 OS 全局成立，但对 GS 需 $(L_{\mathcal{A}}/2)r^2 + \zeta \le \epsilon$ （$\epsilon \le R L_h$ 时自动满足）；若覆盖所有 $\epsilon \gt 0$ ，取 $r = \min\{\epsilon/(8R), \sqrt{\epsilon/L_{\mathcal{A}}}\}$ 、$\zeta = \min\{R r^2/(8L_h), \epsilon/2\}$ 。

---

## 三、报告二推导审查：`(e)–(i)`

### (e) `[有缺口可补]` $\mathcal{C}_\nu$ 一维精确 $\epsilon$-KKT 不可达性

1. **核心障碍（通过）**：对 $x \ne x_\star$ 有 $\operatorname{dist}(0, \partial F(x)) = L_h A'(x) \gt L_h\nu$ ，故 $\epsilon \lt L_h\nu$ 必须精确输出 $x_\star$ ；软阈值 $\operatorname{prox}_{t h}$ 不泄露 $A$ 的根位置。
2. **缺口与补全**：
   - **严格不等号 $0 \lt \nu \lt G_{\mathcal{A}}$ 必需**：一维 $\nu = G_{\mathcal{A}}$ 时连续导数恒等于 $\pm G_{\mathcal{A}}$ ，$A$ 必为仿射函数，一次查询 $(A, A')$ 即精确求出零点。
   - **显式预算与初始 gap 保护**：取 $A_0(x) = s(x - x_0) + \Delta/(4L_h)$ （$s = (\nu+G_{\mathcal{A}})/2, \sigma = \min\{s-\nu, G_{\mathcal{A}}-s\}$ ），将 $x_0$ 列为保护点并给第 $j$ 次光滑 bump $b(x) = \alpha\psi((x-\xi)/w)$ 的 $0, 1, 2$ 阶导数分配预算 $2^{-j}\Delta/(4L_h), 2^{-j}\sigma/2, 2^{-j}L_{\mathcal{A}}/2$ 。因当前零点不在历史查询点中，总存在 $w \gt 0$ 避开历史查询点与 $x_0$ ，再选非零 $\alpha$ 同时满足三项预算即可移走零点且保持 $F(x_0) - \inf F = \Delta/4$ 。
   - **量词说明**：上述预算覆盖任意有限查询预算 $T$ 的确定性算法；若需排除逐实例有限终止（无预设预算），再为第 $j$ 个 bump 补加直至 $j+2$ 阶导数的可求和预算即可使无限 transcript 对应一个固定光滑极限实例。

### (f) `[通过]` 第 3.1–3.2 节六条度量换算

六条换算经逐行验算全部严格通过，关键核对点如下：
1. **$E_\eta \to$ OS（系数 2 紧）**：由 $R$-弱凸性得 $\langle \mathbf{g} - \mathbf{m}, \mathbf{x} - \mathbf{p}\rangle \ge -R\lVert \mathbf{x} - \mathbf{p}\rVert^2$ ，推出 $\lVert \mathbf{g}\rVert \ge (1 - \lambda R)\lVert \mathbf{m}\rVert = \frac{1}{2}\lVert \mathbf{m}\rVert$ 。一维 $F(x) = R\cos x$ 在 $x \to 0$（或 $F(x) = -\frac{R}{2}x^2 + \eta x$ 在 $x = 0$ ）处比值严格达到 $2$ 。
2. **OS $\to V$（系数 $3/2$ 与 $G_{\mathcal{A}}/(2R)$ 准确）**：将 $\mathbf{p}$ 处的次梯度证人 $\mathbf{q} \in \partial h(\mathcal{A}(\mathbf{p}))$ 移到 $\mathbf{x}$ ，由 $R$-弱凸与 $G_{\mathcal{A}}$-Lipschitz 直接得出。
3. **$V_{\mu,\eta} \to$ 支撑不等式 / OS / Goldstein（全部准确）**：
   - 支撑误差项 $2L_h\mu$ 不能缩小为 $L_h\mu$ （反例：$A(z)=z, h(u)=L_h\lvert u\rvert, f(z)=L_h z$ ，在 $x=\mu, y=0, q=-L_h$ 处 $v=0$ 而 $F(\mu) - F(0) = 2L_h\mu$ ）。
   - 导出 $\eta + \sqrt{\eta^2 + 8RL_h\mu}$ 时，需用近端目标的 **$R$-强凸额外下降** $F(\mathbf{x}) - F(\mathbf{p}) \ge \frac{3R}{2}D^2$ 与支撑不等式联立得 $RD^2 \le \eta D + 2L_h\mu$ 。
   - Goldstein 换算：在闭球 $B_r(\mathbf{x})$ 上最小化 $F(\mathbf{z}) + \beta\lVert \mathbf{z} - \mathbf{x}\rVert$ （$\beta = \eta + Rr/2 + 2L_h\mu/r$ ），支撑不等式保证边界值 $\ge F(\mathbf{x})$ ，从而存在内点极小解，Fermat 条件直接给出 $G_{\delta,\beta}(\mathbf{x})$ ，无任何常数放大。
4. **Goldstein $\to$ OS（无需 $F$ 全局 Lipschitz）**：闭球上次梯度并集紧，取有限凸组合 $\bar{\mathbf{q}} = \sum \omega_i \mathbf{q}_i$ 后，$\lVert \nabla f(\mathbf{x}) + J_{\mathcal{A}}(\mathbf{x})^\top \bar{\mathbf{q}}\rVert \le \eta + R\delta = a$ ；$f$ 的影响已由梯度差 $L_f\delta$ 吸收进 $a$ ，而 $B = L_h G_{\mathcal{A}}$ 仅控制 $h$ 的凸支撑误差 $2B\delta$ ，代入强凸近端论证即得 $a + \sqrt{a^2 + 8RB\delta}$ 。
5. **Goldstein $\to V_{\mu,\cdot}$（准确）**：对上述 $\bar{\mathbf{q}}$ 取 $\tau = \mu^2 / (2B\delta)$ ，令 $\mathbf{y} = \operatorname{prox}_{\tau h}(\mathcal{A}(\mathbf{x}) + \tau\bar{\mathbf{q}})$ 、$\mathbf{q} = \bar{\mathbf{q}} + (\mathcal{A}(\mathbf{x}) - \mathbf{y})/\tau \in \partial h(\mathbf{y})$ ，精确与误差支撑联立得 $\lVert \mathcal{A}(\mathbf{x}) - \mathbf{y}\rVert \le \mu$ 且 $\lVert \mathbf{q} - \bar{\mathbf{q}}\rVert \le 2B\delta/\mu$ ，乘以 $G_{\mathcal{A}}$ 即得所列界。
6. **满行秩全局恢复（准确，无额外 $L_{\mathcal{A}}$ 限制）**：考虑常微分方程流 $X'(s) = -J_{\mathcal{A}}(X(s))^+ (\mathcal{A}(X(s)) - \mathbf{y})$ ，全局满行秩保证 $\mathcal{A}(X(s)) - \mathbf{y} = e^{-s}(\mathcal{A}(\mathbf{x}) - \mathbf{y})$ 与 $\lVert X'(s)\rVert \le e^{-s}\mu/\nu$ ，速度界排除有限时间逃逸且总弧长 $\le \mu/\nu$ ，极限点 $\mathbf{x}'$ 满足 $\mathcal{A}(\mathbf{x}') = \mathbf{y}$ 与 $\lVert \mathbf{x}' - \mathbf{x}\rVert \le \mu/\nu$ 。再结合 $\nabla F_\lambda$ 的 $2R$-Lipschitz 性与第 1 条，直接得出 $\lVert \nabla F_\lambda(\mathbf{x})\rVert \le 2\eta + 4R\mu/\nu$ 。

### (g) `[通过]` 两个平方根损失反例

1. **反例一（GS $\to$ OS 及固定半径 $\delta = 1$ Goldstein）**：因 $A(x) = \sqrt{1+x^2}-1 \ge 0$ 故 $F_t(x) = a_t x + g(x)$ ；$f_t''$ 在 $\lvert x\rvert \lt 2$ 为 $-A'' \in [-1, 0)$ 、在 $\lvert x\rvert \gt 2$ 为 $1 - A'' \in (0, 1)$ 且 $f_t'$ 在 $\pm 2$ 连续，故 $L_f = 1$ 。极小点在 $-2 - a_t$ ，$x_0 = 0$ 或 $t$ 均有 $\Delta \le 4$ 。在 $x = t \in (0, 1/2)$ 处，$y = 0, q = -1$ 满足精确原始残差 $0$ 与 $\mu_t = A(t) = \Theta(t^2)$ ；Moreau 近端点 $t - a_t/4 \in (-2, 2)$ 给出 OS 残差恰为 $a_t = \Theta(\sqrt{\mu_t})$ ；$[t-1, t+1] \subset (-2, 2)$ 给出半径 $1$ 的 Goldstein 残差同样恰为 $a_t = \Theta(\sqrt{\mu_t})$ 。
2. **反例二（$\nu = 1, L_{\mathcal{A}} = 0$ 下 Goldstein $\to$ OS 仍损失 $\sqrt{\delta}$ ）**：对 $0 \lt \delta \le 1$ ，三个仿射分支梯度范数为 $2, 2, \sqrt{\delta}$ ，故 $L_h = 2, R = 1$ 。在 $(\pm\delta, \sqrt{\delta}, 0)$ 处次梯度为 $(\pm 2, 0, 0)$ 且距 $\mathbf{x}_\delta$ 为 $\delta$ ，故 $G_{\delta,0}(\mathbf{x}_\delta)$ 成立；近端点恰为 $(0, \sqrt{\delta}/2, 0)$ ，故 $\lVert \nabla F_{1/2}(\mathbf{x}_\delta)\rVert = \sqrt{\delta}$ ，且 $F(\mathbf{x}_\delta) - \inf F = \delta \le 1$ 。

### (h) `[有缺口可补]` $V_{\mu,\epsilon}$ 的 Moreau 光滑化 ＋ 近端点 ＋ 加速梯度上界

1. **光滑性与证书（通过）**：$t = \mu/L_h$ 时 $0 \le F - F_t \le L_h\mu/2$ ，$F_t$ 为 $R$-弱凸且梯度 Lipschitz 常数为 $H = R + L_h G_{\mathcal{A}}^2/\mu$ ；计算一次 $\nabla F_t(\mathbf{x})$ 在无缓存时需至多 3 次分离 oracle 调用（$\mathcal{A}(\mathbf{x}) \to \operatorname{prox}_{t h} \to J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{q}$ ）。
2. **缺口与修复（无函数值 oracle 的外层下降证明）**：令 $\phi_k(\mathbf{z}) = F_t(\mathbf{z}) + R\lVert \mathbf{z} - \mathbf{x}_k\rVert^2$ （$R$-强凸、$L = H + 2R$ 光滑），内层从 $\mathbf{x}_k$ 启动强凸加速梯度法，停在 $\lVert \nabla \phi_k(\mathbf{z}_k)\rVert \le \epsilon/4$ 。若 $\lVert \nabla F_t(\mathbf{z}_k)\rVert \le \epsilon$ 则直接输出（终止步由梯度验收，无需下降）；否则 $D_k = \lVert \mathbf{z}_k - \mathbf{x}_k\rVert \gt 3\epsilon/(8R)$ ，结合 $\phi_k(\mathbf{z}_k) - \min \phi_k \le \epsilon^2/(32R)$ 立即推出严格下降
   $$
   F_t(\mathbf{x}_k) - F_t(\mathbf{z}_k) \ge R D_k^2 - \frac{\epsilon^2}{32R} \gt \frac{7\epsilon^2}{64R}.
   $$
   于是继续步数至多 $\mathcal{O}(R\Delta_\mu/\epsilon^2)$ ，且外层单调保证每步 $\phi_k(\mathbf{x}_k) - \min \phi_k \le \Delta_\mu$ ，内层用 $\mathcal{O}(\sqrt{L/R}\log(2 + L\Delta_\mu/\epsilon^2))$ 次梯度查询即达标，**全程无需函数值查询与全局梯度界**。

### (i) `[有缺口可补]` 梯度型椭球法的 $\widetilde{\mathcal{O}}(d^2\epsilon^{-2})$ 上界

1. **平滑参数与外层衔接（补齐）**：在 `(h)` 中取 $\eta = \epsilon/4$ 、$\mu = \epsilon^2/(16RL_h)$ ，则 `(f3)` 保证输出满足 $\epsilon$-OS，此时 $L/R = 3 + 16B^2/\epsilon^2$ ，内层梯度阈值取 $\sigma = \epsilon/16$ 。
2. **缺口与修复（初始球半径、保球性质与体积论证）**：
   - 由 `(h)` 的外层下降，每个中心满足 $R\lVert \mathbf{p}_k - \mathbf{x}_k\rVert^2 \le \Delta_\mu$ ，故 $D_0 = \sqrt{2\Delta_\mu/R}$ 有效；但为在初始即包含整个小目标球 $B_r(\mathbf{p}_k)$ （$r = \sigma/(2L)$ ），初始球半径须取 **$D_0 + r$**。
   - 若椭球中心 $\mathbf{z}$ 满足 $\lVert \mathbf{g}\rVert = \lVert \nabla\phi_k(\mathbf{z})\rVert \gt \sigma$ ，作中心切割 $\langle \mathbf{g}, \mathbf{w} - \mathbf{z}\rangle \le 0$ 。由凸性与光滑下降得 $\langle \mathbf{g}, \mathbf{z} - \mathbf{p}_k\rangle \ge \phi_k(\mathbf{z}) - \phi_k(\mathbf{p}_k) \ge \lVert \mathbf{g}\rVert^2/(2L)$ ，因此 $\mathbf{p}_k$ 到切割超平面的距离至少 $\lVert \mathbf{g}\rVert/(2L) \gt r$ ，整个 $B_r(\mathbf{p}_k)$ 保留在可行半空间内（全程仅查询梯度）。
   - 中心切割使体积每步乘以至多 $\exp(-1/[2(d+1)])$ ，故在 $\mathcal{O}(d^2 \log(2 + D_0/r)) = \mathcal{O}(d^2 \log(1/\epsilon))$ 步内必遇某个满足 $\lVert \mathbf{g}\rVert \le \sigma$ 的中心并直接返回，总复杂度 $\widetilde{\mathcal{O}}(d^2(1 + R\Delta/\epsilon^2))$ 成立。

---

## 四、Python 数值检验汇总

依据 `research-workflow.md` 协同规则第 3 条，在纯 NumPy 脚本上对关键反例与核心不等式完成独立数值校验（全部 0 违例）：

| 检验项 | 样本规模 / 参数 | 结果与最坏情况 |
|---|---|---|
| 反例一（GS $\to$ OS 与 $\delta=1$ Goldstein） | $t \in \{0.4, 0.1, 10^{-2}, 10^{-4}\}$ | `|f+|A|-F| = 8.9e-16`，$L_f = 1.0000$，$\Delta \le 2.06 \le 4$，原始残差 `0.0`，`os == a_t` 至 6 位小数，`os/sqrt(mu) -> 2.8284`（$= 2\sqrt{2}$ ），$B_1(t) \subset [-2, 2]$ 全通过。 |
| 反例二（$\nu=1, L_{\mathcal{A}}=0$ Goldstein $\to$ OS） | $\delta \in \{0.5, 0.1, 10^{-2}, 10^{-4}\}$ | 数值 Moreau 梯度精确等于 $\sqrt{\delta}$ ，$L_h = 2.0000$ ，$F(\mathbf{x}_\delta) - \inf F = \delta$ 全通过。 |
| $\mathcal{D}_\rho$ 边界法锥内指与联合光滑界 | 1000 组随机 4D 实例 | $\langle \boldsymbol{\lambda}, \nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho\rangle \le 0$ 违例 **0/1000**；缩放后块界谱范数比 $R$ 精确为 `2.618034`（$\lt 3.0$ ）。 |
| 三对角 $M_N$ 逆矩阵全分量非零 | $N \in \{5, 10, 20, 40\}$ | 离散拉普拉斯 $(I + 0.5 M_N)^{-1}\mathbf{e}_1$ 全部坐标严格为正（最小分量 $3.36\times 10^{-23}$ ）。 |
| $\mathcal{C}_\nu$ `(d)` 节三条核心不等式 | 500 组随机 5D$\to$3D 非线性满行秩实例 | 下降、原始残差、可行性违例均为 **0/500**。 |
| 第 3.1 节换算不等式与 Moreau 光滑化 | 1000 组随机 1D 非线性复合实例 | $V_{\mu,\eta} \to$ OS（0/1000，最大比值 `0.8074`）、OS $\to$ GS（0/1000）、Goldstein $\to$ OS（0/1000，最大比值 `0.8470`）、$0 \le F - F_t \le L_h\mu/2$ （0/1000）；$E_\eta \to$ OS 紧测试精确达因子 `2.0000`。 |
