# Darcy-Weisbach pipe headloss

## Overview

The Water Pipe Flow / Velocity / Headloss Calculator returns mean velocity and major headloss for a circular pipe flowing full. The Darcy friction factor is an explicit input.

Production module (`FORMULA-TOOL010-CONTINUITY-001` and the Darcy-Weisbach formula id, engine version 1.0.0), fetched 2026-11-04 from https://waterengineerlab.com/tools/water-pipe-flow-headloss/.

## Formula

$$
A = \frac{\pi D^{2}}{4}, \qquad V = \frac{Q}{A}
$$

$$
h_f = f \frac{L}{D} \frac{V^{2}}{19.6133}
$$

\(19.6133 = 2 \times 9.80665\), so the expression is the Darcy-Weisbach major loss with \(g = 9.80665\,\mathrm{m/s^2}\):

$$
h_f = f \frac{L}{D} \frac{V^{2}}{2g}
$$

Headloss gradient is \(h_f/L\). US inputs are converted first: cfs × 0.028316846592 → m³/s, inches × 0.0254 → m, feet × 0.3048 → m. The friction factor is dimensionless and is not converted.

Every one of flow, diameter, length, and friction factor must be finite and greater than 0.

## Variables

| Symbol | Meaning | Unit in the formula |
|---|---|---|
| \(Q\) | discharge | m³/s |
| \(D\) | internal diameter | m |
| \(L\) | pipe length | m |
| \(f\) | Darcy friction factor | 1 |
| \(V\) | mean velocity | m/s |
| \(h_f\) | major headloss | m of fluid |

## Engineering Principles

Continuity fixes velocity once flow and diameter are known. The headloss is only the distributed Darcy term. Fittings, elevation, pumps, and minor-loss \(K\) values are outside this version; the page says so. The user must supply an \(f\) that matches the Reynolds number, roughness, and fluid. The tool does not solve the Colebrook equation.

## Worked Example

\(Q = 0.01\,\mathrm{m^3/s}\), \(D = 0.1\,\mathrm{m}\), \(L = 100\,\mathrm{m}\), \(f = 0.02\).

1. \(A = \pi \times 0.01 / 4 = 0.00785398163\ldots\,\mathrm{m^2}\).
2. \(V = 0.01 / A = 1.2732395447\ldots\,\mathrm{m/s}\).
3. \(V^{2}/19.6133 = 0.0826550829\ldots\,\mathrm{m}\).
4. \((L/D) f = 20\).
5. \(h_f = 1.653101658\ldots\,\mathrm{m}\).

Result: velocity **1.273 m/s** and major headloss **1.653 m**, to three decimals.

Boundary: the same pipe with \(f\) just above 0 still runs, but \(f = 0\) is rejected. Halving the diameter at constant flow multiplies velocity by 4 and multiplies \(V^{2}/D\) by 32, so headloss scales by 32 when \(f\) and \(L\) stay constant. That scaling is a check on the formula, not a second code path.

## Limitations

- Circular, flowing full, one diameter, major loss only.
- \(f\) is not computed.
- No minor losses, no pumps, no open-channel depth.
- Source ids `SRC-DARCY-WEISBACH-TOOL010-001` and `SRC-PROJECT-METHOD-TOOL010-001` have no URL in the bundle.

## Reference Standards

**Pending** as a fetched document. The implementation is the Darcy-Weisbach major-loss equation with \(g = 9.80665\,\mathrm{m/s^2}\) hard-coded as the constant 19.6133.

## Online Calculator

https://waterengineerlab.com/tools/water-pipe-flow-headloss/

Inventory tool ID: `TOOL-010`.

## Related Formulas

- [Manning open-channel flow](manning-open-channel-flow.md)
- [Duct friction pressure drop](../HVACEngineerLab/duct-friction-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-010` |
| Evidence | Page bundle: area \(\pi D^2/4\), velocity \(Q/A\), headloss \(f(L/D)(V^2/19.6133)\), and \(2\times 9.80665 = 19.6133\) |
| Method | Python evaluation of the worked example |
| Example result | \(V = 1.27323954\ldots\) m/s, \(h_f = 1.65310166\ldots\) m |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
