# **ALM Blueprint v1.0**

**Date:** December 18, 2025
**Status:** CANONICAL

# **Global rule set**

# This document is "Canonical" prime authority and the only source of governance for this project
# All documents other than those found in prime references are leagacy and historical and have no governence authority 
# This document is the current bluprint for ALM and will followed as such
# This document may be amended and changed 
# Any amendments or changes must be dated with local time stamp too
# The amendment or change with the most recent date/time is then the governence bluprint and must be followed 
# Any indecision or doubt flags a stop for clarification
# The **global rule set** (these) may not be changed

---

## 1. NOT/IS ANALYSIS

This section defines what the ALM system **IS** and **IS NOT**. All implementations, extensions, and interpretations **must conform** to these constraints.

### 1.1. System Ontology

*   **IS:** A continuous dynamical system, a semantic conditioning engine based on resonance and dissipation, deterministic, and constrained by hardware simultaneity (SIMD) and cache locality.
*   **IS NOT:** An algorithm, a symbolic reasoning system, a decision-making agent, a goal-directed system, or a control system.

### 1.2. Meaning

*   **IS:** A dynamical property corresponding to persistent relational energy, observable as coherence and survivability, distributed across state, and read-only.
*   **IS NOT:** A symbol, label, token, stored data, a metric of correctness, a reward, or the result of subtraction or evaluation.

### 1.3. Computation

*   **IS:** Lawful state evolution under fixed operators, continuous transformation, SIMD-uniform, branchless, and non-selective.
*   **IS NOT:** Optimization, search, minimization, maximization, or conditional execution based on state values.

### 1.4. Adaptation

*   **IS:** Emergent co-evolution of fast and slow dynamics, result of impedance matching and resonance, continuous and unguided, governed solely by decay and coupling constants.
*   **IS NOT:** Learning, training, parameter fitting, or weight updates based on performance.

### 1.5. Dissipation

*   **IS:** Dissipation of incompatible signal components, redistribution of energy according to lawful dynamics, and observable decay/persistence patterns.
*   **IS NOT:** Error computation, error correction, comparison against a target, corrective feedback, or loss minimization.

---

## 2. Core Invariants

These are the non-negotiable laws of the ALM. Violation of any invariant invalidates the system.

1.  **Meaning is Not Computed:** Meaning is a dynamical property that emerges from the system's evolution. It is never calculated, stored, or retrieved.
2.  **Meaning is Not Selected:** The system does not choose or select meanings. It only allows persistent relational modes to survive.
3.  **No Corrective Feedback:** The system does not use error signals or feedback loops to correct its state. Adaptation is through resonance and dissipation.
4.  **No Stored Memory:** Persistence is achieved through continuous circulation of energy in the system, not through storage in memory buffers.
5.  **Observability is Non-Coupled:** Observation of the system's state must not influence its evolution. All diagnostics are read-only.
6.  **SIMD is Ontology:** The SIMD architecture is a fundamental constraint, not an optimization. All operations must be uniform across all lanes.
7.  **Branchlessness is Law:** The system's evolution must be branchless to ensure continuous and lawful transformation of state.
8.  **Pressure is Orthogonal to Signal:** Pressure modulates the rates of change in the system but never becomes part of the signal itself.

---

## 3. Mechanics

### 3.1. Time Stencil Mechanics

Defined in `TIME_STENCIL_MECHANICS.md`.

*   **Structure:** Four slices (STABLE, RECENT, NOW, FUTURE) that are co-resident in memory.
*   **Rotation:** Slices rotate by index/pointer swap only. `STABLE ← RECENT ← NOW ← FUTURE ← cleared/decayed`. This is unconditional and global.
*   **Permissions:** `STABLE` and `RECENT` are read-only during kernel execution. `NOW` and `FUTURE` are writeable under strict constraints.
*   **FUTURE Slice:** A non-predictive, non-authoritative bias accumulator. It modulates future drift, but does not control or predict.

### 3.2. Relational Kernel Law

The core update loop of the ALM.

*   **Dual-Frequency Dynamics:** Each signal has a fast (angular/interaction) and a slow (radial/persistence) component.
*   **Residual-Based Update:** "Only the difference produced by interaction survives." The update is based on the residual between a mixed-field input and the current state.
*   **Symmetry by Construction:** The mathematical structure of the kernel (skew-symmetric rotation matrices, pair-symmetric coefficients) guarantees the preservation of symmetry.

### 3.3. Pressure & Decay Laws

Defined in `PRESSURE_AND_DECAY_LAWS.md`.

*   **Pressure as Rate Modulation:** Pressure (`P_ow`, `P_bw`) modulates the rates of decay and coupling. It does not alter the system's structure or logic.
*   **Orthogonality:** Pressure is an external field, orthogonal to the signal-carrying payload lanes.

### 3.4. Jitter-Focus Transfer

Defined in `JITTER_FOCUS_TRANSFER.md`.

*   **Jitter as Proprioception:** Temporal instability in data arrival (jitter) is a proprioceptive signal.
*   **Focus as Rate Modulation:** Jitter is transformed into a `Focus` scalar that modulates kernel sensitivity (e.g., neighbor coupling strength). It is not an "attention" mechanism.

### 3.5. AVX2 Kernel Rules

Defined in `AVX2_KERNEL_RULES.md`.

*   **SIMD is Ontology:** The rules enforce the principle that SIMD is not an optimization but the fundamental structure of the system.
*   **Whitelist/Blacklist of Intrinsics:** Only intrinsics that preserve lane uniformity are allowed. Intrinsics that introduce lane-dependent behavior, break fixed lane semantics, or introduce privilege are forbidden.

### 3.6. Cache Residency

Defined in `CACHE_RESIDENCY_PROOF.md`.

*   **L2 Residency as Law:** The entire active cognitive state must reside within the CPU's L2 cache (< 256 KB) to ensure deterministic, low-latency performance.
*   **Working Set:** The canonical working set is defined and its size is proven to be within the L2 cache limit.

---

## 4. Observability

*   **Read-Only Diagnostics:** Observables are for external, read-only diagnostics and must not feed back into the system's evolution.
*   **Spiral Observables:** The primary observables are related to the emergent spiral trajectories:
    *   **Angular Velocity (θ-dot):** Represents phase coherence and rotation.
    *   **Radial Drift (r-dot):** Represents persistence and memory depth.
*   **Meaning as an Observable:** Meaning is a measured property of the system (e.g., the coherence of a spiral), not a computed value.

---

## 5. Test Criteria & Implementation Guardrails

*   **Invariant Regression Tests:** A suite of tests (`INVARIANT_REGRESSION_TESTS.md`) to enforce the ontological invariants of the system. Failure is a hard-fail of the build.
*   **Scalar ↔ AVX2 Equivalence:** A test harness (`scalar ↔ AVX2 equivalence test harness .md`) to ensure the scalar and AVX2 implementations are numerically equivalent within a defined tolerance.
*   **Branch-Free Execution:** The kernel must be provably branch-free.
*   **Failure on Ontology Violation:** The system must be designed to fail if any of its core ontological principles are violated.

---

## Appendix A: Philosophy and Metaphor

This section contains non-canonical narrative, metaphors, and philosophical discussions for didactic purposes.

### The Spiral Concept

The spiral is the minimal structure that allows for both persistence and evolution. It is recurrent progression with drift.
*   **Time as Distance:** Time is encoded as the distance along the spiral.
*   **Memory as Persistence:** Memory is the radial persistence of a spiral.
*   **Adaptation as Shape Change:** Adaptation is the geometric deformation of the spiral's shape.

### Resonant Semantic Conditioning

The ALM can be understood as a resonant tank circuit.
*   **Meaning as Resonance:** Meaningful signals are those that resonate with the system's current state and persist.
*   **Dissipation as Filtering:** Noise and irrelevant signals are dissipated as they fail to find a resonant mode.

### SIMD as Ontology

The SIMD architecture is not an optimization; it is the ontological substrate of the system.
*   **Lanes as Relational Commitments:** Each lane is a relational commitment, not an independent data item.
*   **Branchlessness as a Law of Being:** Branching is forbidden because it violates the uniform application of the system's laws.