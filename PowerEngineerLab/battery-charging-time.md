# Battery charging time

## Overview

Charging time is the ampere-hour gap divided by current and efficiency, then multiplied by a taper factor.

## Formula

$$
t = \frac{Ah(SOC_{target}-SOC_{start})}{I\,\eta} \times k_{taper}
$$

Time is in hours when capacity is in ampere-hours and current is in amperes.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Ah\) | Capacity | Ah |
| \(SOC\) | State of charge | fraction |
| \(I\) | Charge current | A |
| \(\eta\) | Charge efficiency | fraction |
| \(k_{taper}\) | Taper multiplier | dimensionless |

## Engineering Principles

The taper factor is a user multiplier. It is not derived from a current schedule. Target state of charge must be above the start.

## Worked Example

Example: 100 Ah, state of charge 0.2 to 0.8, 20 A, efficiency 0.9, taper 1.2.

$$
t = 100\times 0.6 / (20\times 0.9) \times 1.2 = 4\ \text{h}
$$

Boundary: taper 1 with the same inputs gives \(60/18 = 3.333333333\) h. Current of 0 is rejected.

## Limitations

A constant current plus a scalar taper is not a CC-CV profile. Voltage limits are not computed.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/battery-charging-time/

## Related Formulas

- [Battery energy and runtime](battery-runtime.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `battery-charging-time` (`TOOL-017`) |
| Evidence | Production chunk `29ufvnj-ytaww.js`, Ah gap over current, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 4 h |
| Boundary | taper 1 gives 3.333333333 h; zero current is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
