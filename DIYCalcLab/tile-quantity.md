# Tile count with joints

## Overview

Tile count divides the room area by the tile rectangle grown by the joint on each side. A blank waste field uses the straight-pattern default of 10%.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
N = A / ((t_L + g)(t_W + g))
$$

$$
N_{buy} = \lceil N(1+w/100) - 10^{-9} \rceil
$$

Boxes are the ceiling of \(N_{buy}\) over tiles per box. The imperial default is 10 tiles per box.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| \(A\) | Room area | m² |
| \(t_L, t_W\) | Tile sides, entered in inches | m |
| \(g\) | Joint, entered in inches | m |

## Engineering Principles

Joint is added once to each tile side, which is the module’s model of the grid. Pattern waste for straight lay is 10% when the waste field is blank.

## Worked Example

Imperial defaults: room 10 ft by 8 ft, tile 12 in by 12 in, joint 0.125 in, straight pattern, 10 per box.

Room area is 80 ft². Tile pitch is 12.125 in. Tile count before waste is 78.35901796. With 10% waste the buy count is 87. Box count is 9.

Boundary: a waste entry of 0 buys the ceiling of 78.35901796, which is 79 tiles, and 8 boxes. A zero tile side is rejected.

## Limitations

The count is a grid of rectangles. It does not lay out cuts around a niche. Diagonal patterns are a different waste default when that pattern is selected; the worked example stays on straight.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/tile/tile-calculator/

## Related Formulas

- [Plan area](square-footage.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `tile` |
| Evidence | Production `tile.CaOIB-c7.js`, straight-pattern 10% waste, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 78.35901796 tiles, buy 87, 9 boxes |
| Boundary | explicit 0% waste buys 79 tiles |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
