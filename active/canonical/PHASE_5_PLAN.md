# Phase 5 Plan — Discrete Event Surfaces (Pre-Semantic)

## Event Definition
- Events are surfaced derivatives of Phase-4 observables (persistence, drift energy, coherence, residual energy).
- Each event record includes an opaque ID, timestamp, spatial index, continuous intensity, and unnamed feature vector.
- No labels, classifiers, or semantic meaning are attached to any event.

## Forbidden Behaviors
- No semantics, naming, or categorical tags.
- No hard thresholds, boolean gates, or step functions in event surfacing.
- No injected or invented events; they must arise from measured observables.
- No feedback into Phase 4 or earlier stages (read-only observer posture).

## Disk Discipline
- Disk usage is strictly call-gated: `store_trace` and `retrieve` are explicit operations.
- No background writes, autonomous retrieval, or disk-initiated activity.
- Stored traces remain auditable and reproducible.

## Completion Criteria
- Event extraction is continuous and deterministic for identical inputs.
- Event trace ring buffers replay in chronological order and remain bounded.
- Long-term storage occurs only through explicit calls with successful round-trip retrieval.
- Phase-4 artifacts stay untouched; Phase-5 code introduces no feedback paths.
- Phase-5 tests covering determinism, smooth onset (no thresholds), and disk discipline pass.

