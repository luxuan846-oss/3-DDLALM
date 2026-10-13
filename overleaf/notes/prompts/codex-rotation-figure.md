# Codex 任务：绘制第 4.2 节旋转实例示意图

工作目录：`/Users/liluxuan/Documents/My_Papers/3_DDLALM/overleaf`

## 目标

一张图，两个子图，说明 Example `ex:rotation` 上 SPLALM 从零初值出发的行为：
(a) 原始迭代点 $x^k\in\mathbb R^2$ 绕 $x_c$ 转圈，始终位于圆环 $\frac34X\le\|x-x_c\|\le\frac54X$ 内；
(b) KKT 残差 $R_k$ 始终高于 $\epsilon$。

图只作示意，不作数值验证：不做参数扫描，不加额外检查。

## 输出

- 脚本：`figures/plot_rotation_instance.py`（Python 3.8 可运行，只用 numpy、matplotlib）
- 图：`figures/rotation_instance.pdf`（矢量，`pdf.fonttype=42`）
- 不修改任何 `.tex` 文件。不 commit，不 push。

## 数据：按论文定义直接计算

1. 参数取 $\rho=s=\tau=\gamma=\eta=1$，$\Delta=1$，$\alpha=\beta=\frac12$，$\epsilon=0.002$。
   脚本内按 `notes/gpt-proofs/lb-proof-materials.md` Part III (D1)–(D2) 计算 $c_1,c_2(\Delta)$ 与 $\alpha_\epsilon=1024\max\{1,4\tau,4\gamma\tau\}\epsilon^2$，并 `assert` 定理条件成立：$\epsilon<c_2$，$\epsilon(\rho+s)\le c_1$，$\alpha>\alpha_\epsilon$，$\beta>0$。条件不成立就停止并报告，不改参数凑图。
2. 实例参数按 `appendix/LowerBoundRotation.tex` 的 `eq:rot-basic` 至 `eq:rot-shift` 逐项计算（复数用 `numpy.complex128`，$\mathbb R^2$ 与 $\mathbb C$ 等同）。
3. 迭代点由 **SPLALM 本身**产生，不用闭式公式：按 `sections/Preliminaries.tex` 的 `def:splalm`、`eq:potential`、`eq:prox-multiplier` 实现四步更新，从 $(x^0,\lambda^0,z^0,\mu^0)=0$ 出发。
   - $f(x)=\psi(\|x-x_c\|)-b\langle\lambda_c,x-x_c\rangle$，$\psi$ 为 Example `ex:rotation` 中的三段函数；$\nabla f$ 按链式法则写出。
   - $\mathcal A(x)=b(x-x_c)$，$h=\|\cdot\|_2$，$\operatorname{prox}_{h/\rho}$ 为块软阈值。
   - $R_k$ 按 `eq:kkt-residual` 计算，输出为 $(x^{k+1},y^{k+1},q^k)$。
4. 迭代步数 $K$：取两个完整旋转周期，即 $K=\lceil 2\cdot 2\pi/\arg\zeta\rceil$。若迭代点离开圆环或 $R_k\le\epsilon$，停止并报告，不改图。

## 版式

- 尺寸 `figsize=(5.1, 2.3)`（SIAM 正文宽度），两子图左右排列，左图 `aspect='equal'`。
- 字体：`font.family='serif'`，`mathtext.fontset='cm'`，`font.size=9`，与 SIAM 正文一致。
- 颜色：黑、灰，加一种强调色 `#1f3b73`。不用其他颜色，不用渐变、阴影、透明叠层以外的效果。
- 不要标题、网格、图例框。文字标注直接写在对象旁边。坐标刻度只保留必要的几个，或去掉。
- 线宽 0.8 以内；点的大小不超过 `markersize=2`。

### 子图 (a)：原始平面

- 圆环 $\frac34X\le\|x-x_c\|\le\frac54X$：浅灰填充（`0.92`），无边框或细灰边。
- 半径 $X$ 的圆：灰色细虚线，表示纯旋转分量 $x_c+\zeta^kX$ 的轨道。
- 轨迹 $x^k$：强调色细实线连接，每隔若干步画一个小点；前 30 步用稍深的点，显示瞬态。
- 标注：$x_c$（圆心，黑色小叉或小点）；原点处标 $x^0=0$；在圆环外侧用短线标出 $\frac34X$、$\frac54X$。
- 原点必须出现在图中。

### 子图 (b)：残差

- 横轴 $k$（线性），纵轴 $R_k/\epsilon$。
- $R_k/\epsilon$：强调色细实线。
- 参考线：$R_k/\epsilon=1$ 黑色细实线，旁注 $\epsilon$；$R_k/\epsilon=\frac76$ 灰色细虚线，旁注 $\tfrac76\epsilon$。
- 纵轴下限取 0，使"始终高于 1"一眼可见。
- 轴标签只写 $k$ 和 $R_k/\epsilon$。

## 图注草稿（供论文使用，写入报告，不写入 .tex）

> SPLALM on Example ex:rotation, started from zero, with $\rho=s=\tau=\gamma=\eta=1$, $\alpha=\beta=\frac12$, and $\epsilon=0.002$. (a) The primal iterates $x^k$ stay in the annulus $\frac34X\le\|x-x_c\|\le\frac54X$ (shaded); the dashed circle has radius $X$. (b) The KKT residual $R_k$ stays above $\frac76\epsilon$.

## 报告

- 实际使用的参数值，$c_1,c_2,\alpha_\epsilon$ 数值，$K$，$\arg\zeta$
- $\min_k\|x^k-x_c\|/X$、$\max_k\|x^k-x_c\|/X$、$\min_kR_k/\epsilon$ 三个数
- 生成的文件路径
