# Series RC time constant

## Overview

The RC calculator multiplies resistance by capacitance and then evaluates the exponential charge or discharge voltage at the entered time.

## Formula

$$
\tau = RC
$$

Charge:

$$
v_C = V_0 (1 - e^{-t/\tau})
$$

Discharge:

$$
v_C = V_0 e^{-t/\tau}
$$

Capacitance is entered in microfarads and multiplied by \(10^{-6}\) before the product. The fraction of the step that has occurred is \(v_C/V_0\) on charge and \(1-v_C/V_0\) on discharge.

## Variables

| Symbol | Meaning | Unit after conversion |
|---|---|---|
| \(R\) | Resistance | ohm |
| \(C\) | Capacitance | farad |
| \(V_0\) | Initial or source voltage | volt |
| \(t\) | Time | second |

## Engineering Principles

The product \(RC\) is the only time constant. The page does not add source resistance to a separate load, and it does not model a second energy-storage element. Charge and discharge are two branches of the same script.

## Worked Example

Load example: charge, \(R = 1000\) ohm, \(C = 1000\) µF, \(V_0 = 10\) V, \(t = 1\) s.

$$
\tau = 1000 \times 1000 \times 10^{-6} = 1\ \text{s}
$$

$$
v_C = 10(1-e^{-1}) = 6.321205588\ \text{V}
$$

The completed fraction is \(1-e^{-1} = 0.6321205588\).

Boundary: the same numbers on discharge give \(v_C = 10 e^{-1} = 3.678794412\) V. A non-positive resistance or capacitance is rejected.

## Limitations

The exponential assumes a constant resistance and a single capacitor. It does not include dielectric absorption or a current limit.

## Reference Standards

The production chunk cites OpenStax University Physics Volume 2, section 10.5, at https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits . That URL returned HTTP 200 on 2026-11-04. The textbook body was not transcribed. The arithmetic above is the script, not a quotation of the book.

## Online Calculator

https://powerengineerlab.com/calculators/rc-time-constant/

## Related Formulas

- [DC Ohm’s law](ohms-law.md)
- [Conductor resistance and temperature](conductor-resistance.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `rc-time-constant` (`TOOL-010`) |
| Evidence | Production chunk `41qfq2ttisrbf.js`, charge and discharge exponentials, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | tau 1 s, charge voltage 6.321205588 V |
| Boundary | discharge of the same RC is 3.678794412 V; non-positive R or C is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
