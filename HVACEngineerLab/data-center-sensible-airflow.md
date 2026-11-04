# Data-center sensible cooling airflow

## Overview

Sensible airflow is the IT load divided by 1006 times the supply temperature rise, then divided by density. Plant input is the heat rejected at the air handler divided by COP.

## Formula

$$
Q_{heat} = Q_{IT} / SHF
$$

$$
\dot m = Q_{IT} / (1006\, \Delta T)
$$

$$
\dot V = \dot m / \rho
$$

$$
P_{cool} = Q_{heat} / COP
$$

$$
E_{IT} = (Q_{IT}/1000)\, t\, LF
$$

$$
V_{water} = WUE \times E_{IT}
$$

Latent heat is \(Q_{heat}-Q_{IT}\) and is not part of the airflow. Facility power for a PUE display is \(Q_{IT}\times PUE\). Required units are the ceiling of \(Q_{heat}\) over the unit capacity.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q_{IT}\) | IT load | W |
| \(SHF\) | Sensible heat fraction | fraction |
| \(\Delta T\) | Supply-air temperature rise | K |
| \(\rho\) | Air density | kg/m³ |
| \(WUE\) | Water use | L per IT kWh |

## Engineering Principles

The specific heat 1006 J/(kg·K) is the literal in the script. With SHF = 1 the airflow is sized on the whole IT load and latent heat is zero.

## Worked Example

Defaults: IT 1,000,000 W, PUE 1.4, WUE 1.2 L/kWh, SHF 1, three units of 500,000 W, supply rise 10 K, density 1.2 kg/m³, plant COP 5, 8760 h, load factor 0.5.

$$
\dot m = 10^6 / (1006 \times 10) = 99.40357853\ \text{kg/s}
$$

$$
\dot V = 99.40357853 / 1.2 = 82.83631544\ \text{m}^3/\text{s}
$$

Plant input is \(10^6 / 5 = 200000\) W. Annual IT energy is \(1000 \times 8760 \times 0.5 = 4{,}380{,}000\) kWh. Annual water is \(1.2 \times 4380000 = 5{,}256{,}000\) L. Required units are \(\lceil 10^6 / 5\times 10^5 \rceil = 2\). Three installed units meet an N+1 check of required-plus-one.

Boundary: SHF below 1 raises total heat and the unit count, and it does not change the airflow, which stays on \(Q_{IT}\). A supply rise of 0 is rejected.

## Limitations

The airflow is a sensible screening balance. It is not a containment CFD result. PUE and WUE are inputs, not outputs, except for the facility-power and water products.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/data-center-cooling-planner/

## Related Formulas

- [Data center power usage effectiveness](../NetEngineerLab/data-center-pue.md)
- [Chilled-water flow and plant power](chilled-water-flow.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `data-center-cooling-planner` |
| Evidence | Production sensible-airflow function, cp = 1006, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 99.40357853 kg/s and 82.83631544 m³/s; plant 200 kW |
| Boundary | zero temperature rise is rejected; SHF changes heat and unit count, not airflow |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
