# Geometric section properties

## Overview

The section-properties calculator returns area, centroid, and centroidal second moments for five shapes. This page uses the rectangle defaults and states the circle formulas that the same switch implements.

## Formula

Rectangle of width \(b\) and height \(h\), origin at a corner:

$$
A = bh,\quad c_x = b/2,\quad c_y = h/2
$$

$$
I_x = b h^3/12,\quad I_y = h b^3/12
$$

$$
S_x = I_x/c_y,\quad r_x = \sqrt{I_x/A}
$$

Circle: \(A = \pi d^2/4\) and \(I = \pi d^4/64\) about a diameter. A hollow circle subtracts the inner diameter in both area and moment, and rejects an inner diameter greater than the outer. Dimensions are entered in millimetres and divided by 1000.

## Variables

| Symbol | Meaning | Unit after conversion |
|---|---|---|
| \(b, h, d\) | Width, height, diameter | m |
| \(I\) | Second moment about the centroid | m⁴ |
| \(S\) | Elastic section modulus | m³ |

## Engineering Principles

The moments are centroidal geometric moments. They are not plastic moduli and they are not reduced for holes other than the hollow shapes in the switch. The separate section-modulus page calls this same geometry and highlights \(S\).

## Worked Example

Default rectangle, 200 mm by 400 mm, converted to 0.2 m by 0.4 m.

$$
A = 0.08\ \text{m}^2
$$

$$
I_x = 0.2 \times 0.4^3 / 12 = 0.001066666667\ \text{m}^4
$$

$$
I_y = 0.0002666666667\ \text{m}^4
$$

$$
S_x = 0.005333333333\ \text{m}^3,\quad r_x = 0.1154700538\ \text{m}
$$

Boundary: a circle of diameter 0 is rejected. A hollow circle with the inner diameter equal to the outer has area 0 and is rejected by the positive-area check.

## Limitations

The published moment-of-inertia topic for TOOL-008 is a different URL and a different input form. This page is TOOL-002. Units on the form are millimetres.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://structuralengineerlab.com/tools/section-properties-calculator/

## Related Formulas

- [Elastic section modulus](elastic-section-modulus.md)
- [Centroidal area and section modulus](section-properties.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-002` |
| Evidence | Production five-shape switch, rectangle and circle branches, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | A 0.08 m², Ix 0.001066666667 m⁴, Sx 0.005333333333 m³ |
| Boundary | zero diameter and a hollow circle with no wall are rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
