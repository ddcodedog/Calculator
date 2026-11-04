# Darcy pipe pressure drop

## Overview

The pipe tool computes velocity, Reynolds number, a friction factor by regime, and Darcy plus local pressure drop. Gravity in the head conversion is 9.80665.

## Formula

$$
V = Q / (\pi D^2/4)
$$

$$
Re = \rho V D / \mu
$$

Laminar, \(Re < 2300\): \(f = 64/Re\).

Transition, \(2300 \le Re < 4000\): log-Re blend from \(64/2300\) to the Swamee–Jain value at \(Re = 4000\).

Turbulent, \(Re \ge 4000\):

$$
f = 0.25 / \log_{10}\!\left(\varepsilon/(3.7D) + 5.74/Re^{0.9}\right)^2
$$

$$
\Delta p_f = f(L/D)(\rho V^2/2),\quad \Delta p_K = K(\rho V^2/2)
$$

$$
h = \Delta p / (9.80665\,\rho)
$$

If temperature is omitted and density and viscosity are also omitted, the script uses the 7 °C row: \(\rho = 999.9\) kg/m³ and \(\mu = 1.4271\times 10^{-3}\) Pa·s. Default roughness is \(1.5\times 10^{-6}\) m.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Flow | m³/s |
| \(D, L\) | Diameter and length | m |
| \(K\) | Local loss coefficient | dimensionless |
| \(\varepsilon\) | Roughness | m |

## Engineering Principles

The transition branch is a blend, and the script’s own warning says it is not the Blasius equation. The velocity warning range does not change \(f\).

## Worked Example

Defaults: 0.005 m³/s, diameter 0.05 m, length 30 m, \(K = 4\), static head 0, temperature left so the 7 °C row applies.

Velocity is 2.546479089 m/s. Reynolds number is 89209.74149, turbulent. Friction factor is 0.01846758679. Friction pressure drop is 35922.63622 Pa. Local pressure drop is 12967.8146 Pa. Total pressure drop is 48890.45082 Pa. Total head is 4.98593713 m.

Boundary: a flow small enough that \(Re < 2300\) uses \(f = 64/Re\) and adds the laminar warning. Zero diameter is rejected.

## Limitations

The 7 °C properties are a pinned screening row. The script says they are not an in-repo IAPWS-95 evaluation. The Anton Paar / IAPWS citation in the page text was not opened.

## Reference Standards

The method string names Swamee–Jain (1976) for turbulent flow and a pinned liquid-water row citing IAPWS 2008. Those papers were not opened. Reference standards are pending. The friction expressions are the ones in `calculatePipeFlow`.

## Online Calculator

https://hvacengineerlab.com/tools/pipe-flow-pressure-drop/

## Related Formulas

- [Chilled-water flow and plant power](chilled-water-flow.md)
- [Duct friction and local pressure drop](duct-friction-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `pipe-flow-pressure-drop` |
| Evidence | Production `calculatePipeFlow`, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | Re 89209.74149, f 0.01846758679, total head 4.98593713 m |
| Boundary | Re below 2300 uses f = 64/Re; zero diameter is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
