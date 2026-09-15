# Methodology, Traceability, and Limitations

## Purpose

This public package demonstrates an engineering process without disclosing the
complete geometry, manufacturing definition, proprietary mechanisms, or private
solver implementation. It is suitable for initial technical diligence, not for
reproduction or certification.

## Evidence Chain

1. A versioned private engineering snapshot is selected.
2. Test scope, acceptance criteria, solver class, and outcome are extracted.
3. Enabling dimensions, coordinates, component geometry, tolerances, personal
   paths, detailed meshes, source code, and confidential inputs are removed.
4. Aggregate values are rounded where precision is not needed to understand the
   result.
5. The public repository validator checks prohibited formats, broken local links,
   machine-readable CSV schemas, status vocabulary, and common secret/path leaks.

The private source artifacts remain available for controlled due diligence under
an appropriate confidentiality agreement.

## Maturity Boundaries

The published evidence is virtual and conceptual unless explicitly identified as
a physical test. At the current stage there is no public evidence of a physical
dyno run, endurance test, homologation test, or production-ready design.

Results may change when provisional pressure curves, material data, boundary
conditions, contacts, damping, lubrication, cooling, and manufacturing variation
are replaced by measured inputs. Simulation convergence does not establish that
the modeled assumptions are physically correct.

## Disclosure Boundary

Allowed public artifacts include narrative conclusions, aggregate metrics,
PASS/FAIL/INCONCLUSIVE matrices, and non-enabling plots. Prohibited artifacts
include CAD and mesh formats, `.mr` model sources, exact enabling geometry,
manufacturing tolerances, private numerical solver sources, secrets, and personal
machine paths.
