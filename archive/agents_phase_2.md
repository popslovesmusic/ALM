# AGENTS_PHASE_2.md

> STATUS: ACTIVE (when copied to alm/core/AGENTS.md)  
> PHASE: 2 — Finite-Time Motion (Stencil-Only, No Ring Buffer)  
> SCOPE: alm/core/  
> GOVERNANCE: MGFTS (Mandatory)  
> REVIEW GATE: REQUIRED BEFORE PUSH

This phase implements **time and ingest motion** inside the finite 4-slice stencil.
It explicitly rejects the ring-buffer/queue model.

The Phase 2 objective is to make **time move** and to allow **free-running write pressure**
into the staged future slice, with measurable **jitter/proprioception**.

No cognition kernel. No semantics. No disk. No AVX2.

---

## 0. Canonical Inputs (Read-Only, Must Obey)

Agents MUST obey in this order:

1. `active/canonical/ALM_IMPLEMENTATION_CHARTER.md`
2. `alm/core/constraints_phase_2.md`
3. `active/canonical/SSOT alm.md`
4. `active/canonical/10x10_Substrate_12x12_Relational_Model.md`

If any conflict or ambiguity exists: STOP and REPORT.

---

## 1. Phase Authorization (Hard Boundary)

The agent is authorized to implement **Phase 2 only**.

Phase 2 includes:
- slice index management (finite-time stencil)
- pointer rotation (time progression without copying)
- free-running ingest writes into `staged_future`
- measurement of write pressure / jitter metrics
- deterministic harness for testing

Phase 2 excludes:
- any ring buffer / queue
- any feature extraction or FFT/windowing
- any SIMD kernel work
- any disk persistence/retrieval
- any semantics or naming of lanes/cells beyond numeric indices

The agent MUST STOP at Phase 2 completion.

---

## 2. Core Concept (New Model — Read Carefully)

### 2.1 The Stencil IS the Buffer
There is **no separate transport buffer**.

The existing `TensorCluster` (Phase 1) holds exactly 4 time slices, and those slices are the
only temporal memory allowed inside the core.

### 2.2 Free-Running Writes Create "Pressure"
Ingest writes directly into the slice designated `staged_future`.
Compute reads from `now` and rotates slices at tick boundaries.

Ingest and compute are not synchronized. Collisions (“screen tearing”) are allowed and are treated as signal.

### 2.3 Jitter / Proprioception is Measured, Not Eliminated
We must measure:
- how much of `staged_future` was written since the last rotation
- how often overwrites occur
- whether ingest outpaces compute

These metrics are exported as numbers; they do not change behavior in Phase 2.

---

## 3. Directory / File Plan (Create Exactly)

Create or modify files only within `alm/core/`:

### 3.1 New headers / sources
- `alm/core/include/alm/core/time_stencil.hpp`
- `alm/core/src/time_stencil.cpp`

### 3.2 New tests
- `alm/core/tests/time_stencil_rotation_test.cpp`
- `alm/core/tests/staged_future_pressure_test.cpp`

### 3.3 Allowed edits
- You MAY add minimal declarations to `tensor_cluster.hpp` if required
  (e.g., helper constants), but MUST NOT introduce behavior or accessors.

---

## 4. Implementation Requirements

### 4.1 Define a TimeStencil Controller (No Semantics)
Implement a small controller struct/class, e.g.:

- `TimeStencil` (or `StencilController`)
- Holds:
  - `TensorCluster* cluster` (or reference)
  - 4 slice indices:
    - `i_stable`
    - `i_recent`
    - `i_now`
    - `i_future`

These indices are just numeric roles; no additional meaning is introduced.

### 4.2 Rotation Must Be Pointer/Index-Only (No Copying)
Implement:

- `rotate_once()`

Rotation rule:

- `stable ← recent`
- `recent ← now`
- `now ← future`
- `future ← old stable` (recycled)

No data copy. No memset. No “clear future.”

### 4.3 Staged Future Write Tracking (Pressure)
Implement a write-tracking mechanism that is:

- lock-free or minimal-atomic
- does not block compute
- does not allocate

Required counters (minimum):
- `future_write_epoch` (monotonic tick id or counter)
- `future_write_count` (how many write events since last rotate)
- `future_write_span` (optional: min/max index written)

At minimum, implement:
- `mark_future_write(n_values_written)` called by ingest
- rotation captures snapshot and resets counters for next epoch

### 4.4 Ingest Simulation (Phase 2 Only)
Implement a minimal ingest function that writes into `staged_future`:

- `ingest_write_future(float value, size_t count)` OR similar
- It writes into the *current* future slice's contiguous `data[]`

Rules:
- It may overwrite previously written values (allowed)
- It must update pressure counters
- It must not clear or initialize the future slice globally

In Phase 2, this ingest function is a test harness; it is not real device I/O.

### 4.5 Deterministic Tick Harness
Implement a deterministic function:

- `tick_compute()` which:
  - reads pressure counters
  - rotates the stencil
  - returns a small metric struct (for tests)

No kernel math. No semantics.

---

## 5. Tests (Mandatory)

### 5.1 Rotation Correctness
Test that after one rotate:
- the previous `now` index becomes `recent`
- the previous `recent` becomes `stable`
- the previous `future` becomes `now`
- the recycled index is re-used as `future`

Test must confirm:
- indices form a permutation of {0,1,2,3}
- rotation repeats correctly over multiple ticks

### 5.2 Pressure Measurement
Test that:
- ingest writes increment write counters
- compute tick captures and resets counters
- pressure values are consistent across multiple cycles

### 5.3 No Illegal Constructs
Confirm by inspection/guardrails:
- no ring buffer types exist
- no queue
- no vector growth
- no disk I/O
- no SIMD intrinsics

---

## 6. Explicit Prohibitions (Hard Stops)

The agent MUST NOT:

- Implement a ring buffer, queue, circular sample buffer, or any head-distance system
- Create “frames,” “window sizes,” or “lookahead buffers”
- Add feature extraction (FFT, entropy scan, etc.)
- Add lane naming or semantic grouping
- Add accessors to TensorCluster
- Add `clear()` methods or future-slice initialization policies
- Add multithreading (optional later); tests must be deterministic
- Proceed to Phase 3 (SIMD kernel)

If any of these appear necessary, STOP and REPORT.

---

## 7. Review Gate (Do Not Push)

After producing a diff:

1. STOP.
2. Output:
   - list of files changed
   - a summary of rotation + pressure mechanisms
   - confirmation: “NO RING BUFFER IMPLEMENTED”
3. Await human review.

Do not push or merge until review is complete.

---

## 8. Completion Criteria (Definition of Done)

Phase 2 is complete when:

- TimeStencil controller exists
- Rotation works and is tested
- Staged-future pressure counters work and are tested
- No ring buffer exists anywhere
- No behavior beyond time motion + write tracking exists
- Agent stops after reporting outputs

---

## End of Phase 2 Instructions
