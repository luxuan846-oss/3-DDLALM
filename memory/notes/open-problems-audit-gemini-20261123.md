# 开放问题调研报告独立核查（文献、引用与稿件对齐）

- **核查日期**：2026-11-23
- **核查模型**：Gemini 4 Neon（High）
- **模型说明**：本地 Claude Code CLI（`/opt/homebrew/bin/claude`）因账号订阅逾期（`payment is past due`）在默认、`--model fable` 与 `--model opus` 下均无法调用，Antigravity 内置 Claude 配额亦为 0%。经 coordinator 授权，本独立核查由 Gemini 4 Neon（High）直接基于本地缓存全文（`memory/literature/`）、远程拉取的 arXiv HTML/PDF 与期刊/会议全文（共核查全部 21 篇被引用文献全文）以及本稿源码（`overleaf/sections/Preliminaries.tex`、`LRALMFamily.tex`、`Acceleration.tex`）完成。
- **范围**：核查 GPT Pro 针对大问题一与大问题二的两份阶段 1 调研报告中的全部文献引用、定理/引理/假设/公式编号、遗漏文献以及与本稿和 6 子问题定稿的对齐情况（数学推导与反例的逐行验算由 `codex-audit` 负责）。

---

## 一、核心结论

1. **文献准确度高（21 篇全文本核查）**：GPT Pro 两份报告引用的 21 篇核心论文（含 2026 年 9–11 月最新 arXiv 预印本）全部真实存在，几乎所有定理/引理/公式编号与核心结论均与原文一致；其发现的 **Zhu–Chen–Zhang–Wen（`2308.06470v1`）§2.2 步长笔误**经原文核实完全属实。
2. **捕获 5 处实质偏差或前提错配（`[有误或夸大]`）**：
   - Drusvyatskiy–Paquette（MP 2019）Appendix C 去对数因子的出处定位不准（`Theorem C.1` 只是内层加速算法界，去对数总复杂度在第 57–58 页推导段）；
   - Pan–Zheng–Li（`2609.14235v2`）§4.3.1 的记号 $B_N$ 在 GPT Pro 报告一中被误用作耦合块记号（原文中 $B_N := M_N^{-1}$ ）；
   - Kornowski–Shamir（`2209.10346v2`）Theorem 3 的适用范围（高维随机算法、$\delta \le 1/(12\epsilon)$ ）在摘要表里写得过宽；
   - **与本稿 `Preliminaries.tex` 的两处重大前提错配**：本稿 `Assumption~\ref{ass:smoothness}` 明确假设梯度有界（$G_f$ ），故目标 $F$ 实际全局 Lipschitz，而 GPT Pro 因提示词未给 $G_f$ 反复判定 $F$ 未必全局 Lipschitz；本稿 `Definition~\ref{def:oracle-model}` 返回完整 Jacobian 矩阵与 $f(\mathbf{x})$ ，而 GPT Pro 调研基于无 $f(\mathbf{x})$ 且仅含转置乘积 $J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{v}$ 的弱 oracle；
   - 用户 6 子问题定稿中引用 `Preliminaries.tex` 的行号已因近期改稿发生偏移，且原注释掉的 $\nu$ 正则假设已不在当前 `Preliminaries.tex` 内。
3. **补出 6 篇关键遗漏文献（`[补充遗漏]`）**：重点包括 Liu–Deng–Wang–Wen（`2608.19847`，一致 LICQ 下固定罚线性化 ALM 的 $\mathcal{O}(\epsilon^{-2})$ ）、Zhu–Li（`2607.08954`，局部锥正则加分段线性外函数的一阶 ALM $\mathcal{O}(\epsilon^{-2})$ ）以及 Tian–So（MP 2024）、Liao–Zheng（`2509.02804`）、Zhang–Xu（`2609.17973`）、Ke–Mei–Zhang（`2609.25752`）、Zhang–Luo（SIOPT 2020/2022）。
4. **对两项核心空白的独立核实**：经全文与检索交叉核查，目前确实未见到直接以分离矩阵–向量积加精确 $\mathrm{prox}_h$ 证明「一般 Lipschitz 凸 $h$ 加非线性全局满行秩 $\mathcal{A}$ 上 $\widetilde{\mathcal{O}}(\mathrm{poly}(1/\nu)\,\epsilon^{-2})$ 」或「该 oracle 下精确 $\epsilon$-KKT 不可达」的现成期刊/预印本定理；但后续立项必须与 `2608.19847`（强线性系统步）和 `2607.08954`（局部正则加分段线性 $h$ ）清晰切割。

---

## 二、逐篇文献全文核查表（21 篇）

### 2.1 报告一（大问题一：复杂度定位与下界）

| 文献 | 状态 | 核查来源 | 核查结果与原文要点 |
|---|---|---|---|
| **Pan–Zheng–Li (2026)**, `arXiv:2609.14235v2` (2026-10-22) | `[已核实]` / `[有误或夸大]`（记号） | 拉取 v2 全文 PDF | Defs 2.1–2.4、Theorems 3.1–3.4、Lemma 3.2、§4.3.1 eqs (9)–(10)、eqs (16)/(18)/(49)/(101)、Lemma A.1、§5.4 eqs (30)–(31)、Lemma 5.2、Lemma 8.4、eqs (78)–(80) 与常数 $c_5$ 均核实无误。**记号偏差**：GPT Pro 报告一 §一.3 将耦合块写为 $B_N$ ，但原文 §4.3.1 定义 $B_N := M_N^{-1}$ ，耦合项为 $k_N^{-1/2}\langle a\mathbf{e}_1 - b\mathbf{e}_N, w\rangle$ 。 |
| **Wu–Gu–Yang (2026)**, `arXiv:2609.14233v1` (2026-09-13) | `[已核实]` | 本地缓存 `2609.14233v1.txt` | Defs 2.1–2.6（仅 zero-respecting 算法）、eqs (16)–(17)（三对角路径块 $B_{\alpha,N}$ 及原始球约束）、Theorem 4.1 & eq (31)、Corollary 4.2、§6 公开问题（beyond zero-respecting 与 separate primal/dual oracle complexities）全部与原文吻合。 |
| **Drusvyatskiy–Paquette (2019)**, *Math. Program.* 178:503–558 | `[已核实]` / `[有误或夸大]`（定位） | 拉取作者全文 PDF | Proposition 3.3、Theorem 4.5（一般式 (4.4)，$t=1/\mu$ 特例 (4.8) 常数 $\frac14$ 与 $\frac32(1+1/\sqrt{2})$ ）、Theorem 5.6、§6.3 eq (6.21) 均准确。**定位偏差**：`Theorem C.1` 仅给出内层 Algorithm 13 的 $8lL^2/(j+2)^2$ 误差界；去掉对数因子的总复杂度 $O(L^2 \beta \|\nabla c\| \Delta / \epsilon^3)$ 在其后的第 57–58 页推导段，非 Theorem C.1 本身。 |
| **Zhu–Chen–Zhang–Wen (2023)**, `arXiv:2308.06470v1` | `[已核实]` | 拉取 v1 HTML 全文 | Theorem 3.2、Corollary 2、Theorem 4.3、Corollary 8、eqs (21)–(22)、Lemma 4（$AA^\top$ 特征值 $2+2\cos(\pi i / (2N))$ ，推出最小奇异值 $2\sin(\pi/(4N))$ ）均准确。**特别核实**：§2.2 笔误完全属实——原文确将非凸残差印成前向步长 $1/(2L_f)$ 配 prox 参数 $1/L_f$ ，零点对应 $f+2h(Ax-b)$ 。 |
| **Liu–Lin–Xu (2023 & 2025/2026)**, `arXiv:2307.07605` & `2502.17770v2` / *MOR* 51(2), 2026 | `[已核实]` | 拉取 `2502.17770v2` HTML 与 `2307.07605` PDF | `2502.17770v2` 的 $\mathrm{ORACLE}_1$/$\mathrm{ORACLE}_2$、Algorithm Classes 1–2（linear-span）、Theorem 2.19、Theorem 3.3（显式常数 $72000\pi^2$ ）、Lemma 2.7（$m/4 \le \kappa([\bar{\mathbf{A}};\mathbf{A}]) \lt m$ ）、§3 *Tightness of Lower Complexity Bounds*，以及 `2307.07605` 的 Assumptions 1, 4, 5、Theorem 4.3、Corollary 4.1(a)、eq (4.50) 全部核实无误。 |
| **Shi–Wang (2026)**, Optimization Online 2026-06-28 (`CLB.pdf`) | `[已核实]` | 拉取 Optimization Online PDF | 光滑等式约束、完整 Jacobian oracle、Theorem 1 可行性下界、Theorem 3 eq (24) 驻点下界、Theorem 4 精确线性化子问题上界（含 $\sqrt{n}G$ ）全部与原文一致。 |
| **Li–Pan (2026)**, `arXiv:2608.03246v3` (2026-11-13) | `[已核实]` | 拉取 v3 HTML 全文 | v3 标题确为 *Optimal Oracle Complexity for Weakly Convex Optimization*（较项目旧笔记中的 v1 标题已去掉 Deterministic），Theorem 2 覆盖任意随机与确定性一阶算法（完整次微分 oracle），下界 $\Omega(\rho G^2 \Delta \epsilon^{-4})$ 核实无误。 |
| **Carmon–Duchi–Hinder–Sidford (2020)**, *Math. Program.* 184:71–120 (`1710.11606`) | `[已核实]` | 拉取 PDF 全文 | Theorem 1 给出确定性高阶/一阶光滑非凸下界 $\Omega(L_f \Delta \epsilon^{-2})$ ，核实无误。 |
| **Lin–Jin–Jordan (2020)**, *COLT* 2020, PMLR 125:2738–2779 | `[已核实]` | 拉取 PMLR PDF 全文 | Corollary 13（$\widetilde{\mathcal{O}}(\epsilon^{-5/2})$ ）、Corollary 21（$\widetilde{\mathcal{O}}(\epsilon^{-3})$ ）及随机选取/投影梯度映射差异说明均准确。 |
| **Kovalev–Gasnikov (2022)**, *NeurIPS* 35 (`2205.05653`) | `[已核实]` | 拉取 NeurIPS PDF 全文 | Theorem 3 eq (34) 与 Corollary 1 eq (35) 的 $O((L/\sqrt{\mu_x \mu_y})\log(1/\epsilon))$ 复杂度均与原文一致。 |

### 2.2 报告二（大问题二：可达性、度量换算与 Goldstein 复杂度）

| 文献 | 状态 | 核查来源 | 核查结果与原文要点 |
|---|---|---|---|
| **Zhang–Lin–Jegelka–Sra–Jadbabaie (2020)**, *ICML* 2020 | `[已核实]` | 拉取 PMLR 主文与补充材料 PDF | Assumption 1、Theorem 5（有限步精确 $\epsilon$-驻点不可达）、补充材料 Lemma 12（有限查询点处值与梯度一致但驻点集不交的函数族）、Theorem 8（INGD 高概率界 $192\Delta L^2/(\delta\epsilon^3)\log(4\Delta/(\gamma\delta\epsilon))$ ，确定性 oracle 但算法含随机采样）全部核实无误。 |
| **Kornowski–Shamir (2021 / JMLR 2022)**, *JMLR* 23(314) | `[已核实]` | 拉取 JMLR PDF 全文 | Theorem 1（局部 oracle 下常数邻近驻点的维数指数下界）与 Proposition 11（一维隐藏极小点构造）核实无误。 |
| **Kornowski–Shamir (`2209.10346v2`)** | `[已核实]` / `[有误或夸大]`（范围） | 拉取 v2 HTML 全文 | Theorem 5（一维凸 1-Lipschitz 逼近小次梯度下界）核实无误。**范围补充**：Theorem 3 针对的是随机一阶算法在 $\delta \le 1/(12\epsilon)$ 与 $d = \widetilde{O}(\epsilon^{-6})$ 下的 $(\delta,\epsilon)$-Goldstein 下界，并非任意固定 $\delta$ 下的通用下界。 |
| **Böhm–Wright (2021)**, *JOTA* 188 (`2003.07612`) | `[已核实]` | 拉取 arXiv PDF 全文 | §3.2 eqs (13)–(19)、eq (25)（$x_j^* = x_j - A^\dagger(Ax_j - \operatorname{prox}_{\mu_j g}(Ax_j))$ ）与 Corollary 4.1（满行秩仿射下 $O(\epsilon^{-3})$ 精确驻点保证）全部核实无误。 |
| **Bareilles–Iutzeler–Malick (2023)**, *SIOPT* 33(3) (`2206.15053v3`) | `[已核实]` | 拉取 v3 HTML 全文 | Theorem 14（值域活动流形识别）与 Theorem 24（强局部极小下的有限识别与局部二次收敛）以及需显式流形/二阶 SQP 信息的限定全部核实无误。 |
| **Davis–Drusvyatskiy (2019)**, *SIOPT* 29(1):207–239 | `[已核实]` | 拉取作者 PDF 全文 | Lemma 2.2 与 eq (2.6) 的 Moreau 包络光滑性及基本关系核实无误。 |
| **Tian–Zhou–So (2022)**, *ICML* 2022 | `[已核实]` | 拉取 PMLR PDF 全文 | Proposition 2.7（多面体反例）、Definition 4.2（$(\delta,\eta,\kappa)$-OLC）、Theorem 4.4（GAS 推 NAS）、Theorem 4.5（紧集存在性）、Remark 4.6（明确指出常数 $\eta$ 一般难以估计）、Proposition 4.9（满行秩线性复合参数变换）全部核实无误。 |
| **Davis–Drusvyatskiy–Lee–Padmanabhan–Ye (2022)**, *NeurIPS* 35 | `[已核实]` | 拉取 NeurIPS PDF 全文 | Theorem 6（$\widetilde{\mathcal{O}}(\Delta L^2/(\delta\epsilon^3))$ ）与 Theorem 8（一般 $L$-Lipschitz 给出 $\widetilde{\mathcal{O}}(\Delta L d/(\delta\epsilon^2))$ ；$\rho$-弱凸时以概率 1 改进为 $\widetilde{\mathcal{O}}(\Delta d/(\delta\epsilon)\cdot\log(L/\epsilon)\log(\delta\rho/\epsilon))$ ，仍含随机采样）全部核实无误。 |
| **Jordan–Kornowski–Lin–Shamir–Zampetakis (2023)**, *COLT* 2023 | `[已核实]` | 拉取 PMLR PDF 全文 | Theorem 1（$\Omega(d)$ ）、Theorem 2（无函数值时不可达）、Theorem 5（$H$-smooth 下 $\log(H)$ 依赖上界）全部核实无误。 |
| **Kong–Lewis (2024)**, *MOR* 49(4):2385–2401 | `[已核实]` | 拉取 NSF PAR PDF 全文 | Oracle 1（方向次梯度 oracle）、Theorem 4、Proposition 4（$\rho$-弱凸时 $\Lambda(\delta) \le \rho\delta/2$ ）全部核实无误。 |
| **Kornowski (2026)**, `arXiv:2609.17780v1` | `[已核实]` | 本地缓存 `2609.17780v1.html/txt` | Definition 2.1（Goldstein）、Theorem 3.1（zero-respecting 下界 $\Omega(\Delta L^2/(\delta\epsilon^3))$ ）、Definition 2.2（Zhang–Cutkosky 的 $(\lambda,\epsilon)$-stationarity）、Theorem 3.2（$\Omega(\Delta L^2\sqrt{\lambda}/\epsilon^{7/2})$ ）全部核实无误。 |
| **Kornowski (2026)**, `arXiv:2609.23837v1` | `[已核实]` | 拉取 HTML 全文 | Theorem 3.1（$\delta \lt \Delta/L, \epsilon \lt L/32, d \ge \lceil 2\log_2(L/(8\epsilon))\rceil$ 时的指数下界）与 §5.1 Regularity（$C^1$ mollification 无统一固定光滑常数）全部核实无误。 |
| **Ding–Yuan (2026)**, `arXiv:2609.38082v2` | `[已核实]` | 拉取 v2 HTML 全文 | Theorem 2.2（$d \ge 3, 0 \lt \epsilon \lt L/3$ 时的 $((L-\epsilon)/(2\epsilon))^{(d-2)/2}$ 指数下界）、Theorem 2.3（零阶确定性上界）、Proposition D.1（非有限参数弱凸函数）、§6.1–6.2 公开问题全部核实无误。 |

---

## 三、遗漏文献补充（`[补充遗漏]` 与 `[待核原文]`）

GPT Pro 两份报告在以下与 $\mathcal{C}_\nu$ 上界、局部正则性、单循环 $\mathcal{D}_\rho$ 上界及确定性非光滑不可达性直接相关的文献上存在遗漏：

1. **`[补充遗漏]` Liu–Deng–Wang–Wen (2026), `arXiv:2608.19847`**（*A Fixed-Penalty Linearized Augmented Lagrangian Method with Classical Multiplier Updates*，本地 `memory/literature/readings/2608.19847v1/` 已有 PDF）：在一致 LICQ（满行秩正则）下以固定罚线性化 ALM 达到 $\mathcal{O}(\epsilon^{-2})$ 。与本题的关键区分在于其每步求解 Jacobian 线性方程组（Gauss–Newton 型原语），强于矩阵–向量积 oracle。
2. **`[补充遗漏]` / `[待核原文]` Zhu–Li (2026), `arXiv:2607.08954`**（*Nonconvex Composite Functional Constraints via First-Order Augmented Lagrangian Methods under Local Regularity*）：在非线性复合问题与**局部锥正则性**加分段线性外函数下，一阶 ALM 达到 $\mathcal{O}(\epsilon^{-2})$ 。它直接关联「局部正则性替代全局满行秩」这一空白；本次依据本地 `memory/notes/project/lower-bound-references.md` 补列，尚未重新拉取全文核对局部锥正则的精确量化条件与常数依赖（标为 `[待核原文]`）。
3. **`[补充遗漏]` Tian–So (2024), *Math. Program.***（*No dimension-free deterministic algorithm computes approximate stationarities of Lipschitzians*）：确定性局部 oracle 下的核心不可达性与维数下界文献，亦为 Ding–Yuan（`2609.38082v2`）local oracle 定义的直接出处；报告二未单独核列。
4. **`[补充遗漏]` Zhang–Xu (2026), `arXiv:2609.17973`** 与 **`Ke–Mei–Zhang (2026), `arXiv:2609.25752`**（本地 `memory/literature/complexity_2026-09_to_2026-10-03/raw/` 均有全文）：前者给出单循环确定性 $\mathcal{O}(\epsilon^{-3})$ （OS）与 $\mathcal{O}(\epsilon^{-5/2})$ （GS），后者给出多层循环 $\mathcal{O}(\epsilon^{-5/2})$ ，在一般类 $\mathcal{C}$ 经 $\mathcal{D}_\rho$ 归约的上界对照中应与 PZL Tracked-FOAM 并列。
5. **`[补充遗漏]` Liao–Zheng (2025), `arXiv:2509.02804`**（*A proximal descent method for minimizing weakly convex optimization*）：Li–Pan v3 直接引用的确定性黑盒弱凸 $\mathcal{O}(\rho G^2 \Delta \epsilon^{-4})$ 上界（Theorem 2, Corollary 4.2），可与 Li–Pan 下界配对作为第 1 层确定性基准。
6. **`[补充遗漏]` Zhang–Luo (*SIOPT* 2020 & *SIOPT* 2022)** 与 **De Marchi–Jia–Kanzow–Mehlitz (*Math. Program.* 2023)**：前者为线性约束非凸复合优化全局对偶误差界与 $\mathcal{O}(\epsilon^{-2})$ 复杂度的直接源头，后者为非线性复合约束 ALM 的代表性期刊工作。

**独立查漏结论**：在「非线性 $\mathcal{A}$ 加一般 $L_h$-Lipschitz 凸 $h$ 加全局满行秩 $\mathcal{C}_\nu$ 加分离矩阵–向量积与精确 $\mathrm{prox}_h$ oracle」这一精确组合下，本次未检到已发表论文直接给出 $\widetilde{\mathcal{O}}(\mathrm{poly}(1/\nu)\,\epsilon^{-2})$ 上界或精确 $\epsilon$-KKT 不可达定理。但在立项写作时，必须将 $\mathcal{C}_\nu$ 线与 `2608.19847`（线性方程组步）和 `2607.08954`（局部正则加分段线性 $h$ ）严格区分。

---

## 四、与本稿（`overleaf/`）及 6 子问题定稿的对齐核查

### 4.1 `[有误或夸大]`（前提错配）：`Assumption~\ref{ass:smoothness}` 中的 $G_f$ 与目标全局 Lipschitz 性

- **本稿原文**（`overleaf/sections/Preliminaries.tex` L25–39）及用户 6 子问题定稿 §0.1 均明确假设 $\|\nabla f(\mathbf{x})\| \le G_f$ 、$\|J_{\mathcal{A}}(\mathbf{x})\| \le G_{\mathcal{A}}$ 且 $h$ 为 $L_h$-Lipschitz。因此在本稿问题类 $\mathcal{I}(\mathbf{C}, \Delta)$ 内，复合目标 $F = f + h \circ \mathcal{A}$ **自动全局 $(G_f + L_h G_{\mathcal{A}})$-Lipschitz**。
- **GPT Pro 偏差来源**：阶段 1 提示词仅写了 $f$ 为 $L_f$-smooth、未写入 $G_f$ ，导致 GPT Pro 在报告一 §6.1 与报告二 §1.3 均得出「$\nabla f$ 未必全局有界、$F$ 未必全局 Lipschitz」的结论。
- **对齐建议**：后续新线定稿须二选一写死——若沿用本稿 $\mathcal{I}(\mathbf{C}, \Delta)$ （含 $G_f$ ），则 $F$ 的全局 Lipschitz 常数为 $G_F := G_f + L_h G_{\mathcal{A}}$ （仍不同于弱凸模数 $R = L_f + L_h L_{\mathcal{A}}$ ）；若新线为贴合无约束光滑标准而去掉 $G_f$ ，则新线问题类 $\mathcal{C}$ 应与本稿 $\mathcal{I}(\mathbf{C}, \Delta)$ 显式区分。

### 4.2 `[有误或夸大]`（前提错配）：`Definition~\ref{def:oracle-model}` 的完整 Jacobian vs 矩阵–向量积 oracle

- **本稿原文**（`overleaf/sections/Preliminaries.tex` L86–102）及用户定稿 §0.2 定义：

$$
\mathcal{O}_{f,\mathcal{A}}(\mathbf{x}) := \bigl(f(\mathbf{x}),\nabla f(\mathbf{x}),\mathcal{A}(\mathbf{x}),J_{\mathcal{A}}(\mathbf{x})\bigr), \qquad \mathcal{O}_h(\mathbf{v},t) := \operatorname{prox}_{th}(\mathbf{v}).
$$

- **GPT Pro 设定**：采用 $(\nabla f(\mathbf{x}), \mathcal{A}(\mathbf{x}), J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{v}, \operatorname{prox}_{th}(\mathbf{z}))$ ，既无 $f(\mathbf{x})$ 、也无前向乘积 $J_{\mathcal{A}}(\mathbf{x})\mathbf{w}$ 或完整矩阵 $J_{\mathcal{A}}(\mathbf{x})$ 。
- **双向影响**：
  1. 在本稿中，`LRALMFamily.tex`（L11–35）与 `Acceleration.tex` 仅使用 $J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{q}$ 且只证算法族下界，故 `def:oracle-model` 不影响本稿现有定理；
  2. 但在大问题一/二的**算法无关下界**中，允许单次查询读取完整矩阵 $J_{\mathcal{A}}(\mathbf{x})$ 会直接瓦解高维 zero-chain 下界；反之，若将新线第 2 层 oracle 设为标准矩阵–向量积 $(f(\mathbf{x}), \nabla f(\mathbf{x}), \mathcal{A}(\mathbf{x}), J_{\mathcal{A}}(\mathbf{x})\mathbf{w}, J_{\mathcal{A}}(\mathbf{x})^\top \mathbf{v}, \operatorname{prox}_{th}(\mathbf{z}))$ ，则既可保住 zero-chain 屏障，又能使 GPT Pro 的 $\mathcal{C}_\nu$ 上界彻底摆脱「精确实数无限小差分模拟 $J_{\mathcal{A}}\mathbf{w}$ 」的脆弱假设。

### 4.3 `[已核实]` 其余记号对齐与定稿行号修正

- **`Assumption~\ref{ass:h}`（`Preliminaries.tex` L41–48）**：本稿已写明 $h:\mathbb{R}^m \to \mathbb{R}$ 全域有限、凸且 $L_h$-Lipschitz，与 GPT Pro 报告一 §1.2 与报告二 §1.1 的要求完全一致。
- **$\mathcal{D}_\rho$ 性质（`Preliminaries.tex` L110–154, `lem:reduced-al` 与 `eq:kkt-gs-identity`）**：本稿已建立 $\max_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda}) = F(\mathbf{x})$ 及 $\mathcal{R}_{\mathrm{KKT}}(\mathbf{x},\mathbf{y}(\mathbf{x},\boldsymbol{\lambda}),\mathbf{q}(\mathbf{x},\boldsymbol{\lambda})) = \max\{\|\nabla_{\mathbf{x}}\mathcal{D}_\rho\|, \|\nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho\|\}$ ，与 GPT Pro 报告一 §二.1 的归约基础一致。
- **用户定稿中的行号偏移**：当前 `overleaf/sections/Preliminaries.tex` 的实际行号为：`ass:smoothness`（L25–39）、`ass:h`（L41–48）、`def:eps-kkt`（L52–66）、`def:problem-class`（L73–84）、`def:oracle-model`（L86–102）、`lem:reduced-al`（L125–154）、`prop:curvature-smoothness`（L213–244）。用户定稿中引用的 `Preliminaries.tex#L7-L22`（原注释掉的 $\nu$ 正则假设）在当前版本中已删除，定稿归档时需同步更新行号引用。
- **项目笔记同步提醒**：`memory/notes/project/lower-bound-references.md` 中对 Pan–Zheng–Li（`2609.14235`）仅记录了 v1 的 OS 结果、对 Li–Pan（`2608.03246`）仅记录了 v1 标题，后续更新项目文献笔记时宜同步到 v2 / v3。
