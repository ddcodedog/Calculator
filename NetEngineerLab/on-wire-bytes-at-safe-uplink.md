# Header bytes, then the safe uplink, then the clock

## Question

A 500 GB decimal payload (exactly \(500\times 10^{9}\) bytes) has to cross one 10 Gbit/s uplink. The access ports could nameplate 16 Gbit/s. The MSS is not 1500 bytes. Which rate belongs in the transfer-time division, and which byte count belongs in the numerator?

## Roles

Three tools, in an order that only works if the units are handed across on purpose.

1. MTU calculator: underlay 1500 bytes, no extra tunnel layer, IPv4, TCP. It reports the inner length, the advertised MSS, and the Ethernet wire size of one full frame.
2. Uplink calculator, short baseline (no engineering keys): it reports a safe gigabit slice. It does not know the file.
3. Bandwidth calculator: file bytes, bit rate, efficiency, utilization, concurrency, RTT. It does not know MSS.

## Dataset

| Quantity | Value |
|---|---|
| Underlay MTU | 1500 bytes, no VLAN, no PPPoE |
| Address family | IPv4, TCP without options |
| Payload | \(500\times 10^{9}\) bytes |
| Access ports | 16 × 1000 Mbit/s |
| Utilization, concurrency, overhead, burst | 25%, 40%, 0, 0 |
| Uplink | one × 10,000 Mbit/s, target 50% |
| Transfer efficiency and utilization | 100% and 100%, one transfer, RTT 0 |

This is not the site’s 48×1G with 2×10G oversubscription write-up, and not the bandwidth guide’s 100 GB example.

## The handoff

Advertised MSS = \(1500 - 20 - 20 = 1460\) bytes. A full frame on the wire is \(14 + 1500 + 4 = 1518\) bytes. The payload splits into 342,465,753 full segments and a last segment of 620 bytes. That last inner packet is \(620+40 = 660\) bytes, and its frame is \(14+660+4 = 678\) bytes.

$$
B_{\mathrm{wire}} = 342465753\times 1518 + 678 = 519863013732\ \mathrm{bytes}
$$

The extra over the 500 GB payload is 19,863,013,732 bytes. Those bytes are headers and FCS, not a second copy of the file.

Uplink demand = \(16\times 1000\times 0.25\times 0.40 = 1600\) Mbit/s, displayed 1.60 Gbit/s. Capacity is 10 Gbit/s. The safe slice at 50% is 5.00 Gbit/s. Peak is under that slice, so the short baseline status is `pass`. Oversubscription displays `1.6:1`. Required uplinks = \(\lceil 1600/5000\rceil = 1\).

The transfer tool then sees the **wire** byte count and the **safe** rate, with \(\eta = 1\) and no setup RTT:

$$
t = \frac{8\times 519863013732}{5\times 10^{9}} = 831.78082197\ \mathrm{s}
$$

That is 13.863 minutes. Dividing the raw 500 GB payload by the same 5 Gbit/s instead gives exactly 800 s. The 31.8 s gap is the header tax, and only if you expanded the bytes **or** lowered efficiency, not both. Dividing by 16 Gbit/s of access-port nameplate would describe a different path than the one uplink the file actually crosses.

## Judgment

Use 5 Gbit/s because that is the target fraction of the uplink, not because 16 ports exist. Use 519,863,013,732 bytes because each TCP segment grows by IP, TCP, Ethernet, and FCS. Leave efficiency at 100% once the bytes are already on-wire; the Ethernet preset of 95% × 90% would tax the headers a second time.

If the uplink target were the whole 10 Gbit/s, the same wire bytes would take half as long. The target is an input, not a measured queue.

## Limits

- Full-size frames assume the path really allows a 1500-byte inner packet. A PPPoE layer would shrink MSS; this dataset has none.
- Burst, N-1, and growth are omitted, so the safe slice is the short baseline only.
- RTT is set to 0. A setup delay would add \(R k/1000\) seconds on top of 831.78 s and would not change the byte expansion.

## Tools

- MTU and MSS: https://netengineerlab.com/tools/mtu-calculator/
- Uplink slice: https://netengineerlab.com/tools/switch-uplink-oversubscription-calculator/
- Transfer time: https://netengineerlab.com/tools/bandwidth-calculator/

## Online Calculator

The clock that answers “how long” is the bandwidth tool, after the other two have supplied bytes and rate:

https://netengineerlab.com/tools/bandwidth-calculator/

## Related Formulas

- [MTU, MSS, and encapsulation overhead](mtu-mss-overhead.md)
- [Access-switch demand against uplink headroom](switch-uplink-safe-capacity.md)
- [File transfer time from link rate](bandwidth-transfer-time.md)

## Verification

| Item | Value |
|---|---|
| Source tools | MTU engine byte table, uplink short baseline, bandwidth \(8S/(B\eta)\) |
| Evidence | Python integer segment count; uplink arithmetic matches `engine.js` rounding rules; no browser click |
| Dedup scope | Switch-oversubscription topic hub, the 2×10G guide, and the bandwidth guide were read 2026-11-10. Not a web-wide scan |
| Example result | 519,863,013,732 wire bytes at 5 Gbit/s → 831.781 s |
| Date | 2026-11-10 |
| Status | VERIFIED |
