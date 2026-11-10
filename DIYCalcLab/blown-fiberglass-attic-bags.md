# Blown-fiberglass bags for an attic top-up

Locale: en

## Direct Answer

The insulation calculator can count batts from a coverage table, or blown insulation from a chart of bags per 1,000 ft² and settled depth. This note uses the blown-fiberglass chart and an attic that already has some insulation, so the added R-value is the target minus what is there. The chart row is not a code check. The module mentions 2021 IECC attic R-values in help text; that text was not treated as a compliance result.


## Overview

Production module `insulation.n4EdxFLF.js`, read 2026-11-08. Imperial length and width are converted with 0.3048, then divided by \(0.3048^2\) to recover square feet. A 22 ft by 28 ft attic is therefore 616 ft² inside the formula. Bags use \(\lceil x-10^{-9}\rceil\) after waste. The fiberglass bag in the chart is labeled 27.5 lb (https://diycalclab.com/drywall/insulation-calculator/).
## Formula

Added R-value:

$$
R_{\mathrm{add}} = \max(0,\; R_{\mathrm{target}}-R_{\mathrm{existing}})
$$

The blown-fiberglass chart rows are \((R,\;\text{bags}/1000,\;\text{inches})\):

13 / 5.9 / 5, 19 / 9 / 7, 22 / 10.5 / 8, 26 / 12.6 / 9.5, 30 / 14.6 / 10.75, 38 / 19 / 13.5, 44 / 22.4 / 15.5, 49 / 25 / 17, 60 / 31.5 / 20.5.

Between two rows the module interpolates linearly. Below the first row and above the last row it scales the end row. Bags before the ceiling:

$$
B = \frac{A_{\mathrm{ft^2}}}{1000}\,b_{1000}\,(1+p/100)
$$

The page also multiplies R by 0.1761 when it shows RSI for a batt. The blown result path used here reports bags, depth, and weight, not that RSI line. Weight on the label is bags times 27.5 lb, then shown with zero fraction digits.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Length, width | Attic floor | ft |
| Target R | Desired total | ft²·°F·h/Btu |
| Existing R | What is already there | same |
| Waste | Extra bags | % |
| Chart | Blown fiberglass | bags/1000 ft² and in |

## Engineering Principles

The depth is the chart’s settled thickness for the added R-value, not a measurement of the existing blanket. Existing R is subtracted first, so you do not buy bags for insulation that is already on the ceiling. A target equal to the existing R returns zero bags and the module’s “nothing to add” warning. Added R below 13 is extrapolated from the first chart row and is flagged. A target above 60 is flagged because the chart stops at R-60.

## Worked Example

Attic 22 ft by 28 ft. Target R-52. Existing R-19. Waste 8%. Blown fiberglass.

1. Area = 616 ft². Added R = \(52-19 = 33\).
2. R-33 sits between the R-30 and R-38 rows. Fraction = \((33-30)/(38-30) = 0.375\).
3. Bags per 1,000 ft² = \(14.6 + 0.375\times(19-14.6) = 16.25\). Settled depth = \(10.75 + 0.375\times(13.5-10.75) = 11.78125\) in.
4. Raw bags = \(616\times 16.25/1000 = 10.01\). With 8% waste, \(10.8108\). Ceiling gives 11 bags.
5. Weight = \(11\times 27.5 = 302.5\) lb. The label formatter with zero fraction digits shows 303 lb.

Existing R of 52 against target 52 returns 0 bags. Added R of 8, below the first chart row, scales the R-13 row by \(8/13\) and raises the below-R-13 warning.

## Limitations

- The chart is the table in the module, not a bag label you photographed. Manufacturers publish their own coverage.
- No framing deduction on the blown path. The batt path uses \(1.5\) divided by the on-center spacing, and this example does not take that path.
- RSI × 0.1761 is the module constant. It is not a blown-output field in this run.
- The IECC sentence in the help text is not a zone lookup.

## Reference Standards

2021 IECC attic values are mentioned in the module help. The code book was not re-read, and the calculator does not select a climate zone. Status: pending.
## Online Calculator

Use the blown-fiberglass path for the 22 ft by 28 ft attic:

https://diycalclab.com/drywall/insulation-calculator/

## Related Formulas

- [Board-foot lumber volume](board-foot.md)
- [Slab rebar grid count](slab-rebar-grid.md)

## Verification

| Item | Value |
|---|---|
| Source tool | DIYCalcLab `insulation`, blown-fiberglass chart |
| Evidence | Production interpolation, bag ceiling, and 27.5 lb label |
| Method | Python replay of the R-30 to R-38 segment and \(\lceil 10.8108-10^{-9}\rceil\) |
| Example result | 16.25 bags/1000 ft², 11.78125 in, 11 bags, 302.5 lb |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |