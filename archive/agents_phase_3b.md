AGENTS.md — ALM Phase 3: Physics Operators + SIMD-Adaptive Kernel
Mission
Begin Phase 3 by implementing the first physics glue operator kernel and a SIMD-adaptive execution envelope.

Phase 3 deliverables:

A scalar reference kernel (authoritative truth)

An AVX2 kernel (acceleration), selected via one-time runtime dispatch

A minimal operator set (decay + diffusion first; coupling later)

Deterministic equivalence tests between scalar and AVX2 outputs

Phase 3 documentation (“what exists now, what comes next”)

Phase 2 is sealed; do not change Phase 2 behavior except bug fixes with explicit justification.

Phase 3 Constraints (Non-Negotiable)
1) Phase Boundary Integrity
TimeStencil semantics and Phase-2 metrics contracts are frozen.

The recent atomic-index change is accepted; do not expand concurrency mechanisms further in Phase 3.

No new buffering models (no ring buffer transport abstractions).

2) No Semantics
Forbidden: symbols, tokens, labels, categories, meaning, parsing, “encoding/decoding,” “feature extraction.”
Only allowed: continuous operators (decay, diffusion, coupling) and observational metrics passthrough.

3) No Regulation / Correction
Do not clamp/repair because values are “bad.”
Do not branch based on Phase-2 pressure/jitter metrics.
Metrics remain read-only phenomenology.

4) Analog Intent, Digital Execution
Operators represent continuous dynamics. SIMD is an execution artifact.
If a performance change alters dynamics → reject.

5) Scalar Truth
A scalar kernel must exist and be correct.
SIMD kernels must match scalar output within tolerance.
If disagreement occurs: scalar is right; SIMD is wrong.

6) SIMD Single Dispatch
Detect CPU SIMD at init; choose kernel once via function pointer.
No SIMD-width branching in hot loops.

7) Linear Memory Traversal
Kernels must traverse TensorCluster::data linearly and predictably.
No pointer chasing, no indirect indexing, no dynamic lookup per cell.

8) No Allocation / No I/O in Kernels
No heap allocation, no logging, no disk I/O, no blocking, no locks inside kernels.

Implementation Plan (Do in this exact order)
Step 1 — Define Operator Parameters (Physics Glue)
Create:

alm/core/include/alm/core/operator_params.hpp

Define a small struct, example:

float decay; (0..1 small)

float diffusion; (>=0 small)

(no coupling yet in Step 1)

No semantics in naming. Treat as “coefficients.”

Step 2 — Define Kernel Interface (Pure Compute)
Create:

alm/core/include/alm/core/kernel.hpp

Define a callable signature that takes:

const float* now_slice

float* future_slice

std::size_t slice_span

OperatorParams params

Kernel writes future slice deterministically from now slice.

Do not integrate TimeStencil in the kernel.

Step 3 — Implement Scalar Reference Kernel
Create:

alm/core/src/kernel_scalar.cpp

Implement two operators only:

Decay:

y = x * (1.0f - params.decay)

Diffusion (simple 1D neighbor for Phase 3 start):

Treat the slice as a linear field:

neighbor_left = (i==0 ? x : x[i-1])

neighbor_right = (i==span-1 ? x : x[i+1])

lap = (neighbor_left + neighbor_right - 2*x)

y += params.diffusion * lap
This is intentionally simple and deterministic.

No branches based on values (only boundary handling).

Step 4 — SIMD Capability Detection + Dispatch (Init Only)
Create:

alm/core/include/alm/core/simd_caps.hpp

alm/core/src/simd_caps.cpp

Implement:

CPUID detection for AVX2 and FMA

XGETBV check for OSXSAVE/YMM state support

Expose:

enum class SimdLevel { Scalar, Avx2 }; (keep minimal)

SimdLevel detect_simd_level();

Create:

alm/core/src/kernel_dispatch.cpp
that returns a function pointer to the chosen kernel.

Step 5 — Implement AVX2 Kernel
Create:

alm/core/src/kernel_avx2.cpp

Implement the same decay+diffusion as scalar using AVX2 loads/stores:

operate on 8 floats at a time

handle tail safely (scalar tail loop)

Keep access linear:

load x[i..i+7]

load x[i-1..i+6] and x[i+1..i+8] (use unaligned loads if necessary; correctness first)

compute laplacian

store y[i..i+7]

Do not over-optimize. Do not introduce prefetch or unrolling until equivalence passes.

Step 6 — Equivalence Test (Scalar vs AVX2)
Create:

alm/core/tests/kernel_equivalence_test.cpp

Test plan:

Seed a deterministic input buffer with a fixed PRNG.

Run scalar kernel to produce future_scalar.

Run AVX2 kernel to produce future_avx2 (call directly, not via detection, to test it even on non-AVX2 hosts if compile-gated).

Compare element-wise with tolerance:

abs(a-b) <= 1e-5 or 1e-6 (choose one, document it)

Also assert no NaNs for safe params.

If host lacks AVX2, compile AVX2 kernel behind #if defined(__AVX2__) and skip equivalence with a clear message in test output.

Step 7 — Documentation
Create:

active/canonical/PHASE_3_PLAN.md

Include:

what operators exist (decay+diffusion)

kernel interface contract

scalar truth rule

SIMD dispatch rule

what is explicitly deferred (coupling, lane topology, disk memory, semantics)

Keep it 1–2 pages.

Build / Compilation Notes
Use C++20.

Ensure AVX2 file compiles with appropriate flags when enabled (e.g., -mavx2 -mfma) but keep the project building without AVX2 by guarding with macros.

Do not introduce external dependencies.

Definition of Done (Phase 3 Kickoff Complete)
This Phase 3 task is complete when:

scalar kernel exists and passes tests

AVX2 kernel exists and matches scalar within tolerance (when available)

runtime SIMD detection + one-time dispatch exists

Phase 3 plan doc exists

All new code is committed

Commit message:

Phase 3: scalar operator kernel + AVX2 dispatch + equivalence test

Post-Completion Archiving Rule
After this Phase-3 kickoff task is complete and committed:

Archive this AGENTS.md

Move to: archive/agents/AGENTS_PHASE3_KICKOFF.md

Replace the working directory AGENTS.md with either:

a minimal stub pointing to the archived file, or

remove it

This prevents scope drift and preserves history.