# Antigravity Conversation Export

- **Conversation ID**: `08692ecf-d4f6-42c9-a763-45b4d937d720`
- **Project**: `/Users/liluxuan/Documents/My_Papers/3_DDLALM`
- **Started**: 2026-11-21 01:36
- **Exported**: 2026-11-21 01:52

---

## User (2026-11-21 01:36)

现在需要核对一下我们的全文的引用对不对 会不会有重复引用太多的：人情因素 我们得引 苏文藻老师的学生的很多工作 他的谱系 还有做minamx 做alm 做约束优化的人 还有就是一些引用 要查源头。 
 你懂我的意思吗》

---

## Assistant (2026-11-21 01:37)

### 精华总结

老大，我完全明白你的意思。**当前全稿共 48 条参考文献（见 [main.bbl](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/main.bbl)），存在近两年预印本高频重复引用、经典结论未溯源至原始文献，以及苏文藻（Anthony Man-Cho So）老师谱系与约束优化核心学者代表作覆盖不均衡的问题。**

### 结论

**建议按「降重去冗余 $\to$ 经典结论溯源 $\to$ 补齐苏老师谱系与领域核心学者代表作」三步核对并修订 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib) 及正文引用。** 请确认是否按以下四项诊断清单逐项推进，或直接指定需要优先补入的学者与文献名单。

### 依据与步骤

基于对当前手稿（[Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex)、[Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex)、[LRALMFamily.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex)、[Acceleration.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex) 及附录）的扫描，四个维度的现状如下：

1. **高频重复引用排查**
   - `li2026smoothing`（Li–Nagarajan–Pan–Zhang 2026）全稿出现 **29 次**（正文 10 次，附录 [UpperBounds.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/UpperBounds.tex) 19 次）；`zhang2020smoothed` 出现 **13 次**；`rockafellar1970convex` 出现 **7 次**；`pan2026optimal` 出现 **5 次**。
   - 正文多处将一般性背景结论挂在 `li2026smoothing` 与 `pan2026optimal` 名下，附录也在同一定理换算中逐段重复同一引用，需合并收敛至关键定理与定义处。

2. **引用查源头（把二级转引还原为原始出处）**
   - **Game stationarity 定义**：[Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L176-L178) 将 $\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})$ 的驻点定义归于 `\cite{li2026smoothing,pan2026optimal}`，应溯源至非凸极小极大驻点与近端梯度驻点的早期文献（如 `lin2020gradient`、`lu2020hybrid`、`zhang2020smoothed`）。
   - **Vanilla GDA 振荡与不收敛**：[Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L195-L196) 仅引用 `\cite{li2026smoothing}`，应溯源至 GDA 极限环与发散的原始分析文献。
   - **多循环 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$ 上界源头**：[Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L305) 将多循环达到 $\epsilon^{-5/2}$ 仅归于 `\cite{pan2026optimal}`，漏引了最早给出 NC-C 多循环 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$ 复杂度的 Lin–Jin–Jordan（COLT 2020, Minimax-PPA）。
   - **一阶零保持（zero-respecting）下界框架**：[LRALMFamily.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex#L188) 需核对 Nemirovski–Yudin 经典源头与 Carmon et al. (2020) 的分工。

3. **苏文藻（Anthony Man-Cho So）老师谱系与合作网络覆盖**
   - **当前已引**：李佳进（Jiajin Li）、朱玲玲芝（Linglingzhi Zhu）、郑天翼（Tianyi Zheng）的 `zheng2023universal`（NeurIPS 2023），李佳进参与的 `li2026smoothing`、`pan2026optimal`，以及苏老师与刘亚锋、姜波合作的 `xu2026rada`（MOR 2026）。
   - **明显缺漏**：本项目 8 篇核心范文之一的 **Li–Zhu–So (Math. Program. 2025)**（*Nonsmooth Nonconvex–Nonconcave Minimax Optimization: Primal–Dual Balancing and Iteration Complexity Analysis*）尚未进入 [main.bbl](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/main.bbl)；此外苏老师课题组及同门谱系（包括罗智泉老师谱系、周子睿、刘惠康、岳孟松等在误差界、非凸 ALM/ADMM 与极小极大上的代表作）可按相关性补入引言与预备知识。

4. **Minimax、ALM 与约束优化核心学者覆盖**
   - **Monteiro 组**：已引 `kong2019complexity`、`kong2021accelerated`、`kong2023iteration`，尚缺 [PROJECT_STATUS.md](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/PROJECT_STATUS.md#L69) 已标记的 **Kong–Monteiro (2024)**（固定零中心阻尼乘子单循环 $\mathcal{O}(\epsilon^{-3})$）。
   - **罗智泉 / 洪明毅 / 孙若愚 / 张嘉伟组**：已引 `zhang2020smoothed`、`zhang2022proximal`、`zhang2022global`、`hajinezhad2019perturbed`、`lu2020hybrid`，可补充 Hong–Luo–Razaviyayn (SIOPT 2016) 等非凸 ADMM/ALM 奠基文献。
   - **兰光辉 / 徐洋洋 / 林启航 / 徐姿组**：已引 `xu2023unified`、`li2021rate`、`lin2022complexity`、`pan2021efficient`、`he2024approximation`、`zhang2026matching`；一阶极小极大下界可补入 Ouyang–Xu (Math. Program. 2021)。
   - **国内约束优化与非凸优化团队（文再文、孙德锋、刘亚锋、姜波、陈小君、袁亚湘院士谱系等）**：目前文再文老师团队仅有 `liu2026fixed` 1 篇，可按约束优化与 ALM 脉络补充代表性工作。

请老大指示：我们先列出一份完整的「待删减重复引用 + 待溯源位置 + 待增补学者/文献清单」供你拍板，还是你有明确的必引学者名单先发给我对齐？

---

## User (2026-11-21 01:38)

你用这个模型再干一遍呢

---

## Assistant (2026-11-21 01:41)

### 精华总结

老大，逐行排查全稿与 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib) 后，我整理出四类具体问题：**5 处文献内容错配、2026 预印本高频刷屏（`li2026smoothing` 达 29 次）、7 处基础结论未溯源，以及苏文藻老师谱系和约束优化核心审稿人代表作（多篇已录入 bib 却漏引）覆盖不全。**

### 结论

**全稿引用需做一轮「纠错 + 降频 + 溯源 + 补谱系」的系统修订。** 下方已按具体文件行号列出问题清单与拟补学者谱系；请确认这份清单及有无需要额外点名加入的学者，确认后我再逐处落盘核验。

### 依据与步骤

#### 1. 现有引用错配与元数据缺陷（优先更正）

- **无扰动线性化 ALM 错引**：[Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L157-L158) 与 [LRALMFamily.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex#L152-L177)（共 3 处）将 $(\alpha,\beta)=(1,1)$ 的经典无扰动线性化 ALM 归于 `luSingleLoopGradientDescent2022`；该文实为带对偶扰动的 GDPA（对应 $\beta=0$ 分支），线性化乘子步应溯源至 Rockafellar (1976)、Yang & Yuan (SIOPT 2013)、Hong–Luo–Razaviyayn (SIOPT 2016) 等文献。
- **Table 1 合并错位（两处）**：[Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L247) 将无需正则性条件的 `kong2023iteration`（IAIPAL）并入需正则性条件的 `iALM` 行并标为非 CQ-free；[Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L253)（及第 74 行）将线性约束多循环方法 `sun2024dual_descent_alm_admm`（Sun & Sun, SIOPT 2024）混入非线性约束单循环方法 GDPA 行。
- **内层对偶加速引用偏差**：[Acceleration.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex#L100) 与第 401 行讨论求解对偶子问题 $\max_{\boldsymbol{\lambda}} d_s(\boldsymbol{\lambda};\mathbf{z}^k)$ 的双循环加速方案时引用 `kong2021accelerated`（外层原始近端点加速），准确对应应补入 Lin–Jin–Jordan (COLT 2020) 与 Ostrovskii–Lowy–Razaviyayn (SIOPT 2021)。
- **Bib 文件缺陷**：[refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib#L1459-L1487) 第 1467 行有多余右花括号 `}`；`xu2023unified` 第三作者 `Yan Xu` 误作 `Yang Xu`；`zhang2020proximal` / `zhang2022proximal` 与 `zhang2020single` / `zhang2020smoothed` 重复；`elbourkhissi2025linearized` 编号 `2301.08345` 与年份 `2025` 不一致。

#### 2. 高频重复引用降重

- **预印本密度过高**：未发表预印本 `li2026smoothing` 全稿出现 **29 次**（正文 10 次，附录 [UpperBounds.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/UpperBounds.tex#L8-L278) 19 次），`pan2026optimal` 出现 **6 次**，另有 `zhang2020smoothed` **13 次**。
- **精简位置**：[Acceleration.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Acceleration.tex#L342-L359) 间隔 17 行重复整串 `\cite{zhang2022proximal,zhang2020smoothed,li2026smoothing}`；附录 [UpperBounds.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/appendix/UpperBounds.tex#L8-L10) 首段已声明定理编号沿用 `li2026smoothing`，后文 18 次重复 `\cite` 可直接写定理与条件号；预备知识中的通用概念移交原始文献。

#### 3. 基础概念查源头清单

| 位置 | 当前所引（二级转引） | 应还原的源头文献 |
|---|---|---|
| [Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L44) 有限极大模型 | `zhang2020smoothed` | `nesterov2005smooth`（已在 bib 第 1531 行，未引）及 Nouiehed et al. (2019) |
| [Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L61) Prox-linear 法 | `Drusvyatskiy2019` | Burke (MP 1985)、Lewis & Wright (MP 2016) 并列 `Drusvyatskiy2019` |
| [Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L305) NC-C 多循环 $\tilde{\mathcal{O}}(\epsilon^{-5/2})$ | `pan2026optimal` | Lin–Jin–Jordan (COLT 2020, Minimax-PPA)、Ostrovskii et al. (SIOPT 2021) |
| [Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L8-L20) 近端算子与 Moreau 包络 | `rockafellar1970convex` | `moreau1965`（已在 bib 第 1521 行，未引）并列 `rockafellar1970convex` |
| [Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L176-L178) $\epsilon$-GS 驻点定义 | `li2026smoothing,pan2026optimal` | `lin2020gradient`、Nouiehed et al. (2019)、`li2025nonsmooth`（GS/OS 关系） |
| [Preliminaries.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Preliminaries.tex#L195-L198) GDA 不收敛与对偶正则 | `li2026smoothing` 等 | GDA 发散引 Korpelevich (1976) / Daskalakis et al. (2018)；对偶光滑化引 Tikhonov (1963) / `nesterov2005smooth` |
| [LRALMFamily.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/LRALMFamily.tex#L188) 函数类与 $\inf$–$\sup$ 下界框架 | `nesterov2018lectures,carmon2020lower,li2021complexity` | Nemirovski & Yudin (1983)、`carmon2020lower`、Tian & So (MP 2024) |

#### 4. 学术谱系与领域核心学者增补建议

1. **苏文藻（Anthony Man-Cho So）老师课题组及学生谱系**
   - **已录入 bib 却漏引**：`li2025nonsmooth`（**Li, Zhu, So, Math. Program. 2025**，见 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib#L1554)，李佳进、朱玲玲芝、苏老师旗舰长文）正文中目前为 **0 次引用**，应在引言与预备知识重点补入。
   - **核心增补**：**Tian & So (MP 2024)**（田宇、苏老师，本文 `def:problem-class` 维数取并集写法的直接来源）、**Zhu & Li (2026, arXiv:2607.08954)**（朱玲玲芝、李佳进，固定罚局部正则复合约束一阶 ALM）、**Zhou & So (MP 2017)**（周子睿、苏老师，误差界分析），以及苏老师与刘惠康、岳孟松等在相位恢复（[Introduction.tex](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/sections/Introduction.tex#L20)）或极小极大（DS-OGDA）上的工作。
2. **罗智泉同门谱系（洪明毅、孙若愚、马士谦、刘亚锋、姜波、庞鼎基）**
   - 已覆盖张嘉伟、罗智泉、孙若愚、洪明毅、刘亚锋、姜波；建议补入 **Hong, Luo, Razaviyayn (SIOPT 2016)**（非凸线性化乘子法奠基作）及 **马士谦（Shiqian Ma）**、**庞鼎基（Ting Kei Pong）** 在非凸 ADMM/ALM 与复合优化上的代表作。
3. **ALM 与约束优化核心审稿人**
   - **国内团队**：补 **Deng, Wang, Zhu, Zhang, Wen (SIAM Review 2026)**（文再文、邓康康、张俊宇 ALM 综述）、已在 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib#L1339) 却未引的 **Grapiglia & Yuan (IMA JNA 2021)**（袁亚湘院士非凸 ALM 复杂度），以及 **He & Yuan（何炳生、袁亚湘）** 在乘子法线性化与加速上的先驱工作。
   - **国际高频审稿人**：**吕召松（Zhaosong Lu）** 当前为 0 引用（SIOPT/MP 约束优化核心审稿人，需补 Lu & Mei, MP 2023 等非凸 ALM/罚方法复杂度工作）；Monteiro 组补 **Kong & Monteiro (SIOPT 2024)**（零中心阻尼单循环 $\mathcal{O}(\epsilon^{-3})$）；兰光辉组补 **Boob, Deng, Lan (MP 2025)**；徐洋洋/林启航组补已在 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib#L1640) 却未引的 **Liu, Lin, Xu (MOR 2026)**；Boţ 组补已在 [refer.bib](file:///Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf/tools/refer.bib#L1500) 的 **Boţ & Nguyen (MOR 2020)** / **Boţ & Böhm (2020)**。
4. **Minimax 上下界核心组**
   - 补 **Lin, Jin, Jordan (COLT 2020)**、**Ouyang & Xu (MP 2021)**（鞍点下界源头）与 **Wu, Gu, Yang (2026)**（顾全全、杨天宝组 NC-C 下界，与 `pan2026optimal` 并列）。

请老大确认：哪些谱系与条目直接采纳，或者是否还有特定老师/师兄弟的名字需要补进这张清单？确认后我再按章节给出精确替换方案并校验每条元数据。

---
