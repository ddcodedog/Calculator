# Three readings from one heater shop

## What the shop is asking

Four 1800 W heaters, run 5 hours a day for 14 days, duty 1. The tariff on the energy tool is 0.21 currency units per kWh. Separately, the meter for those same 14 days shows a peak of 6.4 kW, and the nameplate sum is 7.2 kW. Someone will want a single “efficiency.” These tools will not give one.

## Which tool answers which sentence

| Sentence you are allowed to say | Tool | Result here |
|---|---|---|
| The schedule used this much energy, and the tariff turns that into money | Appliance energy | 504 kWh, cost 105.84 |
| Over this meter interval, average demand over peak demand is this fraction | Load factor | 0.234375 |
| The highest demand over the connected nameplate is this fraction | Demand factor | 0.888… |

## Arithmetic

Energy, with duty 1:

$$
E = \frac{1800\times 4\times 5\times 14}{1000} = 504\,\mathrm{kWh}
$$

Cost = \(504\times 0.21 = 105.84\). A blank tariff would leave the cost null and would not change 504.

Load factor uses the **same** 14 days. Hours = \(14\times 24 = 336\). Average demand = \(504/336 = 1.5\,\mathrm{kW}\). With the typed peak of 6.4 kW:

$$
\mathrm{LF} = 1.5/6.4 = 0.234375
$$

That peak has to be the peak inside those 336 hours. A 15-minute peak from a different month is not this definition. If 504 kWh and 6.4 kW could not have occurred together (average above peak), the load-factor tool returns `INTERVAL_BOUNDARY` and no ratio.

Demand factor uses nameplate, not hours:

$$
\mathrm{DF} = 6.4/7.2 = 0.8\overline{8}
$$

A maximum above 7.2 kW is the demand-factor tool’s `BOUNDARY` and produces no ratio. Zero hours never enter that division.

## The product is not a result

\(0.234375\times 0.888\ldots = 0.208\overline{3}\). No page on this site multiplies load factor by demand factor. The 0.21 tariff does not belong in either ratio. 105.84 is money for the typed schedule; it is not a bill, because demand charges and taxes are absent.

A useful check is to move only one input. Cut the daily hours from 5 to 2 and energy falls to 201.6 kWh, average demand to 0.6 kW, and load factor to \(0.6/6.4 = 0.09375\), while demand factor stays \(6.4/7.2\) if the peak and the nameplate did not change. The two ratios move for different reasons. That is the point of keeping them apart.

## Limits

- Heaters are a constant 1800 W in the energy tool. A thermostat that short-cycles needs a duty below 1, typed by you.
- Load factor does not read the energy tool. You copy 504 kWh across.
- Demand factor does not know that four heaters exist. You type 6.4 and 7.2.

## Tools

- Energy and tariff: https://powerengineerlab.com/calculators/appliance-electricity-cost/
- Load factor: https://powerengineerlab.com/calculators/load-factor/
- Demand factor: https://powerengineerlab.com/calculators/demand-factor/

The UPS-versus-runtime guide on the site is a different pair of questions. This note does not size a battery.

## Online Calculator

The ratio that uses the 504 kWh is the load-factor page:

https://powerengineerlab.com/calculators/load-factor/

## Related Formulas

- [Appliance energy over a stated duty](appliance-period-energy-cost.md)
- [Same-interval load factor](interval-load-factor.md)
- [Demand factor from maximum and connected load](maximum-demand-factor.md)

## Verification

| Item | Value |
|---|---|
| Source tools | TOOL-011 energy expression; load factor \(E/h\) over peak; demand factor maximum/connected |
| Evidence | Recomputed from those production expressions. No browser session |
| Dedup scope | Power guides index, including the UPS/runtime and transformer guides, read 2026-11-10. Not a web-wide scan |
| Example result | 504 kWh, load factor 0.234375, demand factor 0.888… |
| Date | 2026-11-10 |
| Status | VERIFIED |
