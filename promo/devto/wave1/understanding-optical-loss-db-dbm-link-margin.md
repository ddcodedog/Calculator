---
title: "Understanding Optical Loss: dB, dBm and Link Margin"
published: false
description: "Separate optical loss in dB from power in dBm, then see how span loss and engineering margin set two different link margins."
tags: [networking, fiberoptics, tutorial, beginners]
series: NetEngineerLab Fiber Engineering
canonical_url: ""
---

Optical loss and optical power share a logarithmic scale and then part ways. A reading in dBm is a power. A reading in dB is a ratio between two powers. Link margin is what remains after that ratio has been spent against a budget or against a receiver threshold. Mixing the units is how a span that looks fine on a spreadsheet fails on a power meter.

The arithmetic below is the single-span model in the Fiber Loss Calculator. It is a loss sum plus a comparison to numbers you type. It is a different calculation from a power budget built out of transmitter minimums and receiver overload.

## dBm is a power, dB is a ratio

dBm is power referred to 1 mW:

```
P_dBm = 10 log10(P_mW / 1 mW)
```

| Power | Level |
|---|---|
| 1 mW | 0 dBm |
| 10 mW | 10 dBm |
| 1 µW (0.001 mW) | −30 dBm |

A change of 10 dB moves the power by ten times. A change of 3 dB moves it by about two times: `10^(0.3) ≈ 1.995`. So 3 dBm is about 2.00 mW, and −3 dBm is about 0.50 mW.

Loss in dB is the same logarithm applied to a ratio, which is why it also equals the difference of the two levels:

```
L_dB = 10 log10(P_in / P_out) = P_in_dBm − P_out_dBm
```

Subtract dB from dBm and the result is still dBm. Add two dBm figures and the result is a sum of logarithms, which is the product of the two powers, scaled by the reference. That product is rarely the quantity a link budget wants. Passive losses along one span add in dB because each element multiplies the power by a factor less than one, and logarithms turn those factors into a sum.

## What this span model adds

For one attenuation over the whole length:

```
L_fiber = d_km × α_dB_per_km
L_splice = N_splice × ℓ_splice
L_conn = N_connector × ℓ_connector
L_split_other = L_splitter1 + L_splitter2 + L_other
L_physical = L_fiber + L_splice + L_conn + L_split_other
L_design = L_physical + M
```

`α` is an input in dB/km. The engine does not look up a wavelength and pick a coefficient. Splitter fields are insertion losses in dB, already inclusive of whatever excess loss you assigned. The engine does not evaluate `10 log10(N)` for an N-way split.

Two comparisons then use that loss. They answer different questions:

```
B_remaining = B_available − L_design
P_rx = P_tx − L_physical
M_rx = P_rx − P_threshold
```

`B_available` is a budget in dB that you supply. `P_tx` and `P_threshold` are levels in dBm. Design loss includes the engineering margin, so remaining budget does too. Receive power uses physical loss alone, so the margin you reserved does not move the estimated meter reading.

The link is failed when remaining budget or receive margin is negative. It is a warning when either is under 3 dB and both are still at least zero. Otherwise it is healthy. The 3 dB band is a planning rule in this calculator. Absolute values at or below 10⁻⁹ dB are treated as zero.

Because the available budget is its own input, it can differ from `P_tx − P_threshold`. The gap between the two margins is fixed by that choice:

```
M_rx − B_remaining = (P_tx − P_threshold) − B_available + M
```

When you set the available budget equal to transmit level minus receive threshold, the two margins differ by exactly the engineering margin. When you set a different budget, they differ by the engineering margin plus that offset.

## Worked example: 10 km PON feeder

These inputs match the calculator's 10 km PON feeder loss case, together with the budget and power fields the engine requires.

| Input | Value |
|---|---|
| Distance / attenuation | 10 km / 0.25 dB/km |
| Splices | 6 × 0.10 dB |
| Connectors | 4 × 0.30 dB |
| Splitter 1 / splitter 2 / other | 21.0 dB / 0 dB / 0 dB |
| Engineering margin | 3 dB |
| Available budget | 32 dB |
| Transmit power | 3 dBm |
| Receive threshold | −27 dBm |

1. Fiber: `10 × 0.25 = 2.50 dB`.
2. Splices `0.60 dB`. Connectors `1.20 dB`. Splitter and other `21.00 dB`.
3. Physical loss: `2.50 + 0.60 + 1.20 + 21.00 = 25.30 dB`.
4. Design loss: `25.30 + 3.00 = 28.30 dB`.
5. Remaining budget: `32 − 28.30 = 3.70 dB`.
6. Receive level: `3 − 25.30 = −22.30 dBm`. Receive margin: `−22.30 − (−27) = 4.70 dB`.

Physical loss is **25.30 dB**, design loss is **28.30 dB**, and the status is **healthy**. Both margins clear the 3 dB warning line, the remaining budget by 0.70 dB and the receive margin by 1.70 dB.

Check the units on the receive level. 3 dBm is `10^(0.3) ≈ 1.995 mW`. −22.30 dBm is `10^(−2.230) ≈ 0.00589 mW`, about 5.89 µW. The ratio of those powers is 25.30 dB, which is the physical loss, and `3.00 − 25.30 = −22.30` brings the level back in dBm.

Here `P_tx − P_threshold = 3 − (−27) = 30 dB`, while the available budget was entered as 32 dB. The identity above gives `4.70 − 3.70 = 30 − 32 + 3 = 1 dB`. The receive margin is 1 dB larger than the remaining budget because the typed budget is 2 dB more generous than the raw window and the engineering margin then takes 3 dB back.

Drop only the available budget to 28 dB. Remaining budget becomes `28 − 28.30 = −0.30 dB` and the status is **failed**. Receive margin is unchanged at 4.70 dB, because the plant and the threshold did not move. A zero-length span drops only the fiber term and leaves physical loss at `25.30 − 2.50 = 22.80 dB`.

## Common mistakes

- Adding dBm to dBm and calling the sum a loss. Loss is a difference of levels, or `10 log10` of a power ratio.
- Subtracting design loss from transmit power when estimating what a meter should read. On this feeder that would give `3 − 28.30 = −25.30 dBm`. The model estimates `−22.30 dBm`, because the 3 dB engineering margin was never a loss in the glass.
- Assuming the available-budget box is filled in from the optics. In the example it is 32 dB and `P_tx − P_threshold` is 30 dB. Both numbers are inputs, and the status uses both.
- Entering 32, or 1:32, in a splitter field that expects decibels. The 21.0 dB in the table is already an insertion loss. An ideal 1:32 split is `10 log10(32) ≈ 15.05 dB` before excess loss. The extra `21.0 − 15.05 ≈ 5.95 dB` in this example is excess and other allocated loss sitting inside that one field.
- Using one margin to declare the link passed when the other has gone negative. The 28 dB budget case fails on remaining budget while the receive margin is still 4.70 dB.
- Letting the connector count mean two different things in two spreadsheets. The engine multiplies count by loss per count. Agree whether one count is a mated pair or one connector end, then keep that rule for the 0.30 dB figure.
- Treating a healthy result as an acceptance test. The 3 dB warning is local to the calculator. Reflection, PMD, and dispersion penalties are outside this sum.

## Where the same numbers are evaluated

One attenuation covers the whole route. There is no splice map, no bidirectional average, and no second wavelength. Splitter loss is whatever decibel value you entered.

Run the table in the [Fiber Loss Calculator](https://netengineerlab.com/tools/fiber-loss/). The matching derivation is [NetEngineerLab/fiber-link-loss.md](https://github.com/ddcodedog/Calculator/blob/main/NetEngineerLab/fiber-link-loss.md). The loss page links ITU-T G.652, G.984.2, and G.671, IEEE 802.3, and IEC 61280-4-2. A healthy flag is the comparison defined above. It is a planning result from the numbers you entered.
