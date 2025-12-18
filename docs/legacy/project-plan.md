# ALM Project Understanding and Execution Plan

## What this project is about
- Build an **Analog Language Model (ALM)**: a cache-resident, branchless, SIMD-first semantic substrate where meaning is the residual of interaction, not discrete tokens.【F:Foundational Background Theory Report.md†L1-L44】【F:source material/Foundational Background Theory.md†L1-L80】
- Preserve **spiral dynamics**: trajectories that tighten/loosen under pressure so memory emerges from survivability, not storage or loss minimization.【F:source material/The Spiral Concept in ALM.md†L1-L140】
- Separate **where** from **how**: a 10×10 spatial lattice chosen for L2 safety, with 12×12 chromatic relations encoded in SIMD lane algebra and coefficients—not in geometry.【F:source material/ALM bullet point.md†L33-L120】【F:source material/10x10_Substrate_12x12_Relational_Model.md†L1-L90】
- Align with **hardware physics**: dual-frequency updates, paired lanes, deterministic AVX2 paths, and non-coupled observability to prove scalar↔vector equivalence and stability under overwrite pressure.【F:Foundational Background Theory Report.md†L47-L96】【F:source material/Foundational Background Theory.md†L120-L210】

## Current materials (quick map)
- Theory & intent: Foundational Background Theory (report + long form), Spiral Concept, 10×10 vs 12×12 resolution, ALM v0.2 bullet plan.
- Implementation guardrails: cache budget (\<256 KB), 4-slice time stencil (Stable/Recent/Now/Future), paired-lane invariants, branchless pressure laws, dual-frequency envelope/beat handling.
<<<<<<< ours
- Adjacent references: DASE operations manual (CLI-driven dual-engine sim platform) and chromatic-cognition analyses (audio/CPWP prototypes); useful for tooling patterns but not core ALM substrate.
=======
- External simulator & analysis hooks: DASE headless CLI (NDJSON mission files), IGSOA/Phase4B engines, Python/C++ APIs, and bundled validation scripts (FFT, drift checks, R_c scaling) for physics-style inspection of ALM kernels.【F:source material/DASE_OPERATIONS_MANUAL.md†L1-L120】【F:source material/DASE_OPERATIONS_MANUAL.md†L120-L240】
- Adjacent references: chromatic-cognition analyses (audio/CPWP prototypes); useful for tooling patterns but not core ALM substrate.
>>>>>>> theirs

## Plan to move forward
1. **Ground the substrate**
   - Define the aligned `TensorCluster`/cell layout (10×10×4 registers×32 lanes, alignas(128/32)) and memory footprint budget; document cache residency assumptions.
   - Implement the 4-slice time stencil with rotation bookkeeping and isolation (no temporal teleportation).
2. **Lane algebra & coefficients**
   - Encode 12-hue/12-tone relations in lane-group coefficients; reserve auxiliary lanes for cross/pressure/stability terms.
   - Formalize paired-lane symmetry checks (even/odd or paired indices) and mask-based blends to keep updates branchless.
3. **Relational update kernel**
   - Write scalar reference kernel for differential/residual updates (only differences persist; balanced cancellation = neutrality).
   - Implement AVX2 path with matched math, dual-frequency components (fast interaction, slow persistence/decay), and residual accumulation; prove scalar ↔ AVX2 parity on fixed seeds.
4. **Pressure, decay, and overwrite resistance**
   - Model baseline decay + pressure-scaled decay; add overwrite pressure tests (future-biased writes stressing stability).
   - Include bandwidth pressure by capping representational energy and letting competition drive suppression.
5. **Spiral observability (non-coupled)**
   - Expose metrics for residual energy, symmetry deviation, radial drift, angular velocity/curvature, persistence half-life—collected in side channels that do not affect evolution.
   - Add diagnostic harness to confirm neutrality when inputs are symmetric and graceful degradation under noise.
6. **Validation harness**
   - Build regression tests: symmetry preservation, overwrite/pressure survival, neutrality smoke, slice-rotation integrity, scalar vs AVX2 equivalence, dual-frequency envelope/beat formation.
   - Profile hot loops for cache residency and branchlessness; confirm lane pairing invariants and deterministic outputs on target hardware assumptions.
<<<<<<< ours
=======
   - Mirror DASE-style checks where applicable: FFT-based spectral purity for stable modes, drift/energy stability under null pressure, and scaling behavior under higher interaction radius/pressure analogs.
>>>>>>> theirs
7. **Integration trajectory**
   - After substrate proof, layer modality adapters (audio/visual streams as continuous fields), routing via authority/pressure fields, and spiral-centric memory probes; keep discrete outputs downstream-only.

## Outputs to produce while executing
- Aligned substrate header/impl, coefficient tables, scalar + AVX2 kernels, time-stencil rotation logic.
- Test/diagnostic suite and perf probes.
- Brief design notes tying invariants back to the theory (why each constraint exists) to prevent drift.
