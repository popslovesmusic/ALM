# ALM Implementation Phased Plan

This plan breaks the ALM blueprint into small, buildable phases with traceability to the canonical references in `gemini.md`.

## Phase 1: Foundational Scaffolding
- Define data structures for the 10×10 grid and four registers (R, G, B, I) per cell, grouped into four AVX2 lane blocks (0–31) to respect the physical runtime envelope.
- Implement the four-slice stencil buffers (`FUTURE`, `NOW`, `RECENT`, `STABLE`) using pointer/index rotation—no copying—per the time structure contract.
- Add deterministic seed/config handling without dynamic tuning to align with coefficient canonicalization rules.

## Phase 2: Coefficient Canonicalization
- Ingest the canonical coefficient tables (`α, β, Γ`) and enforce symmetry (`q[ℓ̄] = q[ℓ]`), normalization, and exact lane/block mapping.
- Validate chromatic structure (12-hue/12-tone layout plus auxiliary lanes) at load time; fail fast on deviations.
- Prepare static, read-only coefficient buffers accessible to both scalar and AVX2 paths to ensure deterministic equivalence.
<<<<<<< ours
=======
- Define the FUTURE bias source term Φ as a deterministic function of NOW/RECENT/STABLE to prevent tuning drift while keeping rotation and decay laws intact.
>>>>>>> theirs

## Phase 3: Topology & Ingest Contract
- Implement the 12-neighbor symmetric topology with uniform weights and static closure; prohibit rewiring or per-lane specialization.
- Build ingest lanes that inject external signals only at the allowed entry points, orthogonal to pressure/persistence channels and synchronized with stencil advancement.
- Add configuration validation to prevent mid-step injections or hidden control metadata.

## Phase 4: Relational Kernel Core (Scalar Path)
- Implement the residual-based update (`Δ* = U* - k*`) with dual-frequency terms (fast angular, slow radial) and skew-symmetric coupling for spin without branching.
- Integrate uniform neighbor aggregation with the canonical coefficients and topology weights.
- Include pressure modulation and decay laws as multiplicative factors only—no control flow or gating.

## Phase 5: AVX2 SIMD Path
- Port the scalar kernel to AVX2 using only whitelisted intrinsics; avoid masking, reductions, gathers, shuffles, and branching to preserve simultaneity.
- Ensure payload fits within L2 cache per `CACHE_RESIDENCY_PROOF.md` (verify layout/stride and avoid spills).
- Add invariant checks to guarantee scalar and AVX2 outputs are deterministically equivalent per stencil step.

## Phase 6: Boundary Conditioning & Focus
- Implement resonant boundary responses without gates, clamps, or thresholds; verify behavior matches the boundary conditioning contract.
- Add focus handoff under jitter following prescribed transfer rules and maintaining orthogonality with pressure channels.
- Validate pressure orthogonality and absence of topology distortion during focus transitions.

## Phase 7: Observability & Instrumentation
- Provide passive observables that sample state without altering stencil rotation, pressure channels, or topology.
- Expose spiral observables (angular/radial trajectories) aligned with the dual-frequency dynamics.
- Add lightweight logging/telemetry hooks that remain read-only and cache-resident.
<<<<<<< ours
=======
- Specify diagnostic retention/durability policy for external observables so traces remain comparable across deployments while honoring the non-intrusive diagnostics contract.
>>>>>>> theirs

## Phase 8: Testing & Compliance
- Implement the invariant regression suite from `docs/tests_and_support/INVARIANT_REGRESSION_TESTS.md` to cover kernel laws, topology, timing, pressure, and scalar/AVX2 equivalence.
- Add readiness gating via the blueprint checklist before integration.
- Automate continuous verification to block violations of cache residency, topology closure, or coefficient canonicalization.

## Phase 9: Performance & Hardening
- Profile memory layout and instruction mix to confirm L2 residency and adherence to allowed AVX2 intrinsics.
- Stress test ingest cadence, pressure modulation, and focus transfer under jitter.
- Document compliance artifacts linking implementation components to the canonical references for traceability.
