***agents_plan.md***
ALM Execution Plan (Governance-First, Phase-Gated)

Plan Scope
This plan governs order and enforcement, not explanation.

Advancement is determined by invariant satisfaction, not documentation volume.

Execution Note:
This plan defines phase order only.
Phase scope, permissions, placement, and exit metrics are defined exclusively in
PHASE_CONTROL_SHEET.md.

Phase 0 — Authority & Structure (Mandatory)
Goal: Eliminate ambiguity and prevent loops.

Deliverables:

canonical execution path declared

non-canonical paths identified

frozen zones defined

phase boundaries named

Exit Condition:

it is mechanically unambiguous where ALM state may evolve

attempts to evolve state elsewhere fail

No logic, math, or optimization allowed.

Phase 1 — State Geometry & Time
Goal: Establish state and temporal mechanics.

Deliverables:

state representation

time or stencil advancement mechanism

deterministic initialization

Exit Condition:

time advances only through declared mechanisms

removing time logic causes invariant failure

Phase 2 — Coefficients & Canonical Parameters
Goal: Lock numeric and structural constants.

Deliverables:

canonical coefficient tables

symmetry and normalization checks

read-only enforcement

Exit Condition:

any coefficient mutation causes failure

scalar and vector paths consume identical parameters

Phase 3 — Topology & Ingest
Goal: Define relational structure and external interaction.

Deliverables:

static topology

ingest pathways

orthogonality enforcement

Exit Condition:

topology cannot change at runtime

ingest cannot bypass declared entry points

Phase 4 — Relational Kernel (Scalar)
Goal: Implement the core law without optimization.

Deliverables:

scalar kernel

residual update logic

no branching or control flow

Exit Condition:

kernel invariants hold under stress

removing the kernel collapses behavior

Phase 5 — Vector / SIMD Kernel
Goal: Achieve law-equivalent parallel execution.

Deliverables:

SIMD kernel

equivalence tests

memory layout enforcement

Exit Condition:

scalar and SIMD paths are provably equivalent

any divergence fails immediately

Phase 6 — Boundary, Focus, Pressure
Goal: Introduce modulation without control.

Deliverables:

boundary conditioning

focus transfer

pressure modulation

Exit Condition:

modulation does not alter topology or control flow

removing this phase does not affect earlier phases

Phase 7 — Observability
Goal: Observe without influence.

Deliverables:

read-only observables

spiral metrics

diagnostics

Exit Condition:

observation does not affect state evolution

Phase 8 — Invariants & Compliance
Goal: Make correctness non-negotiable.

Deliverables:

invariant registry

regression tests

enforcement gates

Exit Condition:

removing any invariant causes failure

tests define existence, not quality

Phase 9 — Performance & Hardening
Goal: Optimize without semantic change.

Deliverables:

performance characterization

stress testing

cache and layout validation

Exit Condition:

optimization does not change meaning

removing optimizations preserves behavior

Final Rule
If a phase cannot be:

isolated

deleted

enforced

then it is not a phase and must be reworked.

