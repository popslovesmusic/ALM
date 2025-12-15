AGENTS.md — Phase 3: Operator Kernel + SIMD-Adaptive Execution
Mission
Implement Phase 3: the Physics Glue Operator Kernel and SIMD-adaptive execution envelope.

Phase 3 introduces:

a minimal, explicit operator set (continuous dynamics),

a kernel interface that updates the TensorCluster slice(s) without semantics,

runtime CPU SIMD capability detection and one-time dispatch to the best kernel (SSE/AVX/AVX2),

deterministic tests verifying correctness across scalar and SIMD implementations.

No meaning, no tokens, no language. This remains non-semantic ALM.

Non-Negotiable Constraints
Phase Boundaries
Phase 2 is frozen. Do not change TimeStencil semantics or metrics contracts unless a test proves a bug.

No new “lookahead” ring buffers or transport models.

ALM Constraints
No semantics: no symbol formation, parsing, classification, “tokenizer,” or meaning assignment.

No correction/regulation: do not add feedback loops that change behavior based on Phase-2 metrics.

Analog intent: implement continuous dynamics; discrete structure exists only as an execution strategy.

Performance/Engineering Constraints
Single dispatch: SIMD selection happens at init; do not branch inside the hot inner loop.

No heap allocation in the kernel.

Preserve TensorCluster alignment and L2 residency intent.

Kernel must operate on linear memory with predictable access.

Scope: What to Build
A) Define the Physics Glue Operator Set (Minimal)
Implement a first operator set that is:

stable

non-semantic

composable

easy to validate

Required operators (start here):

Decay / Damping
x := x * (1 - d) (per lane coefficient allowed)

Coupling / Mixing (linear)
x := x + Σ_j (C_ij * y_j) with a small fixed neighborhood or lane-local coupling matrix

Diffusion (spatial neighbor)
x[cell] := x[cell] + κ * (avg(neighbors) - x[cell])

Notes:

Coefficients are “physics parameters,” not semantics.

Keep matrices small and fixed-size for Phase 3.

B) Kernel Interface Contract
Create a kernel interface like:

Inputs:

pointer(s) to slice memory (e.g., now, future) from TensorCluster

immutable coefficients (decay, coupling weights, diffusion rate)

slice span metadata (cells, registers, lanes)

Output:

writes results into the designated output slice (usually future), destructively (no memset required)

Do not couple the kernel to TimeStencil directly. The kernel is pure compute.

C) SIMD Capability Detection (Runtime)
Implement a small module that determines:

CPU supports AVX2? (CPUID)

OS supports YMM state? (XGETBV / XCR0)

Select one implementation:

scalar fallback

SSE (optional)

AVX

AVX2 (target)

Use a function pointer or std::function set once at init.

D) SIMD Implementations
Implement at least:

scalar reference kernel (always exists, used for correctness tests)

AVX2 kernel (primary target)

Optional:

SSE/AVX kernels if you want broader coverage, but do not overbuild.

E) Correctness Tests
Add tests that:

run scalar kernel and AVX2 kernel on the same seeded input

compare outputs within a tolerance

validate:

deterministic results

invariants (no NaNs if coefficients are safe)

linear memory traversal (no out-of-bounds)

Do not build a benchmark framework yet.

Deliverables
Phase 3 is “complete enough to proceed” when:

Kernel interface exists

Scalar kernel passes correctness tests

AVX2 kernel matches scalar within tolerance

SIMD detection selects correct kernel on supported CPUs

Documentation exists for:

operator definitions

coefficient schema

dispatch rules

Phase 3 constraints

Required File Outputs (Suggested Locations)
alm/core/include/alm/core/simd_capabilities.hpp

alm/core/src/simd_capabilities.cpp

alm/core/include/alm/core/operators.hpp

alm/core/src/operators.cpp (if needed)

alm/core/include/alm/core/kernel.hpp

alm/core/src/kernel_scalar.cpp

alm/core/src/kernel_avx2.cpp

alm/core/tests/kernel_equivalence_test.cpp

active/canonical/PHASE_3_PLAN.md (short)

Post-Task Archiving Rule
After Phase 3 tasks are completed and committed:

archive this Phase-3 folder-specific AGENTS.md into archive/agents/AGENTS_PHASE3.md

replace it with a stub or remove it, to prevent scope drift.

Phase 3 Constraints Document (Create/Update)
Create active/canonical/PHASE_3_CONSTRAINTS.md with:

“No semantics / no correction”

“Single dispatch”

“Scalar truth, SIMD acceleration”

“Kernel operates on linear layout”

“R730 target, adaptive execution”

First Implementation Target (Recommended)
Start with the simplest kernel that still exercises SIMD:

decay + diffusion (no coupling matrix yet)

then add coupling once equivalence testing is stable

This reduces debugging surface area.