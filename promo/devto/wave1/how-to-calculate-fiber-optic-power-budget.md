---
title: "How to Calculate Fiber Optic Power Budget"
published: false
description: "Calculate a fiber power budget from minimum launch power and receiver sensitivity, then check overload and remaining reach."
tags: [networking, fiberoptics, tutorial, networkengineering]
series: NetEngineerLab Fiber Engineering
canonical_url: ""
---

A fiber power budget is the decibel window between the weakest launch a transmitter is allowed to produce and the weakest optical power a receiver can still accept. Fiber, splices, connectors, and splitters spend that window. The sums below are the ones implemented by the Optical Power Budget Calculator, with the same 20 km check recorded in the formula notes.

## Two launch powers, two receiver limits

Sensitivity is judged at minimum transmit power. Overload is judged at maximum transmit power. Both ends of the transmitter specification belong in the budget, because a short jumper can deliver more power than the receiver's overload point while a long span on the same optics still clears sensitivity.

Receiver sensitivity and overload are absolute powers in dBm. The gap between minimum launch and sensitivity is already in dB, since subtracting two dBm values cancels the 1 mW reference:

```
B_raw = P_tx,min − P_sens
B_std = B_raw − P_penalty
```

`P_penalty` is one number you enter, in dB. It stands for the path penalties you have chosen to reserve. The calculator does not compute it from chromatic dispersion or from a wavelength table.

Plant loss splits into fiber, which scales with length, and fixed losses, which do not:

```
L_fiber = d_km × α_dB_per_km
L_splice = N_splice × ℓ_splice
L_conn = N_connector × ℓ_connector
L_split = L1 + L2 + L3
L_fixed = L_splice + L_conn + L_split + L_other
L_physical = L_fiber + L_fixed
L_design = L_physical + M
```

Each splitter field is an insertion loss in dB. A split ratio such as 1:32 has to be converted to an insertion loss before it is typed. The three fields are added. Attenuation `α` must be greater than 0. With `α` at 0 the power-limited reach is undefined, and the engine rejects that input.

Remaining budget subtracts design loss, so the engineering margin is included:

```
B_remaining = B_std − L_design
```

Estimated receive power subtracts physical loss only. The margin is an allowance for the unknowns you listed, and it is kept out of the power you expect the meter to show:

```
P_rx = P_tx,min − L_physical
P_rx,max = P_tx,max − L_physical
M_sensitivity = P_rx − P_sens
M_overload = P_overload − P_rx,max
```

Power-limited distance reuses the same fixed loss, the same margin, and the same attenuation at every length:

```
d_max = max(0, (B_std − M − L_fixed) / α)
```

That length is the point where design loss equals the standard budget. It is a power reach. Dispersion and polarization-mode dispersion can limit a faster client before this distance is used up.

The result is failed when remaining budget, sensitivity margin, or overload margin is negative. It is a warning when any of those three is under 3 dB and still at least zero. Otherwise it is healthy. The 3 dB line is internal to this calculator. Margins within 10⁻⁹ dB of zero are treated as zero. When the standard budget is positive, usage is `100 × L_design / B_std`.

## Worked example: 20 km at 0.35 dB/km

| Input | Value |
|---|---|
| Minimum / maximum transmit power | 2 dBm / 5 dBm |
| Sensitivity / overload | −28 dBm / +2 dBm |
| Path penalty | 1 dB |
| Length / attenuation | 20 km / 0.35 dB/km |
| Splices | 4 × 0.10 dB |
| Connectors | 2 × 0.50 dB |
| Splitters and other loss | 0 dB |
| Engineering margin | 3 dB |

1. Raw budget: `2 − (−28) = 30 dB`. After the 1 dB penalty, `B_std = 29 dB`.
2. Fiber: `20 × 0.35 = 7.00 dB`. Splices `0.40 dB`. Connectors `1.00 dB`. Fixed loss `1.40 dB`.
3. Physical loss `8.40 dB`. Design loss `8.40 + 3.00 = 11.40 dB`.
4. Remaining budget: `29 − 11.40 = 17.60 dB`.
5. Receive level at minimum launch: `2 − 8.40 = −6.40 dBm`. Sensitivity margin: `−6.40 − (−28) = 21.60 dB`.
6. Receive level at maximum launch: `5 − 8.40 = −3.40 dBm`. Overload margin: `2 − (−3.40) = 5.40 dB`.
7. Power-limited reach: `(29 − 3 − 1.40) / 0.35 = 70.2857 km`.

Design loss is **11.40 dB**, remaining budget is **17.60 dB**, and the status is **healthy**. Usage of the standard budget is `100 × 11.40 / 29 = 39.31%`.

On these same losses, sensitivity margin sits 4.00 dB above remaining budget. That gap equals the path penalty plus the engineering margin, because both margins are built from the same minimum launch, the same sensitivity, and the same physical loss. Change any one of those and the 4 dB relationship changes with them.

The overload limit is doing separate work. Set it to −8 dBm and leave every other input alone. Overload margin becomes `−8 − (−3.40) = −4.60 dB`, and the status is **failed**, while the sensitivity margin is still positive. A link can have spare sensitivity and still be rejected because the strong launch is too strong.

## Common mistakes

- Running the sensitivity check from the maximum launch. The weak end of the transmitter range is the one that has to clear sensitivity. On this example that would replace −6.40 dBm with −3.40 dBm and would overstate the sensitivity margin by 3 dB.
- Subtracting the engineering margin a second time when estimating receive power. Physical loss already excludes it. Putting the 3 dB margin into `P_rx` would report −9.40 dBm at minimum launch.
- Quoting remaining budget and sensitivity margin as if they were the same reading. On the table above they are 17.60 dB and 21.60 dB.
- Typing a split ratio into a splitter field. The field adds decibels. An ideal 1:32 split is `10 log10(32) ≈ 15.05 dB` before excess loss. The calculator adds the decibel value you type.
- Treating a module class letter as an output. B+ or C+ shows up in the result only to the extent you typed that class's sensitivity, overload, and penalty into the inputs.
- Publishing `d_max` as a guaranteed span length. At 70.2857 km this model has used up the standard budget only while attenuation stays 0.35 dB/km and fixed loss stays 1.40 dB. A higher line rate can become dispersion-limited earlier.
- Double-counting connector ends. Loss per connector is whatever you decided one count represents. Count mated pairs if 0.50 dB is your pair allowance. Count ends if the allowance is per ferrule. The engine multiplies the count by the loss you entered.

## What a healthy flag leaves open

The flag compares the inputs. It does not replace a power-meter measurement or an OTDR acceptance test. One attenuation covers the whole length. There is no per-wavelength loss table and no automatic penalty from dispersion. Splice and connector counts are integers you supply.

The same 20 km inputs can be rerun in the [Optical Power Budget Calculator](https://netengineerlab.com/tools/optical-power-budget/). The equation list and this numerical check are in [NetEngineerLab/optical-power-budget.md](https://github.com/ddcodedog/Calculator/blob/main/NetEngineerLab/optical-power-budget.md).
