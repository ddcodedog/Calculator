# Predicted mean vote

## Overview

PMV is the ISO 7730 Annex D clothing-temperature iteration with external work fixed at zero. PPD is the usual exponential of that PMV. No edition is pinned in the script.

## Formula

Water vapour pressure:

$$
p_a = 10\, RH\, \exp\!\left(16.6536 - 4030.183/(t_a+235)\right)
$$

Metabolic rate is \(M = 58.15\, met\) in W/m². Clothing resistance is \(I_{cl} = 0.155\, clo\). Clothing factor is \(1+1.29 I_{cl}\) when \(I_{cl} \le 0.078\), otherwise \(1.05+0.645 I_{cl}\). The iteration updates clothing temperature for at most 150 steps and stops when successive estimates differ by at most \(1.5\times 10^{-4}\).

$$
PPD = 100 - 95\exp(-0.03353\, PMV^4 - 0.2179\, PMV^2)
$$

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(t_a, t_r\) | Air and mean radiant temperature | °C |
| \(RH\) | Relative humidity | percent |
| \(v\) | Air speed | m/s |
| met, clo | Activity and clothing | met, clo |

## Engineering Principles

External work is not an input. The script sets it to zero. Inputs outside the script’s common range are rejected before the iteration: humidity outside 0–100, air temperature outside 10–30 °C, radiant temperature outside 10–40 °C, met outside 0.8–4, clo outside 0–2, or air speed outside 0–1 m/s.

## Worked Example

Defaults: 24 °C air, 24 °C radiant, 50% RH, 0.1 m/s, 1.2 met, 0.5 clo. The iteration converges.

$$
PMV = -0.2137764882
$$

$$
PPD = 5.947912698\%
$$

The page displays PMV to two decimal places (−0.21) and PPD to one decimal place (5.9%). The category check is “PPD ≤ 10%”.

Boundary: relative humidity 101 is rejected before the iteration. The same default with the iteration forced to its converged clothing temperature is the value above; a non-converged case is what the 150-step cap returns as invalid.

## Limitations

The page says to verify ASHRAE 55 or ISO 7730, adaptive comfort, and local discomfort before design use. This page does not add those checks. The numbers are the script’s iteration, not a table transcribed from a standard.

## Reference Standards

The method text names ISO 7730 Annex D and ASHRAE 55 and says no edition is pinned. Those documents were not opened. Reference standards are pending.

## Online Calculator

https://hvacengineerlab.com/tools/thermal-comfort-pmv-planner/

## Related Formulas

- [Outdoor-air ventilation flow](outdoor-air-ventilation-flow.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `thermal-comfort-pmv-planner` |
| Evidence | Production Annex D iteration with external work 0, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | PMV −0.2137764882, PPD 5.947912698% |
| Boundary | relative humidity 101 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
