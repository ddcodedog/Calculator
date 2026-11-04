# AC apparent real and reactive power

## Overview

The AC power calculator forms apparent power from voltage and current, then splits it with the power factor. A balanced three-phase selection multiplies by \(\sqrt{3}\).

## Formula

Let \(s = \sqrt{3}\) for balanced three-phase and \(s = 1\) for single-phase. From current:

$$
S = s\, V I
$$

$$
P = S \times pf
$$

$$
Q = \mathrm{sign}\, S \sqrt{1-pf^2}
$$

Lagging reactive power is positive in this script. Leading uses the opposite sign. The from-power path solves current from \(S = P/pf\) and \(I = S/(s V)\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(V\) | Line-to-line voltage in the three-phase path, or the single voltage | V |
| \(I\) | Line current | A |
| \(pf\) | Power factor, 0 to 1 | fraction |
| \(S, P, Q\) | Apparent, real, and reactive power | VA, W, var |

## Engineering Principles

The three-phase factor is applied once to apparent power. Power factor is the cosine magnitude; the sign of \(Q\) comes from the lagging or leading choice, not from the sign of the cosine.

## Worked Example

Load example: balanced three-phase, from current, 400 V, 10 A, power factor 0.8 lagging.

$$
S = \sqrt{3}\times 400 \times 10 = 6928.20323\ \text{VA}
$$

$$
P = 5542.562584\ \text{W}
$$

$$
Q = +4156.921938\ \text{var}
$$

Boundary: power factor 1 gives \(Q = 0\). Power factor 0 is rejected because several rearrangements divide by it. A single-phase selection uses \(s = 1\) on the same voltage and current.

## Limitations

The calculator assumes a sinusoidal, balanced set when the three-phase factor is selected. It does not apply a neutral current or a per-phase unbalance.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/ac-power/

## Related Formulas

- [Sinusoidal power triangle](power-triangle.md)
- [Power-factor correction kvar](power-factor-correction.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `ac-power` (`TOOL-004`) |
| Evidence | Production chunk `0unewv_999j4i.js`, factor s and signed Q, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | S 6928.20323 VA, P 5542.562584 W, Q 4156.921938 var |
| Boundary | power factor 1 gives Q = 0; power factor 0 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
