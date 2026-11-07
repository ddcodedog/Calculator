# Catchment breakdown and peak runoff sum

## Overview

The catchment runoff summary splits one site into sub-areas, computes a composite runoff coefficient, and adds a rational-method peak for each sub-area under one rainfall intensity. The peaks are added directly. There is no routing delay between catchments, so the sum can sit above the peak a real outfall would see.

Production page chunk for TOOL-017, read 2026-11-07. Each catchment needs a unique id, area > 0, and \(C\) in \([0,1]\). Intensity must be > 0. SI entry is m² and mm/h. US entry is ft² and in/h.

## Formula

Composite \(C\) is the area-weighted mean. Area fraction is each area over the total area.

$$
C_{c} = \frac{\sum A_i C_i}{\sum A_i}
$$

Peak discharge for one catchment uses the rational method already published for a single area, with intensity converted to m/s:

$$
i_{\mathrm{SI}} = \frac{I_{\mathrm{mm/h}}}{1000\times 3600}, \qquad Q = C\,i\,A
$$

\(A\) is in m² and \(Q\) is in m³/s. A catchment with \(C = 0\) contributes \(Q = 0\) and is not passed through the single-area routine, which rejects \(C = 0\). US intensity is \(0.0254\times I_{\mathrm{in/h}}/3600\) m/s. The total peak is the sum of the catchment peaks. For one shared intensity that sum equals \(C_c\,i\,A_{\mathrm{total}}\).

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Intensity | Same value on every catchment | mm/h or in/h |
| Area | Plan area of that catchment | m² or ft² |
| \(C\) | Runoff coefficient | 0…1 |
| Id | Non-empty, unique | text |

## Engineering Principles

Composite \(C\) describes the mix of surfaces. The peak sum describes the same mix only when every catchment is given the same intensity and the peaks are allowed to land at the same instant. A zero-\(C\) roof that is ponded, or a catchment on a different time of concentration, is still added at the typed intensity. That is a screening total, not a hydrograph.

## Worked Example

SI defaults: intensity 50 mm/h, catchment A 10000 m² at \(C = 0.80\), catchment B 5000 m² at \(C = 0.40\).

1. \(i = 50/3\,600\,000 = 1.38889\times 10^{-5}\,\mathrm{m/s}\).
2. \(Q_A = 0.80\times i\times 10000 = 1/9 = 0.111111\,\mathrm{m^3/s}\).
3. \(Q_B = 0.40\times i\times 5000 = 1/36 = 0.027778\,\mathrm{m^3/s}\).
4. Total = \(5/36 = 0.138889\,\mathrm{m^3/s}\).
5. \(C_c = (8000+2000)/15000 = 2/3\). Check: \((2/3)\times i\times 15000 = 5/36\).

Boundary: a repeated id, a blank id, \(C = 1.1\), or a non-positive area is rejected. \(C = 0\) on one row returns zero peak for that row and still counts the area in \(C_c\).

## Limitations

- One intensity, no time of concentration, no pipe travel time.
- Direct addition can overstate a combined peak.
- This page does not size a pipe. Diameter and headloss are other tools.

## Reference Standards

The rational-method product \(Q = CiA\) is the expression in the production chunk. The drainage-manual chapter that would justify \(C\) and \(i\) was not re-read. Status: pending.

## Online Calculator

The two-catchment default is on the runoff summary:

https://waterengineerlab.com/tools/catchment-area-breakdown-runoff-summary

## Related Formulas

- [Single-source tree residual head](tree-network-residual-head.md)
- [Rational-method peak runoff](rational-method-peak-runoff.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab TOOL-017 catchment runoff summary |
| Evidence | Production composite-\(C\) sum and \(Q=CiA\) with mm/h converted by \(1000\times 3600\) |
| Method | Recomputed the 50 mm/h, 10000 m² / 5000 m² default |
| Example result | Peaks 0.111111 and 0.027778 m³/s, total 0.138889 m³/s, \(C_c=2/3\) |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
