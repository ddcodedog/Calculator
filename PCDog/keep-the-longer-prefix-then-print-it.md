# Keep the longer prefix, then print that route

## Two decisions in order

The longest-prefix page chooses a route. The static-route page prints a command for a route you already chose. Printing the command for the shorter prefix, because its metric is prettier, undoes the first decision.

## Table

| Prefix | Next hop | Interface | Metric |
|---|---|---|---:|
| 10.8.0.0/16 | 10.1.0.1 | core-edge | 10 |
| 10.8.3.0/24 | 10.8.3.1 | eth1 | 50 |

Target `10.8.3.19`. Both prefixes contain it. Prefix length 24 beats 16. Metric 10 does not override that. The winner is `10.8.3.0/24` via `10.8.3.1`, metric 50. The page would list the /16 as a candidate and mark it not selected.

A target of `10.8.9.4` matches only the /16. Then the metric comparison never starts, because there is one candidate. This ticket’s target is `10.8.3.19`, so the /24 stays selected.

## The command that matches the winner

Linux template on the static-route tool, host bits already clear:

```
ip route add 10.8.3.0/24 via 10.8.3.1 dev eth1 metric 50
```

The tool clears host bits before it prints. Typing `10.8.3.19/24` as the prefix would still print `10.8.3.0/24`. That cleanup is not a second routing decision. It does not consult the /16.

Windows, from the same tool’s template, is a different line and a different operating system. Do not paste the Linux line into `route add` and do not paste a Windows line into `ip route`. This note prints Linux because the interface name `eth1` belongs in the Linux template.

## What the metric is allowed to do

If a second route were also `10.8.3.0/24` with metric 5, longest-prefix would tie on length and the lower metric would win. That second route is not in the table. Metric 10 on a /16 never beats metric 50 on a /24 for `10.8.3.19`.

## Limits

- The table is the whole forwarding set for this check. A more specific route that is not listed cannot be selected.
- The printed command is text. It was not applied to a router.
- No policy routing, no VRF, no NAT.

## Tools

- Choice: https://pcdog.com/tools/longest-prefix-match
- Command: https://pcdog.com/tools/static-route-generator

The site’s “why /24 beats a lower-metric /16” page uses a different address story. The static-route guide’s sample prefix is not `10.8.3.0/24`.

## Online Calculator

Print the command only after the /24 has won:

https://pcdog.com/tools/static-route-generator

## Related Formulas

- [IPv4 longest prefix match](ipv4-longest-prefix-match.md)
- [IPv4 static route commands](ipv4-static-route-commands.md)

## Verification

| Item | Value |
|---|---|
| Source tools | LPM: longer prefix, then lower metric, then input index. Static route: documented Linux template with host bits cleared |
| Evidence | Rules applied to this two-route table. No packet was sent |
| Dedup scope | PC guides for static routes and for /24 versus /16, read 2026-11-10. Not a web-wide scan |
| Example result | `10.8.3.19` selects `10.8.3.0/24` metric 50; Linux command as printed |
| Date | 2026-11-10 |
| Status | VERIFIED |
