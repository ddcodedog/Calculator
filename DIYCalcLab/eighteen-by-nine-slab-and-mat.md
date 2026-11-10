# One 18 by 9 ft pad, then the steel that sits in it

Locale: en

## Bill, not two unrelated projects

The concrete tool counts bags from a volume. The rebar tool counts bars from the same rectangle’s clear spans. The patio case already on the site is 14 by 12 ft at 4 in and does not continue into this mat. The default rebar example is a 20 ft square. This pad is 18 ft by 9 ft.

## Concrete

Thickness 4 in, one slab, 7% waste, 80 lb bags at 0.60 ft³ each. Imperial length enters in feet and depth in inches; the module converts with 0.3048 and 0.0254 before the cubic metres exist.

$$
V = 18\times 9\times\frac{4}{12} = 54\,\mathrm{ft^3} = 1.52911\,\mathrm{m^3}
$$

With waste, \(54\times 1.07 = 57.78\,\mathrm{ft^3}\). Bag yield in cubic metres is \(0.60\times(0.3048)^{3}\).

$$
n = \left\lceil\frac{57.78}{0.60} - 10^{-9}\right\rceil = 97
$$

Ninety-seven bags. A 0% waste still needs \(\lceil 54/0.60\rceil = 90\) bags. The waste is not a second thickness.

## Mat on that same outline

Spacing 16 in, cover 2 in each side, #4 bar, stock 20 ft, extra 5% on the purchase count. Lap is unused because both cut lengths are shorter than 20 ft.

Clear length = \(18 - 2\times(2/12) = 17.\overline{6}\,\mathrm{ft}\). Clear width = \(8.\overline{6}\,\mathrm{ft}\).

Bars across the length, spaced at 16 in: \(\lfloor 17.\overline{6}/(16/12)\rfloor + 1 = 14\), each cut to the clear width \(8.\overline{6}\,\mathrm{ft}\).

Bars across the width: \(\lfloor 8.\overline{6}/(16/12)\rfloor + 1 = 7\), each cut to \(17.\overline{6}\,\mathrm{ft}\).

Total cut length = \(14\times 8.\overline{6} + 7\times 17.\overline{6} = 245\,\mathrm{ft}\).

#4 mass in the module is 0.668 lb/ft, so \(245\times 0.668 = 163.66\,\mathrm{lb}\) before the page’s zero-fraction display, which rounds that label to 164 lb.

Short bars share a 20 ft stick: \(\lfloor 20/8.\overline{6}\rfloor = 2\), so \(\lceil 14/2\rceil = 7\) sticks. Long bars need one stick each: 7. Sticks before extra = 14. After 5%, \(14\times 1.05 = 14.7\), which ceils to **15** bars to buy. Crossings to tie = \(14\times 7 = 98\). Chairs = \(\lceil 162/9\rceil = 18\).

## How the two counts meet, and how they do not

The area 162 ft² is the chair divisor and also the plan area inside the concrete volume. Thickness changes the bag count and does not change 14 and 7. Spacing changes the bars and does not change 97 bags. Do not convert 163.66 lb of steel into a bag count, and do not add 15 sticks to 97 bags as if they were one unit.

## Limits

- Bag yield is the module’s 0.60 ft³, not a ticket from a plant.
- One mat, no hooks, no second layer. 40-diameter lap is irrelevant here because the stock is long enough.
- Chair spacing is the fixed 9 ft² divisor, not a structural spacing design.
- No soil bearing check and no code bar size.

## Tools

- Bags: https://diycalclab.com/concrete/slab-calculator/
- Bars: https://diycalclab.com/concrete/rebar-calculator/

## Online Calculator

Order the 97 bags from the slab page, then open the rebar page for the same 18 by 9:

https://diycalclab.com/concrete/slab-calculator/

## Related Formulas

- [Concrete slab volume and bag count](concrete-slab-volume.md)
- [Slab rebar grid count](slab-rebar-grid.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Slab volume, waste, and \(\lceil V/Y - 10^{-9}\rceil\); rebar clear span, shared sticks, 0.668 lb/ft, chair divisor 9 |
| Evidence | Python replay of the production DIY modules’ rules. No browser session |
| Dedup scope | Patio case (14×12), rebar default (20×20), and the concrete guide, read 2026-11-10. Not a web-wide scan |
| Example result | 97 bags; 14 and 7 bars; 15 sticks; 163.66 lb |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |