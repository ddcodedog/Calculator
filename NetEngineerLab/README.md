# NetEngineerLab Formula & Technical Topics

[← Back to repository README](../README.md)

## Domain

Network engineering calculators — fiber optics, RF/link budgets, IP and cabling planning tools.

**Production site:** [https://netengineerlab.com](https://netengineerlab.com)

## Topic index

Published topics: 12

GATE 3 batch 1. These files match production calculator code checked on 2026-11-04. They are not a complete set of the 46 NetEngineerLab tools. Status labels are defined in [FORMULA_VERIFICATION.md](../reports/FORMULA_VERIFICATION.md).

| Status | Document | Tool |
|--------|----------|------|
| VERIFIED | [Single-span fiber link loss](fiber-link-loss.md) | `fiber-loss` |
| VERIFIED | [Optical link power budget](optical-power-budget.md) | `optical-power-budget` |
| VERIFIED | [Fiber propagation delay and RTT](fiber-propagation-latency.md) | `fiber-latency-calculator` |
| VERIFIED | [Chromatic dispersion coefficient D(λ)](chromatic-dispersion.md) | `chromatic-dispersion-calculator` |
| VERIFIED | [OSPF interface cost](ospf-interface-cost.md) | `ospf-cost-calculator` |
| VERIFIED | [STP port path cost](stp-path-cost.md) | `stp-path-cost-calculator` |
| VERIFIED | [File transfer time from link rate](bandwidth-transfer-time.md) | `bandwidth-calculator` |
| VERIFIED | [MTU, MSS, and encapsulation overhead](mtu-mss-overhead.md) | `mtu-calculator` |
| VERIFIED | [DNS TTL window before a record change](dns-ttl-cache-window.md) | `dns-ttl-propagation-calculator` |
| VERIFIED | [Access-switch demand against uplink headroom](switch-uplink-safe-capacity.md) | `switch-uplink-oversubscription-calculator` |
| VERIFIED | [A cutover wait is not a fiber round trip](cutover-wait-versus-fiber-delay.md) | `dns-ttl-propagation-calculator` |
| VERIFIED | [Header bytes, then the safe uplink, then the clock](on-wire-bytes-at-safe-uplink.md) | `bandwidth-calculator` |

## Simplified Chinese editions

The same twelve topics, not counted in Published topics:

- [单段光纤链路损耗](fiber-link-loss.zh-CN.md)
- [光链路功率预算](optical-power-budget.zh-CN.md)
- [光纤传播时延与往返时间](fiber-propagation-latency.zh-CN.md)
- [色度色散系数 D(λ)](chromatic-dispersion.zh-CN.md)
- [OSPF 接口开销](ospf-interface-cost.zh-CN.md)
- [STP 端口路径开销](stp-path-cost.zh-CN.md)
- [由链路速率得到的文件传输时间](bandwidth-transfer-time.zh-CN.md)
- [MTU、MSS 与封装开销](mtu-mss-overhead.zh-CN.md)
- [记录变更前的 DNS TTL 窗口](dns-ttl-cache-window.zh-CN.md)
- [接入交换机需求与上行余量](switch-uplink-safe-capacity.zh-CN.md)
- [割接等待不是光纤往返时延](cutover-wait-versus-fiber-delay.zh-CN.md)
- [先把报头算进字节，再取安全上行，最后算时间](on-wire-bytes-at-safe-uplink.zh-CN.md)

## Online calculators

Each published topic links to its own production calculator. This index does not list every tool on the site.

## Contribution

See [CONTRIBUTING.md](../CONTRIBUTING.md). Do not invent formulas, standards, or tool URLs.
