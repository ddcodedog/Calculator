# The pitch tool’s rafter length is the board-foot length

## Fork in the order

A gable is 24 ft wide, overhang 1 ft each side, rise 6 in on a 12 in run. Rafters are spaced at 16 in along a 20 ft building. The pitch calculator returns a rafter length in feet. The board-foot calculator bills thickness × width × that length × piece count, divided by 12. Which thickness and width you type decides the bill, because the lumber tool does not convert nominal 2×8 into dressed 1½×7¼.

## Pitch and length

$$
p = 12\times\frac{6}{12} = 6, \qquad k = \sqrt{1+(6/12)^{2}} = \sqrt{1.25} = 1.118034
$$

Angle = \(\arctan(6/12) = 26.565^\circ\). The module’s slope class at pitch 6 is “conventional” (the bands are below 2, below 4, through 9, and above 9).

$$
L_{\mathrm{rafter}} = \left(\frac{24}{2}+1\right)\times 1.118034 = 14.534442\,\mathrm{ft}
$$

Ridge height would be \((24/2)\times(6/12) = 6\,\mathrm{ft}\) above the plate line, before any heel. That height is not a board-foot input.

## How many sticks

Along 20 ft at 16 in (1.333 ft): \(\lfloor 20/1.333333\rfloor + 1 = 16\) rafters. This count is layout arithmetic, not a third calculator. The pitch tool does not emit it.

## Two bills for the same 16 sticks

Dressed sizes typed as 1.5 in × 7.25 in × 14.534442 ft × 16:

$$
\mathrm{BF} = \frac{1.5\times 7.25\times 14.534442\times 16}{12} = 210.749
$$

Nominal 2 × 8 typed instead:

$$
\mathrm{BF} = \frac{2\times 8\times 14.534442\times 16}{12} = 310.068
$$

The difference is 99.3 board feet on the same geometry. The module’s help text says yards often bill the nominal size. The formula uses the numbers in the boxes. Adding 210.749 to 310.068 double-counts the same rafters.

## What does not belong in the length

The span and the overhang are already inside 14.534 ft. Do not also multiply by the slope factor a second time. A deck-board count from the deck planner is a different member, in plan feet, and the site’s deck guide is a 16×12 ft example this note does not use.

## Limits

- No birdsmouth, no ridge thickness subtraction, no hip.
- 16 rafters assumes the first and last sit on the 20 ft ends and the spacing divides evenly enough for the floor-plus-one count. A layout that starts inset needs a different count.
- No span table and no species. Board feet are volume, not capacity.

## Tools

- Pitch and rafter length: https://diycalclab.com/roofing/roof-pitch-calculator/
- Board feet: https://diycalclab.com/lumber/board-foot-calculator/

## Online Calculator

Type 14.534 ft as the length, and decide nominal or dressed before you do:

https://diycalclab.com/lumber/board-foot-calculator/

## Related Formulas

- [Roof pitch and slope factor](roof-pitch.md)
- [Board-foot lumber volume](board-foot.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Pitch \(k=\sqrt{1+(p/12)^{2}}\) and rafter length; board feet \((t w L N)/12\) |
| Evidence | Python replay. No browser session |
| Dedup scope | Deck guide (16×12), roofing-squares guide, and nominal-versus-actual lumber guide titles in the DIY sitemap. Not a web-wide scan |
| Example result | 14.534 ft rafters; 210.749 BF dressed or 310.068 BF nominal |
| Date | 2026-11-10 |
| Status | VERIFIED |
