# Simply supported midspan deflection

Locale: en

## Direct Answer

The beam deflection calculator accepts a simply supported span or a left-fixed cantilever. \(E\) and \(I\) are required. Reactions, shear, and moment are read-only context from the beam solver; this page does not re-derive them. This note checks the published midspan point-load case. The general integrator was not extracted line by line, so the status is `REVIEW_REQUIRED`.


## Overview

Production page script, read 2026-11-07, records supports `simply_supported` and `cantilever_fixed_left`, with \(v(0)=v(L)=0\) on the simple span and \(v(0)=\theta(0)=0\) on the cantilever. The numeric case is the public guide at `/guides/beam-deflection-calculation/` (https://structuralengineerlab.com/tools/beam-deflection-calculator/).
## Formula

Simply supported span \(L\), downward point load \(P\) at midspan, constant \(EI\):

$$
|\delta_{\mathrm{mid}}| = \frac{PL^{3}}{48EI}
$$

Downward deflection is negative. End deflection on this support is zero by the boundary condition, not by a separate load check.

## Variables

| Name | Example | Unit |
|---|---|---|
| Length | 6 | m |
| Point load at midspan | 12 | kN, downward |
| \(E\) | 200 | GPa |
| \(I\) | \(8\times 10^{-6}\) (800 cm⁴) | m⁴ |

## Engineering Principles

For this one load, symmetry puts half the load on each support, so the context reactions are 6 kN and 6 kN and the midspan moment magnitude is \(PL/4 = 18\,\mathrm{kN\cdot m}\). The deflection page treats those as inherited context. The number it is tested against in the guide is the midspan deflection.

## Worked Example

1. \(EI = 200\times 10^{9}\times 8\times 10^{-6} = 1.6\times 10^{6}\,\mathrm{N\cdot m^2}\).
2. \(PL^{3} = 12000\times 6^{3} = 2\,592\,000\,\mathrm{N\cdot m^3}\).
3. \(48EI = 76\,800\,000\,\mathrm{N\cdot m^2}\).
4. Magnitude = \(2\,592\,000/76\,800\,000 = 0.03375\,\mathrm{m} = 33.75\,\mathrm{mm}\) downward.

Boundary: a cantilever tip load is a different formula (\(PL^3/3EI\)) and a different support. Dropping \(E\) or \(I\) leaves this page without a deflection, because both are mandatory here.

## Limitations

- One published load case. Moving the load off midspan changes both the moment stations and the deflection.
- The EI integrator was not line-traced.
- Euler-Bernoulli beam: no shear deformation.
- Not a code capacity check. Bending stress is a separate topic.

## Reference Standards

The guide ties the case to the same beam formula ids used on the cantilever page and cites Hibbeler and Roark without a pinned edition in the script that was read. Those books were not re-opened. Status: pending.


Rechecked 2026-11-10. For 12 kN at midspan of 6 m with the same EI, PL³/(48EI) = 0.03375 m = 33.75 mm. End deflection is zero because v(0) = v(L) = 0, which is a support boundary, not a second load check. The general integrator was still not line-traced. Calculation status stays REVIEW_REQUIRED.

## Online Calculator

The 6 m, 12 kN midspan case is the guide example for this calculator:

https://structuralengineerlab.com/tools/beam-deflection-calculator/

## Related Formulas

- [Cantilever tip load and deflection](cantilever-tip-deflection.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab beam deflection calculator |
| Evidence | Production script confirms the two supports and the zero-deflection boundaries. The midspan identity is the published guide case. The general integrator was not extracted line by line. |
| Method | Recomputed \(PL^3/(48EI)\) for 12 kN, 6 m, 200 GPa, \(8\times 10^{-6}\) m⁴ |
| Example result | 33.75 mm downward |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | REVIEW_REQUIRED |
| Calculation status | REVIEW_REQUIRED |
| Standards status | PENDING |