# Data center power usage effectiveness

## Overview

PUE on this page is total facility power divided by IT power. Annual energy multiplies the power reading by 8760 hours when the mode is power, or scales a period reading by 365 over the entered days when the mode is energy.

## Formula

$$
PUE = P_{total} / P_{IT}
$$

Power mode:

$$
E = P \times 8760
$$

Energy mode, with period length in days:

$$
E_{annual} = E_{period} \times 365 / N_{days}
$$

Cost uses the annual energy difference or the IT and facility energies multiplied by the tariff the user types. The breakdown fields (cooling, UPS, lighting, distribution, other) are summed for a check against the non-IT power; they do not replace \(P_{total}\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P_{total}\) | Facility power | kW in the default power mode |
| \(P_{IT}\) | IT power | kW |
| \(N_{days}\) | Period length in energy mode | days |

## Engineering Principles

The 8760 factor is a non-leap year of hours. The script uses it as a constant. A growth percent scales a projected IT load; it is not part of the definition of present PUE.

## Worked Example

Power-mode defaults: total 500 kW, IT 350 kW, tariff 0.12 per kWh.

$$
PUE = 500/350 = 1.428571429
$$

Annual IT energy is \(350 \times 8760 = 3{,}066{,}000\) kWh. Annual facility energy is \(500 \times 8760 = 4{,}380{,}000\) kWh. The non-IT energy is 1,314,000 kWh. At 0.12 per kWh that non-IT energy costs 157,680.

Boundary: IT power of 0 is rejected because PUE divides by it. In energy mode a period of 0 days is rejected.

## Limitations

PUE does not locate the losses. The category kilowatts are a reconciliation aid. The tariff is a user number with no currency conversion.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/pue-data-center-energy-efficiency/

## Related Formulas

- [Data-center sensible cooling airflow](../HVACEngineerLab/data-center-sensible-airflow.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `pue-data-center-energy-efficiency` |
| Evidence | Production `js/engine.js` PUE ratio and 8760 hour factor, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | PUE 1.428571429, facility 4380000 kWh/year, non-IT cost 157680 |
| Boundary | zero IT power is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
