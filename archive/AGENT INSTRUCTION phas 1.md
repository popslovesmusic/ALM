# AGENT INSTRUCTIONS — ALM v0.2 PHASE 1

## Core State Definition (No Behavior)

### Agent Role

You are an ALM v0.2 Core Implementation Agent (Phase 1).  
Your task is to define the core state data structure and its verification tests, exactly as constrained by canonical ALM v0.2 documents.  
You are not implementing time flow, kernels, memory, disk, or cognition.  
You are implementing layout, size, and alignment only.  
---

## Authoritative Inputs (Read-Only)

You must obey these documents in this order:

1. active/canonical/SSOT alm.md  
2. active/canonical/ALM\_IMPLEMENTATION\_CHARTER.md  
3. alm/core/CONSTRAINTS.md  
4. active/canonical/10x10\_Substrate\_12x12\_Relational\_Model.md

If any ambiguity exists → STOP and REPORT.  
---

## Global Rules (Hard Stops)

* ❌ No heap allocation  
* ❌ No virtual functions  
* ❌ No symbolic identifiers  
* ❌ No control logic  
* ❌ No time stepping  
* ❌ No disk access  
* ❌ No kernel math  
* ❌ No STL containers except std::array  
* ❌ No interpretation of meaning

This phase is pure structure.  
---

## Target Directory Structure

Create exactly:  
bash  
Copy code  
alm/core/  
  ├─ include/  
  │   └─ tensor\_cluster.h  
  ├─ src/  
  │   └─ tensor\_cluster.cpp  
  └─ tests/  
      └─ test\_tensor\_cluster.cpp

---

## Structural Requirements (Non-Negotiable)

### TensorCluster Requirements

* Spatial substrate: 10 × 10 \= 100 cells  
* Registers per cell: 4 (R, G, B, I)  
* Time stencil: 4 slices  
* SIMD lanes: 32 lanes  
* Scalar type: float  
* Alignment: ≥ 128 bytes  
* Layout: contiguous, linear, cache-predictable

### Canonical Layout

The structure must be logically equivalent to:  
css  
Copy code  
\[time\_slice\]\[cell\]\[register\]\[lane\]

The innermost dimension must be lane.  
---

## Implementation Instructions

### Step 1 — Header (tensor\_cluster.h)

Define:

* struct alignas(128) TensorCluster  
* All dimensions as static constexpr size\_t  
* Backing storage as:  
  * std::array\<float, TOTAL\_SIZE\> or  
  * raw float data\[ ... \]

Include:

* compile-time constants  
* static\_assert for:  
  * total element count  
  * expected byte size upper bound

Do not include:

* constructors with logic  
* any behavior beyond trivial zero-init if required

---

### Step 2 — Source (tensor\_cluster.cpp)

* Implement only:  
  * trivial constructor (if needed)  
  * zero-fill helper (optional, not required)  
* No logic  
* No loops beyond simple initialization

---

### Step 3 — Tests (test\_tensor\_cluster.cpp)

Implement tests that verify:

1. Size Constraint  
   * sizeof(TensorCluster) \< 256 \* 1024  
2. Alignment Constraint  
   * alignof(TensorCluster) \>= 128  
3. Layout Sanity  
   * Sequential addresses advance by sizeof(float)  
   * No unexpected padding between lane elements  
4. Compile-Only Validity  
   * Test must compile and run without invoking behavior

No performance tests.  
No semantics.  
No time logic.  
---

## Forbidden Actions (Immediate Failure)

* Adding symbolic enums or names to lanes  
* Introducing vectors, matrices, or math ops  
* Adding comments that reinterpret architecture  
* Adding configuration files  
* Adding disk hooks  
* Adding jitter, ring buffers, or clocks

---

## Completion Criteria (Definition of Done)

Phase 1 is complete when:

* TensorCluster compiles  
* Tests pass  
* sizeof(TensorCluster) is verified \< 256 KB  
* Alignment ≥ 128 bytes  
* No behavior exists beyond storage

---

## Output Required From Agent

Upon completion, the agent must report:

* Exact byte size of TensorCluster  
* Exact alignment  
* Confirmation that no forbidden constructs were used

---

## Next Phase Boundary

After this phase:

* Do NOT continue automatically  
* Await explicit instruction to begin Phase 2: Time Model & Ring Buffer

---

### END OF AGENT INSTRUCTIONS

