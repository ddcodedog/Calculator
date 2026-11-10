# Same-interval load factor

## Overview

Load factor here is the average demand over one interval divided by the peak demand in that same interval. The calculator does not estimate a monthly billing demand, a diversity factor, or a plant efficiency. If the average would exceed the peak, it rejects the inputs instead of returning a number above 1.

Production chunk for `load-factor`, model 1.0.0, read 2026-11-07. The source note in the chunk points at the EIA glossary entry for load factor and marks the license status review-required (https://powerengineerlab.com/calculators/load-factor/).

## Formula

$$
P_{\mathrm{avg}} = \frac{E}{h}, \qquad \mathrm{LF} = \frac{P_{\mathrm{avg}}}{P_{\mathrm{peak}}}, \qquad \mathrm{LF}_{\%} = 100\times\mathrm{LF}
$$

\(E\) is energy in kWh, \(h\) is the interval length in hours, and \(P_{\mathrm{peak}}\) is the peak demand in kW. Energy must be ≥ 0. Hours and peak must be > 0. All three must be finite. \(\mathrm{LF} > 1\) is the error `INTERVAL_BOUNDARY`.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Energy | Metered energy in the interval | kWh |
| Hours | Length of that same interval | h |
| Peak | Highest demand in that interval | kW |

## Engineering Principles

Average demand is energy divided by time, so the hours have to be the hours that produced the kWh. A 15-minute peak paired with a full day of energy is a different definition and is not what this tool computes. Load factor of 1 means the load sat on the peak for the whole interval. Load factor of 0 means the energy was zero while a positive peak was still entered, which the tool allows.

## Worked Example

Energy 1200 kWh, interval 24 h, peak 100 kW.

1. Average demand = \(1200/24 = 50\,\mathrm{kW}\).
2. Load factor = \(50/100 = 0.50\).
3. Percent = 50%.

Boundary: 3000 kWh in 24 h with the same 100 kW peak gives an average of 125 kW. The tool returns `INTERVAL_BOUNDARY` and no load factor. Zero energy, 24 h, peak 100 kW returns load factor 0.

## Limitations

- Same-interval definition only. No demand factor, diversity, utilization, or billing ratchet.
- The peak is an input. The tool does not read a demand interval from a meter file.
- A higher load factor is not, by itself, a claim about cost or equipment size.

## Reference Standards

EIA glossary, “Load factor,” is the citation stored in the calculator chunk, with `licenseStatus: review-required`. The glossary page was not re-read for this note. Status: pending.
## Online Calculator

Enter the 1200 kWh, 24 h, 100 kW case here:

https://powerengineerlab.com/calculators/load-factor/

## Related Formulas

- [Ideal transformer turns and voltage ratio](transformer-turns-ratio.md)
- [Kilowatt to mechanical horsepower](kilowatt-to-horsepower.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `load-factor` |
| Evidence | Production chunk: average = energy/hours, load factor = average/peak, reject when average exceeds peak |
| Method | Recomputed 1200/24/100 and the 3000 kWh rejection |
| Example result | 50 kW average, load factor 0.50 |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
