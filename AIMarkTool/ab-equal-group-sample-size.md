# Equal-group sample size for an absolute rate lift

## Overview

This sample-size tool plans how many visitors each of two equal groups needs before you compare conversion rates. The production API describes the test as two-sided, equal groups, unpooled variance, no continuity correction, alpha 0.05, and power 0.80. The lift is an absolute difference in percentage points. The count is rounded up. It is not a probability that a test has already won.

The page’s own illustration is a 10% baseline plus 2 points. This note uses 8% and 1.5 points so the arithmetic is a separate case. The API was called on 2026-11-08.

## Formula

Baseline rate \(p_1 = P_1/100\) and variant rate \(p_2 = p_1 + \Delta/100\), where \(\Delta\) is the absolute lift in percentage points. The unpooled two-sample expression that matches the API’s ceiling is

$$
n = \frac{(z_{1-\alpha/2}+z_{\mathrm{power}})^2\,\left[p_1(1-p_1)+p_2(1-p_2)\right]}{(p_2-p_1)^2}
$$

with \(\alpha=0.05\) and power 0.80. Visitors per variation are \(\lceil n\rceil\). The total is twice that. A calculator that pools variance under the null, which the API names as Evan Miller’s, prints a different integer. Python’s `NormalDist` inverse CDF gives \(z_{0.975}=1.959963984540054\) and \(z_{0.80}=0.841621233572914\), and that pair produces \(n=5566.59992715\). The API’s unrounded value is \(5566.599929880218\). Both ceiling to the same visitor count. The z constants inside the service were not extracted as literals, so the API integer is the result this note relies on.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Baseline | Current conversion | % |
| Absolute lift | Difference to detect | percentage points |
| Alpha | Two-sided false-positive rate, fixed | 0.05 |
| Power | Fixed | 0.80 |

## Engineering Principles

An 8% baseline plus 1.5 points is a comparison of 8% with 9.5%, not of 8% with 8% times 1.015. Relative and absolute lifts of “1.5” are different experiments. Rounding is per variation, after the unrounded \(n\), and the total is the sum of the two rounded groups.

## Worked Example

Baseline 8%. Absolute lift 1.5 points. Rates 0.08 and 0.095.

1. The API returned unrounded \(n = 5566.599929880218\).
2. Per variation = 5567.
3. Total = \(2\times 5567 = 11134\).

The local NormalDist evaluation ceilings to the same 5567. A pooled calculator can disagree; the API says so, and this note does not reprint that other integer. A lift of 0 is not a detectable difference and is rejected by the rate construction this formula uses.

## Limitations

- Equal group sizes, one conversion definition, no continuity correction, no sequential peeking adjustment.
- Alpha and power are fixed in the response that was checked. They were not sent as inputs.
- 5567 is a planning count. Collecting it does not mean the variant won.

## Reference Standards

The API names the two-sided unpooled z-test and contrasts it with a pooled calculator. A textbook derivation of the z quantiles was not attached by the service. Status: pending.

## Online Calculator

Plan the 8% versus 9.5% comparison here:

https://aimarktool.com/tools/ab-test-sample-size-calculator

## Related Formulas

- [Return on ad spend](return-on-ad-spend.md)
- [Order-value LTV to CAC](order-value-ltv-to-cac.md)

## Verification

| Item | Value |
|---|---|
| Source tool | AIMarkTool `ab-test-sample-size-calculator` 1.0.0 |
| Evidence | Production POST: unrounded 5566.599929880218, 5567 per variation, total 11134; method text as quoted |
| Method | API call plus a NormalDist evaluation of the unpooled expression, same ceiling |
| Example result | 5567 visitors per variation, 11134 total |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
