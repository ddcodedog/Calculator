# A positive latent term is not condensate

## Read the sign before naming a drain

Air enters at 26 °C and 40% RH and leaves at 18 °C and 70% RH, both at 101325 Pa, with 0.15 kg/s of dry air. Dry-bulb temperature falls. That feels like a cooling coil. The latent watt from the psychrometric split does not agree, and the sign is the result that matters.

## States

Entering: \(p_{ws} = 3363.13\,\mathrm{Pa}\), \(W = 0.00836843\,\mathrm{kg/kg}\), \(h = 47490.1\,\mathrm{J/kg}\).

Leaving: \(p_{ws} = 2064.29\,\mathrm{Pa}\), \(W = 0.00899793\,\mathrm{kg/kg}\), \(h = 40913.1\,\mathrm{J/kg}\).

$$
\Delta t = -8\,\mathrm{K}, \qquad \Delta W = +0.00062950\,\mathrm{kg/kg}, \qquad \Delta h = -6577.07\,\mathrm{J/kg}
$$

Humidity ratio went **up**. The air is cooler and wetter.

## Watt split at 0.15 kg/s

The tool’s split, which uses leaving humidity in the sensible term:

$$
q_{\mathrm{total}} = 0.15\times(-6577.07) = -986.56\,\mathrm{W}
$$

$$
q_{\mathrm{sensible}} = 0.15\times(1006+1860\times 0.00899793)\times(-8) = -1227.28\,\mathrm{W}
$$

$$
q_{\mathrm{latent}} = -986.56 - (-1227.28) = +240.72\,\mathrm{W}
$$

Negative total and negative sensible mean the dry air lost enthalpy and lost sensible heat. Positive latent means the moisture term went the other way: water was added in this endpoint difference, or at least the humidity ratio rose. A condensate drain is a story about water leaving the air. This pair of states does not support that story.

Moisture added, if you treat \(\Delta W\) as a steady stream and not as coil blow-off, is

$$
0.15\times 0.00062950 = 9.4425\times 10^{-5}\,\mathrm{kg/s}
$$

about 0.340 kg/h of water **into** the air. Do not drop that into a condensate volume as a positive drain. The live condensate planner is a different tool and expects a latent **removal**. This note does not call it.

## What would flip the sign

The page default, 24 °C at 50% RH down to 14 °C at 90% RH, dries the air and produces a negative latent watt in the single-tool note. Same equations, opposite moisture direction. The decision is the sign of \(\Delta W\), not the fact that dry bulb fell by 8 K.

A blank mass-flow field would stop after \(\Delta h\) and would not invent ±240.72 W. A negative mass flow is rejected.

## These watts are not the duct pressure

The entering volume flow \(0.15\times 0.858860 = 0.128829\,\mathrm{m^3/s}\) can be typed into the duct tool. The −986.56 W cannot. The duct page returns pascals. Adding a pascal result to −986.56 is the same class of mistake as treating +240.72 W as a drain.

## Limits

- Two endpoint states. No coil bypass, no apparatus dew point, no claim that a real coil produced 70% RH.
- The exponential \(p_{ws}\) fits are the adapter’s, not a new curve.
- No code compliance and no sizing of a trap.

## Tools

- Process states: https://hvacengineerlab.com/tools/psychrometric-process-analyzer
- Duct, only after you convert mass flow to m³/s: https://hvacengineerlab.com/tools/duct-airflow-design/
- Load components, if this stream is one term in a zone: https://hvacengineerlab.com/tools/cooling-heating-load-planner

## Online Calculator

Run 26 °C / 40% RH to 18 °C / 70% RH with 0.15 kg/s:

https://hvacengineerlab.com/tools/psychrometric-process-analyzer

## Related Formulas

- [Psychrometric process between two states](psychrometric-process-states.md)
- [Cooling and heating load components](cooling-heating-load-components.md)

## Verification

| Item | Value |
|---|---|
| Source tool | Psychrometric process analyzer production formulas |
| Evidence | Python replay. Entering \(p_{ws}\) uses the same fit that returns 2985.127 Pa at 24 °C. No browser session |
| Dedup scope | HVAC tool list and the “why” page; the default 24 °C to 14 °C example was not reused. Not a web-wide scan |
| Example result | \(\Delta W > 0\), latent +240.72 W, not a condensate rate |
| Date | 2026-11-10 |
| Status | VERIFIED |
