# Successive funnel counts from stage percents

Locale: en

## Direct Answer

This funnel tool starts with a visitor count and applies three stage percents in order. Each percent multiplies the previous unrounded count. The two-decimal strings are for reading. Multiplying those strings again would drift. The result is the count on the path you typed. The API’s own note says that count is not an industry benchmark.


## Overview

Checked with a production POST to the funnel tool on 2026-11-08, tool version 1.0.0. Inputs were numbers. The worked example lists the counts the response returned (https://aimarktool.com/tools/funnel-conversion-calculator).
## Formula

$$
C_1 = V\,\frac{p_1}{100}, \qquad C_2 = C_1\,\frac{p_2}{100}, \qquad C_3 = C_2\,\frac{p_3}{100}
$$

\(V\) is visitors. Each \(p\) is a percent of the previous count, not a percent of the original visitors. Display values are \(C\) formatted to two decimals. Zero visitors is allowed and yields zeros. A blank visitors field is a required-input failure on the API.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Visitors | People entering the path | count |
| Stage 1 percent | Share of visitors who reach stage 1 | % of previous |
| Stage 2 percent | Share of stage 1 who reach stage 2 | % of previous |
| Stage 3 percent | Share of stage 2 who become customers | % of previous |

## Engineering Principles

A stage percent of 20 after a stage of 202.5 is 40.5 customers, not \(1250\times 0.20\). The second reading is a different funnel. The API note says the next multiplication uses the count before two-decimal display rounding. 40.50 on the card is still the unrounded 40.5 for this particular input, because 40.5 already ends at two decimals.

## Worked Example

1,250 visitors. Stage rates 36%, 45%, and 20%.

1. Stage 1 = \(1250\times 0.36 = 450\). Display `450.00`.
2. Stage 2 = \(450\times 0.45 = 202.5\). Display `202.50`.
3. Customers = \(202.5\times 0.20 = 40.5\). Display `40.50`.

The API returned those three numbers and those three display strings on 2026-11-08. Using the rounded stage-2 text as if it were 203 would produce 40.6 customers, which is not this tool. Zero visitors with the same percents returns 0 at every stage.

## Limitations

- Three stages, fixed order. There is no revenue field and no cost field.
- Rates are inputs. Nothing in the response estimates them from a campaign export.
- 40.5 customers is an arithmetic count. It is not a forecast interval.

## Reference Standards

No marketing-science standard is cited by the response. Status: pending.
## Online Calculator

Submit 1250, 36, 45, and 20 on the production tool:

https://aimarktool.com/tools/funnel-conversion-calculator

## Related Formulas

- [Return on ad spend](return-on-ad-spend.md)
- [Order-value LTV to CAC](order-value-ltv-to-cac.md)

## Verification

| Item | Value |
|---|---|
| Source tool | AIMarkTool `funnel-conversion-calculator` 1.0.0 |
| Evidence | Production POST body: stage1 450, stage2 202.5, customers 40.5, displays 450.00 / 202.50 / 40.50 |
| Method | Hand product checked against the API |
| Example result | 450, 202.5, and 40.5 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |