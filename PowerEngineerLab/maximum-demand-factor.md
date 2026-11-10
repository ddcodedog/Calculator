# Demand factor from maximum and connected load

Locale: en

## Direct Answer

Demand factor in this calculator is the highest demand divided by the connected load, both in kW. It is a different ratio from the load factor already published for this site, which divides average power by peak power inside one energy interval. A maximum that is larger than the connected load is rejected. The tool does not apply a code table of demand factors for dwellings or kitchens.


## Overview

Production demand-factor chunk, tool id `BACKLOG-028`, read 2026-11-08 (https://powerengineerlab.com/calculators/demand-factor/).
## Formula

$$
\mathrm{DF} = \frac{P_{\max}}{P_{\mathrm{connected}}}, \qquad \mathrm{DF}_{\%} = 100\times\mathrm{DF}
$$

Connected load must be > 0. Maximum demand must be ≥ 0. Both must be finite. If \(P_{\max} > P_{\mathrm{connected}}\), the result is `BOUNDARY` and no ratio is returned. The check message in the chunk says this comparison is the model’s selected boundary, not a general design approval.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Maximum demand | Highest demand entered for the same load boundary | kW |
| Connected load | Sum of the connected load on that boundary | kW |

## Engineering Principles

The ratio is dimensionless. 0.28 means the highest demand you entered is 28% of the connected load you entered. It says nothing about how long that maximum lasted, so it cannot be substituted for a load factor. Zero maximum demand with a positive connected load is allowed and returns 0.

## Worked Example

A small workshop nameplate adds to 150 kW. The highest demand recorded on that same list is 42 kW.

1. Demand factor = \(42/150 = 0.28\).
2. Percent = 28%.

Boundary: 160 kW maximum against the same 150 kW connected load returns `BOUNDARY` and no factor. Connected load of 0 is `DOMAIN`. A negative maximum is rejected before the division.

## Limitations

- Both inputs are typed. The page does not read a panel schedule.
- There is no diversity table, no continuous-load multiplier, and no service-size recommendation.
- Do not compare this 0.28 with a load factor computed from kWh.

## Reference Standards

The chunk does not attach a NEC or IEC table. Those demand-factor tables were not used. Status: pending.
## Online Calculator

Check 42 kW over 150 kW on the production calculator:

https://powerengineerlab.com/calculators/demand-factor/

## Related Formulas

- [Same-interval load factor](interval-load-factor.md)
- [DC Ohm’s law](ohms-law.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab demand-factor calculator |
| Evidence | Production chunk divides maximumDemandKw by connectedLoadKw and rejects maximum > connected |
| Method | Recomputed 42/150 and the 160 kW rejection |
| Example result | 0.28, which is 28% |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |