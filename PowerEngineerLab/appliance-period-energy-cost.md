# Appliance energy over a stated duty

## Overview

This calculator estimates kilowatt-hours for one appliance rating, a quantity, a daily schedule, a day count, and a duty factor, then multiplies by a tariff if you type one. Currency is a label. The result is not a utility bill, because it has no taxes, demand charges, or time-of-use blocks.

Production appliance calculator, `TOOL-011`, read 2026-11-08. The chunk states the method as watts times quantity times hours per day times days times duty, divided by 1000.

## Formula

$$
E = \frac{P\,n\,h\,d\,u}{1000}
$$

Cost is \(E\) times the tariff when the tariff field is filled, and `null` when the tariff is blank. \(P\) is watts and must be ≥ 0. Quantity is an integer from 1 to 10,000. Hours per day are from 0 to 24. Days are an integer from 0 to 366. Duty is from 0 to 1. Tariff is blank or ≥ 0. All filled numbers must be finite. A product that overflows or underflows the JavaScript range is rejected; the example is far inside that range.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Power | Nameplate or measured draw | W |
| Quantity | How many identical units | count |
| Hours per day | Scheduled on-time | h/day |
| Days | Length of the period | day |
| Duty | Fraction of the scheduled hours that are actually loaded | 1 |
| Tariff | Energy price, optional | currency per kWh |

## Engineering Principles

Duty is a multiplier on the schedule, not a second copy of the hours. A fan rated 65 W that is timetabled for 9 hours but loaded only 80% of that timetable uses \(u=0.8\). Leaving the tariff blank still returns energy. Filling 0 as the tariff returns a cost of 0, which is a price, not a missing price.

## Worked Example

Three circulation fans, 65 W each, 9 h/day on the timer, 22 days in the period, duty 0.8, tariff 0.18 USD/kWh.

1. Energy = \(65\times 3\times 9\times 22\times 0.8 / 1000 = 30.888\) kWh.
2. Cost = \(30.888\times 0.18 = 5.55984\) USD.

Boundary: the same schedule with the tariff field left blank returns 30.888 kWh and a null cost. Duty 0 returns 0 kWh. Quantity 0 and days 400 are outside the integer ranges and are rejected.

## Limitations

- One constant wattage. No thermostat cycling beyond the duty factor you type.
- The currency code does not convert money.
- 5.56 USD is this product only. It is not the meter total for the building.

## Reference Standards

No utility tariff schedule is bundled. Status: pending.

## Online Calculator

Enter the three-fan, 22-day case on the production page:

https://powerengineerlab.com/calculators/appliance-electricity-cost/

## Related Formulas

- [Same-interval load factor](interval-load-factor.md)
- [Kilowatt to mechanical horsepower](kilowatt-to-horsepower.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `TOOL-011` |
| Evidence | Production expression `powerW * quantity * hoursPerDay * days * duty / 1000`, cost null when tariff is null |
| Method | Recomputed 65×3×9×22×0.8/1000 |
| Example result | 30.888 kWh, cost 5.55984 |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
