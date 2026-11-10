# OSPF 接口开销

本文是同目录英文稿的简体中文版，英文原文保持不变：[OSPF interface cost](ospf-interface-cost.md)。

## 概述

OSPF 开销计算器把参考带宽和接口带宽都按 Mbit/s 换成整数 OSPF 开销。开销被限制在 1 到 65535。手工度量覆盖值若落在这个范围内，就替换计算值。可选路径把各接口开销相加。

引擎：`https://netengineerlab.com/tools/ospf-cost-calculator/js/engine.js`（`OspfCostEngine`，schema `ospf-cost-engine/1.0`），取于 2026-11-04。

## 公式

$$
\mathrm{cost} = \mathrm{clamp}\left(1,\ 65535,\ \mathrm{round}\left(\frac{B_{\mathrm{ref}}}{B_{\mathrm{if}}}\right)\right)
$$

`round` 可以是 `ceil`（默认）、`floor` 或 `round`（分别对应 `Math.ceil`、`Math.floor`、`Math.round`）。输入省略参考带宽时，默认值为 \(100000\,\mathrm{Mbit/s}\)。

处于活动状态的接口开销相加得到 `totalCost`。停用的接口不计入。路径开销是该路径上接口的同一求和。最佳路径是路径总和的最小值。ECMP 数量是有多少条路径等于这个最小值且不是无效路径。

## 变量

| 符号 | 引擎字段 | 单位 |
|---|---|---|
| \(B_{\mathrm{ref}}\) | `referenceBandwidthMbps` | Mbit/s |
| \(B_{\mathrm{if}}\) | `bandwidthMbps` | Mbit/s |
| 覆盖值 | `metricOverride` | 整数 1…65535，或留空 |
| 模式 | `calculationMode` | `ceil`、`floor` 或 `round` |

带宽必须是大于 0 的有限数，否则该行无效。

## 工程含义

这是常见 OSPF 实现使用的参考带宽度量，不是跳数，也不是 IS-IS 宽度量。分子和分母必须使用同一单位。引擎假定两者都是 Mbit/s，所以 10 Gbit/s 链路应输入 10000，而不是 10。默认使用向上取整，因为开销不用分数；比值为 1.01 时，`ceil` 模式得到 2，`floor` 模式得到 1。

## 算例

参考带宽 \(100000\,\mathrm{Mbit/s}\)，模式 `ceil`，无覆盖。

| 接口 | 带宽（Mbit/s） | 比值 | 开销 |
|---|---:|---:|---:|
| 千兆 | 1000 | 100 | 100 |
| 万兆 | 10000 | 10 | 10 |
| 快速以太网 | 100 | 1000 | 1000 |
| 400 Gbit/s | 400000 | 0.25 | 1 |

一条 10 Gbit/s 加一条 1 Gbit/s 的路径，开销为 \(10 + 100 = 110\)。

\(100000/3000 = 33.\overline{3}\) 时，`floor` 得到 33，`ceil` 得到 34，`round` 得到 33（正数上 `Math.round` 是半数远离零；这个比值不是恰好半数）。

边界：比参考带宽更快的接口，开销仍是 **1**，不是 0。覆盖值 50 替换计算开销。覆盖值 0 或 70000 是错误（`metric_override_out_of_range`）。非正带宽无效。

## 限制

- 不会从厂商 “bandwidth” CLI 字符串自动得到开销。数字必须已经是 Mbit/s。
- 不含 OSPF 区域、网络类型或 LSA 生成。
- 这里的 ECMP 指计算出的总和相等，不检查转发面是否会分担。
- 开销 65535 是钳位，不是在说链路不可用。

## 参考标准

引擎记录公式字符串 `cost = reference bandwidth / interface bandwidth`，以及界限 1…65535。生产页说明向上取整符合常见 Cisco 和 FRR 行为。本库没有为那句话去取 RFC 或厂商配置指南，所以外部引用仍为 **待定**。算术和钳位已按引擎核对。


## 在线计算器

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/ospf-cost-calculator/zh/

工具 ID：`ospf-cost-calculator`。

## 相关公式

- [STP 端口路径开销](stp-path-cost.zh-CN.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.zh-CN.md)

## 核对

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `ospf-cost-calculator` |
| 证据 | 生产 `js/engine.js` 的 `metricFor` 和 `calculate` |
| 方法 | 用 Python 的 `math.ceil` / `floor` 计算同一比值，再钳位 |
| 算例结果 | 参考 100000 Mbit/s、ceil：1 Gbit/s → 100；10 Gbit/s → 10；100 Mbit/s → 1000；400 Gbit/s → 1 |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
