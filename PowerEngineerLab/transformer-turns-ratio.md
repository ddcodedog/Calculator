# Ideal transformer turns and voltage ratio

Locale: en

## Direct Answer

The transformer ratio calculator solves either the secondary voltage from a turns ratio, or the turns ratio from two voltages. It uses ideal magnitude only: primary and secondary phase voltages are in the same ratio as the turns. Winding resistance, leakage, taps, and regulation are outside the model.


## Overview

Production chunk for `transformer-ratio`, tool model 1.1.0, read 2026-11-07. The page method line is \(N_1/N_2 = V_{\varphi 1}/V_{\varphi 2}\). A wye winding uses \(V_{\varphi} = V_{LL}/\sqrt{3}\). A delta winding, and any single-phase winding, uses the entered voltage as the phase voltage (https://powerengineerlab.com/calculators/transformer-ratio/).
## Formula

Turns ratio in voltage-solve mode is the positive integer ratio \(t = N_1/N_2\). Phase voltage converts first, then the secondary is written back in the requested line or phase form.

$$
V_{\varphi 2} = \frac{V_{\varphi 1}}{t}
$$

Turns-solve mode inverts that: \(t = V_{\varphi 1}/V_{\varphi 2}\). Turns are an output in that mode, not an input. Display formatting uses two fraction digits; the stored ratio is full precision. Ratios outside \(10^{-12}\)…\(10^{12}\) are rejected.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Primary and secondary voltage | Line-line or winding-phase, as selected | V, kV, or mV (1, 1000, 0.001) |
| Connection | Single-phase, wye, or delta on each side | — |
| Turns \(N_1\), \(N_2\) | Positive integers in voltage-solve mode | count |
| Mode | `solve-voltage-ratio` or `solve-turns-ratio` | — |

## Engineering Principles

The ratio the tool calls “turns ratio” is a phase-voltage ratio. On a wye–wye or delta–delta pair the line-line ratio equals that same number. On a wye–delta pair it does not, because one side divides by \(\sqrt{3}\) and the other does not. The calculator reports both ratios so those two numbers are not mixed up.

## Worked Example

Page default. Single-phase, both sides winding-phase, solve voltage, \(V_1 = 230\,\mathrm{V}\), \(N_1 = 100\), \(N_2 = 10\).

1. \(t = 100/10 = 10\).
2. \(V_2 = 230/10 = 23\,\mathrm{V}\).
3. Phase ratio and line ratio are both 10, because a single-phase winding has no \(\sqrt{3}\) step.

Second case, same turns, three-phase, primary wye line-line 480 V, secondary delta line-line.

1. \(V_{\varphi 1} = 480/\sqrt{3} = 277.128129\,\mathrm{V}\).
2. \(V_{\varphi 2} = 277.128129/10 = 27.712813\,\mathrm{V}\).
3. Delta line voltage equals phase voltage, so \(V_{LL2} = 27.712813\,\mathrm{V}\).
4. Line-voltage ratio = \(480/27.712813 = 10\sqrt{3} = 17.320508\). Phase-voltage ratio stays 10.

Boundary: a turns value of 0 is rejected. Average demand is not computed here; that is a different tool.

## Limitations

- Ideal magnitude. No phase shift, impedance, tap, or voltage drop under load.
- Does not replace the full-load current page, which uses rated kVA rather than turns.
- Two fraction digits on screen are formatting. \(10\sqrt{3}\) is not exactly 17.32.

## Reference Standards

The chunk cites OpenStax University Physics Volume 2, section 13.1, accessed 2026-10-14, as the ideal-transformer statement. That page was not re-read for this note. Status: pending.
## Online Calculator

The 230 V, 100:10 case is the voltage-solve default:

https://powerengineerlab.com/calculators/transformer-ratio/

## Related Formulas

- [Transformer full-load current](transformer-full-load-current.md)
- [Same-interval load factor](interval-load-factor.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `transformer-ratio` |
| Evidence | Production calculator chunk, phase-voltage conversion and \(V_{\varphi 2}=V_{\varphi 1}/t\) |
| Method | Recomputed the single-phase default and a 480 V wye to delta case with the same turns |
| Example result | 23 V at turns ratio 10; wye–delta line ratio \(10\sqrt{3}\) |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |