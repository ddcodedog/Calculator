# Sinusoidal power triangle

## Overview

The Power Triangle Calculator takes active power and reactive power and returns apparent power, power factor, and phase angle for a sinusoidal steady state.

Production logic in the power-triangle page bundle (`TOOL-005`), fetched 2026-11-04 from https://powerengineerlab.com/calculators/power-triangle/.

## Formula

$$
S = \sqrt{P^{2} + Q^{2}}, \qquad \mathrm{pf} = \frac{P}{S}, \qquad \theta = \operatorname{atan2}(Q,\ P)\ \text{in degrees}
$$

Implementation detail: if \(s = \max(P, \lvert Q \rvert)\) and \(s \ne 0\), then \(S = s\,\mathrm{hypot}(P/s,\ Q/s)\). If \(s = 0\), then \(S = 0\) and both power factor and angle are null with the reason “Undefined at zero power.”

Sign convention in the solver: \(P \ge 0\); \(Q > 0\) is lagging; \(Q < 0\) is leading.

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(P\) | `activePower` | W | finite, \(\ge 0\) |
| \(Q\) | `reactivePower` | var | finite |
| \(S\) | `apparentPower` | VA | derived |
| pf | `powerFactor` | 1 | derived, or null at zero |
| \(\theta\) | `phaseAngle` | degree | derived, or null at zero |

Input magnitude above \(10^{12}\) is rejected.

## Engineering Principles

The three powers are the sides of a right triangle only when \(P\) and \(Q\) are the RMS active and reactive powers of one sinusoidal port. The angle is the phase of the current relative to voltage under the sign convention above, not a power-factor angle taken from a nameplate. Power factor is \(P/S\), so it is non-negative in this tool because \(P\) is non-negative. Leading versus lagging is carried by the sign of \(Q\) and by the sign of \(\theta\).

## Worked Example

\(P = 3000\,\mathrm{W}\), \(Q = 4000\,\mathrm{var}\).

1. \(S = \sqrt{3000^{2} + 4000^{2}} = 5000\,\mathrm{VA}\).
2. \(\mathrm{pf} = 3000/5000 = 0.6\).
3. \(\theta = \operatorname{atan2}(4000,\ 3000) = 53.13010235\ldots^\circ\).

Result: **5000 VA**, power factor **0.6** lagging, angle **53.13010235…°**. The 3-4-5 triangle is exact.

Boundary: \(P = 0\), \(Q = 0\) yields \(S = 0\) and null power factor and angle. \(Q = -4000\,\mathrm{var}\) with the same \(P\) yields the same \(S\) and pf, with \(\theta = -53.13010235\ldots^\circ\) and a leading warning. Negative \(P\) is rejected.

## Limitations

- One port. No unbalance, harmonics, or displacement-versus-distortion power factor.
- Does not size a capacitor bank. See the separate power-factor-correction tool, which is not documented in this batch.
- Code compliance is explicitly not evaluated.

## Reference Standards

The bundle’s source object for this tool was not a resolvable standards URL in the extracted calculation module (the calculation closure references a source record `i` built beside the function). No edition was verified here. **Pending.**

The relations \(S=\sqrt{P^2+Q^2}\) and \(\mathrm{pf}=P/S\) are what the code computes.

## Online Calculator

https://powerengineerlab.com/calculators/power-triangle/

Inventory tool ID: `power-triangle`.

## Related Formulas

- [DC Ohm’s law](ohms-law.md)
- [Ideal inductive reactance](inductive-reactance.md)
- [Ideal capacitive reactance](capacitive-reactance.md)
- [Transformer full-load current](transformer-full-load-current.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `power-triangle` (`TOOL-005`) |
| Evidence | Production bundle: `Math.hypot` apparent power and `atan2` angle |
| Method | Independent 3-4-5 evaluation |
| Example result | 5000 VA, pf 0.6, angle 53.13010235…° |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
