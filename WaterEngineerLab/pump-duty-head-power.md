# Pump duty head and power

## Overview

Duty head is static head plus the total loss the user supplies. Hydraulic power uses 9806.65 times flow times that head. Shaft power divides by efficiency.

## Formula

$$
H = H_{static} + h_{loss}
$$

$$
P_{hyd} = 9806.65\, Q\, H
$$

$$
P_{shaft} = P_{hyd} / \eta
$$

Head must be positive and loss must be non-negative. Efficiency must lie in (0, 1]. The constant 9806.65 is \(1000 \times 9.80665\), so the power is for a fluid density of 1000 kg/m³.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Flow | m³/s |
| \(H_{static}, h_{loss}\) | Static head and supplied loss | m |
| \(\eta\) | Pump efficiency | fraction |

## Engineering Principles

Density is not an input. A fluid other than 1000 kg/m³ is outside this product. The HVAC pump page multiplies by the density the user types; this page does not.

## Worked Example

SI defaults: flow 0.05 m³/s, static head 18 m, loss 7 m, efficiency 0.75.

$$
H = 25\ \text{m}
$$

$$
P_{hyd} = 9806.65 \times 0.05 \times 25 = 12258.3125\ \text{W}
$$

$$
P_{shaft} = 16344.41667\ \text{W}
$$

Boundary: efficiency 1 returns the hydraulic power as the shaft power. A loss that drives the head to 0 or below is rejected.

## Limitations

The duty point is the entered flow at the entered head. There is no pump curve and no affinity-law resize.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/pump-duty-point-helper/

## Related Formulas

- [Residual pressure from a head balance](residual-pressure-head.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-013` |
| Evidence | Production duty-power function, factor 9806.65, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 25 m, 12258.3125 W hydraulic, 16344.41667 W shaft |
| Boundary | efficiency 1 returns hydraulic power; non-positive head is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
