# Design-storm rainfall depth

## Overview

Depth is intensity times duration. The page does not build or interpolate an intensity-duration-frequency curve.

## Formula

$$
P = i \times t / 60
$$

\(i\) is millimetres per hour and \(t\) is minutes, so \(P\) is millimetres. The return-period field is stored with the scenario and is not in the product.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(i\) | Intensity | mm/h |
| \(t\) | Duration | min |

## Engineering Principles

A constant intensity over the duration is the whole model. The return period is a label unless the user changes intensity to represent it.

## Worked Example

SI defaults: return period 10, duration 60 min, intensity 50 mm/h.

$$
P = 50 \times 60 / 60 = 50\ \text{mm}
$$

Boundary: duration 0 gives depth 0. A negative intensity is rejected.

## Limitations

This is not the log-log interpolator. That tool has its own page and then uses this same depth product on the interpolated intensity.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/rainfall-idf-design-storm-helper/

## Related Formulas

- [Log-log IDF intensity](idf-log-log-interpolation.md)
- [Kirpich time of concentration](kirpich-time-of-concentration.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-002` |
| Evidence | Production depth product P = i t / 60, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 50 mm |
| Boundary | zero duration gives zero depth |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
