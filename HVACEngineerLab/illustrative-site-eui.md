# Site energy use intensity

## Overview

Energy use intensity is annual site energy divided by floor area. A percentile label is then chosen from three hardcoded thresholds.

## Formula

$$
EUI = E / A
$$

The label is 25 when EUI ≤ 80, 50 when EUI ≤ 140, 75 when EUI ≤ 220, and 90 otherwise. The units are the units of the two inputs. The defaults are kWh and m², so the ratio is kWh/m².

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(E\) | Annual site energy | kWh in the default |
| \(A\) | Floor area | m² in the default |

## Engineering Principles

The page text says the bands are not a surveyed dataset. The script copies an illustrative dataset object with sample size 1. The number 50 at the default is the bin label, not a statistical percentile from a census.

## Worked Example

Defaults: 1000 m² and 140000 kWh.

$$
EUI = 140
$$

140 is equal to the second threshold, so the label is 50.

Boundary: 80 maps to 25. A value just above 140, such as 140.0001, maps to 75. Area of 0 is rejected.

## Limitations

Do not report the label as a measured percentile. The thresholds 80, 140, and 220 are literals. Changing building type or geography in the form does not replace those literals.

## Reference Standards

Reference standards are pending. The page states that the bands are illustrative and that no edition of a benchmarking protocol is applied.

## Online Calculator

https://hvacengineerlab.com/tools/building-energy-benchmark/

## Related Formulas

- [HVAC cooling electrical energy](hvac-cooling-energy-cost.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `building-energy-benchmark` |
| Evidence | Production EUI ratio and threshold literals 80, 140, 220, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | EUI 140, bin label 50 |
| Boundary | EUI 80 labels 25; EUI just above 140 labels 75 |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
