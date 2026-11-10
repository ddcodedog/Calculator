# Duct friction and local pressure drop

Locale: en

## Direct Answer

The Duct & Airflow Design tool computes cross-section area, mean velocity, Reynolds number, a friction factor, Darcy friction pressure drop, and a \(K\) local loss for one round or rectangular duct section.


## Overview

Production function in the duct-airflow page bundle, fetched 2026-11-04 from https://hvacengineerlab.com/tools/duct-airflow-design/. The page describes the method as continuity, hydraulic diameter, Darcy–Weisbach friction, a Blasius or Haaland-style turbulent factor, and local loss \(K\rho V^{2}/2\).
## Formula

Round duct, diameter \(D\):

$$
A = \frac{\pi D^{2}}{4}, \qquad P = \pi D
$$

Rectangular duct, width \(w\), height \(h\):

$$
A = w h, \qquad P = 2(w+h)
$$

$$
D_h = \frac{4A}{P}, \qquad V = \frac{\dot{V}}{A}, \qquad \mathrm{Re} = \frac{\rho V D_h}{\mu}
$$

Friction factor:

$$
f =
\begin{cases}
64/\mathrm{Re} & \mathrm{Re} < 2300 \\
0.3164\,\mathrm{Re}^{-0.25} & 2300 \le \mathrm{Re} < 10^{5} \\
\dfrac{0.25}{\left[\log_{10}\left(\dfrac{\varepsilon}{3.7 D_h} + \dfrac{5.74}{\mathrm{Re}^{0.9}}\right)\right]^{2}} & \mathrm{Re} \ge 10^{5}
\end{cases}
$$

$$
\Delta p_f = f \frac{L}{D_h} \frac{\rho V^{2}}{2}, \qquad \Delta p_K = K \frac{\rho V^{2}}{2}, \qquad \Delta p = \Delta p_f + \Delta p_K
$$

Defaults when the corresponding field is omitted: \(\varepsilon = 1.5\times 10^{-4}\,\mathrm{m}\) (`15e-5`), \(\rho = 1.2\,\mathrm{kg/m^3}\), \(\mu = 1.81\times 10^{-5}\,\mathrm{Pa\cdot s}\) (`181e-7`), \(K = 0\).

Warnings that do not change the numbers: laminar correlation when \(\mathrm{Re} < 2300\); velocity above 12 m/s; velocity below 2 m/s. The page says the 2–12 m/s band is a screening range, not a cited code limit.

## Variables

| Symbol | Field | Unit | Constraint |
|---|---|---|---|
| \(\dot{V}\) | `airflow_m3_s` | m³/s | \(> 0\) |
| \(D\) or \(w,h\) | `diameter_m` or `width_m`, `height_m` | m | \(> 0\) |
| \(L\) | `length_m` | m | \(> 0\) |
| \(\varepsilon\) | `roughness_m` | m | \(\ge 0\) |
| \(\rho\) | `airDensity_kg_m3` | kg/m³ | \(> 0\) |
| \(\mu\) | `dynamicViscosity_Pa_s` | Pa·s | \(> 0\) |
| \(K\) | `localLossCoefficient` | 1 | \(\ge 0\) |


## Constraints

- \(\dot{V}\): \(> 0\)
- \(D\) or \(w,h\): \(> 0\)
- \(L\): \(> 0\)
- \(\varepsilon\): \(\ge 0\)
- \(\rho\): \(> 0\)
- \(\mu\): \(> 0\)
- \(K\): \(\ge 0\)

## Engineering Principles

Velocity is flow divided by the geometric area of the section the user typed. It is not a recommended design velocity. Hydraulic diameter lets the round-duct Darcy form be reused for a rectangle. The friction-factor split is explicit in the code: laminar \(64/\mathrm{Re}\), Blasius \(0.3164/\mathrm{Re}^{0.25}\) up to \(\mathrm{Re}=10^{5}\), then the Swamee–Jain explicit turbulent formula (the page calls that branch Haaland-style). Local loss uses the same dynamic pressure as the friction term.

## Worked Example

Round duct, \(\dot{V} = 0.5\,\mathrm{m^3/s}\), \(D = 0.3\,\mathrm{m}\), \(L = 20\,\mathrm{m}\), \(K = 0.5\), defaults for roughness, density, and viscosity.

1. \(A = 0.0706858347\ldots\,\mathrm{m^2}\), \(D_h = 0.3\,\mathrm{m}\).
2. \(V = 7.07355303\ldots\,\mathrm{m/s}\).
3. \(\mathrm{Re} = 140689.452\ldots\) so the third branch applies.
4. \(\varepsilon/(3.7 D_h) + 5.74/\mathrm{Re}^{0.9} = 0.00024705\ldots\)
5. \(f = 0.0196064667\ldots\)
6. Dynamic pressure \(\rho V^{2}/2 = 30.02109145\ldots\,\mathrm{Pa}\).
7. \(\Delta p_f = 39.24050196\ldots\,\mathrm{Pa}\), \(\Delta p_K = 15.01054572\ldots\,\mathrm{Pa}\).
8. Total **54.251 Pa**.

Result: velocity **7.074 m/s**, \(f\) **0.01961**, total pressure drop **54.25 Pa**, to the displayed rounding. Status `valid`. Velocity is inside 2–12 m/s, so those warnings are absent. Reynolds number is above 2300, so the laminar warning is absent.

Boundary: \(\dot{V} = 0.005\,\mathrm{m^3/s}\), \(D = 0.50\,\mathrm{m}\), \(L = 10\,\mathrm{m}\), \(K = 0\), defaults.

- \(V = 0.025465\ldots\,\mathrm{m/s}\), \(\mathrm{Re} = 844.14\ldots < 2300\).
- \(f = 64/\mathrm{Re} = 0.075817\ldots\)
- Friction pressure drop \(= 0.000590\,\mathrm{Pa}\). The result is still numeric. Warnings include laminar flow and velocity below 2 m/s.
- Zero or negative airflow, length, or diameter is `invalid` and produces no pressure drop.

## Limitations

- One straight section. No branch fitting schedule beyond a single \(K\).
- Compressible effects and heat gain are ignored. Density and viscosity are constants.
- The laminar formula is still evaluated below Re 2300, with a warning that the correlation is intended for turbulent flow.
- Not a fan selection. The page points at a separate fan tool for duty comparison.

## Reference Standards

**Pending.** The page text names the method and says the screening velocities are not a cited code limit. No standard edition URL was in the calculation closure.

## Online Calculator

https://hvacengineerlab.com/tools/duct-airflow-design/

Inventory tool ID: `duct-airflow-design`. The inventory URL with a trailing slash redirects to this path.

## Related Formulas

- [Darcy-Weisbach major pipe headloss](../WaterEngineerLab/darcy-weisbach-pipe-headloss.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `duct-airflow-design` |
| Evidence | Production bundle: area, \(D_h=4A/P\), Re, the three-way \(f\) expression, and \(\Delta p = (f L/D_h + K)\rho V^2/2\) |
| Method | Python evaluation of the 0.5 m³/s case (turbulent branch) and the 0.005 m³/s, 0.50 m case (laminar branch) |
| Example result | Total pressure drop 54.251 Pa at 0.5 m³/s, 300 mm round, 20 m, \(K=0.5\) |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |