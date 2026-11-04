# Ring all-reduce traffic and time

## Overview

The all-reduce estimator uses the ring factor \(2(N-1)/N\) on the parameter bytes, then divides by an effective byte rate and adds a latency term.

## Formula

$$
S = N_{params} \times b
$$

$$
S_{rank} = \frac{2(N-1)}{N} S
$$

$$
B = R_{bit/s} / 8 \times \eta
$$

$$
t_{bw} = S_{rank} / B
$$

$$
t_{lat} = 2(N-1)\, t_{hop}
$$

\(b\) is bytes per parameter. The FP16 choice on the page is 2. Efficiency is the entered percent divided by 100. \(t_{hop}\) is the entered latency converted from microseconds to seconds.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(N\) | Rank count | count |
| \(N_{params}\) | Parameter count | count |
| \(R\) | Link rate | bit/s |
| \(\eta\) | Efficiency | fraction |

## Engineering Principles

The ring volume factor is the standard two-pass \((N-1)/N\) expression written as one factor of \(2(N-1)/N\). The script applies it to the full parameter store, not to a gradient shard the user did not enter. Latency uses \(2(N-1)\) hops of the entered one-hop latency.

## Worked Example

Defaults: 8 ranks, 7 billion parameters, FP16 (2 bytes), 400 Gbit/s, 80% efficiency, 5 µs latency.

$$
S = 7\times 10^9 \times 2 = 1.4\times 10^{10}\ \text{bytes}
$$

The factor is \(2\times 7/8 = 1.75\). Bytes per rank are \(2.45\times 10^{10}\). Effective throughput is \(400\times 10^9 / 8 \times 0.8 = 4\times 10^{10}\) bytes/s. Bandwidth time is 0.6125 s. Latency time is \(14 \times 5\times 10^{-6} = 7\times 10^{-5}\) s. Sum is 0.61257 s.

Boundary: one rank makes the factor 0, so the bandwidth time is 0. A link rate of 0 is rejected.

## Limitations

The model is a single ring of equal links. It does not schedule a tree, a hierarchical all-reduce, or overlap with compute. Parameter count is a user entry, not a model file.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/all-reduce-traffic-estimator/

## Related Formulas

- [Ethernet serialization delay](ethernet-serialization-delay.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `all-reduce-traffic-estimator` |
| Evidence | Production `js/engine.js` ring factor and byte-rate division, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 1.75 times 1.4e10 bytes, bandwidth time 0.6125 s, latency 70 µs |
| Boundary | N = 1 gives a zero factor; zero link rate is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
