# 色度色散系数 D(λ)

Locale: zh-CN

本文是同目录英文稿的简体中文版，英文原文保持不变：[Chromatic dispersion coefficient D(λ)](chromatic-dispersion.md)。

## 直接回答

本文回答色度色散：色散系数 D(λ)，以及这段长度累积了多少色散。

色散计算器计算 G.652 形式的色散系数，或使用手工输入的系数，再沿长度累加，减去补偿，并把剩余量与容限比较。它还给出长度窗口，以及由谱宽得到的脉冲展宽项。


## 概述

引擎：`https://netengineerlab.com/tools/chromatic-dispersion-calculator/js/engine.js`（`NELChromaticDispersionEngine`），取于 2026-11-04。
## 公式

模型模式：

$$
D(\lambda) = \frac{S_0}{4}\left(\lambda - \frac{\lambda_0^{4}}{\lambda^{3}}\right)
$$

\(\lambda\) 和 \(\lambda_0\) 的单位是 nm，\(S_0\) 的单位是 ps/(nm²·km)。手工模式改用输入的 \(D\)。

$$
\mathrm{CD}_{\mathrm{fiber}} = D \, L, \qquad \mathrm{CD}_{\mathrm{res}} = \mathrm{CD}_{\mathrm{fiber}} - C
$$

$$
M_{\mathrm{CD}} = T - \lvert \mathrm{CD}_{\mathrm{res}} \rvert, \qquad u = 100\,\frac{\lvert \mathrm{CD}_{\mathrm{res}} \rvert}{T}
$$

$$
\tau = \lvert \mathrm{CD}_{\mathrm{res}} \rvert \, \Delta\lambda
$$

当 \(D \ne 0\) 时，满足 \(\lvert D L - C \rvert \le T\) 的长度窗口为：

$$
L_{\min} = \max\left(0,\ \frac{C\,\mathrm{sign}(D) - T}{\lvert D \rvert}\right), \quad
L_{\max} = \frac{T + C\,\mathrm{sign}(D)}{\lvert D \rvert}
$$

若 \(M_{\mathrm{CD}} < 0\)，状态为 `failed`；否则若 \(u > 80\)，状态为 `warning`；否则为 `healthy`。

引擎的显示舍入：\(D\) 到 3 位小数，累加色散、剩余色散和余量到 1 位小数，长度到 2 位小数。

## 变量

| 符号 | 引擎字段 | 单位 | 模型模式中的约束 |
|---|---|---|---|
| \(\lambda\) | `wavelength` | nm | 1200 到 1700 |
| \(\lambda_0\) | `lambda0` | nm | 1200 到 1700 |
| \(S_0\) | `s0` | ps/(nm²·km) | \(0 < S_0 \le 0.2\) |
| \(D\) | 手工模式中的 `manualD` | ps/(nm·km) | 绝对值 \(\le 50\) |
| \(L\) | `lengthKm` | km | \(0 < L \le 20000\) |
| \(C\) | `compensation` | ps/nm | 有限 |
| \(T\) | `tolerance` | ps/nm | \(> 0\) |
| \(\Delta\lambda\) | `spectralWidth` | nm | \(\ge 0\) |


## 约束

- \(\lambda\): 1200 到 1700
- \(\lambda_0\): 1200 到 1700
- \(S_0\): \(0 < S_0 \le 0.2\)
- \(D\): 绝对值 \(\le 50\)
- \(L\): \(0 < L \le 20000\)
- \(C\): 有限
- \(T\): \(> 0\)
- \(\Delta\lambda\): \(\ge 0\)

## 工程含义

系数在零色散波长处变号。补偿按 ps/nm 的数相减；\(D\) 的符号决定正的 \(C\) 是减小还是增大剩余量。这里的脉冲展宽是剩余色散与谱宽的乘积，是一阶估计，不是完整的接收机代价。

## 算例

模型模式：\(\lambda = 1550\,\mathrm{nm}\)，\(\lambda_0 = 1310\,\mathrm{nm}\)，\(S_0 = 0.092\,\mathrm{ps/(nm^2\cdot km)}\)，\(L = 80\,\mathrm{km}\)，\(C = 0\)，\(T = 1600\,\mathrm{ps/nm}\)，\(\Delta\lambda = 0.1\,\mathrm{nm}\)。

1. \(1310^{4} / 1550^{3} = 790.190139\ldots\)
2. \(D = (0.092/4) \times (1550 - 790.190139\ldots) = 17.4606188\ldots\,\mathrm{ps/(nm\cdot km)}\)。显示 **17.461**。
3. 光纤 CD \(= 1396.8495\ldots\,\mathrm{ps/nm}\)。显示 **1396.8**。剩余量等于光纤 CD。余量 \(= 1600 - 1396.8495\ldots = 203.150\ldots\,\mathrm{ps/nm}\)。显示 **203.2**。
4. 占用比例 \(= 87.303\ldots\%\)。因为高于 80% 且余量为正，状态为 **warning**。
5. 展宽 \(= 139.685\ldots\,\mathrm{ps}\)。显示 **139.68**。
6. \(L_{\max} = 1600 / 17.4606188\ldots = 91.635\ldots\,\mathrm{km}\)。显示 **91.64 km**。\(L_{\min} = 0\)。

边界：同一链路若容限为 \(800\,\mathrm{ps/nm}\)，余量为负，状态为 **failed**。手工模式中 \(D = 0\) 且 \(\lvert C \rvert \le T\) 时，显示逻辑把最大长度报告为无界。

## 限制

- 这个模型是标准单模斜率形式。它不是 G.655 色散图谱。
- 斜率 \(S_0\) 为常数。没有实测 \(D(\lambda)\) 表。
- 容限是输入，不是光模块目录。
- 波长和零色散波长在乘方里使用纳米；不要传入米。

## 参考标准

生产页引用了同一系数公式，引擎注释也写了这个公式：

- ITU-T G.652：https://www.itu.int/rec/T-REC-G.652/en 。页面文字指向公式 (6-1)，\(D(\lambda) = (S_0/4)(\lambda - \lambda_0^4/\lambda^3)\)，以及 G.652 表中的 \(\lambda_0\) 和 \(S_0\) 限值。本库核对的是引擎中的表达式，不是 ITU PDF。
- ITU-T G.650.1：https://www.itu.int/rec/T-REC-G.650.1/en
- ITU-T G.691：https://www.itu.int/rec/T-REC-G.691/en
- ITU-T G.655：https://www.itu.int/rec/T-REC-G.655/en 。页面说明这类光纤应使用数据表上的 \(D\)（手工模式）。


## 在线计算器

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/chromatic-dispersion-calculator/zh/

工具 ID：`chromatic-dispersion-calculator`。

## 相关公式

- [单段光纤链路损耗](fiber-link-loss.zh-CN.md)
- [光链路功率预算](optical-power-budget.zh-CN.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `chromatic-dispersion-calculator` |
| 证据 | 生产 `js/engine.js` 中的函数 `coefficient` 和 `calculate` |
| 方法 | 用 Python 计算 \((S_0/4)(\lambda - \lambda_0^4/\lambda^3)\) 及剩余量检验 |
| 算例结果 | \(D = 17.4606188\ldots\) ps/(nm·km)；显示 17.461；80 km 的 CD 显示 1396.8 ps/nm；容限 1600 ps/nm 时状态为 warning |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |