AGENTS.md — ALM Phase 6 (Structural Projection Stub)
Mission
Implement a minimal, detachable Phase 6 stub whose sole purpose is to lock the structural boundary in code.

Phase 6 must:

expose relational structure hooks

remain purely observational

remain non-semantic

remain causally isolated

be optional and removable

This phase exists to prevent misuse, not to add capability.

Phase 6 Constraints (Hard, Override All)
P6-C0 Read-Only Absolute
Phase 6 may only read Phase-5 artifacts.

No mutation of Phase-5, Phase-4, or earlier state.

Enforced by const correctness and API design.

P6-C1 No Semantics
Forbidden:

labels

symbols

categories

naming

ranking

interpretation

“importance”

“meaning”

Allowed:

opaque identifiers

numeric relations

continuous measures

coordinate embeddings with no names

P6-C2 No Feedback
Phase 6 must not influence:

dynamics

parameters

persistence

selection

pressure

No callbacks.

No observers that modify state.

No write access upstream.

P6-C3 No Thresholds
Forbidden:

hard thresholds

if/else gating on values

boolean triggers

Allowed:

identity mappings

neutral placeholders

continuous passthrough values

P6-C4 No Disk Access
Phase 6 stub performs no persistence

No logging

No background activity

Disk is not involved at this stage

P6-C5 Detachability
Removing Phase-6 code must not:

break compilation

alter Phase-5 outputs

change test results

Phase 6 must be optional at link time.

P6-C6 Determinism
Given the same Phase-5 trace:

Phase-6 stub output must be identical

No randomness

No time dependence

Phase 6 Tasks (Stub Only)
Task 1 — Define Structural Projection Interface
Create a read-only interface that consumes Phase-5 event traces and produces a structural atlas.

Rules

Input is const

Output is a new value object

No side effects

Files

bash
Copy code
alm/phase6/include/alm/phase6/structural_projection.hpp
Task 2 — Implement Neutral / Identity Projection
Provide a minimal implementation that:

preserves event IDs

passes through intensity as a numeric field

assigns neutral coordinates (e.g. zeros)

does not compute relations yet

This implementation must be:

non-semantic

non-interpretive

non-learning

Files

bash
Copy code
alm/phase6/src/structural_projection.cpp
Task 3 — Add Boundary Test (Mandatory)
Add a test proving:

Phase-6 invocation does not mutate Phase-5 traces

Phase-6 output is deterministic

Phase-6 can be removed without breaking Phase-5

This test is more important than functionality.

Files

bash
Copy code
alm/phase6/tests/phase6_read_only_test.cpp
Task 4 — No Expansion Beyond Stub
Do not implement:

similarity

clustering

matching

storage

learning

metrics

visualization

Any such additions violate the mission.

Definition of Done (Phase 6 Stub)
Phase 6 stub is complete when:

Interface exists

Neutral implementation exists

Read-only behavior is enforced

Boundary test passes

No disk access exists

No semantics exist

Phase-5 tests remain unchanged

Phase-6 AGENTS.md is archived after completion

Post-Completion Action
After stub completion and commit:

Archive this file to:

bash
Copy code
archive/agents/AGENTS_PHASE6_STUB.md
Mark Phase 6 as:
“Stubbed — Structural Boundary Locked”

Do not expand Phase 6 without a new constraint review.

One-Line Rule (Phase 6 Stub)
Phase 6 exposes structure, not meaning, and exists to make misuse impossible.