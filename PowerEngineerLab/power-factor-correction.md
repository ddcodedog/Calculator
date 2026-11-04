# Power-factor correction kvar

## Overview

Required capacitive vars are active power times the drop in \(\tan(\arccos pf)\). Branch capacitance then depends on the connection.

## Formula

$$
\tan(\arccos pf) = \sqrt{1-pf^2}/pf
$$

$$
Q_c = P\,[\tan(\arccos pf_1) - \tan(\arccos pf_2)]
$$

$$
C = Q_c / (s\, \pi\, f\, V^2)
$$

The divisor coefficient \(s\) is 2 for single-phase, 6 for delta, and 2 for star. Equal power factors set \(Q_c = 0\) and \(C = 0\). Leading loads are rejected. A target below the initial power factor is rejected.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P\) | Active power | W |
| \(pf_1, pf_2\) | Initial and target power factor | fraction, (0, 1] |
| \(V\) | System voltage | V |
| \(f\) | Frequency | Hz |
| \(C\) | Capacitance per branch | F |

## Engineering Principles

The English example button sets 10000 W, power factor 0.8 to 1, 400 V, 50 Hz, delta, lagging. The zh-CN path can substitute a profile voltage and frequency; the English path uses 400 V and 50 Hz.

## Worked Example

English example, delta:

$$
\tan(\arccos 0.8) = 0.75
$$

$$
Q_c = 10000 \times 0.75 = 7500\ \text{var}
$$

$$
C = 7500 / (6\pi \times 50 \times 400^2) = 4.973591972\times 10^{-5}\ \text{F} = 49.73591972\ \mu\text{F}
$$

Boundary: target equal to 0.8 gives \(Q_c = 0\). A leading direction is rejected before the product. A target of 0.7 from 0.8 is rejected.

## Limitations

The note on the page says resonance, harmonics, switching stages, protection, and code compliance are not evaluated. Star uses \(s = 2\) with the line-to-line voltage the user typed, which is the expression in the script, not a conversion to phase voltage inside this page.

## Reference Standards

The chunk records source id SRC-004 with URL https://www.electrical-installation.org/enwiki/How_to_determine_the_optimum_level_of_compensation%3F . That page was not used as the arithmetic source. The expressions above are the script. The external text is pending.

## Online Calculator

https://powerengineerlab.com/calculators/power-factor-correction/

## Related Formulas

- [AC apparent real and reactive power](ac-power.md)
- [Sinusoidal power triangle](power-triangle.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `power-factor-correction` (`TOOL-006`) |
| Evidence | Production chunk `2rmau6310rdag.js`, English example object and s = 6 for delta, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 7500 var and 49.73591972 µF per branch |
| Boundary | equal power factors give 0 var; leading load is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
