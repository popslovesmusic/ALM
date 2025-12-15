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

