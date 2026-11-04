# Section properties

## Overview

The Moment of Inertia Calculator returns area, centroid, second moments \(I_x\) and \(I_y\), elastic section moduli, and radii of gyration for five built-up shapes: solid rectangle, hollow rectangle, solid circle, hollow circle, and a doubly symmetric I-section.

Production `switch` on `shape` in the moment-of-inertia page bundle, fetched 2026-11-04 from https://structuralengineerlab.com/tools/moment-of-inertia-calculator/. Dimensions are in one consistent length unit; outputs use that unit to the matching power (the formulas below are written as lengths, so a metre input yields m² and m⁴).

## Formula

Rectangle, width \(b\), height \(h\), centroid at the center:

$$
A = bh, \quad I_x = \frac{b h^{3}}{12}, \quad I_y = \frac{h b^{3}}{12}
$$

Hollow rectangle, outer \(b \times h\), inner \(b_i \times h_i\), openings centered:

$$
A = bh - b_i h_i, \quad I_x = \frac{b h^{3} - b_i h_i^{3}}{12}, \quad I_y = \frac{h b^{3} - h_i b_i^{3}}{12}
$$

Solid circle, diameter \(d\):

$$
A = \frac{\pi d^{2}}{4}, \quad I_x = I_y = \frac{\pi d^{4}}{64}
$$

Hollow circle, outer diameter \(d\), inner diameter \(d_i\):

$$
A = \frac{\pi}{4}(d^{2}-d_i^{2}), \quad I = \frac{\pi}{64}(d^{4}-d_i^{4})
$$

I-section, overall depth \(h\), flange width \(b\), flange thickness \(t_f\), web thickness \(t_w\), web clear depth \(h_w = h - 2 t_f\):

$$
A = 2 b t_f + t_w h_w
$$

$$
I_x = 2\left(\frac{b t_f^{3}}{12} + b t_f \left(\frac{h}{2}-\frac{t_f}{2}\right)^{2}\right) + \frac{t_w h_w^{3}}{12}
$$

$$
I_y = 2\frac{t_f b^{3}}{12} + \frac{h_w t_w^{3}}{12}
$$

For every shape the centroid is at half the outer width and half the outer height (circles use \(d/2\)). Then

$$
S_x = \frac{I_x}{c_y}, \quad S_y = \frac{I_y}{c_x}, \quad r_x = \sqrt{\frac{I_x}{A}}, \quad r_y = \sqrt{\frac{I_y}{A}}
$$

where \(c_y\) and \(c_x\) are the distances from the centroid to the outer face (half the outer height and half the outer width).

Rejected cases in the source: a non-positive dimension; hollow rectangle with inner width or height greater than or equal to the outer; hollow circle with inner diameter greater than or equal to the outer; I-section with \(2 t_f \ge h\) or \(t_w \ge b\).

## Variables

All inputs are lengths in one unit. \(I\) is length⁴, \(S\) is length³, \(r\) is length, \(A\) is length². \(\pi\) is `Math.PI`.

## Engineering Principles

These are centroidal second moments for bending and for \(r = \sqrt{I/A}\). The hollow and I formulas assume the void or the web is centered, so the centroid stays at the geometric center and the parallel-axis terms use that center. They are gross geometric properties, not net of holes and not plastic moduli.

## Worked Example

Rectangle \(b = 0.1\,\mathrm{m}\), \(h = 0.2\,\mathrm{m}\).

1. \(A = 0.020\,\mathrm{m^2}\).
2. \(I_x = 0.1 \times 0.2^{3} / 12 = 6.6666\ldots\times 10^{-5}\,\mathrm{m^4}\).
3. \(I_y = 0.2 \times 0.1^{3} / 12 = 1.6666\ldots\times 10^{-5}\,\mathrm{m^4}\).
4. \(c_y = 0.1\,\mathrm{m}\), so \(S_x = 6.6666\ldots\times 10^{-4}\,\mathrm{m^3}\).
5. \(r_x = \sqrt{I_x/A} = 0.0577350269\ldots\,\mathrm{m}\).

Result: \(I_x = b h^{3}/12 = 1/15000\,\mathrm{m^4}\).

Circle check: \(d = 0.2\,\mathrm{m}\). \(A = \pi \times 0.01 = 0.0314159265\ldots\,\mathrm{m^2}\). \(I = \pi (0.2)^{4} / 64 = 7.8539816\ldots\times 10^{-5}\,\mathrm{m^4}\).

Boundary: hollow circle with inner diameter equal to outer diameter is rejected (`INVALID_HOLLOW_CIRCLE`). An I-section with flange thickness large enough that \(2 t_f \ge h\) is rejected.

## Limitations

- Five shapes only. No angle, channel, or arbitrary polygon.
- Thin-wall approximations are not used; the I-section includes the rectangular flange and web parts as written, with the web height excluding both flanges (no overlap).
- Units are whatever length the caller converted to. Mixing inches and millimetres in one call is a user error the formula cannot see.
- Source ids such as `SRC-SECTION-GEOMETRY-TEXTBOOK-001` and `SRC-PARALLEL-AXIS-THEOREM-001` have no URL in the page chunk.

## Reference Standards

**Pending.** No resolvable standard URL in the calculation chunk.

## Online Calculator

https://structuralengineerlab.com/tools/moment-of-inertia-calculator/

Inventory tool ID: `TOOL-008`.

## Related Formulas

- [Beam bending stress](beam-bending-stress.md)
- [Euler column buckling](euler-column-buckling.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-008` |
| Evidence | Page bundle shape `switch`: rectangle \(bh^3/12\), circle \(\pi d^4/64\), hollow and I-section expressions quoted above |
| Method | Python evaluation of the rectangle and the solid circle |
| Example result | Rectangle 0.1 m × 0.2 m: \(I_x = 6.6666\ldots\times 10^{-5}\,\mathrm{m^4}\) |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
