# IPv4 longest prefix match

Locale: en

## Direct Answer

The longest-prefix tool picks one route for an IPv4 address. A route matches when the address, masked to that prefix, equals the route’s network. Among matches, the longest prefix wins. Equal prefixes break toward the lower metric, and equal metrics break toward the earlier line. No matching route is a warning and an empty selection, not a thrown error.


## Overview

Implementation `test.network.longest-prefix-match` version 1.12.0 in the production bundle, read 2026-11-07. The default target and the three default routes are the worked example (https://pcdog.com/tools/longest-prefix-match).
## Formula

Parse each route line on newlines, commas, or semicolons, up to three fields: CIDR, gateway, optional metric. More than three fields is `invalid-route-line`. A repeated CIDR plus gateway plus metric is `duplicate-route`. The metric, when present, must be finite and ≥ 0. A missing metric sorts as \(+\infty\), so a stated metric is preferred.

IPv4 prefix length \(n\) from 0 through 32. The mask is 0 when \(n = 0\), otherwise:

$$
\mathrm{mask} = (2^{32}-1) \ll (32-n) \quad \text{masked to 32 bits}
$$

Network = address AND mask. The target matches when target AND mask equals that network. Sort matches by prefix descending, then metric ascending, then input index ascending. The selected route is the first row after that sort.

## Variables

| Name | Default |
|---|---|
| Target | `192.168.1.42` |
| Routes | `0.0.0.0/0` via `gateway-default`; `192.168.0.0/16` via `gateway-lan`; `192.168.1.0/24` via `gateway-vlan` |

Metrics are omitted on the default rows, so they tie on metric and the prefix decides.

## Engineering Principles

A default route matches everything and still loses to a longer prefix that also matches. The gateway string is a label the tool copies onto the winner; it is not probed. Two identical prefixes with different metrics are a preference list, not two next hops used at once.

## Worked Example

Target `192.168.1.42`.

1. `/0` matches by construction.
2. `/16` mask keeps `192.168.0.0`. The target’s first two octets are `192.168`, so it matches `gateway-lan`.
3. `/24` mask keeps `192.168.1.0`. The target’s third octet is `1`, so it matches `gateway-vlan`.
4. Prefixes 24 > 16 > 0, so the winner is `192.168.1.0/24` via `gateway-vlan`.

Equal-prefix boundary: add `192.168.1.0/24` via `gateway-backup` metric 10 and another `192.168.1.0/24` via `gateway-primary` metric 5. Both match. Metric 5 sorts first, so `gateway-primary` wins. A line with four fields is `invalid-route-line` and is not a candidate. A target outside every non-default route still selects `0.0.0.0/0` when that route is present. With no matching row at all, status stays success, `inputStatus` is no-match, and the result is a partial-result warning.

## Limitations

- IPv4 only on this tool.
- No recursive lookup through a gateway, and no administrative distance beyond the typed metric.
- The result is a route choice on the list you typed. Reachability is not tested.

## Reference Standards

The mask and the longest-prefix ordering are the ones in the production bundle. RFC 4632 was not re-read. Status: pending.
## Online Calculator

The three-route default is filled on the longest-prefix tool:

https://pcdog.com/tools/longest-prefix-match

## Related Formulas

- [IPv4 static route commands](ipv4-static-route-commands.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PCDog `test.network.longest-prefix-match` 1.12.0 |
| Evidence | Production match test `(target & mask) === network` and the prefix, metric, index sort |
| Method | Applied the default table to 192.168.1.42 and the equal-prefix metric tie-break |
| Example result | Winner `192.168.1.0/24` via `gateway-vlan` |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
| Calculation status | VERIFIED |
| Standards status | PENDING |