# Rectangular prism volume

## Overview

Volume is length times width times depth. Imperial depth is in inches. Cubic yards are cubic feet divided by 27.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
V = L \times W \times d
$$

The imperial display divides cubic feet by 27. Cubic metres are cubic feet times \(0.3048^3\).

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| \(L, W\) | Plan sides | m |
| \(d\) | Depth | m |

## Engineering Principles

The quantity field multiplies the prism and is at least 1. There is no waste factor on this page.

## Worked Example

Imperial defaults: 10 ft by 10 ft by 6 in.

$$
V = 10 \times 10 \times 0.5 = 50\ \text{ft}^3 = 50/27 = 1.851851852\ \text{yd}^3
$$

$$
V = 50 \times 0.3048^3 = 1.41584233\ \text{m}^3
$$

Boundary: depth 0 gives volume 0. Two identical prisms double the volume.

## Limitations

This is a rectangular prism. Round columns are the sonotube page. Bag yield is not applied here.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/conversions/cubic-yard-calculator/

## Related Formulas

- [Plan area](square-footage.md)
- [Round column concrete volume](sonotube-concrete.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `cubic-yard` |
| Evidence | Production module `cubic-yard.CvNc9ucm.js`, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 50 ft³, 1.851851852 yd³, 1.41584233 m³ |
| Boundary | zero depth gives zero volume |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
