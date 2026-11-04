# Euler column buckling

## Overview

The Column Euler Buckling Calculator returns the ideal elastic critical load from Young’s modulus, second moment of area, actual length, and a user-supplied effective-length factor \(K\). If a cross-sectional area is enabled, it also returns Euler stress.

Production function in the column-euler-buckling page bundle (`FORMULA-EULER-BUCKLING-STRESS-001` and the effective-length formula id), fetched 2026-11-04 from https://structuralengineerlab.com/tools/column-euler-buckling-calculator/.

## Formula

$$
L_e = K L
$$

$$
P_{\mathrm{cr}} = \frac{\pi^{2} E I}{L_e^{2}}
$$

$$
\sigma_{\mathrm{cr}} = \frac{P_{\mathrm{cr}}}{A} \quad \text{when area is provided}
$$

\(\pi\) is JavaScript `Math.PI`. Inputs are converted to pascals, metres to the fourth, metres, and square metres before this step. The page’s unit map uses \(1\,\mathrm{GPa} = 10^{9}\,\mathrm{Pa}\), \(1\,\mathrm{cm^4} = 10^{-8}\,\mathrm{m^4}\), and \(1\,\mathrm{cm^2} = 10^{-4}\,\mathrm{m^2}\).

## Variables

| Symbol | Meaning | SI unit used in the formula |
|---|---|---|
| \(E\) | Young’s modulus | Pa |
| \(I\) | second moment about the selected axis | m⁴ |
| \(L\) | actual length | m |
| \(K\) | effective-length factor | 1 |
| \(A\) | cross-sectional area, optional | m² |
| \(P_{\mathrm{cr}}\) | critical load | N |
| \(\sigma_{\mathrm{cr}}\) | Euler stress | Pa |

Every enabled input must be finite and greater than zero. The assumptions stored with the result are: ideal elastic Euler behavior, centroidal axial compression, constant \(E\) and \(I\) over the buckling length, user-supplied \(K\), and a single selected buckling axis.

## Engineering Principles

Euler’s formula is an eigenvalue of the elastic column, not a design strength. It is meaningful when the critical stress stays inside the elastic range of the material. \(K\) is not computed from end-fix diagrams; the user types it (1 for the pinned-pinned idealization if that is the intended model). Stress is \(P_{\mathrm{cr}}/A\) only. It is not a code buckling curve with a reduction factor.

## Worked Example

\(E = 200\,\mathrm{GPa}\), \(I = 100\,\mathrm{cm^4}\), \(L = 3\,\mathrm{m}\), \(K = 1\), \(A = 20\,\mathrm{cm^2}\).

1. \(E = 2.00\times 10^{11}\,\mathrm{Pa}\), \(I = 1.00\times 10^{-6}\,\mathrm{m^4}\), \(A = 0.002\,\mathrm{m^2}\), \(L_e = 3\,\mathrm{m}\).
2. \(P_{\mathrm{cr}} = \pi^{2} \times 2.00\times 10^{11} \times 10^{-6} / 9 = 219324.542246\ldots\,\mathrm{N}\) (**219.325 kN** if rounded to three decimals in kN).
3. \(\sigma_{\mathrm{cr}} = P_{\mathrm{cr}}/0.002 = 1.09662271\ldots\times 10^{8}\,\mathrm{Pa}\) (**109.662 MPa**).

Result: critical load **219324.542 N**, Euler stress **109.662 MPa**, with area enabled.

Boundary: omit area. The load is unchanged and `eulerBucklingStress.available` is false. \(K = 2\) on the same column doubles \(L_e\) and divides the load by 4, giving **54831.136 N**. A non-positive \(E\), \(I\), \(L\), \(K\), or enabled \(A\) is invalid.

## Limitations

- Elastic, prismatic, centroidally loaded column. No eccentricity, no residual stress, no inelastic tangent modulus.
- One axis at a time. The smaller \(I\) of a real section must be chosen by the user.
- Not an AISC, Eurocode, or other design-curve check. Source ids in the bundle (`SRC-EULER-BUCKLING-TEXTBOOK-001`, `SRC-COLUMN-STABILITY-TEXTBOOK-001`) have no URL in the page chunk.

## Reference Standards

**Pending.** The bundle names textbook source ids and does not publish a resolvable standard or book URL (the only `https://` links in that chunk are a Stack Overflow question unrelated to column theory).

## Online Calculator

https://structuralengineerlab.com/tools/column-euler-buckling-calculator/

Inventory tool ID: `TOOL-004`.

## Related Formulas

- [Section properties](section-properties.md)
- [Beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-004` |
| Evidence | Page bundle: `P = Math.PI**2 * E * I / (K*L)**2`, stress `P/A` when area is present |
| Method | Python evaluation with \(\pi\) from `math.pi` and the stated unit conversions |
| Example result | 219324.542 N and 109.662 MPa for the inputs above |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
