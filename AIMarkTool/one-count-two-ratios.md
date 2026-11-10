# Forty customers, then a ratio that sometimes equals ROAS

Locale: en

## The trap

A landing path and a money path can print the same 3.00x. That match is an algebra accident of this dataset. Change how often a customer buys and only one of the ratios moves.

## Funnel count

800 visitors, then 50% of visitors, 40% of that stage, 25% of the next. The production API on 2026-11-10 returned stage counts 400, 160, and 40 customers, displayed `400.00`, `160.00`, and `40.00`. Each percent multiplies the unrounded previous count. Forty is not a benchmark. It is this chain.

Assumption used only after that count: each of the 40 customers places one order at 72 currency units in the period you are scoring. Revenue for the ROAS box is \(40\times 72 = 2880\). If some customers buy twice, this revenue is wrong and the funnel tool will not correct it. The funnel tool has no price field.

## ROAS

Spend 960. The ROAS API returned `roas: 3` and `formatted: "3.00x"`.

$$
\mathrm{ROAS} = 2880/960 = 3
$$

The response text that calls 3.00x “worth continued optimization” is commentary attached to the ratio. It is not a second measurement. Spend of 0 is rejected. Revenue of 0 would return 0.

## LTV over CAC, same 40 and same 960

API fields: marketing and sales spend 960, new customers 40, average order value 72, purchases per year 1, retention 1 year. The API returned CAC 24, LTV 72, and `ltvToCac: 3` (`3.00x`).

$$
\mathrm{CAC} = 960/40 = 24, \qquad \mathrm{LTV} = 72\times 1\times 1 = 72, \qquad 72/24 = 3
$$

So ROAS and LTV/CAC both say 3. That happens because LTV collapsed to one order value and revenue was defined as customers times that same order value:

$$
\frac{\mathrm{LTV}}{\mathrm{CAC}} = \frac{\mathrm{AOV}\times 1\times 1}{\mathrm{spend}/\mathrm{customers}} = \frac{\mathrm{customers}\times\mathrm{AOV}}{\mathrm{spend}} = \mathrm{ROAS}
$$

## The purchase-frequency split

Same API with purchases per year set to 4, retention still 1 year: CAC stays 24, LTV becomes \(72\times 4 = 288\), ratio **12** (`12.00x`). ROAS is still 3, because the 2880 and the 960 did not change. Quoting “3x” without saying which tool produced it is how those two sentences get swapped.

Neither ratio subtracts cost of goods. The LTV here is order value, not margin. A comfortable 12x on order value can be a poor margin result. The API does not compute that margin.

## Limits

- Funnel rates are typed. They are not estimated from the 960 spend.
- Sample size is a different tool. Forty customers is not a test plan.
- No attribution window. Currency is whatever you already used in both money fields.

## Tools

- Counts: https://aimarktool.com/tools/funnel-conversion-calculator
- ROAS: https://aimarktool.com/tools/roas-calculator
- LTV/CAC: https://aimarktool.com/tools/cac-ltv-calculator

The ROAS guide’s labeled sample is 42000/12000, and the CAC guide’s sample is not this 40-customer path. The campaign-performance workflow is a planning checklist, not this arithmetic.

## Online Calculator

The ratio that stays at 3.00x when purchase frequency changes is ROAS:

https://aimarktool.com/tools/roas-calculator

## Related Formulas

- [Successive funnel counts from stage percents](funnel-stage-counts.md)
- [Return on ad spend](return-on-ad-spend.md)
- [Order-value LTV to CAC](order-value-ltv-to-cac.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Funnel, ROAS, and CAC/LTV production POST APIs, 2026-11-10 |
| Evidence | HTTP 200 responses: customers 40; ROAS 3; LTV/CAC 3 at 1 purchase/year and 12 at 4 |
| Not done | No browser click. The lead-gen sentences in the JSON were not treated as measurements |
| Dedup scope | ROAS guide, CAC guide, and the review-campaign and landing-page workflows, read 2026-11-10. Not a web-wide scan |
| Example result | 40 customers, ROAS 3.00x, LTV/CAC 3.00x or 12.00x |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |