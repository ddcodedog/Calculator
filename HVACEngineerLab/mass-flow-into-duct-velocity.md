# The coil’s volume flow can enter the duct tool. Its watts cannot.

Locale: en

## Decision

A supply stream is specified as dry-air mass flow. The duct tool wants cubic metres per second. The load planner also speaks in watts. Only one of those can be typed into the duct diameter field’s partner, the airflow box, and it is the volume flow.

## Dataset that is not the office example

Entering air at the psychrometric tool: 26 °C, 40% RH, 101325 Pa. Dry-air mass flow 0.15 kg/s. The duct that carries the same stream at that entering state: round, diameter 0.16 m, length 9 m, local \(K = 0.3\), roughness, density, and viscosity left at the duct defaults (\(1.5\times 10^{-4}\) m, 1.2 kg/m³, \(1.81\times 10^{-5}\) Pa·s).

A separate conduction check, not a duct input: one wall, \(U = 0.35\,\mathrm{W/(m^2\cdot K)}\), area 42 m², indoor 23 °C, outdoor 31 °C for cooling and −5 °C for heating with indoor 20 °C.

## Mass flow to cubic metres per second

The psychrometric adapter at 26 °C and 40% RH gives saturation pressure 3363.13 Pa, humidity ratio 0.00836843 kg/kg, enthalpy 47490.1 J/kg, and moist volume 0.858860 m³ per kg of dry air. The volume flow you may hand to the duct tool is

$$
\dot{V} = 0.15\times 0.858860 = 0.128829\,\mathrm{m^3/s}
$$

That uses the entering moist volume. The leaving state is a different density. This note does not average them.

## Duct result at that flow

Area = \(\pi\times 0.16^{2}/4 = 0.020106\,\mathrm{m^2}\). Velocity = \(0.128829/0.020106 = 6.407\,\mathrm{m/s}\), inside the page’s 2–12 m/s screening band. Reynolds number = \(6.797\times 10^{4}\), so the Blasius branch applies:

$$
f = 0.3164\times\mathrm{Re}^{-0.25} = 0.019596
$$

Dynamic pressure \(\rho V^{2}/2 = 24.633\,\mathrm{Pa}\). Friction drop = \(f (L/D)\) times that pressure = 27.152 Pa. Local drop = \(0.3\times 24.633 = 7.390\,\mathrm{Pa}\). Total **34.542 Pa**.

## Watts that stay on their own page

Wall cooling = \(0.35\times 42\times(31-23) = 117.6\,\mathrm{W}\). Wall heating = \(0.35\times 42\times(20-(-5)) = 367.5\,\mathrm{W}\). Those watts are not pascals and they are not cubic metres per second. Adding 117.6 to 34.542 produces a number with no unit the duct page will accept.

The psychrometric enthalpy can also be turned into watts by multiplying a mass flow by an enthalpy change. That product is still watts. It joins the 117.6 W only after you have defined the process. It never joins the 34.542 Pa.

## Sensitivity

Raise the duct diameter to 0.25 m and the same 0.128829 m³/s slows down and the pressure drop falls, while 117.6 W does not move. Raise \(U\) and the watts move, while 34.542 Pa does not. The handoff is one-directional: moist volume times dry-air mass flow, at a stated state, becomes `airflow_m3_s`.

## Limits

- Density in the duct tool is the default 1.2 kg/m³, not the reciprocal of the moist volume. Velocity uses the typed cubic metres per second and the geometric area. The small inconsistency between 1.2 and the psychrometric density is left visible on purpose; the duct page will not import 0.858860.
- One straight section, one \(K\).
- The wall is a single \(UA\Delta T\). It is not the full load planner’s office study, and solar, people, and ventilation enthalpy are not in the 117.6 W.

## Tools

- State and specific volume: https://hvacengineerlab.com/tools/psychrometric-process-analyzer
- Duct pressure: https://hvacengineerlab.com/tools/duct-airflow-design/
- Component loads, if the wall grows into a zone: https://hvacengineerlab.com/tools/cooling-heating-load-planner

## Online Calculator

Type 0.128829 m³/s into the duct page with the 0.16 m section:

https://hvacengineerlab.com/tools/duct-airflow-design/

## Related Formulas

- [Psychrometric process between two states](psychrometric-process-states.md)
- [Duct friction and local pressure drop](duct-friction-pressure-drop.md)
- [Cooling and heating load components](cooling-heating-load-components.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Psychrometric \(p_{ws}\), \(W\), \(v\); duct area, Blasius \(f\), Darcy pressure |
| Evidence | Python replay of the published production formulas. \(p_{ws}(24^\circ\mathrm{C})\) still matches the known 2985.127 Pa anchor. No browser session |
| Dedup scope | HVAC sitemap has tools and a “why” page, no separate duct-plus-psychrometric guide. Repo single-tool notes were not copied. Not a web-wide scan |
| Example result | 0.128829 m³/s → 6.407 m/s and 34.542 Pa; wall stays 117.6 W |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |