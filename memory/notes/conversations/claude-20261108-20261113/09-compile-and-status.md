# 09-compile-and-status

- **Source session**: `029b99d3`
- **Span (local time)**: 2026-11-13 12:09 to 2026-11-13 12:11
- **User turns**: 1

---

## User (2026-11-13 12:09)

我们现在继续干这个

---

## Assistant (2026-11-13 12:11)

附录 L3 的引理里混进了一段键盘乱码（第 262 行），导致编译失败。我先删掉这段乱码和随后的空行，再重新编译。

`siamart` 的 proof 环境不定义 `\qedhere`，全文其他证明也都没用它。我把这一处删掉。

老大，**`appendix/AccelerationProof.tex` 的 6 步顺推已经全部写完**（最后修改时间是 11-12 22:34）。L1–L4 的证明都已写入，A1–A4 也已放进 L3 的子节。`PROJECT_STATUS.md` 第 6 项仍写着"L3 待写、L4 占位"，这条记录已经过时。剩下的工作是回填正文红色占位块：撤掉红色标记，并恢复 `main.tex` 中被注释的附录。

## 核对结果

- **正文 L3 的常数与附录一致。** 附录 L3 证明的最后一步给出三项耗散系数：$\frac{1}{128\gamma}$、$\frac{1}{16\tau}$、$\frac{\alpha}{6\gamma}$，与正文 `lem:b2-prime-potential-descent` 相同。我逐项手算了收尾的算术。$(14\sqrt{\kappa}+11)\alpha\le\frac{13}{4}$，再由 $\gamma\mu_\gamma\ge\frac{9}{10}$，得到下式：

$$
\frac{11}{24}-\frac{65}{288}=\frac{67}{288}\ge\frac{1}{6}
$$

  状态文件里记的 $c_1=\frac{1}{250\gamma}$ 来自旧路线，现已被 $\frac{1}{128\gamma}$ 取代。
- **$C_R$ 正确。** 由 $\eta=\gamma$ 与 $\sqrt{D_k}\le\sqrt{\sqrt{\kappa}D_k/2}$，原始残差的系数为 $8\sqrt{\gamma}L_{\mathcal{D},\mathbf{x}}+6/\sqrt{\gamma}$，对偶残差的系数为 $\sqrt{8/\tau}$。$\mathcal{R}_{\mathrm{KKT}}$ 取两项残差的 max，所以 $C_R$ 取两者的 max。$K$ 的下界也随之成立。
- **L4 的 $\Delta_{\mathcal{W}}$ 与正文 `eq:b2-prime-initial-gap` 一致。**

## 修复的两处编译错误

1. `appendix/AccelerationProof.tex` 第 262 行混入了一段键盘乱码 `nm,l.;'/kjbn gvcfvbnm,fghiuq  12sd`，我已删除。
2. 第 641 行的 `\qedhere` 在 `siamart220329` 中没有定义，我已删除。全文其他证明也都不用它。

修复后，我在 `/tmp/ddl` 的副本里恢复了附录 A–C 的 `\input` 并编译：**41 页，零错误，零未定义引用**。本地的 `main.tex` 和 `main.pdf` 都没有动。

**附录已经完整，正文常数与附录一致，论文离定稿只差两步：撤掉红色标记、恢复附录 A–C。**
