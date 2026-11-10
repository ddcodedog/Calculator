# DNS TTL window before a record change

Locale: en

Simplified Chinese edition: [记录变更前的 DNS TTL 窗口](dns-ttl-cache-window.zh-CN.md).

## Direct Answer

This note answers a DNS TTL question: how long a cache may keep a record before a change is visible.

A resolver that cached a record keeps the old answer until that cached TTL expires. This calculator turns the old TTL, the time already spent, the new TTL, and a small authoritative delay into three clock estimates and a daily query-rate ratio. It does not query a live resolver, and it does not prove that every recursive server on the internet has dropped the old answer.


## Overview

The numbers below come from `dns-ttl-engine/2.0.0` in the production `engine.js` for this tool, read on 2026-11-08. The example omits `peakOldTtl`, so the engine returns the baseline scenario only (https://netengineerlab.com/tools/dns-ttl-propagation-calculator/).
## Formula

Remaining cache time is what is left of the old TTL:

$$
t_{\mathrm{left}} = \max(T_{\mathrm{old}} - t_{\mathrm{elapsed}}, 0)
$$

Typical and worst waits, in seconds, add the authoritative delay:

$$
t_{\mathrm{typical}} = 0.5\,t_{\mathrm{left}} + t_{\mathrm{auth}}, \qquad t_{\mathrm{worst}} = \max(t_{\mathrm{left}}, T_{\mathrm{neg}}) + t_{\mathrm{auth}}
$$

Displayed minutes use one decimal place: \(\mathrm{round}((v+\epsilon)\times 10)/10\), with \(\epsilon\) the JavaScript `Number.EPSILON`. Query counts for one day are

$$
Q_{\mathrm{old}} = \begin{cases} 86400/T_{\mathrm{old}} & T_{\mathrm{old}}>0 \\ 86400 & T_{\mathrm{old}}=0 \end{cases}, \qquad Q_{\mathrm{new}} = 86400/T_{\mathrm{new}}, \qquad R = Q_{\mathrm{new}}/Q_{\mathrm{old}}
$$

\(T_{\mathrm{old}}\ge 0\), \(T_{\mathrm{new}}>0\), and elapsed time, delay, negative TTL, and the “lowered before” hours must be finite and ≥ 0. Status is `warning` only when the lowered-before window is shorter than the old TTL (`lowerBeforeHours × 3600 < T_old`). A new TTL under 60 seconds adds `highAuthoritativeQps` to the warning list and still leaves status `pass` unless that late-window warning is also present.

## Variables

| Name | Meaning | Unit |
|---|---|---|
| Old TTL | TTL currently cached | s |
| New TTL | TTL after the change | s |
| Elapsed | Time since the old TTL was published | s |
| Authoritative delay | Extra wait after the cache timer | s |
| Negative TTL | How long a negative answer may be kept | s |
| Lowered before | How early the TTL was reduced | h |

## Engineering Principles

Half of the remaining TTL is a planning midpoint, not a measured median of resolver clocks. The worst case takes the longer of the remaining positive cache and the negative-cache TTL, then adds the same authoritative delay. The query ratio assumes one uncached lookup each TTL for a steady 86,400 seconds. It is not a forecast of real QPS, because retries, resolver pools, and serve-stale policy are outside this baseline.

## Worked Example

Old TTL 3600 s, new TTL 300 s, 600 s already elapsed, authoritative delay 30 s, negative TTL 300 s, lowered 24 h beforehand.

1. Remaining seconds = \(\max(3600-600, 0) = 3000\). Displayed remaining time = 50.0 min.
2. Typical seconds = \(0.5\times 3000 + 30 = 1530\), displayed 25.5 min.
3. Worst seconds = \(\max(3000, 300)+30 = 3030\), displayed 50.5 min.
4. Old queries per day = \(86400/3600 = 24\). New queries = \(86400/300 = 288\). Increase = 12.0.
5. \(24\times 3600 = 86400\), which is not less than 3600, so status is `pass`.

Boundary: the same old TTL with “lowered before” set to 0.5 h gives \(1800 < 3600\), so status becomes `warning` with `lowerTtlTooLate`. A new TTL of 30 s adds `highAuthoritativeQps` and does not, by itself, change `pass` to `warning`. A non-finite TTL returns `{ok:false}`.

## Limitations

- Baseline path only. Supplying `peakOldTtl` switches on the later risk report; this note does not walk that branch.
- No live DNS lookup. A resolver may serve stale data longer than \(t_{\mathrm{worst}}\).
- The one-decimal minute display is not the value to multiply again if you need the raw seconds.

## Reference Standards

The engine does not cite an RFC section for the 0.5 factor. RFC 1035 and RFC 2308 describe TTL and negative caching; those documents were not re-read for this note. Status: pending.
## Online Calculator

Run the 3600 s to 300 s case, with 600 s elapsed, on the production page:

https://netengineerlab.com/tools/dns-ttl-propagation-calculator/

## Related Formulas

- [File transfer time from link rate](bandwidth-transfer-time.md)
- [MTU, MSS, and encapsulation overhead](mtu-mss-overhead.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `dns-ttl-propagation-calculator` |
| Evidence | Production `js/engine.js`, model `dns-ttl-engine/2.0.0`, baseline return when `peakOldTtl` is absent |
| Method | Recomputed in Node with the engine’s `round` helper |
| Example result | 50.0 / 25.5 / 50.5 min, query increase 12.0, status pass |
| Date | 2026-11-08 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |