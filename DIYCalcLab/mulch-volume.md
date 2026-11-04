# Mulch bed volume

## Overview

Mulch volume is bed area times depth, times a waste factor that defaults to 0. Bags are the ceiling of that volume divided by the bag size.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
V = L \times W \times d \times (1+w/100)
$$

The 2 cubic foot bag is \(2 \times 0.3048^3\) cubic metres. Bag count is the ceiling of volume over that size.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| \(L, W\) | Bed sides | m |
| \(d\) | Depth, entered in inches | m |
| \(w\) | Extra percent | percent |

## Engineering Principles

The default mode is dimensions, not a typed area. Waste is an advanced field and its default is 0.

## Worked Example

Imperial defaults: 20 ft by 5 ft by 3 in, 2 cubic foot bags, no extra.

$$
V = 20 \times 5 \times 0.25 = 25\ \text{ft}^3 = 0.7079211648\ \text{m}^3
$$

Bag count is \(\lceil 25/2 \rceil = 13\).

Boundary: 10% extra makes the volume 27.5 ft³ and the bag count 14. Depth 0 gives volume 0 and zero bags.

## Limitations

Settlement is only the percent the user types. The calculator does not compact the bed or convert a weight.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/landscaping/mulch-calculator/

## Related Formulas

- [Gravel volume and mass](gravel-tonnage.md)
- [Rectangular prism volume](cubic-yard.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `mulch` |
| Evidence | Production `mulch.xXPSLZC9.js`, 2 ft³ bag, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 25 ft³ and 13 bags |
| Boundary | 10% extra yields 14 bags; zero depth yields zero |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
