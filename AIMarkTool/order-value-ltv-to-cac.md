# Order-value LTV to CAC

## Overview

The CAC/LTV calculator divides marketing-and-sales spend by new customers, multiplies average order value by purchases per year and retention years, and divides those two results. The lifetime value in this tool is order value, not gross profit. A sentence on the page about “lifetime gross profit of 800” is a separate illustration; the five-input form does not ask for margin and does not apply one.

Schema and description on the production page, read 2026-11-07. The calculator POSTs `{inputs, locale}` to `/api/tools/cac-ltv-calculator`. The numbers below are API responses from that date.

## Formula

$$
\mathrm{CAC} = \frac{\mathrm{spend}}{\mathrm{customers}}, \qquad \mathrm{LTV} = \mathrm{AOV}\times \mathrm{purchases\ per\ year}\times \mathrm{years}
$$

When CAC is not zero, the reported ratio is LTV divided by CAC.

Spend must be ≥ 0. New customers must be ≥ 1. Average order value and purchases per year must be ≥ 0. Retention years is required and was accepted as 2.5 in the call below. When CAC is 0, the JSON field `ltvToCac` is null. The sentence text in that same response still said `LTV/CAC = 0.00x`. Those two fields disagree; the null is the numeric result.

## Variables

| Name | Role | Constraint |
|---|---|---|
| Marketing and sales spend | CAC numerator | ≥ 0 |
| New customers | CAC denominator | ≥ 1 |
| Average order value | LTV factor | ≥ 0 |
| Purchases per year | LTV factor | ≥ 0 |
| Retention years | LTV factor | required |

## Engineering Principles

Leaving sales cost out of the spend field lowers CAC and raises the ratio. Using order value instead of gross profit raises LTV by whatever share of the order is not margin. The page FAQ makes the same point: a ratio that looks comfortable for a high-margin subscription can be the wrong reading for a low-margin order. The API label on a high ratio is commentary, not a measured outcome.

## Worked Example

1. Spend 24000, 120 customers, order value 99, 12 purchases per year, 2.5 years.
2. CAC = \(24000/120 = 200\).
3. LTV = \(99\times 12\times 2.5 = 2970\).
4. Ratio = \(2970/200 = 14.85\). The API returned `cac: 200`, `ltv: 2970`, `ltvToCac: 14.85`.

Second call: spend 18000, 450 customers, order value 68, 3.2 purchases per year, 1.8 years.

1. CAC = \(18000/450 = 40\).
2. LTV = \(68\times 3.2\times 1.8 = 391.68\).
3. Ratio = \(391.68/40 = 9.792\). The API returned `391.68000000000006` and `9.792000000000002`, which display as 391.68 and 9.79x.

Boundary: spend 0, 10 customers, order value 80, 1 purchase per year, 1 year returned CAC 0, LTV 80, and `ltvToCac: null`, while the sentence text said `0.00x`.

## Limitations

- Order-value LTV, not margin and not discounted cash flow.
- One average order value and one retention period. No churn curve.
- A larger ratio is not evidence that the spend was a good idea.

## Reference Standards

No marketing-finance standard is referenced by the schema that was read. Status: pending.

## Online Calculator

The 24000 / 120 / 99 / 12 / 2.5 case is accepted by the form:

https://aimarktool.com/tools/cac-ltv-calculator

## Related Formulas

- [Return on ad spend](return-on-ad-spend.md)

## Verification

| Item | Value |
|---|---|
| Source tool | AIMarkTool `cac-ltv-calculator` |
| Evidence | Page schema and POST `/api/tools/cac-ltv-calculator` responses on 2026-11-07 |
| Method | Recomputed CAC, order-value LTV, and the ratio, including the zero-spend null |
| Example result | CAC 200, LTV 2970, ratio 14.85 |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
