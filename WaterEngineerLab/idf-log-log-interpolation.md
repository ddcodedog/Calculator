# Log-log IDF intensity

## Overview

Intensity is a bilinear interpolation in the logarithms of duration and return period. Depth then uses the same product as the design-storm page.

## Formula

For a query value between two table values:

$$
\lambda(x, x_0, x_1) = \ln(x/x_0)/\ln(x_1/x_0)
$$

with \(\lambda = 0\) when \(x = x_0\).

$$
\ln i = (1-\lambda_t)(1-\lambda_r)\ln i_{00} + \lambda_t(1-\lambda_r)\ln i_{10} + (1-\lambda_t)\lambda_r\ln i_{01} + \lambda_t\lambda_r\ln i_{11}
$$

Depth is \(P = i\, t / 60\) with \(t\) in minutes and \(i\) in mm/h. The page states that a numbered HEC-22 or NOAA interpolation equation was not verified as the source of this bilinear form.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(t\) | Duration | min |
| return period | Storm return period | year |
| \(i_{rc}\) | Table intensity at a duration/return corner | mm/h |

## Engineering Principles

All four corners must be positive because the logarithms are taken. The query must lie on the closed interval between the two durations and between the two return periods.

## Worked Example

Default grid: return periods 2 and 10 years; 10-minute intensities 40 and 80 mm/h; 60-minute intensities 10 and 20 mm/h. Query: 30 minutes and 5 years.

$$
\lambda_t = \ln(30/10)/\ln(60/10) = 0.6131471928
$$

$$
\lambda_r = \ln(5/2)/\ln(10/2) = 0.5693234419
$$

$$
i = 25.36833891\ \text{mm/h}
$$

$$
P = 25.36833891 \times 30/60 = 12.68416945\ \text{mm}
$$

Boundary: querying a corner, such as 10 minutes and 2 years, returns that corner intensity, 40 mm/h, because both lambdas are handled by the log ratio. A non-positive corner intensity is rejected.

## Limitations

Two return periods and two durations are the whole table. The method is the script’s bilinear log interpolation, not a fitted IDF formula.

## Reference Standards

The page text says a HEC-22 or NOAA equation for this interpolation was not verified. Those documents were not opened. Reference standards are pending.

## Online Calculator

https://waterengineerlab.com/tools/idf-curve-interpolator/

## Related Formulas

- [Design-storm rainfall depth](design-storm-rainfall-depth.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-018` |
| Evidence | Production log-log bilinear interpolator, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 25.36833891 mm/h and 12.68416945 mm |
| Boundary | a corner query returns that corner; a non-positive intensity is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
