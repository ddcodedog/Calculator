# Fence posts, rails, and pickets

## Overview

The fence calculator turns a run length into a count of sections, posts, rails or panels, pickets, and post-hole concrete bags. It is a quantity takeoff. It does not check post embedment against a soil report or a fence code.

The `fence` calculator in the production Astro bundle, read 2026-11-07, uses the shared length factors 0.3048 m/ft and 0.0254 m/in. Counts use `ceil(x - 1e-9)` so a value that is already an integer is not bumped, and anything above an integer rounds up. Waste is `count × (1 + waste%/100)` before that rounding.

## Formula

Gate width is removed first. Infill length is \(\max(0,\ L - n_{\mathrm{gates}} w_{\mathrm{gate}})\).

$$
N_{\mathrm{sections}} = \lceil L_{\mathrm{infill}} / s \rceil, \qquad N_{\mathrm{posts}} = N_{\mathrm{sections}} + 1 + n_{\mathrm{gates}}
$$

Picket style: picket count before waste is \(\lceil L_{\mathrm{infill}} / (w_{\mathrm{picket}}+g) \rceil\), then waste, then ceil again. Rails are \(\lceil N_{\mathrm{sections}}\times n_{\mathrm{rails}}\times (1+\mathrm{waste}/100) \rceil\). Panel style sets panels equal to sections and pickets to zero.

Concrete per hole is the hole cylinder minus the post footprint, not below zero:

$$
V = \max\left(0,\ \pi (d/2)^{2} h - a^{2} h\right)
$$

Bags per hole = \(\lceil 1.1\,V / Y \rceil\), then times the post count. The 10% is inside the per-hole round-up. A 50 lb bag yield in this bundle is \(0.375\times(0.3048)^{3}\,\mathrm{m^3}\).

## Variables

Imperial defaults used below:

| Input | Value |
|---|---|
| Length, post spacing | 100 ft, 8 ft |
| Gates, gate width | 1, 4 ft |
| Rails per section | 3 |
| Style | Pickets, 5.5 in wide, 0 gap |
| Hole diameter, depth, post | 10 in, 30 in, 3.5 in square |
| Bag, waste | 50 lb, 5% |

## Engineering Principles

Posts are sections plus one, plus one extra post per gate, because the gate opening is cut out of the infill but still needs a post on each side of that logic as coded (`sections + 1 + gates`). Spacing that divides the infill evenly does not add a phantom section. Waste applies to pickets and rails, not to posts.

## Worked Example

1. Infill = \(100 - 4 = 96\) ft.
2. Sections = \(96/8 = 12\). Posts = \(12 + 1 + 1 = 14\).
3. Raw pickets = \(\lceil 96\times 12 / 5.5 \rceil = \lceil 209.4545\rceil = 210\). With 5% waste, \(210\times 1.05 = 220.5\), which ceils to 221.
4. Rails = \(\lceil 12\times 3\times 1.05 \rceil = \lceil 37.8\rceil = 38\).
5. Hole volume in metres, then in cubic feet using \((0.3048)^3\): \(1.15086\,\mathrm{ft^3}\). Times 1.1 is \(1.26595\,\mathrm{ft^3}\). Divided by \(0.375\,\mathrm{ft^3}\) is 3.376, which ceils to 4 bags per hole.
6. Bags = \(4\times 14 = 56\).

The on-page cubic-foot line divides by 0.0283168 for display. Bag count uses \((0.3048)^3\), which is the yield constant. Both round to the same 4 bags on this input.

Boundary: spacing that does not divide evenly ceils the section count. Two gates of 4 ft on a 100 ft run cut infill to 92 ft and add two gate posts instead of one. Waste of 0 leaves pickets at 210 and rails at 36.

## Limitations

- One straight run. Corners, slopes, and stepped panels are not extra posts beyond the formula above.
- The 10% concrete factor is fixed in the hole routine.
- Bag yield is the bundle table (50 lb → 0.375 ft³), not a weighed bag from a brand.
- A count is a material list, not a structural sign-off.

## Reference Standards

No fence standard was cited in the calculator module that was read. Status: pending.

## Online Calculator

The 100 ft picket default is the imperial starting point:

https://diycalclab.com/fencing/fence-calculator/

## Related Formulas

- [Slab rebar grid count](slab-rebar-grid.md)
- [Concrete slab volume and bag count](concrete-slab-volume.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `fence` |
| Evidence | Production `fenceSections`, `picketCount`, `holeConcrete`, and the 50 lb yield `0.375 × ft³` |
| Method | Recomputed the imperial defaults in Python with 0.3048 and 0.0254 |
| Example result | 12 sections, 14 posts, 221 pickets, 38 rails, 56 bags |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
