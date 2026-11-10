# Do not feed a divider tap into a winding

Locale: en

## Two circuits that both “make a lower voltage”

A bench supply is 48 V DC. A resistive divider with \(R_1 = 2200\,\Omega\) on top and \(R_2 = 5600\,\Omega\) below, load left empty, produces an open-circuit tap. Elsewhere in the same building, a single-phase transformer has 480 primary turns and 80 secondary turns and a 240 V primary winding. Both conversations use the word “ratio.” The numbers must not cross.

## Divider path

Unloaded, the tool sets the lower arm equal to \(R_2\):

$$
V_{\mathrm{oc}} = 48\times\frac{5600}{7800} = 34.461538\ldots\,\mathrm{V}
$$

$$
I_{\mathrm{in}} = 48/7800 = 0.006153846\ldots\,\mathrm{A}
$$

That current is the current through \(R_1\). It is about 6.15 mA. The page is a DC resistive model. It has no frequency and no kVA.

## Transformer path

Voltage-solve, single-phase, both sides winding-phase. Turns ratio \(t = 480/80 = 6\).

$$
V_2 = 240/6 = 40\,\mathrm{V}
$$

Phase ratio and line ratio are both 6, because there is no \(\sqrt{3}\) step on a single-phase winding. The turns tool stops at voltage. It does not emit current.

If the nameplate is 1.5 kVA and the rated secondary voltage is that same 40 V, the full-load current tool is the next legitimate step, single-phase:

$$
I = \frac{1500}{40} = 37.5\,\mathrm{A}
$$

Power factor is not in that formula. 37.5 A is \(S/V\) at rated apparent power. It is not a short-circuit current and not a cable rating.

## The illegal handoff

34.46 V is not a primary you may type into the turns tool in place of 240 V. Doing that would invent a secondary of \(34.461538/6 \approx 5.74\,\mathrm{V}\) that no winding in this ticket has. The divider’s 6.15 mA is not a check on 37.5 A. They differ by about four orders of magnitude because one is a bleeder and the other is a rated winding. Subtracting them is not a “load.”

The legal handoff is only inside the AC pair: the turns tool’s 40 V, when it is the rated secondary, is the voltage the full-load page divides into. The divider never joins that pair.

## What changes the 40 V, and what does not

Change \(N_2\) from 80 to 40 and \(t\) becomes 12, so \(V_2\) becomes 20 V and the 1.5 kVA current becomes 75 A. Change \(R_2\) on the divider and the tap moves, and the transformer current stays 37.5 A. A wye–delta pair would also split line voltage from phase voltage by \(\sqrt{3}\). This ticket is single-phase so that split is idle, which is why both ratios printed as 6.

## Limits

- Ideal transformer magnitude. No impedance, tap, or loaded voltage drop.
- Divider load was left empty. A parallel load would pull the tap below 34.46 V and still would not be a transformer.
- 37.5 A is not protection, not ampacity, and not the divider current.

## Tools

- Divider: https://powerengineerlab.com/calculators/voltage-divider/
- Turns and voltage: https://powerengineerlab.com/calculators/transformer-ratio/
- Full-load current: https://powerengineerlab.com/calculators/transformer-full-load-current/

The site guide on turns ratio works a 230 V to 23 V example and a 480 V wye–delta example. Those datasets are not this one.

## Online Calculator

The winding voltage is the step that must stay free of the divider:

https://powerengineerlab.com/calculators/transformer-ratio/

## Related Formulas

- [Resistive voltage divider](voltage-divider.md)
- [Ideal transformer turns and voltage ratio](transformer-turns-ratio.md)
- [Transformer full-load current](transformer-full-load-current.md)

## Verification

| Item | Value |
|---|---|
| Source tools | Divider \(V R_2/(R_1+R_2)\); turns \(V_1 N_2/N_1\); full-load \(S/V\) single-phase |
| Evidence | Recomputed from the production expressions recorded for those three calculators. No browser session |
| Dedup scope | Transformer turns guide and the other power guides in the sitemap, read 2026-11-10. Not a web-wide scan |
| Example result | 34.46 V at 6.15 mA beside 40 V and 37.5 A |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |