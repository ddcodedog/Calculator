# Chilled-water flow and plant power

## Overview

Flow is cooling load divided by 4180, density, and the water temperature rise. The page then runs the shared pipe solver and the pump power function.

## Formula

$$
\dot V = Q / (4180\, \rho\, \Delta T)
$$

Pipe friction uses the same Darcy function as the pipe-flow page, with the density and viscosity entered here and the default roughness \(1.5\times 10^{-6}\) m. Pump head is static head plus major and minor heads. Hydraulic power is \(9.80665\,\rho\,\dot V\, H\). Plant electrical power is \(Q/COP\).

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Cooling load | W |
| \(\rho\) | Density | kg/m³ |
| \(\Delta T\) | Water rise | K |
| \(D, L, K\) | Diameter, length, local loss | m, m, dimensionless |

## Engineering Principles

Specific heat 4180 J/(kg·K) is fixed. Because density and viscosity are both supplied, the 7 °C water table is not substituted.

## Worked Example

Defaults: 100000 W, rise 5 K, diameter 0.1 m, length 50 m, \(K = 8\), static head 10 m, density 998 kg/m³, viscosity 0.001002 Pa·s, pump efficiency 0.72, motor efficiency 0.9, COP 5.5.

$$
\dot V = 100000/(4180\times 998\times 5) = 0.00479427755\ \text{m}^3/\text{s} = 4.79427755\ \text{L/s}
$$

Velocity is 0.6104263765 m/s. Reynolds number is 60798.95447, so the regime is turbulent. Swamee–Jain friction factor is 0.01994460717. Major pressure drop is 1854.225798 Pa (0.1894573255 m). Minor pressure drop is 1487.500482 Pa (0.1519868094 m).

$$
H = 10 + 0.1894573255 + 0.1519868094 = 10.34144413\ \text{m}
$$

Hydraulic power is 485.2388666 W. Shaft-side input is \(485.2388666/(0.72\times 0.9) = 748.8254115\) W. Plant input is \(100000/5.5 = 18181.81818\) W.

Boundary: a temperature rise of 0 is rejected. The velocity is below the 2.5 m/s warning threshold in the pipe helper.

## Limitations

The earlier rounded phrase “about 4.78 L/s” on the page is not the value of this division. The worked numbers are the script. Roughness is the shared default, not an entered field on this form.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/chilled-water-system-planner/

## Related Formulas

- [Darcy pipe pressure drop](pipe-darcy-pressure-drop.md)
- [Pump head and hydraulic power](pump-tdh-hydraulic-power.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `chilled-water-system-planner` |
| Evidence | Production flow division and shared `calculatePipeFlow`, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 4.79427755 L/s, head 10.34144413 m, plant 18181.81818 W |
| Boundary | zero water temperature rise is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
