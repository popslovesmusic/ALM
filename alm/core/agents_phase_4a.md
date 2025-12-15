AGENTS.md — ALM Phase 4: Structural Persistence + Selection Pressure (Pre-Semantic)
Mission
Implement Phase 4: emergent structural persistence and selection pressure on top of the sealed Phase-3 lane-paired operator.

Phase 4 outputs are still non-semantic. The system must not interpret structures—only let them persist, dissolve, or dominate under physical constraints.

Phase 4 Constraints (Hard, Override All Prior Guidance)
1) Phase Boundary Integrity
Do not modify Phase-3 operator semantics, lane-pair rules, SIMD dispatch policy, or Phase-3 tests.

Do not modify TimeStencil contracts except bug fixes with explicit justification and regression tests.

2) No Semantics / No Labels
Forbidden:

tokens, symbols, “phrases,” categories

naming structures (“this is X”)

classifier logic

any explicit pattern recognition producing discrete IDs

Allowed:

measuring persistence, energy, recurrence

applying purely physical constraints (decay, diffusion, crowding)

3) No Control Loops
Phase 4 may introduce selection pressure, but not “control.”
Forbidden:

branching behavior based on metrics thresholds

“if energy > T then …”

gating or clamping “bad states”

Selection must be emergent, continuous, and local.

4) Locality
All Phase 4 effects must be local:

per cell / neighbor region

per lane-pair group
No global “mode switching.”

5) Physical Pressure Only
Selection pressure must come from:

limited bandwidth (finite write capacity)

finite memory (fixed tensor cluster)

decay competition

diffusion crowding
Not from explicit scoring/ranking.

Phase 4 Work Plan (Do in This Order)
Step 1 — Persistence Observables (No Thresholds)
Create a PersistenceProbe module that computes continuous observables from Phase-3 outputs.

Compute and record (continuous values):

Residual Energy Density per cell (already implicit in Phase 3; compute in Phase 4 without changing Phase 3)

Persistence: correlation of now vs recent vs stable

e.g., p = dot(now, recent) and p2 = dot(now, stable) (continuous, no thresholds)

Drift: difference between now and stable

Recurrence field: energy that remains coherent across ≥2 rotations (as a continuous measure)

Deliverables:

alm/core/include/alm/core/persistence_probe.hpp

alm/core/src/persistence_probe.cpp

Step 2 — Selection Pressure as Continuous Competition
Introduce only continuous operators that cause structures to compete:

Allowed mechanisms:

Crowding / Competition Term

locally increases effective decay when energy density is high (continuous function, no threshold)

example: effective_decay = base_decay + k * energy_density

Diffusion Crowding

strong gradients spread and flatten weaker ones over time

Resource Budget

limit per-tick “effective update magnitude” by smooth normalization factor (not hard clamp)

e.g., multiply updates by 1 / (1 + α * total_energy) (global scalar is allowed if smooth and non-branching)

Important:

No if/else

No step functions

No “top-k” selection

No discrete winners

Deliverables:

alm/core/include/alm/core/selection_pressure.hpp

alm/core/src/selection_pressure.cpp

Step 3 — Phase 4 Integration Kernel (Still Lane-Paired)
Create a Phase-4 kernel that:

reads now/recent/stable slices

applies selection pressure smoothly

writes to future

records observables

This kernel must remain:

branchless

vectorizable

lane-paired consistent

Deliverables:

alm/core/include/alm/core/phase4_kernel.hpp

alm/core/src/phase4_kernel.cpp

optional AVX2 variant if needed, but start scalar-first.

Step 4 — Phase 4 Tests (Proofs)
Add tests that prove:

No structure from null

if slices are symmetric/flat, future stays flat (Phase 4 preserves neutrality)

Competition emerges without thresholds

initialize two structures locally; observe one dissipates under crowding while the other persists (continuous measures, not discrete labels)

Invariants preserved

no NaNs under stress

no regression in Phase 3 tests

Deliverables:

alm/core/tests/phase4_neutrality_test.cpp

alm/core/tests/phase4_competition_smoke_test.cpp

Step 5 — Minimal Documentation
Create:

active/canonical/PHASE_4_PLAN.md

Include:

which observables exist

which pressure terms exist

what is explicitly forbidden (semantics, labeling, threshold gating)

Phase 4 completion criteria

Definition of Done (Phase 4)
Phase 4 is complete when:

persistence probe exists and is tested

selection pressure exists and is tested

Phase-4 kernel exists and preserves neutrality

competition emerges under smooth pressure (no thresholds)

Phase 3 regression tests still pass

Phase-4 plan doc exists

Phase-4 AGENTS.md is archived

Post-Completion Archiving Rule
After Phase 4 is complete and committed:

archive this AGENTS.md to archive/agents/AGENTS_PHASE4.md

replace/remove the active AGENTS.md to prevent drift

