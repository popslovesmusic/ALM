# Phase 3 — Constraints (Non-Negotiable)

## 1\. Phase Boundary Integrity

* Phase 2 is frozen.  
* TimeStencil, its metrics, semantics, and tests must not be modified, except to fix demonstrable bugs with explicit justification.  
* Phase 3 may consume Phase-2 outputs but must not reinterpret or regulate them.

---

## 2\. No Semantics, Ever (Phase 3\)

Phase 3 introduces operators, not meaning.  
Forbidden in Phase 3:

* symbols  
* tokens  
* labels  
* categories  
* language constructs  
* interpretation logic  
* “feature extraction”  
* “encoding” or “decoding” steps

All math must be physics-plausible:

* decay  
* coupling  
* diffusion  
* damping  
* transport

If a variable sounds semantic, it does not belong here.  
---

## 3\. No Correction or Regulation

Phase 3 must not:

* suppress jitter  
* smooth pressure  
* clamp values because they are “bad”  
* retry failed operations  
* gate execution based on metrics  
* introduce thresholds that change behavior

Phase 3 computes.  
It does not decide.  
---

## 4\. Analog Intent, Digital Execution

* Operators represent continuous dynamics.  
* Digital structures (SIMD, loops, indices) are execution artifacts, not conceptual ones.  
* Discreteness exists only to satisfy hardware constraints.

If a design choice improves performance but changes dynamics → reject it.  
---

## 5\. Deterministic Scalar Truth

* A scalar reference kernel must exist.  
* SIMD kernels must match scalar output within tolerance.  
* SIMD is acceleration, not definition.

If scalar and SIMD disagree:

* scalar is authoritative  
* SIMD is wrong

---

## 6\. Single-Dispatch SIMD Selection

* SIMD capability detection occurs once at initialization.  
* Kernel selection is done via function pointer or equivalent.  
* No branching inside the hot loop based on SIMD width.

Runtime adaptivity must not introduce runtime divergence.  
---

## 7\. Linear Memory Traversal Only

* Kernels must traverse TensorCluster memory linearly.  
* No pointer chasing.  
* No indirect indexing.  
* No per-cell dynamic lookup.

The CPU prefetcher must always win.  
---

## 8\. No Allocation, No I/O in Kernels

* No heap allocation inside kernels.  
* No disk I/O.  
* No logging.  
* No mutexes or blocking calls.

Kernels are pure math over memory.  
---

## 9\. Reversibility and Dissolution

* Operators must be reversible in principle (e.g., decay can be undone by inverse parameters).  
* No structure introduced in Phase 3 may be permanent or irreversible.  
* Any accumulation must have a decay path.

If something cannot dissolve, it does not belong.  
---

## 10\. Locality of Effect

* Operators act locally:  
  * per lane  
  * per cell  
  * per neighborhood  
* No global state mutation.  
* No system-wide mode switches.

Emergence must arise from composition, not orchestration.  
---

## 11\. Metrics Are Read-Only Inputs

* Phase-2 metrics may be passed through Phase 3 unchanged.  
* Phase 3 must not branch, weight, or alter behavior based on those metrics.  
* Metrics remain phenomenological until a later phase.

---

## 12\. Hardware Targeting Rule

* Target performance assumptions: Dell R730 (AVX2).  
* Development systems may differ.  
* Kernel behavior must remain invariant across hardware; only throughput may change.

---

## 13\. Engineer’s Rule (Formalized)

* If an operator works and preserves constraints → keep it.  
* If it fails → remove it.  
* If analog and digital approaches are equivalent → analog intent wins.  
* If digital is strictly required to satisfy constraints → digital is permitted, scoped, and documented.

---

## 14\. Definition of “Done” for Any Phase-3 Change

A Phase-3 change is acceptable only if:

* it passes scalar correctness tests  
* it passes SIMD equivalence tests  
* it introduces no semantics  
* it introduces no control  
* it preserves Phase-2 invariants

If any condition fails → revert.  
---

### Final Constraint Sentence (Anchor)

Phase 3 implements continuous operator dynamics under measured constraint, using digital execution only as a substrate, never as an authority.

