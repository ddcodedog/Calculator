# Ohm’s law (DC)

## Overview

The Ohm’s Law Calculator solves one of voltage, current, or resistance from the other two, then reports DC power. The model is a DC source and an ohmic resistance.

Production function `computeOhmsLaw` in the page bundle for https://powerengineerlab.com/calculators/ohms-law/ (chunk containing tool id `TOOL-001`, model 1.0.0), fetched 2026-11-04. The page’s “Load example” uses 12 V and 6 Ω and solves for current.

## Formula

$$
V = IR, \qquad P = VI
$$

Solve modes:

| Solve for | Known | Result |
|---|---|---|
| current | \(V \ge 0\), \(R > 0\) | \(I = V/R\) |
| voltage | \(I \ge 0\), \(R > 0\) | \(V = IR\) |
| resistance | \(V > 0\), \(I > 0\) | \(R = V/I\) |

Power is always \(P = VI\) after the missing quantity is filled in. Inputs are converted to SI (V, A, Ω) before this step. The chart series is five points and is not part of the reported scalar result.

## Variables

| Symbol | Unit | Domain in the solver |
|---|---|---|
| \(V\) | volt | see the mode table |
| \(I\) | ampere | see the mode table |
| \(R\) | ohm | must be \(> 0\) when it is an input |
| \(P\) | watt | derived |

Absolute input values are rejected above \(10^{12}\) (`MAX_INPUT_ABS`).

## Engineering Principles

Ohm’s law here is the linear \(V=IR\) model. It does not include temperature coefficient, contact resistance, or AC impedance. Power uses the same \(V\) and \(I\), so it is the power in that resistance for a DC operating point. Solving for resistance requires strictly positive voltage and current, which avoids division by zero.

## Worked Example

Load-example inputs: solve for current, \(V = 12\,\mathrm{V}\), \(R = 6\,\Omega\).

1. \(I = 12/6 = 2\,\mathrm{A}\).
2. \(P = 12 \times 2 = 24\,\mathrm{W}\).

Result: **2 A**, **12 V**, **6 Ω**, **24 W**. These values are exact in binary floating point.

Boundary: \(V = 0\,\mathrm{V}\), \(R = 6\,\Omega\), solve for current, gives \(I = 0\) and \(P = 0\), which the solver accepts. \(R = 0\) is rejected. Solving for resistance with \(I = 0\) is rejected.

## Limitations

- DC and ohmic only. The result object states that electrical-code compliance is not evaluated.
- No internal source resistance separate from \(R\).
- Display formatting can show fewer digits than the full double; the arithmetic is the SI product or quotient.

## Reference Standards

The bundle cites OpenStax University Physics Volume 2, section 9.4:

https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law

Source id in the bundle: `SRC-001`, accessed 2026-11-02, `licenseStatus` `verified` in the tool metadata. This library confirmed the URL returns HTTP 200 and that `computeOhmsLaw` implements \(V=IR\) and \(P=VI\). The textbook page body was not transcribed.

## Online Calculator

https://powerengineerlab.com/calculators/ohms-law/

Inventory tool ID: `ohms-law`.

## Related Formulas

- [Voltage divider](voltage-divider.md)
- [Power triangle](power-triangle.md)
- [Inductive reactance](inductive-reactance.md)
- [Capacitive reactance](capacitive-reactance.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `ohms-law` (`TOOL-001`) |
| Evidence | `computeOhmsLaw` in the production ohms-law chunk, 2026-11-04 |
| Method | Direct evaluation of \(V/R\) and \(VI\) |
| Example result | 2 A and 24 W from 12 V and 6 Ω |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
