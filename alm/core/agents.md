AGENTS.md — Phase 4 Instructions (Continuation)
Phase 4 Name
Structural Persistence & Selection Pressure

Phase 4 Purpose (Operational)
Phase 4 introduces competition among structures that already exist.

Nothing new is invented.
Nothing is named.
Nothing is chosen.

Structures are allowed to:

persist

diffuse

crowd each other

decay

Only those that survive physical pressure remain.

Phase 4 Scope (Strict)
Phase 4 may:

measure persistence

apply smooth selection pressure

let structures crowd and suppress each other

record outcomes

Phase 4 may not:

decide winners

threshold behavior

promote memory

label patterns

introduce semantics

Phase 4 Work Units (Do in Order)
Step 1 — Persistence Probe (Observation Only)
Goal
Quantify how long and how coherently structure survives across time slices.

Implementation
Create a persistence probe that reads:

stable

recent

now

and computes continuous observables, such as:

Correlation(now, recent)

Correlation(now, stable)

Drift magnitude (now − stable)

Residual energy density

Rules
No thresholds

No classification

No branching

No mutation of tensors

Metrics only

Deliverables
swift
Copy code
alm/core/include/alm/core/persistence_probe.hpp
alm/core/src/persistence_probe.cpp
alm/core/tests/persistence_probe_smoke_test.cpp
Step 2 — Selection Pressure (Physics Only)
Goal
Allow structures to suppress each other without decisions.

Allowed Pressure Mechanisms
Crowding-Driven Decay

Higher local energy → higher decay rate

Implemented as a smooth multiplier

Diffusion Competition

Strong gradients spread

Weak structures flatten

Bandwidth Pressure

High total activity → reduced effective update magnitude

Must be smooth and branchless

Forbidden
If/else logic

Thresholds

Max/min clamping

Explicit “selection”

Deliverables
swift
Copy code
alm/core/include/alm/core/selection_pressure.hpp
alm/core/src/selection_pressure.cpp
alm/core/tests/selection_pressure_smoke_test.cpp
Step 3 — Phase 4 Kernel Integration
Goal
Combine Phase-3 residual dynamics + Phase-4 pressure into a single tick.

Kernel Responsibilities
Read stable, recent, now

Apply:

residual persistence weighting

selection pressure

Write only to future

Preserve paired lanes

Preserve neutrality

Rules
Branchless

Vectorizable

Scalar + SIMD compatible

No normalization

Deliverables
swift
Copy code
alm/core/include/alm/core/phase4_kernel.hpp
alm/core/src/phase4_kernel.cpp
alm/core/tests/phase4_neutrality_test.cpp
Step 4 — Competition Smoke Test
Goal
Demonstrate emergent competition without explicit logic.

Test Setup
Initialize two local structures

Allow system to evolve

Observe:

one persists longer

one decays faster

No assertions about “which”

Only assert:

no NaNs

neutrality preserved

dynamics occur

Deliverable
bash
Copy code
alm/core/tests/phase4_competition_smoke_test.cpp
Step 5 — Phase 4 Seal
Documentation
Create:

bash
Copy code
active/canonical/PHASE_4_COMPLETE.md
Must state:

What Phase 4 adds

What it explicitly does not do

That system remains pre-semantic

Archival
After completion:

Archive Phase-4 AGENTS.md

Lock Phase-4 code except bug fixes

Phase 4 Completion Criteria
Phase 4 is complete when:

Persistence is measurable

Selection pressure is continuous and physical

Competition emerges without thresholds

Neutrality preserved

Phase-3 tests still pass

Phase-4 tests pass

No semantics appear

One-Line Phase-4 Rule
Phase 4 lets structure compete, but never choose.