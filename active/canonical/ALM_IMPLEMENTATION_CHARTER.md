# ALM v0.2 Implementation Charter

> STATUS: CANONICAL  
> SCOPE: ALM v0.2  
> PURPOSE: Freeze architectural doctrine and translate it into enforceable implementation constraints.

## 1. Scope and Intent

This charter defines the non-negotiable architectural commitments for **ALM v0.2** and the permitted degrees of freedom for implementation. It exists to prevent implementation convenience from reintroducing legacy assumptions (e.g., symbolic layers, object-centric tensors, or unbounded time).

ALM v0.2 is a **physics-first, relational, cache-resident** cognitive engine. Its core loop is defined by:
- a **finite time stencil** (explicitly bounded time),
- a **cache-bounded working set** (L2-resident state),
- **SIMD lanes as relational ontology** (relations are primary, not symbolic objects),
- **call-gated long-term memory** (disk may be queried, never initiates).

## 2. Canonical Sources

The following are authoritative for ALM v0.2. In the event of conflict, resolve in this order:

1. `active/canonical/SSOT alm.md`
2. `active/canonical/10x10_Substrate_12x12_Relational_Model.md`
3. `active/canonical/ALM bullet point.md`
4. `active/canonical/ALM PROJECT OVERVIEW.md`
5. `active/canonical/FINAL_IMPLEMENTATION_REPORT.md`
6. `active/canonical/ALM_COMPLETION_ANALYSIS.md`

This charter is **binding** and should be treated as part of the canonical spine.

## 3. Non-Negotiable Architectural Commitments

### 3.1 Finite Time Ontology
- Cognition exists only within a small, explicit time stencil.
- There is **no unbounded history** inside the cognitive core.
- Time progression is implemented via **index rotation / pointer swaps**, not copying.

### 3.2 SIMD Ontology (Relations, Not Objects)
- SIMD lanes represent **relations / interaction modes**, not “batched independent tensors.”
- All lanes execute the **same control flow**; lane differentiation is **parametric** (coefficients), not branching.

### 3.3 L2 Cache Residency
- The entire active cognitive state must fit within **private L2** with margin.
- L3 access is tolerated only for ancillary functions, never as a steady-state requirement of the cognitive loop.

### 3.4 Jitter as Proprioception
- Ingest and compute are **free-running** (asynchronous).
- Read/write drift is permitted and measured.
- “Bulldozer” behavior (bounded head-advance) is permitted as an explicit mechanism.
- The system must remain stable under drift; it must not rely on strict synchronization.

### 3.5 Storage and Retrieval (Call-Gated Long-Term Memory)
- Disk is permitted as **long-term memory** only under strict gating:
  - Disk **cannot initiate**.
  - Disk **cannot push**.
  - Disk influence occurs only via **explicit retrieval calls**, outside the hot loop.
- Retrieval returns **parameters / profiles / summaries**, not direct state resurrection.

### 3.6 No Symbolic Layers in the Core
- No tokens, phrase trees, narrative stacks, object graphs, or symbol formation modules exist in the ALM cognitive core.
- Legacy CTL artifacts remain archived and must not be linked into ALM execution.

## 4. Permitted Degrees of Freedom

The following may evolve without violating ALM v0.2, provided constraints are met:

- Coefficient sets and lane parameterization
- Neighborhood stencils and coupling weights (within bounded, stable operators)
- Sample rate / tick regime selection (as a stress-control parameter)
- Instrumentation and observation summaries (read-only to the core)
- Disk schemas for long-term storage (provided call-gated rules are preserved)

## 5. Forbidden Changes (Require a Version Bump)

Any of the following require ALM v0.3 (or later) and explicit re-chartering:

- Changing the finite-time stencil principle (e.g., adding unbounded history)
- Introducing symbolic or semantic memory layers into the core
- Reinterpreting SIMD lanes as mere batching, or adding lane-specific branching
- Making disk retrieval automatic / background / initiatory
- Requiring L3 or heap allocation in the steady-state core loop

## 6. Phase 0 Implementation Entry Criteria

Implementation may begin when both of the following exist and are committed:

- `active/canonical/ALM_IMPLEMENTATION_CHARTER.md` (this file)
- `alm/core/CONSTRAINTS.md` (enforceable engineering constraints)

## 7. Phase 0 Deliverables (Definition of Done)

- Charter and constraints are present and reviewed against canonical docs.
- Repository contains a minimal `alm/core/` skeleton with:
  - `include/`, `src/`, `tests/`
  - a placeholder `README.md`
- A lightweight smoke test exists that verifies:
  - compilation configuration
  - alignment and size checks compile (even before behavior exists)

---  

**End of Charter**
