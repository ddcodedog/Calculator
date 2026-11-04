# Interior wall paint quantity

## Overview

Wall area is twice the sum of length and width, times height, minus door and window openings. Paint volume is that area times coats, divided by coverage.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

A door opening is 20 square feet and a window opening is 15 square feet, from the constants in the paint module. Coverage in square feet per gallon is multiplied by 0.024542386747111157 to become square metres per litre. Litres are packed into US quarts by dividing by \(0.003785411784 \times 250\), taking the ceiling, then grouping four quarts as a gallon. Three leftover quarts are reported as one more gallon.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| room | Length, width, height | m |
| coats | Integer count | count |
| coverage | After conversion | m²/L |

## Engineering Principles

The ceiling is included only when that option is on. The imperial default leaves it off. Primer is a separate optional coat and the default is off.

## Worked Example

Imperial defaults: 12 ft by 12 ft by 8 ft, one door, two windows, two coats, ceiling off, coverage 350 ft²/gal.

Gross wall area is \(2 \times (12+12) \times 8 = 384\) ft². Openings are 20 + 30 = 50 ft². Net area is 334 ft², which is 31.02961536 m².

$$
V = 31.02961536 \times 2 / (350 \times 0.024542386747111157) = 7.224728776\ \text{L}
$$

That is 7.634285714 quarts before the ceiling, so 8 quarts, reported as 2 gallons and 0 quarts.

Boundary: zero coats give zero volume. Coverage left so the divisor would be 0 is rejected. Turning the ceiling on adds \(12 \times 12 = 144\) ft² before the same coverage division.

## Limitations

Opening areas are the constants 20 and 15 square feet, not measured door schedules. The three-quart rollup is a display rule in the module.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/paint/paint-calculator/

## Related Formulas

- [Drywall sheet count](drywall-sheets.md)
- [Plan area](square-footage.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `paint` |
| Evidence | Production `paint.ST-x8jn2.js`, door 20 ft² and window 15 ft², fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 334 ft² net, 7.224728776 L, displayed as 2 gal |
| Boundary | zero coats give zero volume; three leftover quarts display as an extra gallon |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
