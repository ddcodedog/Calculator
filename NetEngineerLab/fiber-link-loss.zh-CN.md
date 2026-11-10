# 单段光纤链路损耗

本文是同目录英文稿的简体中文版，英文原文保持不变：[Single-span fiber link loss](fiber-link-loss.md)。

## 概述

光纤损耗计算器把光纤段的衰减，与熔接、连接器、分光级和其他无源器件的离散损耗相加，再加上使用者输入的工程余量，然后把这个设计损耗与可用功率预算比较，并比较估算接收电平与接收门限。

本页记录生产引擎 `https://netengineerlab.com/tools/fiber-loss/js/engine.js`（`NELFiberLossEngine`，取于 2026-11-04）。公开仓库 `ddcodedog/fiber-loss-calculator` 是另一个静态页面，不是这些公式的来源。

## 公式

光纤、熔接和连接器：

$$
L_{\mathrm{fiber}} = d \, \alpha
$$

$$
L_{\mathrm{splice}} = N_{\mathrm{s}} \, \ell_{\mathrm{s}}, \qquad L_{\mathrm{conn}} = N_{\mathrm{c}} \, \ell_{\mathrm{c}}
$$

$$
L_{\mathrm{split+other}} = L_{\mathrm{s1}} + L_{\mathrm{s2}} + L_{\mathrm{other}}
$$

$$
L_{\mathrm{physical}} = L_{\mathrm{fiber}} + L_{\mathrm{splice}} + L_{\mathrm{conn}} + L_{\mathrm{split+other}}
$$

$$
L_{\mathrm{design}} = L_{\mathrm{physical}} + M
$$

$$
B_{\mathrm{rem}} = B_{\mathrm{avail}} - L_{\mathrm{design}}, \qquad P_{\mathrm{rx}} = P_{\mathrm{tx}} - L_{\mathrm{physical}}, \qquad M_{\mathrm{rx}} = P_{\mathrm{rx}} - P_{\mathrm{th}}
$$

绝对值不超过 \(10^{-9}\,\mathrm{dB}\) 的结果当作 0。若 \(B_{\mathrm{rem}} < 0\) 或 \(M_{\mathrm{rx}} < 0\)，状态为 `failed`；否则任一余量低于 \(3\,\mathrm{dB}\) 时为 `warning`；否则为 `healthy`。

## 变量

| 符号 | 引擎中的名称 | 单位 | 约束 |
|---|---|---|---|
| \(d\) | `distance` | km | 有限，\(\ge 0\) |
| \(\alpha\) | `attenuation` | dB/km | 有限，\(\ge 0\) |
| \(N_{\mathrm{s}}\)，\(N_{\mathrm{c}}\) | `spliceCount`，`connectorCount` | 个 | 安全整数，\(\ge 0\) |
| \(\ell_{\mathrm{s}}\)，\(\ell_{\mathrm{c}}\) | `spliceLoss`，`connectorLoss` | dB | 有限，\(\ge 0\) |
| \(L_{\mathrm{s1}}\)，\(L_{\mathrm{s2}}\) | `splitter1`，`splitter2` | dB | 有限，\(\ge 0\) |
| \(L_{\mathrm{other}}\) | `otherLoss` | dB | 有限，\(\ge 0\) |
| \(M\) | `engineeringMargin` | dB | 有限，\(\ge 0\) |
| \(B_{\mathrm{avail}}\) | `availableBudget` | dB | 有限，\(\ge 0\) |
| \(P_{\mathrm{tx}}\) | `txPower` | dBm | 有限 |
| \(P_{\mathrm{th}}\) | `rxThreshold` | dBm | 有限 |

## 工程含义

在无源单段路径上，以 dB 表示的衰减可以相加。引擎不把波长换算成 \(\alpha\)；dB/km 由使用者或页面预设给出。分光损耗是输入的插入损耗，不是本引擎内部计算的 \(10\log_{10}(N)\)。\(3\,\mathrm{dB}\) 告警带是这个计算器里的规划规则，不是从某份已引用标准取出的合格限值。

## 算例

输入与生产页“10 km PON feeder”案例一致，并补上引擎需要的预算和功率字段：

| 输入 | 取值 |
|---|---|
| 距离、衰减 | 10 km，0.25 dB/km |
| 熔接 | 6 × 0.10 dB |
| 连接器 | 4 × 0.30 dB |
| 分光 1 / 分光 2 / 其他 | 21.0 / 0 / 0 dB |
| 工程余量 | 3 dB |
| 可用预算、发送功率、接收门限 | 32 dB，3 dBm，−27 dBm |

步骤：

1. \(L_{\mathrm{fiber}} = 10 \times 0.25 = 2.50\,\mathrm{dB}\)。
2. \(L_{\mathrm{splice}} = 0.60\,\mathrm{dB}\)，\(L_{\mathrm{conn}} = 1.20\,\mathrm{dB}\)，分光与其他 \(= 21.00\,\mathrm{dB}\)。
3. \(L_{\mathrm{physical}} = 25.30\,\mathrm{dB}\)。
4. \(L_{\mathrm{design}} = 28.30\,\mathrm{dB}\)。
5. \(B_{\mathrm{rem}} = 32 - 28.30 = 3.70\,\mathrm{dB}\)。
6. \(P_{\mathrm{rx}} = 3 - 25.30 = -22.30\,\mathrm{dBm}\)，\(M_{\mathrm{rx}} = -22.30 - (-27) = 4.70\,\mathrm{dB}\)。

结果：物理损耗 **25.30 dB**，设计损耗 **28.30 dB**，状态 **healthy**。引擎保留 IEEE-754 双精度。这些输入都是十进制十分位上的准确数，所以两位小数的 dB 与引擎一致。

边界：同样的无源损耗，若可用预算为 \(28\,\mathrm{dB}\)，则 \(B_{\mathrm{rem}} = -0.30\,\mathrm{dB}\)，状态为 **failed**。距离 \(0\,\mathrm{km}\) 只去掉光纤项（\(L_{\mathrm{physical}} = 22.80\,\mathrm{dB}\)）。

## 限制

- 整段只用一个衰减系数。没有熔接地图、双向或双波长计算。
- 连接器数量是使用者输入的整数。工具不判断一对插接算一个还是两个“连接器”。
- 本引擎不含反射、PMD 或色散代价。
- `healthy` 不是验收测试。

## 参考标准

生产页链接了下列建议，并说明工具如何使用它们。本库没有重新审核这些建议的正文。

- ITU-T G.652：https://www.itu.int/rec/T-REC-G.652/en
- ITU-T G.984.2：https://www.itu.int/rec/T-REC-G.984.2/en
- ITU-T G.671：https://www.itu.int/rec/T-REC-G.671/en
- IEEE 802.3：https://standards.ieee.org/ieee/802.3/10422/
- IEC 61280-4-2:2024：https://webstore.iec.ch/en/publication/77134


## 在线计算器

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/fiber-loss/zh/

工具 ID：`fiber-loss`。

## 相关公式

- [光链路功率预算](optical-power-budget.zh-CN.md)
- [色度色散系数 D(λ)](chromatic-dispersion.zh-CN.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `fiber-loss` |
| 证据 | 生产 `tools/fiber-loss/js/engine.js` 的 `calculate`，取于 2026-11-04。清单中的本机路径 `D:\NetEngineerLab-V173-GitHub\...` 不在这台机器上。 |
| 方法 | 用 Python 重算各项求和，并与页面 10 km 算例比较（物理 25.30 dB，设计 28.30 dB）。 |
| 算例结果 | 物理 25.30 dB，设计 28.30 dB；上表完整输入的状态为 healthy |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
