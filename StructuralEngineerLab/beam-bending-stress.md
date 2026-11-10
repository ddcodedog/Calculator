# Elastic beam bending stress

Locale: en

## Direct Answer

The Beam Bending Stress Calculator returns elastic extreme-fiber normal stress from a bending moment and either a section modulus or a second moment plus the distance to the extreme fiber.


## Overview

Production function in the beam-bending-stress page bundle, fetched 2026-11-04 from https://structuralengineerlab.com/tools/beam-bending-stress-calculator/. The default section-modulus example stored in the page is \(10\,\mathrm{kN\cdot m}\) and \(200\,\mathrm{cm^3}\).
## Formula

Section-modulus mode:

$$
\sigma_{\mathrm{bottom}} = \frac{M}{S}
$$

Inertia-and-distance mode:

$$
\sigma_{\mathrm{bottom}} = \frac{M\, c}{I}
$$

$$
\sigma_{\mathrm{top}} = -\sigma_{\mathrm{bottom}}
$$

The sign convention stored with the result is **positive = tension, negative = compression** on that fiber. A positive moment produces tension on the bottom fiber and compression on the top fiber. The governing magnitude is \(\lvert \sigma_{\mathrm{bottom}} \rvert\).

Unit factors in the page chunk include \(1\,\mathrm{kN\cdot m} = 1000\,\mathrm{N\cdot m}\), \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\), \(1\,\mathrm{cm^4} = 10^{-8}\,\mathrm{m^4}\), and \(1\,\mathrm{cm} = 0.01\,\mathrm{m}\).

## Variables

| Symbol | Meaning | SI unit in the formula |
|---|---|---|
| \(M\) | bending moment | N·m |
| \(S\) | elastic section modulus | m³ |
| \(I\) | second moment of area | m⁴ |
| \(c\) | distance from the neutral axis to the extreme fiber | m |
| \(\sigma\) | normal stress | Pa |

Section modulus, second moment, and extreme-fiber distance must be finite and greater than zero when that mode uses them. Moment may be negative or zero.

## Engineering Principles

This is the elastic flexure formula. It assumes a linear strain diagram, a modulus that is the same in tension and compression, and bending about the axis that \(S\) or \(I\) refers to. The top fiber is defined as the opposite sign of the bottom fiber at the same distance \(c\). The tool does not locate the neutral axis; \(c\) is an input in the inertia mode, and \(S\) already contains \(I/c\) in the other mode.

## Worked Example

Section-modulus mode, page defaults: \(M = 10\,\mathrm{kN\cdot m}\), \(S = 200\,\mathrm{cm^3}\).

1. \(M = 10000\,\mathrm{N\cdot m}\), \(S = 2.00\times 10^{-4}\,\mathrm{m^3}\).
2. \(\sigma_{\mathrm{bottom}} = 10000 / 2.00\times 10^{-4} = 5.00\times 10^{7}\,\mathrm{Pa} = 50\,\mathrm{MPa}\) tension.
3. \(\sigma_{\mathrm{top}} = -50\,\mathrm{MPa}\) compression.
4. Governing magnitude \(= 50\,\mathrm{MPa}\).

Result: bottom **+50 MPa** (tension), top **−50 MPa** (compression).

Inertia check of the same section if \(I/c = S\): \(I = 2.00\times 10^{-5}\,\mathrm{m^4}\), \(c = 0.10\,\mathrm{m}\) gives the same \(50\,\mathrm{MPa}\).

Boundary: \(M = 0\) gives zero stress on both fibers and the “zero” explanations. \(M = -10\,\mathrm{kN\cdot m}\) flips the signs (bottom compression). \(S \le 0\) is invalid.

## Limitations

- Elastic only. No plastic modulus and no lateral-torsional buckling.
- One moment and one section. No shear stress from \(VQ/It\).
- Sign convention is the tool’s (positive moment tensions the bottom). It may not match every textbook’s drawn moment.
- Source ids `SRC-SECTION-MODULUS-RELATION-001` and `SRC-MECHANICS-MATERIALS-FLEXURE-001` have no URL in the page chunk.

## Reference Standards

**Pending.** No resolvable standard URL in the calculation chunk.

## Online Calculator

https://structuralengineerlab.com/tools/beam-bending-stress-calculator/

Inventory tool ID: `TOOL-003`.

## Related Formulas

- [Centroidal area and section modulus](section-properties.md)
- [Euler elastic column buckling load](euler-column-buckling.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-003` |
| Evidence | Page bundle: `bendingMoment/sectionModulus` or `bendingMoment*extremeFiberDistance/secondMoment`, top stress negated |
| Method | SI conversion of the page default 10 kN·m and 200 cm³ |
| Example result | ±50 MPa |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |