# Outdoor-air ventilation flow

## Overview

The required outdoor-air flow is the larger of a people-plus-area sum and an air-change flow. A separate carbon-dioxide balance is reported and is not part of that maximum.

## Formula

$$
Q_{people} = N q_p
$$

$$
Q_{area} = A q_a
$$

$$
Q_{ach} = ACH \times V / 3600
$$

$$
Q = \max(Q_{people}+Q_{area},\ Q_{ach})
$$

$$
Q_{CO_2} = N\, g / (C_{in}-C_{out}) \times 1000
$$

\(g\) is litres per second per person. The factor 1000 converts that balance into m³/s when the concentrations are in ppm. Indoor concentration must be above outdoor.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(N\) | Occupants | count |
| \(q_p\) | Flow per person | m³/s per person |
| \(q_a\) | Flow per area | m³/s per m² |
| \(V\) | Room volume | m³ |
| \(C\) | CO₂ concentration | ppm |

## Engineering Principles

The script takes the maximum of the two ventilation methods. It does not add the air-change flow on top of the people and area flows. The CO₂ flow is a third result.

## Worked Example

Defaults: 20 people, 200 m², 0.0025 m³/s per person, 0.0003 m³/s per m², 0.5 ACH, volume 600 m³, outdoor CO₂ 420 ppm, indoor target 1000 ppm, generation 0.005 L/s per person.

People flow is 0.05 m³/s. Area flow is 0.06 m³/s. Their sum is 0.11 m³/s. Air-change flow is \(0.5 \times 600 / 3600 = 0.08333333333\) m³/s. Required flow is 0.11 m³/s.

$$
Q_{CO_2} = 20 \times 0.005 / (1000-420) \times 1000 = 0.1724137931\ \text{m}^3/\text{s}
$$

Boundary: if the air-change term is larger than the people-plus-area sum, the maximum selects the air-change term. Equal indoor and outdoor concentrations are rejected.

## Limitations

Rates are user assumptions. The page says to verify the applicable code, occupancy, filtration, and demand-control sequence. No ventilation standard PDF was opened.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/outdoor-air-ventilation-planner/

## Related Formulas

- [Predicted mean vote](pmv-ppd.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `outdoor-air-ventilation-planner` |
| Evidence | Production flow maximum and CO₂ balance, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | required 0.11 m³/s, CO₂ balance 0.1724137931 m³/s |
| Boundary | equal CO₂ concentrations are rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
