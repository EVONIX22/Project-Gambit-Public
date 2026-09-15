# Gambit X4 — Sanitized Conceptual Engineering Screening

| Field | Value |
|---|---|
| Evidence maturity | Virtual conceptual screening |
| Study date | September 2026 |
| Disclosure | Geometry, exact interfaces, meshes, and solver sources withheld |

## Scope

An early four-cylinder research model was evaluated as a learning and risk-
discovery platform. The study combined a native CAD assembly motion sweep, a
numerical constraint audit, analytical dynamics, and preliminary linear
structural, modal, friction, thermal, and clearance screens.

The speed sweep covered 1,000–12,000 rpm in 500 rpm increments. The kinematic
motion check covered three crank revolutions at one-degree increments, producing
1,081 audited solver frames after the initial pose.

## Results

| Area | Status | Public conclusion |
|---|---|---|
| Kinematics | **PASS** | The native assembly completed the commanded sweep; the undriven mechanism audit returned the expected single degree of freedom. |
| High-RPM dynamics | **INCONCLUSIVE** | The numerical sweep completed, but measured cylinder pressure, validated firing inputs, counterweight definition, and durability limits were unavailable. |
| Structural screen | **FAIL** | Conservative preliminary screens identified multiple redesign items below the conceptual factor-of-safety threshold. |
| Modal screen | **INCONCLUSIVE** | A possible connecting-rod engine-order crossing was identified inside the operating range; contacts, damping, and a complete torsional model are still required. |
| Friction | **INCONCLUSIVE** | Ring-pack behavior, oil properties, and several interfaces were provisional or absent. |
| Thermal | **INCONCLUSIVE** | A lumped network exposed thermal risk but did not include production-representative chambers, jackets, galleries, or thermal FEA fields. |
| Thermomechanical clearance | **FAIL** | At least one critical bearing/clearance interface was not yet defined in the conceptual CAD. |

## Selected Non-Enabling Metrics

- Native-solver motion sweep: **1,081 audited frames**, PASS.
- Constraint audit: **1 expected and measured degree of freedom**, PASS.
- Maximum normalized constraint residual: below **4 × 10⁻¹⁶**.
- Maximum joint position residual: below **3 × 10⁻¹¹ mm**.
- Preliminary maximum piston speed at 12,000 rpm: approximately **35.8 m/s**.
- Preliminary maximum connecting-rod load: approximately **63.6 kN** under a
  provisional high-load case.
- Preliminary linear structural screen: minimum factor of safety approximately
  **0.53**, triggering redesign rather than validation.

## Interpretation

The useful outcome is not a claim that the engine is ready. The study shows that
the early kinematic model behaved consistently while the broader engineering
screen found concrete structural, modal, lubrication, and thermal work before a
physical prototype would be justified. Retaining FAIL and INCONCLUSIVE findings
is deliberate and supports an auditable engineering learning process.

No complete component geometry, coordinates, bore/stroke pair, crank indexing,
clearance stack, manufacturing tolerance, material recipe, or model source is
included here.
