# Eight thousand planned visitors are not the forty you already have

Locale: en

## Two different visitor words

The sample-size tool asks how many visitors to **collect** before comparing two conversion rates. The funnel tool describes visitors you **already chose as a scenario**. The shop in the companion note has 800 landing visitors and 40 customers. That history does not satisfy a sample-size plan, and the plan does not create customers.

## The plan

Baseline 5%, absolute lift 1 percentage point, so the two rates are 0.05 and 0.06. Alpha 0.05, power 0.80, two-sided, equal groups, unpooled variance, no continuity correction. Those settings are what the API states; they were not sent as extra fields.

The production API on 2026-11-10 returned unrounded \(n = 8154.986047988399\), **8155** visitors per variation, **16310** total. A local evaluation of

$$
n = \frac{(z_{0.975}+z_{0.80})^{2}\,[p_1(1-p_1)+p_2(1-p_2)]}{(p_2-p_1)^{2}}
$$

with Python’s normal quantiles ceilings to the same 8155. The service’s unrounded value and the local value differ in the sixth decimal and agree on the integer that is rounded up. A pooled calculator can print a different integer; the API says so.

## The arrivals

800 visitors at 50%, 40%, and 25% become 40 customers if that funnel is the one you believe. 800 is less than 8155. You do not have a full variation yet, even if all 800 saw only one version. Splitting 800 into two groups would be about 400 each, which is not 8155.

Do not type 8155 into the funnel as “visitors” and treat the resulting customer count as people who already converted. That is a plan, not a log. Do not type 40 into the sample-size tool as the baseline percent. Forty customers out of 800 arrivals is a 5% rate only if you define conversion as customer/visitor on this path (\(40/800 = 0.05\)). That equality is specific to these two inputs. It is not what the sample-size page computes. The sample-size page never sees the 800.

## What you may conclude

- If the test you want is “5% versus 6%,” plan on 8155 visitors in each variation before you compare rates.
- The 40 customers and the 3.00x ROAS from a 2880/960 illustration are a different decision. They do not shrink 8155.
- Stopping at 800 visitors because a dashboard already shows a rate is not this formula.

## Limits

- Equal groups, one conversion definition, no peeking correction.
- 8155 is not a probability that a variant wins.
- No claim about ad ranking or traffic.

## Tools

- Sample size: https://aimarktool.com/tools/ab-test-sample-size-calculator
- Funnel, only as a scenario count: https://aimarktool.com/tools/funnel-conversion-calculator

## Online Calculator

The planning count is the sample-size page:

https://aimarktool.com/tools/ab-test-sample-size-calculator

## Related Formulas

- [Equal-group sample size for an absolute rate lift](ab-equal-group-sample-size.md)
- [Successive funnel counts from stage percents](funnel-stage-counts.md)

## Verification

| Item | Value |
|---|---|
| Source tool | `ab-test-sample-size-calculator` production POST, 2026-11-10 |
| Evidence | Unrounded 8154.986047988399, 8155 per variation, 16310 total. Local NormalDist ceiling matches |
| Not done | No browser click. Funnel 800 → 40 was a separate POST used only as the contrasting count |
| Dedup scope | Landing-page workflow and the earlier 8% + 1.5 point note. This dataset is 5% + 1 point. Not a web-wide scan |
| Example result | 8155 per variation against an 800-visitor scenario |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |