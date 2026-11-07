# Cantilever tip load and deflection

## Overview

The cantilever beam calculator treats the left end as fixed and the right end as free. Downward point loads and full or partial uniform loads are the inputs. This note checks the published tip-load case, which has a closed form. Other load patterns go through the page’s EI integrator. That integrator was not extracted line by line, so the status below stays `REVIEW_REQUIRED` even though the tip-load arithmetic was recomputed.

The support rule and the formula ids `FORMULA-BEAM-EQUILIBRIUM-CANTILEVER-001` and `FORMULA-BEAM-EI-DEFLECTION-001` are in the production page script, read 2026-11-07. The numeric case is the one printed on the public guide at `/guides/cantilever-beam-calculation/`.

## Formula

For a downward point load \(P\) at the free end of a length \(L\), fixed at \(x = 0\):

$$
R = P, \qquad |M_{\mathrm{fixed}}| = PL, \qquad |\delta_{\mathrm{tip}}| = \frac{PL^{3}}{3EI}
$$

The guide reports the fixed-end reaction moment as positive in this downward case and the internal fixed-end moment as negative. Downward deflection is negative. \(E\) and \(I\) are optional. If either is missing, the page still solves reactions and moment and omits deflection. Slope is not shown. The set of moment stations is not an exhaustive list of every peak for an arbitrary load.

## Variables

| Name | Tip-load example | Unit |
|---|---|---|
| Length | 4 | m |
| Point load at the free end | 10 | kN, downward |
| \(E\) | 200 | GPa |
| \(I\) | \(8\times 10^{-6}\) (800 cm⁴) | m⁴ |

## Engineering Principles

Equilibrium fixes the vertical reaction and the end moment before any deflection is computed. Deflection needs both \(E\) and \(I\) because it integrates \(M/EI\). A stiffer section or a shorter span changes the millimetres without changing the 40 kN·m end moment of this particular load.

## Worked Example

1. Vertical reaction at the fixed end = 10 kN, balancing the tip load.
2. Moment magnitude = \(10\,\mathrm{kN}\times 4\,\mathrm{m} = 40\,\mathrm{kN\cdot m}\).
3. \(EI = 200\times 10^{9}\times 8\times 10^{-6} = 1.6\times 10^{6}\,\mathrm{N\cdot m^2}\).
4. Tip deflection magnitude = \(10000\times 4^{3}/(3\times 1.6\times 10^{6}) = 0.133333\,\mathrm{m} = 133.333\,\mathrm{mm}\) downward, reported as negative.

The guide rounds the same case to 133.33 mm.

Boundary: omit \(I\) and the deflection field is absent while the 10 kN and 40 kN·m equilibrium results remain. A zero or negative length is not a valid beam in the page inputs.

## Limitations

- The closed form above is the tip point load. A partial uniform load is a different integral.
- The EI integrator behind arbitrary loads was not line-traced for this note.
- No lateral-torsional buckling, shear deformation, or support settlement.
- Sign convention is the page’s: downward deflection negative.

## Reference Standards

The page cites Hibbeler and Roark for those formula ids without edition or year in the script that was read. Those books were not re-opened. Status: pending.

## Online Calculator

The 4 m, 10 kN tip case is the worked example on the calculator and its guide:

https://structuralengineerlab.com/tools/cantilever-beam-calculator/

## Related Formulas

- [Simply supported midspan deflection](simply-supported-midspan-deflection.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab cantilever beam calculator |
| Evidence | Production script confirms fixed-left, optional EI, and the two formula ids. The tip-load identity is the published guide example. The general EI integrator was not extracted line by line. |
| Method | Recomputed \(PL\) and \(PL^3/(3EI)\) for 10 kN, 4 m, 200 GPa, \(8\times 10^{-6}\) m⁴ |
| Example result | 40 kN·m and 133.333 mm downward |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | REVIEW_REQUIRED |
