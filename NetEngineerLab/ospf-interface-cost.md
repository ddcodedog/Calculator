# OSPF interface cost

Locale: en

Simplified Chinese edition: [OSPF 接口开销](ospf-interface-cost.zh-CN.md).

## Direct Answer

This note answers an OSPF interface cost question: reference bandwidth divided by link rate, then the integer cost clamp.

The OSPF Cost Calculator turns a reference bandwidth and an interface bandwidth, both in Mbit/s, into an integer OSPF cost. Costs are clamped to the range 1 through 65535. A manual metric override replaces the calculated cost when it is inside that range. Optional paths sum the costs of their interfaces.


## Overview

Engine: `https://netengineerlab.com/tools/ospf-cost-calculator/js/engine.js` (`OspfCostEngine`, schema `ospf-cost-engine/1.0`), fetched 2026-11-04.
## Formula

$$
\mathrm{cost} = \mathrm{clamp}\left(1,\ 65535,\ \mathrm{round}\left(\frac{B_{\mathrm{ref}}}{B_{\mathrm{if}}}\right)\right)
$$

`round` is `ceil` (default), `floor`, or `round` (`Math.ceil`, `Math.floor`, or `Math.round`). Default reference bandwidth, when the input omits it, is \(100000\,\mathrm{Mbit/s}\).

Active interface costs sum to `totalCost`. Disabled interfaces are excluded. Path cost is the same sum over that path’s interfaces. The best path is the minimum path total. ECMP count is how many paths share that minimum and are not invalid.

## Variables

| Symbol | Engine field | Unit |
|---|---|---|
| \(B_{\mathrm{ref}}\) | `referenceBandwidthMbps` | Mbit/s |
| \(B_{\mathrm{if}}\) | `bandwidthMbps` | Mbit/s |
| override | `metricOverride` | integer 1…65535, or empty |
| mode | `calculationMode` | `ceil`, `floor`, or `round` |

Bandwidth must be a finite number greater than 0 or the row is invalid.

## Engineering Principles

This is the reference-bandwidth metric used by common OSPF implementations, not a hop count and not IS-IS wide metrics. The numerator and denominator must use the same unit. The engine assumes Mbit/s for both, so a 10 Gbit/s link is entered as 10000, not 10. Ceiling is the default because fractional costs are not used; a ratio of 1.01 becomes 2 in `ceil` mode and 1 in `floor` mode.

## Worked Example

Reference \(100000\,\mathrm{Mbit/s}\), mode `ceil`, no overrides.

| Interface | Bandwidth (Mbit/s) | Ratio | Cost |
|---|---:|---:|---:|
| Gigabit | 1000 | 100 | 100 |
| Ten-gigabit | 10000 | 10 | 10 |
| Fast Ethernet | 100 | 1000 | 1000 |
| 400 Gbit/s | 400000 | 0.25 | 1 |

A path of one 10 Gbit/s hop plus one 1 Gbit/s hop has cost \(10 + 100 = 110\).

`floor` mode on a \(100000/3000 = 33.\overline{3}\) ratio yields 33. `ceil` yields 34. `round` yields 33 (`Math.round` half-up on positive numbers; this ratio is not a halfway case).

Boundary: any interface faster than the reference still has cost **1**, not 0. An override of 50 replaces the calculated cost. An override of 0 or 70000 is an error (`metric_override_out_of_range`). A non-positive bandwidth is invalid.

## Limitations

- No auto-cost from a vendor “bandwidth” CLI string. The number must already be Mbit/s.
- No OSPF area, network type, or LSA generation.
- ECMP here means equal computed totals, not a check that the forwarding plane will load-share.
- Cost 65535 is a clamp, not a statement that the link is unusable.

## Reference Standards

The engine records the formula string `cost = reference bandwidth / interface bandwidth` and the bounds 1…65535. The production page states that ceiling matches common Cisco and FRR behavior. This library did not fetch an RFC or a vendor configuration guide for that sentence, so the external citation stays **pending**. The arithmetic and the clamp are verified from the engine.

## Online Calculator

https://netengineerlab.com/tools/ospf-cost-calculator/

Inventory tool ID: `ospf-cost-calculator`.

## Related Formulas

- [STP port path cost](stp-path-cost.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `ospf-cost-calculator` |
| Evidence | Production `js/engine.js` `metricFor` and `calculate` |
| Method | Python `math.ceil` / `floor` on the same ratios, then clamp |
| Example result | 1 Gbit/s → 100; 10 Gbit/s → 10; 100 Mbit/s → 1000; 400 Gbit/s → 1, at reference 100000 Mbit/s, ceil |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |