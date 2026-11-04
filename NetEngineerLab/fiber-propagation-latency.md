# Fiber propagation latency

## Overview

The Fiber Latency Calculator estimates one-way delay and round-trip time from route distance, a route factor, group index, per-device equipment delay, and optional serialization delay.

Engine: `https://netengineerlab.com/tools/fiber-latency-calculator/js/engine.js` (`NELFiberLatencyEngine`), fetched 2026-11-04.

## Formula

Distance is converted to kilometres (\(1\,\mathrm{mi} = 1.609344\,\mathrm{km}\), \(1\,\mathrm{m} = 0.001\,\mathrm{km}\)).

$$
L_{\mathrm{km}} = d_{\mathrm{km}} \times f_{\mathrm{route}}
$$

$$
t_{\mathrm{prop}} = L_{\mathrm{km}} \times n_g \times \frac{10^{6}}{c}, \quad c = 299792.458\,\mathrm{km/s}
$$

$$
t_{\mathrm{eq}} = N_{\mathrm{eq}} \, t_{\mathrm{dev}}
$$

$$
t_{\mathrm{ser}} = N_{\mathrm{hop}} \times \frac{S_{\mathrm{bytes}} \times 8}{R_{\mathrm{Gbit/s}} \times 10^{9}} \times 10^{6}
$$

$$
t_{\mathrm{ow}} = t_{\mathrm{prop}} + t_{\mathrm{eq}} + t_{\mathrm{ser}}, \qquad t_{\mathrm{rtt}} = 2\, t_{\mathrm{ow}}
$$

All of \(t\) above are in microseconds. Display rounding (`formatDelay`): if the absolute value is under \(1000\,\mu\mathrm{s}\), round to 2 decimal places and keep microseconds; otherwise convert to milliseconds and round to 3 decimal places. Rounding uses `Math.round((value + Number.EPSILON) * 10^n)`.

Default group index in the engine is 1.468. Accepted range is 1 to 1.6. Route factor must be at least 1.

## Variables

| Symbol | Engine field | Unit |
|---|---|---|
| \(d\) | `distance` with `distanceUnit` `km`, `mi`, or `m` | as selected |
| \(f_{\mathrm{route}}\) | `routeFactor` | 1 |
| \(n_g\) | `groupIndex` | 1 |
| \(N_{\mathrm{eq}}\), \(t_{\mathrm{dev}}\) | `equipmentCount`, `equipmentDelay` | count, µs |
| \(S_{\mathrm{bytes}}\) | `packetSize` | bytes |
| \(R\) | `linkRate` | Gbit/s |
| \(N_{\mathrm{hop}}\) | `serializationHops` | count |

## Engineering Principles

Group index, not the phase index, sets the delay of a modulated pulse. The constant \(c\) is the defined speed of light, \(299792.458\,\mathrm{km/s}\). Serialization is \(N\) times one hop of \(8S/R\), not a store-and-forward sum that changes with packet size along the path. Round trip is exactly twice the one-way sum; there is no asymmetric return path.

The engine also reports comparison delays that are not added into \(t_{\mathrm{ow}}\): vacuum \(10^{6}/c\), a microwave factor 1.0003 times vacuum, hollow-core factor 1.003 times vacuum, and copper at NVP 0.65 and 0.70 (vacuum delay divided by NVP).

## Worked Example

Inputs: 100 km, route factor 1, \(n_g = 1.468\), no equipment, packet size 0, link rate 10 Gbit/s, 0 serialization hops.

1. Fiber length \(= 100\,\mathrm{km}\).
2. \(t_{\mathrm{prop}} = 100 \times 1.468 / 299792.458 \times 10^{6} = 489.67209175\ldots\,\mu\mathrm{s}\).
3. Equipment and serialization are 0. One-way delay equals propagation. RTT is twice that, \(979.3441835\ldots\,\mu\mathrm{s}\).

Display rounding: **489.67 µs** one way and **979.34 µs** RTT. Per-kilometre delay is \(4.8967209\ldots\,\mu\mathrm{s/km}\).

Boundary: route factor must be \(\ge 1\). A value below 1 is rejected. Group index 1.6 on the same 100 km raises one-way delay to \(533.7025\ldots\,\mu\mathrm{s}\) (display **533.70 µs**). Group index below 1 or above 1.6 is rejected. Distance must be greater than 0.

Serialization check: 1500 bytes, 1 Gbit/s, 2 hops, other delays zero:

$$
t_{\mathrm{ser}} = 2 \times (1500 \times 8) / 10^{9} \times 10^{6} = 24\,\mu\mathrm{s}.
$$

## Limitations

- No queuing, FEC, or protocol ACK delay.
- Equipment delay is a constant per device, not a lookup by platform.
- Mile conversion is the international mile, 1.609344 km.
- Comparison copper and microwave figures are labels in the engine, not measured paths.

## Reference Standards

The page describes G.652 group-index presets (1.4677 at 1310 nm and 1.4682 at 1550 nm) as published values used by the selector. The engine file itself does not embed a recommendation URL. A specific G.652 edition for those two presets is **pending** in this library until the numeric table is tied to a fetched clause.

The speed \(299792.458\,\mathrm{km/s}\) is the defined vacuum speed used in the source (`C_KM_S`).

## Online Calculator

https://netengineerlab.com/tools/fiber-latency-calculator/

Inventory tool ID: `fiber-latency-calculator`.

## Related Formulas

- [Fiber link loss](fiber-link-loss.md)
- [Chromatic dispersion](chromatic-dispersion.md)
- [STP path cost](stp-path-cost.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `fiber-latency-calculator` |
| Evidence | Production `js/engine.js` constants `C_KM_S`, `MI_TO_KM`, `DEFAULT_GROUP_INDEX`, and `calculate` |
| Method | Direct evaluation of \(L n_g / c\) in Python |
| Example result | 489.672 µs one way before display rounding; display 489.67 µs |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
