# Stair rise and run

## Overview

Riser count is the ceiling of total rise divided by the maximum riser. Tread count is one less. The stringer is the hypotenuse of rise and run.

## Formula

Imperial inputs are converted before the arithmetic. Length in feet is multiplied by 0.3048. Depth in inches, and a joint in inches, are multiplied by 0.0254. One square foot is \(0.3048^2\) square metres. One cubic foot is \(0.3048^3\) cubic metres. Counts use \(\lceil x - 10^{-9} \rceil\).

$$
n = \lceil rise / h_{max} - 10^{-9} \rceil
$$

$$
h = rise / n,\quad n_t = n-1,\quad run = n_t \times t
$$

$$
L = \sqrt{rise^2 + run^2},\quad \theta = \arctan(h/t)
$$

The IRC check stored in the module uses a maximum riser of \(7.75 \times 0.0254\) m and a minimum tread of \(10 \times 0.0254\) m. The geometry itself uses the maximum riser the user typed, which defaults to that same 7.75 in.

## Variables

| Symbol | Meaning | Unit inside the function |
|---|---|---|
| rise, \(h_{max}\), \(t\) | Total rise, max riser, tread | m |

## Engineering Principles

A riser taller than the code maximum by more than \(10^{-9}\) m is flagged. A tread shorter than the code minimum by more than that tolerance is flagged. The IRC entry in this module has no maximum pitch; the UK entry does.

## Worked Example

Imperial defaults: rise 108 in, maximum riser 7.75 in, tread 10 in, check against IRC.

$$
n = 14,\quad h = 108/14 = 7.714285714\ \text{in}
$$

Treads: 13. Run: \(13 \times 10 / 12 = 10.83333333\) ft. Stringer: 14.08407296 ft. Angle: 37.64762064°. The riser is below 7.75 in and the tread equals 10 in, so neither IRC message is added.

Boundary: a maximum riser larger than the code value can still set the geometry, and the check then reports the code exceedance. A tread of 0 is rejected by the field minimum.

## Limitations

The help text names IRC, UK Approved Document K, and typical AU NCC limits. Those publications were not opened. The numbers used are the literals in the module.

## Reference Standards

IRC, UK Approved Document K, and AU NCC are named in the field help and in the code table. The publications were not opened. Reference standards are pending. The comparison values are the literals 7.75 in, 10 in, 220 mm, 42°, 190 mm, and 240 mm as stored.

## Online Calculator

https://diycalclab.com/lumber/stair-calculator/

## Related Formulas

- [Deck board count](deck-board-count.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `stair` |
| Evidence | Production `stair.BGMYrKYH.js`, IRC limits 7.75 in and 10 in, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 14 risers at 7.714285714 in, run 10.83333333 ft, angle 37.64762064° |
| Boundary | a riser above the stored code maximum is flagged; the geometry still uses the typed maximum |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
