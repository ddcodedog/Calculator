# Electrical efficiency and loss

## Overview

Efficiency is output power divided by input power. Loss is the difference. Both powers must be greater than zero, and output must not exceed input.

## Formula

$$
\eta = P_{out} / P_{in}
$$

$$
\eta_{\%} = 100\eta
$$

$$
P_{loss} = P_{in} - P_{out}
$$

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(P_{in}, P_{out}\) | Powers on the same basis | W |

## Engineering Principles

The page has no load-example object. The numbers below are a domain-valid pair: input above output, both positive. The script also rejects a pair whose ratio collapses to 1 while the two parsed powers still differ, which is a precision guard.

## Worked Example

Take \(P_{in} = 1000\) W and \(P_{out} = 850\) W.

$$
\eta = 0.85,\quad \eta_{\%} = 85,\quad P_{loss} = 150\ \text{W}
$$

Boundary: equal powers of 1000 W give efficiency 1 and loss 0. Output of 1001 W is rejected. Output of 0 is rejected.

## Limitations

Same-basis watts are the user’s responsibility. Auxiliary loads are not added unless they are already inside the input figure. The formula string on the page is the three lines above.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://powerengineerlab.com/calculators/electrical-efficiency/

## Related Formulas

- [Three-phase motor line current](motor-line-current.md)
- [AC apparent real and reactive power](ac-power.md)

## Verification

| Item | Value |
|---|---|
| Source tool | PowerEngineerLab `electrical-efficiency` (script id `BACKLOG-026`) |
| Evidence | Production chunk `1zs56gwld9gz4.js`, eta = Pout/Pin, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 0.85 and 150 W from 1000 W and 850 W |
| Boundary | equal powers give eta 1; output above input is rejected |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
