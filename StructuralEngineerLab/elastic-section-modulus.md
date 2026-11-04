# Elastic section modulus

## Overview

Section modulus reuses the TOOL-002 geometry. For a symmetric shape the distance to the extreme fiber is the centroid coordinate measured from the outer face.

## Formula

$$
S_x = I_x / c_y,\quad S_y = I_y / c_x
$$

For the rectangle, \(c_y = h/2\) and \(c_x = b/2\). The second moments are the centroidal values from the section-properties switch.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(I\) | Centroidal second moment | m⁴ |
| \(c\) | Distance from centroid to the extreme fiber | m |
| \(S\) | Elastic section modulus | m³ |

## Engineering Principles

The page does not apply a shape factor or a plastic modulus. It does not look up a steel-manual \(S_x\).

## Worked Example

The same 200 mm by 400 mm rectangle:

$$
S_x = 0.001066666667 / 0.2 = 0.005333333333\ \text{m}^3
$$

$$
S_y = 0.0002666666667 / 0.1 = 0.002666666667\ \text{m}^3
$$

Boundary: a zero dimension that produces a zero moment or a zero \(c\) is rejected with the geometry. Swapping width and height swaps \(S_x\) and \(S_y\).

## Limitations

Elastic modulus is \(I/c\). Bending stress on the beam page is a different tool and uses a different input set.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://structuralengineerlab.com/tools/section-modulus-calculator/

## Related Formulas

- [Geometric section properties](geometric-section-properties.md)
- [Section normal stress at four script points](section-normal-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-009` |
| Evidence | Production reuse of TOOL-002 geometry, S = I/c, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | Sx 0.005333333333 m³, Sy 0.002666666667 m³ |
| Boundary | a zero fiber distance is rejected with the geometry |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
