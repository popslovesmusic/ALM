AGENTS.md — ALM Phase 5: Discrete Event Surfaces & Trace Persistence (Pre-Semantic)
Mission
Implement Phase 5: extraction of discrete, indexable event traces derived from Phase-4 structural dynamics, without introducing semantics, interpretation, or feedback.

Phase 5 outputs remain pre-semantic.
The system must not interpret events—only surface, record, and retrieve them as opaque traces.

Phase 5 Constraints (Hard, Override All Prior Guidance)
1) Phase Boundary Integrity
Do not modify Phase-4 kernel semantics, persistence probes, selection pressure logic, or tests.

Do not modify any files under alm/core.

Phase 5 is observer-only with respect to Phases 1–4.

2) No Semantics / No Labels
Forbidden:

symbols, tokens, categories

naming events (“this is X”)

classifiers or recognizers

linguistic or symbolic interpretation

pattern meaning attribution

Allowed:

opaque event IDs

event coordinates (time, location, intensity)

feature vectors with no names

3) Discrete Events Are Derivatives Only
Phase 5 may produce discrete events, but only as derivatives of continuous Phase-4 observables.

Events must arise from:

persistence

drift

coherence

energy gradients

Events must not be injected, invented, or hard-triggered.

4) No Thresholds
Forbidden:

hard thresholds

step functions

boolean gates

if/else branching on metric values

Allowed:

smooth, continuous onset functions

soft event intensity

probabilistic or graded emergence

5) No Feedback Into Core
Phase 5 must never:

influence Phase-4 parameters

alter decay, diffusion, or pressure

inject signals upstream

apply back-pressure

Phase 5 is read-only with respect to ALM core.

6) Disk Discipline (Strict)
Disk may act as long-term memory if and only if:

disk access is explicitly called

disk cannot initiate activity

disk cannot influence computation

no background writes

no autonomous retrieval

Disk participation must be auditable and testable.

7) Determinism
Given the same Phase-4 observable stream, Phase-5 must produce:

the same event trace (within defined numeric tolerance)

Phase 5 Work Plan (Do in This Order)
Step 1 — Event Surface Extraction (No Interpretation)
Create an EventExtractor that surfaces event candidates from Phase-4 observables.

Each event record may contain:

event ID (opaque)

timestamp

spatial index

intensity (continuous)

feature vector (unnamed)

No classification. No meaning.

Deliverables

bash
Copy code
alm/layer5/include/alm/layer5/event_extractor.hpp
alm/layer5/src/event_extractor.cpp
Step 2 — Event Trace Buffer (RAM Only)
Implement a bounded, append-only event trace ring for:

replay

audit

deterministic testing

No disk access here.

Deliverables

bash
Copy code
alm/layer5/include/alm/layer5/event_trace.hpp
alm/layer5/src/event_trace.cpp
Step 3 — Long-Term Storage Interface (Called-Only)
Implement a minimal disk interface:

Allowed calls:

store_trace(trace_chunk)

retrieve(query)

Forbidden:

background writes

implicit persistence

disk-driven triggers

Deliverables

bash
Copy code
alm/layer5/include/alm/layer5/long_term_memory.hpp
alm/layer5/src/long_term_memory.cpp
Step 4 — Phase 5 Tests (Proofs)
Add tests that prove:

No Feedback

Phase-5 cannot mutate any Phase-4 or earlier state.

Determinism

Same input → same event trace.

No Threshold Use

Static + runtime confirmation of smooth functions only.

Disk Discipline

Disk access occurs only through explicit calls.

Deliverables

bash
Copy code
alm/layer5/tests/event_determinism_test.cpp
alm/layer5/tests/disk_call_discipline_test.cpp
Step 5 — Minimal Documentation
Create:

bash
Copy code
active/canonical/PHASE_5_PLAN.md
Include:

what constitutes an “event”

what is explicitly forbidden

disk discipline rules

Phase 5 completion criteria

Definition of Done (Phase 5)
Phase 5 is complete when:

discrete events exist without semantics

event traces are reproducible

disk is used only when called

no feedback into core exists

Phase-4 tests still pass

Phase-5 tests pass

Phase-5 AGENTS.md is archived

Post-Completion Archiving Rule
After Phase 5 is complete and committed:

archive this AGENTS.md to
archive/agents/AGENTS_PHASE5.md

replace/remove active AGENTS.md to prevent drift

One-Line Rule (Phase 5)
Phase 5 may surface events, but it may not interpret them or influence physics.

