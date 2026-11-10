# STP 端口路径开销

## 概述

STP 路径开销计算器按链路速率给每个端口赋路径开销，再把两条候选路径的开销分别相加。和较小的那条，就是本工具报告的优先路径。和相等时报告为告警，因为打破平局的是桥 ID，不是开销。

引擎：`https://netengineerlab.com/tools/stp-path-cost-calculator/js/engine.js`（`NELStpPathCostEngine`），取于 2026-11-04。

## 公式

长方法（引擎注释标明 IEEE 802.1D-2004 / 802.1Q）：

$$
\mathrm{cost}_{\mathrm{long}} = \mathrm{clamp}\left(1,\ 200000000,\ \mathrm{round}\left(\frac{2\times 10^{10}}{B_{\mathrm{Mbit/s}}\times 1000}\right)\right)
$$

`round` 是 JavaScript 的 `Math.round`（正数半数远离零，实现为对 \(x+0.5\) 下取整）。速率从 Mbit/s 乘以 1000 变成 kbit/s，所以分母是以 kbit/s 表示的链路速率。

短方法只用下表。其他速率返回错误（`short-undefined`），不插值。

| 速率（Mbit/s） | 短开销 |
|---:|---:|
| 4 | 250 |
| 10 | 100 |
| 16 | 62 |
| 100 | 19 |
| 1000 | 4 |
| 10000 | 2 |

路径总和是普通加法。A 的总和更小则胜者为 A，B 更小则胜者为 B，否则为 `tie`。

## 变量

| 名称 | 引擎字段 | 单位 |
|---|---|---|
| 方法 | `method` | `long` 或 `short` |
| 路径 A、路径 B | `pathA`，`pathB` | 以空格、逗号或分号分隔的 Mbit/s 速率文本 |

每个速率必须有限、大于 0，且不超过 \(1.6\times 10^{6}\,\mathrm{Mbit/s}\)。每条路径需要 1 到 32 个速率。

## 工程含义

根路径开销是朝向根的路径上各端口开销之和，不是跳数。长公式使更快的链路得到更小的整数。短表不能给高于 10 Gbit/s 的速率排序，所以两跳 10 Gbit/s 和一跳 1 Gbit/s 可能打平（2+2 对 4），而长方法能分开它们（2000+2000 对 20000）。

## 算例

长方法。路径 A：`10000 10000`。路径 B：`1000`。

1. \(2\times 10^{10} / (10000 \times 1000) = 2000\)。每跳 10 Gbit/s 的开销为 2000。
2. \(2\times 10^{10} / (1000 \times 1000) = 20000\)。1 Gbit/s 那一跳的开销为 20000。
3. A 的总和为 4000。B 的总和为 20000。胜者 **A**。差为 16000。

同样速率用短方法：路径 A 为 \(2+2=4\)，路径 B 为 4，胜者 **tie**，状态 **warning**。

生产页文字中的其他长方法核对：10 Mbit/s → 2000000，100 Mbit/s → 200000，100 Gbit/s → 200，400 Gbit/s → 50。

边界：短方法遇到 `100000`（100 Gbit/s）会被拒绝。长方法开销不会离开 1…200000000。路径字符串超过 32 个数会被拒绝。

## 限制

- 不含端口优先级、根桥 ID 或指定桥的平局处理。平局停在 `tie`。
- 速率按输入的 Mbit/s。引擎不解析 “10G”。
- 短开销只存在于表中的六行。
- 这不会去配置交换机。

## 参考标准

生产页链接：

- IEEE 802.1D-2004：https://standards.ieee.org/ieee/802.1D/3387/
- IEEE 802.1t-2001：https://standards.ieee.org/ieee/802.1t/1043/
- IEEE 802.1D-1998：https://standards.ieee.org/ieee/802.1D/1029/
- IEEE 802.1Q：https://standards.ieee.org/ieee/802.1Q/10323/ 。页面自己把条款号标为未核实
- Cisco STP 技术说明：https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/5234-5.html

长公式、钳位和短表已对照 `engine.js`。这一轮没有重读标准 PDF。页面上关于 802.1Q 条款的说明应保持未核实。

## 中文工具页

同一工具的中文页已在 2026-11-10 的站点地图中，打开后标题为中文：https://netengineerlab.com/tools/stp-path-cost-calculator/zh/

下一节的英文 URL 是验证记录中的生产页。引擎脚本从该路径读取，中文页没有另行抽取。

## Online Calculator

https://netengineerlab.com/tools/stp-path-cost-calculator/

工具 ID：`stp-path-cost-calculator`。

## 相关公式

- [OSPF 接口开销](ospf-interface-cost.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.md)

## Verification

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `stp-path-cost-calculator` |
| 证据 | 生产 `js/engine.js` 的 `longCost`、`SHORT` 和 `calculate` |
| 方法 | 重算 \(2\times 10^{10}/(\mathrm{Mbit/s}\times 1000)\) 以及短表求和，包括页面上的 10G+10G 对 1G |
| 算例结果 | 长方法总和 4000 对 20000，胜者 A；短方法总和 4 对 4，平局 |
| 日期 | 2026-11-04 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
