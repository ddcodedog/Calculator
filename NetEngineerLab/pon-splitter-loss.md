# PON splitter and link loss budget

## Overview

This page records the loss budget in the NetEngineerLab PON splitter calculator. The script adds fiber, splice, connector, and splitter losses, then compares the received level with the sensitivity and overload limits.

## Formula

The ideal split loss and the loss the user enters are separate:

$$
L_{ideal} = 10\log_{10}(r_1 r_2 r_3)
$$

$$
L_{splitter} = s_1 + s_2 + s_3
$$

$$
L_{excess} = \max(0, L_{splitter} - L_{ideal})
$$

$$
L_{physical} = \alpha L + N_s a_s + N_c a_c + L_{splitter} + L_{other}
$$

$$
L_{design} = L_{physical} + M + L_{resilience}
$$

$$
B = (P_{tx} - P_{sens}) - P_{penalty}
$$

$$
P_{rx} = P_{tx} - L_{physical}
$$

The ratio that belongs to an entered splitter loss is the table in the script: 4 dB→2, 7.5 dB→4, 10.5 dB→8, 14 dB→16, 17 dB→32, 20.5 dB→64, 24 dB→128. A value of 0 means a 1:1 stage. Resilience loss is aging + temperature + maintenance + protection. Each of those fields defaults to 0 when omitted.

## Variables

| Symbol | Meaning | Unit in the script |
|---|---|---|
| \(r_i\) | Split ratio implied by stage loss \(s_i\) | dimensionless |
| \(s_i\) | Entered stage loss | dB |
| \(\alpha\) | Fiber attenuation | dB/km |
| \(L\) | Distance | km |
| \(N_s, a_s\) | Splice count and loss each | count, dB |
| \(N_c, a_c\) | Connector count and loss each | count, dB |
| \(M\) | Design margin | dB |
| \(P_{tx}, P_{tx,max}\) | Transmit level and maximum transmit level | dBm |
| \(P_{sens}, P_{ol}\) | Sensitivity and overload | dBm |
| \(P_{penalty}\) | Penalty subtracted from the raw window | dB |

## Engineering Principles

The entered splitter loss is what the budget spends. The ideal loss only measures how far that entry sits above \(10\log_{10}\) of the ratio. Status is failed when remaining budget, sensitivity margin, or overload margin is negative. It is warning when any of those three is below 3 dB and still non-negative. Otherwise it is healthy. Values within \(10^{-9}\) of zero are treated as zero.

## Worked Example

Page defaults, two stages of 10.5 dB and a third stage of 0: ratios \(8 \times 8 \times 1 = 64\).

$$
L_{ideal} = 10\log_{10}(64) = 18.06179974\ \text{dB}
$$

$$
L_{excess} = 21 - 18.06179974 = 2.938200259\ \text{dB}
$$

Distance 10 km at 0.25 dB/km is 2.5 dB. Six splices at 0.10 dB and four connectors at 0.30 dB add 0.6 dB and 1.2 dB. Splitter loss is 21 dB. Physical loss is \(2.5 + 0.6 + 1.2 + 21 = 25.3\) dB. With margin 3 dB and resilience 0, design loss is 28.3 dB.

Transmit 3 dBm and sensitivity −30 dBm give a raw window of 33 dB. Penalty 1 dB leaves a standard budget of 32 dB. Remaining budget is \(32 - 28.3 = 3.7\) dB. Received power is \(3 - 25.3 = -22.3\) dBm. With maximum transmit 7 dBm the highest receive level is −18.3 dBm. Sensitivity margin is 7.7 dB. Overload margin against −8 dBm is 10.3 dB. All three margins are at least 3 dB, so the status is healthy.

Boundary: distance 0 km removes only the 2.5 dB fiber term. Physical loss becomes 22.8 dB and design loss becomes 25.8 dB. A non-positive attenuation, or a splitter loss that is not in the ratio table, is rejected.

## Limitations

The ratio table is a fixed map inside the script, not a measurement of a particular splitter. Excess loss is not added a second time; the budget already uses the entered splitter loss. The 3 dB healthy/warning cut is a script threshold.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/pon-splitter-loss/

## Related Formulas

- [PON maximum optical distance](pon-maximum-distance.md)
- [Optical link power budget](optical-power-budget.md)
- [Single-span fiber link loss](fiber-link-loss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `pon-splitter-loss` |
| Evidence | Production `js/engine.js`, function that builds physicalLoss and designLoss, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | physical 25.3 dB, design 28.3 dB, remaining 3.7 dB, status healthy |
| Boundary | zero distance drops the 2.5 dB fiber term; unknown splitter loss is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
