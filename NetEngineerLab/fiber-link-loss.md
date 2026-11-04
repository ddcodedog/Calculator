# Fiber link loss

## Overview

The Fiber Loss Calculator sums attenuation of the fiber span with discrete losses from splices, connectors, splitter stages, and other passive components. It then adds a user-entered engineering margin and compares that design loss with an available power budget and with the estimated receive level versus a receive threshold.

This page documents the production engine at `https://netengineerlab.com/tools/fiber-loss/js/engine.js` (`NELFiberLossEngine`, fetched 2026-11-04). The separate public repository `ddcodedog/fiber-loss-calculator` is a different static page and is not the source of these equations.

## Formula

Fiber, splice, and connector contributions:

$$
L_{\mathrm{fiber}} = d \, \alpha
$$

$$
L_{\mathrm{splice}} = N_{\mathrm{s}} \, \ell_{\mathrm{s}}, \qquad L_{\mathrm{conn}} = N_{\mathrm{c}} \, \ell_{\mathrm{c}}
$$

$$
L_{\mathrm{split+other}} = L_{\mathrm{s1}} + L_{\mathrm{s2}} + L_{\mathrm{other}}
$$

$$
L_{\mathrm{physical}} = L_{\mathrm{fiber}} + L_{\mathrm{splice}} + L_{\mathrm{conn}} + L_{\mathrm{split+other}}
$$

$$
L_{\mathrm{design}} = L_{\mathrm{physical}} + M
$$

$$
B_{\mathrm{rem}} = B_{\mathrm{avail}} - L_{\mathrm{design}}, \qquad P_{\mathrm{rx}} = P_{\mathrm{tx}} - L_{\mathrm{physical}}, \qquad M_{\mathrm{rx}} = P_{\mathrm{rx}} - P_{\mathrm{th}}
$$

Values with absolute value at most \(10^{-9}\,\mathrm{dB}\) are treated as zero. Status is `failed` if \(B_{\mathrm{rem}} < 0\) or \(M_{\mathrm{rx}} < 0\); otherwise `warning` if either margin is below \(3\,\mathrm{dB}\); otherwise `healthy`.

## Variables

| Symbol | Name in the engine | Unit | Constraint |
|---|---|---|---|
| \(d\) | `distance` | km | finite, \(\ge 0\) |
| \(\alpha\) | `attenuation` | dB/km | finite, \(\ge 0\) |
| \(N_{\mathrm{s}}\), \(N_{\mathrm{c}}\) | `spliceCount`, `connectorCount` | count | safe integers, \(\ge 0\) |
| \(\ell_{\mathrm{s}}\), \(\ell_{\mathrm{c}}\) | `spliceLoss`, `connectorLoss` | dB | finite, \(\ge 0\) |
| \(L_{\mathrm{s1}}\), \(L_{\mathrm{s2}}\) | `splitter1`, `splitter2` | dB | finite, \(\ge 0\) |
| \(L_{\mathrm{other}}\) | `otherLoss` | dB | finite, \(\ge 0\) |
| \(M\) | `engineeringMargin` | dB | finite, \(\ge 0\) |
| \(B_{\mathrm{avail}}\) | `availableBudget` | dB | finite, \(\ge 0\) |
| \(P_{\mathrm{tx}}\) | `txPower` | dBm | finite |
| \(P_{\mathrm{th}}\) | `rxThreshold` | dBm | finite |

## Engineering Principles

Attenuation in dB adds along a passive single-span path. The engine does not convert wavelength into \(\alpha\); the user (or a preset in the page) supplies dB/km. Splitter loss is an entered insertion loss, not \(10\log_{10}(N)\) computed inside this engine. The \(3\,\mathrm{dB}\) warning band is a planning rule in this calculator, not a pass/fail limit taken from a cited standard.

## Worked Example

Inputs matching the production page’s “10 km PON feeder” case, plus the budget and power fields the engine requires:

| Input | Value |
|---|---|
| Distance, attenuation | 10 km, 0.25 dB/km |
| Splices | 6 × 0.10 dB |
| Connectors | 4 × 0.30 dB |
| Splitter 1 / splitter 2 / other | 21.0 / 0 / 0 dB |
| Engineering margin | 3 dB |
| Available budget, transmit power, receive threshold | 32 dB, 3 dBm, −27 dBm |

Steps:

1. \(L_{\mathrm{fiber}} = 10 \times 0.25 = 2.50\,\mathrm{dB}\).
2. \(L_{\mathrm{splice}} = 0.60\,\mathrm{dB}\), \(L_{\mathrm{conn}} = 1.20\,\mathrm{dB}\), splitter and other \(= 21.00\,\mathrm{dB}\).
3. \(L_{\mathrm{physical}} = 25.30\,\mathrm{dB}\).
4. \(L_{\mathrm{design}} = 28.30\,\mathrm{dB}\).
5. \(B_{\mathrm{rem}} = 32 - 28.30 = 3.70\,\mathrm{dB}\).
6. \(P_{\mathrm{rx}} = 3 - 25.30 = -22.30\,\mathrm{dBm}\), \(M_{\mathrm{rx}} = -22.30 - (-27) = 4.70\,\mathrm{dB}\).

Result: physical loss **25.30 dB**, design loss **28.30 dB**, status **healthy**. The engine keeps IEEE-754 doubles; these inputs are exact in decimal tenths, so two-decimal dB figures match the engine.

Boundary: same passive losses with available budget \(28\,\mathrm{dB}\) gives \(B_{\mathrm{rem}} = -0.30\,\mathrm{dB}\) and status **failed**. Distance \(0\,\mathrm{km}\) drops only the fiber term (\(L_{\mathrm{physical}} = 22.80\,\mathrm{dB}\)).

## Limitations

- One attenuation coefficient for the whole length. No splice-map, bidirectional, or dual-wavelength calculation.
- Connector count is a user integer. The tool does not decide whether a mated pair is one or two “connectors.”
- No reflection, PMD, or dispersion penalty in this engine.
- A healthy flag is not an acceptance test.

## Reference Standards

The production page links these recommendations and states how the tool uses them. This library did not re-audit the recommendation text.

- ITU-T G.652: https://www.itu.int/rec/T-REC-G.652/en
- ITU-T G.984.2: https://www.itu.int/rec/T-REC-G.984.2/en
- ITU-T G.671: https://www.itu.int/rec/T-REC-G.671/en
- IEEE 802.3: https://standards.ieee.org/ieee/802.3/10422/
- IEC 61280-4-2:2024: https://webstore.iec.ch/en/publication/77134

## Online Calculator

https://netengineerlab.com/tools/fiber-loss/

Inventory tool ID: `fiber-loss`.

## Related Formulas

- [Optical power budget](optical-power-budget.md)
- [Chromatic dispersion](chromatic-dispersion.md)
- [Fiber propagation latency](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `fiber-loss` |
| Evidence | Production `tools/fiber-loss/js/engine.js` `calculate`, fetched 2026-11-04. Inventory local path `D:\NetEngineerLab-V173-GitHub\...` was not on this machine. |
| Method | Reimplemented the sums in Python and compared with the page’s 10 km worked case (25.30 dB physical, 28.30 dB design). |
| Example result | 25.30 dB physical, 28.30 dB design, healthy for the full input set above |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
