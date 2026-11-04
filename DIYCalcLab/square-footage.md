# Plan area

## Overview

Plan area is the selected shape times a count. The imperial defaults are a 12 ft by 10 ft rectangle counted once.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

Rectangle area is the product of the two sides. A triangle is half that product. A circle is \(\pi (d/2)^2\). A trapezoid is \((a+c)/2\) times the height. Square yards are square metres divided by \(9 \times 0.3048^2\).

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| sides | Converted lengths | m |
| count | Identical copies | count, at least 1 |

## Engineering Principles

The shape switch is the whole model. Count multiplies after the shape area and is at least 1 even if a smaller number were passed.

## Worked Example

Imperial defaults: rectangle 12 ft by 10 ft, count 1.

$$
A = 12 \times 10 \times 0.3048^2 = 11.1483648\ \text{m}^2 = 120\ \text{ft}^2
$$

Square yards: \(120/9 = 13.33333333\).

Boundary: count is forced to at least 1. A circle with diameter 0 has area 0. A zero side on the rectangle has area 0.

## Limitations

The page does not subtract openings. Paint, tile, and drywall pages do that in their own tools.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/conversions/square-footage-calculator/

## Related Formulas

- [Rectangular prism volume](cubic-yard.md)
- [Interior wall paint quantity](interior-paint.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `square-footage` |
| Evidence | Production module `square-footage.CsXhzqZL.js`, rectangle product and count, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 120 ft² and 11.1483648 m² |
| Boundary | a zero side is zero area; count below 1 is raised to 1 |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
