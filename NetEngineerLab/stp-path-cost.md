# STP port path cost

Locale: en

Simplified Chinese edition: [STP 端口路径开销](stp-path-cost.zh-CN.md).

## Direct Answer

This note answers an STP path cost question: the long rate formula and the short rate table, then which path sum is smaller.

The STP Path Cost Calculator assigns a port path cost to each link speed and sums those costs for two candidate paths. The lower sum is the path this tool reports as preferred. A tie is reported as a warning because the bridge ID, not the cost, would break it.


## Overview

Engine: `https://netengineerlab.com/tools/stp-path-cost-calculator/js/engine.js` (`NELStpPathCostEngine`), fetched 2026-11-04.
## Formula

Long method (the engine comment identifies IEEE 802.1D-2004 / 802.1Q):

$$
\mathrm{cost}_{\mathrm{long}} = \mathrm{clamp}\left(1,\ 200000000,\ \mathrm{round}\left(\frac{2\times 10^{10}}{B_{\mathrm{Mbit/s}}\times 1000}\right)\right)
$$

`round` is JavaScript `Math.round` (half away from zero for positive values, implemented as floor of \(x+0.5\)). The speed is converted from Mbit/s to kbit/s by multiplying by 1000, so the denominator is the link rate in kbit/s.

Short method uses only this table. Any other speed returns an error (`short-undefined`) instead of an interpolated cost.

| Speed (Mbit/s) | Short cost |
|---:|---:|
| 4 | 250 |
| 10 | 100 |
| 16 | 62 |
| 100 | 19 |
| 1000 | 4 |
| 10000 | 2 |

Path totals are ordinary sums. The winner is A if total A is smaller, B if total B is smaller, otherwise `tie`.

## Variables

| Name | Engine field | Unit |
|---|---|---|
| Method | `method` | `long` or `short` |
| Path A, path B | `pathA`, `pathB` | text list of speeds in Mbit/s, separated by spaces, commas, or semicolons |

Each speed must be finite, greater than 0, and at most \(1.6\times 10^{6}\,\mathrm{Mbit/s}\). Each path needs 1 to 32 speeds.

## Engineering Principles

Root path cost is the sum of the costs of the ports on the path toward the root, not a count of hops. The long formula makes a faster link a smaller integer. The short table cannot rank speeds above 10 Gbit/s, so two 10 Gbit/s hops and one 1 Gbit/s hop can tie (2+2 versus 4) even though the long method separates them (2000+2000 versus 20000).

## Worked Example

Long method. Path A: `10000 10000`. Path B: `1000`.

1. \(2\times 10^{10} / (10000 \times 1000) = 2000\). Each 10 Gbit/s hop costs 2000.
2. \(2\times 10^{10} / (1000 \times 1000) = 20000\). The 1 Gbit/s hop costs 20000.
3. Total A = 4000. Total B = 20000. Winner **A**. Difference 16000.

The same speeds with the short method: path A is \(2+2=4\), path B is 4, winner **tie**, status **warning**.

Further long-method checks from the production page text: 10 Mbit/s → 2000000, 100 Mbit/s → 200000, 100 Gbit/s → 200, 400 Gbit/s → 50.

Boundary: short method with `100000` (100 Gbit/s) is rejected. Long-method cost never leaves 1…200000000. A path string with more than 32 numbers is rejected.

## Limitations

- No port priority, root bridge ID, or designated-bridge tie break. A tie stops at `tie`.
- Speeds are Mbit/s as typed. The engine does not parse “10G”.
- Short costs exist only for the six table rows.
- This does not configure a switch.

## Reference Standards

The production page links:

- IEEE 802.1D-2004: https://standards.ieee.org/ieee/802.1D/3387/
- IEEE 802.1t-2001: https://standards.ieee.org/ieee/802.1t/1043/
- IEEE 802.1D-1998: https://standards.ieee.org/ieee/802.1D/1029/
- IEEE 802.1Q: https://standards.ieee.org/ieee/802.1Q/10323/ — the page itself marks the clause number unverified
- Cisco STP technical note: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/5234-5.html

The long formula, the clamp, and the short table were checked against `engine.js`. The standards PDFs were not re-read in this pass. The page’s 802.1Q clause note should stay unverified.

## Online Calculator

https://netengineerlab.com/tools/stp-path-cost-calculator/

Inventory tool ID: `stp-path-cost-calculator`.

## Related Formulas

- [OSPF interface cost](ospf-interface-cost.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `stp-path-cost-calculator` |
| Evidence | Production `js/engine.js` `longCost`, `SHORT`, and `calculate` |
| Method | Recomputed \(2\times 10^{10}/(\mathrm{Mbit/s}\times 1000)\) and the short-table sums, including the page’s 10G+10G versus 1G case |
| Example result | Long totals 4000 vs 20000, winner A; short totals 4 vs 4, tie |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |