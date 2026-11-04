# HVAC cooling electrical energy

## Overview

Thermal energy is the cooling load times hours and a load factor. Compressor energy divides that by COP. Auxiliary energy is added before the tariff.

## Formula

$$
E_{th} = (Q/1000)\, t\, LF
$$

$$
E_{comp} = E_{th} / COP
$$

$$
E_{aux} = (P_{aux}/1000)\, t
$$

$$
E = E_{comp} + E_{aux}
$$

$$
P_{peak} = Q/(1000\, COP) + P_{aux}/1000
$$

Energy cost is \(E\) times the energy rate. A blank demand-rate field omits demand cost. \(Q\) and \(P_{aux}\) are in watts, \(t\) is in hours, and energies are in kWh.

## Variables

| Symbol | Meaning | Unit |
|---|---|---|
| \(Q\) | Cooling capacity | W |
| \(COP\) | Cooling COP | dimensionless |
| \(LF\) | Load factor | fraction |
| \(t\) | Hours | h |

## Engineering Principles

Auxiliary power is charged for the full hour count, not multiplied by the load factor. The compressor term is the only one divided by COP.

## Worked Example

Defaults: 100000 W, COP 4, auxiliary 5000 W, 2000 h, load factor 0.5, rate 0.12.

Thermal energy is \(100 \times 2000 \times 0.5 = 100000\) kWh. Compressor energy is 25000 kWh. Auxiliary energy is \(5 \times 2000 = 10000\) kWh. Electrical energy is 35000 kWh. Energy cost is \(35000 \times 0.12 = 4200\). Peak demand is \(100/4 + 5 = 30\) kW.

Boundary: load factor 0 removes thermal and compressor energy and leaves the auxiliary 10000 kWh. COP of 0 is rejected. With the demand rate left blank, demand cost is not added.

## Limitations

The location field does not change the arithmetic. The rate is a user number. Part-load COP curves are not applied.

## Reference Standards

No standards document was opened while writing this page. The production script names the relationship it implements. A code, guide, or textbook citation stays **pending** until that document is opened and checked against the script.

## Online Calculator

https://hvacengineerlab.com/tools/hvac-energy-operating-cost-analyzer/

## Related Formulas

- [Site energy use intensity](illustrative-site-eui.md)
- [Condensate from latent cooling load](condensate-from-latent-load.md)

## Verification

| Item | Value |
|---|---|
| Source tool | HVACEngineerLab `hvac-energy-operating-cost-analyzer` |
| Evidence | Production energy split, fetched 2026-11-04 |
| Method | Direct evaluation of the expressions above |
| Example result | 35000 kWh and cost 4200, peak 30 kW |
| Boundary | load factor 0 leaves auxiliary energy only; blank demand rate omits demand cost |
| Date | 2026-11-04 |
| Doc version | 1.0.0 |
| Status | VERIFIED |
