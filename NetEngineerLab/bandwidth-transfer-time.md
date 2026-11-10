# File transfer time from link rate

Simplified Chinese edition: [由链路速率得到的文件传输时间](bandwidth-transfer-time.zh-CN.md).

## Overview

The bandwidth calculator answers four planning questions from the same rate model: how long a file takes to cross a link, how much link rate a deadline needs, how many concurrent users fit, and how much volume a rate moves in a period. This note walks the transfer-time path, which is the one most people open first.

Rates are decimal SI. 1 Mbps is \(1\times 10^{6}\) bit/s, not \(2^{20}\). File size can be decimal (kB, MB) or IEC (KiB, MiB). The engine is `js/engine.js` with `data/bandwidth-units.js` on the production tool, read 2026-11-07 (https://netengineerlab.com/tools/bandwidth-calculator/).

## Formula

Efficiency and utilization are each clamped to 0…100 and then divided by 100. Their product is the combined payload fraction:

$$
\eta = \frac{\mathrm{efficiency}}{100}\times\frac{\mathrm{utilization}}{100}
$$

With \(B\) the link rate in bit/s, \(S\) the file size in bytes, \(N\) the concurrent transfers (`max(1, floor(count))`), \(R\) the round-trip time in milliseconds, and \(k\) the setup RTTs:

$$
t_{\mathrm{ser}} = \frac{8S}{B\,\eta / N}, \qquad t_{\mathrm{setup}} = \frac{R\,k}{1000}, \qquad t = t_{\mathrm{ser}}+t_{\mathrm{setup}}
$$

A non-finite input is invalid. Combined fraction below 0.5 is a warning, not a different formula. The burst factor used by the concurrent-user mode is not part of transfer time.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| File size | Decimal or IEC, converted to bytes | B |
| Link rate | Decimal SI | bit/s |
| Efficiency, utilization | Clamped 0…100, then used as fractions | % |
| Concurrent transfers | At least 1 after `floor` | count |
| RTT and setup RTTs | Added as \(R k / 1000\) | ms, count |

## Engineering Principles

Serialization time is file bits divided by the share of the link that one transfer actually gets. Protocol efficiency and a utilization cap both shrink that share, so they multiply. Setup delay is a fixed number of round trips; it does not grow with the file. Splitting one file across \(N\) concurrent transfers divides the payload rate by \(N\), which makes one file slower, not faster. That field is a contention model, not a speedup.

## Worked Example

File 100 MB decimal (\(100\times 10^{6}\) bytes), link 100 Mbps, one transfer, zero RTT.

1. File bits = \(800\times 10^{6}\).
2. Ideal efficiency 100% and utilization 100% give \(\eta = 1\).
3. \(t = 800\times 10^{6} / 100\times 10^{6} = 8\) seconds. Setup is 0.

Same file and rate with the Ethernet preset values in the tool: efficiency 95%, utilization 90%, RTT 1 ms, one setup RTT.

1. \(\eta = 0.95\times 0.90 = 0.855\).
2. Payload rate = \(85.5\times 10^{6}\) bit/s.
3. \(t_{\mathrm{ser}} = 800\times 10^{6} / 85.5\times 10^{6} = 9.356725146\) seconds.
4. \(t_{\mathrm{setup}} = 0.001\) second.
5. Total \(9.357725146\) seconds.

Boundary: efficiency 0 or utilization 0 makes \(\eta = 0\), and the transfer-time path reports a non-finite time. Required-bandwidth mode also returns infinity when the deadline is shorter than the setup delay.

## Limitations

- No TCP slow start, loss, or application pacing. Setup is a flat RTT count.
- Concurrent transfers share the link equally. They do not stripe one file faster.
- A result under these inputs is not a throughput test of a live path.

## Reference Standards

No standards PDF was re-read for this note. The SI decimal rate table is the one in `bandwidth-units.js`. Status of the cited documents: pending.
## Online Calculator

The same inputs can be typed into the bandwidth calculator:

https://netengineerlab.com/tools/bandwidth-calculator/

## Related Formulas

- [MTU, MSS, and encapsulation overhead](mtu-mss-overhead.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab bandwidth calculator |
| Evidence | Production `js/engine.js` transfer-time path and `data/bandwidth-units.js` |
| Method | Recomputed 100 MB decimal at 100 Mbps, ideal and Ethernet-preset efficiency |
| Example result | 8 s ideal; 9.357725146 s with 95% × 90% and 1 ms setup |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
