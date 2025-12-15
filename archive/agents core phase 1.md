# AGENTS.md

> STATUS: ACTIVE  
> PHASE: 1 — Core State Definition  
> SCOPE: alm/core/  
> GOVERNANCE: MGFTS (Mandatory)

This file authorizes **Phase 1 execution only** within `alm/core/`.

All global rules defined in the root `AGENTS.md` apply without exception.

---

## 1. Phase Authorization

The agent is authorized to perform **Phase 1 only**.

Phase 1 is defined as:
> *Definition and verification of the core ALM state layout, with no behavior.*

No other phase is active or implied.

---

## 2. Authorized Work (Explicit)

The agent MAY:

- Define the `TensorCluster` data structure
- Declare compile-time constants for:
  - time slices
  - spatial substrate size
  - register count
  - SIMD lane count
- Allocate a **single contiguous backing store**
- Enforce:
  - size constraints (< 256 KB)
  - alignment constraints (≥ 128 bytes)
- Create minimal test code that verifies:
  - size
  - alignment
  - trivial layout sanity

All work must remain within `alm/core/`.

---

## 3. Explicit Prohibitions (Hard Stops)

The agent MUST NOT:

- Add any behavior (including clearing, initialization logic, or iteration helpers)
- Add accessors, views, or semantic partitions
- Introduce symbolic names, enums, or abstractions
- Add time stepping, clocks, ring buffers, or indices
- Add SIMD math, kernels, or intrinsics
- Add disk I/O, persistence, or retrieval logic
- Modify canonical documents
- Modify or reference legacy or archived code
- Proceed to Phase 2 or beyond

If any of the above are required, the agent MUST STOP and REPORT.

---

## 4. Structural Requirements (Non-Negotiable)

The core state MUST satisfy:

- Spatial substrate: **10 × 10 = 100 cells**
- Registers per cell: **4**
- Time stencil: **4 slices**
- SIMD lanes: **32**
- Scalar type: `float`
- Layout: logically equivalent to  
  `[time_slice][cell][register][lane]`
- Memory:
  - contiguous
  - linearly traversable
  - cache-predictable

No semantic interpretation of these dimensions is permitted.

---

## 5. MGFTS Compliance Checks (Mandatory)

### 5.1 Phase Entry Check
Before acting, the agent MUST verify:
- Phase 1 is explicitly authorized (this file)
- No Phase 2+ artifacts exist in `alm/core/`

If not satisfied → STOP.

---

### 5.2 In-Phase Compliance
While executing:
- Ensure no forbidden constructs are introduced
- Ensure all changes remain structural only
- Ensure no semantic drift occurs

Violation → STOP + REPORT.

---

### 5.3 Phase Completion Check
Before declaring completion, the agent MUST verify:

- `TensorCluster` compiles
- `sizeof(TensorCluster) < 256 KB`
- `alignof(TensorCluster) ≥ 128`
- No behavior exists beyond storage
- No unauthorized files were modified

Only then may Phase 1 be declared complete.

---

## 6. Completion & Stop Condition

Upon successful completion, the agent MUST:

- Report:
  - exact byte size of `TensorCluster`
  - exact alignment
  - confirmation of MGFTS compliance
- STOP

The agent is **not authorized** to continue to any further phase.

---

## End of Phase 1 `alm/core/AGENTS.md`
