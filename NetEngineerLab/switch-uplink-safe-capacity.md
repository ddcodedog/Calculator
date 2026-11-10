# Access-switch demand against uplink headroom

Locale: en

Simplified Chinese edition: [接入交换机需求与上行余量](switch-uplink-safe-capacity.zh-CN.md).

## Direct Answer

This note answers an access-switch uplink question: demand against uplink capacity and the headroom that remains.

An access switch can offer far more edge bandwidth than its uplinks can carry. This tool multiplies port count, port rate, utilization, concurrency, and overhead into a demand, compares that demand with the uplink capacity and with a safer fraction of it, and reports how many uplinks the target fraction would need. The example leaves out `engineering`, `peakPorts`, `growthPct`, `burstPct`, and `failedUplinks`, so the engine returns the short baseline object.


## Overview

Production `js/engine.js` for the switch-uplink tool, model `switch-uplink-engine/2.0.0`, read 2026-11-08. Displayed gigabit figures use JavaScript `toFixed` and then a unary plus, so 4.536 becomes 4.54 at two decimals (https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/).
## Formula

Demand and the burst-adjusted peak, in Mbit/s:

$$
D = N\,R\,\frac{u}{100}\,\frac{c}{100}\left(1+\frac{h}{100}\right), \qquad D_{\mathrm{peak}} = D\left(1+\frac{b}{100}\right)
$$

Capacity and the safe slice:

$$
C = R_{\mathrm{up}}\,N_{\mathrm{up}}, \qquad C_{\mathrm{safe}} = C\,\frac{t}{100}
$$

Oversubscription is \((N R / C)\) shown to one decimal with `:1`. Utilization percent is \(100\,D_{\mathrm{peak}}/C\) to one decimal. Required uplinks are

$$
N_{\mathrm{req}} = \left\lceil \frac{D_{\mathrm{peak}}}{R_{\mathrm{up}}\,t/100} \right\rceil
$$

Spare gigabits are \((C_{\mathrm{safe}}-D_{\mathrm{peak}})/1000\), two decimals. Status is `fail` when no uplink capacity exists or when the peak exceeds capacity, `pass` when the peak is at or under the safe slice, and `warning` when the peak sits between the safe slice and full capacity. Inputs must be finite. Port count, both rates, uplink count, utilization, concurrency, and target must be > 0. Utilization, concurrency, and target must be ≤ 100. Overhead must be ≥ 0.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Ports | Access ports in the model | count |
| Port rate | Each access port | Mbit/s |
| Utilization | Fraction of port rate treated as busy | % |
| Concurrency | Fraction of ports busy together | % |
| Overhead | Extra on the demand | % |
| Uplink rate | Each uplink | Mbit/s |
| Uplinks | Active uplinks | count |
| Target | Safe fraction of uplink capacity | % |
| Burst | Extra on the demand; 0 in the short example | % |

## Engineering Principles

Oversubscription here is nameplate access bandwidth divided by uplink capacity. It ignores utilization. The demand path is the one that includes utilization, concurrency, and overhead, and that is what the safe-capacity test uses. A result under the target is planning headroom inside this model. It is not a queueing delay and not a promise about microbursts the burst field was left at zero to exclude.

## Worked Example

24 access ports at 1000 Mbit/s, 30% utilization, 60% concurrency, 5% overhead, two 10,000 Mbit/s uplinks, 70% target, burst 0.

1. Demand = \(24\times 1000\times 0.30\times 0.60\times 1.05 = 4536\) Mbit/s, which is 4.536 Gbit/s and displays as 4.54.
2. Peak equals demand because burst is 0. Capacity = \(10000\times 2 = 20000\) Mbit/s, displayed 20 Gbit/s. Safe slice = \(0.70\times 20 = 14\) Gbit/s.
3. Oversubscription = \(24000/20000 = 1.2\), displayed `1.2:1`.
4. Utilization = \(4536/20000\times 100 = 22.68\), displayed 22.7%.
5. Required uplinks = \(\lceil 4536/7000\rceil = 1\). Spare = \((14000-4536)/1000 = 9.464\), displayed 9.46 Gbit/s.
6. Peak is under the safe slice, two uplinks are active, and burst is 0, so status is `pass`.

Boundary: 48 ports at 1000 Mbit/s, utilization 100%, concurrency 100%, overhead 0, one 10,000 Mbit/s uplink, target 70%, burst 0. Peak is 48 Gbit/s against 10 Gbit/s of capacity, so status is `fail`. Required uplinks become \(\lceil 48000/7000\rceil = 7\).

## Limitations

- The short return does not run the N-1 or growth scenarios. Those appear only after one of the engineering keys is present.
- Utilization and concurrency are inputs. The tool does not read switch counters.
- `toFixed` display is not the exact demand. Keep 4536 Mbit/s if you chain another calculation.

## Reference Standards

No IEEE or vendor capacity standard is applied inside the engine. Status: pending.
## Online Calculator

Enter the 24-port, two-uplink case on the production page:

https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/

## Related Formulas

- [OSPF interface cost](ospf-interface-cost.md)
- [STP port path cost](stp-path-cost.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `switch-uplink-oversubscription-calculator` |
| Evidence | Production `js/engine.js`, short return when engineering keys are omitted |
| Method | Node replay of demand, `toFixed`, `Math.ceil`, and the status branches |
| Example result | 4.54 Gbit/s demand, 1.2:1, 22.7% util, 1 uplink required, 9.46 Gbit/s spare, pass |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |