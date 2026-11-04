# Gravel volume and mass

## Overview

Gravel volume includes the waste percent. Mass is volume times the material density. The crushed-stone default is 1.6 tonnes per cubic metre.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
V = L \times W \times d \times (1+w/100)
$$

$$
m = V \times \rho
$$

Short tons are tonnes times \(1000 / (2000 \times 0.45359237)\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(\rho\) | Density | t/m³ |
| \(w\) | Waste | percent, default 5 |

## Engineering Principles

A blank custom density keeps the material table. Crushed stone is 1.6 t/m³. Pea gravel, river rock, decomposed granite, and crusher run have their own table entries and are not used by the default.

## Worked Example

Imperial defaults: 20 ft by 10 ft by 3 in, crushed stone, 5% waste.

The net prism is 50 ft³. With 5% waste:

$$
V = 52.5\ \text{ft}^3 = 1.486634446\ \text{m}^3
$$

$$
m = 1.486634446 \times 1.6 = 2.378615114\ \text{t} = 2.621974344\ \text{short tons}
$$

Boundary: waste 0 leaves 50 ft³ and \(50 \times 0.3048^3 \times 1.6\) tonnes. A custom density replaces 1.6 when the field is not blank.

## Limitations

Density is a screening value in the script, not a quarry ticket. Compaction beyond the waste percent is not modeled.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/landscaping/gravel-calculator/

## Related Formulas

- [Mulch bed volume](mulch-volume.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `gravel` |
| Evidence | Production `gravel.C6Lf3PYa.js`, crushed density 1.6 t/m³, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 1.486634446 m³, 2.378615114 t, 2.621974344 short tons |
| Boundary | zero waste removes the 5% factor |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
