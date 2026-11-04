# Concrete slab volume and bag count

## Overview

The Concrete Slab calculator returns the volume of one or more rectangular or circular slabs, applies a waste factor, and rounds the number of premix bags up.

Production functions `slabVolume` and `bagsFor` in the DIYCalcLab calculator bundle (calculator id `concrete-slab`), fetched 2026-11-04 from https://diycalclab.com/concrete/slab-calculator/. Lengths are converted to metres before the volume formula. The page’s illustrated math uses a 10 ft by 10 ft by 4 in slab.

## Formula

Rectangular area \(b \times w\), or circular area \(\pi (d/2)^{2}\), times thickness \(t\) and a count of identical slabs \(N\):

$$
V = A \, t \, N
$$

$$
V_{w} = V \left(1 + \frac{\max(0,\ \mathrm{waste\%})}{100}\right)
$$

Bag count, for a positive finite volume:

$$
n_{\mathrm{bags}} = \left\lceil \frac{V_w}{Y} - 10^{-9} \right\rceil
$$

\(Y\) is the bag yield in cubic metres. Imperial yields in the source are fractions of one cubic foot, with \(1\,\mathrm{ft^3} = (0.3048)^{3}\,\mathrm{m^3}\):

| Bag | Yield |
|---|---|
| 40 lb | 0.30 ft³ |
| 50 lb | 0.375 ft³ |
| 60 lb | 0.45 ft³ |
| 80 lb | 0.60 ft³ |
| 20 kg | 0.0094 m³ |
| 25 kg | 0.0117 m³ |
| 30 kg | 0.014 m³ |

Unit conversion before \(V\) is computed (`prefs.js`): imperial length × 0.3048 (feet to metres), imperial depth × 0.0254 (inches to metres), metric length × 1 (already metres), metric depth × 0.01 (centimetres to metres). Display divides cubic metres by \((0.3048)^{3}\) for cubic feet and by \(27(0.3048)^{3}\) for cubic yards.

The ceiling helper returns 0 when the argument is not finite or is \(\le 0\). Subtracting \(10^{-9}\) keeps a value that is only a floating-point hair above an integer from rounding up to the next bag.

## Variables

| Name | Field | Imperial entry | Metric entry |
|---|---|---|---|
| Shape | `shape` | `rect` or `circle` | same |
| Length, width, or diameter | `length`, `width`, `diameter` | feet | metres |
| Thickness | `thickness` | inches | centimetres |
| Count | `qty` | slabs, minimum 1 | same |
| Waste | `waste` | percent, 0 to 50 | same |
| Bag | `bag` | 40/60/80 lb | 20/25/30 kg |

## Engineering Principles

Volume is geometric. Waste is a percentage increase of that volume, intended for spillage and uneven subgrade, not a structural overdesign factor. Bags are purchased whole, so the count is rounded up. Yields are the table above, not a weighed density. The page warns when thickness exceeds 0.3 m.

## Worked Example

Rectangle, 10 ft × 10 ft, thickness 4 in, one slab, 10% waste, 80 lb bags. This is the case shown in the page math block (100 sq ft, 1.23 cu yd before waste).

1. \(L = W = 3.048\,\mathrm{m}\), \(t = 0.1016\,\mathrm{m}\).
2. \(V = 0.9438948864\,\mathrm{m^3} = 33.3333\ldots\,\mathrm{ft^3} = 1.2345679\ldots\,\mathrm{yd^3}\).
3. With 10% waste, \(V_w = 1.038284375\,\mathrm{m^3} = 36.6666\ldots\,\mathrm{ft^3} = 1.35802469\ldots\,\mathrm{yd^3}\).
4. Yield \(= 0.6 \times (0.3048)^{3} = 0.016990618\ldots\,\mathrm{m^3}\).
5. \(V_w/Y = 61.1111\ldots\), ceiling **62 bags**.

The page prints 1.23 cu yd, 1.36 cu yd with waste, and 61.1 rounded up to 62. Those are display roundings of the same quantities.

Boundary: 0% waste on the same slab gives \(V/Y = 55.555\ldots\), so **56 bags**. Thickness 0 or a non-positive volume yields **0 bags**. Waste is floored at 0% inside the multiplier.

## Limitations

- No reinforcement, edge thickening, or slope. Those are separate calculators.
- Circular area uses the full disk. There is no subtraction for a hole.
- Metric kilogram yields are fixed cubic-metre constants, not the imperial 0.6 ft³ scaled by weight.
- Not a structural slab design.

## Reference Standards

**Pending.** No design-standard URL is in the volume function. The arithmetic and the bag table are from the production bundle and `prefs.js`.

## Online Calculator

https://diycalclab.com/concrete/slab-calculator/

Inventory tool ID: `concrete-slab`.

## Related Formulas

- [Board-foot lumber volume](board-foot.md)
- [Roof pitch and slope factor](roof-pitch.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `concrete-slab` |
| Evidence | Bundle `slabVolume`, waste multiplier in `_shared` (`volume * (1 + waste/100)`), `bagsFor` via prefs ceiling, and the page math for 10×10×4 in |
| Method | Python with 0.3048 and 0.0254, compared with the page’s 62-bag illustration |
| Example result | 1.23457… yd³ neat, 62 bags of 80 lb mix at 10% waste |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
