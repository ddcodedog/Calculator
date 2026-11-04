# Kirpich time of concentration

## Overview

Time of concentration on this page is the Kirpich power formula. The script does not add a sheet-flow or channel-flow segment.

## Formula

$$
t_c = 0.0195\, L^{0.77}\, S^{-0.385}
$$

\(t_c\) is in minutes when \(L\) is in metres and \(S\) is the dimensionless slope \(\Delta h/L\). Slope must be in (0, 1].

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(L\) | Flow length | m |
| \(S\) | Slope | m/m |

## Engineering Principles

The coefficient 0.0195 and the exponents are literals. The formula id in the script is FORMULA-TOOL004-KIRPICH-001. A warning in the engine says the relation is for the small steep watersheds Kirpich studied; that warning is not a second equation.

## Worked Example

SI defaults: length 300 m, slope 0.02.

$$
t_c = 0.0195 \times 300^{0.77} \times 0.02^{-0.385} = 7.104302235\ \text{min}
$$

Boundary: slope 0 is rejected. Slope 1 makes the slope power equal to 1, so \(t_c = 0.0195 \times 300^{0.77} = 1.57549844\) min.

## Limitations

One reach, one slope. The page does not convert this time into a rainfall intensity.

## Reference Standards

The engine cites FHWA HDS-2 in its source identifiers. That publication was not opened. Reference standards are pending.

## Online Calculator

https://waterengineerlab.com/tools/time-of-concentration/

## Related Formulas

- [Design-storm rainfall depth](design-storm-rainfall-depth.md)
- [Rational-method peak runoff](rational-method-peak-runoff.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-004` |
| Evidence | Production page chunk, Kirpich product, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 7.104302235 min |
| Boundary | slope outside (0, 1] is rejected; slope 1 removes the slope power |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
