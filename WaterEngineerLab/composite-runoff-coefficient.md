# Area-weighted runoff coefficient

## Overview

The composite coefficient is the area-weighted average of the coefficients the user enters for each surface.

## Formula

$$
C = \sum (A_i C_i) / \sum A_i
$$

The denominator must be greater than zero. The script does not clip \(C\) to 1.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(A_i\) | Sub-area | m² in the SI default |
| \(C_i\) | Runoff coefficient | dimensionless |

## Engineering Principles

Each pair is a user entry. There is no land-cover lookup. A coefficient above 1 is kept in the average if the user typed it; the rational-method page on this site rejects \(C > 1\) in its own tool.

## Worked Example

SI defaults: impervious 100 m² at 0.90, and pervious 300 m² at 0.30.

$$
C = (100\times 0.90 + 300\times 0.30) / 400 = 0.45
$$

Boundary: a zero total area is rejected. Dropping the pervious row leaves \(C = 0.90\).

## Limitations

The result is only a weighted \(C\). Peak flow still needs intensity and the rational-method equation, which is a different page.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://waterengineerlab.com/tools/composite-runoff-coefficient-calculator/

## Related Formulas

- [Rational-method peak runoff](rational-method-peak-runoff.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-016` |
| Evidence | Production weighted-average function, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | C = 0.45 |
| Boundary | zero total area is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
