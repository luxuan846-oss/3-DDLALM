# 03-potential-and-proof-sketch

- **Source session**: `e138119c`
- **Span (local time)**: 2026-11-11 12:12 to 2026-11-11 19:50
- **User turns**: 57

---

## User (2026-11-11 12:12)

老大，进展已经写进 PROJECT_STATUS.md §4 第 4、5 条，新对话里从这个文件接着做就行。

第 4 条（$\epsilon^{-5/2}$ 结果）：记了算法和证明材料在哪，以及查新结论。你已经定了"主定理 + 附录完整证明"，这条也记上了。还没定的有：新建文件的五点方案、族内 $\Omega(\epsilon^{-3})$ 写不写、标题候选、改写 (Q)，以及写进论文之前你要复核 G2 的哪两处。
第 5 条（全文改名）：SPLALM 改成 LRALM、combined penalty 改成 effective penalty，已经改完，在临时目录编译通过。main.pdf 没有重新生成，标签没动。还没定的是 potential function 那个叫法，以及 LRALM 还没查重名。

新对话可以直接从"讨论新建文件的五点方案"开始，方案就写在第 4 条"待讨论"里。  你看下哈

---

## Assistant (2026-11-11 12:13)

老大，下面是算法定义的 LaTeX 草稿。写法照搬 `def:splalm`：$\mu$ 固定为 $\mathbf{0}$；外推系数写成 $(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})$，不加新符号；输出和 oracle 计数与 LRALM 相同。我还没有写进任何文件。

```latex
\begin{definition}[LRALM with dual extrapolation]
\label{def:lralm-extrapolation}
Let \(\theta=(\rho,s,\gamma,\eta,\tau)\) be as in Definition~\ref{def:splalm}
and let \(\alpha\in[0,1]\). LRALM with dual extrapolation starts from
\((\bx^0,\blmbd^0,\bz^0)=\zero\), sets \(\blmbd^{-1}:=\blmbd^0\), and,
for \(k\ge0\), computes
\begin{equation}
\begin{aligned}
    \bar\blmbd^k&=\blmbd^k+\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}
        \bigl(\blmbd^k-\blmbd^{k-1}\bigr),\\
    \bx^{k+1}&=\bx^k-\eta\,\nabla_{\bx}\mathcal P_s(\bx^k,\bar\blmbd^k;\bz^k,\zero),\\
    \blmbd^{k+1}&=\bar\blmbd^k+\tau\,\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar\blmbd^k;\bz^k,\zero),\\
    \bz^{k+1}&=\bz^k+\alpha(\bx^{k+1}-\bz^k).
\end{aligned}
    \label{eq:lralm-extrapolation-updates}
\end{equation}
At iteration \(k\), it outputs
\((\bx^{k+1},\by^{k+1},\bq^k)
:=(\bx^{k+1},\by(\bx^{k+1},\bar\blmbd^k),\bq(\bx^{k+1},\bar\blmbd^k))\).
\end{definition}

Compared with \(\mathrm{LRALM}_{\theta,\alpha,0}\), the only change is that
both gradient steps are evaluated at the extrapolated multiplier
\(\bar\blmbd^k\) instead of \(\blmbd^k\); replacing the extrapolation
coefficient by zero recovers~\eqref{eq:splalm-updates} with \(\beta=0\).
Since \(\bar\blmbd^k\) depends on \(\blmbd^{k-1}\), the method does not belong
to \(\calC_\theta\). Each iteration evaluates \(\by(\cdot,\cdot)\) at
\((\bx^k,\bar\blmbd^k)\) and \((\bx^{k+1},\bar\blmbd^k)\) and reuses the
first-order information at \(\bx^{k+1}\), so \(K\) iterations and their outputs
again use \(3K+1\) oracle calls.
```

**Three choices to confirm**

1. **The extrapolation coefficient is fixed in the definition.** It equals $(1-\varsigma)/(1+\varsigma)$ with $\varsigma=\sqrt{\tau/s}$. Writing it with $\sqrt{s}$ and $\sqrt{\tau}$ avoids $\theta_{\mathrm{m}}$, which clashes with the parameter tuple $\theta$, and avoids $\varsigma$. Since $\tau\le s$, the coefficient lies in $[0,1)$. The theorem then only needs $\alpha=c\sqrt{\tau/s}$, $\eta=\gamma$ and $s=c_s/\epsilon$. The constant $c$ needs a new name, because $c_\alpha$ is already used in appendix C.
2. **The primal step uses $\eta$.** The B2′ notes use $\gamma$ for the primal step; the paper's convention is $\eta$. The notes' condition (H) assumes $\eta=\gamma$, so the theorem must state $\eta=\gamma$ as a condition. The appendix rewrite has to replace $\gamma$ with $\eta$ throughout.
3. **No abbreviation.** The method has no short name like "LRALM-DE"; the theorem and Remarks refer to it as "LRALM with dual extrapolation" or by the definition's label. That follows our no-abbreviations rule for drafts. The cost is that comparison tables and the Remarks will read wordy.

**Section placement**

I recommend changing this item of the five-point plan. `LowerBound.tex` is the "Main Results" section, and `LowerBoundProof.tex` is a pure proof section. Putting a section with a main theorem after a proof section would mix results and proofs. A better order:

- The new section goes right after `LowerBound.tex`, as §5, holding this definition plus the main theorem.
- The hard-instance proofs move back one section, to §6.
- `appendix/AccelerationProof.tex` goes right after `UpperBoundBetaZero.tex`, because the proof reuses appendix C Step 1–2, the reduction to $\mathcal{D}_\rho$.

Once you settle these three choices and the placement, I'll write the theorem statement in the same style.

---

## User (2026-11-11 12:15)

就是2.5的； 然后是算法证明用的 我们说中文谢谢  先告诉我 我们证明的算法？

---

## Assistant (2026-11-11 12:16)

老大，我们证明的算法叫 **B2′**，就是 **LRALM（$\beta=0$）在对偶变量上加一步 Nesterov 外推**。原始步是普通梯度步，没有 OGDA 修正，也没有投影。$O(\epsilon^{-5/2})$ 证明的就是这个算法，上一轮给你的定义草稿也和它一致。

## 更新格式

初值取 $(\mathbf{x}^0,\boldsymbol{\lambda}^0,\mathbf{z}^0)=\mathbf{0}$，令 $\boldsymbol{\lambda}^{-1}=\boldsymbol{\lambda}^0$。对偶中心固定为 $\boldsymbol{\mu}=\mathbf{0}$。对 $k\ge0$，第一步是对偶外推：

$$
\bar{\boldsymbol{\lambda}}^k=\boldsymbol{\lambda}^k+\theta_{\mathrm{m}}\left(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}\right)
$$

第二步是原始梯度步，在外推点 $\bar{\boldsymbol{\lambda}}^k$ 处取梯度：

$$
\mathbf{x}^{k+1}=\mathbf{x}^k-\gamma\nabla_{\mathbf{x}}\mathcal{P}_s\left(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\mathbf{0}\right)
$$

第三步是对偶梯度步，从外推点出发：

$$
\boldsymbol{\lambda}^{k+1}=\bar{\boldsymbol{\lambda}}^k+\tau\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s\left(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k,\mathbf{0}\right)
$$

第四步更新原始中心：

$$
\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha\left(\mathbf{x}^{k+1}-\mathbf{z}^k\right)
$$

输出在外推点处取值：

$$
\left(\mathbf{x}^{k+1},\ \mathbf{y}(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k),\ \mathbf{q}(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k)\right)
$$

$K$ 步共调用 oracle $3K+1$ 次，与 LRALM 相同。

## 参数条件 (H)

- $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$，原始步长 $\eta=\gamma$。
- $\tau\le\min\{\rho/4,\ 1/(14\gamma G_{\mathcal{A}}^2)\}$。
- $s=c_s/\epsilon$，系数满足 $c_s\ge 2\bar{C}_\lambda L_h$，并且 $s\ge\max\{\rho,4\tau\}$。$s$ 在整次运行中固定。
- 记 $\varsigma=\sqrt{\tau/s}\le 1/2$。外推系数取下式；中心步长取 $\alpha=c_\alpha\varsigma$，其中 $0\lt c_\alpha\le 1/6$。

$$
\theta_{\mathrm{m}}=\frac{1-\varsigma}{1+\varsigma}=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}
$$

## 结论

当迭代次数满足下式时，前 $K$ 个输出中至少有一个满足 $\mathcal{R}_{\mathrm{KKT}}\le\epsilon$：

$$
K\ge 4C_R^2\Delta_{\mathcal{W}}\sqrt{c_s/\tau}\ \epsilon^{-5/2}
$$

其中 $\Delta_{\mathcal{W}}=\Delta+L_h^2/\rho+(G_f+G_{\mathcal{A}}L_h)^2/(2\mu_\gamma)$，与 $s$ 无关。

## 与 LRALM 的区别和证明边界

- **相对 $\mathrm{LRALM}_{\theta,\alpha,0}$ 只改了一处**：原始步和对偶步都在 $\bar{\boldsymbol{\lambda}}^k$ 处取梯度，对偶步也从 $\bar{\boldsymbol{\lambda}}^k$ 出发。把 $\theta_{\mathrm{m}}$ 换成 $0$，就退回 LRALM。
- **中心步长从 $\epsilon$ 量级提高到 $\varsigma$ 量级。** 族内上界取 $\alpha\sim\epsilon$。B2′ 取 $\alpha\sim\sqrt{\tau/s}\sim\sqrt{\epsilon}$，依据是固定中心时每步收缩 $1-\varsigma$（G2.4）。这就是 $\epsilon^{-3}$ 降到 $\epsilon^{-5/2}$ 的原因。
- **G0 里的 B2（原始步带 OGDA 修正 $2\mathbf{g}^k-\mathbf{g}^{k-1}$）没有证明。** 论文只写 B2′。
- **写入论文前要换记号**：
  - $\theta_{\mathrm{m}}$ 与参数组 $\theta$ 重名，可以直接写成 $\sqrt{s}$、$\sqrt{\tau}$ 的形式；
  - $c_\alpha$ 与附录 C 重名；
  - 证明用 $\gamma$ 作原始步长，论文用 $\eta$，定理里需要写明 $\eta=\gamma$。

下一步写主定理的陈述吗？

---

## User (2026-11-11 12:18)

我们用的势函数是啥 不要啰嗦

---

## Assistant (2026-11-11 12:19)

老大，总势函数是外层值函数加内层能量的一半：

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k
$$

其中 $p_s(\mathbf{z})=\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\mathbf{0})$。内层能量 $\mathcal{E}_k$ 在中心 $\mathbf{z}^k$ 处度量，共四项：

$$
\mathcal{E}_k=p_s(\mathbf{z}^k)-d_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}^\star(\mathbf{z}^k)\rVert^2+c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z}^k)\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

- **第一项是对偶间隙**：$d_s(\boldsymbol{\lambda};\mathbf{z})=\min_{\mathbf{x}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\mathbf{0})$。
- **第二项是 Nesterov 动量项**：$\mathbf{w}^k=\boldsymbol{\lambda}^{k-1}+\varsigma^{-1}(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$，$\boldsymbol{\lambda}^\star(\mathbf{z})$ 是鞍点的对偶分量。
- **第三项是原始跟踪误差**：$\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})=\arg\min_{\mathbf{x}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\mathbf{0})$，系数 $c_e=12(\gamma L_{\mathcal{D},\mathbf{x}})^2(L_x+\mu_\gamma/2)$。
- **第四项是对偶步长平方**：系数 $c_r=G_{\mathcal{A}}^2/(4\mu_\gamma)$。

两个下降不等式：

- **固定中心（G2.4）**：$\mathcal{E}_{k+1}\le(1-\varsigma)\mathcal{E}_k$，其中 $\varsigma=\sqrt{\tau/s}$。
- **移动中心（G3.4）**：$\mathcal{W}_k$ 单步下降，求和后得到下式，其中 $\Delta_{\mathcal{W}}$ 与 $s$ 无关。

$$
\sum_{k\lt K}\varsigma\left[\frac{c_\alpha}{5\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2+\frac{1}{4}\mathcal{E}_k\right]\le\Delta_{\mathcal{W}}
$$

---

## User (2026-11-11 12:38)

本质上我们证明了mu动不动其实没关心 mu=0是最简答操作 不要啰嗦

---

## Assistant (2026-11-11 12:39)

老大，证明支持的是"**$s=c_s/\epsilon$ 时取 $\boldsymbol{\mu}\equiv\mathbf{0}$ 就够**"；"$\boldsymbol{\mu}$ 动不动都一样"还没有证明。

- **已证**：B2′ 在 $\boldsymbol{\mu}\equiv\mathbf{0}$ 下达到 $O(\epsilon^{-5/2})$。固定 $\boldsymbol{\mu}=\mathbf{0}$ 的代价只有输出残差里的偏差 $\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s$；$s=c_s/\epsilon$ 时它是 $O(\epsilon)$，所以移动 $\boldsymbol{\mu}$ 在阶上没有收益。
- **族内同样成立**：按你证的族内 $\Omega(\epsilon^{-3})$，$s=c_s/\epsilon$ 时所有 $(\alpha,\beta)$ 都不优于 $\beta=0$。
- **未证**：B2′ 加上 $\beta\gt0$ 是否仍有 $\epsilon^{-5/2}$。G1 的乘子界、$\lVert\boldsymbol{\lambda}^\star(\mathbf{z})\rVert\le sL_h/(\rho+s)$ 和 $\Delta_{\mathcal{W}}$ 的界都用了 $\boldsymbol{\mu}=\mathbf{0}$。
- **适用范围**：$s$ 取常数时偏差是 $\Theta(1)$，这时必须移动 $\boldsymbol{\mu}$，$\beta=1$ 的 $O(\epsilon^{-4})$ 属于这种情形。

论文里可以写 "with $s=c_s/\epsilon$, the dual center can be fixed at zero"，不能写 "the dual center is irrelevant"。

---

## User (2026-11-11 12:39)

为啥你的输出有时候不能完全把公式编译好

---

## Assistant (2026-11-11 12:40)

老大，我没法看到你那边的渲染结果，下面是对照我上一条回复的诊断，其中哪一条是真因属于推断。

**我上一条回复里的风险点**

- 行内公式里有 `\lVert\bar{\boldsymbol{\lambda}}^k\rVert/s` 这种长式子，含上标、多层花括号和斜杠，已超出规则里"行内只放短符号"的上限。
- 行内公式里有 `\boldsymbol{\mu}\equiv\mathbf{0}` 和 `\Omega(\epsilon^{-3})` 这类带多个命令的式子，长度也接近上限。
- 列表项里同时出现多个行内公式，且夹着加粗 `**...**`。Markdown 先处理 `*`、`_`、`^`，下划线和星号可能在公式闭合前被当成强调符号吞掉。这是 VSCode 插件显示不稳定最常见的原因。
- `\boldsymbol` 嵌套 `\mathbf`、`\bar{\boldsymbol{...}}` 的深层嵌套，在 KaTeX 里可以解析，但在 Markdown 预处理阶段更容易被切断。

**根本原因**

VSCode 插件先用 Markdown 解析正文，再把 `$...$` 交给 KaTeX。行内公式越长、含 `_` 和 `*` 越多，被 Markdown 提前破坏的概率越高。你的规则文件已写明"VSCode 插件渲染部分不稳定"。

**我之后的做法**

1. 行内只放单个符号，例如 $s$、$\boldsymbol{\mu}$、$\epsilon$。
2. 凡是含 `\lVert`、`\bar`、上下标组合或超过 25 个字符的式子，一律改成独立的 `$$` 块。
3. 加粗文字里不放公式；公式与相邻中文之间留空格。
4. 少用 `\boldsymbol` 套 `\bar`，必要时只写 $\bar{\lambda}$ 一类短形式并在首次出现时说明它是向量。

你可以把渲染出错的那一句贴给我，我能定位具体是哪个字符被吞掉。

---

## User (2026-11-11 12:43)

不要啰嗦 给出势函数 我们的proof sketch是什么？

---

## Assistant (2026-11-11 12:43)

老大，势函数是外层值函数加内层能量的一半，证明分四步。

## 势函数

$$
\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k
$$

内层能量在中心 $\mathbf{z}^k$ 处度量，依次是对偶间隙、Nesterov 动量项、原始跟踪误差、对偶步长平方：

$$
\mathcal{E}_k=p_s-d_s(\boldsymbol{\lambda}^k)+\frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}^\star\rVert^2+c_e\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1})\rVert^2+c_r\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

其中 $\varsigma=\sqrt{\tau/s}$，动量点为

$$
\mathbf{w}^k=\boldsymbol{\lambda}^{k-1}+\varsigma^{-1}\left(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}\right)
$$

## Proof sketch

**第一步（G1）：乘子无投影有界。** 对任意乘子都有 $\lVert\mathbf{q}\rVert\le L_h$。对偶递推是由 $\mathbf{q}$ 驱动的二阶线性滤波，脉冲响应的 $\ell_1$ 范数有界，于是

$$
\lVert\boldsymbol{\lambda}^k\rVert\le C_\lambda L_h,\qquad \lVert\bar{\boldsymbol{\lambda}}^k\rVert\le\bar{C}_\lambda L_h
$$

两个常数都与 $s$ 无关。

**第二步（G2.4）：固定中心时能量线性收缩。**

$$
\mathcal{E}_{k+1}\le(1-\varsigma)\mathcal{E}_k-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\varsigma\Gamma_k^\star
$$

关键做法：Nesterov 估计建在部分函数 $\mathcal{P}_s(\mathbf{x}^{k+1},\cdot)$ 上。对偶方向正好是它在外推点的梯度，所以对偶梯度没有误差。原始跟踪误差由动量位移项支付。

**第三步（G3.4）：移动中心时总势函数单步下降。** 中心移动带来两项代价：

- (F1) 能量对中心的灵敏度产生交叉项，量级是 $\sqrt{\mathcal{E}_k}$ 乘以中心位移，由每步 $\varsigma$ 份额的收缩吸收。
- (F2) $p_s$ 的下降漏出 $\mathbf{x}^{k+1}$ 到鞍点原始分量的距离平方，由第二步的 $\varsigma\Gamma_k^\star$ 支付。

两处都只要求 $\alpha$ 与 $\varsigma$ 同阶，取 $\alpha=c_\alpha\varsigma$ 且 $c_\alpha\le 1/6$ 即可。灵敏度常数与 $s$ 无关，因为对偶距离项中 $s$ 的幂次相消。

**第四步（G3.6）：求和并换算残差。** 第三步求和给出

$$
\sum_{k\lt K}\varsigma\left[\frac{c_\alpha}{5\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2+\frac{1}{4}\mathcal{E}_k\right]\le\Delta_{\mathcal{W}}
$$

其中 $\Delta_{\mathcal{W}}$ 与 $s$ 无关。于是存在某个 $k$ 使方括号内的量不超过 $\Delta_{\mathcal{W}}/(\varsigma K)$，记该量为 $M_k$。输出残差满足

$$
\mathcal{R}_{\mathrm{KKT}}\le C_R\sqrt{M_k}+\frac{\bar{C}_\lambda L_h}{s}
$$

取 $s=c_s/\epsilon$，第二项不超过 $\epsilon/2$。第一项不超过 $\epsilon/2$ 需要 $\varsigma K\ge 4C_R^2\Delta_{\mathcal{W}}\epsilon^{-2}$，代入 $\varsigma=\sqrt{\tau\epsilon/c_s}$ 得

$$
K\ge 4C_R^2\Delta_{\mathcal{W}}\sqrt{c_s/\tau}\,\epsilon^{-5/2}
$$

---

## User (2026-11-11 12:45)

$$\mathcal{E}_{k+1}\le(1-\varsigma)\mathcal{E}_k-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\varsigma\Gamma_k^\star$$ 这个\varsigma\Gamma_k^\star$ 是什么 不要啰嗦 不要用工科的语言 要用数学优化的语言

---

## Assistant (2026-11-11 12:45)

老大，$\Gamma_k^\star$ 是 $\mathbf{x}^{k+1}$ 在鞍点乘子处的**原始最优性间隙**（primal suboptimality gap）：

$$
\Gamma_k^\star=\mathcal{P}_s\left(\mathbf{x}^{k+1},\boldsymbol{\lambda}^\star(\mathbf{z});\mathbf{z},\mathbf{0}\right)-p_s(\mathbf{z})
$$

**非负性与强凸下界。** 函数 $\mathcal{P}_s(\cdot,\boldsymbol{\lambda}^\star(\mathbf{z});\mathbf{z},\mathbf{0})$ 是 $\mu_\gamma$-强凸的，极小点是鞍点的原始分量 $\mathbf{x}^\star(\mathbf{z})$，极小值是 $p_s(\mathbf{z})$。因此

$$
\Gamma_k^\star\ge\frac{\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}^\star(\mathbf{z})\rVert^2
$$

**来源。** Nesterov 估计序列用的是 $\mathcal{P}_s(\mathbf{x}^{k+1},\cdot)$ 关于乘子的凹性，比较点取 $\boldsymbol{\lambda}^\star(\mathbf{z})$，权重为 $\varsigma$。该函数在 $\boldsymbol{\lambda}^\star(\mathbf{z})$ 处的值比 $p_s(\mathbf{z})$ 多出 $\Gamma_k^\star$，所以不等式右端出现 $-\varsigma\Gamma_k^\star$。

**用途。** 中心更新后，$p_s$ 的下降不等式右端有正项

$$
\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^\star(\mathbf{z}^k)\rVert^2
$$

它由 $-\varsigma\Gamma_k^\star$ 抵消，这要求 $\alpha$ 与 $\varsigma$ 同阶。

---

## User (2026-11-11 12:46)

第三步（G3.4）：移动中心时总势函数单步下降。 中心移动带来两项代价：

(F1) 能量对中心的灵敏度产生交叉项，量级是 $\sqrt{\mathcal{E}_k}$ 乘以中心位移，由每步 $\varsigma$ 份额的收缩吸收。
(F2) $p_s$ 的下降漏出 $\mathbf{x}^{k+1}$ 到鞍点原始分量的距离平方，由第二步的 $\varsigma\Gamma_k^\star$ 支付。

两处都只要求 $\alpha$ 与 $\varsigma$ 同阶，取 $\alpha=c_\alpha\varsigma$ 且 $c_\alpha\le 1/6$ 即可。灵敏度常数与 $s$ 无关，因为对偶距离项中 $s$ 的幂次相消 这个 核心的lemma 内容是什么？ 
你输出 就是条件和 结果式子

---

## Assistant (2026-11-11 12:47)

老大，第三步由三个引理组成，核心是 Lemma G3.2。

## 记号

四个量都在第 $k$ 步定义：

$$
\chi_k=\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert,\qquad \chi_k^\star=\lVert\mathbf{x}^{k+1}-\mathbf{x}^\star(\mathbf{z}^k)\rVert
$$

$$
r_k=\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert,\qquad \varpi_k=\lVert\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^k;\mathbf{z}^k)-\mathbf{x}_s(\boldsymbol{\lambda}^k;\mathbf{z}^k)\rVert
$$

另记 $\mu_\gamma=1/\gamma-L_{\mathcal{D},\mathbf{x}}$。

## Lemma G3.2（能量关于中心的扰动界）

**条件**：$\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$，$s\gt 0$。迭代点固定，中心 $\mathbf{z}$、$\mathbf{z}'$ 任意。

**结果**：

$$
\mathcal{E}_k(\mathbf{z}')-\mathcal{E}_k(\mathbf{z})\le C_{\mathbf{z},1}\sqrt{\mathcal{E}_k(\mathbf{z})}\,\lVert\mathbf{z}'-\mathbf{z}\rVert+C_{\mathbf{z},2}\lVert\mathbf{z}'-\mathbf{z}\rVert^2
$$

$$
C_{\mathbf{z},1}=\frac{1}{\gamma}\sqrt{\frac{10}{3\mu_\gamma}},\qquad C_{\mathbf{z},2}=\frac{4}{3\gamma^2\mu_\gamma}
$$

两个常数与 $s$、$\tau$、$\rho$ 无关。

## Lemma G3.3（中心步上 $p_s$ 的下降）

**条件**：$\alpha\in[0,1]$。

**结果**：

$$
p_s(\mathbf{z}^{k+1})-p_s(\mathbf{z}^k)\le-\frac{\alpha(1-\alpha)}{2\gamma}\chi_k^2+\frac{\alpha}{2\gamma}(\chi_k^\star)^2
$$

## Theorem G3.4（总势函数单步下降）

**条件 (H)**：

- $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$，$\eta=\gamma$。
- $\tau\le\min\{\rho/4,\ 1/(14\gamma G_{\mathcal{A}}^2)\}$。
- $s\ge\max\{\rho,4\tau\}$。
- 外推系数为 $(1-\varsigma)/(1+\varsigma)$，其中 $\varsigma=\sqrt{\tau/s}$。
- $\alpha=c_\alpha\varsigma$，$0\lt c_\alpha\le 1/6$。

**结果**：

$$
\mathcal{W}_{k+1}\le\mathcal{W}_k-\frac{\alpha}{5\gamma}\chi_k^2-\frac{\varsigma}{4}\mathcal{E}_k-\frac{1}{16\tau}r_k^2-\frac{\varsigma\mu_\gamma}{8}(\chi_k^\star)^2-\frac{5\mu_\gamma}{192}\varpi_k^2
$$

推论形式：

$$
\mathcal{W}_{k+1}\le\mathcal{W}_k-\frac{\alpha\gamma}{10}\lVert\nabla p_s(\mathbf{z}^k)\rVert^2-\frac{\varsigma}{4}\mathcal{E}_k
$$

## 三者的组合

G2.4 给出固定中心的收缩，G3.2 取 $\mathbf{z}=\mathbf{z}^k$、$\mathbf{z}'=\mathbf{z}^{k+1}$，对线性项用 Young 不等式（权重 $\varsigma/2$），得到

$$
\mathcal{E}_{k+1}-\mathcal{E}_k\le-\frac{\varsigma}{2}\mathcal{E}_k-\varsigma\Gamma_k^\star+\left(\frac{C_{\mathbf{z},1}^2}{2\varsigma}+C_{\mathbf{z},2}\right)\alpha^2\chi_k^2-\frac{1}{8\tau}r_k^2-\frac{5\mu_\gamma}{96}\varpi_k^2
$$

把它的一半加到 G3.3 上，剩下两个系数条件：

- **(F1)** $\chi_k^2$ 的系数为负，需要 $\alpha^2 C_{\mathbf{z},1}^2/\varsigma$ 小于 $\alpha/\gamma$ 的常数倍。
- **(F2)** $(\chi_k^\star)^2$ 的系数为负，需要 $\alpha/(2\gamma)$ 小于 $\varsigma\mu_\gamma/4$。

两条都由 $c_\alpha\le 1/6$ 保证。

---

## User (2026-11-11 12:48)

你读的是哪个文件 输出的证明

---

## Assistant (2026-11-11 12:48)

老大，上一条的引理和定理全部读自 [b2-G3-20261109.md](overleaf/notes/gpt-proofs/b2-G3-20261109.md)，它是 B2′ 证明的第三部分（移动中心与总势函数下降）。

本次对话读过的证明文件共四个，都在 [overleaf/notes/gpt-proofs/](overleaf/notes/gpt-proofs/) 下：

- [b2-summary-20261109.md](overleaf/notes/gpt-proofs/b2-summary-20261109.md)：算法、参数条件 (H)、复杂度结论、查新。
- [b2-G0G1-20261109.md](overleaf/notes/gpt-proofs/b2-G0G1-20261109.md)：算法定义、oracle 计数、乘子有界性。
- [b2-G2-20261109.md](overleaf/notes/gpt-proofs/b2-G2-20261109.md)：固定中心的收缩，即 Theorem G2.4 和能量的定义。
- [b2-G3-20261109.md](overleaf/notes/gpt-proofs/b2-G3-20261109.md)：Lemma G3.2、G3.3、Theorem G3.4、Corollary G3.6。

其中 G2 和 G3 我只读了定理陈述和部分证明段落，没有逐行读完全文。

---

## User (2026-11-11 12:53)

B2′：对偶 Nesterov 外推的 LRALM
B2′ 在 LRALM（
β
=
0
β=0）的对偶变量上加入 Nesterov 外推。原始步采用普通梯度步，没有 OGDA 修正，也没有投影。
O
(
ϵ
−
5
/
2
)
O(ϵ 
−5/2
 ) 的证明对应此算法。 确定没人做过吗？
我们相当于额外加一个对偶正则。 我害怕这个迭代一化简就变成其他的了

---

## Assistant (2026-11-11 12:55)

老大，不能说"确定没人做过"。目前的依据只有 11-09 的一次检索：没找到相同的算法。我刚把迭代化简了一遍，它不会变成 Zhang–Xu 的算法，但会变成"Perturbed Smoothed GDA 加对偶 Nesterov 外推"，那次检索是否用这个说法查过，记录里没有写明。

## 化简结果

对偶步写开后是

$$
\boldsymbol{\lambda}^{k+1}=\left(1-\frac{\tau}{\rho}-\frac{\tau}{s}\right)\bar{\boldsymbol{\lambda}}^k+\frac{\tau}{\rho}\,\mathbf{q}(\mathbf{x}^{k+1},\bar{\boldsymbol{\lambda}}^k)
$$

由此得到三个事实。

**1. 对偶块是标准的强凹 Nesterov 格式。** 目标函数是

$$
\boldsymbol{\lambda}\mapsto\mathcal{D}_\rho(\mathbf{x}^{k+1},\boldsymbol{\lambda})-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2
$$

它的强凹模是 $1/s$，步长是 $\tau$，所以外推系数 $(1-\varsigma)/(1+\varsigma)$ 就是教科书里的常数动量。

**2. 你说的"额外加一个对偶正则"是对的，但这一项 LRALM 本来就有。** 按 `lem:effective-penalty`，对 $\boldsymbol{\lambda}$ 取最大后得到

$$
\max_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\mathbf{0})=\mathcal{D}_{\rho+s}(\mathbf{x},\mathbf{0})+\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}\rVert^2
$$

所以 B2′ 是在罚参数为 $\rho+s$ 的罚函数上做近端点迭代，内层的最大化每步只做一次 Nesterov 对偶步。B2′ 相对 LRALM 新增的只有外推。

**3. 从 minimax 角度看，B2′ 等于 Li26 的 Perturbed Smoothed GDA 作用在 $\mathcal{D}_\rho$ 上，再加对偶 Nesterov 外推。** 这是化简后最接近的已有算法，也是最可能撞车的地方。

## 与已知算法的关系

| 算法 | 与 B2′ 的关系 |
|---|---|
| Zhang–Xu（arXiv:2609.17973） | 不会化简成它。它每步在预测点和校正点各取一次完整梯度，共 $1+2T$ 次，还带投影；B2′ 是交替的单次梯度步。但把它作用在 $\mathcal{D}_\rho$ 上，同样得到单循环、固定 $\rho$ 的 $\epsilon^{-5/2}$（状态文件里标为推断）。 |
| Tracked-FOAM | 双层循环，不是同一个迭代；势函数的结构与我们的相同。 |
| Li26 Perturbed Smoothed GDA | 外推系数取 $0$ 时 B2′ 就是它，也就是 LRALM（$\beta=0$）。 |

## 判断

- **速率不新**：单循环、固定 $\rho$ 的 $\epsilon^{-5/2}$，Zhang–Xu 的算法已经能给出。
- **证明骨架不新**：外层值函数加内层能量的势函数，Zhang–Xu 和 Tracked-FOAM 都用过。
- **可能新的部分**：算法更简单（一次外推，不用 extragradient，不用投影，oracle 数与 LRALM 相同），以及乘子无界时的有界性证明（G1）。
- **需要补的检索**：用 minimax 的说法再查一遍，例如 "smoothed GDA / AGDA with dual momentum 或 Nesterov acceleration, nonconvex–concave, single-loop"。

现在就做这次检索吗？

---

## User (2026-11-11 12:56)

从 minimax 角度看，B2′ 等于 Li26 的 Perturbed Smoothed GDA 作用在 $\mathcal{D}_\rho$ 上，再加对偶 Nesterov 外推。 这是化简后最接近的已有算法，也是最可能撞车的地方。 但是 他们没有加动量

---

## Assistant (2026-11-11 12:57)

老大，对，Li26 没有动量，所以 Li26 本身不构成撞车。它的 GS 复杂度是 $O(\epsilon^{-3})$，B2′ 多出的对偶外推正好是 $\epsilon^{-3}$ 降到 $\epsilon^{-5/2}$ 的来源。

我上一条的意思是：撞车风险来自"在 Li26 的框架上加对偶动量"的其他论文。目前已知的这类工作只有一篇：

- **Zhang–Xu**：原文写明使用与 Li26 相同的正则化鞍点问题，再加对偶动量，得到 $\epsilon^{-5/2}$。它的更新是投影 extragradient，每步取两次完整梯度。

所以 B2′ 在文献中的位置是：

| | 辅助问题 | 对偶动量 | 原始–对偶更新 | GS 复杂度 |
|---|---|---|---|---|
| Li26 | 正则化鞍点问题 | 无 | 交替梯度步 | $\epsilon^{-3}$ |
| Zhang–Xu | 同上 | 有 | 投影 extragradient | $\epsilon^{-5/2}$ |
| B2′ | 同上 | Nesterov 外推 | 交替梯度步 | $\epsilon^{-5/2}$ |

**B2′ 的贡献可以表述为**：保留 Li26 的交替梯度步，只加一次对偶外推，就达到 Zhang–Xu 的速率，不需要 extragradient 和投影。

还没排除的情形是：有第三篇论文做了"交替梯度步加对偶 Nesterov 外推"。这要用 minimax 的关键词补一次检索才能确认。

---

## User (2026-11-11 12:57)

你给我一个指令我去检索

---

## Assistant (2026-11-11 12:57)

Written for: 一个能联网检索的模型（GPT Pro、Deep Research 一类），它没有本项目的任何上下文。

```text
Task: prior-art search. I need to know whether a specific single-loop algorithm, or an equivalent one, already exists in the literature. Report what you find with exact citations; I care more about a correct "found / not found" than about a long survey.

## The algorithm

Problem: nonconvex–concave minimax, min_x max_y K(x, y), with K smooth, nonconvex in x and concave in y. (In my application K is a reduced augmented Lagrangian and y is an unbounded multiplier, but the algorithm is stated for general K.)

Regularized saddle function with a primal proximal center z and a dual Tikhonov term:

  P(x, y; z) = K(x, y) + (1/(2γ)) ||x − z||^2 − (1/(2s)) ||y||^2.

This is the auxiliary problem of "Perturbed Smoothed GDA" in Li et al. (2026), and it is also the one used by Zhang–Xu, arXiv:2609.17973.

Iteration, for k ≥ 0, with ς = sqrt(τ/s):

  ȳ^k     = y^k + ((1 − ς)/(1 + ς)) (y^k − y^{k−1})        (dual Nesterov extrapolation)
  x^{k+1} = x^k − η ∇_x P(x^k, ȳ^k; z^k)                    (one primal gradient step)
  y^{k+1} = ȳ^k + τ ∇_y P(x^{k+1}, ȳ^k; z^k)                (one dual gradient step, alternating)
  z^{k+1} = z^k + α (x^{k+1} − z^k),   α = c·ς              (center update)

Parameters: s = Θ(1/ε), so ς = Θ(sqrt(ε)) and α = Θ(sqrt(ε)). Each iteration uses one primal gradient and one dual gradient. There is no extragradient step, no optimistic correction, no projection, and no inner loop.

Claimed result: O(ε^{-5/2}) iterations to reach an ε-game-stationary point (ε-KKT point in the ALM application). Without the extrapolation the method is Perturbed Smoothed GDA, whose rate is O(ε^{-3}).

## What counts as a hit

A. Exact or equivalent: a single-loop method for nonconvex–concave minimax (or for nonconvex constrained/composite optimization via an augmented Lagrangian) that combines (i) a moving primal proximal center, i.e. Smoothed GDA / Smoothed AGDA / proximal ALM style, with (ii) Nesterov-type extrapolation or momentum on the dual variable only, using plain alternating gradient steps. Any stated rate.

B. Near: single-loop methods reaching O(ε^{-5/2}) for nonconvex–concave problems by any momentum or acceleration mechanism on the dual block (heavy-ball, Nesterov, optimistic, anchoring), even if they also use extragradient or projection.

C. ALM-specific: nonconvex ALM, linearized ALM, or proximal ALM methods with fixed penalty parameter where the multiplier update is extrapolated or accelerated, single-loop, with a rate better than O(ε^{-3}).

## Already known to me — do not report these as new findings, but do tell me if a newer version changes their algorithm

- Zhang–Xu, arXiv:2609.17973: single-loop projected damped extragradient with dual momentum, O(ε^{-5/2}) GS.
- Pan–Zheng–Li, arXiv:2609.14235 (Tracked-FOAM): double loop, accelerated inner solver with warm start, O(ε^{-5/2}) GS.
- Li et al. 2026, Smoothed GDA and Perturbed Smoothed GDA: no momentum, O(ε^{-4}) and O(ε^{-3}).
- Zhang et al. 2020 (Smoothed GDA), Yang et al. 2022 (Smoothed-AGDA), Xu et al. 2023 (AGP), Lin–Jin–Jordan 2020 (Minimax-PPA, multi-loop), Kong–Monteiro and Melo et al. (accelerated inexact proximal ALM, multi-loop).
- Convex-case accelerated ALM/ADMM with multiplier extrapolation (He–Yuan 2010; Xu 2017).

## Where to search

arXiv (math.OC, cs.LG, stat.ML), Optimization Online, Google Scholar, Semantic Scholar, and the proceedings of NeurIPS, ICML, ICLR, COLT, AISTATS, plus SIOPT, Mathematical Programming, JMLR, MOR, COAP, JOTA. Prioritize 2020 to the present, and check the citing papers of Zhang–Xu (2609.17973), Pan–Zheng–Li (2609.14235), Li et al. 2026, Zhang et al. 2020, and Yang et al. 2022.

Suggested queries (combine and vary them):
- "smoothed GDA" momentum nonconvex-concave single-loop
- "smoothed AGDA" Nesterov OR extrapolation OR accelerated dual
- single-loop nonconvex-concave minimax "epsilon^{-2.5}" OR "ε^{-5/2}" OR "2.5"
- alternating gradient descent ascent dual momentum nonconvex concave moving proximal center
- "proximal ALM" OR "linearized ALM" nonconvex multiplier extrapolation OR "dual acceleration" single-loop
- accelerated dual ascent nonconvex augmented Lagrangian fixed penalty single loop complexity
- primal-dual nonconvex "dual extrapolation" Tikhonov regularization complexity

## Output format

1. Verdict in one line: "exact/equivalent method found", "only near methods found", or "nothing found".
2. For each relevant paper: full citation with arXiv ID or DOI, the category (A, B, or C), the update rule in its own notation (quote the equation or algorithm number), the problem class and assumptions, the stationarity measure, the rate, and single-loop or multi-loop.
3. For each category-A or close category-B paper: a term-by-term comparison with the iteration above, stating exactly which lines coincide and which differ (momentum type and where it is applied, simultaneous vs alternating updates, extragradient or not, projection or not, gradient evaluations per iteration, order of the center stepsize).
4. A list of the queries you ran and the sources you covered, so I can see what was not searched.

Rules: cite only papers you actually opened; quote equation numbers from the source; mark anything you infer rather than read as "inferred". If you cannot access a full text, say so and report what the abstract states.
```

检索结果回来后贴给我，我按 A 类逐项对照迭代式，判断是否等价。

---

## User (2026-11-11 13:12)

我们现在似乎还差两个紧界？ 我还没给你证明？

---

## Assistant (2026-11-11 13:12)

老大，对，差两个下界，仓库里都没有证明。

| 上界 | 对应的下界 | 状态 |
|---|---|---|
| 族内 $O(\epsilon^{-4})$，$\epsilon(\rho+s)\le c_1$ | 族内 $\Omega(\epsilon^{-4})$，`thm:lower-bound` | 已写入论文，紧 |
| 族内 $O(\epsilon^{-3})$，$s=c_s/\epsilon$、$\beta=0$ | 族内 $\Omega(\epsilon^{-3})$，对所有 $(\alpha,\beta)$ | 你已证明，证明没有给我，论文没有写入 |
| B2′ 的 $O(\epsilon^{-5/2})$ | 更大算法类上的 $\Omega(\epsilon^{-5/2})$ | 记录里没有任何证明 |

**第一个缺口：族内 $\Omega(\epsilon^{-3})$。** 我这边只有一条记录：你在 $s=c_s/\epsilon$ 下对所有 $(\alpha,\beta)$ 证明了它。有了它，论文才能写族内 $\Theta(\epsilon^{-3})$，才能称 B2′ 与算法族"分离"。请把证明给我，我来核对并写入。

**第二个缺口：$\Omega(\epsilon^{-5/2})$。** 这个下界我没有看到任何证明，也不确定你是否已经证了。已知的情况是：

- Pan–Zheng–Li 的 GS 下界 $\Omega(\epsilon^{-5/2})$ 不能直接转移到我们的问题类。原因是它的困难实例里对偶二次项依赖 $\mathbf{x}$，而且它的 oracle 不含 $\mathrm{prox}_h$。
- 所以 B2′ 的 $\epsilon^{-5/2}$ 目前只是上界，论文里不能写 "optimal" 或 "tight"。

第二个缺口需要先定算法类：是包含 B2′ 的一个带对偶外推的参数族，还是带 $\mathrm{prox}_h$ oracle 的一般一阶方法类。你手上的证明针对的是哪一个？

---

## User (2026-11-11 13:12)

-2.5不打算证明紧了。 
就差一个族的是吧

---

## Assistant (2026-11-11 13:13)

老大，对，只差族内 $\Omega(\epsilon^{-3})$ 这一个，证明在你手上，还没给我。

$\epsilon^{-5/2}$ 不证紧的话，论文里有两处要相应处理：

- **B2′ 的表述**：只写上界，措辞用 "improves the complexity to $O(\epsilon^{-5/2})$"，不出现 "optimal"、"tight"。Remark 里说明 $\Omega(\epsilon^{-5/2})$ 在本文问题类上是开放问题，并写进 Conclusion 的 open questions。
- **"分离"的含义**：有了族内 $\Omega(\epsilon^{-3})$，可以写 B2′ 严格快于 $\mathcal{C}_\theta$ 中 $s=c_s/\epsilon$ 的所有方法。这里要注意适用范围：你证的下界限定在 $s=c_s/\epsilon$。$\rho=c/\epsilon$、$s$ 固定等其他参数路径的族内复杂度还没有刻画，所以不能写"快于整个 LRALM 族"。

把族内 $\Omega(\epsilon^{-3})$ 的证明发我，我先核对量词和适用的参数范围，再写入。

---

## User (2026-11-11 13:20)

你可以让x1api的6-astra进行核对 或则最新的astra进行核对？  你先简单看看？ 先不要？

---

## Assistant (2026-11-11 13:22)

老大，我看过了，没有启动任何核对。现在不适合交给 astra：完整证明文件已失效，对话里只剩大步长分支的提纲，没有可逐行核对的证明。

## 两个分支的现状

| 分支 | 内容 | 状态 |
|---|---|---|
| $\alpha\le B\epsilon$ | 平台引理直接给出 $\Omega(\epsilon^{-3})$ | 已在论文里 |
| $\alpha\gt B\epsilon$ | 新的旋转实例，所有输出的残差都大于 $2\epsilon$ | 只有提纲，完整证明丢失 |

小步长分支我对照了 `lem:plateau`：它对 $[0,1]^2$ 中所有 $(\alpha,\beta)$ 成立，条件里没有 $s$ 的大小限制，也不要求 $\alpha$ 小。这一半没有问题。

## 大步长分支：提纲里有什么

- **构造**：旋转频率取 $\nu=\omega^2\alpha^2$，随 $\alpha$ 变化。其余参数沿用附录 A 的代数式。条件从 "$\epsilon s$ 小" 换成 "$d/\alpha$ 小"，其中 $d=\tau/s$。
- **结论**：对每个 $k$ 都有 $R_k\ge c_{\mathrm{r}}\alpha$，所以 $\alpha\gt B\epsilon$ 时算法永远不达标。
- **$\beta=0$**：提纲称新公式在 $\beta=0$ 仍有定义，剩余项只需要有界。

## 提纲里只有结论、没有证明的部分

1. 零初值的分解公式。提纲说沿用附录 A，但论文的 `lem:rot-spectral` 要求 $\beta\gt 0$，并断言剩余项所在不变子空间上的谱半径小于 $1$。$\beta=0$ 时提纲自己写了该子空间含单位根，所以附录 A 的论证不能直接引用。
2. 递推核的界 $4/D$，以及 $D$ 的上下界。
3. 原始剩余项的界 $X/8$ 和乘子剩余项的界。
4. 实例属于问题类：$G_f$、$L_f$ 不超过 $1$，初始间隙不超过 $\Delta$。
5. 两次 prox 的输出恒为零（提纲只给了 $3/16$ 这个数）。

GPT 在对话末尾也写明：这个分支要通过独立核验后才能当作正式定理。

## 一个需要专门核对的一致性条件

大步长分支断言 $\alpha\gt B\epsilon$ 时不收敛，而 `thm:upper-beta0` 断言 $\alpha=\kappa/(\ell s)$ 时收敛。两者相容要求 $B$ 大于 $\kappa/(\ell c_s)$。提纲没有检查这一点；如果不成立，就说明其中一个证明有错。

## 建议的顺序

1. 我按提纲和附录 A 把大步长分支重写成完整证明，存到 [overleaf/notes/gpt-proofs/](overleaf/notes/gpt-proofs/)。
2. 重写时如果某一步推不出来，我直接告诉你卡在哪里。
3. 完整稿写好后再交给 astra 核对，重点查上面五项和一致性条件。

要我现在开始第 1 步吗？

记忆里原先记的是"族内 $\Omega(\epsilon^{-3})$ 已证"，我已改成"小步长分支已证，大步长分支只有提纲"。

---

## User (2026-11-11 13:23)

给我一个比较简洁的指令 让gptpro去做 我认只差一个实例构造？

---

## Assistant (2026-11-11 13:24)

老大，对，只差大步长分支 $\alpha\gt B\epsilon$ 的困难实例，以及这个实例上的几条估计；小步长分支和上界都已经有了。

Written for: GPT Pro（能读 GitHub 仓库 `luxuan846-oss/3-DDLALM`，但不知道本次对话的内容）。

```text
任务：补全一个下界证明里缺失的分支。只做这一件事，不做文献检索，不做数值实验。

## 背景（都在仓库 overleaf/ 下）

- 算法与算法族：sections/AlgorithmFamily.tex，def:splalm 与 def:algorithm-family。算法名在仓库里可能写作 SPLALM 或 LRALM，是同一个算法。
- 问题类 I(C_0, Δ)、KKT 残差 R_k、首次达标时间 T^KKT_ε：sections/Preliminaries.tex 与 AlgorithmFamily.tex。
- 已有的旋转实例及其证明：sections/LowerBoundProof.tex 的 ex:rotation、lem:rot-spectral、lem:rot-estimates、lem:rot-trajectory，以及 appendix/LowerBoundRotation.tex。它们要求 ε(ρ+s) ≤ c_1 且 β > 0，本任务的参数区域不满足这两个条件。

## 要证的命题

固定 ρ > 0、0 < η ≤ γ、τ > 0、c_s > 0、Δ > 0，令 s = c_s/ε。证明存在与 ε、α、β 无关的常数 B 和 ε_0，使得对所有 0 < ε < ε_0、所有 α ∈ (Bε, 1]、所有 β ∈ [0,1]，存在实例 I ∈ I(C_0, Δ)（允许依赖 α、β、ε），算法从全零初值出发，对每个 k ≥ 0 都有 R_k > ε，即 T^KKT_ε = +∞。

（α ≤ Bε 的情形已由 lem:plateau 解决，不需要重做。）

## 建议的构造（之前一次推导的提纲，完整证明已丢失，请重新推导并自行判断是否成立）

记 χ = η/γ，d = τ/s。取与 ε 无关的小常数 ω，旋转频率 ν = ω²α²，并令

  V = β + d(1−β),
  W = 1 + χα(1−α) / (α² + (1−α)ν),   D = αW,
  H = V² + (1−V)ν,   J = βV + (1−V)ν,
  b² = νWH / (ητJ),   ξ = νW(V−β)/J,   a = ν(W−1)/(ηα) + ξ/η,

单位模特征值 ζ = 1 − ν/2 + i·sqrt(ν − ν²/4)。实例形式沿用 ex:rotation：A(x) = b(x − x_c)，h(y) = ‖y‖_2，f 为径向延拓的二次函数。条件 ε(ρ+s) ≤ c_1 换成 d/α ≤ δ（由 α > Bε 和 B ≥ τ/(c_s δ) 保证）。提纲声称残差满足 R_k ≥ c_r·α。

如果这个构造走不通，请给出你自己的构造，或者明确指出哪一步失败、失败的原因。

## 必须逐项写出完整证明的内容

1. 零初值轨迹的分解 w^k = w_c + ζ^k v + T^k r：给出 v、r、w_c 的显式公式并验证。注意 β = 0 时剩余项所在的不变子空间含特征值 1，附录 A 中“谱半径小于 1”的论证不适用，需要单独证明 T^k r 一致有界。
2. 剩余项的一致界：原始分量不超过旋转振幅的常数倍（小于 1），乘子分量的界不含随 s 增长的因子。
3. 实例属于 I(C_0, Δ)：逐个验证 L_f、G_f、L_A、G_A、L_h 以及 F(0) − inf F ≤ Δ。
4. 两次 prox 的输出恒为零，因此线性递推就是算法的真实轨迹。
5. 残差下界 R_k ≥ c_r·α 对所有 k ≥ 0 成立，c_r 与 ε、α、β 无关。
6. 一致性检查：appendix/UpperBoundBetaZero.tex 的 thm:upper-beta0 在 α = κ/(ℓ s)、β = 0 时给出 O(ε^{-3}) 上界。验证你的 B 满足 Bε > κ/(ℓ s)，即两个结论的参数范围不重叠。

## 输出要求

- 英文 LaTeX，宏、环境、记号与仓库论文一致，可以直接放进附录。
- 每个引理给完整证明，所有常数写出显式表达式或显式的充分条件，并说明它们依赖哪些量。
- 每一步标注：已证 / 未能证明。未能证明的步骤不要用“显然”“类似可得”带过，直接写明缺口。
- 最后单列一节，说明 β = 0 与 β > 0 两种情形在证明中的区别。
```

GPT Pro 的结果回来后发我，我先按这六项核对，再决定是否交给 astra 复审。

---

## User (2026-11-11 13:26)

我们如果想写这个章节 比较好的参考是类似的文章 最好是25年之前的？给我一个 就是加速这个章节？

---

## Assistant (2026-11-11 13:27)

老大，我推荐 **Yangyang Xu, "Accelerated first-order primal-dual proximal methods for linearly constrained composite convex programming", SIAM J. Optim. 27(3), 2017**（arXiv:1606.09155）。书目信息和下面对内容的描述是凭记忆写的，没有联网核对，用之前请对一下原文。

**选它的理由**

- **题材最接近**：它讲的就是 linearized ALM 的加速版本，先给不加速的速率，再说明改动参数后速率提高。
- **期刊对口**：SIOPT，与我们的评议参照一致。
- **写法可以直接参照**：一节之内依次是算法框、带参数条件的主定理、与未加速速率对比的 Remark，证明细节放在后面。我们这一章需要的正是"定义、定理、三条 Remark"这个结构。

**可以参照的部分**

- 算法的陈述方式：在基础迭代上标出加速新增的那一行。
- 定理的陈述方式：参数条件单独列出，结论只写一个不等式。
- Remark 的写法：说明加速来自哪个参数选择，以及与基础方法的差别。

**不能参照的部分**

它是凸问题，证明用的是加权求和的遍历估计。我们的证明是"外层值函数加内层能量"的势函数下降，证明的组织方式要另找参照。这类写法最接近的是 Zhang–Xiao–Sun–Luo 2020（Smoothed GDA，NeurIPS），论文里已经引用了它。

这两篇目前都不在 `tools/refer.bib` 和 `notes/project/literature.md` 里以 Xu 2017 的条目出现，采用的话需要新增条目。

---

## User (2026-11-11 13:29)

非凸-凹极小极大与增广拉格朗日单循环对偶外推算法先有技术检索报告

截至 2026 年 11 月 11 日的先有技术检索显示，排除您已列出的已知文献后，结果判定为 "nothing found"（若将您已知的 arXiv:2609.17973v1 计入全库视野则对应 "only near methods found"，而类别 A 在全部已发表与预印本文献中严格为空）。具体而言，针对平滑非凸-凹极小极大问题 $\min_x \max_y K(x, y)$ 及其正则化辅助鞍点函数 $P(x, y; z) = K(x, y) + \frac{1}{2\gamma}\|x - z\|^2 - \frac{1}{2s}\|y\|^2$，现有文献中不存在任何将“移动原始近端中心 $z^k$”、“仅作用于对偶变量的 Nesterov 外推 $\bar{y}^k = y^k + \frac{1-\varsigma}{1+\varsigma}(y^k - y^{k-1})$”与“无外梯度、无投影、每步仅 1 次原始梯度与 1 次对偶梯度的纯交替（Gauss–Seidel）梯度步”相结合的单循环算法，无论其声明何种收敛率（类别 A 未命中）。同时，除您已知的 Zhang–Xu（arXiv:2609.17973v1）外，未发现其他通过任何对偶动量或加速机制达到 $O(\varepsilon^{-5/2})$ 复杂度的非凸-凹单循环方法（类别 B 无新命中），亦未发现固定罚参数、对乘子更新做外推或加速且复杂度优于 $O(\varepsilon^{-3})$ 的非凸单循环增广拉格朗日（ALM）方法（类别 C 未命中）。

针对您要求核查版本变动的“已知文献”，逐篇审计确认均未演变为您的目标算法：第一，Zhang 与 Xu（arXiv:2609.17973）于 2026 年 9 月 16 日提交 v1，截至目前无 v2 更新，算法仍为单循环投影阻尼外梯度结合对偶阻尼动量状态与移动近端中心；但需注意该团队联合 H. Zhang 与 Y.-H. Dai 于 2026 年 10 月 31 日新发布了针对非线性耦合约束的单循环 ALM 扩展 ALDER（arXiv:2611.00691v1），其在乘子更新上采用欠松弛（relaxation）而非加速外推，且在对偶强凹假设下的 KKT 复杂度为 $O(\varepsilon^{-7/2})$。第二，Pan、Zheng 与 Li（arXiv:2609.14235，Tracked-FOAM）已于 2026 年 10 月 22 日更新至 v2，其算法结构未变，仍使用 Kovalev–Gasnikov 的加速 FOAM 子求解器近似求解一系列原始平滑与对偶扰动的强凸-强凹（SC-SC）子问题并跨阶段保留完整 FOAM 内部状态以消除对数因子；尤为关键的是，v2 第 1 节新增的“同期工作（Concurrent works）”综述在梳理达到 $O(\varepsilon^{-5/2})$ 博弈平稳性（GS）上界的同期文献时，仅列出 Ke 等人（arXiv:2609.25752v1，经核查为三层嵌套多循环方法）与 Zhang 和 Xu（arXiv:2609.17973v1），未见任何其他 $O(\varepsilon^{-5/2})$ 单循环方案。第三，Li 等人（arXiv:2602.14185）最新为 2026 年 4 月 29 日的 v2，全文不含任何动量机制，单循环 Perturbed Smoothed GDA 的紧复杂度仍为 $\Theta(\varepsilon^{-3})$（GS）与 $\Theta(\varepsilon^{-4})$（OS），唯一达到 $\tilde{O}(\varepsilon^{-5/2})$ 的 Perturbed Smoothed FOAM 明确为双循环算法；此外，早期基准 Zhang 等人（2020，arXiv:2010.15768）与 Yang 等人（2022，PMLR Vol. 151）亦无引入对偶 Nesterov 外推的新版本。

在已知文献之外，本次检索新打开并核查了 7 篇结构或目标最接近的边界文献（涵盖 2019 年至 2026 年 10 月末），它们从三个方向勾勒出您所提算法的新颖性边界：在非凸-凹单循环动量方向，Zhang 与 Xu 的 FORMDA（arXiv:2310.15448v2 / COAP 2024）虽引入对偶 Tikhonov 正则与动量，但缺少近端中心 $z^k$，且对原始与对偶两侧同步施加 STORM 递归方差缩减梯度动量，随机复杂度为 $\tilde{O}(\varepsilon^{-6.5})$；在单梯度步对偶线性外推方向，Thekumparampil、He 与 Oh 的 Lifted Primal-Dual（LPD，AISTATS 2022）在双线性耦合强凸-强凹及凸-强凹问题中实现了单循环对偶点列外推 $\tilde{y}_{k+1} = y_k + \theta(y_k - y_{k-1})$，但作者明确将推广至不可分耦合及非凸-凹（NC-C）情形列为未解决的公开问题；在非凸单循环 ALM 与耦合约束方向，PProx-PDA（2019）、PDAPG（arXiv:2212.04672v5）、AdaSSP（2025）及最新的 ALDER（arXiv:2611.00691v1）均采用无动量或欠松弛乘子步，没有任何工作在固定罚参数下利用无投影乘子 Nesterov 外推突破 $O(\varepsilon^{-3})$ 门槛。

1. 一句话判定结果

"nothing found"（排除您已知文献后未发现任何类别 A、B 或 C 的新方法；若计入您已知的 arXiv:2609.17973v1 则全库状态为 "only near methods found"，类别 A 严格为空）。

2. 相关文献逐篇核查详单

本节严格遵循检索规则，仅列出实际打开并查阅了全文（PDF/HTML）或官方摘要页面的文献，保留原文献记号及公式/算法编号，并对所有推断内容显式标注 inferred。下表汇总全部已核查文献的分类定位与访问深度，随后分段给出完整引用与技术细节。

文献与标识符	状态与类别判定	循环结构	对偶加速/外推机制	平稳性准则与复杂度	原文访问深度
Zhang & Xu (2026) arXiv:2609.17973v1	已知文献核查：类别 B（无 v2）	单循环	对偶梯度残差指数平滑状态 v_t, \bar{v}_t	GS: O(\varepsilon^{-5/2})；OS: O(\varepsilon^{-3})	已打开 PDF 与 HTML 全文
Pan, Zheng & Li (2026) arXiv:2609.14235v2	已知文献核查：多循环基准（v2 算法未变）	多循环（状态跨期追踪）	内层加速 FOAM 算子状态保留	GS: O(\varepsilon^{-5/2})；OS: O(\varepsilon^{-3})	已打开 PDF 与 HTML 全文
Li et al. (2026) arXiv:2602.14185v2	已知文献核查：无动量母本（v2 算法未变）	单循环（PS-GDA）/ 双循环（PS-FOAM）	单循环无任何动量或外推	单循环 GS: \Theta(\varepsilon^{-3})，OS: \Theta(\varepsilon^{-4})	已打开摘要、HTML 与 PDF
Zhang, Zhang, Xu & Dai (2026) arXiv:2611.00691v1 (ALDER)	新检索边界：未命中（非类别 B/C）	单循环（固定罚参数）	y 用阻尼状态 v_t；乘子 \lambda_t 为欠松弛（无外推）	\varepsilon-KKT：强凹下 O(\varepsilon^{-7/2})	已打开摘要与 HTML 第 1–3 节
Ke, Mei & Zhang (2026) arX[span_18](start_span)[span_18](end_span)[span_22](start_span)[span_22](end_span)iv:2609.25752v1	新检索边界：未命中（多循环同期工作）	三层嵌套多循环	内层原始-对偶联合块 u=(x,y) 中心外推	单调包含 \varepsilon-平稳点：O(\varepsilon^{-5/2})	已打开摘要、PDF 与 HTML 全文
Zhang & Xu (2024) arXiv:2310.15448v2 (FORMDA)	新检索边界：未命中（无中心、双侧动量）	单循环	原始与对偶双侧 STORM 递归梯度动量	随机目标函数 \varepsilon-平稳点：\tilde{O}(\varepsil[span_42](start_span)[span_42](end_span)[span_44](start_span)[span_44](end_span)on^{-6.5})	已打开摘要与 PDF 全文
Zhang, Wang, Xu & Dai (2022) arXiv:2212.04672v5 (PDAPG)	新检索边界：未命中（无中心、无动量）	单循环	无动量、无外推	线性耦合约束 \varepsilon-KKT：O(\varepsilon^{-4}) (inferred)	已打开摘要、HTML 与 PDF 节选
Thekumparampil, He & Oh (2022) PMLR v151 (LPD)	新检索边界：未命中（仅限凸/强凸双线性）	单循环	对偶点列线性外推 \tilde{y}_{k+1} = y_k + \theta(y_k - y_{k-1})	凸鞍点间隙：O(\[span_46](start_span)[span_46](end_span)[span_48](start_span)[span_48](end_span)[span_50](start_span)[span_50](end_span)dots\log(1/\varepsilon))	已打开 NSF PAR 全文与讲义
Hajinezhad & Hong (2019) Math. Program. (PProx-PDA)	新检索边界：未命中（无乘子外推、速率慢）	单循环（固定罚参数）	对偶扰动 (1-\rho\gamma)\lambda^r，无外推	线性约束 \varepsilon-KKT：O(\varepsilon^{-4})	已打开作者公开全文 PDF
AdaSSP (2025) Opt. Online 2025/04/AdaSSP-1	新检索边界：未命中（自适应递增罚参数）	单循环	随机自适应罚参数 \beta_k，无固定罚乘子外推	随机约束 KKT 点（引述 SPD 为 O(\varepsilon^{-5})）	已打开 Optimization Online PDF
Boţ & Böhm (2023) 10.1137/21M1465470	新检索边界：未命中（标准交替近端梯度）	单循环	无近端中心、无对偶 Nesterov 外推	值函数临界点（非加速率）	仅访问 SIAM 摘要（未获取全文）

2.1 已知核心文献版本与原文公式核查

Minghao Zhang, Zi Xu (2026), Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex--Concave Minimax Optimization, arXiv:2609.17973v1 [math.OC]（提交于 2026 年 9 月 16 日，https://doi.org/10.48550/arXiv.2609.17973，已打开 PDF 与 HTML 全文，确认无 v2 更新）。该文属于您已知的类别 B 单循环方法。其求解光滑约束问题 $\min_{x \in X} \max_{y \in Y} f(x, y)$，Assumption 2.1（式 (2.2)–(2.4)）要求 $X \subseteq \mathbb{R}^n$ 为非空闭凸集，$Y \subseteq \mathbb{R}^p$ 为非空紧致（compact）凸集且满足直径上界 $\|y\| \le D_Y$（设 $0 \in Y$），$\nabla f$ 在 $X \times Y$ 开邻域上 $L$-Lipschitz 连续（式 (2.2)），$f(x, \cdot)$ 为 $\mu$-强凹（$0 \le \mu \le L$，非凸-凹情形对应 $\mu = 0$，式 (2.3)），且值函数 $\phi(x) = \max_{y \in Y} f(x, y)$ 在 $X$ 上下有界（式 (2.4)）。基于式 (3.3) 证明中出现的原始梯度展开 $\nabla_x f(\tilde{x}_t, \tilde{y}_t) + \lambda(\tilde{x}_t - z_t)$、参数要求 $\lambda > L, \tau \ge 0, \mu + \tau > 0$ 及第 4 节关于 $\tau$ 平衡收敛界与原问题平稳性偏差的说明，可推断（inferred）其正则化鞍点函数为 $G(x, y; z) = f(x, y) + \frac{\lambda}{2}\|x - z\|^2 - \frac{\tau}{2}\|y\|^2$ 。其第 3.2 节 Algorithm 1（Single-loop projected damped extragradient method，Lines 1–12）以 $z_0 = x_0, \xi_0 = n_0 = v_0 = 0$ 初始化（Line 1），对 $t = 0, \dots, T-1$（Line 2）执行如下单循环更新 ：


$$\begin{aligned}
\tilde{x}_t &= \Pi_X\big(x_t - h[\nabla_x G(x_t, y_t; z_t) + \xi_t]\big), \qquad \tilde{y}_t = \Pi_Y\big(y_t + h[\nabla_y G(x_t, y_t; z_t) - n_t + v_t]\big) && \text{(Lines 3–4)} \\
\bar{v}_t &= \alpha v_t + (1 - \alpha)\gamma \nabla_y G(\tilde{x}_t, \tilde{y}_t; z_t) && \text{(Line 5)} \\
x_{t+1} &= \Pi_X\big(x_t - h \nabla_x G(\tilde{x}_t, \tilde{y}_t; z_t)\big), \qquad \xi_{t+1} = (x_t - x_{t+1})/h - \nabla_x G(\tilde{x}_t, \tilde{y}_t; z_t) && \text{(Lines 6–7)} \\
y_{t+1} &= \Pi_Y\big(y_t + h[\nabla_y G(\tilde{x}_t, \tilde{y}_t; z_t) + \bar{v}_t]\big), \qquad n_{t+1} = \frac{(y_t - y_{t+1})/h + \nabla_y G(\tilde{x}_t, \tilde{y}_t; z_t) + \bar{v}_t}{1 + (1 - \alpha)\gamma} && \text{(Lines 8–9)} \\
v_{t+1} &= \alpha v_t + (1 - \alpha)\gamma\big[\nabla_y G(x_{t+1}, y_{t+1}; z_t) - n_{t+1}\big], \qquad z_{t+1} = z_t + \beta(x_{t+1} - z_t) && \text{(Lines 10–11)}
\end{aligned}$$


其中法锥向量满足 $\xi_t \in N_X(x_t), n_t \in N_Y(y_t)$（式 (3.3)）。在非凸-凹（$\mu = 0$）设定下，Algorithm 1 达到优化平稳性（OS，Moreau 包络梯度 $\mathbb{E}\|\nabla \Phi_{2L}(z_{\text{out}})\|^2 \le \varepsilon^2$）与博弈平稳性（GS，含 $N_X, N_Y$ 的联合一阶残差 $R(x_{\text{out}}, y_{\text{out}}) \le \varepsilon$）的梯度评估复杂度分别为 $O(L^2 D_Y \bar{\Delta}_0 \varepsilon^{-3})$ 与 $O(L^{3/2} D_Y^{1/2} \bar{\Delta}_0 \varepsilon^{-5/2})$；加入固定中心同结构预热阶段（Algorithm 2，Corollary 4.4）后，主项复杂度分别为 $O(L^2 D_Y \Delta_\phi \varepsilon^{-3})$ 与 $O(L^{3/2} D_Y^{1/2} \Delta_\phi \varepsilon^{-5/2})$。

Siyu Pan, Taoli Zheng, Jiajin Li (2026), Optimal Deterministic First-Order Oracle Complexity for Nonconvex-Concave Minimax Optimization, arXiv:2609.14[span_61](start_span)[span_61](end_span)[span_63](start_span)[span_63](end_span)235v2 [math.OC]（v1 提交于 2026 年 9 月 13 日，v2 修订于 2026 年 10 月 22 日，https://doi.org/10.48550/arXiv.2609.14235，已打开 PDF 与 HTML 全文）。核查确认 v2 未改变 Tracked-FOAM（Algorithm 1，第 6 节）的算法机制：面对联合 $\ell$-光滑、紧致凸对偶域 $Y$（直径 $D_Y$）、初始间隙 $\Phi(x_0) - \inf_{x \in X}\Phi(x) \le \Delta$ 的问题（式 (P)），Tracked-FOAM 沿用原始平滑与对偶扰动构造一系列光滑 SC-SC 子问题，采用 Kovalev–Gasnikov (2022) 的加速 FOAM 方法求解子问题，并通过跨相邻外层子问题保留完整加速 FOAM 状态来消除每次重启的 $\log(1/\varepsilon)$ 开销，在确定性一阶预言机下同时匹配其证明的 $\Omega(\varepsilon^{-3})$（OS）与 $\Omega(\varepsilon^{-5/2})$（GS）任意确定性算法下界。v2 第 1 节亦讨论了 Wu et al. [2026]（本文未直接打开该文献原文，据 arXiv:2609.14235v2 记载其仅针对零尊重一阶算法建立 OS 下界）。

Jiajin Li, Mahesh Nagarajan, Siyu Pan, Nanxi Zhang (2026), Smoothing Meets Perturbation: Unified and Tight Analysis for Nonconvex-Concave Minimax Optimization, arXiv:2602.14185v2 [math.OC]（v1 提交于 2026 年 2 月 15 日，v2 修订于 2026 年 4 月 29 日，https://doi.org/10.48550/arXiv.2602.14185，已打开摘要、HTML 与 PDF）。核查确认 v2 未引入任何动量或外推步骤：其第 3.1 节式 (3.1) 构造结合原始平滑（$r_x > \ell$）与对偶扰动（$r_y > 0$）的代理函数 $\tilde{F}(\mathbf{x}, \mathbf{y}, \mathbf{z})$（v2 记为 $F_t(\mathbf{x}, \mathbf{y}, \mathbf{z})$，由第 2.1–3.1 节描述推断 inferred 显式形式为 $f(\mathbf{x}, \mathbf{y}) + \frac{r_x}{2}\|\mathbf{x} - \mathbf{z}\|^2 - \frac{r_y}{2}\|\mathbf{y}\|^2$），并在 Algorithm 3（Perturbed Smoothed GDA）中执行投影原始梯度步 $\mathbf{x}_{t+1} = \mathrm{proj}_{\mathcal{X}}(\mathbf{x}_t - c \nabla_{\mathbf{x}} \tilde{F}(\mathbf{x}_t, \mathbf{y}_t, \mathbf{z}_t))$ 以及无外推的 $\mathbf{y}$ 梯度上升步（步长 $\alpha > 0$）与 $\mathbf{z}$ 梯度下降中心步（步长 $\beta \in (0, 1)$）。Theorem 3 与 Theorem 4 证明该单循环算法在紧致对偶集 $\mathcal{Y}$ 上的紧迭代复杂度为 $\Theta(\ell^2 D_{\mathcal{Y}} \Delta_{\Psi_2} \varepsilon^{-3})$（GS）与 $\Theta(\ell^3 D_{\mathcal{Y}}^2 \Delta_{\Psi_2} \varepsilon^{-4})$（OS），而达到 $O(\varepsilon^{-5/2}\log(1/\varepsilon))$ 的 Perturbed Smoothed FOAM 为双循环方法。此外，已核查您列出的 Jiawei Zhang, Peijun Xiao, Ruoyu Sun, Zhi-Quan Luo (2020)（arXiv:2010.15768，第 3.1 节式 (3.2) $K(x, z; y) = f(x, y) + \frac{p}{2}\|x - z\|^2$，Algorithm 2 Smoothed-GDA，一般凹情形 Theorem 3.6 为 $O(\varepsilon^{-[span_65](start_span)[span_65](end_span)[span_67](start_span)[span_67](end_span)4})$） 与 Junchi Yang, Antonio Orvieto, Aurelien Lucchi, Niao He (2022)（PMLR Vol. 151，AISTATS 2022，分析 NC-PL 设定下的 AGDA 与 Smoothed-AGDA），两者均无添加对偶 Nesterov 外推的后续版本。

2.2 新检索并打开全文的相关边界文献

1. H. Zhang（由合作发表记录推断 inferred 为 Huiling Zhang）, Minghao Zhang, Zi Xu, Yu-Hong Dai (2026), ALDER: A Single-Loop Augmented-Lagrangian Damped Extragradient Method for Nonconvex--Concave Minimax Problems with Nonlinear Coupled Constraints, arXiv:2611.00691v1 [math.OC]（提交于 2026 年 10 月 31 日，https://doi.org/10.48550/arXiv.2611.00691；已打开摘要与 HTML 第 1–3 节，其中一般凹情形复杂度定理正文未能完整读取，但第 2 节完整迭代式与强凹情形 Theorem 16 已直接读取）。类别判定：未命中（邻近类别 B/C 边界文献）。该文求解带非线性耦合不等式约束 $c_i(x, y) \le 0$（$i \in \mathcal{K} = \{1, \dots, p\}$）的非凸-凹极小极大问题，假设条件 (A1)–(A4)（含式 (8)）要求 $\mathcal{X} \subseteq \mathbb{R}^n, \mathcal{Y} \subseteq \mathbb{R}^m$ 均为紧致凸集（$D_Y := \max_{y \in \mathcal{Y}} \|y\|$），$f$ 全梯度 $L_f$-Lipschitz 且有界，$c_i(x, \cdot)$ 凸且 $c, Jc$ 有界 Lipschitz，并满足一致严格可行方向条件 $\delta + \nabla_y c_i(x, y)^\top d(x, y) \le 0$。针对增广拉格朗日函数 $\mathcal{L}_\gamma(x, y, \lambda) := f(x, y) - P_\gamma(x, y, \lambda)$（式 (3)，固定罚参数 $\gamma$），第 2 节 Algorithm 1 在 $(x_t, y_t)$ 上利用法锥残差 $\xi_t, n_t$ 与阻尼状态 $v_t$ 执行同步投影预测-校正步（对偶校正使用 $\bar{v}_t = \alpha v_t + \vartheta \nabla_y G(\tilde{x}_t, \tilde{y}_t, z_t, \lambda_t)$），随后对约束乘子执行正象限投影与欠松弛（relaxation）更新并移动近端中心：


$$\widetilde{\lambda}_{t+1} = [\lambda_t + \gamma c(x_{t+1}, y_{t+1})]_+, \qquad \lambda_{t+1} = (1 - \theta_t / \gamma)\lambda_t + (\theta_t / \gamma)\widetilde{\lambda}_{t+1}, \qquad z_{t+1} = z_t + \beta(x_{t+1} - z_t).$$


该算法为单循环，平稳性度量为 $\varepsilon$-KKT 点。由于乘子 $\lambda_t$ 采用欠松弛而非外推加速，且 Theorem 16 显示即便在对偶强凹假设下也需要 $1 + 2T_1 = O(\varepsilon^{-7/2})$ 次梯度评估（由此推断 inferred 一般凹情形复杂度幂次不低于 $7/2$），未优于 $O(\varepsilon^{-3})$；而当耦合约束退化消失（式 (2)）时，ALDER 直接退化为您已知的 arXiv:2609.17973v1。

2. Shaozhe Ke, Sanyou Mei, Jiheng Zhang (2026), Efficient Parameter-Free First-Order Methods for Nonsmooth Composite Minimax Optimization, arXiv:2609.25752v1 [math.OC]（提交于 2026 年 9 月 22 日，https://doi.org/10.48550/arXiv.2609.25752，已打开摘要、PDF 与 HTML 全文）。类别判定：未命中（多循环 $O(\varepsilon^{-5/2})$ 对照文献）。该文求解非光滑复合非凸-凹问题 $\min_x \max_y \{h(x, y) + p(x) - q(y)\}$，Assumption 1 要求 $p, q$ 为近端算子可精确计算的适当闭凸函数、对偶域有界 $\|y\| \le D_y$、$h$ 在 $\mathcal{X} \times \mathcal{Y}$ 上 $L_{\nabla h}$-光滑且对 $y$ 凹、最优值 $H^*$ 有限。其方法为三层嵌套多循环架构：外层近端点循环（式 (16)–(17)）构造正则化子问题 $h_t(x, y) = h(x, y) + \beta_t \|x - x^t\|^2 - \frac{\mu}{2}\|y - y^0\|^2$（式 (16)），在算子评估上限（式 (17)）内调用 Algorithm 2（SCSC 累积正则化法），后者反复调用 Algorithm 1（SCSC 收缩非精确近端法，式 (6)–(11)），而 Algorithm 1 内部还需调用满足 Assumption 3 的单调包含子求解器 $\mathcal{A}$，并在原始-对偶联合向量 $u = (x, y)$ 上执行中心外推 $c^{k+1} = \tilde{u}^{k+1} + \frac{k}{k+3}(\tilde{u}^{k+1} - \tilde{u}^k) + \frac{k+2}{(k+3)\mu_x}(2r_x^{k+1}, -r_y^{k+1})$（式 (10)）。其达到单调包含 $\var[span_131](start_span)[span_131](end_span)[span_134](start_span)[span_134](end_span)[span_137](start_span)[span_137](end_span)epsilon$-平稳点的总算子评估复杂度为 $O(\varepsilon^{-5/2})$（无对数因子，含无参数变体 Algorithm 3），但不属于单循环方法 。

3. Huiling Zhang, Zi Xu (2024), An accelerated first-order regularized momentum descent ascent algorithm for stochastic nonconvex-concave minimax problems, Computational Optimization and Applications, Vol. 90, No. 2（2024 年 12 月在线发表），预印本 arXiv:2310.15448v2 [math.OC]（已打开摘要与 PDF 全文）。类别判定：未命中。针对有界域上的随机光滑非凸-凹极小极大问题，第 2 节式 (2.1) 引入纯对偶 Tikhonov 正则化函数 $g_k(x, y) = g(x, y) - \frac{\rho_k}{2}\|y\|^2$（无移动原始近端中心 $z^k$），Algorithm 1（FORMDA）在式 (2.5)–(2.6) 中对原始与对偶两侧同时构造 STORM 型递归动量估计子 $v_k = \nabla_x \tilde{G}_k(x_k, y_k; I_k) + (1 - \gamma_{k-1})[v_{k-1} - \nabla_x \tilde{G}_{k-1}(x_{k-1}, y_{k-1}; I_k)]$ 与 $w_k = \nabla_y \tilde{G}_k(x_k, y_k; I_k) + (1 - \theta_{k-1})[w_{k-1} - \nabla_y \tilde{G}_{k-1}(x_{k-1}, y_{k-1}; I_k)]$，并在 Step 3 执行同步投影更新。该算法为单循环，达到目标函数 $\varepsilon$-平稳点的随机迭代复杂度为 $\tilde{O}(\varepsilon^{-6.5})$。

4. Huiling Zhang, Junlin Wang, Zi Xu, Yu-Hong Dai (2022), Primal Dual Alternating Proximal Gradient Algorithms for Nonsmooth Nonconvex Minimax Problems with Coupled Linear Constraints, arXiv:2212.04672v5 [math.OC]（已打开摘要、HTML 与 PDF 节选）。类别判定：未命中。针对带耦合线性约束 $Ax + By - c \le 0$（满足相对内部 Slater 型条件）的非光滑非凸-凹极小极大问题，第 2.2 节式 (10) 构造对偶正则化拉格朗日函数 $\mathcal{L}_k(x, y, \lambda) = \mathcal{L}(x, y, \lambda) - \frac{\rho_k}{2}\|y\|^2$，Algorithm 1（PDAPG，Steps 1–5）交替执行 $y_{k+1} = \mathrm{Prox}_{g, \mathcal{Y}}^\beta(y_k + \frac{1}{\beta}\nabla_y \mathcal{L}(x_k, y_k, \lambda_k) - \frac{\rho_k}{\beta}y_k)$（Step 2）、$x_{k+1}$ 近端梯度步（Step 3）及无外推乘子梯度步 $\lambda_{k+1} = \lambda_k - \gamma_k \nabla_\lambda \mathcal{L}(x_{k+1}, y_{k+1}, \lambda_k)$（式 (13) / Step 4）。该算法为单循环，无移动原始中心 $z^k$ 且无任何动量外推；达到 $\varepsilon$-KKT 点（$\|\nabla G_{\alpha_k, \beta, \gamma_k}(x_{k+1}, y_{k+1}, \lambda_{k+1})\| \le \varepsilon$，Step 5）的非凸-凹迭代复杂度与 AGP 及 Smoothed GDA 相同（由第 1 节第 70–71 行明确声明匹配该二者复杂度，推断 inferred 为 $O(\varepsilon^{-4})$）。

5. Kiran K. Thekumparampil, Niao He, Sewoong Oh (2022), Lifted Primal-Dual Method for Bilinearly Coupled Smooth Minimax Optimization, Proceedings of the 25th International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR Vol. 151, 2022（NSF PAR 存档 https://par.nsf.gov/servlets/purl/10334339，已打开论文 PDF 与作者公开报告讲义；所打开文档未标注 DOI 或 arXiv ID）。类别判定：未命中（凸情形对偶外推结构参照）。该文针对双线性耦合问题 $\varphi(x, y) = f(x) + \langle y, Ax \rangle - h(y)$（式 (3)），在 Assumption 1（$f$ 为 $L_x$-光滑且 $\mu_x$-强凸或凸，$h$ 为 $L_y$-光滑且 $\mu_y$-强凸）下提出单循环 Lifted Primal-Dual（LPD）算法，每步仅调用 1 次梯度预言机，利用对偶线性外推 $\tilde{y}_{k+1} = y_k + \theta(y_k - y_{k-1})$（引自作者 AISTATS 讲义更新式，正文摘录未含该式编号）达到最优 $\varepsilon$-原始-对偶间隙复杂度 $O\big((\sqrt{L_x/\mu_x} + \|A\|/\sqrt{\mu_x \mu_y} + \sqrt{L_y/\mu_y})\log(1/\varepsilon)\big)$（Theorem 2）。作者在结论中明确指出，将该单循环对偶外推框架推广至一般不可分耦合及 NC-SC、NC-C（非凸-凹）设定仍是未解决的公开问题。

6. Davood Hajinezhad, Mingyi Hong (2019), Perturbed Proximal Primal-Dual Algorithm for Nonconvex Nonsmooth Optimization, Mathematical Programming, 2019（已打开作者公开全文 PProx_PDA.pdf，文档未附 DOI 或 arXiv ID）。类别判定：未命中（类别 C 边界文献）。针对线性等式约束非凸复合问题 $\min_{x \in X} f(x) + h(x) \text{ s.t. } Ax = b$（式 (1)，$X$ 紧致凸），其 Algorithm 1（PProx-PDA）在原始步（式 (3a) 及其最优性条件式 (17)）中最小化线性化近似增广拉格朗日函数，包含对偶阻尼扰动项 $(1 - \rho\gamma)\lambda^r$（$\rho\gamma < 1$）与以上一步迭代点为中心的近端项 $\frac{\beta}{2}\|B(x - x^r)\|^2$，但不含慢速移动中心 $z^k$，乘子更新亦无任何外推或动量，单循环达到 $\varepsilon$-KKT 点的复杂度为 $O(\varepsilon^{-4})$。

7. AdaSSP (2025), An adaptive single-loop stochastic penalty method for nonconvex constrained stochastic optimization, Optimization Online 2025/04/AdaSSP-1.pdf（已打开预印本 PDF 第 1–2 节；首页作者行未在摘录中显示，无 DOI）。类别判定：未命中。针对带确定性约束的非凸随机优化，第 2 节式 (2) 定义标准增广拉格朗日函数 $L_\beta(x, \lambda) = f(x) + \psi_\beta(c(x), \lambda)$，Algorithm 1（AdaSSP）通过依随机迭代进展自适应递增罚参数 $\{\beta_k\}$ 构建单循环罚方法（非固定罚参数乘子外推），并在综述中记载同类单循环随机原始-对偶法 SPD 达到 $\varepsilon$-平稳点的复杂度为 $O(\varepsilon^{-5})$。

2.3 未能访问全文、仅核查摘要的文献

Radu Ioan Boţ, Axel Böhm (2023), Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex-Concave Minimax Problems, SIAM Journal on Optimization, Vol. 33, No. 3, https://doi.org/10.1137/21M1465470（预印本 arXiv:2007.13605）。受期刊访问权限限制，本次未能打开该文全文，仅访问其 SIAM 官方摘要页：摘要指出该文针对非凸-凹设定下寻找值函数 $\psi(\cdot) := \max_y \Psi(\cdot, y)$ 临界点的问题，证明了随机交替近端梯度法（AGDA）的全局收敛速率；结合已打开文献对其的交叉引用说明，该方法为标准无平滑中心、无对偶 Nesterov 外推的交替近端梯度步，不属于类别 A 或 B。

---

3. 与相近类别 B 及同族单循环方法的逐项行级比对

由于类别 A 无命中结果，本节将您的四行迭代方案与全库唯一达到 $O(\varepsilon^{-5/2})$ 的单循环类别 B 文献 Zhang–Xu（arXiv:2609.17973v1 Algorithm 1）、该团队最新的单循环约束增广拉格朗日推广 ALDER（arXiv:2611.00691v1 Algorithm 1）以及您的无外推直接退化基准 Perturbed Smoothed GDA（arXiv:2602.14185v2 Algorithm 3）进行逐行、逐项精确比对。

比对维度 / 迭代行	您的待查算法	Zhang–Xu (arXiv:2609.17973v1, Alg. 1)	ALDER (arXiv:2611.00691v1, Alg. 1)	Perturbed Smoothed GDA (arXiv:2602.14185v2, Alg. 3)
正则化鞍点函数	P(x, y; z) = K(x, y) + \frac{1}{2\gamma}\|x - z\|^2 - \frac{1}{2s}\|y	重合：G(x, y; z) = f(x, y) + \frac{\lambda}{2}\|x - z\|^2 - \frac{\tau}{2}\|y（对偶项形式 inferred）	相异：增广拉格朗日 \mathcal{L}_\gamma(x, y, \lambda) 叠加原始近端中心 z_t	重合：\tilde{F}(x, y, z) = f(x,[span_91](start_span)[span_91](end_span)[span_99](start_span)[span_99](end_span) y) + \frac{r_x}{2}\|x - z\|^2 - \frac{r_y}{2}\|y（合并形式 inferred）
第 1 行（动量类型与作用位置）	仅对偶点列 Nesterov 外推：\bar{y}^k = y^k + \frac{1-\varsigma}{1+\varsigma}(y^k - y^{k-1})，\varsigma = \sqrt{\tau/s}	相异：无点列外推 \bar{y}^k；仅在对偶侧维护阻尼梯度残差移动平均向量 \bar{v}_t, v_{t+1}（Lines 5, 10），注入预测步与校正步（Lines 4, 8）	相异：鞍点变量 y 用阻尼梯度状态 v_t, \bar{v}_t；ALM 乘子 \lambda_t 用欠松弛 \lambda_{t+1} = (1-\theta_t/\gamma)\lambda_t + (\theta_t/\gamma)\widetilde{[span_34](start_span)[span_34](end_span)[span_36](start_span)[span_36](end_span)[span_38](start_span)[span_38](end_span)\lambda}_{t+1}	相异：无任何动量或外推（取 \bar{y}^k = y^k 即退化为此基准）
第 2–3 行（同步 vs 交替更新）	纯交替（Gauss–Seidel）更新：先算 x^{k+1} = x^k - \eta \nabla_x P(x^k, \bar{y}^k; z^k)，再用最新 x^{k+1} 算 y^{k+1} = \bar{y}^k + \tau \nabla_y P(x^{k+1}, \bar{y}^k; z^k)	相异：两阶段同步更新——预测步 (\tilde{x}_t, \tilde{y}_t) 同步在 (x_t, y_t) 处评估（Lines 3–4），校正步 (x_{t+1}, y_{t+1}) 同步在 (\tilde{x}_t, \tilde{y}_t) 处评估（Lines 6, 8）	相异：(x, y) 为两阶段同步预测-校正步，仅耦合约束乘子 \widetilde{\lambda}_{t+1} 在 (x_{t+1}, y_{t+1}) 更新后计算	部分相异：在无外推点 (x_t, y_t, z_t) 上执行单步原始下降与对偶上升
外梯度（Extragradient）与否	无外梯度（亦无乐观梯度校正项）	含阻尼外梯度：核心依赖预测点 (\tilde{x}_t, \tilde{y}_t) 与校正点 (x_{t+1}, y_{t+1}) 的双阶段外梯度步	含阻尼外梯度：(x, y) 更新采用投影阻尼外梯度预测-校正步	无外梯度
投影与对偶域有界性	无投影；支持 y \in \mathbb{R}^m 无界乘子（适配约化 ALM）	含投影且强依赖有界对偶域：每步执行 4 次投影（\Pi_X, \Pi_Y 各 2 次，Lines 3, 4, 6, 8），维护法锥向量 \xi_t \in N_X(x_t), n_t \in N_Y(y_t)（Lines 7, 9），复杂度显式依赖紧致集直径 D_Y	含投影与紧致域假设：(x, y) 要求紧致集投影与法锥残差 \xi_t, n_t，不等式乘子含正象限投影 [\cdot]_+	含原始投影与紧致对偶域假设：原始步含 \mathrm{proj}_{\mathcal{X}}，对偶扰动偏差控制显式依赖紧致集直径 D_{\mathcal{Y}}
每步梯度评估次数	1 次原始梯度 \nabla_x P + 1 次对偶梯度 \nabla_y P（共 2 次偏梯度）	相异（开销翻倍）：每步需在 (\tilde{x}_t, \tilde{y}_t) 与 (x_{t+1}, y_{t+1}) 处计算 2 次全梯度（即 2 次 \nabla_x f + 2 次 \nabla_y f，共 4 次偏梯度；跨步缓存复用 Line 10 梯度 inferred）	相异：每步 2 次全梯度与约束 Jacobian 评估（Theorem 16 精确计为 1 + 2T_1）	重合：每步 1 次原始梯度 + 1 次对偶梯度
第 4 行（中心更新与步长量级）	z^{k+1} = z^k + \alpha(x^{k+1} - z^k)，步长 \alpha = c\cdot\varsigma = \Theta(\sqrt{\varepsilon})	完全重合：Line 11 为 z_{t+1} = z_t + \beta(x_{t+1} - z_t)；在 \tau = \Theta(\varepsilon/D_Y) 下有效条件数 \kappa_y = L/\tau = \Theta(\varepsilon^{-1})，故 \beta = \Theta(1/\sqrt{\kappa_y}) = \Theta(\sqrt{\varepsilon})（量级 inferred）	形式重合，量级更慢：形式同为 z_{t+1} = z_t + \beta(x_{t+1} - z_t)，但受耦合约束惩罚限制，强凹下总复杂度为 O(\varepsilon^{-7/2})	形式重合，量级相异：中心更新式相同，但无对偶动量加速时中心步长受限于 \beta = \Theta(\varepsilon)（量级 inferred），总速率 \Theta(\varepsilon^{-3})

3.1 逐行重合度与机理差异深度解析

综合上述行级对照，您的算法与最相近的类别 B 单循环方法 Zhang–Xu（arXiv:2609.17973v1 Algorithm 1）仅在辅助目标函数结构与第 4 行近端中心凸组合步 $z^{k+1} = z^k + \alpha(x^{k+1} - z^k)$（含 $\Theta(\sqrt{\varepsilon})$ 步长阶）上重合，而在前 3 行核心原始-对偶更新上采用了完全不同的数学稳定化与加速路径 。

首先，在动量形态与状态空间（第 1 行对比 Lines 4, 5, 8, 10）上，您的第 1 行直接对无约束对偶点列执行经典 Nesterov 强凹外推 $\bar{y}^k = y^k + \frac{1-\varsigma}{1+\varsigma}(y^k - y^{k-1})$，外推动量率由对偶步长 $\tau$ 与 Tikhonov 正则模量 $1/s$ 的几何比值 $\varsigma = \sqrt{\tau/s} = \Theta(\sqrt{\varepsilon})$ 唯一确定，仅需保留前一时刻点 $y^{k-1}$；而 Zhang–Xu 并未对 $y_t$ 进行点列外推，而是额外引入辅助状态 $v_t \in \mathbb{R}^p$ 与法锥残差 $n_t \in N_Y(y_t)$，在每步内部对预测点对偶梯度 $\nabla_y G(\tilde{x}_t, \tilde{y}_t; z_t)$（Line 5）和校正点有效对偶梯度 $[span_92](start_span)[span_92](end_span)[span_100](start_span)[span_100](end_span)\nabla_y G(x_{t+1}, y_{t+1}; z_t) - n_{t+1}$（Line 10）做两次指数加权平滑，本质上属于带法锥补偿的梯度级阻尼重球/锚定滤波 。

其次，在耦合稳定性来源与预言机开销（第 2–3 行对比 Lines 3–9）上，一般鞍点问题若在同步梯度步上直接施加单侧 Nesterov 外推，双线性或非线性交叉导数项会破坏能量函数的单调下降；Zhang–Xu 为压制这一同步耦合失稳，不得不引入投影外梯度预测-校正循环（Lines 3–4 预测、Lines 6–9 校正）。即便观察到 $\nabla_y G(x, y; z)$ 与中心 $z$ 无关，从而可将第 $t$ 步 Line 10 计算的 $\nabla_y f(x_{t+1}, y_{t+1})$ 连同 $\nabla_x f(x_{t+1}, y_{t+1})$ 一并缓存复用于第 $t+1$ 步的预测步 Lines 3–4（inferred），Zhang–Xu 每步仍需在 $(\tilde{x}_t, \tilde{y}_t)$ 与 $(x_{t+1}, y_{t+1})$ 两点处各做一次完整梯度评估（每步 2 次原始梯度 + 2 次对偶梯度）。相比之下，您的第 2–3 行利用了 $P(\cdot, \bar{y}^k; z^k)$ 在近端系数 $\frac{1}{\gamma} > L$ 下具有 $O(1)$ 条件数强凸性的结构优势，先在外推对偶点 $\bar{y}^k$ 处做一步原始梯度下降得到 $x^{k+1}$，随即在对偶步中代入最新原始点计算 $\nabla_y P([span_94](start_span)[span_94](end_span)[span_102](start_span)[span_102](end_span)x^{k+1}, \bar{y}^k; z^k)$。这种 Gauss–Seidel 交替顺序在不增加任何额外梯度评估的前提下提供了隐式预测-校正阻尼，使每步开销严格保持在 1 次原始梯度与 1 次对偶梯度，解答了此前 LPD（Thekumparampil 等，2022）仅在凸双线性问题中实现而在非凸-凹不可分情形下悬而未决的单步对偶外推难题。

最后，在投影算子与无界乘子适配性上，Zhang–Xu（arXiv:2609.17973v1）、Pan 等（arXiv:2609.14235v2）、Ke 等（arXiv:2609.25752v1）以及 Li 等（arXiv:2602.14185v2）的 $\varepsilon$-GS 界全部显式包含紧致对偶域直径 $D_Y$（通过先验假设 $\|y\| \le D_Y$ 来界定对偶 Tikhonov 项 $-\frac{1}{2s}\|y\|^2$ 引发的 $\frac{1}{s}\|y\|$ 梯度扰动误差）。当 $K(x, y)$ 取为非凸约束优化的约化增广拉格朗日函数时，拉格朗日乘子 $y$ 天然无先验紧致集合约束；您的算法完全省去欧氏投影 $\Pi_X, \Pi_Y$ 与法锥追踪变量 $\xi_t, n_t$，直接在全空间上以单循环 $O(\varepsilon^{-5/2})$ 迭代逼近 $\varepsilon$-KKT 点，这一特性在 ALDER（arXiv:2611.00691v1）、PDAPG（arXiv:2212.04672v5）与 PProx-PDA（2019）等现有单循环 ALM 文献中均无对应实现。

4. 已执行的检索式与数据源覆盖范围

4.1 实际执行的检索式清单

本次检索围绕平滑近端中心 GDA、对偶动量/外推、$O(\varepsilon^{-5/2})$ 单循环复杂度、非凸固定罚参数 ALM 以及核心文献引文链，组合执行了以下 26 条检索式：

1. "2609.17973" OR "2509.17973" OR "2409.17973"

2. "2609.14235" OR "2509.14235" OR "2409.14235" OR "Tracked-FOAM"

3. "Perturbed Smoothed GDA" OR "Perturbed Smoothed-GDA"

4. "smoothed GDA" momentum nonconvex-concave single-loop

5. single-loop nonconvex-concave minimax "epsilon^{-2.5}" OR "epsilon^{-5/2}" OR "ε^{-5/2}" OR "5/2"

6. "Matching Multi-Loop Comp[span_186](start_span)[span_186](end_span)lexities with a Single Loop"

7. "Ke" "2026" nonconvex-con[span_187](start_span)[span_187](end_span)cave minimax "5/2" OR "game stationarity" OR "optimization stationarity"

8. "Smoothing Meets Perturbation: Unified and Tight Analysis"

9. "2609.25752" "Al[span_191](start_span)[span_191](end_span)gorithm" OR "single-loop" OR "double-loop" OR "inner" OR "5/2"

10. "2609.17973" "Algorithm 1" "Initialize"

11. "A Single-Loop S[span_193](start_span)[span_193](end_span)moothed Gradient Descent-Ascent" "Nesterov" OR "extrapolation" OR "dual momentum"

12. "2611.00691" OR "ALDER: A Single-Loop Augmented-Lagrangian"

13. "2609.17973" OR "2609.14235" OR "2602.14185" site:arxiv.org

14. "Lifted Primal-Dual" nonconvex minimax OR "augmented Lagrangian" single-loop

15. "Single-Loop" "Augmented Lagrangian" OR "ALM" "5/2" OR "-2.5" OR "epsilon^{-2.5}" nonconvex

16. "2611.00691" "Algorithm 1" OR "5/2" OR "Theorem"

17. "PDAPG" "PDPG-L" "Primal Dual Alternating Proximal Gradient" nonconvex minimax

18. "Boţ" "Böhm" "Alternating proximal-gradient steps" minimax momentum OR e[span_116](start_span)[span_116](end_span)xtrapolation OR center

19. "PProx-PDA" "Hajinezhad" "Hong" extrapolation OR momentum OR Nesterov

20. "2611.00691" "complexity" OR "varepsilon" OR "K[span_128](start_span)[span_128](end_span)KT" OR "Algorithm 1"

21. "accelerated first-order regularized m[span_197](start_span)[span_197](end_span)omentum descent ascent" "FORMDA"

22. "2212.04672" "PDAPG" OR "PDPG-L" "Algorithm"

23. "2609.142[span_129](start_span)[span_129](end_span)35" "Algorithm 1" "TRACKED-FOAM" OR "Tracked-FOAM"

24. "2602.14185v2" "Perturbed Smoothed GDA" "Algorithm 3"

25. "2007.13605" "Algorithm 1" "Boţ" OR "Böhm"

26. nonconvex-concave "single-loop" ("optimistic" OR "heavy-ball" OR "Halpern" OR "anchored") ("5/2" OR "-2.5" OR "proximal center" OR "Smoothed")

4.2 已覆盖数据源与检索盲区说明

在已覆盖范围方面，本次检索直接穿透了截至 2026 年 11 月初的 arXiv（math.OC、cs.LG、stat.ML 的 PDF 与实验性 HTML 全文索引，完整追踪了 2609.17973v1、2609.14235v2、2602.14185v2 的正向施引文献及核心作者 Zi Xu、Minghao Zhang、Huiling Zhang、Jiajin Li、Siyu Pan、Taoli Zheng 的全部近期预印本如 2611.00691v1、2610.20345v1、2609.35206v1）、Optimization Online（含 2025–2026 年约束优化与极小极大预印本 PDF）、Google Scholar 作者主页与 Semantic Scholar 引文卡片、DBLP 与 ResearchGate 出版物记录，以及 PMLR（ICML / AISTATS）、NeurIPS / ICLR（OpenReview）、JMLR 全文库和 SIAM（SIOPT 施引列表至 2026 年 10 月）、Springer（Mathematical Programming、COAP、Journal of Global Optimization）的索引与对应开放预印本。

在未覆盖或受限盲区方面，存在三处边界供您参考：其一，对于发表在 Mathematics of Operations Research (MOR)、Journal of Optimization Theory and Applications (JOTA)、SIOPT 或 Mathematical Programming 付费墙内、既未在 arXiv / Optimization Online 存放预印本、亦未被上述 2026 年 9–11 月核心综述（如 arXiv:2609.17973v1 与 arXiv:2609.14235v2）引用的纯期刊论文，公开全文检索无法直接读取其内部公式。其二，针对传统非凸算子分裂与 ADMM 社区可能完全不使用 "minimax"、"GDA" 或 "5/2" 等复杂度术语，而是仅证明渐近收敛或基于 Kurdyka–Łojasiewicz（KŁ）性质研究带惯性/乘子外推的线性化 ALM 或近端 ADMM 的工作（即声称速率不优于 $O(\varepsilon^{-3})$ 或无全局非渐近 $\varepsilon$-KKT 速率，仅潜在关联类别 A 的定性结构），本次检索主要通过 PProx-PDA 引文链与 "Single-Loop" "Augmented Lagrangian" 复杂度检索式覆盖了非渐近复杂度分支，未对无复杂度界的纯渐近惯性 ADMM 文献做穷尽式排查。其三，对于 2026 年 10 月 31 日新提交的 arXiv:2611.00691v1（ALDER），本次已核实其第 2 节全部更新式（确认乘子为欠松弛而非外推）及强凹情形 Theorem 16（$O(\varepsilon^{-7/2})$），但未读取其一般凹情形复杂度定理的完整段落。




Sources used in the report
  [2609.17973] Matching Multi-Loop Complexities with a Single ... - arXiv

  Matching Multi-Loop Complexities with a Single Loop - arXiv

  Matching Multi-Loop Complexities with a Single Loop - arXiv

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  Taoli Zheng - Google Scholar

  Smoothing Meets Perturbation: Unified and Tight Analysis for ... - arXiv

  Smoothing Meets Perturbation: Unified and Tight Analysis for ... - arXiv

  Unified and Tight Analysis for Nonconvex-Concave Minimax ... - arXiv

  Matching Randomized Bounds for Finite-Sum Nonconvex-Concave

  Faster Single-loop Algorithms for Minimax Optimization without

  Minghao Zhang (disambiguation) - dblp

  Tight Lower Bounds for Stochastic Nonconvex-Strongly-Concave

  Efficient Parameter-Free First-Order Methods for Nonsmooth ... - arXiv

  Efficient Parameter-Free First-Order Methods for Nonsmooth

  Efficient Parameter-Free First-Order Methods for Nonsmooth ... - arXiv

  Siyu Pan - Google Scholar

  Efficient Parameter-Free First-Order Methods for Nonsmooth ... - arXiv

  ALDER: A Single-Loop Augmented-Lagrangian Damped ... - arXiv

  Envelope Cubic Regularized Newton Method for Nonconvex ... - arXiv

  A Single-Loop Smoothed Gradient Descent-Ascent Algorithm ... - arXiv

  Are Single-Loop Algorithms Sufficient for Unbalanced Minimax

  ALDER: A Single-Loop Augmented-Lagrangian Damped ... - arXiv

  Lifted Primal-Dual Method for Bilinearly Coupled Smooth Minimax

  Lifted Primal-Dual Method for Bilinearly Coupled Smooth Minimax

  (PDF) Primal Dual Alternating Proximal Gradient Algorithms for

  ACCELERATED OVER-RELAXATION HEAVY-BALL METHOD

  A first-order augmented Lagrangian method for constrained minimax

  An adaptive single-loop stochastic penalty method for nonconvex

  Huiling Zhang's research while affiliated with Shanghai University

  Alternating proximal-gradient steps for (stochastic) nonconvex

  Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex

  Radu Ioan Boţ (Speaker)

  Axel Böhm PostDoc Position at University of Vienna - ResearchGate

  Nonsmooth Nonconvex-Concave Minimax Optimization - arXiv

  Perturbed Proximal Primal Dual Algorithm for Nonconvex

  Damped Proximal Augmented Lagrangian Method for weakly ... - arXiv

  Fast First-Order Methods for Large-Scale Nonconvex Optimization

  An accelerated first-order regularized momentum descent ascent

  An accelerated first-order regularized momentum descent ascent

  Iterative Minimax Games with Coupled Linear Constraints - arXiv

  Iterative Minimax Games with Coupled Linear Constraints - arXiv

  a single loop method for quadratic minmax optimization

  Faster Single-loop Algorithms for Minimax Optimization without

  Global Convergence and Variance Reduction for a Class of

  [PDF] A Single-Loop Smoothed Gradient Descent-Ascent Algorithm

  Two-Timescale Gradient Descent Ascent Algorithms for Nonconvex




Sources read but not used
  Publikationen (begutachtet) - Institut für Theoretische Physik

  The coupling flow for supergravity | Request PDF - ResearchGate

  Nicolai map in nLab

  JHEP02(2026)185 - CERN

  Olaf Lechtenfeld in nLab

  Towards a Nicolai map for supergravity - SCOAP3 Repository

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  非凸-凹极小极大优化的最优确定性一阶预言机复杂度 - arXivDaily

  $\mathbb{R}^d$ 上的形变量子化｜arXiv 2509.14235｜arXivDaily

  Taoli Zheng's research works | Chinese University of Hong Kong

  [Literature Review] Smoothing Meets Perturbation: Unified and Tight

  [PDF] A first-order method for nonconvex-nonconcave minimax

  [PDF] Lower Bounds for Nonconvex-Concave Minimax Optimization

  [PDF] A Primal-Dual Smoothing Framework for Max-Structured Non

  1 Introduction - arXiv

  Ruoyu Sun | alphaXiv

  NeurIPS Poster A Single-Loop Accelerated Extra-Gradient

  [PDF] Faster Single-loop Algorithms for Minimax Optimization

  A classification of the Nim-sequences for the two-element

  Computer Science Sep 2026 - arXiv

  Nest Your Adaptive Algorithm for Parameter-Agnostic Nonconvex

  41. Machine Learning

  A novel adaptive non-convex TV model in image restoration

  Publications - Jianqing Fan - Princeton University

  Advances in Quadratic Programming: Regularization, Learning

  Publications - Jiajin Li

  非凸-凹极小极大优化的下界｜arXiv 2609.14233 - arXivDaily

  Mathematics - arXiv

  Envelope Cubic Regularized Newton Method for Nonconvex ... - arXiv

  Statistics Nov 2026 - arXiv

  Machine Learning - arXiv

  [论文评述] A Single-Loop Stochastic Gradient Algorithm for Minimax

  ALDER: A Single-Loop Augmented-Lagrangian Damped

  Gradient Norm Regularization Second-Order Algorithms for Solving

  Machine Learning - arXiv

  [Revue de papier] Matching Multi-Loop Complexities with a Single

  Deep Truncated FBSDE Method for High-Dimensional Nonlinear

  Publications · ODI - Optimization and Decision Intelligence Group

  A Stochastic Linearized Augmented Lagrangian Method for

  A Newton-CG Based Augmented Lagrangian Method for Finding a

  The inexact power augmented Lagrangian method ... - OpenReview

  Statistics - arXiv

  Computer Science - arXiv

  Mathematics - arXiv

  NDLI: Primal Dual Alternating Proximal Gradient Algorithms for

  Zeroth-Order primal-dual Alternating Projection Gradient Algorithms

  The 14th International Conference on Numerical Optimization and

  liangzid/robench-eval-Time27-c · Datasets at Hugging Face

  张量优化与数据科学研讨会程序册 - 陈省身数学研究所- 南开大学

  Complete program - GERAD

  arXiv Statistics (@arxiv_stats@social.cleverlibre.org) - CleverLibre

  Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex

  Solving Nonconvex-Nonconcave Min-Max Problems exhibit

  一种求解凸-PL极小极大优化问题的随机交替梯度投影算法

  An accelerated minimax algorithm for convex-concave saddle point

  DISSERTATION / DOCTORAL THESIS - u:theses

  The stationarity-gap achieved by the proposed methods for the

  Zeroth-Order Nonconvex Multiagent Optimization Over Networks

  On Nonconvex Decentralized Gradient Descent - arXiv

  Optimization and Control - arXiv

  Computer Science - arXiv

  An accelerated first-order regularized momentum descent ascent

  Adaptive Stochastic Gradient Descent Ascent Algorithm for

  正交更新制胜：迈向加速的自适应极小极大优化 - arXivDaily

  [PDF] Accelerated Primal-dual Scheme for a Class of Stochastic

  Zeroth-Order primal-dual Alternating Projection Gradient Algorithms

  Zi Xu - CatalyzeX

  Optimal Deterministic First-Order Oracle Complexity for Nonconvex

  The Complexity of Nonconvex-Strongly-Concave Minimax

  Nest Your Adaptive Algorithm for Parameter-Agnostic Nonconvex

  The Complexity of Nonconvex-Strongly-Concave Minimax

  GRADIENT DESCENT ASCENT FOR MIN-MAX PROB - OpenReview

  Nonsmooth Composite Nonconvex-Concave Minimax Optimization

  AUC Maximization in the Era of Big Data and AI: A Survey

  Accelerated Zeroth-Order and First-Order Momentum Methods from

  Taoli Zheng - Google 学术搜索




Thoughtsx安看下这个 不要啰嗦

---

## Assistant (2026-11-11 13:29)

老大，报告的结论对我们有利：**没有找到相同或等价的算法**，$O(\epsilon^{-5/2})$ 的单循环方法仍然只有 Zhang–Xu 一篇。这是检索模型的报告，我没有逐篇打开核对。

**对我们有用的三条新信息**

- **ALDER**（arXiv:2611.00691，10-31 提交，Zhang–Zhang–Xu–Dai）：Zhang–Xu 团队已经把他们的方法推广到 ALM。它处理的是带耦合约束的 minimax 问题，乘子用欠松弛更新，强凹下复杂度是 $O(\epsilon^{-7/2})$。它与 B2′ 的问题和速率都不同，但说明这个团队在往 ALM 方向走，我们要尽快成稿。Remark 里必须引用并区分。
- **LPD**（Thekumparampil–He–Oh，AISTATS 2022）：凸、双线性耦合情形下的单循环对偶点列外推，作者把非凸–凹情形列为开放问题。这是对偶外推这条线上最近的前人工作，可以用来写动机。
- **Zhang–Xu 的 Algorithm 1 全文**：报告给出了逐行更新式，确认它每步在预测点和校正点各算一次完整梯度，并带投影和法锥变量。这与我之前的对比一致。

**报告里不能当证据用的部分**

- 第 3.1 节说 B2′ "解答了悬而未决的难题"、交替顺序 "提供隐式预测–校正阻尼"。这是检索模型自己的评价，没有文献依据，不能写进论文。
- 报告自己列了两处盲区：只证渐近收敛或 KŁ 收敛的惯性 ADMM 和线性化 ALM 文献没有穷尽；付费墙内没有预印本的期刊论文读不到。前一类即使有结构相同的算法，也没有 $\epsilon^{-5/2}$ 的复杂度，影响的是"算法结构首次出现"的说法，不影响速率的新意。
- ALDER 的一般凹情形定理它没有读到，"$7/2$" 只对强凹情形成立。

**论文里的表述**

查新结果支持写 "to our knowledge, the first single-loop method with plain alternating gradient steps attaining $O(\epsilon^{-5/2})$"。不要写 "first single-loop $O(\epsilon^{-5/2})$ method"，因为 Zhang–Xu 在先。

报告原文应存入 `notes/progress/`，并把 ALDER、LPD、Ke–Mei–Zhang 三篇补进 `literature.md`。

---

## User (2026-11-11 13:37)

请不要啰嗦 我们目前的算法已经写进去了 你核对一下。 我只想知道就是最原始的nesterov和我们的乘子外推 是一样的对吧？ 不要啰嗦

---

## Assistant (2026-11-11 13:38)

老大，对，乘子这一步就是 Nesterov 强凸情形的常数动量格式（*Introductory Lectures* 第 2.2 节的 Constant Step Scheme III），只是目标函数每步在变。

**对应关系**

- Nesterov 原式：外推系数是 $(1-\sqrt{\mu/L})/(1+\sqrt{\mu/L})$，然后在外推点做步长 $1/L$ 的梯度步。
- 我们的第 4、6 行：强凹模 $\mu=1/s$，步长 $\tau$ 代替 $1/L$，系数变成 $(1-\sqrt{\tau/s})/(1+\sqrt{\tau/s})$，与文件里的写法相等。
- 唯一的区别：梯度取自 $\mathcal{P}_s(\mathbf{x}^{k+1},\cdot\,;\mathbf{z}^k,\mathbf{0})$，这个函数随 $k$ 变。递推形式相同，分析要另做，这就是 G2 的内容。

**核对 [Acceleration.tex](overleaf/sections/Acceleration.tex) 的结果**

四行更新、初值、输出与证明一致。有三处要改：

1. **Input 缺两个步长条件**：证明要求 $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$ 和 $\tau\le\min\{\rho/4,\ 1/(14\gamma G_{\mathcal{A}}^2)\}$。现在只写了 $\rho,\gamma,\tau\gt 0$。这两条放进算法框或留给定理都行，但不能漏。
2. **$\alpha$ 的写法**：文件写 $0\lt\alpha\le\frac{1}{6}\sqrt{\tau/s}$，单步下降成立。但 $\epsilon^{-5/2}$ 需要 $\alpha$ 与 $\sqrt{\tau/s}$ 同阶，定理里要写成 $\alpha=c\sqrt{\tau/s}$，$c\in(0,1/6]$ 固定。
3. **笔误**：第 5 行 "we takes" 应为 "we take"；第 3 行的 `\leavevmode\par` 多余。

---

## User (2026-11-11 13:38)

现在需要干的就这俩事 最本质的 请你写的时候 不要额外加解释和 防御性说法 这个写到记忆里 我让你加什么 你就什么？ 你能理解我吗？

---

## Assistant (2026-11-11 13:39)

老大，理解，已写进记忆：你让我加什么我就加什么，不加额外解释，不加防御性说法。

我理解的两件事是：

1. 族内 $\Omega(\epsilon^{-3})$ 的大步长分支实例，等 GPT Pro 的结果。
2. 把加速这一章写完，即 [Acceleration.tex](overleaf/sections/Acceleration.tex) 的主定理和附录证明。

如果你指的是另外两件，告诉我。

---

## User (2026-11-11 13:40)

先把nesterov的基础更新写进去 不要额外的啰嗦 
再把强凹模 $\mu=1/s$，步长 $\tau$ 代替 $1/L$，系数变成 $(1-\sqrt{\tau/s})/(1+\sqrt{\tau/s})$，与文件里的写法相等。写进去，核心思想就是我们借助nesterov加速 标准的技术

---

## Assistant (2026-11-11 13:41)

老大，已写进 [Acceleration.tex](overleaf/sections/Acceleration.tex)，放在 min–max 式子之后、算法框之前，没有编译。

写入的内容：

```latex
The dual step uses Nesterov's accelerated gradient
method~\cite{nesterov2018lectures}. For maximizing an \(L\)-smooth and
\(\mu\)-strongly concave function \(\phi\), this method reads
\[
    \bar{\bu}^{k}=\bu^k+
    \frac{1-\sqrt{\mu/L}}{1+\sqrt{\mu/L}}(\bu^k-\bu^{k-1}),
    \qquad
    \bu^{k+1}=\bar{\bu}^{k}+\frac1L\nabla\phi(\bar{\bu}^{k}).
\]
The function \(\blmbd\mapsto\mathcal P_s(\bx,\blmbd;\bz,\zero)\) is
\(1/s\)-strongly concave. Taking \(\mu=1/s\) and replacing \(1/L\) by the
dual stepsize \(\tau\) gives the extrapolation coefficient
\[
    \frac{1-\sqrt{\tau/s}}{1+\sqrt{\tau/s}}
    =\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}.
\]
```

`tools/refer.bib` 里原来没有 Nesterov 的书，我加了条目 `nesterov2018lectures`（*Lectures on Convex Optimization*，Springer 2018）。

---

## User (2026-11-11 13:44)

核对 Acceleration.tex 的结果

四行更新、初值、输出与证明一致。有三处要改：

Input 缺两个步长条件：证明要求 $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$ 和 $\tau\le\min\{\rho/4,\ 1/(14\gamma G_{\mathcal{A}}^2)\}$。现在只写了 $\rho,\gamma,\tau\gt 0$。这两条放进算法框或留给定理都行，但不能漏。
$\alpha$ 的写法：文件写 $0\lt\alpha\le\frac{1}{6}\sqrt{\tau/s}$，单步下降成立。但 $\epsilon^{-5/2}$ 需要 $\alpha$ 与 $\sqrt{\tau/s}$ 同阶，定理里要写成 $\alpha=c\sqrt{\tau/s}$，$c\in(0,1/6]$ 固定。
笔误：第 5 行 "we takes" 应为 "we take"；第 3 行的 \leavevmode\par 多余。 我认为参数不需要在算法框细节写出来到底 这个交给我们的 参数结果。

---

## Assistant (2026-11-11 13:46)

老大，对，算法框只列参数、初始化、更新和输出，已按这个改好 [Acceleration.tex](overleaf/sections/Acceleration.tex)：

- **Input 行**改为 `Parameters \(\rho,s,\gamma,\eta,\tau>0\), \(\alpha\in(0,1]\); iteration limit \(K\).`，步长条件全部留给定理。
- "we takes" 改为 "we take"。
- 删掉了 `\leavevmode\par`。

没有编译。

---

## User (2026-11-11 13:46)

主定理与简短解释：陈述复杂度，再说明外推允许更大的原始中心步长；  你觉得呢？

---

## Assistant (2026-11-11 13:46)

老大，同意，这个结构够了，而且"外推允许更大的原始中心步长"正是证明里真正起作用的机制。

**定理**只写三样：

- 参数条件：$\gamma$、$\tau$ 的步长条件，$\eta=\gamma$，$s=c_s/\epsilon$，$\alpha=c\sqrt{\tau/s}$。
- 结论：前 $K$ 个输出里有一个是 $\epsilon$-KKT 点。
- 迭代数：$K=O(\epsilon^{-5/2})$，带显式常数。

**解释**用两句话，各带一个量级对比：

- 固定中心时，不加外推的对偶步每步收缩 $1-\Theta(\tau/s)$，加外推后是 $1-\sqrt{\tau/s}$。
- 因此中心步长可以从 $\Theta(\epsilon)$ 提高到 $\Theta(\sqrt{\epsilon})$，迭代数从 $\epsilon^{-3}$ 降到 $\epsilon^{-5/2}$。

第一句里"不加外推时收缩 $1-\Theta(\tau/s)$"我是从 10-26 的状态表里取的，那里记的是直接计算的结论；写进论文前要对一下它在论文里对应哪个式子。

要我按这个写进 Acceleration.tex 吗？

---

## User (2026-11-11 13:47)

2. 我们目前的我认为有一个核心的动机是把-3拆解一下？    我记得我们之前有一个结果

---

## Assistant (2026-11-11 13:48)

老大，记得，是这个结果：把 Li '26 的界用对偶条件数 $\kappa=\ell s$ 改写，Perturbed Smoothed GDA 的复杂度是 $O(\kappa\,\epsilon^{-2})$。这个 $\kappa$ 形式是我们自己的改写，Li 的原文没有这样写。

**拆解**

$$
\epsilon^{-3}=\kappa\cdot\epsilon^{-2},\qquad \kappa=\ell s=\Theta(\epsilon^{-1})
$$

- $\epsilon^{-2}$ 是非凸问题找驻点的基本代价。
- $\kappa$ 是对偶正则化子问题的条件数：强凹模是 $1/s$，取 $s=c_s/\epsilon$ 后 $\kappa\sim\epsilon^{-1}$。

**动机**

Nesterov 加速的标准效果是把 $\kappa$ 换成 $\sqrt{\kappa}$，于是

$$
\sqrt{\kappa}\cdot\epsilon^{-2}=\epsilon^{-5/2}
$$

我们的定理正好是这个形式，迭代数为

$$
K\ge 4C_R^2\Delta_{\mathcal{W}}\sqrt{s/\tau}\;\epsilon^{-2}
$$

其中 $\sqrt{s/\tau}$ 就是 $\sqrt{\kappa}$。

**论文里已有的两个支撑**

- 上界一侧：`thm:upper-beta0` 取 $\alpha=\kappa_0/(\ell s)$，中心步长与 $1/\kappa$ 同阶。
- 下界一侧：`lem:plateau` 给出 $T\gt\Delta/(16\gamma\alpha\epsilon^2)$，即 $\alpha^{-1}\cdot\epsilon^{-2}$。

所以这一章的动机可以写成：族内的 $\epsilon^{-3}$ 是 $\kappa\epsilon^{-2}$，对偶外推把它变成 $\sqrt{\kappa}\epsilon^{-2}$。

---

## User (2026-11-11 13:48)

结论：前 $K$ 个输出里有一个是 $\epsilon$-KKT 点。 我们现在是做不出来last iterate? 就是在nesterov我们的5的项目，我还关注lasriterate的速度。 或许可以变成我们的推论？ 不要啰嗦

---

## Assistant (2026-11-11 13:48)

老大，非凸的整体算法现在做不出 last-iterate 的速率，但有两个可以直接写成推论的结果。

**做不出的原因**：证明只给出求和界

$$
\sum_{k\lt K}\varsigma M_k\le\Delta_{\mathcal{W}}
$$

$M_k$ 本身不单调，所以只能取最小的那一步。

**推论一：不达标的迭代至多 $O(\epsilon^{-5/2})$ 个。** 残差大于 $\epsilon$ 的每一步都满足 $M_k\gt\epsilon^2/(4C_R^2)$，由求和界，这样的步数不超过

$$
4C_R^2\Delta_{\mathcal{W}}\sqrt{c_s/\tau}\;\epsilon^{-5/2}
$$

同时 $M_k\to 0$，所以从某一步起所有输出都是 $\epsilon$-KKT 点。这比"前 $K$ 个里有一个"强，但没有给出最后一步达标的时刻。这条是我刚从求和界推的，写入前要对一下 Corollary G3.6 的常数。

**推论二：固定中心时是 last-iterate 线性收敛。** 取 $\alpha=0$，Theorem G2.4 给出

$$
\mathcal{E}_k\le\left(1-\sqrt{\tau/s}\right)^k\mathcal{E}_0
$$

这是对强凸–强凹子问题的 last-iterate 速率，条件数依赖是 $\sqrt{s/\tau}$，已证。

真正的 last-iterate 速率需要额外的结构，例如 KŁ 条件，目前没有证明。

---

## User (2026-11-11 13:48)

就是我记得之前把-3写成-2乘-q这种。

---

## Assistant (2026-11-11 13:49)

老大，仓库和记忆里没有检索到带 $q$ 的写法。记录下来的是条件数形式：$\epsilon^{-3}=\kappa\cdot\epsilon^{-2}$，其中 $\kappa=\ell s$。

你记的形式可以这样对上，把 $\kappa$ 的幂次记作 $q$：

$$
K=\Theta\left(\kappa^{q}\,\epsilon^{-2}\right)=\Theta\left(\epsilon^{-(2+q)}\right),\qquad \kappa=\Theta(\epsilon^{-1})
$$

| 方法 | $q$ | 复杂度 |
|---|---|---|
| LRALM，$\beta=0$，无外推 | $1$ | $\epsilon^{-3}$ |
| 加对偶 Nesterov 外推 | $1/2$ | $\epsilon^{-5/2}$ |

$\epsilon^{-2}$ 来自外层势函数的下降，$\epsilon^{-q}$ 来自对偶子问题的条件数。$q=1/2$ 是 Nesterov 加速对条件数依赖的标准改进。

如果你记得的是另一份材料里的式子，告诉我大概在哪次讨论里，我再找。

---

## User (2026-11-11 13:54)

大概讲一下-3那个拆解 gemini我们也讨论了。 **结论**

单循环 ALM 的总复杂度统一拆解为“**外层非凸驻点步数 $\times$ 内层追踪代价**”：

$$
K \asymp \epsilon^{-2} \times \frac{1}{\alpha} = \epsilon^{-2} \times (\epsilon^{-1})^q
$$

**锚定、动量、外推三者各司其职：锚定（Tikhonov 对偶正则）把指数 $q$ 从 $2$ 降到 $1$（$\epsilon^{-4}\to\epsilon^{-3}$）；动量把指数 $q$ 从 $1$ 降到 $1/2$（$\epsilon^{-3}\to\epsilon^{-2.5}$）；外推负责压制原始–对偶耦合旋转，保证加动量后系统不发散。**

---

### 一、三种加速技巧的极简对照表

| 技巧 | 作用对象 | 核心功能 | 解决的阶数跃迁 |
| :--- | :--- | :--- | :--- |
| **1. 锚定 / Tikhonov 正则**（$-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$） | 无曲率单调算子（$\mu_\lambda=0\to 1/s$） | 给平直的对偶方向注入 $1/s\sim\epsilon$ 的曲率，把单调残差代价从 $\epsilon^{-2}$ 压到条件数 $s\sim\epsilon^{-1}$ | **$q: 2 \to 1$**（总复杂度 **$\epsilon^{-4} \to \epsilon^{-3}$**，我们现稿已完成） |
| **2. 惯性动量**（Nesterov / 梯度累加器 $\mathbf{v}^k$） | 病态强凹单块（条件数 $\kappa_\lambda = Ls \sim \epsilon^{-1}$） | 在曲率 $1/s$ 的慢方向上累加约 $\sqrt{s}$ 步同向梯度，把条件数 $s$ 开根号变成 $\sqrt{s}\sim\epsilon^{-1/2}$ | **$q: 1 \to 1/2$**（总复杂度 **$\epsilon^{-3} \to \epsilon^{-2.5}$**） |
| **3. 算子外推**（EG / OGDA 梯度差 / PDHG 耦合外推） | 跨块反对称耦合项 $\langle\boldsymbol{\lambda},\mathcal{A}(\mathbf{x})\rangle$ | 用预测步或一步历史差分提供超前相移，抵消原始–对偶旋转模态的发散 | **本身不降 $q$**（单独用仍停在 $\epsilon^{-3}$），但**是动量能稳定工作的必要护栏** |

---

### 二、三句话记住全部逻辑

1. **为什么锚定到 $\epsilon^{-3}$ 就停了**：锚定（或加 $1/s$ 正则）只能把无曲率的 $\epsilon^{-2}$ 变成曲率倒数 $s\sim\epsilon^{-1}$，无法把已有的条件数 $s$ 开根号。
2. **为什么从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$ 必须靠对偶动量（或直接放大 $\rho\sim\epsilon^{-1/2}$）**：内层原始块有近端项 $\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}^k\rVert^2$ 托底，条件数 $\kappa_x=\Theta(1)$ 不病态；只有对偶块条件数 $\kappa_\lambda\sim s\sim\epsilon^{-1}$ 病态，必须用对偶动量把内层步数从 $s$ 压到 $\sqrt{s}$，中心步长才能放大到 $\alpha\sim\epsilon^{1/2}$。
3. **为什么动量和外推必须一起上**：极小化问题没有旋转，单加 Nesterov 动量即可；鞍点问题有原始–对偶耦合旋转，单加动量会放大振荡，必须配外推（Zhang–Xu 用双步 EG，单步化简可用 OGDA 梯度差或 PDHG 耦合外推）来稳住耦合项。

---

**核心要义：锚定（Tikhonov $1/s$）负责 $\epsilon^{-4}\to\epsilon^{-3}$，对偶动量负责把条件数 $s$ 开根号实现 $\epsilon^{-3}\to\epsilon^{-2.5}$，算子外推负责在加动量时压住原始–对偶耦合振荡。** 就是这个-3不知道咋弄的  我只知道算法是单循环

---

## Assistant (2026-11-11 13:54)

老大，$\epsilon^{-3}$ 是三个不等式相乘得到的，每一个在论文里都有对应的式子。

**第一步：外层给出 $\epsilon^{-2}/\alpha$。** 势函数每步下降

$$
\Psi^k-\Psi^{k+1}\ge\frac{\alpha}{8\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2
$$

求和后右端总量不超过初始间隙。KKT 残差里含 $\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert/\gamma$，要它小于 $\epsilon$，需要

$$
K\gtrsim\frac{\Delta}{\alpha\,\epsilon^{2}}
$$

平台引理的下界 $T\gt\Delta/(16\gamma\alpha\epsilon^2)$ 说明这个量级是紧的。

**第二步：单循环迫使 $\alpha\lesssim 1/s$。** 每次迭代只对子问题

$$
\min_{\mathbf{x}}\max_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z}^k,\mathbf{0})
$$

做一步梯度下降–上升。子问题的对偶强凹模是 $1/s$，一步只把迭代点到鞍点的距离缩小 $1-\Theta(\tau/s)$。中心每步移动 $\alpha\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert$，鞍点随之移动。迭代点要跟得上鞍点，中心的移动必须慢于这个收缩，所以

$$
\alpha\lesssim\frac{1}{\ell s}
$$

这就是 `thm:upper-beta0` 里 $\alpha=\kappa/(\ell s)$ 的来源。单循环的含义就在这里：内层不求解到收敛，改为把中心放慢 $1/\alpha$ 倍。

**第三步：精度迫使 $s\gtrsim 1/\epsilon$。** 对偶中心固定在 $\mathbf{0}$ 时，输出残差里有偏差 $L_h/s$，要它小于 $\epsilon$。

**合起来：**

$$
K\asymp\epsilon^{-2}\cdot\frac{1}{\alpha}\asymp\epsilon^{-2}\cdot s\asymp\epsilon^{-3}
$$

B2′ 只改第二步：Nesterov 外推把收缩变成 $1-\sqrt{\tau/s}$，于是 $\alpha\sim\sqrt{\tau/s}$，得到 $\epsilon^{-2}\cdot\sqrt{s}=\epsilon^{-5/2}$。

Gemini 表里第三行和"动量和外推必须一起上"与我们的证明不符：B2′ 只有对偶动量和交替梯度步，没有 EG 或 OGDA，证明已经闭合。

---

## User (2026-11-11 13:55)

但是这个势函数 似乎我们都没用啊  你确定我们目前

---

## Assistant (2026-11-11 13:56)

老大，你说得对，上一条第一步的 $\Psi^k$ 写得有问题：论文里没有自己推过这个势函数的下降。

**论文里的 $\epsilon^{-3}$ 上界实际怎么来的**（附录 C，`thm:upper-beta0`）：

- Step 1 把 LRALM（$\beta=0$）逐项对应到 Li26 的 Perturbed Smoothed GDA。
- Step 5 直接引用 Li26 的 Theorem 3.3(i) 得到速率。
- 势函数只以初始间隙 $\Delta_{\Psi_2}=v_0-2d_0+2p_0-\inf\Phi_s$ 的形式出现在 Step 4。下降不等式在 Li26 的 Section 4.2 里，我们没有重写。

上一条里我写的系数 $\alpha/(8\gamma)$ 取自 10-26 那份 GPT 对话对 Li26 Lemmas 4.4–4.5 的转述，不是论文中的式子。

**所以三步拆解里各步的依据是**：

| 步骤 | 依据 | 是否我们自己的证明 |
|---|---|---|
| $K\gtrsim\Delta/(\alpha\epsilon^2)$ | 上界引用 Li26；下界是 `lem:plateau` | 下界是，上界引用 |
| $\alpha\lesssim 1/(\ell s)$ | Li26 的步长条件，对应 `eq:beta0-stepsizes` | 引用 |
| $s\gtrsim 1/\epsilon$ | 附录 C Step 6 的偏差项 $L_h/s$ | 是 |

**自己用势函数做证明的只有 B2′**：$\mathcal{W}_k=p_s(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$，在笔记 G3 里，还没写进论文。

拆解 $\epsilon^{-3}=\epsilon^{-2}\cdot s$ 本身成立，但论文里写这段动机时，上界那一半要标明出自 Li26。

---

## User (2026-11-11 13:57)

外层我也看不懂 最简单干净的语言呢 数学优化

---

## Assistant (2026-11-11 13:57)

老大，外层就是**对 Moreau 包络做梯度下降，步长是 $\alpha\gamma$**。

**对象。** 记罚函数 $\Phi(\mathbf{x})=\mathcal{D}_{\rho+s}(\mathbf{x},\mathbf{0})$，它的 Moreau 包络是

$$
p(\mathbf{z})=\min_{\mathbf{x}}\left\{\Phi(\mathbf{x})+\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}\rVert^2\right\}
$$

记极小点为 $\mathbf{x}^\star(\mathbf{z})$。包络的梯度是

$$
\nabla p(\mathbf{z})=\frac{\mathbf{z}-\mathbf{x}^\star(\mathbf{z})}{\gamma}
$$

$\lVert\nabla p(\mathbf{z})\rVert\le\epsilon$ 就是近似驻点的判据。

**中心更新是梯度步。** 假设 $\mathbf{x}^{k+1}$ 恰好等于 $\mathbf{x}^\star(\mathbf{z}^k)$，则

$$
\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha\left(\mathbf{x}^\star(\mathbf{z}^k)-\mathbf{z}^k\right)=\mathbf{z}^k-\alpha\gamma\,\nabla p(\mathbf{z}^k)
$$

**梯度下降的标准估计。** $p$ 是光滑的，步长为 $\alpha\gamma$ 的梯度下降满足

$$
p(\mathbf{z}^{k+1})\le p(\mathbf{z}^k)-\frac{\alpha\gamma}{2}\lVert\nabla p(\mathbf{z}^k)\rVert^2
$$

对 $k$ 求和，得到

$$
\min_{k\lt K}\lVert\nabla p(\mathbf{z}^k)\rVert^2\le\frac{2\Delta}{\alpha\gamma K}
$$

要右端小于 $\epsilon^2$，需要

$$
K\ge\frac{2\Delta}{\alpha\gamma\,\epsilon^2}
$$

这就是 $\epsilon^{-2}\cdot\alpha^{-1}$：$\epsilon^{-2}$ 是光滑非凸函数上梯度下降的标准迭代数，$\alpha^{-1}$ 来自步长是 $\alpha\gamma$。

**内层的作用。** 实际的 $\mathbf{x}^{k+1}$ 只是 $\mathbf{x}^\star(\mathbf{z}^k)$ 的近似，由一步原始–对偶梯度步给出。$\alpha$ 越小，$\mathbf{z}^k$ 动得越慢，这个近似越准。内层收缩越快，允许的 $\alpha$ 越大：无外推时 $\alpha\sim 1/s$，加 Nesterov 外推后 $\alpha\sim\sqrt{\tau/s}$。

---

## User (2026-11-11 13:58)

这种分析 我比如写成-2*-这种25年 及其之前  有没有最准确可以照着模仿的文章？

---

## Assistant (2026-11-11 13:59)

老大，最适合照着写的是 **Lin, Jin, Jordan, "Near-Optimal Algorithms for Minimax Optimization", COLT 2020**。下面对它的描述是凭记忆写的，定理编号和对数因子请对照原文。

**它的写法正好是 $\epsilon^{-2}\times$ 条件数因子**

- **非凸–强凹**：外层是不精确近端点法，迭代数 $O(\epsilon^{-2})$；每次外层调用一个加速求解器，代价 $\tilde{O}(\sqrt{\kappa})$。总复杂度写成 $\tilde{O}(\sqrt{\kappa}\,\epsilon^{-2})$。
- **非凸–凹**：给对偶变量加一个量级为 $\epsilon$ 的二次正则，问题变成 $\kappa\sim\epsilon^{-1}$ 的非凸–强凹问题，代入上式得到 $\tilde{O}(\epsilon^{-5/2})$。

这与我们的三步完全对应：外层 $\epsilon^{-2}$，对偶正则使 $\kappa\sim\epsilon^{-1}$，加速把 $\kappa$ 变成 $\sqrt{\kappa}$。

**与我们的差别**：它是多层循环，$\sqrt{\kappa}$ 是内层求解器的迭代数。我们是单循环，$\sqrt{\kappa}$ 体现在中心步长 $\alpha\sim 1/\sqrt{\kappa}$ 上。照它的叙述顺序写，把"内层迭代数"换成"中心步长的倒数"即可。

`tools/refer.bib` 里目前只有同一组作者的 `lin2020gradient`（GDA 那篇），这一篇需要新增条目。

---

## User (2026-11-11 14:16)

https://proceedings.mlr.press/v125/lin20a/lin20a.pdf 我们和他们的区别是什么 我去

---

## Assistant (2026-11-11 14:17)

老大，我读了原文第 5 节（Theorem 12、Corollary 13、Algorithm 5）。分解的思路相同，区别在算法结构、问题类和结论形式。

| | Lin–Jin–Jordan | 我们的 B2′ |
|---|---|---|
| 循环结构 | 多层：外层近端点法，内层调用 Maximin-AG2，最后再跑一次 AGD | 单循环，每步一次原始梯度步、一次对偶梯度步 |
| $\epsilon^{-2}$ 的来源 | 外层近端点迭代数 $T$ | 势函数下降求和 |
| $\sqrt{\kappa}$ 的来源 | 每次外层迭代内层的梯度次数 | 中心步长的倒数，$\alpha\sim 1/\sqrt{\kappa}$ |
| 加速作用在哪里 | 内层求解器对两块都加速 | 只对乘子做一次 Nesterov 外推 |
| 对偶正则 | $-\frac{\epsilon}{4D_y}\lVert y-y_0\rVert^2$ | $-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$，$s=c_s/\epsilon$ |
| 对偶域 | 有界，复杂度含 $D_y$ | 乘子无界，有界性由证明给出 |
| 复杂度 | $\tilde{O}(\epsilon^{-5/2})$，带 $\log^2$ 因子 | $O(\epsilon^{-5/2})$，无对数因子 |
| 输出 | 随机抽一个外层迭代点，以至少 $2/3$ 的概率成立 | 确定性，前 $K$ 个输出里有一个达标 |
| 问题 | 光滑非凸–凹 minimax | $f+h\circ\mathcal{A}$ 的复合问题，$\epsilon$-KKT |

**可以照着模仿的部分**是第 5 节的叙述顺序：

1. 先写强凹情形：外层 $\tilde{O}(\epsilon^{-2})$ 次迭代，内层 $\tilde{O}(\sqrt{\kappa_y})$，相乘得到 $\tilde{O}(\sqrt{\kappa_y}\,\epsilon^{-2})$。原文在 Theorem 12 后面用一段话把这两个因子分开解释。
2. 再写凹情形：加对偶正则，说明梯度只改变 $O(\epsilon)$，于是 $\kappa_y=\Theta(\epsilon^{-1})$，代入得到 $\epsilon^{-5/2}$。

原文还有一句可以引用：外层不做加速，因为梯度下降在光滑非凸函数上找驻点已经是最优的。这正好解释了我们为什么只在对偶块加外推。

PDF 和提取的文本在 [temp/lin20a/](temp/lin20a/)。

---

## User (2026-11-11 14:23)

Analyzed AGENTS.md:L1-79
Analyzed Acceleration.tex:L1-56

**结论与提纲**

**在固定罚参数 $\rho=\Theta(1)$、对偶中心固定于零（$\beta=0$）的设定下，单循环算法复杂度 $\Theta(\epsilon^{-3})$ 严格拆解为“外层非凸驻点步数 $\epsilon^{-2}$”与“内层鞍点跟踪代价 $\frac{1}{\alpha}\asymp\epsilon^{-1}$”的乘积：**

$$
K \asymp \frac{\Delta}{\alpha\epsilon^2} = \epsilon^{-2} \times \frac{1}{\alpha} \asymp \epsilon^{-2} \times \epsilon^{-1} = \epsilon^{-3}
$$

下文按“外层 $\epsilon^{-2}$ 的来源 $\to$ 参数 $s\asymp\epsilon^{-1}$ 的来源 $\to$ 内层 $\frac{1}{\alpha}\asymp\epsilon^{-1}$ 的来源”三步说明该拆解。

---

### 一、三步推导链

1. **外层驻点条件给出因子 $\epsilon^{-2}$（不可降低）**
   中心更新 $\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha(\mathbf{x}^{k+1}-\mathbf{z}^k)$ 等价于在正则化包络函数上以步长 $\alpha$ 执行近似梯度下降（包络函数是对内层鞍点变量取极值后得到的关于中心 $\mathbf{z}$ 的光滑非凸函数）。因为当包络梯度范数大于 $\epsilon$ 时，中心每移动一步至多使函数值下降 $\Theta(\alpha\epsilon^2)$，所以在初始函数值间隙 $\Delta$ 下，达到 $\epsilon$-驻点至少需要 $K \gtrsim \frac{\Delta}{\alpha\epsilon^2}$ 步（对应论文的平台引理）。由于问题类包含无约束光滑非凸优化，受一阶复杂度下界 $\Omega(\epsilon^{-2})$ 限制，因子 $\epsilon^{-2}$ 无法改进。

2. **可行性精度要求迫使对偶正则尺度取 $s \asymp \epsilon^{-1}$**
   固定中心 $\mathbf{z}^k$ 时，算法在内层求解正则化鞍点函数 $\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z}^k,\mathbf{0})=\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})+\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}^k\rVert^2-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$。对该函数关于 $\boldsymbol{\lambda}$ 取极大值后，有效罚参数为 $\rho+s$（有效罚参数是决定子问题精确解处约束违反量上界的组合参数），稳态可行性偏差上界为 $\frac{L_h}{\rho+s}$。因为罚参数固定为 $\rho=\Theta(1)$，要使可行性残差不超过 $\epsilon$，因此必须取 $s = \Theta(\epsilon^{-1})$。

3. **内层对偶慢收缩限制 $\alpha \lesssim \epsilon$，给出因子 $\epsilon^{-1}$（可加速项）**
   当 $\frac{1}{\gamma}>\ell$ 时，固定中心后的 $\mathcal{P}_s$ 是强凸–强凹函数：原始块强凸模数为 $\mu_x=\frac{1}{\gamma}-\ell=\Theta(1)$，条件数 $\kappa_x=\Theta(1)$；对偶块强凹模数为 $\mu_\lambda=\frac{1}{s}=\Theta(\epsilon)$，光滑常数为 $\frac{1}{\rho}=\Theta(1)$，条件数 $\kappa_\lambda \asymp \frac{s}{\rho}=\Theta(\epsilon^{-1})$。单步梯度下降–上升（GDA）的内层单步收缩率由条件数更大的对偶块决定，即 $\delta_{\mathrm{inner}}=\Theta(\kappa_\lambda^{-1})=\Theta(s^{-1})=\Theta(\epsilon)$。为了使迭代点稳定跟踪移动的中心 $\mathbf{z}^k$，中心步长 $\alpha$ 不能超过内层单步收缩率，因此 $\alpha \lesssim \delta_{\mathrm{inner}} \asymp \epsilon$。将 $\alpha\asymp\epsilon$ 代入 $K\asymp\frac{\Delta}{\alpha\epsilon^2}$，从而得到 $K=\Theta(\epsilon^{-3})$。

---

### 二、拆解汇总表

| 拆解项 | 量级 | 决定该项的数学机制 | 能否改进 |
| :--- | :--- | :--- | :--- |
| **外层基准因子** | $\epsilon^{-2}$ | 光滑非凸包络寻找 $\epsilon$-驻点的最小有效下降量 | **不能**（受一阶非凸下界 $\Omega(\epsilon^{-2})$ 约束） |
| **对偶条件数 $s$** | $\epsilon^{-1}$ | 固定 $\rho=\Theta(1)$ 时，消除可行性偏差 $\frac{L_h}{\rho+s}\le\epsilon$ 所需的最小尺度 | **不能**（若 $\rho+s\ll\epsilon^{-1}$，复杂度退回 $\Omega(\epsilon^{-4})$） |
| **内层跟踪代价 $\frac{1}{\alpha}$** | $s^1 \asymp \epsilon^{-1}$ | 单步 GDA 在 $1/s$-强凹对偶块上的收缩率 $\delta_{\mathrm{inner}}\asymp s^{-1}$，限制 $\alpha\lesssim s^{-1}$ | **能改进至 $s^{1/2}\asymp\epsilon^{-1/2}$**（引入加速机制把内层收缩率提至 $s^{-1/2}$，即可令 $\alpha\asymp\epsilon^{1/2}$，总复杂度降至 $\epsilon^{-2.5}$） |

---

**核心要义：$\Theta(\epsilon^{-3})$ 由不可降的外层非凸驻点代价 $\epsilon^{-2}$ 与可加速的内层对偶跟踪代价 $\frac{1}{\alpha}\asymp s\asymp\epsilon^{-1}$ 相乘得到；一切突破 $\epsilon^{-3}$ 的加速方案，本质上都是把内层跟踪代价从 $s$ 压低到 $\sqrt{s}\asymp\epsilon^{-1/2}$。** 结合这个 我现在在想 怎么把独特的见解写入我们的文章里？

---

## Assistant (2026-11-11 14:23)

老大，我的建议是把它写成加速这一章的开头一段，用一个等式加三句话，每句对应论文里已有的一个结果，再用一句话说明外推只改变第三项。

**放在哪里**

- **主要位置**：[Acceleration.tex](overleaf/sections/Acceleration.tex) 开头，在现有的 min–max 式子之前。读者先看到 $\epsilon^{-3}$ 是哪三项相乘，再看到 Nesterov 那段，就知道外推针对的是哪一项。
- **次要位置**：Introduction 的贡献里加一句，指向这一段。

**每句话的依据**

| 内容 | 论文里的依据 | 能写到什么程度 |
|---|---|---|
| $K\asymp\Delta/(\alpha\epsilon^2)$ | 下界 `lem:plateau`，上界 `thm:upper-beta0` | 可以写成两侧都成立 |
| $s\gtrsim\epsilon^{-1}$ | `thm:lower-bound`：$\epsilon(\rho+s)\le c_1$ 时是 $\Omega(\epsilon^{-4})$ | 可以写"必须" |
| $\alpha\lesssim 1/s$ | 目前只有 `eq:beta0-stepsizes` 的充分条件 | 大步长分支证出来之前只能写 "the analysis requires" |

**Gemini 那段里不能照搬的两处**

- "一切突破 $\epsilon^{-3}$ 的加速方案本质上都是把 $s$ 压到 $\sqrt{s}$"：没有证明，不写。
- "受一阶下界限制，$\epsilon^{-2}$ 不能改进"：对 $\mathcal{C}_\theta$ 由 `lem:plateau` 给出；对一般一阶方法要引 Carmon 等人的下界，并说明问题类包含 $\mathcal{A}\equiv 0$ 的光滑非凸情形。

**草稿**

```latex
For \(\beta=0\), the \(\epsilon^{-3}\) complexity of LRALM is the product of
two factors,
\[
    K\asymp\frac{\Delta}{\alpha\epsilon^{2}}
    =\epsilon^{-2}\cdot\frac1\alpha .
\]
The factor \(\epsilon^{-2}\) is the number of steps needed to drive the
center \(\bz^k\) to an \(\epsilon\)-stationary point; Lemma~\ref{lem:plateau}
shows that it cannot be reduced for any \(\alpha\). The factor \(1/\alpha\)
is the cost of tracking the saddle point of
\(\mathcal P_s(\cdot,\cdot;\bz^k,\zero)\) with one gradient
descent--ascent step per iteration. This function is \(1/s\)-strongly
concave in \(\blmbd\), a gradient ascent step contracts at rate
\(1-\Theta(\tau/s)\), and Theorem~\ref{thm:upper-beta0} takes
\(\alpha=\Theta(1/s)\). Since Theorem~\ref{thm:lower-bound} forces
\(s=\Omega(\epsilon^{-1})\), we obtain \(1/\alpha=\Theta(\epsilon^{-1})\).
Dual extrapolation changes only the second factor: the contraction rate
becomes \(1-\sqrt{\tau/s}\), which allows \(\alpha=\Theta(\sqrt{\tau/s})\)
and gives \(K=O(\epsilon^{-5/2})\).
```

要我把这段写进文件吗？

---

## User (2026-11-11 14:25)

但是我并不知道你这个思路是怎么来的 比如我们可以形式化写成一个定理或者几个命题（最多不超过三个）就像上面看到的 25年及其之前的工作

---

## Assistant (2026-11-11 14:25)

老大，可以写成三个命题加一个主定理，结构对应 Lin–Jin–Jordan 的 Theorem 12：他们是"外层迭代数 × 内层求解代价"，我们是"外层下降 × 内层收缩 × 两者的耦合条件"。三个命题都来自 B2′ 的证明笔记，我上面讲的拆解就是把这三步的结论连起来读。

记 $p(\mathbf{z})$ 为包络函数，$\mathbf{x}^\star(\mathbf{z})$ 为子问题鞍点的原始分量，$\mathcal{E}_k$ 为内层能量。

## 命题 1：中心步是包络函数上的不精确梯度步

**条件**：$\alpha\in[0,1]$，$\mathbf{x}^{k+1}$ 任意。

**结论**：

$$
p(\mathbf{z}^{k+1})\le p(\mathbf{z}^k)-\frac{\alpha(1-\alpha)}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2+\frac{\alpha}{2\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^\star(\mathbf{z}^k)\rVert^2
$$

**含义**：第二项给出 $\epsilon^{-2}/\alpha$；第三项是跟踪误差，要由内层控制。

**来源**：Lemma G3.3，论文里已有同一个式子 `eq:z-step-p`。

## 命题 2：固定中心时内层能量线性收缩

**条件**：步长条件 (H)，中心固定，外推系数为 $(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})$。

**结论**：记 $\delta=\sqrt{\tau/s}$，则

$$
\mathcal{E}_{k+1}\le(1-\delta)\,\mathcal{E}_k-\frac{\delta\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}^\star(\mathbf{z})\rVert^2
$$

**含义**：这是 Nesterov 加速的收缩率，对应条件数 $s/\tau$ 的平方根。

**来源**：Theorem G2.4。

## 命题 3：中心步长不超过内层收缩率时，总势函数下降

**条件**：命题 2 的不等式以某个 $\delta\in(0,1/2]$ 成立，$\alpha=c\,\delta$，$c\le 1/6$。

**结论**：$\mathcal{W}_k=p(\mathbf{z}^k)+\frac{1}{2}\mathcal{E}_k$ 满足

$$
\mathcal{W}_{k+1}\le\mathcal{W}_k-\frac{\alpha}{5\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{z}^k\rVert^2-\frac{\delta}{4}\mathcal{E}_k
$$

**含义**：这是单循环的核心。内层不需要求解到收敛，只需要 $\alpha\lesssim\delta$。

**来源**：Theorem G3.4 与 Lemma G3.2。笔记里只对 $\delta=\sqrt{\tau/s}$ 写了证明；证明只用到命题 2 的不等式和 $\delta\le 1/2$，写成一般的 $\delta$ 是我的整理，写入前要逐行核对一遍。

## 主定理：三者合并

对命题 3 求和，再取 $s=c_s/\epsilon$：

$$
K=O\left(\frac{\Delta_{\mathcal{W}}}{\delta\,\epsilon^{2}}\right)=O\left(\sqrt{s/\tau}\;\epsilon^{-2}\right)=O\left(\epsilon^{-5/2}\right)
$$

**来源**：Corollary G3.6。

## 与 $\epsilon^{-3}$ 的关系

定理后面加一个 Remark，写两点：

- **下界**：`lem:plateau` 给出 $T\gt\Delta/(16\gamma\alpha\epsilon^2)$，说明命题 1 里的 $\epsilon^{-2}/\alpha$ 对整个族是紧的。
- **不加外推**：`thm:upper-beta0` 取 $\alpha=\Theta(1/s)$，得到 $\epsilon^{-2}\cdot s=\epsilon^{-3}$。这个结果是引用 Li26 得到的。我们没有为不加外推的情形单独证明命题 2 的收缩不等式，所以 Remark 里只对比 $\alpha$ 的量级，不写"收缩率为 $1-\Theta(\tau/s)$"。

这样写的好处是：读者从命题 3 直接看到 $\alpha$ 与 $\delta$ 的关系，$\epsilon^{-3}$ 到 $\epsilon^{-5/2}$ 的差别只在 $\delta$ 从 $\tau/s$ 变成 $\sqrt{\tau/s}$。

---

## User (2026-11-11 14:26)

我的意思是在这个-2.5之前怎么支撑我们的考虑加速的 命题

---

## Assistant (2026-11-11 14:27)

老大，明白了：要的是在 $\epsilon^{-5/2}$ 之前、针对不加外推的族 $\mathcal{C}_\theta$ 的命题，用来说明为什么要加速。可以写成下面三个，其中两个已经在论文里，第三个就是等 GPT Pro 的那个实例。

## 命题 1：复杂度至少是 $\epsilon^{-2}/\alpha$

**条件**：任意 $\theta$，任意 $(\alpha,\beta)\in(0,1]\times[0,1]$，$\epsilon$ 充分小。

**结论**：

$$
\sup_{I\in\mathcal{I}(\mathbf{C}_0,\Delta)}T^{\mathrm{KKT}}_\epsilon(\theta,\alpha,\beta;I)\gt\frac{\Delta}{16\gamma\,\alpha\,\epsilon^{2}}
$$

**状态**：已证，就是 `lem:plateau`。它对 $s$ 的大小没有要求。

## 命题 2：$\alpha=\Theta(1/s)$ 时这个下界可达

**条件**：$\beta=0$，$s=c_s/\epsilon$，$\alpha=\kappa/(\ell s)$，步长满足 `eq:beta0-stepsizes`。

**结论**：

$$
\sup_{I}T^{\mathrm{KKT}}_\epsilon(\theta,\alpha,0;I)\le\frac{C}{\alpha\,\epsilon^{2}}=O(\epsilon^{-3})
$$

**状态**：已证，就是 `thm:upper-beta0`。现在的定理只写了 $O(\epsilon^{-3})$，要改写成 $C/(\alpha\epsilon^2)$ 的形式，需要把常数里对 $\alpha$ 的依赖显式写出来。10-26 那份换算给出的常数含 $8r/\alpha$ 这一项，形式上支持这种写法，写入前要核对。

## 命题 3：$\alpha$ 超过 $\tau/s$ 的常数倍时不收敛

**条件**：$s=c_s/\epsilon$，$\beta\in[0,1]$，$\alpha\gt B\,\tau/s$，$B$ 与 $\epsilon$ 无关。

**结论**：存在 $I\in\mathcal{I}(\mathbf{C}_0,\Delta)$，使所有输出的残差都大于 $\epsilon$。

**状态**：未证。这正是大步长分支。提纲里的条件 $d/\alpha\le\delta$（$d=\tau/s$）就是 $\alpha\ge\tau/(\delta s)$，所以阈值可以用 $\tau/s$ 来表述。提纲里还有第二个阈值 $\alpha\gt 2\epsilon/c_{\mathrm{r}}$，在 $s=c_s/\epsilon$ 下两者同阶。

## 三个命题合起来说明什么

$$
T^{\mathrm{KKT}}_\epsilon\asymp\frac{1}{\alpha\,\epsilon^{2}},\qquad \alpha\lesssim\frac{\tau}{s}
$$

- 命题 1 和 2：族内的复杂度由 $\alpha$ 一个量决定，形式是 $\epsilon^{-2}\cdot\alpha^{-1}$。
- 命题 3：族内 $\alpha$ 的上限是 $\tau/s$ 的常数倍。$\tau/s$ 是对偶梯度步的步长乘以强凹模，即条件数的倒数。
- 结论：族内最好是 $\epsilon^{-2}\cdot s/\tau=\Theta(\epsilon^{-3})$。要更快，只能提高 $\alpha$ 的上限，也就是改对偶步。Nesterov 外推把上限从 $\tau/s$ 变成 $\sqrt{\tau/s}$。

这样加速一章的定理就可以直接写成"$\alpha=c\sqrt{\tau/s}$ 时 $K=O(\epsilon^{-2}/\alpha)$"，与命题 1、2 同一个形式。

命题 3 证出来之前，这一段可以先用命题 1、2 写，第三条写成 "the analysis of Theorem~\ref{thm:upper-beta0} requires $\alpha=O(1/s)$"。

---

## User (2026-11-11 14:28)

就是我的意思是 怎么**结论**

单循环 ALM 的总复杂度统一拆解为“**外层非凸驻点步数 $\times$ 内层追踪代价**”：

$$
K \asymp \epsilon^{-2} \times \frac{1}{\alpha} = \epsilon^{-2} \times (\epsilon^{-1})^q
$$

**锚定、动量、外推三者各司其职：锚定（Tikhonov 对偶正则）把指数 $q$ 从 $2$ 降到 $1$（$\epsilon^{-4}\to\epsilon^{-3}$）；动量把指数 $q$ 从 $1$ 降到 $1/2$（$\epsilon^{-3}\to\epsilon^{-2.5}$）；外推负责压制原始–对偶耦合旋转，保证加动量后系统不发散。**

---

### 一、三种加速技巧的极简对照表

| 技巧 | 作用对象 | 核心功能 | 解决的阶数跃迁 |
| :--- | :--- | :--- | :--- |
| **1. 锚定 / Tikhonov 正则**（$-\frac{1}{2s}\lVert\boldsymbol{\lambda}\rVert^2$） | 无曲率单调算子（$\mu_\lambda=0\to 1/s$） | 给平直的对偶方向注入 $1/s\sim\epsilon$ 的曲率，把单调残差代价从 $\epsilon^{-2}$ 压到条件数 $s\sim\epsilon^{-1}$ | **$q: 2 \to 1$**（总复杂度 **$\epsilon^{-4} \to \epsilon^{-3}$**，我们现稿已完成） |
| **2. 惯性动量**（Nesterov / 梯度累加器 $\mathbf{v}^k$） | 病态强凹单块（条件数 $\kappa_\lambda = Ls \sim \epsilon^{-1}$） | 在曲率 $1/s$ 的慢方向上累加约 $\sqrt{s}$ 步同向梯度，把条件数 $s$ 开根号变成 $\sqrt{s}\sim\epsilon^{-1/2}$ | **$q: 1 \to 1/2$**（总复杂度 **$\epsilon^{-3} \to \epsilon^{-2.5}$**） |
| **3. 算子外推**（EG / OGDA 梯度差 / PDHG 耦合外推） | 跨块反对称耦合项 $\langle\boldsymbol{\lambda},\mathcal{A}(\mathbf{x})\rangle$ | 用预测步或一步历史差分提供超前相移，抵消原始–对偶旋转模态的发散 | **本身不降 $q$**（单独用仍停在 $\epsilon^{-3}$），但**是动量能稳定工作的必要护栏** |

---

### 二、三句话记住全部逻辑

1. **为什么锚定到 $\epsilon^{-3}$ 就停了**：锚定（或加 $1/s$ 正则）只能把无曲率的 $\epsilon^{-2}$ 变成曲率倒数 $s\sim\epsilon^{-1}$，无法把已有的条件数 $s$ 开根号。
2. **为什么从 $\epsilon^{-3}$ 到 $\epsilon^{-2.5}$ 必须靠对偶动量（或直接放大 $\rho\sim\epsilon^{-1/2}$）**：内层原始块有近端项 $\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}^k\rVert^2$ 托底，条件数 $\kappa_x=\Theta(1)$ 不病态；只有对偶块条件数 $\kappa_\lambda\sim s\sim\epsilon^{-1}$ 病态，必须用对偶动量把内层步数从 $s$ 压到 $\sqrt{s}$，中心步长才能放大到 $\alpha\sim\epsilon^{1/2}$。
3. **为什么动量和外推必须一起上**：极小化问题没有旋转，单加 Nesterov 动量即可；鞍点问题有原始–对偶耦合旋转，单加动量会放大振荡，必须配外推（Zhang–Xu 用双步 EG，单步化简可用 OGDA 梯度差或 PDHG 耦合外推）来稳住耦合项。

---

**核心要义：锚定（Tikhonov $1/s$）负责 $\epsilon^{-4}\to\epsilon^{-3}$，对偶动量负责把条件数 $s$ 开根号实现 $\epsilon^{-3}\to\epsilon^{-2.5}$，算子外推负责在加动量时压住原始–对偶耦合振荡。**这个拆开乘的 本质上是什么 你咋听不懂我意思 我可能自己也表达不清楚

---

## Assistant (2026-11-11 14:28)

老大，这次我听懂了。拆开相乘的本质是一个公式：**对光滑非凸函数做梯度下降，迭代数等于"初始间隙除以步长乘 $\epsilon^2$"**。这里的函数是包络 $p$，步长是 $\alpha\gamma$。

$$
K\asymp\frac{\Delta}{(\alpha\gamma)\,\epsilon^{2}}
$$

所以 $\epsilon^{-2}$ 和 $1/\alpha$ 是同一个梯度下降公式里的两个量：精度和步长。

**步长为什么只能取 $\alpha$。** 平常梯度下降的步长由光滑常数决定。$p$ 的光滑常数是 $1/\gamma$，是常数，本来可以取 $\alpha=\Theta(1)$。限制来自另一处：算法拿不到 $p$ 的梯度

$$
\nabla p(\mathbf{z})=\frac{\mathbf{z}-\mathbf{x}^\star(\mathbf{z})}{\gamma}
$$

因为 $\mathbf{x}^\star(\mathbf{z})$ 是子问题的解。算法用 $\mathbf{x}^{k+1}$ 代替它。$\mathbf{x}^{k+1}$ 每步只向 $\mathbf{x}^\star(\mathbf{z}^k)$ 靠近一个比例 $\delta$，这个 $\delta$ 是内层方法的单步收缩率。$\mathbf{z}$ 每步移动的比例是 $\alpha$。要让 $\mathbf{x}^{k+1}$ 一直是 $\mathbf{x}^\star(\mathbf{z}^k)$ 的好近似，必须

$$
\alpha\lesssim\delta
$$

**所以 $1/\alpha$ 的含义是：算一次包络梯度要花多少步。**

- 双循环的写法：外层做 $\Delta/\epsilon^2$ 次梯度步，每次用 $1/\delta$ 步内层迭代算出 $\nabla p$，总数是两者的乘积。Lin–Jin–Jordan 就是这样写的。
- 单循环的写法：每次迭代做 $1$ 步内层，同时做 $\delta$ 比例的外层步。总工作量相同，$1/\delta$ 从"内层迭代数"变成"步长的倒数"。

**指数 $q$ 就是内层收缩率 $\delta$ 对 $\epsilon$ 的阶：**

| 内层 | $\delta$ | 复杂度 |
|---|---|---|
| 梯度上升，强凹模 $1/s$ | $\tau/s\sim\epsilon$ | $\epsilon^{-3}$ |
| 加 Nesterov 外推 | $\sqrt{\tau/s}\sim\sqrt{\epsilon}$ | $\epsilon^{-5/2}$ |

**写成一句定理形式的话：**

$$
K=O\left(\frac{\Delta}{\gamma\,\delta\,\epsilon^{2}}\right),\qquad \delta=\text{内层方法在子问题上的单步收缩率}
$$

这句话的严格版本就是上面的命题 3：只要内层满足收缩率 $\delta$，取 $\alpha=c\delta$ 就有这个界。

---

## User (2026-11-11 14:35)

我们需要学习的写作的语言风格和固定风格 列出25年及其之前的问闸

---

## Assistant (2026-11-11 14:35)

老大，下面是 2025 年及之前、适合这一章照着学的文章。除第 1 篇今天读过原文，其余对内容的描述是凭记忆写的，用之前请对照原文。

| # | 文章 | 学什么 | 用在哪一部分 | bib |
|---|---|---|---|---|
| 1 | Lin, Jin, Jordan, *Near-Optimal Algorithms for Minimax Optimization*, COLT 2020 | 定理后用一段话把复杂度拆成"外层迭代数 × 内层代价"；用对偶正则把凹情形化为强凹情形 | 定理之后的解释段、$\epsilon^{-2}\times\sqrt{\kappa}$ 的叙述 | 需新增 |
| 2 | Zhang, Xiao, Sun, Luo, *A Single-Loop Smoothed Gradient Descent-Ascent Algorithm for Nonconvex-Concave Min-Max Problems*, NeurIPS 2020 | 单循环加移动近端中心的势函数证明：先定义势函数，再分别给原始、对偶、中心三个下降引理，最后合并 | Iteration Complexity 小节和附录证明的组织 | 已有 `zhang2020single` |
| 3 | Yang, Orvieto, Lucchi, He, *Faster Single-loop Algorithms for Minimax Optimization without Strong Concavity*, AISTATS 2022 | 交替梯度步的单循环方法；定理用条件数 $\kappa$ 陈述，形式是 $O(\kappa\epsilon^{-2})$ | 用条件数写定理和对比 | 需新增 |
| 4 | Lin, Jin, Jordan, *On Gradient Descent Ascent for Nonconvex-Concave Minimax Problems*, ICML 2020 | 复杂度写成 $\kappa$ 的幂乘 $\epsilon^{-2}$；非凸–强凹与非凸–凹两种情形的并列写法 | Remark 里与族内结果的对比 | 已有 `lin2020gradient` |
| 5 | Nesterov, *Lectures on Convex Optimization*, 2018，第 2.2 节 | 常数动量格式和估计序列的写法 | 固定中心收缩引理（G2）的证明语言 | 已有 `nesterov2018lectures` |
| 6 | Xu, *Accelerated first-order primal-dual proximal methods for linearly constrained composite convex programming*, SIOPT 2017 | SIOPT 的版式：算法框、带参数条件的定理、与未加速速率对比的 Remark | 整章的版式和 Remark 的写法 | 需新增 |
| 7 | Kong, Monteiro, *An accelerated inexact proximal point method for solving nonconvex-concave min-max problems*, SIOPT 2021 | 非凸–凹问题上 $\epsilon^{-5/2}$ 结果在 SIOPT 的陈述方式，问题带复合结构 | 主定理的陈述、与多循环方法的对比 | 需新增 |

**分工建议**

- **定理陈述与解释段**：照第 1、3、7 篇。
- **证明的组织**：照第 2 篇，这是和我们结构最接近的一篇。
- **固定中心那一步**：照第 5 篇。
- **版式**：照第 6 篇。

按项目规则，选定后要把各篇的固定表达摘进 `notes/project/writing-phrasebook.md`。

---

## User (2026-11-11 15:18)

\begin{lemma}[Multiplier bounds]
\label{lem:b2-prime-multiplier-bounds}
Suppose \(\tau\le\rho/4\), \(s\ge4\tau\), and the extrapolation
coefficient is constant and equal to
\(\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}\).
Then, for every \(k\ge0\), 先看下这 这个条件 后面是会被满足吗

---

## Assistant (2026-11-11 15:19)

老大，会被满足。这条引理的三个条件都被下一条引理和主定理的参数选择包含。

| 引理的条件 | 后面由什么保证 |
|---|---|
| $\tau\le\rho/4$ | `lem:b2-prime-potential-descent` 的 $\tau\le\min\{\rho/4,\ 1/(14\gamma G_{\mathcal{A}}^2)\}$ |
| $s\ge 4\tau$ | 同一引理的 $s\ge\max\{\rho,4\tau\}$；主定理取 $s=c_s/\epsilon$，$\epsilon$ 充分小时成立 |
| 外推系数为常数 | 算法第 4 行本身就是这个系数，$s$ 和 $\tau$ 在一次运行中固定 |

对照证明笔记 Proposition G1.4：它只要求 $0\lt\tau(1/\rho+1/s)\lt 1$ 和常数外推系数。$\tau\le\rho/4$、$s\ge 4\tau$ 给出 $\tau(1/\rho+1/s)\le 1/2$，所以文件里的条件比笔记的条件强，引理成立。两个界 $\max\{4,2\sqrt{2}\sqrt{\rho/\tau}\}L_h$ 和它的 $3$ 倍也与笔记一致。

一处措辞可以简化："the extrapolation coefficient is constant and equal to …" 是算法的定义，可以改成 "Let $\{\boldsymbol{\lambda}^k\}$ be generated by Algorithm~\ref{alg:b2-prime} with $\tau\le\rho/4$ and $s\ge 4\tau$"。要改的话告诉我。

---

## User (2026-11-11 15:19)

gamma是什么？

---

## Assistant (2026-11-11 15:19)

老大，$\gamma$ 是势函数里近端项的参数：

$$
\mathcal{P}_s(\mathbf{x},\boldsymbol{\lambda};\mathbf{z},\boldsymbol{\mu})=\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})+\frac{1}{2\gamma}\lVert\mathbf{x}-\mathbf{z}\rVert^2-\frac{1}{2s}\lVert\boldsymbol{\lambda}-\boldsymbol{\mu}\rVert^2
$$

- $1/\gamma$ 是原始近端项的系数，$\gamma$ 越小，$\mathbf{x}$ 被拉向中心 $\mathbf{z}$ 的力度越大。
- 它保证子问题关于 $\mathbf{x}$ 强凸：强凸模是 $\mu_\gamma=1/\gamma-L_{\mathcal{D},\mathbf{x}}$，所以要求 $\gamma\lt 1/L_{\mathcal{D},\mathbf{x}}$。
- 它是参数组 $\theta=(\rho,s,\gamma,\eta,\tau)$ 的一员，与原始步长 $\eta$ 是两个量，定义里要求 $\eta\le\gamma$。加速这一章的分析取 $\eta=\gamma$。

你选中的这条乘子有界引理里没有 $\gamma$：它的界只依赖 $\rho/\tau$ 和 $L_h$。

---

## User (2026-11-11 15:26)

根据我浅薄的认知 我们这个技术和结果在minmax 非凸凹并不新？ 但是我们是单循环啊 我们对于参数rho的是固定的啊 这个说明我们的邻近算子 可以取rho任意取对吧。 这个对于alm是有意义的。 先回答这个问题呢

---

## Assistant (2026-11-11 15:27)

老大，你的判断基本对，有两处要说准确。

**在 minimax 里不新的部分**

- 速率 $\epsilon^{-5/2}$：多循环有 Lin–Jin–Jordan 2020，单循环有 Zhang–Xu 2026。
- 证明框架：包络函数加内层加速能量，Zhang–Xu 和 Tracked-FOAM 都用过。

**对 ALM 有意义的部分**

- **$\rho$ 与 $\epsilon$ 无关。** 任意固定的 $\rho\gt 0$ 都可以，条件只有 $\tau\le\rho/4$、$s\ge\max\{\rho,4\tau\}$ 和 $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$。
- **邻近算子是 $\mathrm{prox}_{h/\rho}$，参数不随精度变化。**
- **原始步长不随精度变化。** 光滑常数是

$$
L_{\mathcal{D},\mathbf{x}}=L_f+L_{\mathcal{A}}L_h+\rho G_{\mathcal{A}}^2
$$

  $\rho$ 固定时它是常数。罚方法或 $\rho\sim 1/\epsilon$ 的 ALM 里这个常数是 $\Theta(1/\epsilon)$，原始步长被迫取 $\Theta(\epsilon)$。
- **乘子不需要投影，也不需要先验的有界对偶域。** minimax 的结果都假设对偶域有界。

**要说准确的两处**

1. **"$\rho$ 任意取"的含义是任意固定值，其他参数随之调整。** 常数依赖 $\rho$：乘子的界含 $\sqrt{\rho/\tau}$，$\Delta_{\mathcal{W}}$ 含 $L_h^2/\rho$。
2. **精度由 $s=c_s/\epsilon$ 承担，$s$ 仍然依赖 $\epsilon$。** 有效罚参数是 $\rho+s$。区别在于 $s$ 只出现在对偶步的 $-\boldsymbol{\lambda}/s$ 这一项里，不进入邻近算子，也不进入原始光滑常数。所以论文里要写 "the penalty parameter and the primal stepsize are independent of $\epsilon$"，不能写 "all parameters are independent of $\epsilon$"。

**一个要正视的对比**：把 Zhang–Xu 的算法作用在 $\mathcal{D}_\rho$ 上，推断也能得到单循环、固定 $\rho$ 的 $\epsilon^{-5/2}$。所以"单循环加固定 $\rho$"这个组合不是我们独有的；我们独有的是算法更简单，以及乘子无界时不用投影。

---

## User (2026-11-11 15:27)

结果不新 单丝是单循环？ 也就是现阶段 我们的参数条件只有s和alpha

---

## Assistant (2026-11-11 15:28)

老大，两点都基本对，各补一句。

**结果不新，单循环也不是我们独有。** Zhang–Xu 2026 已经是单循环的 $\epsilon^{-5/2}$。我们能说的是：

- 单循环，并且每步只有一次原始梯度步和一次对偶梯度步，没有 extragradient，没有投影；
- 在 ALM 的设定下成立：$\rho$ 固定，乘子无界。

**依赖 $\epsilon$ 的参数只有 $s$ 和 $\alpha$。**

| 参数 | 取值 | 是否依赖 $\epsilon$ |
|---|---|---|
| $\rho,\gamma,\eta,\tau$ | 常数 | 否 |
| $s$ | $c_s/\epsilon$ | 是 |
| $\alpha$ | $c\sqrt{\tau/s}=\Theta(\sqrt{\epsilon})$ | 是，由 $s$ 决定 |
| 外推系数 | $(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})$ | 是，由 $s$ 决定 |

所以独立的精度相关参数只有 $s$ 一个，$\alpha$ 和外推系数都是 $s$ 的函数。

---

## User (2026-11-11 15:28)

和eps 有关？

---

## Assistant (2026-11-11 15:28)

老大，对，和 $\epsilon$ 有关的只有 $s$：

$$
s=\frac{c_s}{\epsilon}
$$

$\alpha$ 和外推系数通过 $s$ 间接依赖 $\epsilon$：

$$
\alpha=c\sqrt{\frac{\tau}{s}}=c\sqrt{\frac{\tau\,\epsilon}{c_s}},\qquad \frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}=1-\Theta(\sqrt{\epsilon})
$$

$\rho,\gamma,\eta,\tau$ 与 $\epsilon$ 无关。

这意味着算法要预先知道目标精度 $\epsilon$ 才能设定 $s$。不依赖 $\epsilon$ 的 anytime 版本（$s_k\sim k^{2/5}$）目前是待证。

---

## User (2026-11-11 15:28)

这个一个灵魂问题： 一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？ 一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？一个灵魂问题是，目前的复杂度对算法真正表现的指导意义有多大？ 不要罗素

---

## Assistant (2026-11-11 15:29)

老大，我的判断：**对"参数怎么随精度取"有指导意义，对"实际跑多快"指导意义小。** 本项目到现在没有做过数值实验，下面的判断都来自理论本身。

**有指导意义的三点**

- **$\alpha$ 的量级。** 理论给出不加外推时 $\alpha\sim\tau/s$，加外推后 $\alpha\sim\sqrt{\tau/s}$。这是可以直接照着调参的结论。
- **两种失败方式。** $\alpha$ 太小，平台实例上推进慢；$\alpha$ 太大，旋转实例上不收敛。下界的实例说明了调参时会碰到什么。
- **$\rho$ 不用增大。** 精度交给 $s$，邻近算子和原始步长不必随精度变化。

**指导不了的四点**

- **最坏情形与典型情形的差距。** 平台和旋转实例是专门构造的。实际问题常有 KŁ 性质或局部正则性，速率会比 $\epsilon^{-5/2}$ 快得多，理论没有刻画这一点。
- **常数。** $\gamma L_{\mathcal{D},\mathbf{x}}\le 1/10$、$c\le 1/6$ 这类条件是证明需要的充分条件，实际可用的步长通常更大。
- **$\epsilon^{-3}$ 与 $\epsilon^{-5/2}$ 的差别何时显现。** 两者相差 $\epsilon^{-1/2}$ 倍，$\epsilon=10^{-4}$ 时是 $100$ 倍。但只有对偶子问题确实病态、存在接近平坦的对偶方向时，这个差别才会出现；对偶方向曲率好的实例上，加不加外推可能差不多。
- **预先知道 $\epsilon$。** 定理要求 $s=c_s/\epsilon$ 事先定好。实际使用更自然的是递增的 $s_k$，这个版本还没有证明。

**对论文的含义**：复杂度结果回答的是"哪个参数必须随精度变、哪个机制限制了速度"，是结构性的结论。论文里不要把它写成对实际性能的预测。

---

## User (2026-11-11 15:31)

这个数值实验 我不知道适合做什么 比如这个圈子的 顶会顶刊 大家会做啥？

---

## Assistant (2026-11-11 15:31)

老大，这个圈子大致有三种做法。下面的例子是凭记忆列的，具体实验设置请对照原文。

**一、不做实验**

纯复杂度的文章常见。Lin–Jin–Jordan（COLT 2020）全文没有实验，下界类文章基本也没有。投 COLT 或 Mathematical Programming 可以这样，SIOPT 的审稿人通常希望至少有一个小实验。

**二、验证理论的合成实验**

紧性分析和下界类文章的常见做法：在困难实例或简单二次模型上跑算法，画迭代数对 $\epsilon$ 的双对数图，看斜率是否等于理论指数；再画不同步长下的轨迹，展示理论预测的失败方式。

**三、标准应用问题**

| 方向 | 常见问题 | 代表文章 |
|---|---|---|
| 非凸–凹 minimax | 鲁棒神经网络训练、分布鲁棒优化、公平分类、WGAN 的简化模型 | Zhang et al. 2020（Smoothed GDA）、Nouiehed et al. 2019、Yang et al. 2022 |
| 非凸约束优化与 ALM | 非凸二次约束二次规划、线性约束非凸二次规划、聚类的 Burer–Monteiro 分解、基追踪、Neyman–Pearson 分类 | Sahin et al. 2019（iALM）、Li et al. 2021、Kong–Monteiro |
| 复合问题 $f+h\circ\mathcal{A}$ | 鲁棒相位恢复、有限个光滑函数取最大、带 $\ell_1$ 精确罚的约束问题 | 非光滑复合优化的文章常用 |

**对我们的建议：做两个小实验**

1. **验证实验。** 在平台实例和旋转实例上比较 LRALM（$\beta=0$，$\alpha\sim\epsilon$）与加对偶外推的版本（$\alpha\sim\sqrt{\epsilon}$）。
   - 图一：迭代数对 $\epsilon$ 的双对数图，预期斜率 $-3$ 和 $-5/2$。
   - 图二：固定 $\epsilon$，改变 $\alpha$，展示 $\alpha$ 过大时不加外推的版本不收敛。
   
   这个实验直接对应论文的定理，成本低。

2. **一个应用问题。** 鲁棒相位恢复最贴合我们的问题类：

$$
\min_{\mathbf{x}}\ \frac{1}{m}\sum_{i=1}^{m}\left\lvert\langle\mathbf{a}_i,\mathbf{x}\rangle^2-b_i\right\rvert
$$

   这里 $h$ 是 $\ell_1$ 范数，$\mathcal{A}$ 是二次映射。比较对象：LRALM 的 $\beta=0$ 和 $\beta=1$、加外推的版本、$\rho\sim 1/\epsilon$ 的罚方法。要注意二次映射的 Jacobian 不是全局有界的，假设只在有界区域内成立，论文里要说明。

第一个实验能回答你刚才的问题：$\epsilon^{-3}$ 和 $\epsilon^{-5/2}$ 的差别在什么实例上看得到。

---

## User (2026-11-11 15:32)

理论给出不加外推时 $\alpha\sim\tau/s$，加外推后 $\alpha\sim\sqrt{\tau/s}$。这是可以直接照着调参的结论。
两种失败方式。 $\alpha$ 太小，平台实例上推进慢；$\alpha$ 太大，旋转实例上不收敛。下界的实例说明了调参时会 这份不是普通优化的结论吗😂 还是啥 我不清楚的

---

## Assistant (2026-11-11 15:32)

老大，定性上是的："步长太小慢、太大不收敛"是普通结论。这里具体的内容在于**是哪个步长、阈值是多少**。

**和普通梯度下降不同的地方**

- 普通梯度下降的阈值由光滑常数决定。包络 $p$ 的光滑常数是 $1/\gamma$，是常数，按这个标准 $\alpha$ 可以取到 $\Theta(1)$。
- 这里 $\alpha$ 的阈值是 $\tau/s\sim\epsilon$，远小于 $1$。限制来自 $\mathbf{x}^{k+1}$ 对 $\mathbf{x}^\star(\mathbf{z}^k)$ 的跟踪，与 $p$ 的光滑性无关。梯度步长 $\eta$、$\tau$ 本身都是常数。

**它属于哪一类已知原理**

这是两时间尺度（two-timescale）原理：慢变量的移动要慢于快变量的收敛速率。两时间尺度 GDA 里原始步长与对偶步长之比取 $1/\kappa^2$，双层优化和 actor–critic 里也有同样的条件。所以原理本身不新。

**我们的结果在这个原理上加了什么**

1. **阈值的精确量级和紧性。** 上界说 $\alpha\sim\tau/s$ 可行；下界说 $\alpha$ 取任何值，复杂度都不低于 $\Delta/(16\gamma\alpha\epsilon^2)$。两者合起来说明族内没有更好的选择。
2. **阈值可以通过改内层方法移动。** 对偶外推把阈值从 $\tau/s$ 提到 $\sqrt{\tau/s}$。

"$\alpha$ 太大不收敛"这一条，在 $\epsilon(\rho+s)\le c_1$ 的区域已由论文的旋转实例证明；在 $s=c_s/\epsilon$ 的区域就是等 GPT Pro 的那个实例，还没有证明。

---

## User (2026-11-11 15:34)

好的 gptpro先给你 **Proved. The proposed construction works for the entire requested range, including \(\beta=0\).** The proof uses a uniformly bounded second-order recurrence rather than assuming that the remainder decays.

:chatgpt-content-reference{index="4"}[Complete appendix-ready English LaTeX proof](sandbox:/mnt/data/LowerBoundLargeAlpha.tex)

The file contains the theorem, explicit constants, complete proofs of all supporting lemmas, all six requested checks, and a final section distinguishing \(\beta=0\) from \(\beta>0\). It preserves the repository’s update order, zero initialization, problem class, and post-primal KKT output.  

## Result and explicit constants

Write \(\chi=\eta/\gamma\). One sufficient choice is
\[
\omega
=
\min\left\{
\frac{\chi}{512},
\frac{\sqrt{\eta\tau}}{2},
\sqrt{\frac{\eta}{4(1+\rho/\tau)}}
\right\},
\qquad
\delta=\frac{\omega^2}{64},
\]
\[
C_\lambda=\frac{400}{\chi^2},
\qquad
A_0=
\min\left\{
\frac14,\frac{\Delta}{4},
\frac{1}{8(1+C_\lambda)+5\rho}
\right\},
\]
and
\[
c_{\mathrm r}
=
\frac34 A_0\omega
\min\left\{
\frac{1}{\sqrt{\eta\tau}},
\frac{1}{2\tau}
\right\}.
\]
Then take
\[
\boxed{
B=
\max\left\{
1,\frac{\tau}{c_s\delta},\frac{2}{c_{\mathrm r}}
\right\},
\qquad
\epsilon_0=
\min\left\{
1,\frac{c_s}{2\tau},\frac{1}{2B}
\right\}.
}
\]

These constants depend only on the fixed quantities
\[
(\rho,\gamma,\eta,\tau,c_s,\Delta).
\]

For every
\[
0<\epsilon<\epsilon_0,\qquad
\alpha\in(B\epsilon,1],\qquad
\beta\in[0,1],
\]
the constructed two-dimensional instance satisfies
\[
\boxed{
I\in\mathcal I(\mathbf C_0,\Delta),
\qquad
R_k\ge c_{\mathrm r}\alpha>2\epsilon
\quad\text{for every }k\ge0.
}
\]
Consequently,
\[
\boxed{
T_\epsilon^{\mathrm{KKT}}
\bigl(\theta(\epsilon),\alpha,\beta;I\bigr)=+\infty.
}
\]

## The six required steps

### 1. Zero-initialization decomposition — Proved

The appendix gives explicit formulas for
\[
\mathbf v,\qquad \mathbf r,\qquad \mathbf w_c,\qquad \mathbb T
\]
and proves
\[
\mathbb T\mathbf v=\zeta\mathbf v,
\qquad
Q(\mathbb T)\mathbf r=0,
\qquad
\mathbf v+\mathbf r=-\mathbf w_c,
\]
where
\[
Q(t)
=
(t-1+D)(t-1+V)-\vartheta(t-1+\alpha),
\qquad
\vartheta=(1-V)\xi.
\]

Thus the candidate trajectory starts **exactly at zero**:
\[
\mathbf w^k
=
\mathbf w_c+\zeta^k\mathbf v+\mathbb T^k\mathbf r.
\]

The annihilator identity is proved algebraically. Its extension to \(\beta=0\) does not extend any strict-stability assertion.

### 2. Uniform remainder bounds — Proved

The decisive estimates are
\[
\boxed{
\sup_{k\ge0}|(\mathbb T^k\mathbf r)_x|
\le\frac{36\omega}{\chi}X
<\frac X8,
\qquad
\sup_{k\ge0}|(\mathbb T^k\mathbf r)_\lambda|
\le\frac{400}{\chi^2}|\Lambda|.
}
\]

Both center components are also uniformly bounded. **No bound contains a factor growing with \(s\).**

The multiplier estimate follows from the primal row,
\[
\eta b(\mathbb T^k\mathbf r)_\lambda
=
(1+\eta a-\chi)(\mathbb T^k\mathbf r)_x
+\chi(\mathbb T^k\mathbf r)_z
-(\mathbb T^{k+1}\mathbf r)_x,
\]
together with
\[
\eta b|\Lambda|\ge\omega DX,
\qquad D\ge\chi/2.
\]
This avoids summing a remainder that may fail to decay.

### 3. Membership in the original problem class — Proved

The construction retains the repository’s radial extension, with new parameters and amplitude. 

The appendix verifies
\[
L_f\le\frac12,
\qquad
G_f\le\frac9{32}<1,
\qquad
L_{\mathcal A}=0,
\qquad
G_{\mathcal A}=b\le1,
\qquad
L_h=1,
\]
and
\[
F(0)-\inf F
\le\frac{205}{128}A_0
<2A_0
\le\Delta.
\]

### 4. Both proximal outputs and the actual trajectory — Proved

For both \(j=k\) and \(j=k+1\),
\[
\boxed{
\|\lambda^k+\rho\mathcal A(x^j)\|
\le\frac14<1.
}
\]
Since \(h(y)=\|y\|_2\), both proximal evaluations therefore return zero.

The candidate trajectory also remains in the quadratic region:
\[
\frac34X\le\|x^k-x_c\|\le\frac54X.
\]
The proof first establishes these properties for the candidate sequence, then verifies that it satisfies the actual four updates. This removes any circular reliance on the linear recurrence.

### 5. Residual lower bound — Proved

The feasibility component alone suffices:
\[
R_k
\ge b\|x^{k+1}-x_c\|
\ge\frac34bX.
\]
With
\[
L=\frac{\Lambda}{X},
\qquad
X=\frac{A_0}{\max\{1,|L|\}},
\]
the construction gives
\[
b\ge\frac{\omega\alpha}{\sqrt{\eta\tau}},
\qquad
\frac b{|L|}\ge\frac{\omega\alpha}{2\tau}.
\]
Hence
\[
bX
=A_0\min\{b,b/|L|\}
\ge
A_0\omega\alpha
\min\left\{
\frac1{\sqrt{\eta\tau}},\frac1{2\tau}
\right\},
\]
which proves \(R_k\ge c_{\mathrm r}\alpha\) for every iteration.

### 6. Separation from the upper-bound path — Proved

The upper-bound appendix requires
\[
\alpha_{\mathrm{ub}}
\le\frac{1}{384r\tau\omega_s^2}.
\]
Its own formula for \(\omega_s\) implies
\[
\omega_s^2\ge\frac{s}{\tau^2a_s},
\qquad 0<a_s<r.
\]
Therefore,
\[
\alpha_{\mathrm{ub}}
=\frac{\kappa_{\mathrm{ub}}}{\ell s}
\le\frac{\tau a_s}{384rs}
<\frac d{384}.
\]
These are precisely the existing upper-bound parameter restrictions. 

Our threshold satisfies
\[
B\epsilon\ge\frac d\delta>\frac d{384}.
\]
Thus
\[
\boxed{
B\epsilon>\frac{\kappa_{\mathrm{ub}}}{\ell s}.
}
\]
The two parameter regions are disjoint.

## The distinction between \(\beta=0\) and \(\beta>0\)

For **\(\beta>0\)**,
\[
Q(1)=\frac{D\beta H}{J}>0.
\]
Both roots of \(Q\) lie strictly inside the unit disk. The remainder therefore tends to zero for each fixed parameter choice.

For **\(\beta=0\)**, the exact factorization is
\[
\boxed{
Q(t)=(t-1)(t-r_0),
\qquad
r_0=1-D+d(W-1).
}
\]
Moreover,
\[
0\le r_0<1,
\qquad
1-r_0\ge(1-\delta)D\ge\frac{\chi}{4}.
\]
The unit root is simple, and
\[
\mathbb T^k\mathbf r
=
\mathbf r^{(1)}+r_0^k\mathbf r^{(0)},
\]
with explicit components
\[
\mathbf r^{(1)}
=
\frac{(\mathbb T-r_0I)\mathbf r}{1-r_0},
\qquad
\mathbf r^{(0)}
=
\frac{(I-\mathbb T)\mathbf r}{1-r_0}.
\]

The persistent component is permitted. The proved \(X/8\) bound prevents the entire primal remainder from cancelling the rotational component. Also,
\[
\mu^k=0
\qquad\text{for every }k\ge0,
\]
exactly as required by zero initialization and \(\beta=0\).

**No unproved step remains in this large-\(\alpha\) branch.**他的文件一直到下载不了

---

## Assistant (2026-11-11 15:35)

老大，文件还是拿不到，所以完整证明我仍然看不到。我对摘要里能独立验算的三处做了核对，都成立；剩下的四项只有结论，无法核对。

**我验算通过的三处**

- **第 6 项，与上界参数范围不重叠。** 附录 C 的 $\omega_s$ 定义给出 $\omega_s^2\ge s/(\tau^2 a_s)$，于是上界的 $\alpha$ 不超过 $\tau a_s/(384rs)$，小于 $d/384$。下界要求 $\alpha\gt B\epsilon\ge d/\delta$，而 $\delta\lt 1$。两个范围不相交。
- **$b\ge\omega\alpha/\sqrt{\eta\tau}$。** 由 $b^2=\nu WH/(\eta\tau J)$、$W\ge 1$ 和 $H\ge J$ 得到；$H\ge J$ 来自 $V\ge\beta$。
- **$G_{\mathcal{A}}=b\le 1$。** 我算得 $\alpha^2W\le 2$、$H/J\le 2$，所以 $b^2\le 4\omega^2/(\eta\tau)$，正好对应它选的 $\omega\le\sqrt{\eta\tau}/2$。

**没法核对的四项**

1. $\mathbf{v}$、$\mathbf{r}$、$\mathbf{w}_c$ 的显式公式和零初值分解。
2. 剩余项的两个一致界，包括递推核的估计。
3. $L_f$、$G_f$ 和初始间隙的验证。
4. 两次 prox 输出为零的验证。

$\beta=0$ 时的因式分解 $Q(t)=(t-1)(t-r_0)$ 和 $1-r_0\ge\chi/4$ 是合理的，单位根是单根，剩余项有界这个结论站得住，但细节在文件里。

**让 GPT Pro 把证明直接贴出来**，发这一句就行：

```text
The sandbox file link cannot be downloaded. Paste the full contents of LowerBoundLargeAlpha.tex directly in the chat inside a single ```latex code block, complete and unabridged. If it is too long for one message, split it into consecutive messages at section boundaries and say "continued" until the end.
```

拿到全文后我存进 `notes/gpt-proofs/`，再核对上面四项。

---

## User (2026-11-11 15:39)

% !TEX root = ../main.tex
% Insert this file as an appendix section.
% Status labels requested for this proof audit: "Proved" means "已证".
% Every asserted step below is proved; no unproved step is used.

\section{A large-center-stepsize lower bound}
\label{app:q3-large-alpha}

This appendix proves only the large primal-center stepsize branch for
\(s=c_s/\epsilon\). We use the initialization, update order, output,
problem class, and first hitting time of
Definitions~\ref{def:splalm}, \ref{def:problem-class}, and
\ref{def:complexity-measure}. The instance has the radial form of
Example~\ref{ex:rotation}, but its frequency and amplitude are chosen
differently. Neither the hypothesis \(\epsilon(\rho+s)\le c_1\) nor
\(\beta>0\) is imposed. In particular, the strict spectral-radius
conclusion of Lemma~\ref{lem:rot-spectral} is not invoked.

We identify \(\RR^2\) with \(\mathbb C\), as in the preliminaries.
Thus each complex coordinate below represents a real two-dimensional
block, its modulus is its Euclidean norm, and
\(\langle p,q\rangle=\operatorname{Re}(\overline p q)\).
All matrices acting on the four complex coordinates have real entries.

\subsection{Fixed constants and the statement}
\label{subsec:q3-large-constants}

\paragraph{Status: proved.}
Fix
\[
\rho>0,\qquad 0<\eta\le\gamma,\qquad
\tau>0,\qquad c_s>0,\qquad \Delta>0,
\qquad \chi:=\frac{\eta}{\gamma}\in(0,1].
\]
Choose the following explicit positive constants:
\begin{equation}
\begin{aligned}
\omega&:=\min\left\{
  \frac{\chi}{512},\,
  \frac{\sqrt{\eta\tau}}{2},\,
  \sqrt{\frac{\eta}{4(1+\rho/\tau)}}\right\},
&\delta&:=\frac{\omega^2}{64},\\
C_\lambda&:=\frac{400}{\chi^2},
&A_0&:=\min\left\{
  \frac14,\,\frac{\Delta}{4},\,
  \frac{1}{8(1+C_\lambda)+5\rho}\right\},\\
c_{\rm r}&:=\frac34 A_0\omega
  \min\left\{\frac{1}{\sqrt{\eta\tau}},\frac{1}{2\tau}\right\},
&B&:=\max\left\{1,\frac{\tau}{c_s\delta},\frac{2}{c_{\rm r}}\right\},\\
\epsilon_0&:=\min\left\{1,\frac{c_s}{2\tau},\frac{1}{2B}\right\}.
\end{aligned}
\label{eq:q3-large-fixed-constants}
\end{equation}
These constants depend only on
\((\rho,\gamma,\eta,\tau,c_s,\Delta)\). They do not depend on
\(\epsilon,\alpha,\beta\), or the instance dimensions.
The constant \(\delta\) here bounds \(d/\alpha\); it is not the
symbol \(\delta=1/s\) used in Appendix~\ref{app:upper-beta0}.

\begin{theorem}[Large primal-center stepsizes at \(s=c_s/\epsilon\)]
\label{thm:q3-large-alpha}
\textbf{Status: proved.}
Let the constants be given by~\eqref{eq:q3-large-fixed-constants}.
For every
\[
0<\epsilon<\epsilon_0,\qquad
\alpha\in(B\epsilon,1],\qquad \beta\in[0,1],\qquad
s:=\frac{c_s}{\epsilon},
\]
there exists an instance
\(I\in\mathcal I(\mathbf C_0,\Delta)\), with
\(\mathbf C_0=(1,1,0,1,1)\) and \(n=m=2\), such that SPLALM
started from zero satisfies
\[
R_k\ge c_{\rm r}\alpha>\epsilon
\qquad\text{for every }k\ge0.
\]
Consequently,
\[
T^{\mathrm{KKT}}_\epsilon(\theta(\epsilon),\alpha,\beta;I)
=+\infty,
\qquad
\theta(\epsilon)=(\rho,c_s/\epsilon,\gamma,\eta,\tau).
\]
\end{theorem}

The proof is completed in Step~5 below. Throughout the construction let
\[
d:=\frac{\tau}{s}=\frac{\tau\epsilon}{c_s}.
\]
The choice of \(B\) and the strict inequality \(\alpha>B\epsilon\)
give
\begin{equation}
0<d<\delta\alpha,\qquad 0<\alpha\le1,
\qquad d<\frac12,
\qquad 0<\omega\le\frac{\chi}{512}\le\frac1{512}.
\label{eq:q3-large-domain}
\end{equation}
In particular, \(s>\tau\), as required by Definition~\ref{def:splalm}.

\subsection{Parameters of the linear recursion}
\label{subsec:q3-large-parameters}

Set
\begin{equation}
\begin{aligned}
\nu&:=\omega^2\alpha^2,
&\zeta&:=1-\frac{\nu}{2}
       +\mathrm{i}\sqrt{\nu-\frac{\nu^2}{4}},
&u&:=\zeta-1,\\
V&:=\beta+d(1-\beta),
&E&:=\alpha^2+(1-\alpha)\nu,
&W&:=1+\frac{\chi\alpha(1-\alpha)}{E},\\
D&:=\alpha W,
&H&:=V^2+(1-V)\nu,
&\Upsilon&:=\beta V+(1-V)\nu,\\
b^2&:=\frac{\nu WH}{\eta\tau\Upsilon},
&\xi&:=\frac{\nu W(V-\beta)}{\Upsilon},
&a&:=\frac{\nu(W-1)}{\eta\alpha}+\frac{\xi}{\eta},\\
\kappa&:=\rho b^2+a,
&\vartheta&:=(1-V)\xi,
&U&:=\alpha+\chi(1-\alpha),
\end{aligned}
\label{eq:q3-large-parameters}
\end{equation}
where \(b\) denotes the positive square root. The symbol
\(\Upsilon\) is the denominator denoted by \(J\) in the proposed
construction. The radial curvature \(\kappa\) has the same meaning
as in Example~\ref{ex:rotation}; it is unrelated to the coefficient
called \(\kappa\) in~\eqref{eq:beta0-alpha}.

\begin{lemma}[Uniform parameter bounds]
\label{lem:q3-large-parameters}
\textbf{Status: proved.}
All quantities in~\eqref{eq:q3-large-parameters} are well-defined,
including when \(\beta=0\). They satisfy
\begin{equation}
\begin{gathered}
|\zeta|=1,\qquad |u|=\sqrt{\nu}=\omega\alpha,
\qquad u^2+\nu u+\nu=0,\\
\frac{\chi}{2}\le D\le1,\qquad D\ge\alpha,
\qquad 0\le\xi\le2\delta D,
\qquad 0\le\vartheta\le\delta D,\\
\frac{\omega^2\alpha^2}{\eta\tau}
\le b^2\le\frac{2\omega^2}{\eta\tau}\le\frac12,
\qquad 0\le\eta a\le2\omega^2,
\qquad 0<\kappa\le\frac12.
\end{gathered}
\label{eq:q3-large-parameter-bounds}
\end{equation}
For every \(t\in[0,1]\),
\begin{equation}
|u+t|^2=t^2+(1-t)\nu\ge\frac{\nu}{4}.
\label{eq:q3-large-denominator-bound}
\end{equation}
Finally,
\begin{equation}
\begin{aligned}
\eta a&=\frac{\nu(W-1)}{\alpha}+\xi,
&\eta\tau b^2&=\nu W+V\xi,\\
U-D&=\frac{(1-\alpha)\nu(W-1)}{\alpha},
&\beta\eta\tau b^2&=\nu(WV-\vartheta).
\end{aligned}
\label{eq:q3-large-algebra-identities}
\end{equation}
\end{lemma}

\begin{proof}
By~\eqref{eq:q3-large-domain}, \(0<\nu<1\) and \(0<V\le1\).
If \(\beta>0\), then \(\Upsilon\ge\beta V>0\).
If \(\beta=0\), then
\(V=d<1\) and \(\Upsilon=(1-d)\nu>0\).
Also \(E>0\) and \(H>0\). This proves that the definitions are valid.
The definition of \(\zeta\) gives its modulus, \(|u|^2=\nu\), and
\(u^2+\nu u+\nu=0\). Since
\(\operatorname{Re}(u)=-\nu/2\),
\[
|u+t|^2=t^2+(1-t)\nu
=(t-\nu/2)^2+\nu(1-\nu/4)
\ge\frac34\nu\ge\frac14\nu.
\]
This proves~\eqref{eq:q3-large-denominator-bound}.

Substitution of \(\nu=\omega^2\alpha^2\) gives
\[
D=\alpha+
\frac{\chi(1-\alpha)}{1+(1-\alpha)\omega^2}.
\]
It follows that
\[
D\ge\alpha,\qquad
\frac{U}{1+\omega^2}\le D\le U\le1,
\qquad U\ge\chi.
\]
Since \(\omega\le1\), these inequalities imply \(D\ge\chi/2\).

For \(\beta<1\), use
\(V-\beta=d(1-\beta)\),
\(1-V=(1-d)(1-\beta)\), and
\(\Upsilon\ge(1-V)\nu\) to obtain
\[
\frac{\xi}{W}
=\frac{\nu(V-\beta)}{\Upsilon}
\le\frac{d}{1-d}\le2d,
\]
\[
\vartheta
=\frac{\nu W(V-\beta)(1-V)}{\Upsilon}
\le W(V-\beta)\le Wd\le\delta D.
\]
Thus \(\xi\le2dW\le2\delta D\).
When \(\beta=1\), both \(\xi\) and \(\vartheta\) are zero, so the
same bounds hold.

The identity \(H-\Upsilon=V(V-\beta)\) gives
\[
\eta\tau b^2
=\frac{\nu WH}{\Upsilon}
=\nu W+V\xi.
\]
Since \(H\ge\Upsilon\) and \(W\ge1\),
\[
b^2\ge\frac{\nu}{\eta\tau}.
\]
For the upper bound, use \(\nu W=\omega^2\alpha D\),
\(V\le1\), and \(D\le1\):
\[
\eta\tau b^2
\le\omega^2\alpha D+2\delta D
\le\omega^2+2\delta\le2\omega^2.
\]
Moreover,
\[
\eta a
=\omega^2\alpha(W-1)+\xi
=\omega^2(D-\alpha)+\xi
\le\omega^2D+2\delta D\le2\omega^2.
\]
The choices of \(\omega\) in~\eqref{eq:q3-large-fixed-constants}
therefore imply
\[
b^2\le\frac{2\omega^2}{\eta\tau}\le\frac12,
\qquad
0<\kappa=\rho b^2+a
\le\frac{2\omega^2}{\eta}\left(1+\frac{\rho}{\tau}\right)
\le\frac12.
\]
Strict positivity of \(\kappa\) follows from \(\rho>0\) and \(b>0\).

The first identity in~\eqref{eq:q3-large-algebra-identities} is the
definition of \(a\); the second was proved above. For the third,
\[
U-D
=\chi(1-\alpha)\left(1-\frac{\alpha^2}{E}\right)
=\frac{\chi(1-\alpha)^2\nu}{E}
=\frac{(1-\alpha)\nu(W-1)}{\alpha}.
\]
For the last identity, the definition of \(\xi\) gives
\(\xi[\beta V+(1-V)\nu]=\nu W(V-\beta)\). Hence
\[
\begin{aligned}
\beta(\nu W+V\xi)-\nu(WV-\vartheta)
&=-\nu W(V-\beta)+\xi[\beta V+(1-V)\nu]\\
&=0.
\end{aligned}
\]
\end{proof}

\subsection{Step 1: explicit zero-initialization decomposition}
\label{subsec:q3-large-decomposition}

Define
\begin{equation}
\begin{aligned}
L&:=\frac{\tau b\zeta(u+\beta)}{u(u+V)},
&X&:=\frac{A_0}{\max\{1,|L|\}},
&\Lambda&:=LX,\\
Z&:=\frac{\alpha\zeta}{u+\alpha}X,
&M&:=\frac{\beta\zeta}{u+\beta}\Lambda,
&\bv&:=(X,\Lambda,Z,M)^{\mathsf{T}}.
\end{aligned}
\label{eq:q3-large-eigenvector}
\end{equation}
Thus \(X>0\), \(L\ne0\), and
\(\max\{X,|\Lambda|\}=A_0\).
Set
\begin{equation}
\begin{aligned}
r_x&:=-\frac{
 (W-1)\dfrac{u}{u+\alpha}
 +\xi\dfrac{\zeta}{u+V}}{W+\xi}\,X,\\
\Omega_x&:=\xi\left((1-\alpha)r_x
                  +(V-\alpha)\frac{\zeta}{u+V}X\right),\\
r_\lambda&:=\frac{\chi(X-Z)+(\eta a+D)r_x-\Omega_x}{\eta b},\\
r_z&:=r_x+X-Z,
\qquad r_\mu:=r_\lambda+\Lambda-M,\\
x_c&:=-(X+r_x),
\qquad\lambda_c:=-(\Lambda+r_\lambda),\\
\br&:=(r_x,r_\lambda,r_z,r_\mu)^{\mathsf{T}},
\qquad
\bw_c:=(x_c,\lambda_c,x_c,\lambda_c)^{\mathsf{T}}.
\end{aligned}
\label{eq:q3-large-initial-shift}
\end{equation}
All denominators are nonzero by Lemma~\ref{lem:q3-large-parameters}.
The real matrix of the shifted four-step recursion is
\begin{equation}
\mathbb{T}:=\begin{pmatrix}
1+\eta a-\chi & -\eta b & \chi & 0\\
\tau b(1+\eta a-\chi) & 1-d-\eta\tau b^2 & \tau b\chi & d\\
\alpha(1+\eta a-\chi) & -\alpha\eta b & 1-\alpha+\alpha\chi & 0\\
\beta\tau b(1+\eta a-\chi) & \beta(1-d-\eta\tau b^2)
  & \beta\tau b\chi & 1-\beta+\beta d
\end{pmatrix}.
\label{eq:q3-large-matrix}
\end{equation}
Introduce
\begin{equation}
Q(t):=(t-1+D)(t-1+V)-\vartheta(t-1+\alpha).
\label{eq:q3-large-Q}
\end{equation}

\begin{lemma}[Spectral identities and the prescribed initialization]
\label{lem:q3-large-decomposition}
\textbf{Status: proved.}
For every parameter choice above, including \(\beta=0\),
\begin{equation}
\mathbb{T}\bv=\zeta\bv,
\qquad Q(\mathbb{T})\br=0,
\qquad \bv+\br=-\bw_c.
\label{eq:q3-large-decomposition-identities}
\end{equation}
Consequently, the candidate sequence
\begin{equation}
\widetilde{\bw}^{\,k}:=
\bw_c+\zeta^k\bv+\mathbb{T}^k\br
\label{eq:q3-large-candidate}
\end{equation}
satisfies \(\widetilde{\bw}^{\,0}=0\) and
\[
\widetilde{\bw}^{\,k+1}-\bw_c
=\mathbb{T}(\widetilde{\bw}^{\,k}-\bw_c).
\]
The subspace \(\ker Q(\mathbb{T})\) is invariant under \(\mathbb{T}\).
No assertion of strict stability at \(\beta=0\) is made here.
\end{lemma}

\begin{proof}
We first prove the characteristic factorization. In
\((1+t)I-\mathbb{T}\), replace the third row by the third row minus
\(\alpha\) times the first row, and the fourth row by the fourth row
minus \(\beta\) times the original second row. Then replace the second
row by the second row minus \(\tau b\) times the first row.
These determinant-preserving operations give the matrix
\[
\begin{pmatrix}
t-\eta a+\chi&\eta b&-\chi&0\\
-\tau b(1+t)&t+d&0&-d\\
-\alpha(1+t)&0&t+\alpha&0\\
0&-\beta(1+t)&0&t+\beta
\end{pmatrix}.
\]
For a spectral variable \(1+t\), elimination of the two center
coordinates therefore gives
\[
z=\frac{\alpha(1+t)}{t+\alpha}x,
\qquad
\mu=\frac{\beta(1+t)}{t+\beta}\lambda.
\]
Substitution into the primal and dual rows produces the two equations
\[
\bigl[t(t+U)-\eta a(t+\alpha)\bigr]x
       +\eta b(t+\alpha)\lambda=0,
\]
\[
t(t+V)\lambda-\tau b(1+t)(t+\beta)x=0.
\]
The center block has determinant \((t+\alpha)(t+\beta)\),
which cancels the denominators introduced in these two equations.
Thus, initially away from these denominators and then as a polynomial
identity,
\begin{equation}
\begin{aligned}
P(t):=\det((1+t)I-\mathbb{T})
={}&t^2(t+U)(t+V)-\eta a\,t(t+\alpha)(t+V)\\
&+\eta\tau b^2(t+1)(t+\alpha)(t+\beta).
\end{aligned}
\label{eq:q3-large-characteristic-unfactored}
\end{equation}
Write
\[
A:=\frac{\nu(W-1)}{\alpha},\qquad
C:=D+V-\vartheta,\qquad N:=DV-\alpha\vartheta.
\]
Then~\eqref{eq:q3-large-algebra-identities} reads
\[
\eta a=A+\xi,\quad
\eta\tau b^2=\nu W+V\xi,\quad
U=D+(1-\alpha)A,\quad
\alpha A=\nu(W-1),\quad
\beta\eta\tau b^2=\nu(WV-\vartheta).
\]
The coefficient of \(t^3\) in \(P\) is
\[
U+V-\eta a+\eta\tau b^2
=D+V-\vartheta-\alpha A+\nu W=C+\nu.
\]
The coefficient of \(t^2\) is
\[
\begin{aligned}
UV-\eta a(\alpha+V)+\eta\tau b^2(1+\alpha+\beta)
&=N+\nu(V+1)+\nu W(\alpha+\beta-V)+\beta V\xi\\
&=N+\nu(V+1)+\nu D-\nu\vartheta\\
&=N+\nu C+\nu.
\end{aligned}
\]
Here the second equality uses
\(\nu W(\beta-V)+\beta V\xi=-\nu\vartheta\), which follows
from the last identity in~\eqref{eq:q3-large-algebra-identities}.
The coefficient of \(t\) is
\[
\begin{aligned}
-\eta a\alpha V+\eta\tau b^2(\alpha+\beta+\alpha\beta)
&=-\nu V(W-1)+\nu D
   +(1+\alpha)\nu(WV-\vartheta)\\
&=\nu(C+N).
\end{aligned}
\]
The constant coefficient is
\(\alpha\beta\eta\tau b^2=\nu N\), and the leading coefficient
is one. Hence
\begin{equation}
P(t)=(t^2+\nu t+\nu)
       \bigl((t+D)(t+V)-\vartheta(t+\alpha)\bigr).
\label{eq:q3-large-characteristic-factorization}
\end{equation}

Next, \(u^2+\nu u+\nu=0\) implies \(P(u)=0\).
Divide~\eqref{eq:q3-large-characteristic-unfactored}, evaluated at
\(u\), by \(u(u+V)(u+\alpha)\). The result is
\[
\frac{u(u+U)}{u+\alpha}-\eta a
 +\frac{\eta\tau b^2\zeta(u+\beta)}{u(u+V)}=0.
\]
Since
\(X-Z=(1-\alpha)uX/(u+\alpha)\) and
\(\Lambda/X=\tau b\zeta(u+\beta)/(u(u+V))\), this equation gives
\[
uX=\eta aX-\eta b\Lambda-\chi(X-Z).
\]
This is precisely the first row of \(\mathbb{T}\bv=\zeta\bv\).
The definition of \(\Lambda\) gives
\[
u(u+V)\Lambda=\tau b\zeta(u+\beta)X.
\]
Together with
\(\Lambda-M=(1-\beta)u\Lambda/(u+\beta)\), it implies
\[
u\Lambda=\tau b\zeta X-d(\Lambda-M),
\]
which verifies the dual row after the primal row.
The identities
\[
(u+\alpha)Z=\alpha\zeta X,
\qquad (u+\beta)M=\beta\zeta\Lambda
\]
verify the two center rows. Thus \(\mathbb{T}\bv=\zeta\bv\).

We now prove the annihilator identity without assuming stability.
For this algebraic argument only, allow \(\nu\) to vary independently
in \((0,4)\), with the other formulas unchanged and with arbitrary
\(X>0\). Initially assume
\[
0<\alpha,\beta,d<1,\qquad V\ne\alpha,
\]
and that the roots \(t_1,t_2\) of \(Q\) are distinct.
Here
\[
Q(1)=N=\frac{D\beta H}{\Upsilon}>0,
\]
\[
Q(1-\alpha)=\alpha(W-1)(V-\alpha)\ne0,
\qquad Q(1-V)=\vartheta(V-\alpha)\ne0.
\]
Therefore none of the following eigenvector denominators vanishes:
\[
\mathbf{e}(t):=
\left(
1,\frac{\tau bt(t-1+\beta)}{(t-1)(t-1+V)},
\frac{\alpha t}{t-1+\alpha},
\frac{\tau b\beta t^2}{(t-1)(t-1+V)}
\right)^{\mathsf{T}}.
\]
The elimination equations above, and the factorization of \(P\), give
\(\mathbb{T}\mathbf{e}(t_j)=t_j\mathbf{e}(t_j)\).
For coefficients \(c_1,c_2\), requiring
\(\bv+\sum_jc_j\mathbf{e}(t_j)\) to have equal first and third
coordinates, and equal second and fourth coordinates, yields
\begin{equation}
\sum_{j=1}^2c_j\frac{t_j-1}{t_j-1+\alpha}
=-\frac{u}{u+\alpha}X,
\qquad
\sum_{j=1}^2c_j\frac{t_j}{t_j-1+V}
=-\frac{\zeta}{u+V}X.
\label{eq:q3-large-synchronization-system}
\end{equation}
Indeed, the first coordinate difference in \(\mathbf{e}(t)\) is
\((1-\alpha)(t-1)/(t-1+\alpha)\); the second coordinate
difference is \((1-\beta)\tau bt/(t-1+V)\). Dividing by the
nonzero factors \(1-\alpha\) and \((1-\beta)\tau b\),
respectively, gives~\eqref{eq:q3-large-synchronization-system}.

Let \(v_j=t_j-1\). These numbers satisfy
\(v_j^2+Cv_j+N=0\). At any such root,
\[
\frac{v_j}{v_j+\alpha}
=\frac{N+\alpha v_j}{\alpha^2-C\alpha+N},
\qquad
\frac{v_j+1}{v_j+V}
=\frac{N-C+V-(1-V)v_j}{V^2-CV+N}.
\]
These identities follow by multiplying by their denominators and
replacing \(v_j^2\) by \(-Cv_j-N\).
The two constant denominators are
\[
A_\alpha:=\alpha^2-C\alpha+N
=\alpha(W-1)(V-\alpha),
\]
\[
A_V:=V^2-CV+N=\vartheta(V-\alpha).
\]
With \(S_0=c_1+c_2\) and \(S_1=c_1v_1+c_2v_2\),
the synchronization system becomes
\begin{equation}
\begin{pmatrix}
N&\alpha\\ N-C+V&-(1-V)
\end{pmatrix}
\begin{pmatrix}S_0\\ S_1\end{pmatrix}
=-X\begin{pmatrix}
A_\alpha u/(u+\alpha)\\ A_V\zeta/(u+V)
\end{pmatrix}.
\label{eq:q3-large-two-by-two-system}
\end{equation}
Its determinant is
\[
-N(1-V)-\alpha(N-C+V)
=(\alpha-V)\bigl[D(1-V)+\alpha\vartheta\bigr]
=\alpha(1-V)(\alpha-V)(W+\xi)\ne0.
\]
Cramer's rule for the first component gives
\[
S_0
=-\frac{(W-1)u/(u+\alpha)+\xi\zeta/(u+V)}{W+\xi}X
=r_x.
\]
The first equation in~\eqref{eq:q3-large-two-by-two-system}
then gives
\[
S_1=-(WV-\vartheta)r_x
       -(W-1)(V-\alpha)\frac{u}{u+\alpha}X.
\]
Using
\[
(W-1)\frac{u}{u+\alpha}X
=-(W+\xi)r_x-\xi\frac{\zeta}{u+V}X,
\]
we obtain
\[
\begin{aligned}
S_1
&=\bigl[-WV+\vartheta+(V-\alpha)(W+\xi)\bigr]r_x
  +\xi(V-\alpha)\frac{\zeta}{u+V}X\\
&=-Dr_x+\Omega_x.
\end{aligned}
\]
The coefficients themselves exist explicitly:
\[
c_1=\frac{S_1-v_2S_0}{v_1-v_2},
\qquad
c_2=\frac{v_1S_0-S_1}{v_1-v_2}.
\]
For \(\br':=c_1\mathbf{e}(t_1)+c_2\mathbf{e}(t_2)\),
its first coordinate is \(r_x\), and its synchronization equations
give \(r'_z=r_x+X-Z\) and
\(r'_\mu=r'_\lambda+\Lambda-M\).
The first row of \(\mathbb{T}-I\) gives
\[
S_1=\eta ar_x-\eta br'_\lambda+\chi(X-Z).
\]
Consequently
\[
r'_\lambda
=\frac{\chi(X-Z)+(\eta a+D)r_x-\Omega_x}{\eta b}
=r_\lambda.
\]
All four coordinates of \(\br'\) therefore equal those of \(\br\).
Since each \(t_j\) is a root of \(Q\),
\(Q(\mathbb{T})\br=0\) in this nondegenerate case.

For completeness, the continuation to excluded parameter values is
purely algebraic. On
\[
0<\alpha\le1,\quad 0\le\beta\le1,\quad 0<d<1,
\quad 0<\nu<4,
\]
all entries of \(Q(\mathbb{T})\br\) are continuous: \(b>0\),
\(W+\xi>0\), \(\Upsilon>0\), and the complex denominators
\(u\), \(u+\alpha\), \(u+\beta\), and \(u+V\) do not vanish.
The nondegenerate parameters used above are dense. To see this, first
choose interior \((\alpha,\beta,d)\) with \(V\ne\alpha\) and
\(V\ne U\), which is possible arbitrarily close to any target since
\(V=\beta+d(1-\beta)\) varies strictly with \(\beta\) when \(d<1\).
For these fixed interior parameters, the discriminant
\(C^2-4N\) is a rational function of \(\nu\) and tends to
\((U-V)^2>0\) as \(\nu\downarrow0\). Its numerator is therefore
not the zero polynomial, and its zeros are isolated. Perturbing \(\nu\)
arbitrarily little avoids them. Taking limits proves the annihilator
identity at repeated roots, \(V=\alpha\), \(\alpha=1\),
\(\beta=1\), and \(\beta=0\). One then specializes back to
\(\nu=\omega^2\alpha^2\). This continuation concerns only an
identity, not strict stability.

Finally, the definitions give, coordinate by coordinate,
\[
\bv+\br
=(X+r_x,\Lambda+r_\lambda,X+r_x,\Lambda+r_\lambda)^{\mathsf{T}}
=-\bw_c.
\]
The candidate initialization and recurrence now follow from
\(\mathbb{T}\bv=\zeta\bv\). The kernel is invariant because
\(Q(\mathbb{T})\mathbb{T}=\mathbb{T}Q(\mathbb{T})\).
\end{proof}

\subsection{Step 2: uniform bounds for the remainder}
\label{subsec:q3-large-remainder}

\begin{lemma}[A uniformly bounded second-order kernel]
\label{lem:q3-large-kernel}
\textbf{Status: proved.}
Write \(Q(t)=t^2-St+P_0\), so that
\[
S=2-D-V+\vartheta,
\qquad P_0=(1-D)(1-V)+\vartheta(1-\alpha).
\]
Both roots \(t_1,t_2\) lie in the closed unit disk. Define
\[
G_{-1}:=0,
\qquad G_j:=\sum_{i=0}^jt_1^{\,j-i}t_2^{\,i},\quad j\ge0,
\]
with the same finite sum used when the roots coincide. Then
\begin{equation}
\sup_{j\ge0}|G_j|\le\frac4D.
\label{eq:q3-large-kernel-bound}
\end{equation}
Every sequence satisfying \(y_{k+2}=Sy_{k+1}-P_0y_k\) has
\begin{equation}
y_k=G_{k-1}y_1-P_0G_{k-2}y_0,\qquad k\ge1.
\label{eq:q3-large-recurrence-solution}
\end{equation}
These statements include \(\beta=0\).
\end{lemma}

\begin{proof}
Let \(h_0=(1-\delta)D\). The parameter bounds give
\[
S\ge0,\qquad
0\le P_0\le1-D+\vartheta\le1-h_0<1,
\]
\[
Q(1)=DV-\alpha\vartheta
=\frac{D\beta H}{\Upsilon}\ge0.
\]
If the roots are real, their nonnegative sum and product imply that
both are nonnegative. If one exceeded one and the other were less
than one, \(Q(1)\) would be negative. If both were at least one and
one exceeded one, their product would exceed one. Thus both roots
belong to \([0,1]\). Order them as \(t_1\ge t_2\). Then
\[
t_2\le\sqrt{P_0}\le\sqrt{1-h_0},
\qquad
|G_j|\le\sum_{i=0}^jt_2^i
\le\frac{1}{1-\sqrt{1-h_0}}
\le\frac{2}{h_0}\le\frac4D.
\]
Here \(1-\sqrt{1-h_0}=h_0/(1+\sqrt{1-h_0})\ge h_0/2\),
and \(\delta\le1/2\).
If the roots are nonreal, they are conjugate and have common modulus
\(q=\sqrt{P_0}\le\sqrt{1-h_0}<1\). Hence
\[
|G_j|\le(j+1)q^j
\le\sum_{i=0}^jq^i
\le\frac{1}{1-\sqrt{1-h_0}}\le\frac4D.
\]
This proves the kernel bound, including repeated real roots.
The kernel satisfies \(G_0=1\), \(G_1=S\), and
\(G_{j+1}=SG_j-P_0G_{j-1}\).
Thus the right-hand side of~\eqref{eq:q3-large-recurrence-solution}
has initial values \(y_1\), \(Sy_1-P_0y_0\), and satisfies the
same recurrence. Induction proves the formula.
\end{proof}

\begin{lemma}[Remainder bounds independent of \(s\)]
\label{lem:q3-large-remainder}
\textbf{Status: proved.}
Write
\[
(p_k,\ell_k,z_k^{\rm r},m_k)^{\mathsf{T}}:=\mathbb{T}^k\br.
\]
Then, for every \(k\ge0\),
\begin{equation}
\begin{aligned}
|p_k|&\le\frac{36\omega}{\chi}X<\frac X8,
&|z_k^{\rm r}|&\le\frac{36\omega}{\chi}X,\\
|\ell_k|&\le C_\lambda|\Lambda|,
&|m_k|&\le(1+C_\lambda)|\Lambda|.
\end{aligned}
\label{eq:q3-large-remainder-bounds}
\end{equation}
In particular, \(\mathbb{T}^k\br\) is uniformly bounded also when
\(\beta=0\). None of the constants in these bounds grows with \(s\).
\end{lemma}

\begin{proof}
From the formula for \(r_x\), the inequalities
\(|u+\alpha|\ge\alpha\),
\(\xi/W\le2d\), and
\(|u+V|\ge\sqrt{\nu}/2\) give
\[
\begin{aligned}
\frac{|r_x|}{X}
&\le\frac{W-1}{W+\xi}\frac{|u|}{|u+\alpha|}
   +\frac{\xi}{W+\xi}\frac{1}{|u+V|}\\
&\le\omega+\frac{4d}{\sqrt{\nu}}
\le\omega+\frac{4\delta}{\omega}
=\frac{17}{16}\omega\le2\omega.
\end{aligned}
\]
The estimates \(\xi\le2\delta D\),
\(|V-\alpha|\le V+\alpha\),
\(V/|u+V|\le1\), and
\(\alpha/|u+V|\le2/\omega\) imply
\[
\begin{aligned}
\frac{|\Omega_x|}{DX}
&\le2\delta\left(2\omega+1+\frac{2}{\omega}\right)\\
&=4\delta\omega+2\delta+\frac{4\delta}{\omega}
=\frac{\omega^3}{16}+\frac{\omega^2}{32}+\frac{\omega}{16}
\le\frac{5\omega}{32}\le\omega.
\end{aligned}
\]
By the first row of \(\mathbb{T}\) and the definition of
\(r_\lambda\),
\[
p_0=r_x,
\qquad p_1=(1-D)r_x+\Omega_x.
\]
The identity \(Q(\mathbb{T})\br=0\) shows that \(p_k\)
satisfies the recurrence in Lemma~\ref{lem:q3-large-kernel}.
For \(k\ge1\), its solution formula therefore yields
\[
\begin{aligned}
|p_k|
&\le\frac4D\bigl(|p_1|+P_0|p_0|\bigr)\\
&\le\frac4D\bigl(2|r_x|+|\Omega_x|\bigr)\\
&\le\left(\frac{16\omega}{D}+4\omega\right)X
\le\frac{36\omega}{\chi}X.
\end{aligned}
\]
The bound also holds for \(k=0\).
Because \(\omega\le\chi/512\),
\(36\omega/\chi\le36/512<1/8\).

The center identity gives
\[
X-Z=\frac{(1-\alpha)u}{u+\alpha}X,
\qquad |X-Z|\le\omega X.
\]
Consequently \(|r_z|\le3\omega X\).
The third row of the recursion is
\[
z_{k+1}^{\rm r}=(1-\alpha)z_k^{\rm r}+\alpha p_{k+1}.
\]
Since \(0<\alpha\le1\), induction bounds \(|z_k^{\rm r}|\)
by \(\max\{|r_z|,\sup_j|p_j|\}\), which is at most
\(36\omega X/\chi\).

To estimate the multiplier without a factor proportional to \(s\),
use the primal row itself:
\[
\eta b\ell_k=(1+\eta a-\chi)p_k+\chi z_k^{\rm r}-p_{k+1}.
\]
Its first coefficient is nonnegative because \(\chi\le1\) and
\(a\ge0\). Since \(\eta a\le2\omega^2\le2\),
\begin{equation}
\eta b|\ell_k|
\le(2+\eta a)\frac{36\omega}{\chi}X
\le\frac{144\omega}{\chi}X.
\label{eq:q3-large-dual-from-primal}
\end{equation}
Let \(E_\beta:=|u+\beta|^2=\beta^2+(1-\beta)\nu\).
Using \(\operatorname{Re}(u)=-\nu/2\), we have
\[
\operatorname{Re}\bigl((u+V)\overline{(u+\beta)}\bigr)
=\Upsilon+\frac{\nu}{2}(V-\beta)
\ge\Upsilon.
\]
The modulus of this product is \(\sqrt{HE_\beta}\), so
\(\sqrt{HE_\beta}\ge\Upsilon\). The definition of \(\Lambda\)
then implies
\begin{equation}
\begin{aligned}
\eta b|\Lambda|
&=\frac{\eta\tau b^2\sqrt{E_\beta}}{\sqrt{\nu H}}X\\
&=\frac{\sqrt{\nu}W\sqrt{HE_\beta}}{\Upsilon}X
\ge\sqrt{\nu}WX=\omega DX.
\end{aligned}
\label{eq:q3-large-dual-amplitude-lower}
\end{equation}
Combining~\eqref{eq:q3-large-dual-from-primal}
and~\eqref{eq:q3-large-dual-amplitude-lower} gives
\[
|\ell_k|
\le\frac{144}{\chi D}|\Lambda|
\le\frac{288}{\chi^2}|\Lambda|
\le C_\lambda|\Lambda|.
\]

Finally,
\[
\Lambda-M=\frac{(1-\beta)u}{u+\beta}\Lambda.
\]
Since \(E_\beta\ge(1-\beta)\nu\),
\[
|\Lambda-M|^2
=\frac{(1-\beta)^2\nu}{E_\beta}|\Lambda|^2
\le(1-\beta)|\Lambda|^2\le|\Lambda|^2.
\]
Thus \(|r_\mu|\le(1+C_\lambda)|\Lambda|\).
The fourth row reads
\[
m_{k+1}=(1-\beta)m_k+\beta\ell_{k+1}.
\]
Induction gives the asserted bound for \(m_k\), including
\(\beta=0\), when \(m_k=r_\mu\) for every \(k\).
\end{proof}

\subsection{Step 3: membership in the normalized problem class}
\label{subsec:q3-large-instance}

Set \(R_*:=5X/4\), and define the instance by
\begin{equation}
\calA(x):=b(x-x_c),\qquad
h(y):=\|y\|_2,\qquad
f(x):=\psi(\|x-x_c\|)-b\langle\lambda_c,x-x_c\rangle,
\label{eq:q3-large-instance}
\end{equation}
where
\begin{equation}
\psi(r):=
\begin{cases}
-\dfrac{\kappa}{2}r^2,&0\le r\le R_*,\\[3pt]
\dfrac{\kappa}{2}(r-2R_*)^2-\kappa R_*^2,
   &R_*\le r\le3R_*,\\[3pt]
\kappa R_*(r-3R_*)-\dfrac{\kappa}{2}R_*^2,
   &r\ge3R_*.
\end{cases}
\label{eq:q3-large-radial-extension}
\end{equation}

\begin{lemma}[Uniform global constants and the initial gap]
\label{lem:q3-large-instance}
\textbf{Status: proved.}
The instance in~\eqref{eq:q3-large-instance} belongs to
\(\mathcal I(\mathbf C_0,\Delta)\). More explicitly, it satisfies
\[
L_f\le\frac12,\qquad G_f\le\frac9{32}<1,
\qquad L_{\calA}=0,\qquad G_{\calA}=b\le1,
\qquad L_h=1,
\]
and \(F(0)-\inf F\le\Delta\).
\end{lemma}

\begin{proof}
By the remainder bounds at \(k=0\),
\[
|x_c|\le X+|r_x|\le\frac98X<R_*,
\]
\[
|\lambda_c|\le|\Lambda|+|r_\lambda|
\le(1+C_\lambda)A_0\le\frac18.
\]
The last inequality follows from
\(A_0\le[8(1+C_\lambda)+5\rho]^{-1}\).
Also \(R_*\le5A_0/4\).

The values and first derivatives of \(\psi\) agree at both junctions.
At \(R_*\) the two values equal \(-\kappa R_*^2/2\), and both
first derivatives equal \(-\kappa R_*\). At \(3R_*\) both values
again equal \(-\kappa R_*^2/2\), and both first derivatives equal
\(\kappa R_*\). On the three open pieces,
\[
\psi'(r)=
\begin{cases}
-\kappa r,&r<R_*,\\
\kappa(r-2R_*),&R_*<r<3R_*,\\
\kappa R_*,&r>3R_*,
\end{cases}
\qquad
\psi''(r)\in\{-\kappa,\kappa,0\}.
\]
In particular, \(|\psi'(r)|\le\kappa R_*\).
For \(r>0\), the radial and tangential Hessian eigenvalues of
\(\psi(\|x-x_c\|)\) are \(\psi''(r)\) and \(\psi'(r)/r\).
The latter equals \(-\kappa\) in the first piece, belongs to
\([-\kappa,\kappa/3]\) in the middle piece, and belongs to
\([0,\kappa/3]\) in the last piece. Near the origin of these radial
coordinates, the function is the quadratic
\(-\kappa\|x-x_c\|^2/2\).
Its gradient is therefore continuous everywhere. Integrating its
piecewise bounded Hessian along a line segment proves that this gradient
is globally \(\kappa\)-Lipschitz. The added linear term does not change
this Lipschitz constant. Hence \(L_f\le\kappa\le1/2\).
Furthermore,
\[
\|\nabla f(x)\|
\le\kappa R_*+b|\lambda_c|
\le\frac58A_0+\frac18
\le\frac9{32}.
\]
The affine map has constant Jacobian \(bI_2\), so
\(L_{\calA}=0\) and \(G_{\calA}=b\le1\).
The Euclidean norm is convex, and the reverse triangle inequality
shows that its Lipschitz constant is one.

The radial extension satisfies \(\psi(r)\ge-\kappa R_*^2\).
Writing \(r=\|x-x_c\|\), the objective satisfies
\[
F(x)=\psi(r)-b\langle\lambda_c,x-x_c\rangle+br
\ge-\kappa R_*^2+b(1-|\lambda_c|)r
\ge-\kappa R_*^2.
\]
At zero, \(|x_c|<R_*\), so \(\psi(|x_c|)\le0\). Therefore
\[
F(0)\le b(1+|\lambda_c|)|x_c|
\le\frac98 bR_*\le\frac{45}{32}A_0.
\]
It follows that
\[
\begin{aligned}
F(0)-\inf F
&\le\frac{45}{32}A_0+\kappa R_*^2\\
&\le\frac{45}{32}A_0+\frac{25}{32}A_0^2\\
&\le\frac{205}{128}A_0
<2A_0\le\frac{\Delta}{2}\le\Delta.
\end{aligned}
\]
This verifies every constant in \(\mathbf C_0\) and the gap budget.
\end{proof}

\subsection{Step 4: both proximal outputs and the actual trajectory}
\label{subsec:q3-large-realization}

\begin{lemma}[The candidate sequence is the actual algorithm sequence]
\label{lem:q3-large-realization}
\textbf{Status: proved.}
For the instance above, the actual SPLALM iterates are
\[
\bw^k=\bw_c+\zeta^k\bv+\mathbb{T}^k\br,
\qquad k\ge0.
\]
For every \(k\ge0\), both proximal evaluations, at
\((x^k,\lambda^k)\) and \((x^{k+1},\lambda^k)\), return zero.
Moreover,
\begin{equation}
\frac34X\le|x^k-x_c|\le\frac54X=R_*.
\label{eq:q3-large-annulus}
\end{equation}
\end{lemma}

\begin{proof}
First consider only the candidate sequence
\(\widetilde{\bw}^{\,k}\) in~\eqref{eq:q3-large-candidate}.
Its first coordinate satisfies
\[
\widetilde x^{\,k}-x_c=\zeta^kX+p_k.
\]
Since \(|\zeta|=1\) and \(|p_k|<X/8\),
\[
\frac78X\le|\widetilde x^{\,k}-x_c|\le\frac98X.
\]
These bounds imply the weaker annulus in
\eqref{eq:q3-large-annulus} for every candidate point.
Its multiplier satisfies
\[
|\widetilde\lambda^{\,k}|
\le|\lambda_c|+|\Lambda|+|\ell_k|
\le2(1+C_\lambda)A_0.
\]
Consequently, for both \(j=k\) and \(j=k+1\),
\begin{equation}
\begin{aligned}
|\widetilde\lambda^{\,k}+\rho\calA(\widetilde x^{\,j})|
&\le2(1+C_\lambda)A_0+\frac54\rho bX\\
&\le\left[2(1+C_\lambda)+\frac54\rho\right]A_0
\le\frac14<1.
\end{aligned}
\label{eq:q3-large-prox-interior}
\end{equation}
The final inequality uses the definition of \(A_0\), whose third
upper bound is the reciprocal of four times the bracket.

For \(h(y)=\|y\|_2\),
\(\partial h(0)=\{q:\|q\|_2\le1\}\).
The optimality condition for the strongly convex proximal problem is
\[
y=\prox_{h/\rho}(\calA(x)+\lambda/\rho)
\quad\Longleftrightarrow\quad
\lambda+\rho(\calA(x)-y)\in\partial h(y).
\]
Thus \(|\lambda+\rho\calA(x)|\le1\) makes its unique minimizer
\(y=0\). Equation~\eqref{eq:q3-large-prox-interior} proves this
for both candidate evaluations, at every iteration.

On the candidate trajectory, all primal points lie in the quadratic
piece. With \(p=x-x_c\) and \(\ell=\lambda-\lambda_c\),
the reduced function is exactly
\[
\calD_\rho(x,\lambda)
=-\frac{\kappa-\rho b^2}{2}|p|^2+b\langle\ell,p\rangle
=-\frac a2|p|^2+b\langle\ell,p\rangle.
\]
Here \(h(0)=0\). Its gradients at the relevant evaluation points are
\[
\nabla_x\calD_\rho=-ap+b\ell,
\qquad \nabla_\lambda\calD_\rho=bp.
\]
After shifting both centers by \((x_c,\lambda_c)\), the actual four
updates consequently read
\[
\begin{aligned}
p^+&=(1+\eta a-\chi)p-\eta b\ell+\chi z,\\
\ell^+&=\ell+\tau bp^+-d(\ell-m),\\
z^+&=(1-\alpha)z+\alpha p^+,\\
m^+&=(1-\beta)m+\beta\ell^+.
\end{aligned}
\]
These are precisely the rows of~\eqref{eq:q3-large-matrix}.
The candidate sequence satisfies this recurrence and starts from zero
by Lemma~\ref{lem:q3-large-decomposition}. It also satisfies every
proximal and quadratic-region condition just verified.
Therefore, at iteration zero its four updates equal the actual updates.
If the two sequences agree through iteration \(k\), the unique primal
update and the unique proximal output at the new primal point agree,
and then the dual and center updates agree as well. Induction proves
identity of the two sequences for all \(k\).
\end{proof}

\subsection{Step 5: a residual lower bound at every iteration}
\label{subsec:q3-large-residual}

\begin{lemma}[Uniform residual lower bound]
\label{lem:q3-large-residual}
\textbf{Status: proved.}
For every \(k\ge0\), the actual post-primal output satisfies
\[
R_k\ge\frac34 bX\ge c_{\rm r}\alpha.
\]
\end{lemma}

\begin{proof}
The previous lemma gives \(y^{k+1}=0\), and hence
\[
q^k=\lambda^k+\rho\calA(x^{k+1})\in\partial h(0).
\]
The prescribed KKT residual is therefore
\[
R_k=\max\left\{
\left|-a(x^{k+1}-x_c)+b(\lambda^k-\lambda_c)\right|,
\ b|x^{k+1}-x_c|\right\}.
\]
Using only its feasibility component and the annulus gives
\(R_k\ge3bX/4\).

It remains to lower-bound the normalized amplitude \(bX\).
The parameter bounds give
\[
b\ge\frac{\sqrt{\nu}}{\sqrt{\eta\tau}}
=\frac{\omega\alpha}{\sqrt{\eta\tau}}.
\]
Also, since \(|u+V|=\sqrt H\) and
\(|u+\beta|=\sqrt{E_\beta}\),
\[
\sqrt{E_\beta}=|u+\beta|
\le|u+V|+(V-\beta)\le\sqrt H+d.
\]
By \(\sqrt H\ge\sqrt\nu/2\) and \(d\le\delta\alpha\),
\[
\frac{d}{\sqrt H}
\le\frac{2\delta}{\omega}=\frac{\omega}{32}\le1.
\]
Consequently \(\sqrt{E_\beta}\le2\sqrt H\).
The definition of \(L\) now yields
\[
\frac{b}{|L|}
=\frac{\sqrt\nu\sqrt H}{\tau\sqrt{E_\beta}}
\ge\frac{\omega\alpha}{2\tau}.
\]
Since \(L\ne0\) and \(X=A_0/\max\{1,|L|\}\),
\[
\begin{aligned}
bX
&=A_0\min\left\{b,\frac{b}{|L|}\right\}\\
&\ge A_0\omega\alpha
\min\left\{\frac{1}{\sqrt{\eta\tau}},\frac{1}{2\tau}\right\}.
\end{aligned}
\]
Multiplication by \(3/4\) gives the asserted constant
\(c_{\rm r}\) in~\eqref{eq:q3-large-fixed-constants}.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:q3-large-alpha}]
The conditions \(0<\epsilon<\epsilon_0\) and
\(\alpha>B\epsilon\) imply~\eqref{eq:q3-large-domain}.
Lemmas~\ref{lem:q3-large-parameters}--\ref{lem:q3-large-decomposition}
therefore define the instance parameters and its zero-initialized
candidate trajectory. Lemma~\ref{lem:q3-large-instance} places the
instance in \(\mathcal I(\mathbf C_0,\Delta)\), and
Lemma~\ref{lem:q3-large-realization} proves that this is the actual
algorithm trajectory. By Lemma~\ref{lem:q3-large-residual} and
\(B\ge2/c_{\rm r}\),
\[
R_k\ge c_{\rm r}\alpha
>c_{\rm r}B\epsilon\ge2\epsilon>\epsilon
\qquad\text{for every }k\ge0.
\]
No output satisfies the tolerance. Definition~\ref{def:complexity-measure}
therefore gives \(T^{\mathrm{KKT}}_\epsilon=+\infty\).
\end{proof}

\subsection{Step 6: separation from the proved upper-bound path}
\label{subsec:q3-large-upper-separation}

\begin{proposition}[Nonoverlap with Theorem~\ref{thm:upper-beta0}]
\label{prop:q3-large-upper-separation}
\textbf{Status: proved.}
Whenever the fixed parameters also satisfy the hypotheses of
Theorem~\ref{thm:upper-beta0}, its prescribed stepsize
\[
\alpha_{\rm ub}=\frac{\kappa_{\rm ub}}{\ell s},\qquad\beta=0,
\]
where \(\kappa_{\rm ub}\) denotes the coefficient in
\eqref{eq:beta0-alpha}, satisfies
\[
\alpha_{\rm ub}<\frac{d}{384}<B\epsilon
\]
for all sufficiently small \(\epsilon\) at the same
\(s=c_s/\epsilon\). Thus the two conclusions have disjoint
parameter ranges.
\end{proposition}

\begin{proof}
Use the upper-bound appendix's notation, with subscripts here to avoid
confusing it with the present instance parameters:
\[
r_{\rm ub}:=\gamma^{-1},\qquad
b_s^{\rm ub}:=\ell+s^{-1},\qquad
 a_s^{\rm ub}:=r_{\rm ub}-b_s^{\rm ub}>0.
\]
The quantity in~\eqref{eq:beta0-stepsizes} is
\[
(\omega_s^{\rm ub})^2
=s\frac{[a_s^{\rm ub}
 +\tau b_s^{\rm ub}(3r_{\rm ub}-2b_s^{\rm ub})]^2}
 {\tau^2(a_s^{\rm ub})^3}.
\]
Since \(b_s^{\rm ub}<r_{\rm ub}\),
\(3r_{\rm ub}-2b_s^{\rm ub}>0\); hence
\[
(\omega_s^{\rm ub})^2\ge\frac{s}{\tau^2a_s^{\rm ub}}.
\]
The third upper bound on \(\alpha\) in
\eqref{eq:beta0-stepsizes} consequently gives
\[
\alpha_{\rm ub}
\le\frac{1}{384r_{\rm ub}\tau(\omega_s^{\rm ub})^2}
\le\frac{\tau a_s^{\rm ub}}{384r_{\rm ub}s}
<\frac{\tau}{384s}=\frac{d}{384}.
\]
On the other hand, our threshold satisfies
\[
B\epsilon\ge\frac{\tau\epsilon}{c_s\delta}
=\frac{d}{\delta}>\frac{d}{384},
\]
because \(0<\delta<1\).
This proves, in particular, the requested strict inequality
\[
B\epsilon>\frac{\kappa_{\rm ub}}{\ell s}.
\]
No extra dependence of \(B\) on an unspecified upper-bound coefficient
is needed.
\end{proof}

\subsection{The difference between \(\beta=0\) and \(\beta>0\)}
\label{subsec:q3-large-beta-endpoint}

\paragraph{Status: proved.}
The construction, all six steps, and their constants are uniform over
\(\beta\in[0,1]\). Their spectral interpretations differ as follows.

For \(\beta>0\),
\[
Q(1)=\frac{D\beta H}{\Upsilon}>0.
\]
The root argument in Lemma~\ref{lem:q3-large-kernel} then puts both
roots strictly inside the unit disk: real roots lie in \([0,1]\),
and the displayed strict inequality excludes one; nonreal roots have
modulus \(\sqrt{P_0}<1\).
Each component of \(\mathbb{T}^k\br\) satisfies the scalar
second-order recurrence. For distinct roots, its solution is a linear
combination of their powers. For a repeated root \(t\), the solution
has the form \((c_0+c_1k)t^k\), with the zero-root case interpreted
directly from the recurrence. These expressions tend to zero.
Thus the remainder decays for each fixed \(\beta>0\), although no
uniform decay rate as \(\beta\downarrow0\) is needed or asserted.

For \(\beta=0\), the parameter formulas instead give exactly
\[
V=d,\qquad \Upsilon=(1-d)\nu,
\qquad \xi=\frac{Wd}{1-d},\qquad \vartheta=Wd.
\]
Therefore
\begin{equation}
Q(t)=(t-1)(t-r_0),
\qquad r_0:=1-D+d(W-1).
\label{eq:q3-large-beta-zero-factorization}
\end{equation}
Because \(W\ge1\), \(D\le1\), and \(Wd\le\delta D\),
\[
0\le1-D\le r_0
\le1-(1-\delta)D<1,
\qquad
1-r_0\ge(1-\delta)D\ge\frac{\chi}{4}.
\]
The unit root is simple. There is no Jordan growth at that root on
\(\ker Q(\mathbb{T})\), because the two factors in
\eqref{eq:q3-large-beta-zero-factorization} are distinct.
More explicitly, define
\[
\br^{(1)}:=\frac{(\mathbb{T}-r_0I)\br}{1-r_0},
\qquad
\br^{(0)}:=\frac{(I-\mathbb{T})\br}{1-r_0}.
\]
The annihilator identity proves directly that
\[
\br=\br^{(1)}+\br^{(0)},\qquad
\mathbb{T}\br^{(1)}=\br^{(1)},\qquad
\mathbb{T}\br^{(0)}=r_0\br^{(0)}.
\]
Consequently,
\begin{equation}
\mathbb{T}^k\br=\br^{(1)}+r_0^k\br^{(0)},\qquad k\ge0.
\label{eq:q3-large-beta-zero-remainder}
\end{equation}
The denominator \(1-r_0\) is bounded below by \(\chi/4\).
Independently of this decomposition, Lemma~\ref{lem:q3-large-remainder}
already provides the stated componentwise uniform bounds, so no
summation of a nondecaying remainder is used.

In this endpoint case \(M=0\), and the fourth row of \(\mathbb{T}\)
is the identity on the fourth coordinate. Moreover,
\[
r_\mu=r_\lambda+\Lambda=-\lambda_c.
\]
Thus the actual dual center is exactly
\[
\mu^k=\lambda_c+\zeta^kM+(\mathbb{T}^k\br)_\mu
=\lambda_c+r_\mu=0\qquad(k\ge0),
\]
as required by the algorithm with \(\beta=0\) and zero initialization.
The persistent component in~\eqref{eq:q3-large-beta-zero-remainder}
need not vanish; its primal component is nevertheless bounded together
with the entire remainder by \(X/8\). It therefore cannot cancel the
unit-modulus rotational component of primal amplitude \(X\).
This is the precise replacement for the strict-stability argument used
in the original \(\beta>0\) rotation branch. 你看一下

---

## Assistant (2026-11-11 15:47)

老大，我通读了全文，逐步验算了代数，又在实例上跑了真实算法：**没有发现错误，大步长分支成立，包括 $\beta=0$。**

## 手工验算通过的部分

- **递推矩阵**：从实例的梯度公式推出的四行更新与 $\mathbb{T}$ 一致，$(x_c,\lambda_c)$ 是平移后的不动点。
- **参数界**：$D$、$\xi$、$\vartheta$、$b^2$、$\eta a$、$\kappa$ 的上下界，以及四个代数恒等式。
- **特征多项式分解**：我逐项核对了 $t^3$、$t^2$、$t$ 和常数项的系数，分解式 $P(t)=(t^2+\nu t+\nu)\,Q(1+t)$ 成立。
- **零初值分解**：$2\times 2$ 方程组、行列式、Cramer 法则给出的 $r_x$，以及 $r_\lambda$ 的公式。
- **递推核的界 $4/D$ 和剩余项的界**：实根、复根两种情形都对；乘子界由原始行反解，不含 $s$。
- **问题类成员关系**：$L_f\le 1/2$、$G_f\le 9/32$、$G_{\mathcal{A}}=b\le 1$、初始间隙不超过 $\Delta/2$。
- **prox 输出为零**：$\lVert\boldsymbol{\lambda}^k+\rho\mathcal{A}(\mathbf{x}^j)\rVert\le 1/4$ 的推导。
- **残差下界**和**与 `thm:upper-beta0` 的参数范围不重叠**。

## 数值核对

脚本在 [temp/q3check/check.py](temp/q3check/check.py)。我按证明的公式构造实例，再用带 $\mathrm{prox}$ 的原始四步更新从零初值运行。

- 两组固定参数；$\alpha\in\{0.41,0.7,1\}$，都在 $(B\epsilon,1]$ 内；$\beta\in\{0,10^{-6},10^{-3},0.2,0.5,1\}$；每次 $3\times 10^5$ 到 $4\times 10^5$ 步。
- $\mathbb{T}\mathbf{v}=\zeta\mathbf{v}$ 和 $Q(\mathbb{T})\mathbf{r}=\mathbf{0}$ 的误差不超过 $10^{-13}$，$\beta=0$ 也是。
- 每一步的 prox 输出都是零。
- 所有输出的残差与 $c_{\mathrm{r}}\alpha$ 之比最小为 $2.4$，与定理一致。

## 三点说明

1. **证明里唯一的间接论证**是零化恒等式 $Q(\mathbb{T})\mathbf{r}=\mathbf{0}$：先在非退化参数上证，再用稠密性和连续性推到 $\beta=0$ 等边界。论证本身我没找到问题，数值上 $\beta=0$ 时恒等式也成立。
2. **常数 $B$ 很大。** 我算的两组参数里 $B\approx 10^7$。全族下界的常数是 $\Delta/(16\gamma B)$，量级约 $10^{-8}$。阶是 $\epsilon^{-3}$，结论不受影响；但 Remark 里不要把阈值 $B\epsilon$ 说成"略大于 $\tau/s$"。
3. **写入论文前要清理**：算法名 SPLALM 改 LRALM；删掉 "Status: proved" 标注；$\delta$、$\kappa$、$C_\lambda$ 与附录 C 和加速一章的记号重名，证明里已自己注明，定稿时最好换名。

## 还没做的一件事

这份证明目前只在聊天记录里，仓库里没有。请把你贴的全文存成 `overleaf/appendix/LowerBoundLargeAlpha.tex`，或者告诉我，我来写入。

---

## User (2026-11-11 19:02)

意思是目前的已经这个紧了？

*[Context was auto-compacted here; the summary repeats the text above and is omitted.]*

---

## Assistant (2026-11-11 19:02)

老大，是的：**在 $s=c_s/\epsilon$ 这一设定下，LRALM 族的 $\epsilon^{-3}$ 已经是紧的**，上界和下界对所有 $\alpha\in(0,1]$、$\beta\in[0,1]$ 匹配。

- **上界**：`thm:upper-beta0` 给出 $O(\epsilon^{-3})$。
- **下界，小步长分支** $\alpha\le B\epsilon$：`lem:plateau` 给出下式。

$$
T\gt\frac{\Delta}{16\gamma\alpha\epsilon^{2}}\ge\frac{\Delta}{16\gamma B}\,\epsilon^{-3}
$$

- **下界，大步长分支** $\alpha\gt B\epsilon$：GPT Pro 这份证明给出实例，所有迭代的残差都大于 $\epsilon$，算法永远到不了 $\epsilon$-KKT 点。

适用范围有两条限制：

1. 结论只覆盖 $s=c_s/\epsilon$，其余参数为与 $\epsilon$ 无关的常数，且 $\epsilon\lt\epsilon_0$。$s$ 取其他阶时的下界没有证。
2. 论文正文还没同步这个结论，大步长分支的证明也还没存进仓库。

---

## User (2026-11-11 19:16)

我觉得 我们可能需要用alm的语言重新写一下算法？ 这四个步骤实际上是？

---

## Assistant (2026-11-11 19:17)

老大，对分裂问题 $\min f(\mathbf{x})+h(\mathbf{y})$，约束 $\mathcal{A}(\mathbf{x})=\mathbf{y}$，这四步是**带乘子外推和乘子衰减的线性化邻近 ALM**：$\mathbf{y}$ 精确极小化，$\mathbf{x}$ 走一步线性化邻近梯度步，乘子按约束残差上升。

**1. 乘子外推**

$$
\bar{\boldsymbol{\lambda}}^{k}=\boldsymbol{\lambda}^k+\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}\left(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1}\right)
$$

**2. 原始步**：先对 $\mathbf{y}$ 精确极小化增广 Lagrange 函数，再对 $\mathbf{x}$ 走一步梯度步，邻近中心为 $\mathbf{z}^k$。

$$
\bar{\mathbf{y}}^{k}=\mathrm{prox}_{h/\rho}\left(\mathcal{A}(\mathbf{x}^k)+\frac{\bar{\boldsymbol{\lambda}}^{k}}{\rho}\right)
$$

$$
\mathbf{x}^{k+1}=\mathbf{x}^k-\eta\left[\nabla f(\mathbf{x}^k)+\nabla\mathcal{A}(\mathbf{x}^k)^{\top}\left(\bar{\boldsymbol{\lambda}}^{k}+\rho\left(\mathcal{A}(\mathbf{x}^k)-\bar{\mathbf{y}}^{k}\right)\right)+\frac{\mathbf{x}^k-\mathbf{z}^k}{\gamma}\right]
$$

定理条件取 $\eta=\gamma$，此时 $\mathbf{x}$ 步化为下式，即线性化的邻近 ALM 子问题的精确解。

$$
\mathbf{x}^{k+1}=\mathbf{z}^k-\gamma\,\nabla_{\mathbf{x}}\mathcal{D}_\rho(\mathbf{x}^k,\bar{\boldsymbol{\lambda}}^{k})
$$

**3. 乘子步**：在新的 $\mathbf{x}^{k+1}$ 处重新极小化 $\mathbf{y}$，再按约束残差更新乘子。

$$
\mathbf{y}^{k+1}=\mathrm{prox}_{h/\rho}\left(\mathcal{A}(\mathbf{x}^{k+1})+\frac{\bar{\boldsymbol{\lambda}}^{k}}{\rho}\right)
$$

$$
\boldsymbol{\lambda}^{k+1}=\left(1-\frac{\tau}{s}\right)\bar{\boldsymbol{\lambda}}^{k}+\tau\left(\mathcal{A}(\mathbf{x}^{k+1})-\mathbf{y}^{k+1}\right)
$$

第二项是经典 ALM 的乘子更新，步长为 $\tau$。因子 $1-\tau/s$ 来自对偶正则项，它把乘子向零衰减。

**4. 邻近中心更新**

$$
\mathbf{z}^{k+1}=\mathbf{z}^k+\alpha\left(\mathbf{x}^{k+1}-\mathbf{z}^k\right)
$$

去掉外推并令 $s=\infty$，这四步就是单循环的线性化邻近 ALM。两次 prox 对应每步两次 $\mathcal{O}_h$ 调用，与 $3K+1$ 的计数一致。

---

## User (2026-11-11 19:21)

这个是不是可以起一个名字

---

## Assistant (2026-11-11 19:21)

老大，可以，我建议叫 **LRALM-E**，全称 LRALM with multiplier extrapolation。

- **沿用族名**：它是 LRALM 取 $\beta=0$ 再加一步乘子外推，名字直接显示这层关系，读者不用记新缩写。
- **用 multiplier extrapolation**：这是 ALM 文献的说法，和上一条改写算法的语言一致；现在标题里的 dual extrapolation 是 minimax 文献的说法。
- **不建议叫 accelerated LRALM**：accelerated 在 ALM 文献里多指凸问题的 $O(1/k^2)$ 方法（如 Xu 2017），容易让人误读成原始变量也加了动量。复杂度从 $\epsilon^{-3}$ 降到 $\epsilon^{-5/2}$ 这件事放在定理和正文里说。

全稿里 `LRALM-E` 目前没有被占用的记号冲突需要你确认后我再检索替换。

---

## User (2026-11-11 19:22)

但是我们是跳出的算法族了

---

## Assistant (2026-11-11 19:22)

老大，你说得对：在本文里 $\mathrm{LRALM}_{\theta,\alpha,\beta}$ 专指族 $\mathcal{C}_\theta$ 的成员，后缀式的 LRALM-E 会被读成族内的一个参数选择。我上一条说「名字直接显示这层关系」，错在没有区分「由 LRALM 修改得到」和「属于族」。

这一点对论文的论证有实际影响：族内 $\Theta(\epsilon^{-3})$ 已经紧，$\epsilon^{-5/2}$ 能成立的原因正是 $\boldsymbol{\lambda}^{k+1}$ 依赖 $\boldsymbol{\lambda}^{k-1}$，更新不再是族内的形式。名字应当让读者看出这是族外的方法。

我的建议改为 **Extrapolated LRALM，缩写 ELRALM**：

- 修饰词放在前面，作为一个独立的方法名，不带族的参数下标。
- 保留 LRALM 词根，说明它只比族内 $\beta=0$ 的方法多一步乘子外推，「最小改动即突破族内下界」这个卖点能保住。
- 算法首次出现时加一句：ELRALM does not belong to $\mathcal{C}_\theta$，原因是乘子步用到 $\boldsymbol{\lambda}^{k-1}$。

如果你想让它和族完全脱钩，备选是 **EPALM**，即 extrapolated proximal ALM，代价是读者看不出它和 LRALM 的关系，我不推荐。

---

## User (2026-11-11 19:22)

这个是动量类的 Fast LRALM?

---

## Assistant (2026-11-11 19:22)

老大，可以，**Fast LRALM 比我提的 ELRALM 好**。

- **有先例**：FISTA 是 ISTA 加 Nesterov 动量，Fast ADMM（Goldstein et al. 2014）是 ADMM 加 Nesterov 动量，Boț 的 fast OGDA 也是这个命名方式。读者看到 Fast 就会预期「原方法加动量、复杂度阶改进」，和我们的情况一致。
- **名副其实**：复杂度从 $\epsilon^{-3}$ 降到 $\epsilon^{-5/2}$，阶有改进。
- **读作独立方法**：Fast LRALM 不带族的参数下标，不会被当成 $\mathcal{C}_\theta$ 的成员。

两处要在正文交代清楚：动量只加在乘子上，原始变量没有动量；该方法不属于 $\mathcal{C}_\theta$。缩写建议直接写 Fast LRALM，不再压成 FLRALM。

---

## User (2026-11-11 19:22)

我们其中名字把

---

## User (2026-11-11 19:46)

我们现在的证明 关于乘子有界性 乍一看感觉像是工科思路：这个 难道不能找一些优化的文章 看看人家的思路吗？ 比如反证法？ 这个是工科思路啊？先纵观全局。让告诉我第一步是？ 

我会针对“惯性/加速乘子迭代的有界性证明”查优化文献，重点区分反证法与稳定性、Lyapunov 或递推核估计各自适用的场景。

可以，**应先看优化文献常用的有界性证明，再选我们这条递推最合适的写法**。惯性近端与加速算法的分析常用 Lyapunov 函数或 quasi-Fejér 估计；例如 Alvarez–Attouch（2001）的惯性近端方法，以及 Attouch–Peypouquet–Redont（2014）的惯性 forward-backward 方法。反证法本身通常不是关键，关键是先找到能排除“首次越界”的势函数或不变量。
第一步先**核对文献中相近的惯性/加速算法如何证明迭代有界**：区分投影不变集、Lyapunov/准 Fejér 分析和递推特征根分析，再判断哪种证明框架适用于我们的无投影乘子递推。  目前用的是一些其他什么脉冲手段很奇怪
对我们的递推，直接用范数做“首次越界”估计会得到

$$
\|\boldsymbol\lambda^{k+1}\|
\le a(1+2\theta)\,R+bL_h,
$$

其中 $R$ 是假设的越界阈值。所需参数区间内，尤其 $s$ 较大时，$a(1+2\theta)$ 可以大于 $1$，所以这个估计不能闭合首次越界反证。**反证法可以使用，但需要先构造更强的不变量；仅对原递推取范数不够。**

目前已有的直接相关工作使用了投影或 Lyapunov 分析，不能直接给出我们这个无投影乘子递推的证明模板。对当前 B2′，更贴合结构的做法是代入指定的 Nesterov 系数，直接估计二阶递推的复根及其脉冲响应；这比对任意外推系数做三分情形更短。

---

## Assistant (2026-11-11 19:48)

老大，**第一步是一个结构性事实，不必先查文献**：对偶函数关于乘子等于一个强凹二次函数加一个 Lipschitz 项，且 Lipschitz 常数与 $\mathbf{x}$ 无关。有了它，有界性用一个二次 Lyapunov 函数五行证完，现在的脉冲响应和三分情形都可以删掉。

## 第一步：结构

由 `lem:effective-penalty` 的对偶光滑化表示，

$$
\nabla_{\boldsymbol{\lambda}}\mathcal{D}_\rho(\mathbf{x},\boldsymbol{\lambda})=\frac{\mathbf{q}(\mathbf{x},\boldsymbol{\lambda})-\boldsymbol{\lambda}}{\rho},\qquad \lVert\mathbf{q}(\mathbf{x},\boldsymbol{\lambda})\rVert\le L_h .
$$

因此乘子步是带有界扰动的惯性迭代，$\mathbf{x}$ 只通过 $\mathbf{q}^k$ 进入：

$$
\boldsymbol{\lambda}^{k+1}=a(1+\theta)\boldsymbol{\lambda}^k-a\theta\boldsymbol{\lambda}^{k-1}+\frac{\tau}{\rho}\mathbf{q}^k,\qquad a=1-\frac{\tau}{\rho}-\frac{\tau}{s}.
$$

## 第二步：Lyapunov 函数

记 $p=a(1+\theta)/2$。代入 Nesterov 系数后有恒等式

$$
\sigma^2:=a\theta-p^2=a\theta\cdot\frac{\tau/\rho}{1-\tau/s}\gt 0 .
$$

所以特征根恒为复根，三分情形只剩一种。定义

$$
E_k:=\lVert\boldsymbol{\lambda}^k-p\boldsymbol{\lambda}^{k-1}\rVert^2+\sigma^2\lVert\boldsymbol{\lambda}^{k-1}\rVert^2 .
$$

直接展开得到带扰动的压缩：

$$
\sqrt{E_{k+1}}\le\sqrt{a\theta}\,\sqrt{E_k}+\frac{\tau}{\rho}L_h .
$$

## 第三步：结论

由 $E_0=0$ 得 $\sqrt{E_k}\le(\tau/\rho)L_h/(1-\sqrt{a\theta})$，再用 $\lVert\boldsymbol{\lambda}^{k-1}\rVert\le\sqrt{E_k}/\sigma$。在 $\tau\le\rho/4$、$s\ge4\tau$ 下得到

$$
\lVert\boldsymbol{\lambda}^k\rVert\le 2\sqrt{6}\sqrt{\frac{\rho}{\tau}}\,L_h ,
$$

与 $s$ 无关，阶与现有 $C_\lambda$ 相同，常数从 $2\sqrt2$ 变为 $2\sqrt6$。

## 对你贴的那段回复的判断

- **反证法用不上**。它自己也算出单步范数估计不闭合；需要的是上面的 $E_k$，有了 $E_k$ 直接递推即可。
- **「先查文献」可以省**。这种「二次能量加扰动压缩」的写法就是 heavy-ball 类分析的标准形式，Polyak (1964) 和 Alvarez–Attouch (2001) 都是这个风格，引用它们作为出处即可。

以上是我手推的结果，代数恒等式逐项核过，还没有数值验证，也还没有写进 Acceleration.tex。

---

## User (2026-11-11 19:48)

这里的技巧是 **“把二阶递推看成一个稳定的线性系统，用脉冲响应的绝对和控制有界输入产生的输出”**。你觉得它和原先想法不同，是因为它没有直接对乘子序列做能量估计，而是先分析了递推的特征根。

具体来说，你指出的这一步只是为了**区分特征根是实根还是复根**，不是额外引入一个假设。

### 1. 为什么写成 \(u=1-\theta\)？

我们有
\[
p(\zeta)=\zeta^2-a(1+\theta)\zeta+a\theta,
\qquad a=1-\nu.
\]
判别式为
\[
\Delta=a^2(1+\theta)^2-4a\theta
=-a\bigl[4\theta-a(1+\theta)^2\bigr].
\]
因为 \(a>0\)，所以判别式与方括号内的量符号相反。

令 \(u=1-\theta\)，则
\[
\begin{aligned}
4\theta-a(1+\theta)^2
&=4(1-u)-(1-\nu)(2-u)^2\\
&=\nu(2-u)^2-u^2.
\end{aligned}
\]
**这样改写，是为了显露 \(1-\theta\) 与 \(\sqrt{\nu}\) 两个尺度之间的比较。** 根的性质恰好由
\[
\nu(2-u)^2\quad\text{与}\quad u^2
\]
谁大决定。

### 2. 为什么需要区分实根与复根？

因为我们最终要控制的不是普通求和，而是
\[
\|c\|_1=\sum_{j\ge0}|c_j|.
\]

- **实根情形：** 两个根都在 \([0,1)\)，从而 \(c_j\ge0\)。绝对值可以去掉，直接得到
  \[
  \sum_{j\ge0}|c_j|=\sum_{j\ge0}c_j=\frac1{p(1)}=\frac1\nu.
  \]

- **复根情形：** \(c_j\) 可能振荡、变号。此时即使
  \[
  \sum_{j\ge0}c_j=\frac1\nu,
  \]
  也不能据此控制 \(\sum_{j\ge0}|c_j|\)，因为普通求和存在正负抵消。

  写成 \(\zeta_{1,2}=Re^{\pm i\phi}\)，就有
  \[
  c_j=R^j\frac{\sin((j+1)\phi)}{\sin\phi}.
  \]
  于是可以使用两种互补的估计：
  \[
  |c_j|\le(j+1)R^j,
  \qquad
  |c_j|\le\frac{R^j}{\sin\phi}.
  \]
  第一种不怕 \(\phi\) 很小；第二种在 \(\sin\phi\) 有下界时更有效。原证明的三种情况，就是为了选择适用的估计。

### 3. 但你的感觉有道理：对我们这个具体的 \(\theta\)，三分类其实可以省掉

**原证明证明了一个比当前需要更一般的结论——它允许 \(\theta\) 自由变化。** 但我们的 \(\theta\) 已经由 \(s,\tau\) 指定，利用这个特殊结构，证明会更直接。

令
\[
t:=\sqrt{\tau/s}\in(0,1/2].
\]
则
\[
\theta=\frac{1-t}{1+t},
\qquad
\nu=\frac{\tau}{\rho}+t^2.
\]
直接代入可得
\[
\boxed{
4\theta-a(1+\theta)^2
=\frac{4(\nu-t^2)}{(1+t)^2}
=\frac{4\tau/\rho}{(1+t)^2}>0.
}
\]
所以，**本引理中的特征根始终是复根，根本不需要讨论实根情形。**

进一步，令 \(b=\tau/\rho\)，则
\[
\sin^2\phi
=\frac{4\theta-a(1+\theta)^2}{4\theta}
=\frac{b}{1-t^2}
\ge b.
\]
同时
\[
R=\sqrt{a\theta}\le\sqrt a,
\qquad
1-R\ge\frac{\nu}{2}.
\]
于是直接得到
\[
\|c\|_1
\le\frac1{(1-R)\sin\phi}
\le\frac{2}{\nu\sqrt b}.
\]
代回乘子估计：
\[
\boxed{
\|\boldsymbol\lambda^k\|
\le bL_h\|c\|_1
\le\frac{2\sqrt b}{\nu}L_h
\le\frac2{\sqrt b}L_h
=2\sqrt{\frac{\rho}{\tau}}\,L_h.
}
\]
这个界还比前面使用的 \(2\sqrt2\sqrt{\rho/\tau}\,L_h\) 更紧。

**因此，区别在于：前面的证明采用了“任意外推系数下的通用递推估计”；针对当前引理，更推荐“代入指定的外推系数，直接估计复根”的证明，不必做三分类。** 如果你原本想的是直接从更新式构造 Lyapunov 函数、做能量估计，那确实是另一条路线；不能把这两种思路混为一谈。 这个和你的思路一样，

---

## Assistant (2026-11-11 19:49)

老大，**数学内容相同，写法不同**：两边用的是同一个事实，即代入 Nesterov 系数后特征根恒为复根；它用脉冲响应的 $\ell_1$ 和表述，我用二次 Lyapunov 函数表述。

**对应关系。** 我的 $E_k$ 就是它的复根写法的模平方。记复根为 $\zeta=Re^{\mathrm{i}\phi}$，则

$$
E_k=\lVert\boldsymbol{\lambda}^k-\zeta\boldsymbol{\lambda}^{k-1}\rVert^2,\qquad p=R\cos\phi,\quad \sigma=R\sin\phi .
$$

它的 $\sin^2\phi=b/(1-t^2)$ 与我的 $\sigma^2=a\theta\cdot(\tau/\rho)/(1-\tau/s)$ 是同一个恒等式。

**常数。** 它的 $2\sqrt{\rho/\tau}\,L_h$ 我核过，成立。我上一条的 $2\sqrt6$ 偏松，原因是最后一步用了 $\lVert\boldsymbol{\lambda}^{k-1}\rVert\le\sqrt{E_k}/\sigma$，多出一个 $1/R$。改用 Cauchy–Schwarz 不等式

$$
\sigma\lVert\boldsymbol{\lambda}^k\rVert\le\sqrt{p^2+\sigma^2}\,\sqrt{E_k}=R\sqrt{E_k}
$$

就得到同样的界：

$$
\lVert\boldsymbol{\lambda}^k\rVert\le\frac{\sqrt{E_k}}{\sin\phi}\le\frac{(\tau/\rho)L_h}{(1-R)\sin\phi}\le 2\sqrt{\frac{\rho}{\tau}}\,L_h .
$$

**写进论文我推荐 Lyapunov 写法。** 它只出现实数量 $p$、$\sigma$、$E_k$ 和一条压缩不等式，不需要特征根、三角函数和脉冲响应序列 $c_j$，篇幅更短，也与后面 $\mathcal{W}_k$ 的分析风格一致。引理中的常数可以相应改为 $C_\lambda=2\sqrt{\rho/\tau}$。

---

## User (2026-11-11 19:49)

吗

我们是否真的需要先引入势函数 所以你依赖于构造的势函数？

---

## Assistant (2026-11-11 19:49)

老大，**不需要**。证明只依赖递推本身，$E_k$ 只是一个换元后的范数，写法上可以完全不提「势函数」。

**换元写法。** 令

$$
\mathbf{A}^k:=\boldsymbol{\lambda}^k-p\boldsymbol{\lambda}^{k-1},\qquad \mathbf{B}^k:=\sigma\boldsymbol{\lambda}^{k-1}.
$$

乘子递推等价于

$$
\mathbf{A}^{k+1}=p\mathbf{A}^k-\sigma\mathbf{B}^k+\frac{\tau}{\rho}\mathbf{q}^k,\qquad \mathbf{B}^{k+1}=\sigma\mathbf{A}^k+p\mathbf{B}^k .
$$

齐次部分把 $(\mathbf{A}^k,\mathbf{B}^k)$ 的范数恰好乘以 $\sqrt{p^2+\sigma^2}=\sqrt{a\theta}$，再用三角不等式和 $\lVert\mathbf{q}^k\rVert\le L_h$ 就结束。$E_k$ 就是 $\lVert\mathbf{A}^k\rVert^2+\lVert\mathbf{B}^k\rVert^2$。

**两点说明。**

- 这个换元由递推唯一确定：特征多项式配方为 $(\zeta-p)^2+\sigma^2$，$p$ 和 $\sigma$ 直接读出，没有待定参数，也没有猜测的成分。
- 某个同时含 $\boldsymbol{\lambda}^k$ 和 $\boldsymbol{\lambda}^{k-1}$ 的量是避不开的。只对 $\lVert\boldsymbol{\lambda}^k\rVert$ 做单步归纳时系数是 $a(1+2\theta)$，它可以大于 $1$，归纳不闭合。

它与论文的 $\mathcal{P}_s$、$\mathcal{W}_k$ 无关，有界性引理可以放在这些定义之前，独立成立。

---

## User (2026-11-11 19:49)

老大，这是引理 6.1 的完整证明（来自 `b2-G0G1-20261109.md` 的 G1 部分），核心是用二阶线性递推的脉冲响应 $\ell_1$ 范数控制乘子：

### Proof of Lemma 6.1

Let $\nu := \tau(1/\rho + 1/s)$, $a := 1 - \nu$, $b := \tau/\rho$, and denote the extrapolation coefficient by

$$
\theta := \frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}} \in [0, 1).
$$

Since $0 < \tau \le \rho/4$ and $s \ge 4\tau$, we have $0 < \nu \le 1/2$ and $a \in [1/2, 1)$.

**Step 1: Second-order linear recursion.**
With $\mathbf{q}^k = \mathbf{q}(\mathbf{x}^{k+1}, \bar{\boldsymbol{\lambda}}^k)$, the gradient expression $\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x}^{k+1}, \bar{\boldsymbol{\lambda}}^k; \mathbf{z}^k, \mathbf{0}) = (\mathbf{q}^k - \bar{\boldsymbol{\lambda}}^k)/\rho - \bar{\boldsymbol{\lambda}}^k/s$ turns the dual update into

$$
\boldsymbol{\lambda}^{k+1} = a\bar{\boldsymbol{\lambda}}^k + b\mathbf{q}^k = a(1+\theta)\boldsymbol{\lambda}^k - a\theta\boldsymbol{\lambda}^{k-1} + b\mathbf{q}^k.
$$

By Assumption 2.2 and $\mathbf{q}^k \in \partial h(\mathbf{y}^{k+1})$, we have $\lVert \mathbf{q}^k \rVert \le L_h$ for all $k \ge 0$. Since $\boldsymbol{\lambda}^{-1} = \boldsymbol{\lambda}^0 = \mathbf{0}$, unrolling this constant-coefficient linear recursion yields

$$
\boldsymbol{\lambda}^k = b \sum_{i=0}^{k-1} c_{k-1-i} \mathbf{q}^i,
$$

where the scalar impulse response $\{c_j\}_{j \ge 0}$ satisfies $c_{-1} = 0$, $c_0 = 1$, and $c_j = a(1+\theta)c_{j-1} - a\theta c_{j-2}$ for $j \ge 1$. Taking norms gives

$$
\lVert \boldsymbol{\lambda}^k \rVert \le b L_h \sum_{j=0}^{\infty} \lvert c_j \rvert = b L_h \lVert c \rVert_1.
$$

**Step 2: $\ell_1$ bound on the impulse response.**
The characteristic polynomial of $\{c_j\}$ is $P(r) = r^2 - a(1+\theta)r + a\theta$ with discriminant $\Delta_P = a^2(1+\theta)^2 - 4a\theta$. Write $u := 1 - \theta \in (0, 1]$. We bound $\lVert c \rVert_1$ across three cases:

1. **Nonnegative real roots ($\Delta_P \ge 0$).** Both roots lie in $[0, 1)$, so $c_j \ge 0$ for all $j \ge 0$. Thus

$$
\lVert c \rVert_1 = \sum_{j=0}^{\infty} c_j = \frac{1}{P(1)} = \frac{1}{(1-a)(1-\theta)} \ge \frac{1}{\nu}.
$$

Wait—when $\Delta_P \ge 0$, we have $4a(1-u) \le a^2(2-u)^2$, which implies $\nu(2-u)^2 \le u^2$. Since $2-u \ge 1$, this forces $u \ge \sqrt{\nu}$. The root modulus is bounded by the larger root $r_+ \le 1 - \nu/2$, or more directly, whenever $\Delta_P \ge 0$, $c_j \ge 0$ gives $\lVert c \rVert_1 = \frac{1}{\nu u} \le \frac{1}{\nu^{3/2}}$. (More tajamly: if $a(1+\theta)^2 \ge 4\theta$, then $P(1) = \nu u$; since $\Delta_P \ge 0 \implies u \ge \sqrt{\nu}$ is false for small $\nu$, let us use the exact root split from G1.3 below.)

*(Exact three-case split from Lemma G1.3)*:
- **Case (a): $\Delta_P \ge 0$ and $u \ge 1/2$.** Since $c_j \ge 0$, $\lVert c \rVert_1 = \frac{1}{P(1)} = \frac{1}{\nu u} \le \frac{2}{\nu} \le \frac{4}{\nu}$.
- **Case (b): $\Delta_P \ge 0$ and $\sqrt{\nu} < u < 1/2$.** Both roots are real and positive, bounded by $R := \sqrt{a(1+\theta)/2}$... 

---

老大，上面 Step 2 的 Case (b) 我先把原文 `b2-G0G1-20261109.md` 第 170–225 行的精确放缩核对一下，把完全对齐的 LaTeX 证明直接给你：”]

老大，上面 Step 2 的 Case (a) 我刚才手写时把 $p(1)$ 写成了 $\nu u$，实际特征多项式在 $1$ 处的值是 $p(1)=1-a(1+\theta)+a\theta=1-a=\nu$。下面给出与 `b2-G0G1-20261109.md` 完全一致、可直接放入论文的完整证明（含渲染版与 LaTeX 源码）：

### 渲染版

*Proof of Lemma 6.1.* Let $\nu := \tau(1/\rho + 1/s)$, $a := 1 - \nu$, $b := \tau/\rho$, and denote the extrapolation coefficient by

$$
\theta := \frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}} \in [0, 1).
$$

Since $0 < \tau \le \rho/4$ and $s \ge 4\tau$, we have $0 < \nu \le 1/2$ and $a \in [1/2, 1)$.

**Step 1: Second-order linear recursion.**
By the dual gradient identity $\nabla_{\boldsymbol{\lambda}}\mathcal{P}_s(\mathbf{x}^{k+1}, \bar{\boldsymbol{\lambda}}^k; \mathbf{z}^k, \mathbf{0}) = (\mathbf{q}^k - \bar{\boldsymbol{\lambda}}^k)/\rho - \bar{\boldsymbol{\lambda}}^k/s$, the dual update reads

$$
\boldsymbol{\lambda}^{k+1} = a\bar{\boldsymbol{\lambda}}^k + b\mathbf{q}^k = a(1+\theta)\boldsymbol{\lambda}^k - a\theta\boldsymbol{\lambda}^{k-1} + b\mathbf{q}^k.
$$

Since $\mathbf{q}^k \in \partial h(\mathbf{y}^{k+1})$, Assumption 2.2 gives $\lVert \mathbf{q}^k \rVert \le L_h$. Define the scalar impulse response $\{c_j\}_{j \ge -1}$ by $c_{-1} := 0$, $c_0 := 1$, and $c_{j+1} := a(1+\theta)c_j - a\theta c_{j-1}$ for $j \ge 0$. Let $\zeta_1, \zeta_2$ be the roots of $p(\zeta) := \zeta^2 - a(1+\theta)\zeta + a\theta$. Then $c_j = \sum_{i=0}^j \zeta_1^i \zeta_2^{j-i}$, and induction from $\boldsymbol{\lambda}^{-1} = \boldsymbol{\lambda}^0 = \mathbf{0}$ yields

$$
\boldsymbol{\lambda}^k = b \sum_{i=0}^{k-1} c_{k-1-i} \mathbf{q}^i, \qquad \lVert \boldsymbol{\lambda}^k \rVert \le b L_h \sum_{j=0}^{k-1} \lvert c_j \rvert \le b L_h \lVert c \rVert_1.
$$

**Step 2: $\ell_1$ bound on the impulse response.**
Write $u := 1 - \theta \in (0, 1]$. Since $a > 0$, the discriminant of $p(\zeta)$ has the opposite sign of

$$
4\theta - a(1+\theta)^2 = \nu(2-u)^2 - u^2.
$$

We partition $u \in (0, 1]$ into three disjoint cases:
1. **Case (a): $\nu(2-u)^2 \le u^2$.** The roots $\zeta_1, \zeta_2$ are real with sum $a(1+\theta) > 0$ and product $a\theta \ge 0$, and $p(1) = 1 - a = \nu > 0$ with vertex $a(1+\theta)/2 \le a < 1$. Thus $\zeta_1, \zeta_2 \in [0, 1)$, so $c_j \ge 0$ and

$$
\lVert c \rVert_1 = \sum_{j=0}^\infty c_j = \frac{1}{(1-\zeta_1)(1-\zeta_2)} = \frac{1}{p(1)} = \frac{1}{\nu}.
$$

2. **Case (b): $\nu(2-u)^2 > u^2$ and $u > \sqrt{\nu}$.** The roots are complex conjugates $\zeta_{1,2} = R e^{\pm \mathrm{i}\phi}$ with $R = \sqrt{a\theta}$ and $\phi \in (0, \pi/2)$. Since $1 - R^2 = 1 - (1-\nu)(1-u) = u + \nu(1-u) \ge u$, we have $1 - R \ge (1 - R^2)/2 \ge u/2 > \sqrt{\nu}/2$. Using $\lvert c_j \rvert \le (j+1)R^j$ gives

$$
\lVert c \rVert_1 \le \sum_{j=0}^\infty (j+1)R^j = \frac{1}{(1-R)^2} < \frac{4}{\nu}.
$$

3. **Case (c): $u \le \sqrt{\nu}$.** Since $\nu < 1$, we have $\nu(2-u)^2 - u^2 \ge \nu(1-u)(3-u) > 0$, so the roots are again $R e^{\pm \mathrm{i}\phi}$. From $\cos^2\phi = a(1+\theta)^2/(4\theta)$, we obtain

$$
\sin^2\phi = \frac{\nu(2-u)^2 - u^2}{4(1-u)} \ge \frac{\nu(3-u)}{4} \ge \frac{\nu}{2}.
$$

Moreover, $R \le \sqrt{a}$ implies $1 - R \ge 1 - \sqrt{a} = \nu/(1+\sqrt{a}) \ge \nu/2$. Using $c_j = R^j \sin((j+1)\phi)/\sin\phi$ gives

$$
\lVert c \rVert_1 \le \frac{1}{(1-R)\sin\phi} \le \frac{2}{\nu}\sqrt{\frac{2}{\nu}} = 2\sqrt{2}\,\nu^{-3/2}.
$$

**Step 3: Uniform multiplier bounds.**
Combining the three cases with $b = \tau/\rho = \nu s / (\rho + s) \le \nu$ and $\nu \ge \tau/\rho$ yields

$$
\lVert \boldsymbol{\lambda}^k \rVert \le b L_h \lVert c \rVert_1 \le \frac{s}{\rho+s}\nu \max\left\{\frac{4}{\nu}, \frac{2\sqrt{2}}{\nu^{3/2}}\right\} L_h \le \max\left\{4, 2\sqrt{2}\sqrt{\frac{\rho}{\tau}}\right\} L_h = C_\lambda L_h.
$$

Finally, since $\theta \in [0, 1)$, the triangle inequality gives $\lVert \bar{\boldsymbol{\lambda}}^k \rVert \le (1+\theta)\lVert \boldsymbol{\lambda}^k \rVert + \theta\lVert \boldsymbol{\lambda}^{k-1} \rVert \le 3 C_\lambda L_h$. $\square$

---

### LaTeX 源码

```latex
\begin{proof}[Proof of Lemma~\ref{lem:b2-prime-multiplier-bounds}]
Let \(\nu:=\tau(1/\rho+1/s)\), \(a:=1-\nu\), \(b:=\tau/\rho\), and denote the
extrapolation coefficient by
\(\theta:=(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})\in[0,1)\). Since
\(0<\tau\le\rho/4\) and \(s\ge4\tau\), we have \(0<\nu\le1/2\) and
\(a\in[1/2,1)\).

By~\eqref{eq:prox-multiplier},
\(\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
=(\bq^k-\bar{\blmbd}^k)/\rho-\bar{\blmbd}^k/s\), so the dual update reads
\[
    \blmbd^{k+1}
    =a\bar{\blmbd}^k+b\bq^k
    =a(1+\theta)\blmbd^k-a\theta\blmbd^{k-1}+b\bq^k,
    \qquad \|\bq^k\|\le L_h.
\]
Define \(c_{-1}:=0\), \(c_0:=1\), and
\(c_{j+1}:=a(1+\theta)c_j-a\theta c_{j-1}\) for \(j\ge0\). If
\(\zeta_1,\zeta_2\) are the roots of
\(p(\zeta):=\zeta^2-a(1+\theta)\zeta+a\theta\), then
\(c_j=\sum_{i=0}^j\zeta_1^i\zeta_2^{j-i}\). Induction from
\(\blmbd^{-1}=\blmbd^0=\zero\) gives
\[
    \blmbd^k=b\sum_{i=0}^{k-1}c_{k-1-i}\bq^i,
    \qquad
    \|\blmbd^k\|\le bL_h\sum_{j=0}^{k-1}|c_j|\le bL_h\|c\|_1.
\]

Write \(u:=1-\theta\in(0,1]\). Since \(a>0\) and
\(4\theta-a(1+\theta)^2=\nu(2-u)^2-u^2\), three cases arise:
\begin{enumerate}[label=(\alph*)]
\item If \(\nu(2-u)^2\le u^2\), the roots \(\zeta_1,\zeta_2\) are real and lie
in \([0,1)\) because \(\zeta_1+\zeta_2=a(1+\theta)>0\),
\(\zeta_1\zeta_2=a\theta\ge0\), \(a(1+\theta)/2<1\), and \(p(1)=\nu>0\). Thus
\(c_j\ge0\) and
\(\|c\|_1=\sum_{j\ge0}c_j=1/p(1)=1/\nu\).
\item If \(\nu(2-u)^2>u^2\) and \(u>\sqrt{\nu}\), the roots are
\(Re^{\pm\mathrm i\phi}\) with \(R=\sqrt{a\theta}\) and
\(\phi\in(0,\pi/2)\). Then
\(1-R\ge(1-R^2)/2=(u+\nu(1-u))/2\ge u/2>\sqrt{\nu}/2\), and
\(|c_j|\le(j+1)R^j\) yields
\(\|c\|_1\le(1-R)^{-2}<4/\nu\).
\item If \(u\le\sqrt{\nu}\), then
\(\nu(2-u)^2-u^2\ge\nu(1-u)(3-u)>0\), so the roots are again
\(Re^{\pm\mathrm i\phi}\). From
\(\cos^2\phi=a(1+\theta)^2/(4\theta)\), we have
\[
    \sin^2\phi=\frac{\nu(2-u)^2-u^2}{4(1-u)}
    \ge\frac{\nu(3-u)}{4}\ge\frac{\nu}{2},
    \qquad
    1-R\ge1-\sqrt{a}=\frac{\nu}{1+\sqrt{a}}\ge\frac{\nu}{2}.
\]
Using \(c_j=R^j\sin((j+1)\phi)/\sin\phi\) gives
\(\|c\|_1\le((1-R)\sin\phi)^{-1}\le2\sqrt{2}\,\nu^{-3/2}\).
\end{enumerate}

Since \(b=\tau/\rho=\nu s/(\rho+s)\le\nu\) and \(\nu\ge\tau/\rho\), combining
the three cases gives
\[
    \|\blmbd^k\|
    \le bL_h\|c\|_1
    \le \frac{s}{\rho+s}\nu
        \max\left\{\frac{4}{\nu},\frac{2\sqrt{2}}{\nu^{3/2}}\right\}L_h
    \le C_\lambda L_h.
\]
Finally, \(\|\bar{\blmbd}^k\|\le(1+\theta)\|\blmbd^k\|
+\theta\|\blmbd^{k-1}\|\le3C_\lambda L_h\).
\end{proof}
```

你要把这个证明直接放进 `Acceleration.tex` 的 Lemma 6.1 后面，还是新建附录 `appendix/AccelerationProof.tex` 放进去？

---

## Assistant (2026-11-11 19:50)

老大，这份是旧的三分情形证明，推导正确，但**不建议放进论文**：我们的 $\theta$ 是固定的 Nesterov 系数，情形 (a)(b) 永远不会出现，脉冲响应序列 $c_j$ 也用不上。

换元证明只有十几行，得到的界是 $2\sqrt{\rho/\tau}\,L_h$。由 $\tau\le\rho/4$ 知它不超过现有的 $C_\lambda L_h$，所以**引理 6.1 的陈述不用改**，证明直接跟在引理后面，不必另开附录。

```latex
\begin{proof}
Let \(a:=1-\tau/\rho-\tau/s\) and
\(\theta:=(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})\). Since
\(\tau\le\rho/4\) and \(s\ge4\tau\), we have \(a\in[1/2,1)\) and
\(\theta\in[1/3,1)\). By~\eqref{eq:prox-multiplier},
\(\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
=(\bq^k-\bar{\blmbd}^k)/\rho-\bar{\blmbd}^k/s\) with
\(\bq^k:=\bq(\bx^{k+1},\bar{\blmbd}^k)\in\partial h(\by^{k+1})\), so
\(\|\bq^k\|\le L_h\) by Assumption~\ref{ass:h} and
\begin{equation}
    \blmbd^{k+1}
    =a(1+\theta)\blmbd^k-a\theta\blmbd^{k-1}+\frac{\tau}{\rho}\bq^k .
    \label{eq:multiplier-recursion}
\end{equation}
Let \(p:=a(1+\theta)/2\) and \(\sigma^2:=a\theta-p^2\). Since
\(4\theta/(1+\theta)^2=1-\tau/s\),
\[
    \sigma^2=a\theta\Bigl(1-\frac{a}{1-\tau/s}\Bigr)
    =\frac{a\theta}{1-\tau/s}\cdot\frac{\tau}{\rho}>0 .
\]
Define \(\mathbf d^k:=\blmbd^k-p\blmbd^{k-1}\) and
\(\mathbf e^k:=\sigma\blmbd^{k-1}\). Then
\eqref{eq:multiplier-recursion} reads
\[
    \mathbf d^{k+1}=p\,\mathbf d^k-\sigma\mathbf e^k+\frac{\tau}{\rho}\bq^k,
    \qquad
    \mathbf e^{k+1}=\sigma\mathbf d^k+p\,\mathbf e^k .
\]
Since
\(\|p\,\mathbf d^k-\sigma\mathbf e^k\|^2+\|\sigma\mathbf d^k+p\,\mathbf e^k\|^2
=a\theta(\|\mathbf d^k\|^2+\|\mathbf e^k\|^2)\), the quantity
\(N_k:=(\|\mathbf d^k\|^2+\|\mathbf e^k\|^2)^{1/2}\) satisfies
\[
    N_{k+1}\le\sqrt{a\theta}\,N_k+\frac{\tau}{\rho}L_h .
\]
Because \(N_0=0\) and
\(1-\sqrt{a\theta}\ge1-\sqrt a\ge(1-a)/2\ge\tau/(2\rho)\), we obtain
\(N_k\le2L_h\) for all \(k\ge0\). Finally,
\(\sigma\|\blmbd^k\|=\|\sigma\mathbf d^k+p\,\mathbf e^k\|
\le\sqrt{a\theta}\,N_k\), and therefore
\[
    \|\blmbd^k\|\le\frac{\sqrt{a\theta}}{\sigma}\,2L_h
    =2\sqrt{\frac{\rho}{\tau}\Bigl(1-\frac{\tau}{s}\Bigr)}\,L_h
    \le2\sqrt{\frac{\rho}{\tau}}\,L_h\le C_\lambda L_h .
\]
The bound on \(\bar{\blmbd}^k\) follows from
\(\|\bar{\blmbd}^k\|\le(1+\theta)\|\blmbd^k\|+\theta\|\blmbd^{k-1}\|\).
\end{proof}
```

这份证明是我手推的，每个恒等式都逐项核过，还没有写入 Acceleration.tex，也没有编译。`\mathbf d^k`、`\mathbf e^k`、`N_k`、`p`、`\sigma` 是证明内的局部记号，写入前需要检索全稿确认不冲突。

---

## User (2026-11-11 19:50)

这个是目前的证明

你看下怎么修改 你先输出

---

## Assistant (2026-11-11 19:50)

老大，改动有两处：**引理的常数简化为 $C_\lambda=2\sqrt{\rho/\tau}$**，**附录证明的第 9–75 行整体替换**为换元证明。其余用到 $C_\lambda$ 的地方只引用符号，不用动。

## 改动一：引理陈述

[Acceleration.tex:165](sections/Acceleration.tex#L165) 的常数定义改为下面这行。第 166 行 `\end{lemma}.` 后面多了一个句点，一并删掉。

```latex
\] where the constant \(C_\lambda:=2\sqrt{\rho/\tau}\) is independent of \(s\).
```

## 改动二：证明

[AccelerationProof.tex:9-75](appendix/AccelerationProof.tex#L9-L75) 替换为：

```latex
Let \(a:=1-\tau/\rho-\tau/s\), \(b:=\tau/\rho\), and denote the
extrapolation coefficient by
\(\theta_{\mathrm m}:=(\sqrt{s}-\sqrt{\tau})/(\sqrt{s}+\sqrt{\tau})\).
Since \(0<\tau\le\rho/4\) and \(s\ge4\tau\), we have \(a\in[1/2,1)\) and
\(\theta_{\mathrm m}\in[1/3,1)\).

By~\eqref{eq:prox-multiplier},
\(\nabla_{\blmbd}\mathcal P_s(\bx^{k+1},\bar{\blmbd}^k;\bz^k,\zero)
=(\bq^k-\bar{\blmbd}^k)/\rho-\bar{\blmbd}^k/s\), so the dual update reads
\begin{equation}
    \blmbd^{k+1}
    =a\bar{\blmbd}^k+b\bq^k
    =a(1+\theta_{\mathrm m})\blmbd^k-a\theta_{\mathrm m}\blmbd^{k-1}+b\bq^k,
    \qquad \|\bq^k\|\le L_h,
    \label{eq:b2-prime-multiplier-recursion}
\end{equation}
where the bound on \(\bq^k\in\partial h(\by^{k+1})\) follows from
Assumption~\ref{ass:h}.

Let \(p:=a(1+\theta_{\mathrm m})/2\) and
\(\sigma^2:=a\theta_{\mathrm m}-p^2\). Since
\(4\theta_{\mathrm m}/(1+\theta_{\mathrm m})^2=1-\tau/s\),
\[
    \sigma^2
    =a\theta_{\mathrm m}\Bigl(1-\frac{a}{1-\tau/s}\Bigr)
    =\frac{a\theta_{\mathrm m}\,b}{1-\tau/s}>0 .
\]
Define \(\mathbf d^k:=\blmbd^k-p\blmbd^{k-1}\) and
\(\mathbf e^k:=\sigma\blmbd^{k-1}\) for \(k\ge0\).
Then~\eqref{eq:b2-prime-multiplier-recursion} is equivalent to
\[
    \mathbf d^{k+1}=p\,\mathbf d^k-\sigma\mathbf e^k+b\bq^k,
    \qquad
    \mathbf e^{k+1}=\sigma\mathbf d^k+p\,\mathbf e^k .
\]
Because
\[
    \|p\,\mathbf d^k-\sigma\mathbf e^k\|^2
    +\|\sigma\mathbf d^k+p\,\mathbf e^k\|^2
    =(p^2+\sigma^2)\bigl(\|\mathbf d^k\|^2+\|\mathbf e^k\|^2\bigr)
    =a\theta_{\mathrm m}\bigl(\|\mathbf d^k\|^2+\|\mathbf e^k\|^2\bigr),
\]
the quantity \(N_k:=(\|\mathbf d^k\|^2+\|\mathbf e^k\|^2)^{1/2}\) satisfies
\[
    N_{k+1}\le\sqrt{a\theta_{\mathrm m}}\,N_k+bL_h .
\]
Since \(\blmbd^{-1}=\blmbd^0=\zero\), we have \(N_0=0\). Together with
\(1-\sqrt{a\theta_{\mathrm m}}\ge1-\sqrt a\ge(1-a)/2\ge b/2\), this gives
\(N_k\le2L_h\) for all \(k\ge0\). Moreover,
\(\sigma\blmbd^k=\mathbf e^{k+1}=\sigma\mathbf d^k+p\,\mathbf e^k\) and the
Cauchy--Schwarz inequality give
\(\sigma\|\blmbd^k\|\le\sqrt{a\theta_{\mathrm m}}\,N_k\). Therefore
\[
    \|\blmbd^k\|
    \le\frac{\sqrt{a\theta_{\mathrm m}}}{\sigma}\,2L_h
    =2\sqrt{\frac{\rho}{\tau}\Bigl(1-\frac{\tau}{s}\Bigr)}\,L_h
    \le C_\lambda L_h .
\]
Finally, \(\|\bar{\blmbd}^k\|\le(1+\theta_{\mathrm m})\|\blmbd^k\|
+\theta_{\mathrm m}\|\blmbd^{k-1}\|\le3C_\lambda L_h\).
```

## 核对情况

- 记号 `\mathbf d`、`\mathbf e`、`N_k`、`p`、`\sigma` 在 Acceleration.tex 和 AccelerationProof.tex 里没有被占用；`\theta_{\mathrm m}`、`a`、`b` 沿用现有证明的写法。
- 新常数 $2\sqrt{\rho/\tau}$ 不超过旧常数，定理里的条件 $c_s\ge6C_\lambda L_h$ 和残差界照常成立。
- 证明是手推的，恒等式逐项核过；没有数值验证，没有编译，文件还没有改。
