# IPv4 subnet size

## Overview

The subnet calculator turns an IPv4 address and a prefix length into a mask, a network address, a broadcast address, and a usable-host count.

## Formula

For prefix length \(p\):

$$
mask = (2^{32}-1) \ll (32-p) \quad (p>0)
$$

Network is address AND mask. Broadcast is network OR the inverted mask, in 32-bit arithmetic.

$$
N_{total} = 2^{32-p}
$$

Usable hosts are 1 when \(p = 32\), 2 when \(p = 31\), and \(N_{total}-2\) otherwise. The mask for \(p = 0\) is 0.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| address | Dotted IPv4 address | four octets |
| \(p\) | Prefix length | 0 to 32 |

## Engineering Principles

The special cases for /31 and /32 keep the two-address and one-address prefixes from reporting a negative host count. For every other prefix the script still subtracts two addresses. The broadcast value is still computed for /31 as the last address of the two-address block.

## Worked Example

Example: 192.168.10.20/26.

Mask 255.255.255.192. Network 192.168.10.0. Broadcast 192.168.10.63. Total addresses 64. Usable hosts 62.

Boundary: 10.0.0.1/31 has mask 255.255.255.254, network 10.0.0.0, broadcast 10.0.0.1, total 2, usable 2. A /32 has usable 1. A prefix outside 0–32 is rejected.

## Limitations

The tool is IPv4 only. It does not allocate DHCP ranges, and it does not test whether an address is public or private beyond the numeric split.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://netengineerlab.com/tools/subnet-calculator/

## Related Formulas

- [Ethernet serialization delay](ethernet-serialization-delay.md)

## Verification

| Item | Value |
|---|---|
| Source tool | NetEngineerLab `subnet-calculator` |
| Evidence | Production `js/engine.js` IPv4 mask and usable-host branches, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 192.168.10.20/26 → network 192.168.10.0, usable 62, broadcast 192.168.10.63 |
| Boundary | /31 reports 2 usable hosts; prefix outside 0–32 is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
