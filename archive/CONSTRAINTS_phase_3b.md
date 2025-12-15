# ALM v0.2 Core Constraints

> STATUS: CANONICAL (Implementation Constraint Sheet)  
> SCOPE: `alm/core/*`  
> PURPOSE: Hard, testable constraints for ALM v0.2 implementation.

## 1. Real-Time Core Rules

### 1.1 No Blocking
- No blocking syscalls in the hot loop (compute tick path).
- No mutex locks in the hot loop.
- No disk I/O in the hot loop.

### 1.2 No Allocation After Init
- No heap allocation (`new`, `malloc`, `std::vector` growth) on the hot path.
- Any required buffers must be preallocated during initialization.

### 1.3 Deterministic Control Flow
- No lane-dependent branching in the SIMD kernel.
- No per-lane “special cases” implemented via conditionals.

## 2. Memory and Cache Constraints

### 2.1 Working Set Size
- Active cognitive state **MUST** fit within private L2:
  - Target: <= 200 KB for primary state
  - Hard cap: < 256 KB for the state object(s) required each tick

### 2.2 Alignment
- Primary state structures used by SIMD loads/stores:
  - minimum: 64-byte alignment
  - target: 128-byte alignment for predictable prefetching

### 2.3 Layout
- State layout must be contiguous and linearly traversable.
- Inner-most dimension corresponds to lane batches suitable for AVX2 loads/stores.

## 3. Time Model Constraints

### 3.1 Time Stencil
- Time stencil is **exactly 4 slices**:
  - Stable History
  - Recent Past
  - Now
  - Staged Future

### 3.2 Time Progression
- Time advancement via index rotation (pointer swap), not memcpy.
- “Future” slice may be written destructively; no mandatory clearing step.

## 4. Spatial Substrate Constraints

### 4.1 Substrate Geometry
- Spatial substrate is **10×10** (100 cells) unless SSOT explicitly revises it.
- The substrate is **not** a chromatic basis; chromatic structure is relational.

### 4.2 Registers
- 4 registers per cell (R, G, B, I) as the default state channels.

## 5. SIMD Kernel Constraints (AVX2)

### 5.1 ISA
- AVX2 is required; FMA is permitted and preferred where available.
- Kernel must operate on 256-bit vectors (`__m256`) with aligned loads where feasible.

### 5.2 Inner Loop Discipline
- Pointer hoisting: compute base pointers outside innermost loops.
- Linear traversal: no random access in the kernel hot path.
- Avoid function calls in the hot loop (inline or static preferred).

### 5.3 Lane Semantics
- Lanes are relations (interaction modes).
- Lane differentiation via coefficient tables, not control flow.

## 6. Ingest / Jitter Constraints

### 6.1 Free-Running Model
- Ingest and compute threads may be asynchronous.
- Drift is allowed and must be measurable.

### 6.2 Bulldozer Bound
- If read head must be advanced, the advancement must be bounded.
- Under no circumstances may bulldozer logic advance beyond the maximum future window required for staged computations.

## 7. Disk Memory Constraints (Call-Gated)

### 7.1 Gating
- Disk memory must be pull-only:
  - No background retrieval that initiates changes.
  - Retrieval occurs only via explicit API calls.

### 7.2 Influence Surface
- Retrieval may adjust:
  - coefficients
  - thresholds
  - profiles / presets
- Retrieval may not:
  - overwrite live core state directly
  - restore historical time slices
  - block the hot loop

## 8. Mandatory Tests (Phase 1 Minimum)

The following must be testable in `alm/core/tests`:

- `sizeof(core_state) < 256 KB`
- alignment assertions compile and pass
- time stencil rotation correctness
- SIMD kernel compiles and runs without lane-branching (static analysis or review gate)
- no-allocation-in-hot-loop (instrumentation or code review checklist)

---  

**End of Constraints**
