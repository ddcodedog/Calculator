# Off-center point load on a simple span

Locale: en

## Direct Answer

A simply supported beam with one point load that is not at midspan has unequal end reactions. The shear changes at the load, and the moment peaks at the load rather than at midspan. This note uses the production beam solver shared by the simply-supported calculator, engine `beam-core-0.2.0-gate2`, read on 2026-11-08. The 6 m beam with a 12 kN midspan load and the 33.75 mm midspan deflection printed on the public guide are a different case and are not repeated here (https://structuralengineerlab.com/tools/simply-supported-beam-calculator/).


## Overview

Downward load is positive. Upward reaction is positive. Sagging moment is positive. Downward deflection is negative.
## Formula

For a point load \(P\) at distance \(a\) from the left support, with \(b=L-a\):

$$
R_B = \frac{P a}{L}, \qquad R_A = P - R_B, \qquad M(a) = \frac{P a b}{L}
$$

The solver reaches the same reactions by summing force and the first moment about the left end, then \(R_B = M_1/L\). Moment at \(x\) is

$$
M(x) = R_A x - P\,\langle x-a\rangle
$$

with the left fixed-end moment equal to 0 on a simple span, and \(\langle x-a\rangle = 0\) when \(x\le a\).

Deflection integrates \(M/EI\) twice. For a simple span the integration constants are \(c_2=0\) and

$$
c_1 = -\frac{1}{EI\,L}\int\!\!\int M(L)
$$

The closed form at the load, used here only as a check, is

$$
\delta(a) = -\frac{P a^2 b^2}{3 E I L}
$$

\(E\) and \(I\) must be the modulus and second moment the solver multiplies. In the example they are entered as kN/m² and m⁴ so the product is kN·m².

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Span | Distance between simple supports | m |
| Load | Downward point load | kN |
| Position | Distance from the left support | m |
| \(E\) | Elastic modulus | kN/m² |
| \(I\) | Second moment of area | m⁴ |

## Engineering Principles

Equilibrium fixes the reactions before elasticity is involved. Stiffness changes the deflection and does not change \(R_A\), \(R_B\), or \(M(a)\) for this static simple span. The sign of deflection is a plotting convention of the solver: a sag is a negative number, and the magnitude is the downward movement.

## Worked Example

Span 8 m. One 15 kN load at 3 m from the left. \(E = 200\times 10^6\) kN/m² (200 GPa). \(I = 8\times 10^{-6}\) m⁴. Then \(EI = 1600\) kN·m², and \(b=5\) m.

1. \(R_B = 15\times 3/8 = 5.625\) kN. \(R_A = 15-5.625 = 9.375\) kN. Left moment = 0.
2. Moment at the load = \(9.375\times 3 = 28.125\) kN·m. The same value is \(15\times 3\times 5/8\).
3. Solver deflection at 3 m = \(-0.087890625\) m, which is 87.890625 mm downward.
4. The check \(15\times 3^2\times 5^2 / (3\times 1600\times 8) = 3375/38400 = 0.087890625\) m matches that magnitude.

A load placed at 0 or beyond the span is outside `assertPosition`. This 3 m position is inside the span.

## Limitations

- Linear elastic Euler-Bernoulli beam. No shear deformation, no axial load, no plasticity.
- One point load. Adding a distributed load changes both the moment expression and \(c_1\).
- Self-weight is omitted unless you add it as a load.
- Hibbeler and Roark are named by the surrounding structural pages without an edition in the chunk that was read. Those PDFs were not re-read.

## Reference Standards

Beam equilibrium and the \(M/EI\) integration are standard elastic-beam relations. The edition-specific tables were not opened. Status: pending.
## Online Calculator

The simply-supported page calls this solver. The 8 m, 15 kN, 3 m case is the one to enter:

https://structuralengineerlab.com/tools/simply-supported-beam-calculator/

## Related Formulas

- [Simply supported midspan deflection](simply-supported-midspan-deflection.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab simply-supported beam calculator, `analyzeBeam` |
| Evidence | Production `solver.js` reactions, moment, and `calculateDeflectionAt` for `simply_supported` |
| Method | Python port of those functions, checked against \(P a b/L\) and \(P a^2 b^2/(3EIL)\) |
| Example result | Reactions 9.375 kN and 5.625 kN, moment 28.125 kN·m, deflection −87.890625 mm |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |