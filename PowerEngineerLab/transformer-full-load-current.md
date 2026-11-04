# Transformer full-load current

## Overview

The Transformer Full-Load Current Calculator converts a rated apparent power and one winding voltage into ideal full-load current. Single-phase and balanced three-phase are separate modes. Primary and secondary are not solved together.

Production function in the transformer-full-load-current page bundle (`BACKLOG-054`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/transformer-full-load-current/.

## Formula

Rated power is entered in kVA and multiplied by 1000 to obtain volt-amperes.

$$
k = \begin{cases} 1 & \text{single-phase} \\ \sqrt{3} & \text{balanced three-phase} \end{cases}
$$

$$
I = \frac{S}{k\, V}
$$

\(V\) is the voltage of the winding being calculated. For three-phase the result assumptions call it the line-to-line voltage. Power factor is not applied. The current must be finite and positive.

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(S\) | `ratedVa` after ×1000 from `ratedKva` | VA | \(> 0\) |
| \(V\) | `voltageV` | V | \(> 0\) |
| phase | `phase` | `single` or `three` | required |
| \(I\) | `currentA` | A | derived |
| \(k\) | `factor` | 1 | 1 or \(\sqrt{3}\) |

## Engineering Principles

Full-load current here is \(S/V\) or \(S/(\sqrt{3}V)\), the current at rated apparent power and rated voltage with the ideal balance assumption. It is not a short-circuit current, not a protection setting, and not a cable ampacity. The checks array says protection is not evaluated. Because power factor is absent, this is not \(P/(\sqrt{3} V \mathrm{pf})\).

## Worked Example

Three-phase, \(S = 100\,\mathrm{kVA}\), \(V = 480\,\mathrm{V}\).

1. \(S = 100000\,\mathrm{VA}\).
2. \(k = \sqrt{3}\).
3. \(I = 100000 / (\sqrt{3} \times 480) = 120.28130608\ldots\,\mathrm{A}\).

Result: **120.28130608… A**.

Single-phase check: \(10\,\mathrm{kVA}\), \(240\,\mathrm{V}\).

$$
I = 10000 / 240 = 41.6666\ldots\,\mathrm{A}.
$$

Boundary: \(V \le 0\) or \(S \le 0\) is rejected. A non-finite product is rejected as overflow. The tool does not accept a second voltage in the same call.

## Limitations

- One winding per calculation.
- Balanced three-phase only. No neutral current and no phase shift.
- No efficiency, no voltage regulation, no inrush.
- Display rounding is separate from the stored double.

## Reference Standards

No standards URL was extracted from this calculation closure. **Pending.** The \(\sqrt{3}\) line-current relation is what the code implements (`Math.sqrt(3)` when `phase === "three"`).

## Online Calculator

https://powerengineerlab.com/calculators/transformer-full-load-current/

Inventory tool ID: `transformer-full-load-current`.

## Related Formulas

- [Sinusoidal power triangle](power-triangle.md)
- [DC Ohm’s law](ohms-law.md)
- [AC machine synchronous speed](synchronous-speed.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `transformer-full-load-current` (`BACKLOG-054`) |
| Evidence | Production bundle: `ratedVa/(k*voltageV)` with `k = Math.sqrt(3)` or `1` |
| Method | Python `100000/(sqrt(3)*480)` and `10000/240` |
| Example result | 120.28130608… A at 100 kVA, 480 V, three-phase |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
