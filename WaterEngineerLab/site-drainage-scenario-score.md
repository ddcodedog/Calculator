# Weighted score for two drainage layouts

## Overview

The site-drainage comparator ranks layouts you have already sized. It normalizes the metrics you type and applies weights you type. The production page says no new hydraulic solver is introduced. Peak flow, capacity, pipe length, excavation, diameter, and outfall count are inputs. This note does not solve Manning flow or a rainfall hydrograph (https://waterengineerlab.com/tools/site-drainage-layout-scenario-comparator).

Production function in the TOOL-015 page chunk, engine 1.0.0, formula id `FORMULA-TOOL015-SCENARIO-COMPARATOR-001`, read 2026-11-08. The worked pair is not the pair prefilled in the form.

## Formula

Capacity-margin ratio, higher is better:

$$
m = \frac{Q_{\mathrm{available}} - Q_{\mathrm{peak}}}{Q_{\mathrm{peak}}}
$$

For a metric with values \(v_i\), let \(v_{\min}\) and \(v_{\max}\) be the minimum and maximum inside the current pair. If they are equal, every scenario scores 1 on that metric. Otherwise

$$
s_i = \frac{v_i-v_{\min}}{v_{\max}-v_{\min}} \text{ when higher is better}, \qquad s_i = \frac{v_{\max}-v_i}{v_{\max}-v_{\min}} \text{ when lower is better}
$$

Pipe length, excavation length, maximum diameter, and outfall count are lower-is-better. The weighted score is the sum of weight times score. Weights must be ≥ 0 and must sum to 1 within \(10^{-9}\). At least two scenarios are required, with unique ids. Flows, pipe length, and diameter must be finite and > 0. Excavation must be ≥ 0. Outfalls must be an integer ≥ 1.

Utilization is \(Q_{\mathrm{peak}}/Q_{\mathrm{available}}\). Capacity status is `adequate` when available capacity is at least the peak, and `inadequate` otherwise. Inadequate rows stay in the ranking. Sort is score descending, then id with `localeCompare`. A later row keeps the previous rank when the absolute score difference is ≤ \(10^{-12}\).

## Variables

| Name | Meaning | Unit in this example |
|---|---|---|
| Design peak | Flow the layout must carry | m³/s |
| Available capacity | Capacity you already computed | m³/s |
| Pipe length | Total pipe | m |
| Excavation | Trench length | m |
| Max diameter | Largest pipe | m |
| Outfalls | Discharge points | count |
| Weights | Five explicit weights | 1, sum to 1 |

## Engineering Principles

A score of 1 on a metric means “best inside this pair,” not “acceptable in the watershed.” Changing either scenario, or changing a weight, changes the normalization. The top rank can still be hydraulically inadequate. The chunk labels that outcome `one-or-more-inadequate` when any member of the tied top set is inadequate.

## Worked Example

Weights: capacity margin 0.40, pipe length 0.25, excavation 0.15, diameter 0.10, outfalls 0.10.

North: peak 0.50 m³/s, capacity 0.80 m³/s, pipe 240 m, excavation 180 m, diameter 0.60 m, 1 outfall.

South: peak 0.70 m³/s, capacity 0.65 m³/s, pipe 160 m, excavation 150 m, diameter 0.45 m, 2 outfalls.

1. Margin ratios: North \((0.80-0.50)/0.50 = 0.60\). South \((0.65-0.70)/0.70 = -0.07142857\ldots\).
2. North is better on margin and on outfall count, so those scores are 1 and South’s are 0. South is better on pipe, excavation, and diameter, so those scores are 1 and North’s are 0.
3. North score = \(0.40\times 1 + 0.10\times 1 = 0.50\). South score = \(0.25+0.15+0.10 = 0.50\).
4. Utilization: North \(0.50/0.80 = 0.625\) (adequate). South \(0.70/0.65 \approx 1.0769\) (inadequate).
5. The scores tie within \(10^{-12}\), so both ranks are 1. Id order `north` then `south` is only the sort order. The top-set label is `one-or-more-inadequate`.

Moving 0.10 from pipe length onto capacity margin, so the weights become 0.50, 0.15, 0.15, 0.10, 0.10, makes North 0.60 and South 0.40. That sensitivity is the reason the weights are inputs rather than hidden constants. A weight set that sums to 0.90 is rejected.

## Limitations

- No runoff, pipe-capacity, or hydraulic-grade-line solution is executed here.
- Two scenarios in the V1 form. The normalizer itself maps every scenario you pass, but this example uses two.
- US customary fields are converted with 0.3048 m/ft, 0.0254 m/in, and 0.028316846592 m³/s per cfs before scoring. The example stays in SI so that conversion is idle.

## Reference Standards

Source ids stored in the chunk are `SRC-SCENARIO-COMPARATOR-TOOL015-001` and `SRC-PROJECT-METHOD-TOOL015-001`, version 1.0.0. The underlying method statements were not re-read. Status: pending.
## Online Calculator

Compare a pair you have already sized on the production page:

https://waterengineerlab.com/tools/site-drainage-layout-scenario-comparator

## Related Formulas

- [Catchment breakdown and peak runoff sum](catchment-runoff-summary.md)
- [Rational-method peak runoff](rational-method-peak-runoff.md)

## Verification

| Item | Value |
|---|---|
| Source tool | WaterEngineerLab `TOOL-015` |
| Evidence | Production min-max function, weight sum check, tie tolerance \(10^{-12}\), inadequate rows retained |
| Method | Python replay of the two-scenario score |
| Example result | Both weighted scores 0.50, shared rank 1, South inadequate |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
