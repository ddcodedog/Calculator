# Condensate from latent cooling load

## Overview

Condensate volume uses a fixed latent heat of 2450 kJ/kg and a density of 1 kg/L. A safety factor at least 1 multiplies the rate.

## Formula

$$
\dot V = (Q_{kW}/2450)\times 3600
$$

$$
\dot V_{design} = \dot V \times k
$$

\(\dot V\) is litres per hour. Litres per minute are that design rate divided by 60. Volume over a stated duration is design rate times hours. \(k\) must be at least 1.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q_{kW}\) | Latent load | kW |
| \(k\) | Safety factor | dimensionless |

## Engineering Principles

2450 kJ/kg is the latent heat stored in the script, and 1 kg/L is the density stored beside it. They are not looked up from a steam table at runtime.

## Worked Example

Defaults: 10 kW, 1 hour, safety 1.25.

$$
\dot V = 10/2450 \times 3600 = 14.69387755\ \text{L/h}
$$

$$
\dot V_{design} = 18.36734694\ \text{L/h} = 0.306122449\ \text{L/min}
$$

One hour at the design rate is 18.36734694 L.

Boundary: safety factor 1 returns 14.69387755 L/h. A safety factor below 1 is rejected. A load of 0 gives a rate of 0.

## Limitations

The result is condensate from the latent load only. Sensible load does not add water. Drain size, slope, and trap depth are not calculated.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/condensate-drain-planner/

## Related Formulas

- [HVAC cooling electrical energy](hvac-cooling-energy-cost.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `condensate-drain-planner` |
| Evidence | Production chunk latent heat 2450 kJ/kg, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 14.69387755 L/h base, 18.36734694 L/h design |
| Boundary | safety factor 1 removes the multiplier; k < 1 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
