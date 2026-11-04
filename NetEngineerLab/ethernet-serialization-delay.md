# Ethernet serialization delay

## Overview

Serialization delay here is the time to clock a frame onto one link, multiplied by the number of hops. The script adds an 8-byte preamble and start-of-frame delimiter plus a 12-byte interframe gap when it reports wire time.

## Formula

$$
t_{frame} = N_{bytes} \times 8 / R
$$

$$
N_{wire} = N_{bytes} + 8 + 12
$$

$$
t_{wire} = N_{wire} \times 8 / R
$$

$$
t_{total} = t_{frame} \times N_{hops}
$$

The displayed nanosecond values are those times multiplied by \(10^9\). The hop total uses the frame time, not the wire time.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(N_{bytes}\) | Frame length entered by the user | bytes |
| \(R\) | Link rate | bit/s |
| \(N_{hops}\) | Hop count | count |

## Engineering Principles

Preamble plus SFD is the constant 8, and the interframe gap is the constant 12. A comment in the script points at IEEE 802.3 for those two lengths. The PDF was not opened. Rate must be positive. The page’s 10 Gbit/s choice is \(10 \times 10^9\) bit/s.

## Worked Example

Defaults: 1518 bytes, 10 Gbit/s, 3 hops.

$$
t_{frame} = 1518 \times 8 / 10^{10} = 1214.4\ \text{ns}
$$

Wire length is 1538 bytes and wire time is 1230.4 ns. Three hops of frame time are 3643.2 ns.

Boundary: one hop returns the frame time unchanged, 1214.4 ns. A rate of 0 is rejected.

## Limitations

The hop product does not add store-and-forward of the wire overhead, and it does not add propagation delay. Jumbo or short frames are whatever byte count the user types.

## Reference Standards

The engine comment names IEEE 802.3 preamble, SFD, and interpacket gap. That document was not opened, so the citation is pending. The constants used are the literals 8 and 12.

## Online Calculator

https://netengineerlab.com/tools/ethernet-serialization-delay-calculator/

## Related Formulas

- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `ethernet-serialization-delay-calculator` |
| Evidence | Production `js/engine.js` PREAMBLE_SFD = 8 and IFG = 12, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 1214.4 ns per hop, 3643.2 ns for 3 hops, wire 1230.4 ns |
| Boundary | 1 hop equals the frame time; zero rate is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
