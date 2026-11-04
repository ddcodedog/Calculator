# Battery energy and runtime

## Overview

Runtime is the watt-hours available between two states of charge, after state of health and discharge efficiency, divided by the load.

## Formula

$$
E = V \times Ah \times (SOC_{start}-SOC_{end}) \times SOH \times \eta
$$

$$
t = E / P
$$

States of charge and state of health are fractions. Efficiency is a fraction. The result \(t\) is in hours when \(E\) is in watt-hours and \(P\) is in watts.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(V\) | Battery voltage | V |
| \(Ah\) | Nameplate capacity | ampere-hour |
| \(SOC\) | State of charge | fraction |
| \(SOH\) | State of health | fraction |
| \(\eta\) | Discharge efficiency | fraction |
| \(P\) | Load | W |

## Engineering Principles

The energy uses the voltage as a constant. There is no Peukert exponent in this tool. End state of charge must be below the start, and both must lie in a range the script accepts as fractions.

## Worked Example

Example: 12 V, 100 Ah, state of charge from 1 to 0.2, state of health 1, efficiency 0.9, load 100 W.

$$
E = 12 \times 100 \times 0.8 \times 1 \times 0.9 = 864\ \text{Wh}
$$

$$
t = 864/100 = 8.64\ \text{h}
$$

Boundary: efficiency 1 with the same window stores \(12\times 100\times 0.8 = 960\) Wh and runs 9.6 h. A load of 0 is rejected. An end state of charge above the start is rejected.

## Limitations

Constant voltage ignores the discharge curve. The efficiency is one number for the whole window.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/battery-runtime/

## Related Formulas

- [Battery charging time](battery-charging-time.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `battery-runtime` (`TOOL-016`) |
| Evidence | Production chunk `3o1et8vioejmo.js`, watt-hour product, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 864 Wh and 8.64 h |
| Boundary | efficiency 1 gives 960 Wh; zero load is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
