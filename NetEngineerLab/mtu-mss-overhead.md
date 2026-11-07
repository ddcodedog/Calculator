# MTU, MSS, and encapsulation overhead

## Overview

The MTU calculator subtracts each encapsulation layer from an underlay MTU, then reports the remaining inner packet, the TCP MSS that fits inside it, and the Ethernet wire length of that packet. It is a header budget, not a path-MTU probe.

Engine: `js/engine.js` and `js/mtu-library.js` on the production tool, read 2026-11-07. The underlay must be a finite number of at least 576 bytes. A smaller underlay is `underlay_mtu_out_of_range`.

## Formula

VLAN overhead is \(4\) bytes per outer tag, and the tag count is `min(16, floor(count))`. If strict VLAN accounting is off, those bytes are not removed from the inner packet.

$$
L_{\mathrm{inner}} = \max\left(0,\ M_{\mathrm{underlay}} - \sum_i \mathrm{bytes}_i\times\mathrm{count}_i\right)
$$

Fixed headers inside that inner packet:

| Protocol | Bytes |
|---|---:|
| IPv4 | 20 |
| IPv6 | 40 |
| TCP, no options | 20 |
| UDP | 8 |
| ICMP | 8 |

Advertised TCP MSS is \(\max(0, L_{\mathrm{inner}} - \mathrm{IP} - 20)\). Extra IP header bytes and TCP options are subtracted only from the actual TCP data length, not from the advertised MSS. The wire frame the tool reports is \(14 + \mathrm{VLAN} + \mathrm{payload} + 4\) (Ethernet header, tags, payload, FCS).

The path fails when the inner length cannot hold the IP header plus 8 bytes, or when the desired inner size is larger than \(L_{\mathrm{inner}}\). IPv6 warns below 1280 bytes. IPv4 warns below 576. Headroom in \([0, 40)\) adds `low_headroom`. Overhead of 10% or more adds `high_overhead`.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Underlay MTU | Outer packet limit before the selected layers | bytes, ≥ 576 |
| Layers | Named overhead from the library, each with a byte size and a count | bytes |
| Desired inner size | The payload size you hoped to keep | bytes |
| Address family | Chooses the 20-byte or 40-byte IP header | IPv4 or IPv6 |
| Path count | Fewer than 2 paths adds a `single_path` warning | count |

## Engineering Principles

MSS is what remains after the IP and TCP headers, so it is 40 bytes smaller than the inner IPv4 packet (20 + 20) and 60 bytes smaller for IPv6. Encapsulation does not change that 40 or 60; it shrinks the packet those headers sit in. A desired size equal to the effective inner size leaves no spare bytes for options, which is why headroom of 0 is a warning even when the arithmetic succeeds.

## Worked Example

PPPoE preset: underlay 1500 bytes, one 8-byte PPPoE layer, desired inner size 1492, IPv4, no VLAN, path count 1.

1. \(L_{\mathrm{inner}} = 1500 - 8 = 1492\). Desired size matches, so headroom is 0.
2. Advertised MSS = \(1492 - 20 - 20 = 1452\) bytes.
3. UDP payload = \(1492 - 20 - 8 = 1464\) bytes. ICMP payload is the same 1464.
4. Wire frame = \(14 + 1492 + 4 = 1510\) bytes.
5. Overhead = \(8 / 1500 = 0.5333\%\).

Status stays healthy. Warnings are `low_headroom` (0 bytes spare) and `single_path`. Both sit in the tool’s priority-1 warning list, so the risk label is P1 even though the sizes fit.

Boundary: desired inner size 1493 on this path is `desired_exceeds_effective`. An underlay of 575 is rejected before any layer math.

## Limitations

- Layer sizes are the library constants (PPPoE 8, GRE IPv4 24, VXLAN IPv4 50, WireGuard IPv4 60, MPLS 4 per label). They are not measured on a live tunnel.
- Options, vendor tags, and double encapsulation that are not in the selected layer list are omitted.
- The tool does not send packets.

## Reference Standards

The page names Ethernet, IP, and TCP header sizes as fixed constants in the engine. The standards documents themselves were not re-read. Status: pending.

## Online Calculator

Run the same PPPoE case in the MTU calculator:

https://netengineerlab.com/tools/mtu-calculator/

## Related Formulas

- [File transfer time from link rate](bandwidth-transfer-time.md)
- [Optical link power budget](optical-power-budget.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab MTU calculator |
| Evidence | Production `js/engine.js` inner-length, MSS, and wire-frame expressions; PPPoE size from `js/mtu-library.js` |
| Method | Recomputed 1500 − 8 and the IPv4 header split |
| Example result | Inner 1492, advertised MSS 1452, wire 1510, overhead 0.5333% |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
