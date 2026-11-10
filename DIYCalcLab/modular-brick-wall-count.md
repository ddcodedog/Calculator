# Modular bricks for a wall with one opening

## Overview

The brick calculator counts masonry units from a net wall area, a brick size, a mortar joint, a number of skins, and a waste percent, then rounds up. Mortar bags are a separate volume estimate. The example is a US modular brick wall 18 ft long and 6 ft high with one 3 ft by 4 ft opening, not the 20 ft by 4 ft sample filled in on the form.

The production module `brick.BB34k2FS.js` and the unit table in `prefs.B8zLZl5V.js` were read on 2026-11-08. Imperial lengths are multiplied by 0.3048 before the count. The joint, when the field is left blank, uses the brick’s own joint. US modular brick is 7.625 in by 2.25 in by 3.625 in with a 0.375 in joint. Those inches become metres by multiplying by 0.0254. Positive counts use \(\lceil x-10^{-9}\rceil\). Waste multiplies by \(1+\max(0,p)/100\) (https://diycalclab.com/masonry/brick-calculator/).

## Formula

Bricks per square metre of one skin:

$$
n = \frac{1}{(L+j)(H+j)}
$$

Net area, after the imperial-to-metre conversion:

$$
A = \max(0,\; L_{\mathrm{wall}} H_{\mathrm{wall}} - A_{\mathrm{open}})
$$

Ordered bricks for \(s\) skins:

$$
N = \lceil A\, n\, s\,(1+p/100) - 10^{-9}\rceil
$$

Mortar volume for a single skin is the wall-face volume minus the brick solid volume, and it cannot go below 0:

$$
V = \max\left(0,\; A D - (A n)\, L H D\right)
$$

A double skin adds another copy of that volume plus \(A j\). Bags start from a reference brick. For the imperial 80 lb bag the reference is the same US modular brick and the bag is charged at 37 bricks, with an extra 10% (`MORTAR_EXTRA`) before the ceiling. The 10% is not the waste percent you typed for the brick count.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Length, height | Wall face, imperial entry | ft |
| Opening | Area removed | ft² |
| Brick | US modular | in, converted |
| Joint | Blank, so 0.375 | in |
| Skins | 1 in this example | count |
| Waste | Cuts and breakage | % |

## Engineering Principles

The count is a face count. It does not decide whether a half-brick wall is stable, and it does not include lintels, sills, or ties. Ties appear in the module only for two skins. One skin therefore returns bricks and mortar bags only. The opening is an area you subtract. The module does not know whether that opening is a door or a window.

## Worked Example

18 ft by 6 ft, one 12 ft² opening, single skin, modular brick, joint left blank, 8% waste.

1. Net area in square feet = \(18\times 6-12 = 96\). In square metres, \(96\times 0.3048^2 = 96\times 0.09290304 = 8.91869184\).
2. \(L+j = 8\times 0.0254 = 0.2032\) m. \(H+j = 2.625\times 0.0254 = 0.066675\) m. Bricks per square metre = \(1/(0.2032\times 0.066675) = 73.80967143\).
3. Raw count = \(8.91869184\times 73.80967143 = 658.28571429\). With 8% waste, \(710.94857143\). Ceiling gives 711 bricks.
4. Mortar volume = 0.15030683 m³. Dividing by the reference volume per brick, applying 10%, and dividing by 37 gives 19.57065637, which ceilings to 20 bags of the 80 lb mix.

A waste of 0 still ceilings 658.28571429 up to 659 bricks. A wall area that is entirely opening returns 0 bricks. A negative length is clamped by the field minimum before this arithmetic.

## Limitations

- Modular size and the 0.375 in joint are table values. A brick that measures differently needs the matching option or an explicit joint.
- Bag yield is the module’s 0.67 ft³ reference, not a weigh-in of a brand.
- No structural check, no bond pattern beyond the face module, and no corner return unless that area is inside the length and height.

## Reference Standards

The module’s size labels are trade sizes. ASTM brick specifications were not re-read. Status: pending.
## Online Calculator

Count the 18 ft by 6 ft wall, with the 12 ft² opening and 8% waste, here:

https://diycalclab.com/masonry/brick-calculator/

## Related Formulas

- [Concrete slab volume and bag count](concrete-slab-volume.md)
- [Fence posts, rails, and pickets](fence-post-and-picket-count.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `brick` |
| Evidence | Production brick module and prefs conversions 0.3048 and 0.0254, ceil \(x-10^{-9}\), mortar extra 10% |
| Method | Python replay of area, bricks per square metre, waste, and bag ceiling |
| Example result | 711 bricks and 20 mortar bags |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
