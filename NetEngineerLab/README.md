# NetEngineerLab 公式与技术专题

[← 返回仓库说明](../README.md)

## 范围

网络工程计算器：光纤、链路预算、IP 与布线规划。

**生产站点：** [https://netengineerlab.com](https://netengineerlab.com)

## 专题索引

Published topics: 12

这些文件对应已核对的生产计算器。它们不是该站全部工具。状态说明见 [FORMULA_VERIFICATION.md](../reports/FORMULA_VERIFICATION.md)。各篇正文给出已核实的中文工具页；下面表格不另计篇数。

| 状态 | 文档 | 工具 |
|--------|----------|------|
| VERIFIED | [单段光纤链路损耗](fiber-link-loss.md) | `fiber-loss` |
| VERIFIED | [光链路功率预算](optical-power-budget.md) | `optical-power-budget` |
| VERIFIED | [光纤传播时延与往返时间](fiber-propagation-latency.md) | `fiber-latency-calculator` |
| VERIFIED | [色度色散系数 D(λ)](chromatic-dispersion.md) | `chromatic-dispersion-calculator` |
| VERIFIED | [OSPF 接口开销](ospf-interface-cost.md) | `ospf-cost-calculator` |
| VERIFIED | [STP 端口路径开销](stp-path-cost.md) | `stp-path-cost-calculator` |
| VERIFIED | [由链路速率得到的文件传输时间](bandwidth-transfer-time.md) | `bandwidth-calculator` |
| VERIFIED | [MTU、MSS 与封装开销](mtu-mss-overhead.md) | `mtu-calculator` |
| VERIFIED | [记录变更前的 DNS TTL 窗口](dns-ttl-cache-window.md) | `dns-ttl-propagation-calculator` |
| VERIFIED | [接入交换机需求与上行余量](switch-uplink-safe-capacity.md) | `switch-uplink-oversubscription-calculator` |
| VERIFIED | [割接等待不是光纤往返时延](cutover-wait-versus-fiber-delay.md) | `dns-ttl-propagation-calculator` |
| VERIFIED | [先把报头算进字节，再取安全上行，最后算时间](on-wire-bytes-at-safe-uplink.md) | `bandwidth-calculator` |

## 在线计算器

每篇专题有自己的生产计算器链接。本索引不列出站点上的全部工具。`## Online Calculator` 仍使用验证记录里的英文生产 URL。同工具的 `/zh/` 页面在各篇里另行标出，并在 2026-11-10 核对过站点地图与页面标题。

## 贡献

见 [CONTRIBUTING.md](../CONTRIBUTING.md)。不要编造公式、标准或工具 URL。
