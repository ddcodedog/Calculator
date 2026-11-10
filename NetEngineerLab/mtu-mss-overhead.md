# MTU、MSS 与封装开销

## 概述

MTU 计算器从底层 MTU 逐层减去封装，然后报告剩余的内层包、能放进其中的 TCP MSS，以及该包的以太网帧长。这是报头预算，不是路径 MTU 探测。

引擎：生产工具上的 `js/engine.js` 和 `js/mtu-library.js`，读于 2026-11-07。底层必须是至少 576 字节的有限数。更小的底层为 `underlay_mtu_out_of_range`。

## 公式

VLAN 开销是每个外层标签 4 字节，标签数是 `min(16, floor(count))`。若关闭严格 VLAN 记账，这些字节不从内层包中扣除。

$$
L_{\mathrm{inner}} = \max\left(0,\ M_{\mathrm{underlay}} - \sum_i \mathrm{bytes}_i\times\mathrm{count}_i\right)
$$

内层包里的固定报头：

| 协议 | 字节 |
|---|---:|
| IPv4 | 20 |
| IPv6 | 40 |
| TCP，无选项 | 20 |
| UDP | 8 |
| ICMP | 8 |

对外通告的 TCP MSS 是 \(\max(0, L_{\mathrm{inner}} - \mathrm{IP} - 20)\)。额外的 IP 报头字节和 TCP 选项只从实际 TCP 数据长度中扣除，不从通告 MSS 中扣除。工具报告的线上帧是 \(14 + \mathrm{VLAN} + \mathrm{payload} + 4\)（以太网头、标签、载荷、FCS）。

内层长度放不下 IP 头加 8 字节，或者希望保留的内层尺寸大于 \(L_{\mathrm{inner}}\) 时，路径失败。IPv6 低于 1280 字节会告警。IPv4 低于 576 会告警。余量落在 \([0, 40)\) 时增加 `low_headroom`。开销达到或超过 10% 时增加 `high_overhead`。

## 变量

| 名称 | 含义 | 单位 |
|---|---|---|
| 底层 MTU | 选定各层之前的外包上限 | 字节，≥ 576 |
| 各层 | 库中有名称的开销，各有字节数和个数 | 字节 |
| 希望的内层尺寸 | 你希望保住的载荷大小 | 字节 |
| 地址族 | 选择 20 字节或 40 字节的 IP 头 | IPv4 或 IPv6 |
| 路径数 | 少于 2 条路径时增加 `single_path` 告警 | 个 |

## 工程含义

MSS 是去掉 IP 头和 TCP 头之后剩下的部分，所以比内层 IPv4 包小 40 字节（20 + 20），IPv6 则小 60 字节。封装不改变这 40 或 60；它缩小的是这些报头所在的包。希望的尺寸等于有效内层尺寸时，没有多余字节留给选项，所以即使算术成功，余量为 0 仍是告警。

## 算例

PPPoE 预设：底层 1500 字节，一层 8 字节 PPPoE，希望的内层尺寸 1492，IPv4，无 VLAN，路径数 1。

1. \(L_{\mathrm{inner}} = 1500 - 8 = 1492\)。希望的尺寸与它相同，所以余量为 0。
2. 通告 MSS = \(1492 - 20 - 20 = 1452\) 字节。
3. UDP 载荷 = \(1492 - 20 - 8 = 1464\) 字节。ICMP 载荷同样是 1464。
4. 线上帧 = \(14 + 1492 + 4 = 1510\) 字节。
5. 开销 = \(8 / 1500 = 0.5333\%\)。

状态仍为 healthy。告警是 `low_headroom`（0 字节富余）和 `single_path`。二者都在工具的优先级 1 告警列表里，所以尺寸虽然放得下，风险标签仍是 P1。

边界：这条路径上希望的内层尺寸 1493 为 `desired_exceeds_effective`。底层 575 在任何层计算之前就被拒绝。

## 限制

- 层大小是库中的常数（PPPoE 8，GRE IPv4 24，VXLAN IPv4 50，WireGuard IPv4 60，MPLS 每个标签 4）。它们不是在现网隧道上测到的。
- 未列入所选层的选项、厂商标签和双重封装会被略去。
- 工具不发送数据包。

## 参考标准

页面把以太网、IP 和 TCP 的报头大小当作引擎里的固定常数。标准文件本身没有重读。状态：待定。

## 中文工具页

同一工具的中文页已在 2026-11-10 的站点地图中，打开后标题为中文：https://netengineerlab.com/tools/mtu-calculator/zh/

下一节的英文 URL 是验证记录中的生产页。引擎脚本从该路径读取，中文页没有另行抽取。

## Online Calculator

在 MTU 计算器中运行同一 PPPoE 案例：

https://netengineerlab.com/tools/mtu-calculator/

## 相关公式

- [由链路速率得到的文件传输时间](bandwidth-transfer-time.md)
- [光链路功率预算](optical-power-budget.md)

## Verification

| 项 | 值 |
|---|---|
| 来源工具 | NetEngineerLab MTU 计算器 |
| 证据 | 生产 `js/engine.js` 的内层长度、MSS 和线上帧表达式；PPPoE 大小来自 `js/mtu-library.js` |
| 方法 | 重算 1500 − 8 以及 IPv4 报头拆分 |
| 算例结果 | 内层 1492，通告 MSS 1452，线上 1510，开销 0.5333% |
| 日期 | 2026-11-07 |
| 文档版本 | 1.0.0 |
| Status | VERIFIED |
