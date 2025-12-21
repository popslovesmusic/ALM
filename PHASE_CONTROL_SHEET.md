ALM — Phase Control Sheet (One-Page)
GLOBAL RULES (Always in Force)
Governance order:
agents.md → agents_plan.md → directory markers → user instruction → blueprints

Only canonical execution paths may evolve state.

All non-canonical paths are frozen unless governance changes.

Phase advances only when explicitly authorized.

Phase advance command: “Next.”

Every phase must end with LOC metrics.

DIRECTORY PLACEMENT RULES
Canonical (Writable Only in Active Phase)
bash
Copy code
alm/core/
Markers:

java
Copy code
CANONICAL_EXECUTION
FROZEN_NO_EDITS   (removed only when phase opens)
Reference / Non-Canonical (Read-Only)
bash
Copy code
src/alm/
tests/
Markers:

nginx
Copy code
REFERENCE_ONLY
FROZEN_NO_EDITS
Documentation (Read-Only)
Copy code
docs/
Marker:

nginx
Copy code
FROZEN_NO_EDITS
If unsure where a file belongs → treat as non-canonical.

PHASE DEFINITIONS (Agent-Executable)
Each phase:

modifies only alm/core/

touches only phase-relevant files

ends with LOC metrics report

Phase 0 — Authority & Structure ✅
Allowed

Governance files

Marker files

Directory moves (no content edits)

Exit Report

Authority established (yes/no)

Canonical paths

Frozen zones

LOC: added / modified / deleted / net

Phase 1 — State Geometry & Time
Allowed

State structures

Time / stencil advancement

Initialization

Placement

bash
Copy code
alm/core/
Exit Report

State defined (yes/no)

Time advance defined (yes/no)

LOC metrics

Phase 2 — Coefficients & Parameters
Allowed

Canonical coefficient tables

Immutability enforcement

Validation logic

Placement

bash
Copy code
alm/core/
Exit Report

Coefficients locked (yes/no)

Mutation prevented (yes/no)

LOC metrics

Phase 3 — Topology & Ingest
Allowed

Static topology

Ingest pathways

Orthogonality enforcement

Placement

bash
Copy code
alm/core/
Exit Report

Topology static (yes/no)

Ingest gated (yes/no)

LOC metrics

Phase 4 — Relational Kernel (Scalar)
Allowed

Scalar kernel

Residual update logic

No SIMD, no optimization

Placement

bash
Copy code
alm/core/
Exit Report

Kernel callable (yes/no)

Invariants referenced (yes/no)

LOC metrics

Phase 5 — SIMD / Vector Kernel
Allowed

SIMD kernel

Scalar ↔ SIMD equivalence tests

Placement

bash
Copy code
alm/core/
Exit Report

Equivalence pass/fail

LOC metrics

Phase 6 — Boundary / Focus / Pressure
Allowed

Boundary conditioning

Focus transfer

Pressure modulation

Placement

bash
Copy code
alm/core/
Exit Report

Modulation present (yes/no)

Topology unchanged (yes/no)

LOC metrics

Phase 7 — Observability
Allowed

Read-only observables

Metrics extraction

Placement

bash
Copy code
alm/core/
Exit Report

Observables passive (yes/no)

LOC metrics

Phase 8 — Invariants & Compliance
Allowed

Invariant registry

Regression tests

Enforcement gates

Placement

bash
Copy code
alm/core/
Exit Report

Invariants enforced (yes/no)

Removal causes failure (yes/no)

LOC metrics

Phase 9 — Performance & Hardening
Allowed

Optimization

Profiling

Stress testing

Placement

bash
Copy code
alm/core/
Exit Report

Semantics preserved (yes/no)

LOC metrics

ADVANCEMENT PROTOCOL
User input required:

vbnet
Copy code
Next.
Agent response:

Execute exactly one phase

Respect placement rules

End with required report + LOC metrics

HARD STOPS (Any Phase)
Agent must STOP if:

Same file modified > 2×

< 50 LOC net change over 5 commits

No file add/remove/move occurs

Non-canonical path modified

END OF CONTROL SHEET