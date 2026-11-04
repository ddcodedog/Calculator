# Inductive reactance

## Overview

The Inductive Reactance Calculator returns the magnitude of ideal inductive reactance in sinusoidal steady state.

Production calculation in the inductive-reactance page bundle (`TOOL-009`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/inductive-reactance/.

## Formula

For \(f > 0\),

$$
X_L = 2\pi f L
$$

The code evaluates \(\exp(\ln(2\pi)+\ln f+\ln L)\) and rejects overflow and underflow against the JavaScript number range. At \(f = 0\), \(X_L = 0\), with the reason “Ideal DC limit; reactance is zero.”

The reported value is a magnitude in ohms. The warning text states that the ideal impedance is \(+jX_L\).

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(f\) | `frequency` | Hz | finite, \(\ge 0\) |
| \(L\) | `inductance` | H | finite, \(> 0\) |
| \(X_L\) | `inductiveReactance` | Ω | derived |

## Engineering Principles

Reactance \(2\pi f L\) is the imaginary part of \(j\omega L\) for a pure inductance at one frequency. Winding resistance, core loss, saturation, and parasitic capacitance are outside the model, as the result assumptions state. DC is the limit \(X_L \to 0\), not an open circuit.

## Worked Example

\(f = 60\,\mathrm{Hz}\), \(L = 0.1\,\mathrm{H}\).

$$
X_L = 2\pi \times 60 \times 0.1 = 37.699111843\ldots\,\Omega
$$

Result: **37.699111843… Ω**. The UI may format this with fewer digits; the engine stores the IEEE value of that product.

Boundary: \(f = 0\) returns **0 Ω** and the DC-limit reason. \(L \le 0\) and \(f < 0\) are rejected. A product above `Number.MAX_VALUE` is an overflow error rather than `Infinity`.

## Limitations

- Single frequency, linear inductance.
- No quality factor and no series resistance.
- Not a component-selection or current-rating tool.

## Reference Standards

No standards URL was present in the extracted calculation closure. **Pending.**

## Online Calculator

https://powerengineerlab.com/calculators/inductive-reactance/

Inventory tool ID: `inductive-reactance`.

## Related Formulas

- [Capacitive reactance](capacitive-reactance.md)
- [Ohm’s law](ohms-law.md)
- [Power triangle](power-triangle.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `inductive-reactance` (`TOOL-009`) |
| Evidence | Production bundle: \(\ln(2\pi)+\ln f+\ln L\), and 0 at \(f=0\) |
| Method | `2 * math.pi * 60 * 0.1` in Python |
| Example result | 37.699111843… Ω |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
