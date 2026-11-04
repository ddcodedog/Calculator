# Section normal stress at four script points

## Overview

Normal stress is axial force over area, minus \(M_x\) times one lever over \(I_x\), plus \(M_y\) times another lever over \(I_y\). The levers are the ones in the point table, which are not the mid-side offsets of a textbook section.

## Formula

$$
\sigma = N/A - M_x n / I_x + M_y r / I_y
$$

The rectangle runs from \(x = 0\) to \(b\) and \(y = 0\) to \(h\), with the centroid at \((b/2,\ h/2)\). The four rows are:

| Point | \(r\) | \(n\) |
|---|---|---|
| top | \(c_x\) | \(h - c_y\) |
| bottom | \(c_x\) | \(0 - c_y\) |
| left | \(0 - c_x\) | \(c_y\) |
| right | \(b - c_x\) | \(c_y\) |

Positive \(M_x\) produces bottom-fiber tension. Positive stress is tension. Dimensions are millimetres divided by 1000. Moments entered in kN·m and axial force in kN are multiplied by 1000.

## Variables

| Symbol | Meaning | Unit in the product |
|---|---|---|
| \(N\) | Axial force | N |
| \(M_x, M_y\) | Moments | N·m |
| \(n, r\) | Levers in the table above | m |

## Engineering Principles

Top and bottom use the true vertical offset from the centroid. Left and right use \(n = c_y\), the centroid’s y coordinate, not the offset of a mid-depth fiber. The stored y coordinate of a side point is \(n + c_y\), which lands on the top of the rectangle. That is what the script evaluates.

## Worked Example

Default rectangle 200 mm by 400 mm, \(M_x = 10\) kN·m, \(M_y = 0\), \(N = 0\). Area is 0.08 m² and \(I_x = 0.001066666667\) m⁴.

$$
\sigma = \mp (10000 \times 0.2) / 0.001066666667 = \mp 1.875\times 10^6\ \text{Pa} = \mp 1.875\ \text{MPa}
$$

Bottom \(n = -0.2\) m, so bottom stress is +1.875 MPa (tension). Top \(n = +0.2\) m, so top stress is −1.875 MPa (compression). Left and right also use \(n = 0.2\) m, so both are −1.875 MPa when \(M_y = 0\).

Boundary: all loads zero produce zero stress at every point. A zero area is rejected with the geometry.

## Limitations

Do not read the side values as mid-depth fibers. Mid-depth bending stress would use \(n = 0\) and would be zero for pure \(M_x\). This script does not do that. The sign note in the result is the sentence quoted above.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://structuralengineerlab.com/tools/section-stress-distribution-calculator/

## Related Formulas

- [Geometric section properties](geometric-section-properties.md)
- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-012` |
| Evidence | Production four-point map and sign convention string, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | bottom +1.875 MPa, top and both side points −1.875 MPa |
| Boundary | zero loads give zero stress; side levers are the script values, not mid-depth offsets |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
