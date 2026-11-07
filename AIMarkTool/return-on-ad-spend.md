# Return on ad spend

## Overview

The ROAS calculator divides attributed revenue by advertising spend and formats the ratio. If either input is missing or not a finite number, the API says so instead of inserting a benchmark. The ratio is not a profit figure: revenue is the numerator, and cost of goods is not an input.

The production page schema, read 2026-11-07, requires `revenue` ≥ 0 and `adSpend` > 0. The calculator POSTs JSON `{inputs, locale}` to `/api/tools/roas-calculator`. The worked numbers below are responses from that endpoint on the same date.

## Formula

$$
\mathrm{ROAS} = \frac{\mathrm{revenue}}{\mathrm{ad\ spend}}
$$

The formatted field is the ratio with two fraction digits and an `x` suffix. `Math` rounding of a trailing 5 follows the API, which returned `2.64x` for the second example below.

## Variables

| Name | Constraint | Unit |
|---|---|---|
| Revenue | Finite number ≥ 0 | money, same currency as spend |
| Ad spend | Finite number > 0 | money |

Strings are rejected with “must be a finite number”. Spend of 0 is HTTP 400, `adSpend must be greater than 0`. Revenue of 0 is allowed and returns ROAS 0.

## Engineering Principles

ROAS answers “how many currency units of the entered revenue came back per currency unit of the entered spend.” It does not subtract refunds, fees, or cost of goods unless those were already removed from the revenue you type. A ratio above 1 only means revenue exceeded spend. It does not say the ads were profitable.

## Worked Example

Paid-search style inputs from the page, sent as numbers.

1. Revenue 42000, spend 12000. ROAS = \(42000/12000 = 3.5\). The API returned `3.5` and formatted `3.50x`.
2. Revenue 18500, spend 7000. ROAS = \(18500/7000 = 2.642857142857143\). The API returned that full value and formatted `2.64x`.
3. Revenue 0, spend 2500. The API returned `0` and `0.00x`.

Boundary: `adSpend: 0` returned HTTP 400. String inputs returned HTTP 400, “revenue must be a finite number”.

## Limitations

- No attribution model, no time window, no margin.
- The lead-gen sentences on the page are commentary attached to ranges of the ratio. They are not a second formula and they are not a guarantee about a campaign.
- Currency symbols are not parsed. The two inputs have to already be in one currency.

## Reference Standards

No advertising standard is referenced by the schema that was read. Status: pending.

## Online Calculator

The 42000 / 12000 case is accepted by the ROAS form:

https://aimarktool.com/tools/roas-calculator

## Related Formulas

- [Order-value LTV to CAC](order-value-ltv-to-cac.md)

## Verification

| Item | Value |
|---|---|
| Source tool | AIMarkTool `roas-calculator` |
| Evidence | Page schema and POST `/api/tools/roas-calculator` responses on 2026-11-07 |
| Method | Compared 42000/12000, 18500/7000, and the zero-revenue and zero-spend cases with the API |
| Example result | 3.5 formatted 3.50x; 2.642857… formatted 2.64x |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
