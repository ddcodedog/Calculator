---
title: "Fiber Latency Calculation Explained"
published: false
description: "Calculate one-way fiber delay and round-trip time from route length, group index, equipment delay, and serialization."
tags: [networking, fiberoptics, tutorial, performance]
series: NetEngineerLab Fiber Engineering
canonical_url: ""
---

Fiber latency at this level is propagation time plus a few delays you can name. The propagation term is the route length divided by the speed of the modulated pulse in the glass. Round-trip time, in the model used here, is twice the one-way total. Queuing, forward error correction, and a protocol's acknowledgements are separate and are left out.

The equations match the Fiber Latency Calculator: distance scaled by a route factor, group index, a flat equipment delay, and optional serialization.

## Propagation uses the group index

Distance is converted to kilometres first. One international mile is 1.609344 km. One metre is 0.001 km. A route factor of at least 1 then stretches that length:

```
L_km = d_km × f_route
```

A factor of 1 means the distance you typed is already the glass length you want charged. A factor above 1 is how you grow a shorter map distance into a routed length. Factors below 1 are rejected.

Group index `n_g` sets the delay of a modulated pulse. A phase index describes a single-frequency wavefront and will mis-state that delay if you drop it into this formula. The vacuum speed in the engine is the defined constant `c = 299792.458 km/s`. One-way propagation in microseconds is:

```
t_prop_µs = L_km × n_g × 1e6 / c
```

The default group index is 1.468. The accepted range is 1 to 1.6. Outside that range the engine rejects the input. Per kilometre at the default index:

```
t_per_km = 1.468 × 1e6 / 299792.458 = 4.8967209… µs/km
```

The speed implied by that index is `c / 1.468 ≈ 204218 km/s`. The selector on the calculator page also offers 1.4677 at 1310 nm and 1.4682 at 1550 nm as published G.652-style presets. The formula notes still mark a specific recommendation edition for those two presets as pending, so the worked example below stays on the engine default, 1.468.

Vacuum delay on the same kilometre is `1e6 / c = 3.335641 µs`. The fiber figure is that vacuum delay multiplied by `n_g`.

## Equipment, serialization, and round trip

Equipment delay is a constant per device, multiplied by a count. It is not a lookup by platform:

```
t_eq_µs = N_equipment × t_device_µs
```

Serialization is the time to clock a frame onto a link, repeated for a hop count. `S` is the frame size in bytes and `R` is the rate in Gbit/s:

```
t_ser_µs = N_hops × (S × 8) / (R × 1e9) × 1e6
```

One hop of 1500 bytes at 1 Gbit/s is 12 µs. Two hops are 24 µs. The engine applies that same hop delay `N_hops` times. It does not build a store-and-forward sum that changes packet size at each node.

One-way delay adds the three terms. Round-trip time doubles the sum. The return path is the same total, not a second route with its own length:

```
t_one_way = t_prop + t_eq + t_ser
t_rtt = 2 × t_one_way
```

Displayed values follow the engine's rounding. Under 1000 µs the figure is rounded to two decimal places and kept in microseconds. At 1000 µs and above it is converted to milliseconds and rounded to three decimal places. Rounding is half-up on the scaled value, using the same `Math.round((value + Number.EPSILON) × 10^n)` step as the page.

The engine also prints comparison delays that stay out of `t_one_way`: vacuum, microwave at 1.0003 times vacuum, hollow core at 1.003 times vacuum, and copper at velocity factors 0.65 and 0.70. Those rows are labels next to the fiber result.

## Worked example: 100 km, default group index

Inputs: 100 km, route factor 1, `n_g = 1.468`, equipment count 0, packet size 0, link rate 10 Gbit/s, serialization hops 0.

1. Fiber length is 100 km.
2. `t_prop = 100 × 1.468 × 1e6 / 299792.458 = 489.67209175… µs`.
3. Equipment and serialization are 0, so one-way delay equals propagation.
4. Round-trip time is `979.3441835… µs`.

Display rounding reports **489.67 µs** one way and **979.34 µs** round trip. The per-kilometre figure is **4.8967209… µs/km**. A 5 µs/km rule of thumb on this span would say 500 µs one way, about 10.3 µs high, a little over 2 percent.

The same 100 km at the top of the allowed group index, 1.6, is `533.70255… µs` one way, which displays as **533.70 µs**. Distance must be greater than 0.

The 24 µs serialization check is a different input set, used only to confirm that term: 1500 bytes, 1 Gbit/s, 2 hops, and the other delays left at zero. It does not belong in the 100 km total above, where the hop count and the packet size are both zero.

## Common mistakes

- Charging 5 µs/km and presenting it as this model. At group index 1.468 the engine's own kilometre is 4.8967 µs. The 5 µs figure is a rough allowance, and on 100 km it moves the one-way result by about 10 µs.
- Inserting a phase index, or a generic "fiber is two-thirds of c", in place of the group index. Two-thirds of c is a group index of 1.5, which is inside the allowed range and is simply a different input: `1.5 / 1.468 ≈ 1.022`, about 2.2 percent more delay than the default.
- Folding the vacuum, microwave, hollow-core, or copper comparison rows into the fiber total. They are printed beside it. Copper at velocity factor 0.65 is `3.335641 / 0.65 ≈ 5.13 µs/km` of comparison delay, and it is not part of `t_one_way`.
- Building round-trip time as twice the fiber and then adding equipment once. Equipment sits inside the one-way sum, and the round trip doubles that whole sum. With 10 µs of equipment, one-way delay grows by 10 µs and round-trip time grows by 20 µs.
- Adding serialization on top of a 100 km run that already used zero hops. Serialization appears only for the hop count and frame size you entered.
- Reading this round trip as a ping. The sum has no queue, no FEC, no ACK timeout, and no asymmetric return path. A ping above `t_rtt` still has room for those delays; the calculator never received them.

## Limits that stay outside the number

Equipment delay is the constant you typed. Mile inputs use the international mile, 1.609344 km. The comparison media are labels beside the fiber result. They are not measured routes on the same trench.

The 100 km case can be rerun in the [Fiber Latency Calculator](https://netengineerlab.com/tools/fiber-latency-calculator/). Constants, the rounding rule, and this numerical check are in [NetEngineerLab/fiber-propagation-latency.md](https://github.com/ddcodedog/Calculator/blob/main/NetEngineerLab/fiber-propagation-latency.md).
