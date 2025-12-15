Phase 2 Constraints — Finite-Time Motion (Stencil-Only)
STATUS: CANONICAL (Phase-Scoped Constraint Law)
PHASE: 2
SCOPE: alm/core/*
GOVERNANCE: MGFTS
PURPOSE: Enforce correct implementation of time motion without transport abstractions.

1. Ontological Constraints (Non-Negotiable)
1.1 Finite Time Only
Time exists only as the 4-slice stencil defined in Phase 1.

No additional temporal buffers may be introduced.

No history, queue, or lookahead beyond the stencil is permitted.

1.2 Stencil Is the Buffer
The TensorCluster time slices are the only storage for temporal state.

Introducing any separate ingest buffer (ring, queue, FIFO, deque, etc.) is forbidden.

2. Forbidden Transport Abstractions (Hard Stop)
The following are explicitly forbidden in Phase 2:

Ring buffers

Circular buffers

Queues or FIFOs

“Frame” abstractions

Producer/consumer queues

Head-distance or occupancy-based logic

Windowing or batching concepts

If any of these appear → STOP and REPORT.

3. Time Progression Constraints
3.1 Pointer / Index Rotation Only
Time progression MUST be implemented by index or pointer rotation.

No memcpy, std::copy, or element-wise copying is permitted.

No implicit clearing of slices is permitted.

3.2 Fixed Stencil Cardinality
Exactly 4 slices must exist at all times.

Slice roles are operational, not semantic:

stable_history

recent_past

now

staged_future

No additional slices may be created.

4. Ingest Constraints (Free-Running Writes)
4.1 Direct Writes Only
Ingest writes directly into the currently designated staged_future slice.

Ingest MUST NOT write into any other slice.

4.2 No Synchronization Guarantee
Ingest and compute may be unsynchronized.

Partial writes, overwrites, and tearing are allowed.

4.3 No Clearing Policy
The staged_future slice MUST NOT be automatically cleared.

“Dirty” data is permitted and intentional.

5. Pressure / Jitter Constraints
5.1 Pressure Is Measured, Not Controlled
The system MUST measure write pressure.

The system MUST NOT attempt to eliminate pressure.

5.2 Required Metrics
At minimum, Phase 2 must expose:

write count since last rotation

rotation count

overwrite indication (boolean or count)

These metrics are observational only in Phase 2.

6. Behavior Constraints
6.1 No Cognition
No kernel math

No feature extraction

No FFT or transforms

No inference logic

No adaptation based on pressure

6.2 No Semantics
No naming of lanes, cells, or registers

No symbolic meaning

No categorization or tagging

7. Memory & Performance Constraints
7.1 Allocation
No heap allocation in hot paths.

All structures must be statically sized or stack-bound.

7.2 Cache Discipline
No expansion of TensorCluster size.

All new structures must be negligible compared to the core state.

8. Determinism Requirement (Testing Only)
A deterministic, single-threaded execution path MUST exist for testing.

Free-running behavior may be simulated, not required, in tests.

9. Phase Boundary Constraints
9.1 Phase Isolation
Phase 2 MUST NOT introduce any Phase 3 constructs.

SIMD intrinsics are forbidden.

Disk access is forbidden.

9.2 Stop Condition
Phase 2 ends when:

time rotation works

pressure metrics are correct

no ring buffer exists

Any further work requires explicit Phase 3 authorization.

10. Compliance Enforcement
Violations require STOP + REPORT.

No workaround or “temporary” violation is permitted.

Silence is preferred over assumption.

End of Phase 2 Constraints