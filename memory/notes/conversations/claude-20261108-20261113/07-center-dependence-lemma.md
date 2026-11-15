# 07-center-dependence-lemma

- **Source session**: `82cb571a`
- **Span (local time)**: 2026-11-12 17:03 to 2026-11-12 17:07
- **User turns**: 1

---

## User (2026-11-12 17:03)

\begin{lemma}
\label{lem:b2-prime-center-dependence}
Suppose that Assumptions~\ref{ass:smoothness} and~\ref{ass:h} hold. Let
\(\bz,\bz'\in\RR^n\) and \(\blmbd\in\RR^m\). Then
\begin{align*} 我不知道这个是啥意思

---

## Assistant (2026-11-12 17:07)

老大，[AccelerationProof.tex:125-146](overleaf/appendix/AccelerationProof.tex#L125-L146) 给出近端中心从 $\mathbf{z}$ 移到 $\mathbf{z}'$ 时值函数与鞍点映射的灵敏度界，用来控制下一步的中心移动误差和外层值函数下降。

[AccelerationProof.tex:200-211](overleaf/appendix/AccelerationProof.tex#L200-L211) 刚证完的固定中心压缩给出的是旧中心 $\mathbf{z}^k$ 处的收缩：

$$
\mathcal{E}_{k+1}(\mathbf{z}^k) \le (1-\varsigma)\mathcal{E}_k(\mathbf{z}^k) - \frac{1}{66\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2 - \frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2 - \frac{\varsigma\mu_\gamma}{2}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

算法随后将中心更新到 $\mathbf{z}^{k+1}$，下一轮递推进入的是新中心处的内层能量。因此需要固定第 $k+1$ 步的迭代点，估计中心从 $\mathbf{z}$ 变为 $\mathbf{z}'$ 时的能量增量，即上一段交接说明里提到的**中心移动误差**。对照 [AccelerationProof.tex:186-190](overleaf/appendix/AccelerationProof.tex#L186-L190) 中 $\mathcal{E}_k(\mathbf{z})$ 的定义：

$$
\mathcal{E}_k(\mathbf{z}) := p_s(\mathbf{z}) - d_s(\boldsymbol{\lambda}^k;\mathbf{z}) + \frac{1}{2s}\lVert\mathbf{w}^k-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert^2 + \frac{\mu_\gamma}{4}\lVert\mathbf{x}^k-\mathbf{x}_s(\bar{\boldsymbol{\lambda}}^{k-1};\mathbf{z})\rVert^2 + \frac{G_{\mathcal{A}}^2}{4\mu_\gamma}\lVert\boldsymbol{\lambda}^k-\bar{\boldsymbol{\lambda}}^{k-1}\rVert^2
$$

最后一项与 $\mathbf{z}$ 无关，该引理用两组不等式分别控制前三个含 $\mathbf{z}$ 的项。

**第一组不等式控制外层值函数与对偶值间隙的变化。** 中心 $\mathbf{z}$ 在 $\mathcal{P}_s$ 中只通过二次近端项出现，在各自极小点处展开二次项即得 $p_s$ 的上界与 $d_s$ 的下界：

$$
p_s(\mathbf{z}') - p_s(\mathbf{z}) \le \frac{1}{\gamma}\langle\mathbf{z}-\mathbf{x}_s^\star(\mathbf{z}),\mathbf{z}'-\mathbf{z}\rangle + \frac{1}{2\gamma}\lVert\mathbf{z}'-\mathbf{z}\rVert^2
$$

$$
d_s(\boldsymbol{\lambda};\mathbf{z}') - d_s(\boldsymbol{\lambda};\mathbf{z}) \ge \frac{1}{\gamma}\langle\mathbf{z}-\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z}'),\mathbf{z}'-\mathbf{z}\rangle + \frac{1}{2\gamma}\lVert\mathbf{z}'-\mathbf{z}\rVert^2
$$

第一个不等式代入相邻两步中心直接给出外层值函数 $p_s$ 的一步下降。两式相减时右端的二次项抵消，给出 $\mathcal{E}_k(\mathbf{z})$ 第一项值间隙的增量上界：

$$
\left[p_s(\mathbf{z}')-d_s(\boldsymbol{\lambda};\mathbf{z}')\right] - \left[p_s(\mathbf{z})-d_s(\boldsymbol{\lambda};\mathbf{z})\right] \le \frac{1}{\gamma}\langle\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z}')-\mathbf{x}_s^\star(\mathbf{z}),\mathbf{z}'-\mathbf{z}\rangle
$$

**第二组不等式控制原始极小点与鞍点随中心的漂移。** 由 $\mathcal{P}_s$ 关于原始变量的 $\mu_\gamma$ 强凸性与关于对偶变量的 $s^{-1}$ 强凹性，引理给出：

$$
\max\left\{\lVert\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z}')-\mathbf{x}_s(\boldsymbol{\lambda};\mathbf{z})\rVert,\, \lVert\mathbf{x}_s^\star(\mathbf{z}')-\mathbf{x}_s^\star(\mathbf{z})\rVert\right\} \le \frac{\lVert\mathbf{z}'-\mathbf{z}\rVert}{\gamma\mu_\gamma}
$$

$$
\lVert\boldsymbol{\lambda}_s^\star(\mathbf{z}')-\boldsymbol{\lambda}_s^\star(\mathbf{z})\rVert \le \frac{\sqrt{s}\,\lVert\mathbf{z}'-\mathbf{z}\rVert}{2\gamma\sqrt{\mu_\gamma}}
$$

原始极小点的灵敏度界将上式内积中在 $\mathbf{z}'$ 处取值的极小点换回中心 $\mathbf{z}$ 处，同时控制 $\mathcal{E}_k(\mathbf{z})$ 第三项中参考点随中心的移动。对偶鞍点的灵敏度界因 $s^{-1}$ 强凹性带有因子 $\sqrt{s}$，代入 $\mathcal{E}_k(\mathbf{z})$ 第二项后与前置权重 $(2s)^{-1}$ 相消，保证最终中心移动误差的常数与 $s$ 无关。

另外提醒一处源码问题：[AccelerationProof.tex:88-89](overleaf/appendix/AccelerationProof.tex#L88-L89) 的第 89 行目前处于注释状态，导致第 88 行的范数符号未闭合，并且该行对应的原始鞍点距离下界在下一步控制值间隙的中心移动误差时正好要用到。
