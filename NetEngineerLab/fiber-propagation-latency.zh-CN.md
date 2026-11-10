# 光纤传播时延与往返时间

Locale: zh-CN

本文是同目录英文稿的简体中文版，英文原文保持不变：[Fiber propagation delay and RTT](fiber-propagation-latency.md)。

## 直接回答

本文回答光纤传播时延：由长度、群折射率和光速得到单向时延和往返时间。

光纤时延计算器根据路由距离、路由系数、群折射率、每台设备的设备时延，以及可选的串行化时延，估算单向时延和往返时间。


## 概述

引擎：`https://netengineerlab.com/tools/fiber-latency-calculator/js/engine.js`（`NELFiberLatencyEngine`），取于 2026-11-04。
## 公式

距离先换成公里（\(1\,\mathrm{mi} = 1.609344\,\mathrm{km}\)，\(1\,\mathrm{m} = 0.001\,\mathrm{km}\)）。

$$
L_{\mathrm{km}} = d_{\mathrm{km}} \times f_{\mathrm{route}}
$$

$$
t_{\mathrm{prop}} = L_{\mathrm{km}} \times n_g \times \frac{10^{6}}{c}, \quad c = 299792.458\,\mathrm{km/s}
$$

$$
t_{\mathrm{eq}} = N_{\mathrm{eq}} \, t_{\mathrm{dev}}
$$

$$
t_{\mathrm{ser}} = N_{\mathrm{hop}} \times \frac{S_{\mathrm{bytes}} \times 8}{R_{\mathrm{Gbit/s}} \times 10^{9}} \times 10^{6}
$$

$$
t_{\mathrm{ow}} = t_{\mathrm{prop}} + t_{\mathrm{eq}} + t_{\mathrm{ser}}, \qquad t_{\mathrm{rtt}} = 2\, t_{\mathrm{ow}}
$$

上面的 \(t\) 都以微秒为单位。显示舍入（`formatDelay`）：绝对值小于 \(1000\,\mu\mathrm{s}\) 时保留微秒并舍入到 2 位小数；否则换成毫秒并舍入到 3 位小数。舍入使用 `Math.round((value + Number.EPSILON) * 10^n)`。

引擎中群折射率的默认值是 1.468。允许范围是 1 到 1.6。路由系数至少为 1。

## 变量

| 符号 | 引擎字段 | 单位 |
|---|---|---|
| \(d\) | `distance`，`distanceUnit` 为 `km`、`mi` 或 `m` | 随所选单位 |
| \(f_{\mathrm{route}}\) | `routeFactor` | 1 |
| \(n_g\) | `groupIndex` | 1 |
| \(N_{\mathrm{eq}}\)，\(t_{\mathrm{dev}}\) | `equipmentCount`，`equipmentDelay` | 个，µs |
| \(S_{\mathrm{bytes}}\) | `packetSize` | 字节 |
| \(R\) | `linkRate` | Gbit/s |
| \(N_{\mathrm{hop}}\) | `serializationHops` | 个 |

## 工程含义

决定调制脉冲时延的是群折射率，不是相位折射率。常数 \(c\) 是定义的光速，\(299792.458\,\mathrm{km/s}\)。串行化是 \(N\) 跳、每跳 \(8S/R\)，不是沿路径随包长变化的存储转发累加。往返正好是单向之和的两倍；没有不对称的回程。

引擎还给出若干比较时延，它们不加进 \(t_{\mathrm{ow}}\)：真空 \(10^{6}/c\)，微波为真空的 1.0003 倍，空芯为真空的 1.003 倍，以及 NVP 为 0.65 和 0.70 的铜缆（真空时延除以 NVP）。

## 算例

输入：100 km，路由系数 1，\(n_g = 1.468\)，无设备，包长 0，链路速率 10 Gbit/s，串行化跳数 0。

1. 光纤长度 \(= 100\,\mathrm{km}\)。
2. \(t_{\mathrm{prop}} = 100 \times 1.468 / 299792.458 \times 10^{6} = 489.67209175\ldots\,\mu\mathrm{s}\)。
3. 设备和串行化都是 0。单向时延等于传播时延。RTT 是它的两倍，\(979.3441835\ldots\,\mu\mathrm{s}\)。

显示舍入：单向 **489.67 µs**，RTT **979.34 µs**。每公里时延为 \(4.8967209\ldots\,\mu\mathrm{s/km}\)。

边界：路由系数必须 \(\ge 1\)。小于 1 会被拒绝。同一 100 km 上群折射率 1.6 使单向时延升到 \(533.7025\ldots\,\mu\mathrm{s}\)（显示 **533.70 µs**）。群折射率低于 1 或高于 1.6 会被拒绝。距离必须大于 0。

串行化核对：1500 字节，1 Gbit/s，2 跳，其他时延为 0：

$$
t_{\mathrm{ser}} = 2 \times (1500 \times 8) / 10^{9} \times 10^{6} = 24\,\mu\mathrm{s}.
$$

## 限制

- 不含排队、FEC 或协议 ACK 时延。
- 设备时延是每台设备一个常数，不是按平台查表。
- 英里换算用国际英里，1.609344 km。
- 用于比较的铜缆和微波数字是引擎里的标签，不是实测路径。

## 参考标准

页面把 G.652 群折射率预设（1310 nm 为 1.4677，1550 nm 为 1.4682）描述为选择器使用的已公布数值。引擎文件本身没有嵌入建议书 URL。在把这两个预设的数字表对应到已获取的条款之前，本库对具体 G.652 版本标为 **待定**。

速度 \(299792.458\,\mathrm{km/s}\) 是源码中使用的定义真空光速（`C_KM_S`）。


## 在线计算器

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/fiber-latency-calculator/zh/

工具 ID：`fiber-latency-calculator`。

## 相关公式

- [单段光纤链路损耗](fiber-link-loss.zh-CN.md)
- [色度色散系数 D(λ)](chromatic-dispersion.zh-CN.md)
- [STP 端口路径开销](stp-path-cost.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `fiber-latency-calculator` |
| 证据 | 生产 `js/engine.js` 中的常数 `C_KM_S`、`MI_TO_KM`、`DEFAULT_GROUP_INDEX` 以及 `calculate` |
| 方法 | 在 Python 中直接计算 \(L n_g / c\) |
| 算例结果 | 显示舍入前单向 489.672 µs；显示为 489.67 µs |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |