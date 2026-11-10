# Rational-method peak runoff

Locale: en

## Direct Answer

The Rational Method Peak Runoff Calculator estimates peak discharge as the product of a runoff coefficient, rainfall intensity, and catchment area, after converting the inputs to metres and seconds.


## Overview

Production module (`FORMULA-TOOL003-RATIONAL-001`, engine version 1.0.0), fetched 2026-11-04 from https://waterengineerlab.com/tools/rational-method-peak-runoff/.
## Formula

$$
Q = C \, i \, A
$$

with \(Q\) in m³/s, \(i\) in m/s, and \(A\) in m².

SI inputs:

$$
A = A_{\mathrm{ha}} \times 10^{4}, \qquad i = \frac{i_{\mathrm{mm/h}}}{1000 \times 3600}
$$

US inputs:

$$
A = A_{\mathrm{acre}} \times 4046.8564224, \qquad i = \frac{0.0254\, i_{\mathrm{in/h}}}{3600}
$$

Display of a US result multiplies m³/s by 35.31466672148859 to show cubic feet per second. That factor is \(1/0.028316846592\).

Validation: area \(> 0\), intensity \(> 0\), and \(0 < C \le 1\). The coefficient is not computed from a land-use table in this function.

## Variables

| Symbol | Meaning | Unit after normalization |
|---|---|---|
| \(C\) | runoff coefficient | 1 |
| \(i\) | rainfall intensity | m/s |
| \(A\) | catchment area | m² |
| \(Q\) | peak discharge | m³/s |

## Engineering Principles

The rational method, in the form this tool uses, treats the peak rate as \(C\) times intensity times area once intensity and area share SI base units. There is no unit-conversion constant left in \(Q = CiA\) because the millimetres-per-hour and acre conversions already happened. A customary US hand formula that is approximately \(Q_{\mathrm{cfs}} = CiA\) with \(i\) in in/h and \(A\) in acres is a different arrangement of the same idea; this engine does not apply a 1.008 factor on top of the SI product.

The page states that a peak-flow estimate does not confirm pipe capacity, detention volume, or compliance.

## Worked Example

SI: \(A = 10\,\mathrm{ha}\), \(C = 0.8\), \(i = 50\,\mathrm{mm/h}\).

1. \(A = 100000\,\mathrm{m^2}\).
2. \(i = 50/3.6\times 10^{6} = 1.388888\ldots\times 10^{-5}\,\mathrm{m/s}\).
3. \(Q = 0.8 \times 1.388888\ldots\times 10^{-5} \times 100000 = 1.111111\ldots\,\mathrm{m^3/s}\).

Result: **1.111 m³/s** to three decimals (exactly \(10/9\,\mathrm{m^3/s}\)).

US boundary: \(10\,\mathrm{acres}\), \(C = 0.5\), \(2\,\mathrm{in/h}\).

1. \(A = 40468.564224\,\mathrm{m^2}\).
2. \(i = 0.0508/3600 = 1.41111\ldots\times 10^{-5}\,\mathrm{m/s}\).
3. \(Q = 0.285528203\ldots\,\mathrm{m^3/s} = 10.083333\ldots\,\mathrm{cfs}\) after × 35.31466672148859.

\(C = 0\) and \(C > 1\) are rejected. \(C = 1\) is allowed.

## Limitations

- One catchment and one intensity. No time of concentration is computed in this tool.
- \(C\) is an input. The calculator does not look up a surface type.
- No pipe, inlet, or storage routing.
- Source ids `SRC-RATIONAL-METHOD-TOOL003-001` and `SRC-PROJECT-METHOD-TOOL003-001` have no URL in the bundle.

## Reference Standards

**Pending.** The page and the formula id name the rational method. No handbook or agency URL was in the fetched script.

## Online Calculator

https://waterengineerlab.com/tools/rational-method-peak-runoff/

Inventory tool ID: `TOOL-003`.

## Related Formulas

- [Manning open-channel discharge](manning-open-channel-flow.md)
- [Darcy-Weisbach major pipe headloss](darcy-weisbach-pipe-headloss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-003` |
| Evidence | Bundle: `Q = C * i * A` after ha→m² (`×1e4`), mm/h→m/s (`/1e3/3600`), acre factor `4046.8564224`, inch factor `0.0254/3600` |
| Method | Exact fraction for the SI case and direct multiplication for the US case |
| Example result | \(10/9\) m³/s for 10 ha, \(C=0.8\), 50 mm/h |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |