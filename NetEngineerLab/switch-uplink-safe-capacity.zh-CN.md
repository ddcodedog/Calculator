# 接入交换机需求与上行余量

本文是同目录英文稿的简体中文版，英文原文保持不变：[Access-switch demand against uplink headroom](switch-uplink-safe-capacity.md)。

## 概述

接入交换机可以提供远大于上行承载能力的边缘带宽。这个工具把端口数、端口速率、利用率、并发和开销乘成需求，再把需求与上行容量、以及容量中更安全的一部分比较，并报告目标比例需要多少条上行。算例留空 `engineering`、`peakPorts`、`growthPct`、`burstPct` 和 `failedUplinks`，所以引擎返回短基线对象。

交换机上行工具的生产 `js/engine.js`，模型 `switch-uplink-engine/2.0.0`，读于 2026-11-08。显示的吉比特数先用 JavaScript `toFixed`，再做一元加号，所以两位小数时 4.536 变成 4.54。

## 公式

需求和经突发调整的峰值，单位 Mbit/s：

$$
D = N\,R\,\frac{u}{100}\,\frac{c}{100}\left(1+\frac{h}{100}\right), \qquad D_{\mathrm{peak}} = D\left(1+\frac{b}{100}\right)
$$

容量和安全切片：

$$
C = R_{\mathrm{up}}\,N_{\mathrm{up}}, \qquad C_{\mathrm{safe}} = C\,\frac{t}{100}
$$

超售比是 \((N R / C)\)，显示到一位小数并带 `:1`。利用率百分比是 \(100\,D_{\mathrm{peak}}/C\)，到一位小数。所需上行条数为

$$
N_{\mathrm{req}} = \left\lceil \frac{D_{\mathrm{peak}}}{R_{\mathrm{up}}\,t/100} \right\rceil
$$

富余吉比特是 \((C_{\mathrm{safe}}-D_{\mathrm{peak}})/1000\)，两位小数。没有上行容量，或峰值超过容量时，状态为 `fail`；峰值不超过安全切片时为 `pass`；峰值位于安全切片和满容量之间时为 `warning`。输入必须有限。端口数、两种速率、上行条数、利用率、并发和目标必须 > 0。利用率、并发和目标必须 ≤ 100。开销必须 ≥ 0。

## 变量

| 名称 | 含义 | 单位 |
|---|---|---|
| 端口 | 模型中的接入端口 | 个 |
| 端口速率 | 每个接入端口 | Mbit/s |
| 利用率 | 当作忙碌的端口速率比例 | % |
| 并发 | 同时忙碌的端口比例 | % |
| 开销 | 加在需求上的额外部分 | % |
| 上行速率 | 每条上行 | Mbit/s |
| 上行条数 | 活动上行 | 个 |
| 目标 | 上行容量中的安全比例 | % |
| 突发 | 加在需求上的额外部分；短算例中为 0 | % |

## 工程含义

这里的超售比是接入标称带宽除以上行容量。它不考虑利用率。需求路径才计入利用率、并发和开销，安全容量检验用的是这条路径。低于目标的结果是本模型内部的规划余量。它不是排队时延，也不是对微突发的承诺；突发字段留在 0，就是为了把微突发留在模型外面。

## 算例

24 个接入端口，每个 1000 Mbit/s，利用率 30%，并发 60%，开销 5%，两条 10,000 Mbit/s 上行，目标 70%，突发 0。

1. 需求 = \(24\times 1000\times 0.30\times 0.60\times 1.05 = 4536\) Mbit/s，即 4.536 Gbit/s，显示为 4.54。
2. 突发为 0，所以峰值等于需求。容量 = \(10000\times 2 = 20000\) Mbit/s，显示 20 Gbit/s。安全切片 = \(0.70\times 20 = 14\) Gbit/s。
3. 超售比 = \(24000/20000 = 1.2\)，显示 `1.2:1`。
4. 利用率 = \(4536/20000\times 100 = 22.68\)，显示 22.7%。
5. 所需上行 = \(\lceil 4536/7000\rceil = 1\)。富余 = \((14000-4536)/1000 = 9.464\)，显示 9.46 Gbit/s。
6. 峰值低于安全切片，两条上行都活动，突发为 0，所以状态为 `pass`。

边界：48 个端口，每个 1000 Mbit/s，利用率 100%，并发 100%，开销 0，一条 10,000 Mbit/s 上行，目标 70%，突发 0。峰值 48 Gbit/s，容量 10 Gbit/s，状态为 `fail`。所需上行变为 \(\lceil 48000/7000\rceil = 7\)。

## 限制

- 短返回不计算 N-1 或增长情景。那些只在出现某个工程键之后才出现。
- 利用率和并发是输入。工具不读取交换机计数器。
- `toFixed` 的显示值不是精确需求。若要接到下一步计算，保留 4536 Mbit/s。

## 参考标准

引擎内部没有采用 IEEE 或厂商的容量标准。状态：待定。


## Online Calculator

在生产页输入 24 端口、两条上行的案例：

中文工具页。2026-11-10 已在站点地图中核对，页面标题为中文。计算引擎仍取自英文路径下的脚本。

https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/zh/

## 相关公式

- [OSPF 接口开销](ospf-interface-cost.zh-CN.md)
- [STP 端口路径开销](stp-path-cost.zh-CN.md)

## Verification

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab `switch-uplink-oversubscription-calculator` |
| 证据 | 生产 `js/engine.js`；省略工程键时的短返回 |
| 方法 | 用 Node 重放需求、`toFixed`、`Math.ceil` 和状态分支 |
| 算例结果 | 需求 4.54 Gbit/s，1.2:1，利用率 22.7%，需要 1 条上行，富余 9.46 Gbit/s，状态 pass |
| 日期 | 2026-11-08 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
