# Deck board count

## Overview

Board rows are the ceiling of deck width divided by board width plus gap. Board count applies 10% waste to the row length and divides by the stock length.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
n_{rows} = \lceil W / (b+g) - 10^{-9} \rceil
$$

$$
n_{boards} = \lceil n_{rows} L (1+w/100) / L_{stock} - 10^{-9} \rceil
$$

Joist count, from the same module, is \(\lceil L / s - 10^{-9} \rceil + 1\) with spacing \(s\) entered as a depth in inches.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| \(L, W\) | Deck length and width | m |
| \(b\) | Actual board width | m |
| \(g\) | Gap | m |

## Engineering Principles

Board width uses the inch conversion. Gap uses the joint conversion, also 0.0254 m per inch. Waste defaults to 10%.

## Worked Example

Imperial defaults: length 16 ft, width 12 ft, board 5.5 in, gap 0.1875 in, stock 16 ft, waste 10%, joist spacing 16 in.

$$
b+g = 5.6875 \times 0.0254\ \text{m}
$$

Rows: 26. Linear length: \(26 \times 16 = 416\) ft. With 10% waste the board count is 29. Joist count is \(\lceil 16\times 0.3048 / (16\times 0.0254) - 10^{-9} \rceil + 1 = 13\).

Boundary: waste 0 gives \(\lceil 416/16 \rceil = 26\) boards, one per row when the stock length equals the deck length. A zero board width is rejected.

## Limitations

The row count is a straight run along the length. Picture-frame borders and diagonal layouts are only the higher waste percent the user types, not a second layout.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/decking/deck-board-calculator/

## Related Formulas

- [Stair rise and run](stair-geometry.md)
- [Drywall sheet count](drywall-sheets.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `deck-board` |
| Evidence | Production `deck-board._t6dGD4p.js`, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 26 rows, 416 ft, 29 boards, 13 joists |
| Boundary | zero waste returns 26 boards |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
