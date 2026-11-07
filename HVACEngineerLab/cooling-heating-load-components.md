# Cooling and heating load components

## Overview

The cooling and heating load planner adds envelope, solar, people, lights, equipment, ventilation, and infiltration for one zone, then applies a sizing margin. It is a component worksheet. It does not pick a coil, a chiller, or a code-minimum outdoor-air rate.

The component equations are in the production page chunk for `cooling-heating-load-planner` (model TOOL-001-V1.0), read 2026-11-07. Moist-air properties come from the PsychroLib V2.5.0 adapter in the shared chunk: saturation pressure, humidity ratio, enthalpy, and specific volume. EnergyPlus engineering reference 26.1 is named as a cross-check in the tool. That PDF was not re-read.

## Formula

Conduction for a surface with conductance \(U\), area \(A\), and the two temperatures the tool assigns to that surface:

$$
q = UA\,(T_{\mathrm{other}}-T_{\mathrm{in}})
$$

Cooling demand is \(\max(0,q)\). Heating demand is \(\max(0,-q)\). Outdoor surfaces use the outdoor design temperature. Other surfaces use the adjacent-space temperature.

Solar, only when SHGC, design irradiance, and an external shade factor are all present:

$$
q_{\mathrm{solar}} = A\times\mathrm{SHGC}\times G\times f_{\mathrm{shade}}
$$

That term is cooling-only. People, lights, and equipment use the entered watt ratings times diversity or use factor. Lighting is either installed power or a density times floor area, not both. Ventilation is either a volume flow or a dry-air mass flow, not both. Infiltration is either air changes per hour or a volume flow, not both.

$$
\dot{V}_{\mathrm{ACH}} = \frac{\mathrm{ACH}\times V_{\mathrm{zone}}}{3600}
$$

Zone volume is floor area times ceiling height when volume is left blank. Cooling air uses moist specific volume at the outdoor cooling state to turn \(\dot{V}\) into dry-air mass. Heating air uses dry-air specific volume at the outdoor heating temperature and the station pressure. Enthalpy is \(1006\,T + W(2501000+1860\,T)\) in J/kg of dry air, with \(T\) in °C.

Cooling air: total = \(m(h_{\mathrm{out}}-h_{\mathrm{in}})\). If that total is not positive, cooling from that stream is zero. Otherwise sensible is clipped into \([0,\mathrm{total}]\) using \(m(1006+1860\,W_{\mathrm{out}})(T_{\mathrm{out}}-T_{\mathrm{in}})\), and latent is the remainder. Heating air is sensible only:

$$
q_{\mathrm{heat,air}} = \max\left(0,\ -1006\,m\,(T_{\mathrm{out}}-T_{\mathrm{in}})\right)
$$

Sized load = base \(\times(1+\mathrm{margin}/100)\). Margin must sit in 0…30 when it is set. If internal-gain credit is off, heating does not subtract people, lights, or equipment. SHR is cooling sensible divided by the cooling base when the base is positive.

## Variables

The built-in “Example Office Load Study” is the worked case. SI units:

| Input | Value |
|---|---|
| Floor, height | 100 m², 3 m (volume 300 m³) |
| Indoor cooling / heating | 24 °C at 50% RH, 21 °C |
| Outdoor cooling / heating | 35 °C, humidity ratio 0.014 kg/kg; 0 °C |
| Pressure | 101325 Pa |
| Wall, roof, window | 20 m² at U 0.5; 100 m² at U 0.3; 10 m² at U 2, SHGC 0.4, 500 W/m², shade 0.8 |
| People | 10 × 75 W sensible × 55 W latent × diversity 0.8 |
| Lights | 8 W/m² × use 0.9 |
| Equipment | 1000 W sensible and 100 W latent × use 0.8 |
| Ventilation | 0.2 kg/s dry air |
| Infiltration | 0.4 ACH |
| Margin, internal credit | 10%, credit off |

## Engineering Principles

Each component is signed, then clipped into a cooling demand or a heating demand. A warm outdoor surface can be a cooling load and a heating load in the other season without a second U-value. Solar and latent gains do not heat the heating total. The 10% margin is a multiplier on the summed base, not a second copy of any one component.

## Worked Example

Envelope and internal gains, cooling:

| Component | Cooling |
|---|---:|
| Wall \(0.5\times 20\times(35-24)\) | 110 W |
| Roof \(0.3\times 100\times 11\) | 330 W |
| Window conduction \(2\times 10\times 11\) | 220 W |
| Solar \(10\times 0.4\times 500\times 0.8\) | 1600 W |
| People \(10\times 75\times 0.8\), latent \(10\times 55\times 0.8\) | 600 W, 440 W |
| Lights \(8\times 100\times 0.9\) | 720 W |
| Equipment \(1000\times 0.8\), \(100\times 0.8\) | 800 W, 80 W |

Heating conduction is the same surfaces at outdoor 0 °C and indoor 21 °C: wall 210 W, roof 630 W, window 420 W. Solar is not added.

Psychrometric adapter at 101325 Pa: indoor 24 °C, 50% RH gives humidity ratio 0.00929851 kg/kg and enthalpy 47814.6 J/kg. Outdoor cooling enthalpy at 35 °C and \(W=0.014\) is 71135.4 J/kg.

Ventilation at 0.2 kg/s: total \(0.2\times(71135.4-47814.6)=4664.15\,\mathrm{W}\), sensible 2270.49 W, latent 2393.66 W.

Infiltration volume flow = \(300\times 0.4/3600 = 1/30\,\mathrm{m^3/s}\). Moist outdoor volume converts that to 0.0373439 kg/s for cooling: total 870.89 W, sensible 423.94 W, latent 446.94 W. The heating mass from dry-air volume at 0 °C is 0.0430773 kg/s, and \(1006\times 0.0430773\times 21 = 910.05\,\mathrm{W}\). Ventilation heating uses the entered 0.2 kg/s: \(1006\times 0.2\times 21 = 4225.2\,\mathrm{W}\).

Cooling base = 7074.43 W sensible + 3360.61 W latent = 10435.04 W. SHR = 0.6779. With 10% margin, sized cooling = 11478.54 W.

Heating base, credit off = 1260 + 4225.2 + 910.05 = 6395.25 W. Sized heating = 7034.78 W.

Boundary: a margin of 31 is rejected. Supplying both an ACH and an infiltration volume flow is rejected. Solar inputs left incomplete omit the solar term and raise `W_SOLAR_INPUT_INCOMPLETE` instead of inventing an irradiance.

## Limitations

- One zone, steady design temperatures, no schedule beyond the diversity and use factors.
- Heating air ignores latent credit. The tool warns `W_HEATING_AIR_SENSIBLE_ONLY`.
- The adapter is a pinned PsychroLib port. It is not a substitute for a full energy model.
- These watts are the worksheet result for the example inputs, not a measured building load.

## Reference Standards

PsychroLib V2.5.0 equations as copied into the production adapter. EnergyPlus engineering reference 26.1 is cited by the tool and was not re-opened. Status: pending.

## Online Calculator

The office study is the built-in example on the load planner:

https://hvacengineerlab.com/tools/cooling-heating-load-planner

## Related Formulas

- [Psychrometric process between two states](psychrometric-process-states.md)
- [Duct friction and local pressure drop](duct-friction-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab cooling and heating load planner |
| Evidence | Production component functions and the PsychroLib V2.5.0 adapter in the shared chunk |
| Method | Recomputed the built-in office example in Python from those expressions, including ventilation and infiltration |
| Example result | Cooling base 10435.04 W, sized 11478.54 W; heating base 6395.25 W, sized 7034.78 W |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
