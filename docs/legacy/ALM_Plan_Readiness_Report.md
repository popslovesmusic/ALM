# ALM Plan Readiness Review

## Summary of the existing plan
`ALM_Project_Analysis.md` delivers a strong philosophical synthesis (spiral dynamics, SIMD-as-ontology, L2 residency) and a phased roadmap covering substrate grounding through observability. It is directionally consistent with the theoretical sources.

## Gaps and conflicts against source documents
- **Merge conflicts in baseline plan docs:** `project-plan.md` and `Intended Usage of the DASE Engine.md` still contain conflict markers, leaving portions of the intent unresolved and blocking authoritative implementation guidance.
- **Missing ingestion and jitter specifics:** The analysis plan mentions an ingest ring but omits the concrete clock, frame, head, and bulldozer rules that govern proprioceptive focus mapping (215 kHz nominal clock, 256-sample frames, 8-frame ring, dual heads, forced advance on overrun, allowed tearing/loss). These are required to keep jitter-as-signal intact and to test overwrites under stress.
- **Underspecified SIMD invariants:** While symmetry and branchlessness are noted, the explicit invariants that define the ontology (uniform law, simultaneity, parametric differentiation only, no privileged lanes, earned asymmetry, non-coupled observability) are not yet captured as acceptance gates for kernel design.
- **Pressure and objective constraints:** The analysis reiterates “no objective function,” but the plan could add explicit checks that pressure never rides on the same lanes as signal and that decay/pressure modulation from jitter cannot gate or flip branch paths.
- **Cache-fit proof and profiling hooks:** The plan invokes L2 residency but lacks a concrete accounting/proof artifact (footprint math plus perf probes) to enforce the <256 KB law during implementation.

## Recommendations
1. **Resolve conflicted documents first** to establish canonical intent and external-tool references before coding (plan and DASE usage guides).
2. **Fold ingestion/jitter specs into the roadmap** as exit criteria for Phase 1, including clock, frame, ring, head behavior, bulldozer rule, allowed tearing, and focus_intensity mapping.
3. **Adopt the SIMD invariants as design gates** (uniform law, simultaneity, parametric differentiation, no privileged lane, earned asymmetry, continuity, non-coupled observability) and require each kernel/test to assert compliance.
4. **Add a cache-residency checklist**: document the TensorCluster size proof, stack/temporary budget, and perf counters to verify L2-only execution during validation.
5. **Keep pressure orthogonal to signal**: codify that overwrite/bandwidth/decay pressures live outside payload lanes and cannot branch, gate, or discretely select paths; jitter may scale decay/pressure but never flip signs or enable/disable kernels.

## Suggested augmented implementation path
- **Phase 0 (unblockers):** Resolve merge conflicts in `project-plan.md` and `Intended Usage of the DASE Engine.md`; restate canonical DASE/ALM boundaries.
- **Phase 1 (substrate + ingest):** Implement aligned TensorCluster with footprint proof; implement 4-slice rotation; implement ingest ring with 215 kHz/256-sample/8-frame defaults, dual heads, bulldozer advancement, and allowed tearing; expose distance→focus_intensity mapping.
- **Phase 2 (invariant-bound kernel):** Encode 12×12 lane coefficients; implement scalar reference and AVX2 kernels that explicitly prove uniform law, simultaneity, and earned asymmetry; prohibit per-lane branching.
- **Phase 3 (pressure/decay):** Integrate baseline and pressure-scaled decay; overwrite/bandwidth pressure paths that remain orthogonal to payload lanes; jitter-driven modulation without gating.
- **Phase 4 (observability and cache proof):** Add non-coupled metrics (residual energy, symmetry deviation, radial drift, angular velocity/curvature, persistence half-life) and perf probes verifying L2 residency/branchlessness.
- **Phase 5 (regression harness):** Tests for slice rotation, overwrite survival, symmetry neutrality, scalar↔AVX2 equivalence, dual-frequency spiral formation, bulldozer event distribution, and jitter-to-focus mapping stability.
