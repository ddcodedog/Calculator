# IPv4 static route commands

## Overview

The static-route generator checks an IPv4 destination and gateway, normalizes host bits in the destination, and prints command text for several platforms. It does not log into a router and it does not test whether the gateway answers. The result field `reachability` is the constant `not-tested`.

Implementation `test.network.static-route-generator` version 1.11.0 in the production bundle, read 2026-11-07. Defaults: destination `192.168.10.0/24`, gateway `192.168.1.1`, interface `eth0`, metric `20`, persistent `true`, platform `linux` (https://pcdog.com/tools/static-route-generator).

## Formula

The destination must parse as an IPv4 CIDR. The gateway must parse as an IPv4 address (`/32` in the checker). A metric, when present, must be finite and ≥ 0. An omitted metric becomes 1 inside the command builder. The typed default is the string `20`, so the default commands use 20.

Host bits are cleared with the same prefix mask as the longest-prefix tool. If the typed CIDR is not already the network address, the result records `host-bits-normalized` and a warning. The netmask for a prefix \(n\) is four octets. Octet \(i\) (from 0) takes \(b = \mathrm{clamp}(n-8i,\ 0,\ 8)\) bits:

$$
\mathrm{octet} = 0 \text{ when } b = 0, \text{ else } 256-2^{8-b}
$$

Prefix 24 is `255.255.255.0`. Persistent `true` or `1` selects the persistent Windows form. A non-empty interface is inserted where that platform’s template has an interface slot.

## Variables

| Name | Default | Role |
|---|---|---|
| Destination CIDR | `192.168.10.0/24` | Network after host-bit clearing |
| Gateway | `192.168.1.1` | Next hop, copied into the command |
| Interface | `eth0` | Optional; omitted templates skip it |
| Metric | `20` | Preference value; blank becomes 1 |
| Persistent | `true` | Windows `-p` only |

## Engineering Principles

The generator’s job is a command string that matches the normalized prefix, not a prediction that the route will be installed. Linux `ip route` in this template is immediate; the note on that row says persistence depends on the distribution. Windows persistence is the `-p` flag. OpenWrt’s template commits and reloads network config. None of those side effects run inside the browser tool.

## Worked Example

Defaults, which are already on a network boundary, so no host-bit warning.

Linux:

```
ip route add 192.168.10.0/24 via 192.168.1.1 dev eth0 metric 20
```

Windows, because persistent is true:

```
route -p add 192.168.10.0 mask 255.255.255.0 192.168.1.1 metric 20
```

RouterOS uses distance for the metric field:

```
/ip route add dst-address=192.168.10.0/24 gateway=192.168.1.1 distance=20
```

Cisco inserts the interface when one was typed:

```
ip route 192.168.10.0 255.255.255.0 eth0 192.168.1.1 20
```

Boundary: destination `192.168.10.5/24` normalizes to `192.168.10.0/24` and adds `host-bits-normalized`. Gateway `999.1.1.1` fails the IPv4 check. A metric of `-1` fails the finite non-negative check. Clearing the metric field changes the printed metric from 20 to 1.

## Limitations

- Command text only. `reachability` stays `not-tested`.
- Platform templates are the ones in version 1.11.0 of this bundle, including macOS `sudo route -n add -net` and the OpenWrt `uci set` sequence. A vendor syntax newer than that bundle is not invented here.
- No IPv6 destination.

## Reference Standards

Mask construction and the command templates were read from the production bundle. Vendor command references were not re-read. Status: pending.
## Online Calculator

The Linux default is the form’s starting point:

https://pcdog.com/tools/static-route-generator

## Related Formulas

- [IPv4 longest prefix match](ipv4-longest-prefix-match.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PCDog `test.network.static-route-generator` 1.11.0 |
| Evidence | Production netmask helper and the Windows, Linux, RouterOS, and Cisco template strings |
| Method | Built the default commands from those templates and checked /24 masking of a host address |
| Example result | Linux `ip route add 192.168.10.0/24 via 192.168.1.1 dev eth0 metric 20` |
| Date | 2026-11-07 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
