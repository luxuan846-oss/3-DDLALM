# 06a-branch-short

- **Source session**: `bcee9312 (branch)`
- **Span (local time)**: 2026-11-12 17:12 to 2026-11-12 17:15
- **User turns**: 1
- **Continues from**: [05-proof-restructure-trunk](05-proof-restructure-trunk.md)

---

## Assistant (2026-11-12 17:12)

老大，系数直接改成 $\frac{1}{64\gamma}$，同时把 $\varsigma$ 从正文和附录里全部去掉，直接写 $\sqrt{\tau/s}$。

1. **为什么之前不是 64**：`Combination` 里 $\frac{\mu_\gamma}{8}-\frac{3}{100}\left(L_x+\frac{3\mu_\gamma}{4}\right)\ge\frac{227}{4000\gamma}=\frac{1}{17.62\gamma}$。我之前放缩成了 $\frac{1}{18\gamma}$，除以 $\frac{363}{100}$ 之后等于 $\frac{1}{65.34\gamma}$，向上取整才写成 66。这里其实直接满足
   $$
   \frac{227}{4000}\cdot\frac{100}{363}=\frac{227}{14520}\ge\frac{1}{64}
   $$
   所以在 `Combination` 里把中间过渡的 $\frac{1}{18\gamma}$ 换成 $\frac{5}{88\gamma}$（因为 $\frac{5}{88}\cdot\frac{100}{363}=\frac{125}{7986}\ge\frac{1}{64}$），引理右端就直接是 $-\frac{1}{64\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2$，不需要改前面的任何一步。

2. **去掉 $\varsigma$**：算法里动量系数已经是 $\omega=\frac{\sqrt{s}-\sqrt{\tau}}{\sqrt{s}+\sqrt{\tau}}$，$\varsigma$ 只是给 $\sqrt{\tau/s}$ 起的别名。去掉之后：
   - 正文 (6.4) 里删掉 $\varsigma=\sqrt{\tau/s}$，直接写 $\alpha=\kappa_\alpha\sqrt{\tau/s}$；
   - 估计序列写成 $\mathbf{w}^k:=\boldsymbol{\lambda}^{k-1}+\sqrt{s/\tau}(\boldsymbol{\lambda}^k-\boldsymbol{\lambda}^{k-1})$；
   - 引理 4 陈述变成：

$$
\mathcal{E}_{k+1}(\mathbf{z}^k)\le\left(1-\sqrt{\frac{\tau}{s}}\right)\mathcal{E}_k-\frac{1}{64\gamma}\lVert\mathbf{x}^{k+1}-\mathbf{x}^k\rVert^2-\frac{1}{8\tau}\lVert\boldsymbol{\lambda}^{k+1}-\bar{\boldsymbol{\lambda}}^k\rVert^2-\frac{\mu_\gamma}{2}\sqrt{\frac{\tau}{s}}\lVert\mathbf{x}^{k+1}-\mathbf{x}_s^\star(\mathbf{z}^k)\rVert^2
$$

我直接把这两处改掉？

---

## User (2026-11-12 17:12)

然后是我们第二步是 中心移动 这个很简单 引理6 可以写进去？

---

## Assistant (2026-11-12 17:15)

API Error: 400 unknown provider for model claude-fable-5-2
