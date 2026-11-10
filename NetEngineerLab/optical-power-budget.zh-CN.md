# 光链路功率预算

Locale: zh-CN

本文是同目录英文稿的简体中文版，英文原文保持不变：[Optical link power budget](optical-power-budget.md)。

## 直接回答

本文回答光功率预算：发射光功率与接收灵敏度之间的分贝，扣掉光纤、无源损耗、代价和工程余量，并检查过载。

光功率预算计算器由最小发送功率和接收灵敏度构成链路预算，先减去路径代价，再减去光纤、熔接、连接器、三项分光、其他无源损耗和工程余量。它还用同一物理损耗检查最大发送功率是否超过接收机过载。


## 概述

引擎：`https://netengineerlab.com/tools/optical-power-budget/js/engine.js`（`NELOpticalPowerBudgetEngine`），取于 2026-11-04。
## 公式

$$
B_{\mathrm{raw}} = P_{\mathrm{tx,min}} - P_{\mathrm{sens}}
$$

$$
B_{\mathrm{std}} = B_{\mathrm{raw}} - P_{\mathrm{pen}}
$$

$$
L_{\mathrm{fiber}} = d \, \alpha, \quad L_{\mathrm{splice}} = N_{\mathrm{s}}\ell_{\mathrm{s}}, \quad L_{\mathrm{conn}} = N_{\mathrm{c}}\ell_{\mathrm{c}}
$$

$$
L_{\mathrm{split}} = L_1 + L_2 + L_3, \quad L_{\mathrm{fixed}} = L_{\mathrm{splice}} + L_{\mathrm{conn}} + L_{\mathrm{split}} + L_{\mathrm{other}}
$$

$$
L_{\mathrm{physical}} = L_{\mathrm{fiber}} + L_{\mathrm{fixed}}, \quad L_{\mathrm{design}} = L_{\mathrm{physical}} + M
$$

$$
B_{\mathrm{rem}} = B_{\mathrm{std}} - L_{\mathrm{design}}
$$

$$
P_{\mathrm{rx}} = P_{\mathrm{tx,min}} - L_{\mathrm{physical}}, \quad P_{\mathrm{rx,max}} = P_{\mathrm{tx,max}} - L_{\mathrm{physical}}
$$

$$
M_{\mathrm{sens}} = P_{\mathrm{rx}} - P_{\mathrm{sens}}, \quad M_{\mathrm{over}} = P_{\mathrm{over}} - P_{\mathrm{rx,max}}
$$

$$
d_{\max} = \max\left(0,\ \frac{B_{\mathrm{std}} - M - L_{\mathrm{fixed}}}{\alpha}\right)
$$

接近 0 的余量（\(\le 10^{-9}\,\mathrm{dB}\)）变成 0。若 \(B_{\mathrm{rem}}\)、\(M_{\mathrm{sens}}\)、\(M_{\mathrm{over}}\) 中有一个为负，状态为 `failed`；否则其中有一个低于 \(3\,\mathrm{dB}\) 时为 `warning`；否则为 `healthy`。当 \(B_{\mathrm{std}} > 0\) 时，占用百分比为 \(100 \times L_{\mathrm{design}} / B_{\mathrm{std}}\)。

## 变量

| 符号 | 引擎字段 | 单位 | 约束 |
|---|---|---|---|
| \(P_{\mathrm{tx,min}}\)，\(P_{\mathrm{tx,max}}\) | `tx`，`txMax` | dBm | 有限，\(P_{\mathrm{tx,min}} \le P_{\mathrm{tx,max}}\) |
| \(P_{\mathrm{sens}}\)，\(P_{\mathrm{over}}\) | `sens`，`over` | dBm | 有限，\(P_{\mathrm{sens}} < P_{\mathrm{over}}\) |
| \(P_{\mathrm{pen}}\) | `penalty` | dB | \(\ge 0\) |
| \(d\)，\(\alpha\) | `d`，`a` | km，dB/km | \(d \ge 0\)，\(\alpha > 0\) |
| \(N_{\mathrm{s}}\)，\(\ell_{\mathrm{s}}\) | `sc`，`sl` | 个，dB | 个数为安全整数 |
| \(N_{\mathrm{c}}\)，\(\ell_{\mathrm{c}}\) | `cc`，`cl` | 个，dB | 个数为安全整数 |
| \(L_1,L_2,L_3\) | `s1`，`s2`，`s3` | dB | \(\ge 0\) |
| \(L_{\mathrm{other}}\)，\(M\) | `other`，`margin` | dB | \(\ge 0\) |


## 约束

- \(P_{\mathrm{tx,min}}\)，\(P_{\mathrm{tx,max}}\): 有限，\(P_{\mathrm{tx,min}} \le P_{\mathrm{tx,max}}\)
- \(P_{\mathrm{sens}}\)，\(P_{\mathrm{over}}\): 有限，\(P_{\mathrm{sens}} < P_{\mathrm{over}}\)
- \(P_{\mathrm{pen}}\): \(\ge 0\)
- \(d\)，\(\alpha\): \(d \ge 0\)，\(\alpha > 0\)
- \(N_{\mathrm{s}}\)，\(\ell_{\mathrm{s}}\): 个数为安全整数
- \(N_{\mathrm{c}}\)，\(\ell_{\mathrm{c}}\): 个数为安全整数
- \(L_1,L_2,L_3\): \(\ge 0\)
- \(L_{\mathrm{other}}\)，\(M\): \(\ge 0\)

## 工程含义

所谓“标准”预算，是灵敏度窗口再减去一项代价。过载使用最大出光，所以灵敏度余量很大时，链路仍可能因为功率过高而失败。最大距离假定固定损耗和 \(\alpha\) 在任何长度上都不变；它不是色散限制的传输距离。

## 算例

| 输入 | 取值 |
|---|---|
| \(P_{\mathrm{tx,min}}\)，\(P_{\mathrm{tx,max}}\) | 2 dBm，5 dBm |
| 灵敏度、过载 | −28 dBm，+2 dBm |
| 代价 | 1 dB |
| 长度、衰减 | 20 km，0.35 dB/km |
| 熔接、连接器 | 4 × 0.10 dB，2 × 0.50 dB |
| 分光与其他 | 0 dB |
| 余量 | 3 dB |

步骤：

1. \(B_{\mathrm{raw}} = 2 - (-28) = 30\,\mathrm{dB}\)。\(B_{\mathrm{std}} = 29\,\mathrm{dB}\)。
2. 光纤 \(7.00\,\mathrm{dB}\)。固定损耗 \(0.40 + 1.00 = 1.40\,\mathrm{dB}\)。物理损耗 \(8.40\,\mathrm{dB}\)。设计损耗 \(11.40\,\mathrm{dB}\)。
3. 剩余 \(29 - 11.40 = 17.60\,\mathrm{dB}\)。
4. \(P_{\mathrm{rx}} = 2 - 8.40 = -6.40\,\mathrm{dBm}\)。灵敏度余量 \(21.60\,\mathrm{dB}\)。
5. \(P_{\mathrm{rx,max}} = 5 - 8.40 = -3.40\,\mathrm{dBm}\)。过载余量 \(2 - (-3.40) = 5.40\,\mathrm{dB}\)。
6. \(d_{\max} = (29 - 3 - 1.40) / 0.35 = 70.2857\ldots\,\mathrm{km}\)。

结果：设计损耗 **11.40 dB**，剩余 **17.60 dB**，状态 **healthy**。引擎不对中间结果另做舍入。

边界：把过载设为 \(-8\,\mathrm{dBm}\)。过载余量变为 \(-8 - (-3.40) = -4.60\,\mathrm{dB}\)，状态为 **failed**，此时灵敏度余量仍为正。衰减必须大于 0；引擎拒绝 \(\alpha = 0\)。

## 限制

- 三个分光字段是相加的 dB，不是分光比。
- 一个代价数字覆盖全部发送机和路径代价。
- 3 dB 告警门限是这个计算器内部的。
- 不从波长表计算光纤损耗。

## 参考标准

在本引擎文件内，作为已引用版本的标准仍为待定。同站光纤损耗页链接了 ITU-T G.652、G.984.2 和 G.671；这个预算引擎没有嵌入那些 URL。除非把灵敏度、过载和代价按那些限值输入，不要把等级字母（B+、C+）当成这个函数的输出。


## 在线计算器

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/optical-power-budget/zh/

工具 ID：`optical-power-budget`。

## 相关公式

- [单段光纤链路损耗](fiber-link-loss.zh-CN.md)
- [色度色散系数 D(λ)](chromatic-dispersion.zh-CN.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `optical-power-budget` |
| 证据 | 生产 `tools/optical-power-budget/js/engine.js` 的 `calculate`，2026-11-04 |
| 方法 | 用 Python 按 `calculate` 中的每一项赋值重算 |
| 算例结果 | 设计损耗 11.40 dB，剩余 17.60 dB，状态 healthy；过载边界为失败 |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |