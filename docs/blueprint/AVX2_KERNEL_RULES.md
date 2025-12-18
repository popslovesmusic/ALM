

# **AVX2\_KERNEL\_RULES.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED (definition-phase completion)  
**Scope:** ALM / DASE core kernel (AVX2 implementation only)

---

## **1\. Purpose**

This document defines **mandatory coding rules** for AVX2 implementations of the ALM kernel.

SIMD is not an optimization layer in ALM.  
It is the **ontological substrate** that enforces simultaneity and uniform law.

Any AVX2 code that violates this document is **invalid**, even if numerically “correct.”

---

## **2\. SIMD Ontology Constraints (Hard)**

All AVX2 kernel code must satisfy:

1. **Uniform Law** — every lane executes the same operations  
2. **Simultaneity** — no lane is privileged or delayed  
3. **Continuity** — no thresholds, masks, or gating  
4. **Determinism** — scalar and AVX2 are equivalent  
5. **Boundedness** — no cache-breaking constructs

These are enforced mechanically by the rules below.

---

## **3\. Canonical Vector Geometry**

### **3.1 Vector Width**

* AVX2 vector width: **256 bits**  
* Element type: **float32**  
* Lanes per vector: **8**

### **3.2 Lane Block Mapping (Mandatory)**

The 32-lane payload is mapped as:

| Block | Lanes |
| ----- | ----- |
| 0 | 0–7 |
| 1 | 8–15 |
| 2 | 16–23 |
| 3 | 24–31 |

All kernel loops must iterate over **exactly 4 blocks** in this order.

---

## **4\. Allowed Instructions (Whitelist)**

Only the following AVX2 intrinsics are permitted inside the kernel:

### **4.1 Arithmetic**

* `_mm256_add_ps`  
* `_mm256_sub_ps`  
* `_mm256_mul_ps`  
* `_mm256_fmadd_ps` (if `-mfma` enabled)

### **4.2 Loads / Stores**

* `_mm256_load_ps`  
* `_mm256_store_ps`  
* `_mm256_loadu_ps` *(only if alignment cannot be guaranteed, documented)*

### **4.3 Constants**

* `_mm256_set1_ps`  
* `_mm256_setzero_ps`

These intrinsics preserve:

* lane independence  
* uniform execution  
* predictable latency

---

## **5\. Forbidden Instructions (Hard Prohibitions)**

The following are **explicitly forbidden** inside the kernel:

### **5.1 Control / Masking**

* `_mm256_cmp_ps`  
* `_mm256_blend_ps`  
* `_mm256_blendv_ps`  
* `_mm256_movemask_ps`  
* `_mm256_testz_ps`  
* `_mm256_and_ps`, `_mm256_or_ps`, `_mm256_xor_ps` *(except zeroing via setzero)*

**Reason:** introduces lane-dependent behavior or gating.

---

### **5.2 Data Movement**

* `_mm256_permute*`  
* `_mm256_shuffle*`  
* `_mm256_insert*`  
* `_mm256_extract*`  
* `_mm256_gather*`  
* `_mm256_scatter*`

**Reason:** breaks fixed lane semantics and cache predictability.

---

### **5.3 Reductions / Collapses**

* Horizontal adds  
* Horizontal max/min  
* Any scalar extraction used for control

**Reason:** violates simultaneity and introduces privileged lanes.

---

## **6\. Loop Structure Rules**

### **6.1 Fixed Iteration Counts**

Kernel loops must:

* iterate over known-constant bounds  
* never early-exit  
* never depend on data values

Example (legal):

for (int b \= 0; b \< 4; \++b) {  
  \_\_m256 x \= \_mm256\_load\_ps(ptr \+ b\*8);  
  ...  
}

Illegal:

if (\_mm256\_movemask\_ps(x)) { ... } // ❌

---

### **6.2 No Lane-Dependent Branching**

**Absolutely forbidden:**

* branching on SIMD results  
* branching on pressure/focus  
* branching on observables

All branching must occur:

* outside the kernel  
* on compile-time constants only

---

## **7\. Memory Rules**

### **7.1 Alignment**

* All payload vectors must be **32-byte aligned**  
* Prefer `alignas(32)` or stronger  
* Misaligned loads are allowed **only** if unavoidable and documented

### **7.2 No Dynamic Allocation**

Inside kernel execution:

* no `new`  
* no `malloc`  
* no STL containers  
* no heap access

Stack usage must remain bounded and small.

---

## **8\. Scalar ↔ AVX2 Equivalence (Mandatory)**

Every AVX2 kernel must have a **scalar reference implementation**.

### **8.1 Equivalence Requirements**

* identical arithmetic ordering per lane  
* identical coefficient usage  
* identical temporal rotation  
* tolerance-bounded numerical equality

Passing correctness tests but failing equivalence tests is **not acceptable**.

---

## **9\. Pressure, Focus, and SIMD**

Pressure and focus values:

* may appear only as scalar multipliers  
* must be broadcast via `_mm256_set1_ps`  
* must not affect control flow

Illegal:

if (focus \> 0.5f) { ... } // ❌

Legal:

\_\_m256 f \= \_mm256\_set1\_ps(focus);  
x \= \_mm256\_mul\_ps(x, f);

---

## **10\. Auxiliary Lane Handling**

Aux lanes (24–31):

* must be processed identically to other lanes  
* must not be masked out  
* must not be skipped

OBS lanes:

* may be written **after** kernel execution  
* must not be read inside kernel code

---

## **11\. Numerical Stability Rules**

* No clamping (`min`, `max`)  
* No absolute value for control  
* No normalization that depends on runtime magnitude  
* No division by state-derived values

All functions must be:

* polynomial  
* smooth  
* branchless

---

## **12\. Performance Invariants (Not Optional)**

AVX2 kernel code must:

* produce **zero branch mispredictions**  
* produce **no L3 accesses**  
* maintain **L2 residency**

Violating performance invariants violates ontology.

---

## **13\. Required Tests**

The following tests must pass for any AVX2 kernel:

1. Scalar ↔ AVX2 equivalence  
2. Lane permutation invariance  
3. Paired-lane antisymmetry preservation  
4. Pressure continuity  
5. OBS non-interference  
6. Cache residency verification

Failure of any test invalidates the implementation.

---

## **14\. Relationship to Other Specs**

This document enforces:

* LANE\_MAP.md  
* RELATIONAL\_KERNEL\_LAW.md  
* PRESSURE\_AND\_DECAY\_LAWS.md  
* PRESSURE\_SIGNAL\_ORTHOGONALITY.md  
* INVARIANT\_REGRESSION\_TESTS.md  
* CACHE\_RESIDENCY\_PROOF.md

If an optimization conflicts with any of these, **the optimization is illegal**.

---

## **15\. Summary (Non-Negotiable)**

* AVX2 is **law**, not acceleration  
* Every lane is equal  
* No lane may decide  
* No branch may observe state  
* No mask may suppress evolution  
* No shuffle may rewrite meaning

**If SIMD is treated as a trick, the system ceases to be ALM.**

---

## **16\. Definition-Phase Closure**

With this document complete:

* ❌ SIMD misuse → **BLOCKED**  
* ❌ Lane privilege → **BLOCKED**  
* ❌ Hidden control via intrinsics → **BLOCKED**  
* ❌ Optimization drift → **BLOCKED**

**All definition-phase documents are now complete.**

---

