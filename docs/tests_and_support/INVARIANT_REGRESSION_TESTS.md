

# **INVARIANT\_REGRESSION\_TESTS.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED / BLOCKING  
**Scope:** ALM / DASE core kernel, scalar \+ AVX2

---

## **1\. Purpose**

This document defines a **non-negotiable regression suite** that enforces:

* SIMD ontology  
* lane symmetry  
* pressure–signal orthogonality  
* continuity (no thresholds)  
* non-coupled observability

These tests are designed to **fail loudly** when ontology is violated, even if numerical outputs look “reasonable.”

---

## **2\. Test Classification**

All invariant tests fall into one of three classes:

1. **Preservation tests** – invariants must hold under lawful evolution  
2. **Equivalence tests** – scalar and SIMD must behave identically  
3. **Negative tests** – violations must be detected and rejected

All three are mandatory.

---

## **3\. Invariant 1: Uniform Law / No Lane Privilege**

### **3.1 Test: Lane Permutation Invariance**

**Setup**

* Initialize a state (X)  
* Create a permuted state (X') by swapping paired lanes consistently  
* Use identical coefficients and parameters

**Execution**

* Run one kernel step on both states  
* Un-permute the output of (X')

**Pass condition**  
\[  
\\text{output}(X) \\approx \\text{unpermute}(\\text{output}(X'))  
\]

**Failure indicates**

* per-lane branching  
* hidden lane indexing logic  
* accidental control flow

---

## **4\. Invariant 2: Paired-Lane Symmetry Preservation**

### **4.1 Test: Antisymmetry Preservation**

**Setup**

* Initialize all payload registers with:  
  \[  
  x\[\\bar{\\ell}\] \= \-x\[\\ell\]  
  \]  
* Zero pressure, zero jitter

**Execution**

* Run kernel step

**Pass condition**  
\[  
x'\[\\bar{\\ell}\] \\approx \-x'\[\\ell\]  
\\quad \\forall \\ell  
\]

**Failure indicates**

* sign flips  
* asymmetric coefficient tables  
* nonlinear gating

---

## **5\. Invariant 3: Earned Asymmetry Only**

### **5.1 Test: Neutral Input Neutrality**

**Setup**

* All cells identical  
* All neighbor states identical  
* All pressures \= 0

**Execution**

* Run kernel step

**Pass condition**

* No new structure emerges  
* Residual norm remains \~0  
* No spiral curvature appears

**Failure indicates**

* spontaneous symmetry breaking  
* injected meaning  
* numerical bias

---

## **6\. Invariant 4: Continuity (No Thresholds)**

### **6.1 Test: Small Perturbation Continuity**

**Setup**

* Baseline input (X)  
* Perturbed input (X \+ \\epsilon) with small (\\epsilon)

**Execution**

* Run kernel step on both

**Pass condition**  
\[  
|\\text{out}(X+\\epsilon) \- \\text{out}(X)| \= O(\\epsilon)  
\]

**Failure indicates**

* hidden thresholds  
* max/min clipping  
* conditional logic on values

---

## **7\. Invariant 5: Pressure–Signal Orthogonality**

### **7.1 Test: Pressure Injection Negative Test**

**Setup**

* Intentionally inject pressure values into payload lanes (test-only hack)

**Execution**

* Run kernel step

**Pass condition**

* Test framework flags violation  
* Execution aborts or test fails

**Failure indicates**

* pressure leakage is undetectable  
* ontology is unenforced

---

### **7.2 Test: Signal-to-Pressure Feedback Negative Test**

**Setup**

* Instrument kernel to compute pressure from payload (test-only)

**Execution**

* Run kernel step

**Pass condition**

* Test fails immediately

---

## **8\. Invariant 6: Non-Coupled Observability**

### **8.1 Test: OBS Lane Feedback Prohibition**

**Setup**

* Write arbitrary values into OBS lanes  
* Zero everything else

**Execution**

* Run kernel step

**Pass condition**

* Output identical to run with OBS lanes zeroed

**Failure indicates**

* observability contamination  
* hidden feedback path

---

## **9\. Invariant 7: Scalar ↔ AVX2 Ontology Equivalence**

### **9.1 Test: Randomized Equivalence (Required)**

This is satisfied by the existing harness, but **must be part of the invariant suite**, not optional.

**Pass condition**

* All registers, all lanes, all cells match within tolerance

**Failure indicates**

* SIMD path divergence  
* non-uniform law implementation

---

## **10\. Invariant 8: Auxiliary Lane Containment**

### **10.1 Test: Aux Isolation**

**Setup**

* Populate AUX lanes with large random values  
* Zero Hue/Tone lanes

**Execution**

* Run kernel step

**Pass condition**

* Hue/Tone evolution unchanged  
* Only AUX lanes decay or remain inert per spec

**Failure indicates**

* aux lanes acting as control channels

---

## **11\. Required Test Matrix**

Each invariant test must be run across:

| Dimension | Required |
| ----- | ----- |
| Scalar | YES |
| AVX2 | YES |
| Zero pressure | YES |
| Non-zero pressure | YES |
| Zero jitter | YES |
| Non-zero jitter | YES |
| Single cell | YES |
| Multi-cell grid | YES |

Skipping any axis is a spec violation.

---

## **12\. Failure Semantics**

Any invariant failure must:

* hard-fail CI  
* produce a minimal reproduction  
* print exact cell / register / lane indices  
* never be ignored or softened

No “warning-only” invariant failures are permitted.

---

## **13\. Relationship to Other Specs**

This document enforces:

* SIMD\_INVARIANTS.md  
* RELATIONAL\_KERNEL\_LAW.md  
* PRESSURE\_AND\_DECAY\_LAWS.md  
* JITTER\_FOCUS\_TRANSFER.md  
* PRESSURE\_SIGNAL\_ORTHOGONALITY.md  
* LANE\_MAP.md

If any implementation passes correctness tests but fails invariant tests, **the implementation is invalid**.

---

## **14\. Summary (Non-Negotiable)**

* Invariants are **laws**, not guidelines  
* Regression tests are **ontology enforcers**  
* Negative tests are mandatory  
* Silence is failure  
* Passing these tests means “still ALM”

**If you remove these tests, you are no longer building the same system.**

---

## **15\. Status After This Document**

With this document complete:

* ❌ Ontology drift → **BLOCKED**  
* ❌ Silent control injection → **BLOCKED**  
* ❌ Optimization betrayal → **BLOCKED**  
* ❌ SIMD misuse → **BLOCKED**

This closes **Item 4** from the report.

---

