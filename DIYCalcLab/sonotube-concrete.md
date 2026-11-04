# Round column concrete volume

## Overview

Each column is a cylinder. The total is multiplied by the waste factor, then divided by the 80 lb bag yield of 0.6 cubic feet.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
V = n\, \pi (d/2)^2 h
$$

$$
V_{buy} = V (1 + w/100)
$$

Bag count is \(V_{buy}\) divided by \(0.6 \times 0.3048^3\), then the ceiling above. The 0.6 cubic foot yield is the `80lb` entry in the shared bag table. Tube count, when the sold tube length equals the column height, is one tube per column.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| \(d\) | Diameter, entered in inches | m |
| \(h\) | Height, entered in feet | m |
| \(n\) | Column count | count |
| \(w\) | Waste percent | percent |

## Engineering Principles

Diameter uses the depth conversion (inches). Height uses the length conversion (feet). Waste default is 10%.

## Worked Example

Imperial defaults: diameter 12 in, height 4 ft, 4 columns, 10% waste, 80 lb bags, tubes sold in 4 ft lengths.

One column is 0.08895999723 m³. Four columns are 0.3558399889 m³. With 10% waste the order volume is 0.3914239878 m³. Bag yield is \(0.6 \times 0.3048^3\) m³. The bag count is 24. Tube count is 4, one per column, because the sold length equals the height.

Boundary: 0% waste orders 0.3558399889 m³ and fewer bags (the ceiling of that volume over the same yield is 21). Zero diameter gives zero volume and zero bags.

## Limitations

The yield is the constant in the bag table, not a supplier ticket. The page does not add a footing unless the height already includes it.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://diycalclab.com/concrete/sonotube-calculator/

## Related Formulas

- [Concrete slab volume and bag count](concrete-slab-volume.md)
- [Rectangular prism volume](cubic-yard.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `sonotube` |
| Evidence | Production `sonotube.BysjZOHC.js` and bag yield `m3: 0.6` cubic feet in the shared yield module, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 0.3914239878 m³ with waste, 24 bags of 80 lb |
| Boundary | 0% waste drops the 10% factor; zero diameter gives zero bags |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
