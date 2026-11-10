# Slab rebar grid count

Locale: en

## Direct Answer

The rebar calculator counts bars in a rectangular grid, splices a bar that is longer than the stock length, and rounds up a purchase quantity with a spare percentage. Weight uses the kilograms-per-metre value stored for that bar size. It does not design spacing or development length.


## Overview

Production module `rebar.vrhyH9u0.js`, read 2026-11-07. Imperial length is feet times 0.3048. Spacing and cover are inches times 0.0254. The pound-per-foot labels are converted with \(0.45359237/0.3048\) (https://diycalclab.com/concrete/rebar-calculator/).
## Formula

Clear span is the side minus two covers. Bar count across that side:

$$
n = \left\lfloor \frac{\mathrm{clear}}{\mathrm{spacing}} + 10^{-9} \right\rfloor + 1
$$

Zero when the clear span or the spacing is not positive. Each bar’s cut length is the other side minus two covers. If that run is no longer than the stock bar, one piece is enough and the lap is unused. If it is longer:

$$
n_{\mathrm{pieces}} = \left\lceil \frac{\mathrm{run}-\mathrm{lap}}{\mathrm{stock}-\mathrm{lap}} \right\rceil, \qquad L_{\mathrm{cut}} = \mathrm{run}+(n_{\mathrm{pieces}}-1)\,\mathrm{lap}
$$

Lap length is the typed diameter count times the bar diameter. Short runs share a stock bar: sticks = ceil(count / floor(stock/run)). Long runs use ceil(count × spliced length / stock). Purchase quantity ceils the sum of both directions after the extra percent. Crossings to tie equal \(n_L \times n_W\). Chair count ceils the area divided by 9 ft² in imperial mode.

Stored imperial masses, before conversion: #3 is 0.376 lb/ft, #4 is 0.668, #5 is 1.043, #6 is 1.502. Metric rows are stored directly as 0.617, 0.888, and 1.578 kg/m for 10, 12, and 16 mm.

## Variables

Imperial defaults:

| Input | Value |
|---|---|
| Length × width | 20 ft × 20 ft |
| Spacing, cover | 18 in, 3 in |
| Bar, stock, lap, extra | #4, 20 ft, 40 diameters, 5% |

## Engineering Principles

The first and last bars sit at the cover lines, so the count is one more than the number of spaces that fit in the clear span. A 20 ft stock bar can hold one 19.5 ft cut and nothing else, so the “several cuts per bar” branch does not reduce the count on this default. The lap field does nothing until a cut exceeds the stock length.

## Worked Example

1. Clear span = \(20 - 2\times 0.25 = 19.5\) ft. Spaces = \(19.5 / 1.5 = 13\) exactly, so bars in each direction = \(13+1 = 14\).
2. Each bar is 19.5 ft. Stock is 20 ft, so each bar is one piece and laps = 0.
3. Total length = \(14\times 19.5\times 2 = 546\) ft.
4. Weight = \(546\times 0.668 = 364.728\) lb. The page formats that with zero fraction digits, which displays 365 lb. The kilogram value before that rounding is 165.438 kg.
5. Sticks before extra = 14 + 14 = 28, because floor(20/19.5) = 1. With 5%, \(28\times 1.05 = 29.4\), which ceils to 30 bars to buy.
6. Crossings = \(14\times 14 = 196\). Chairs = ceil(\(400\,\mathrm{ft^2}/9\)) = 45.

Boundary: spacing above 24 in raises the module’s warning that the spacing is unusual; it still returns a count. Cover large enough to erase the clear span returns zero bars. A stock length shorter than 19.5 ft switches on the lap branch instead of the one-piece branch.

## Limitations

- One mat, rectangular, same spacing both ways. No hooks, bends, or a second mat.
- 40 diameters is the typed default, not a code lookup.
- Chair spacing is the fixed 9 ft² divisor, described in the module as about one per 3 × 3 ft.
- Masses are the constants in the module, not a mill certificate.

## Reference Standards

No reinforcing-steel standard is cited in the module that was read. Status: pending.
## Online Calculator

The 20 ft × 20 ft, #4, 18 in grid is the imperial default:

https://diycalclab.com/concrete/rebar-calculator/

## Related Formulas

- [Fence posts, rails, and pickets](fence-post-and-picket-count.md)
- [Concrete slab volume and bag count](concrete-slab-volume.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `rebar` |
| Evidence | Production `barCount`, `runWithLaps`, `sticksFor`, and the #4 mass 0.668 lb/ft |
| Method | Recomputed the 20 ft imperial default in Python |
| Example result | 14 × 14 grid, 546 ft, 30 stock bars after 5%, display weight 365 lb |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |