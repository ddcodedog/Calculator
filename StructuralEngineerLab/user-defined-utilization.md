# User-defined demand over allowable

## Overview

Utilization is demand divided by allowable after both values are converted to the canonical unit for the selected quantity. The page does not choose the allowable.

## Formula

$$
U = q_{demand} / q_{allowable}
$$

Canonical force is newtons, with kN multiplied by 1000. Moment is newton-metres, stress is pascals, length is metres, and distributed load is newtons per metre. Demand must be greater than or equal to zero. Allowable must be greater than zero. The ratio is not capped at 1.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(q_{demand}\) | Demand in the selected quantity | user unit, then canonical |
| \(q_{allowable}\) | Allowable in the same quantity | user unit, then canonical |

## Engineering Principles

Identical units cancel. The script’s own note says it does not infer an allowable from TOOL-001 through TOOL-009 and does not apply AISC, Eurocode, ACI, or GB rules.

## Worked Example

Defaults: quantity type force, demand 80 kN, allowable 100 kN.

$$
U = (80\times 1000) / (100\times 1000) = 0.8
$$

Boundary: demand 0 gives utilization 0. Allowable 0 is rejected. Demand 120 kN against 100 kN returns 1.2, which the script still reports.

## Limitations

A ratio below 1 is not a code check. It is the quotient of the two numbers, in one unit system, that the user supplied.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://structuralengineerlab.com/tools/user-defined-utilization-calculator/

## Related Formulas

- [Elastic beam bending stress](beam-bending-stress.md)

## Verification

| Item | Value |
|---|---|
| Source tool | StructuralEngineerLab `TOOL-010` |
| Evidence | Production ratio after unit factors, kN factor 1000, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 0.8 |
| Boundary | zero demand returns 0; zero allowable is rejected; the ratio is not capped |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
