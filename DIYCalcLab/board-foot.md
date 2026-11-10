# Board-foot lumber volume

Locale: en

## Direct Answer

The Board Foot calculator converts thickness, width, length, and a piece count into board feet. One board foot is a volume of 144 cubic inches, which the module also expresses in cubic metres.


## Overview

Production module `board-foot`, fetched 2026-11-04 from https://diycalclab.com/lumber/board-foot-calculator/. The exported helper is `boardFeet(thicknessIn, widthIn, lengthFt, pieces) = thickness × width × length / 12 × pieces`.
## Formula

$$
\mathrm{BF} = \frac{t_{\mathrm{in}} \times w_{\mathrm{in}} \times L_{\mathrm{ft}} \times N}{12}
$$

The compute path stores the product of the three converted metre dimensions times the piece count, then divides by

$$
144 \times (0.0254)^{3}\,\mathrm{m^3}
$$

which is one board foot. \(1/0.002359737216 = 423.77600066\ldots\) board feet per cubic metre. The page step text rounds that statement to “1 m³ ≈ 423.8 board feet.”

Imperial fields: thickness and width are inches (`depth` × 0.0254), length is feet (`length` × 0.3048). Metric fields: thickness and width are centimetres (`depth` × 0.01), length is metres. Piece count is at least 1.

Cubic feet displayed beside the result are board feet divided by 12, because 1 board foot = 1/12 cubic foot when the inch-foot definition is used.

## Variables

| Name | Field | Imperial unit | Metric unit |
|---|---|---|---|
| Thickness | `thickness` | inch | centimetre |
| Width | `width` | inch | centimetre |
| Length | `length` | foot | metre |
| Pieces | `qty` | count | count |
| Board feet | result | BF | BF |

The help text says yards often bill nominal size (a 2×6 billed as 2 by 6 even when the dressed size is smaller). The formula uses the numbers entered. It does not subtract dressing.

## Engineering Principles

A board foot is a volume unit, not a measure of board length. Thickness and width are in inches and length is in feet in the traditional quotient, which is why the divisor is 12 rather than 144: \(t w L / 12 = (t w (L \times 12)) / 144\) cubic inches. The metric path reaches the same volume by dividing cubic metres by the cubic-metre size of 144 cubic inches.

## Worked Example

Nominal 2 × 6, 8 ft long, 10 pieces, imperial.

1. \(\mathrm{BF} = 2 \times 6 \times 8 / 12 \times 10 = 80\).
2. Volume \(= 80 \times 144 \times (0.0254)^{3} = 0.188778977\ldots\,\mathrm{m^3}\).
3. Cubic feet \(= 80/12 = 6.6666\ldots\,\mathrm{ft^3}\).
4. Per piece \(= 8\,\mathrm{BF}\).

Result: **80 BF**, **0.1888 m³**, **6.667 ft³**.

Boundary: thickness 0 gives **0 BF**. The metre equivalent of 1 BF is \(144 \times (0.0254)^{3} = 0.002359737216\,\mathrm{m^3}\). A metric entry of 50.8 mm × 152.4 mm × 2.4384 m (the metre image of 2 in × 6 in × 8 ft) produces the same 8 BF per piece, within floating-point conversion of 0.3048 and 0.0254.

## Limitations

- No kerf, tongue, or nominal-to-actual table. Enter the size you intend to pay for or the size you intend to install, and do not mix them silently.
- Price per board foot is a straight multiplication when a price is entered. There is no tax or delivery model in the volume formula.
- Large orders (above 1000 BF) only add a UI warning about bundle pricing.

## Reference Standards

**Pending.** No lumber-standard URL is in the module. The 144 in³ definition is the divisor in the source (`BOARD_FOOT_M3 = 144 * (0.0254)**3` via the prefs inch constant).

## Online Calculator

https://diycalclab.com/lumber/board-foot-calculator/

Inventory tool ID: `board-foot`.

## Related Formulas

- [Concrete slab volume and bag count](concrete-slab-volume.md)
- [Roof pitch and slope factor](roof-pitch.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `board-foot` |
| Evidence | `boardFeet` and `BOARD_FOOT_M3 = 144 * inch**3` with `inch = 0.0254` from `prefs.js` |
| Method | \(2\times 6\times 8/12\times 10\) and \(80 \times 144 \times 0.0254^3\) |
| Example result | 80 BF and 0.188779 m³ |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |