# Full uniform load on a simple span

## Overview

A uniform load covering a simply supported span produces equal end reactions, a midspan moment of \(wL^2/8\), and a midspan sag of \(5wL^4/(384EI)\). The beam-analysis page can also model a cantilever and a partial uniform load. This note stays on the full-span simple-beam case and uses a different intensity from the 5 kN/m illustration on that page.

The page calls `analyzeBeam` from the same `beam-core-0.2.0-gate2` solver read on 2026-11-08. Downward load is positive, sagging moment is positive, and downward deflection is negative.

## Formula

For \(w\) constant from \(x=0\) to \(x=L\):

$$
R_A = R_B = \frac{wL}{2}, \qquad M_{\max} = \frac{wL^2}{8}
$$

The solver builds the resultant \(wL\) at midspan, then \(R_B\) from the first moment. Moment at \(x\) is

$$
M(x) = R_A x - \frac{w}{2}\left(\langle x-0\rangle^2 - \langle x-L\rangle^2\right)
$$

Deflection uses the same double integration as the point-load tool, with \(c_2=0\) and \(c_1=-\iint M(L)/(EI L)\). The magnitude check at midspan is

$$
|\delta_{\mathrm{mid}}| = \frac{5 w L^4}{384 E I}
$$

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Span | Simple span | m |
| Intensity | Downward uniform load | kN/m |
| \(E\) | Elastic modulus | kN/m² |
| \(I\) | Second moment of area | m⁴ |

## Engineering Principles

On a full uniform load the shear is zero at midspan, so the moment peak is there. The slope is also zero at midspan for this symmetric case, which is why the sag is the midspan deflection. A uniform load that stops short of one support moves both the shear zero and the moment peak; that partial-load path is in the solver and is not the example below.

## Worked Example

Span 6 m. Uniform load 2 kN/m from 0 to 6 m. \(E = 200\times 10^6\) kN/m². \(I = 20\times 10^{-6}\) m⁴. Then \(EI = 4000\) kN·m².

1. Total load = \(2\times 6 = 12\) kN. \(R_A = R_B = 6\) kN.
2. Midspan moment = \(6\times 3 - (2/2)\times 3^2 = 18-9 = 9\) kN·m, which is \(wL^2/8 = 2\times 36/8\).
3. Solver deflection at 3 m = \(-0.0084375\) m, or 8.4375 mm downward.
4. Check: \(5\times 2\times 6^4 / (384\times 4000) = 12960/1536000 = 0.0084375\) m.

Shear just left of midspan is positive and just right is negative; the solver’s right-side shear at 3 m is 0 for this symmetric load. A zero span or a non-finite \(I\) fails validation before these expressions run.

## Limitations

- Elastic, small-deflection beam theory. The 8.4 mm sag is small next to a 6 m span; a much smaller \(I\) would still be computed by the same formula even when that theory is no longer appropriate.
- No self-weight beyond the 2 kN/m you enter.
- Support settlement and partial continuity are not in this support type.
- Standard editions cited elsewhere on the site were not re-read.

## Reference Standards

The \(wL^2/8\) and \(5wL^4/384EI\) identities are standard simple-beam results. The specific textbook edition was not opened. Status: pending.

## Online Calculator

Enter the 6 m span and 2 kN/m full load on the beam-analysis page:

https://structuralengineerlab.com/tools/beam-analysis-calculator/

## Related Formulas

- [Cantilever tip load and deflection](cantilever-tip-deflection.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab beam-analysis calculator, `TOOL-001` |
| Evidence | Production `solver.js` `calculateReactions`, `calculateMomentAt`, and `calculateDeflectionAt` |
| Method | Python port checked against \(wL/2\), \(wL^2/8\), and \(5wL^4/384EI\) |
| Example result | Reactions 6 kN, moment 9 kN·m, deflection −8.4375 mm |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
