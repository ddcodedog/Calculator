# A cutover wait is not a fiber round trip

Locale: en

## Direct Answer

This note answers a cutover question: a DNS cache wait and a fiber round trip are different clocks and are not added.

Simplified Chinese edition: [割接等待不是光纤往返时延](cutover-wait-versus-fiber-delay.zh-CN.md).

## The decision

A metro link is 27 km of fiber, and a DNS change is planned on that same afternoon. Two clocks show up in the ticket: how long resolvers may still hold the old record, and how long a packet spends on the glass. They are both “delay.” They are not one delay. Adding them does not produce a maintenance window.

## What each tool is for

The DNS TTL calculator, baseline path with no `peakOldTtl`, turns the old TTL and the time already elapsed into remaining, typical, and worst minutes, plus a daily query ratio. The fiber latency calculator turns distance and group index into microseconds of propagation. Nothing in either engine reads the other engine’s output.

## One ticket, two units

| Input | Value | Tool |
|---|---|---|
| Old TTL, new TTL | 7200 s, 300 s | DNS |
| Already elapsed, authoritative delay, negative TTL | 1800 s, 20 s, 300 s | DNS |
| Lowered-before | 48 h | DNS |
| Distance, route factor, group index | 27 km, 1, 1.468 | Fiber |
| Equipment and serialization | none | Fiber |

Group index 1.468 and \(c = 299792.458\) km/s are the latency engine’s constants. The DNS minute display is one decimal place, `round((seconds/60 + ε) × 10) / 10`.

## Step through the two clocks

Remaining cache time:

$$
t_{\mathrm{left}} = \max(7200-1800,\ 0) = 5400\,\mathrm{s} = 90.0\,\mathrm{min}
$$

Typical wait = \(0.5\times 5400 + 20 = 2720\,\mathrm{s}\), displayed 45.3 min. Worst wait = \(\max(5400,\ 300)+20 = 5420\,\mathrm{s}\), displayed 90.3 min. Daily queries go from \(86400/7200 = 12\) to \(86400/300 = 288\), a factor of 24. The 48 h lowered-before window is longer than 7200 s, so the baseline status stays `pass`.

Fiber propagation, one way:

$$
t_{\mathrm{prop}} = 27 \times 1.468 \times \frac{10^{6}}{299792.458} = 132.211\ldots\,\mu\mathrm{s}
$$

The engine’s display rule (under 1000 µs, two decimals) prints **132.21 µs**. Round trip is twice that, **264.42 µs**. No equipment delay and no serialization were added.

## Why the numbers do not meet

90.0 minutes is \(5.4\times 10^{9}\) microseconds. The fiber RTT is 264 µs, about one part in twenty million of the remaining TTL. Putting 264.42 µs onto 90.0 min does not change a displayed minute. It also does not change the query-ratio warning. The cutover wait you plan against is the DNS worst case, 90.3 min on this baseline. The fiber number answers a different question: once a resolver does ask again, the path delay is a fraction of a millisecond, not another hour.

If the group index were wrong, the RTT would still be sub-millisecond at 27 km. If the old TTL had not been lowered and elapsed time were 0, the remaining cache would be the full 7200 s. That change moves the DNS clock by hours. It does not move the fiber clock.

## Limits

- Baseline DNS only. A `peakOldTtl` field switches on a second scenario this note does not use.
- Fiber distance is route kilometres you type, not a measured OTDR trace.
- Neither result is a promise that every resolver has expired or that the optical path is healthy. Loss and dispersion are other tools.

## Tools

- DNS TTL: https://netengineerlab.com/tools/dns-ttl-propagation-calculator/
- Fiber propagation: https://netengineerlab.com/tools/fiber-latency-calculator/

The site’s fiber link-budget guide is about decibels and distance, and the bandwidth guide is about file transfer. Neither compares a TTL minute to a propagation microsecond. This note does not reuse the 100 km latency example or the 100 GB transfer example.

## Online Calculator

Start with the TTL inputs above:

https://netengineerlab.com/tools/dns-ttl-propagation-calculator/

## Related Formulas

- [DNS TTL window before a record change](dns-ttl-cache-window.md)
- [Fiber propagation delay and RTT](fiber-propagation-latency.md)

## Verification

| Item | Value |
|---|---|
| Source tools | DNS `dns-ttl-engine/2.0.0` baseline; fiber latency engine constants |
| Evidence | Formulas already traced in production JS; this dataset recomputed in Node, including display rounding |
| Not done | No browser run, no live DNS query, no OTDR |
| Dedup scope | English sitemap guides and topic hubs fetched 2026-11-10, plus repo notes on main and PR #4 titles. Not a web-wide scan |
| Example result | 90.0 / 45.3 / 90.3 min beside 132.21 µs one way |
| Date | 2026-11-10 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |