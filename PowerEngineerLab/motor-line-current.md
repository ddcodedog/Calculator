# Three-phase motor line current

## Overview

Line current is output power divided by \(\sqrt{3}\), line voltage, efficiency, and power factor. Starting and planning currents are multiples of that current.

## Formula

$$
I = \frac{1000\, P_{kW}}{\sqrt{3}\, V_{LL}\, \eta\, pf}
$$

$$
I_{start} = I \times m
$$

$$
I_{plan} = I \times SF \times (1+margin)
$$

Power is entered in kilowatts and multiplied by 1000. Efficiency and power factor are fractions.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P_{kW}\) | Output power | kW |
| \(V_{LL}\) | Line-to-line voltage | V |
| \(\eta\) | Efficiency | fraction |
| \(pf\) | Power factor | fraction |
| \(m\) | Starting multiple | dimensionless |
| \(SF\) | Service factor | dimensionless |

## Engineering Principles

The English form defaults are 7.5 kW, 400 V, efficiency 0.9, power factor 0.85, start multiple 6, service factor 1.15, and margin 0.1. The planning current is not a breaker size. It is the product written above.

## Worked Example

English defaults:

$$
I = 7500 / (\sqrt{3}\times 400 \times 0.9 \times 0.85) = 14.15074189\ \text{A}
$$

Starting current is \(6 \times 14.15074189 = 84.90445135\) A. Planning current is \(14.15074189 \times 1.15 \times 1.1 = 17.90068849\) A.

Boundary: margin 0 and service factor 1 return the running current unchanged. Efficiency or power factor of 0 is rejected.

## Limitations

The formula is a single equivalent current. It does not include a service-factor temperature model or a code table of conductor ampacity.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/motor-current/

## Related Formulas

- [Shaft torque from power and speed](shaft-torque.md)
- [Induction-motor slip](induction-motor-slip.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `motor-current` (script id `BACKLOG-004`) |
| Evidence | Production chunk `2-fhldm9ukect.js`, English default inputs, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 14.15074189 A running, 84.90445135 A start, 17.90068849 A planned |
| Boundary | margin 0 and service factor 1 leave I unchanged; eta or pf of 0 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
