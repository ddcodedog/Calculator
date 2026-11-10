# Optical link power budget

## Overview

The Optical Power Budget Calculator builds a link budget from minimum transmit power and receiver sensitivity, subtracts a path penalty, then subtracts fiber, splice, connector, three splitter entries, other passive loss, and an engineering margin. It also checks the maximum transmit power against receiver overload after the same physical loss.

Engine: `https://netengineerlab.com/tools/optical-power-budget/js/engine.js` (`NELOpticalPowerBudgetEngine`), fetched 2026-11-04.

## Formula

$$
B_{\mathrm{raw}} = P_{\mathrm{tx,min}} - P_{\mathrm{sens}}
$$

$$
B_{\mathrm{std}} = B_{\mathrm{raw}} - P_{\mathrm{pen}}
$$

$$
L_{\mathrm{fiber}} = d \, \alpha, \quad L_{\mathrm{splice}} = N_{\mathrm{s}}\ell_{\mathrm{s}}, \quad L_{\mathrm{conn}} = N_{\mathrm{c}}\ell_{\mathrm{c}}
$$

$$
L_{\mathrm{split}} = L_1 + L_2 + L_3, \quad L_{\mathrm{fixed}} = L_{\mathrm{splice}} + L_{\mathrm{conn}} + L_{\mathrm{split}} + L_{\mathrm{other}}
$$

$$
L_{\mathrm{physical}} = L_{\mathrm{fiber}} + L_{\mathrm{fixed}}, \quad L_{\mathrm{design}} = L_{\mathrm{physical}} + M
$$

$$
B_{\mathrm{rem}} = B_{\mathrm{std}} - L_{\mathrm{design}}
$$

$$
P_{\mathrm{rx}} = P_{\mathrm{tx,min}} - L_{\mathrm{physical}}, \quad P_{\mathrm{rx,max}} = P_{\mathrm{tx,max}} - L_{\mathrm{physical}}
$$

$$
M_{\mathrm{sens}} = P_{\mathrm{rx}} - P_{\mathrm{sens}}, \quad M_{\mathrm{over}} = P_{\mathrm{over}} - P_{\mathrm{rx,max}}
$$

$$
d_{\max} = \max\left(0,\ \frac{B_{\mathrm{std}} - M - L_{\mathrm{fixed}}}{\alpha}\right)
$$

Near-zero margins (\(\le 10^{-9}\,\mathrm{dB}\)) become 0. Status is `failed` if any of \(B_{\mathrm{rem}}\), \(M_{\mathrm{sens}}\), \(M_{\mathrm{over}}\) is negative; otherwise `warning` if any is below \(3\,\mathrm{dB}\); otherwise `healthy`. Usage percent is \(100 \times L_{\mathrm{design}} / B_{\mathrm{std}}\) when \(B_{\mathrm{std}} > 0\).

## Variables

| Symbol | Engine field | Unit | Constraint |
|---|---|---|---|
| \(P_{\mathrm{tx,min}}\), \(P_{\mathrm{tx,max}}\) | `tx`, `txMax` | dBm | finite, \(P_{\mathrm{tx,min}} \le P_{\mathrm{tx,max}}\) |
| \(P_{\mathrm{sens}}\), \(P_{\mathrm{over}}\) | `sens`, `over` | dBm | finite, \(P_{\mathrm{sens}} < P_{\mathrm{over}}\) |
| \(P_{\mathrm{pen}}\) | `penalty` | dB | \(\ge 0\) |
| \(d\), \(\alpha\) | `d`, `a` | km, dB/km | \(d \ge 0\), \(\alpha > 0\) |
| \(N_{\mathrm{s}}\), \(\ell_{\mathrm{s}}\) | `sc`, `sl` | count, dB | count is a safe integer |
| \(N_{\mathrm{c}}\), \(\ell_{\mathrm{c}}\) | `cc`, `cl` | count, dB | count is a safe integer |
| \(L_1,L_2,L_3\) | `s1`, `s2`, `s3` | dB | \(\ge 0\) |
| \(L_{\mathrm{other}}\), \(M\) | `other`, `margin` | dB | \(\ge 0\) |

## Engineering Principles

The “standard” budget is the sensitivity window after a single penalty term. Overload uses the maximum launch, so a link can fail on too much power even when the sensitivity margin is large. Maximum distance assumes the same fixed loss and the same \(\alpha\) at every length; it is not a dispersion-limited reach.

## Worked Example

| Input | Value |
|---|---|
| \(P_{\mathrm{tx,min}}\), \(P_{\mathrm{tx,max}}\) | 2 dBm, 5 dBm |
| Sensitivity, overload | −28 dBm, +2 dBm |
| Penalty | 1 dB |
| Length, attenuation | 20 km, 0.35 dB/km |
| Splices, connectors | 4 × 0.10 dB, 2 × 0.50 dB |
| Splitters and other | 0 dB |
| Margin | 3 dB |

Steps:

1. \(B_{\mathrm{raw}} = 2 - (-28) = 30\,\mathrm{dB}\). \(B_{\mathrm{std}} = 29\,\mathrm{dB}\).
2. Fiber \(7.00\,\mathrm{dB}\). Fixed loss \(0.40 + 1.00 = 1.40\,\mathrm{dB}\). Physical loss \(8.40\,\mathrm{dB}\). Design loss \(11.40\,\mathrm{dB}\).
3. Remaining \(29 - 11.40 = 17.60\,\mathrm{dB}\).
4. \(P_{\mathrm{rx}} = 2 - 8.40 = -6.40\,\mathrm{dBm}\). Sensitivity margin \(21.60\,\mathrm{dB}\).
5. \(P_{\mathrm{rx,max}} = 5 - 8.40 = -3.40\,\mathrm{dBm}\). Overload margin \(2 - (-3.40) = 5.40\,\mathrm{dB}\).
6. \(d_{\max} = (29 - 3 - 1.40) / 0.35 = 70.2857\ldots\,\mathrm{km}\).

Result: design loss **11.40 dB**, remaining **17.60 dB**, status **healthy**. No intermediate rounding in the engine.

Boundary: set overload to \(-8\,\mathrm{dBm}\). Overload margin becomes \(-8 - (-3.40) = -4.60\,\mathrm{dB}\) and status is **failed**, with sensitivity margin still positive. Attenuation must stay greater than 0; the engine rejects \(\alpha = 0\).

## Limitations

- Three splitter fields are additive dB entries, not split ratios.
- One penalty number covers all transmitter and path penalties.
- The 3 dB warning threshold is internal to this calculator.
- Does not compute fiber loss from a wavelength table.

## Reference Standards

Pending as a cited edition inside this engine file. The fiber-loss page on the same site links ITU-T G.652, G.984.2, and G.671; this budget engine does not embed those URLs. Do not treat a class letter (B+, C+) as an output of this function unless those limits are entered as sensitivity, overload, and penalty.

## Online Calculator

https://netengineerlab.com/tools/optical-power-budget/

Inventory tool ID: `optical-power-budget`.

## Related Formulas

- [Single-span fiber link loss](fiber-link-loss.md)
- [Chromatic dispersion coefficient D(λ)](chromatic-dispersion.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `optical-power-budget` |
| Evidence | Production `tools/optical-power-budget/js/engine.js` `calculate`, 2026-11-04 |
| Method | Python reimplementation of each assignment in `calculate` |
| Example result | Design loss 11.40 dB, remaining 17.60 dB, healthy; overload boundary fails |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
