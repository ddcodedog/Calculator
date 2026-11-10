# Psychrometric process between two states

Locale: en

## Direct Answer

The psychrometric process analyzer builds two moist-air states, subtracts them, and, if you enter a dry-air mass flow, turns the enthalpy change into watts. Positive \(\Delta h\) means the leaving state carries more energy per kilogram of dry air. Negative \(\Delta h\) means it carries less. The page text says to treat that as a direction check before coil selection, not as a selected coil.


## Overview

State properties and the delta are in the production page chunk, read 2026-11-07. Each state takes dry-bulb temperature and exactly one moisture input (relative humidity or humidity ratio) and exactly one pressure input (pascal or elevation). The default screen is relative humidity at a typed pressure (https://hvacengineerlab.com/tools/psychrometric-process-analyzer).
## Formula

Saturation vapor pressure uses the adapter’s two exponential fits, with \(T\) in kelvin. At \(t \le 0.01\,^\circ\mathrm{C}\):

$$
\ln p_{ws} = -\frac{5674.5359}{T}+6.3925247-0.009677843\,T+6.2215701\times 10^{-7}T^{2}+2.0747825\times 10^{-9}T^{3}-9.484024\times 10^{-13}T^{4}+4.1635019\ln T
$$

Above \(0.01\,^\circ\mathrm{C}\):

$$
\ln p_{ws} = -\frac{5800.2206}{T}+1.3914993-0.048640239\,T+4.1764768\times 10^{-5}T^{2}-1.4452093\times 10^{-8}T^{3}+6.5459673\ln T
$$

Humidity ratio from relative humidity \(\phi\) (0…1) and total pressure \(p\):

$$
W = \max\left(10^{-7},\ 0.621945\,\frac{\phi\,p_{ws}}{p-\phi\,p_{ws}}\right)
$$

Enthalpy, J per kg of dry air, and moist volume, m³ per kg of dry air:

$$
h = 1006\,t + \max(W,10^{-7})\,(2501000+1860\,t)
$$

$$
v = \frac{287.042\,(t+273.15)\,(1+1.607858\max(W,10^{-7}))}{p}
$$

Process deltas are leaving minus entering: \(\Delta t\), \(\Delta W\), \(\Delta h\). With dry-air mass flow \(m \ge 0\):

$$
q_{\mathrm{total}} = m\,\Delta h, \qquad q_{\mathrm{sensible}} = m\,(1006+1860\,W_{\mathrm{leave}})\,\Delta t, \qquad q_{\mathrm{latent}} = q_{\mathrm{total}}-q_{\mathrm{sensible}}
$$

A blank mass-flow field omits the watt split. A negative mass flow is `E_MASS_FLOW`.

## Variables

| Name | Default on the page | Unit |
|---|---|---|
| Entering dry bulb, RH | 24, 50 | °C, % |
| Leaving dry bulb, RH | 14, 90 | °C, % |
| Pressure | 101325 | Pa |
| Dry-air mass flow | blank | kg/s |

The humidity-ratio boxes (0.0093 and 0.00896) are the other moisture mode. They are not used while the control is set to relative humidity.

## Engineering Principles

Both states share one pressure and one moisture method. The delta is only the difference of two endpoint states. It does not model coil bypass, condensate temperature, or a mixed-air fraction. Sensible watts use the leaving humidity ratio, which is the same split the load planner uses for a cooling airstream.

## Worked Example

Defaults: 24 °C at 50% RH to 14 °C at 90% RH, 101325 Pa, mass flow left blank.

Entering state:

1. \(p_{ws}(24\,^\circ\mathrm{C}) = 2985.127\,\mathrm{Pa}\).
2. \(W = 0.00929851\,\mathrm{kg/kg}\).
3. \(h = 47814.6\,\mathrm{J/kg}\). Specific volume \(0.854377\,\mathrm{m^3/kg}\).

Leaving state:

1. \(p_{ws}(14\,^\circ\mathrm{C}) = 1598.669\,\mathrm{Pa}\).
2. \(W = 0.00895875\,\mathrm{kg/kg}\).
3. \(h = 36723.1\,\mathrm{J/kg}\).

Deltas: \(\Delta t = -10\,\mathrm{K}\), \(\Delta W = -0.00033975\,\mathrm{kg/kg}\), \(\Delta h = -11091.5\,\mathrm{J/kg}\). The blank flow field stops here. The negative enthalpy change is the cooling/drying direction the page describes.

If the optional flow is set to 0.5 kg/s:

1. Total = \(0.5\times(-11091.5) = -5545.76\,\mathrm{W}\).
2. Sensible = \(0.5\times(1006+1860\times 0.00895875)\times(-10) = -5113.32\,\mathrm{W}\).
3. Latent = \(-5545.76-(-5113.32) = -432.44\,\mathrm{W}\).

Boundary: relative humidity outside 0…100 is rejected. Entering both a humidity ratio and a relative humidity is rejected. Vapor pressure at or above the total pressure throws rather than returning a state.

## Limitations

- Endpoint difference only. Bypass factor and part-load coil behavior are called out on the page as a separate review.
- IP labels (°F, Btu/lb, ft³/lb, psi) are display conversions of the SI result.
- A negative watt is a direction, not a catalog capacity.

## Reference Standards

Coefficients are the production adapter’s PsychroLib V2.5.0 port. The upstream library note and any ASHRAE psychrometric chapter were not re-read. Status: pending.
## Online Calculator

The entering and leaving defaults are already filled on the process analyzer:

https://hvacengineerlab.com/tools/psychrometric-process-analyzer

## Related Formulas

- [Cooling and heating load components](cooling-heating-load-components.md)
- [Duct friction and local pressure drop](duct-friction-pressure-drop.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab psychrometric process analyzer |
| Evidence | Production state function, saturation-pressure fits, and \(m\Delta h\) duty split |
| Method | Recomputed both default states and the 0.5 kg/s optional duty in Python |
| Example result | \(\Delta h = -11091.5\,\mathrm{J/kg}\); at 0.5 kg/s, total −5545.76 W |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |