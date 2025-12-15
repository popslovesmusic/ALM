AGENTS.md — ALM Phase 4 (Continuation)
Role
You are implementing Phase 4 of the ALM core:
Structural Persistence & Selection Pressure.

Phase 4 is pre-semantic and physics-only.

Absolute Constraints (Read First)
You MUST NOT:

introduce semantics, symbols, labels, or identifiers

introduce thresholds, branching, or if/else on data

introduce control loops, optimization, or “fixing”

modify Phase-3 operator semantics

modify TimeStencil rotation semantics

normalize, clamp, or gate values

promote persistence to state

You MAY:

measure continuous observables

apply smooth, continuous pressure

allow structures to decay, diffuse, or dominate naturally

record metrics passively

If unsure, do less.

Current State (Do Not Redo)
Completed:

Phase-3 residual dynamics (sealed)

SIMD adaptivity (sealed)

TimeStencil accessors (sealed)

Phase-4 PersistenceProbe (measurement only)

You must build on top of these, not replace them.

Phase 4 Tasks (Execute in Order)
Task 1 — Selection Pressure Operator
Objective
Introduce continuous physical pressure so structures compete without decisions.

Requirements
Branchless

Continuous (no thresholds)

Lane-pair preserving

Parameterized only by observables

No mutation of observables themselves

Allowed Mechanisms (Choose ≥1)
Crowding-modulated decay
(higher local energy → higher decay coefficient)

Diffusion flattening
(strong gradients spread, weak ones fade)

Smooth global activity normalization
(e.g. divide by 1 + α * total_energy)

Deliverables
swift
Copy code
alm/core/include/alm/core/selection_pressure.hpp
alm/core/src/selection_pressure.cpp
Include only:

pure functions

no side effects

no logging inside hot paths

Task 2 — Phase-4 Kernel Integration
Objective
Combine:

Phase-3 residual dynamics

Persistence observables

Selection pressure

Into a single Phase-4 tick.

Rules
Read from stable, recent, now

Write only to future

Preserve paired lanes

Preserve neutrality

No normalization

Branchless

Scalar + SIMD compatible

Deliverables
swift
Copy code
alm/core/include/alm/core/phase4_kernel.hpp
alm/core/src/phase4_kernel.cpp
Task 3 — Tests (Mandatory)
Test 1: Neutrality Preservation
Flat input

Paired symmetry

Output remains flat

bash
Copy code
alm/core/tests/phase4_neutrality_test.cpp
Test 2: Competition Smoke Test
Initialize two local structures

Allow system to evolve

Observe divergence in persistence

Do NOT assert a winner

Only assert:

no NaNs

dynamics occurred

invariants preserved

bash
Copy code
alm/core/tests/phase4_competition_smoke_test.cpp
Task 4 — Documentation Seal
When all tests pass, create:

bash
Copy code
active/canonical/PHASE_4_COMPLETE.md
Must include:

What Phase 4 adds

What Phase 4 explicitly does NOT do

Statement that system remains pre-semantic

Task 5 — Archival
After completion:

Archive this AGENTS.md to:

bash
Copy code
archive/agents/AGENTS_PHASE4.md
Remove or replace active AGENTS.md

This prevents drift.

Definition of Done (Strict)
Phase 4 is complete when:

Selection pressure exists

Competition emerges without thresholds

Persistence is measured, not asserted

Neutrality is preserved

Phase-3 tests still pass

Phase-4 tests pass

No semantics appear

AGENTS.md is archived

One-Line Rule
Phase 4 lets structure compete, but never decide.

Notes to Agent
If you feel the urge to:

classify

choose

stabilize

optimize

interpret

Stop. You are leaving Phase 4.