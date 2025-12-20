# ALM Compliance Map

This document links the canonical blueprint references to the implementation artifacts and regression coverage that enforce them. It is a living map for auditors to confirm traceability without reading the full codebase.

## Ingest, Topology, and Timing Guards
- **Blueprint references:** `TOPOLOGY & INGEST CONTRACT.md`, `TIME_STENCIL_MECHANICS.md`
- **Implementation artifacts:** `alm/core/include/alm/topology.hpp`, `alm/core/include/alm/ingest.hpp`
- **Regression coverage:** `tests/test_invariants.py` (topology closure), `tests/test_hardening.py` (blueprint checklist sections)

## Coefficient Canonicalization and Chromatic Structure
- **Blueprint references:** `COEFFICIENT CANONICALIZATION CONTRACT.md`, `ALM Lane Map and Coefficient Tables Spec v0.md`
- **Implementation artifacts:** `alm/core/include/alm/coefficients.hpp`, `alm/core/include/alm/constants.hpp`
- **Regression coverage:** `tests/test_invariants.py` (symmetry/normalization), `tests/test_performance.py` (residency literals tied to lane geometry)

## Deterministic Time Stencil and Kernel Equivalence
- **Blueprint references:** `TIME_STENCIL_MECHANICS.md`, `Relational Kernel Law Spec v0.md`, `AVX2_KERNEL_RULES.md`
- **Implementation artifacts:** `alm/core/include/alm/stencil.hpp`, `alm/core/include/alm/kernel.hpp`
- **Regression coverage:** `tests/test_invariants.py` (scalar/AVX2 equivalence), `tests/test_residency.py` (stencil payload sizing)

## Boundary Conditioning and Focus Orthogonality
- **Blueprint references:** `Resonant Semantic Conditioning via Dynamic Boundary Constraints.md`, `PRESSURE_SIGNAL_ORTHOGONALITY.md`, `JITTER_FOCUS_TRANSFER.md`
- **Implementation artifacts:** `alm/core/include/alm/boundary.hpp`, `alm/core/include/alm/focus.hpp`
- **Regression coverage:** `tests/test_invariants.py` (isolation and continuity helpers)

## Compile-Time Guardrails and Canonical Flags
- **Blueprint references:** `CACHE_RESIDENCY_PROOF.md`, `SIMD as Ontology.md`
- **Implementation artifacts:** `CMakeLists.txt`, `alm/core/CMakeLists.txt`, `alm/core/include/alm/build.hpp`, `alm/core/checks.cpp`
- **Regression coverage:** `tests/test_performance.py` (flag allowlist and architecture guards), `tests/test_residency.py` (cache budget headroom)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

## Toolchain and Architecture Enforcement
- **Blueprint references:** `AVX2_KERNEL_RULES.md`, `CACHE_RESIDENCY_PROOF.md`
- **Implementation artifacts:** `CMakeLists.txt`, `alm/core/CMakeLists.txt`, `alm/core/include/alm/build.hpp`, `alm/core/include/alm/config.hpp`, `alm/core/checks.cpp`
- **Regression coverage:** `tests/test_performance.py` (architecture and compiler hardening), `tests/test_hardening.py` (blueprint checklist enforcement)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
=======
>>>>>>> theirs

## Performance Residency and Intrinsic Allowlist
- **Blueprint references:** `CACHE_RESIDENCY_PROOF.md`, `SIMD as Ontology.md`, `AVX2_KERNEL_RULES.md`
- **Implementation artifacts:** `alm/core/include/alm/constants.hpp`, `alm/core/include/alm/performance.hpp`, `src/alm/performance.py`
- **Regression coverage:** `tests/test_performance.py` (intrinsic allowlist and compile-option enforcement), `tests/test_residency.py` (cache headroom validation)
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs

## Stress Resilience and Observability Traceability
- **Blueprint references:** `PRESSURE_AND_DECAY_LAWS.md`, `PRESSURE_SIGNAL_ORTHOGONALITY.md`, `JITTER_FOCUS_TRANSFER.md`, `SPIRAL_OBSERVABLES.md`
- **Implementation artifacts:** `alm/core/include/alm/ingest.hpp`, `alm/core/include/alm/focus.hpp`, `alm/core/include/alm/observability.hpp`, `src/alm/performance.py`
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
- **Regression coverage:** `tests/test_performance.py` (ingest cadence and focus stress compliance), `tests/test_invariants.py` (pressure orthogonality), `tests/test_compliance_docs.py` (compliance map traceability)
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
- **Regression coverage:** `tests/test_performance.py` (ingest cadence and focus stress compliance), `tests/test_invariants.py` (pressure orthogonality), `tests/test_stress_paths.py` (ingest/focus/observability guards), `tests/test_compliance_docs.py` (compliance map traceability)
>>>>>>> theirs
=======
- **Regression coverage:** `tests/test_performance.py` (ingest cadence and focus stress compliance), `tests/test_invariants.py` (pressure orthogonality), `tests/test_stress_paths.py` (ingest/focus/observability guards), `tests/test_compliance_docs.py` (compliance map traceability)
>>>>>>> theirs
=======
- **Regression coverage:** `tests/test_performance.py` (ingest cadence and focus stress compliance), `tests/test_invariants.py` (pressure orthogonality), `tests/test_stress_paths.py` (ingest/focus/observability guards), `tests/test_compliance_docs.py` (compliance map traceability)

## Invariant Regression and Readiness Compliance
- **Blueprint references:** `docs/tests_and_support/INVARIANT_REGRESSION_TESTS.md`, `docs/blueprint/Blueprint checklist.md`, `ALM_READINESS_REPORT.md`
- **Implementation artifacts:** `docs/tests_and_support/INVARIANT_REGRESSION_TESTS.md`, `docs/blueprint/Blueprint checklist.md`, `ALM_READINESS_REPORT.md`
- **Regression coverage:** `tests/test_invariants.py` (kernel/topology invariants), `tests/test_hardening.py` (checklist enforcement), `tests/test_compliance_docs.py` (compliance map traceability)
>>>>>>> theirs
