# Ideal capacitive reactance

Locale: en

## Direct Answer

The Capacitive Reactance Calculator returns the magnitude of ideal capacitive reactance in sinusoidal steady state.


## Overview

Production calculation in the capacitive-reactance page bundle (`TOOL-008`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/capacitive-reactance/.
## Formula

For \(f > 0\),

$$
X_C = \frac{1}{2\pi f C}
$$

The code evaluates \(\exp(-\ln(2\pi)-\ln f-\ln C)\). At \(f = 0\), the metric value is null and the reason is “DC open-circuit limit.” The magnitude is what is displayed. The warning states that the ideal impedance is \(-jX_C\).

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(f\) | `frequency` | Hz | finite, \(\ge 0\) |
| \(C\) | `capacitance` | F | finite, \(> 0\) |
| \(X_C\) | `capacitiveReactance` | Ω | derived, or null at DC |


## Constraints

- \(f\): finite, \(\ge 0\)
- \(C\): finite, \(> 0\)
- \(X_C\): derived, or null at DC

## Engineering Principles

A pure capacitor’s impedance is \(1/(j\omega C)\). The calculator publishes the positive magnitude. ESR, leakage, dielectric loss, and voltage rating are not in the model. Zero frequency is treated as an open circuit (no finite ohm value), which is the opposite of the inductor tool’s DC short-circuit limit.

## Worked Example

\(f = 60\,\mathrm{Hz}\), \(C = 100\,\mu\mathrm{F} = 100\times 10^{-6}\,\mathrm{F}\).

$$
X_C = \frac{1}{2\pi \times 60 \times 100\times 10^{-6}} = 26.5258238486\ldots\,\Omega
$$

Result: **26.52582385… Ω**.

Boundary: \(f = 0\) does not return 0 Ω; the metric is null with the open-circuit reason. \(C \le 0\) is rejected. Very small \(fC\) products that would overflow the ohm value are rejected as overflow.

## Limitations

- One frequency and one ideal capacitor.
- Does not convert microfarads by itself if the caller passes the wrong SI scale. The page’s unit control is responsible for converting to farads before `compute`.
- Not a filter-design or motor-start sizing tool.

## Reference Standards

No standards URL was present in the extracted calculation closure. **Pending.**

## Online Calculator

https://powerengineerlab.com/calculators/capacitive-reactance/

Inventory tool ID: `capacitive-reactance`.

## Related Formulas

- [Ideal inductive reactance](inductive-reactance.md)
- [DC Ohm’s law](ohms-law.md)
- [Sinusoidal power triangle](power-triangle.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `capacitive-reactance` (`TOOL-008`) |
| Evidence | Production bundle: \(\exp(-\ln 2\pi -\ln f -\ln C)\), null at \(f=0\) |
| Method | Python `1/(2*pi*60*100e-6)` |
| Example result | 26.52582385… Ω |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |