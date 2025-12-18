---

# **TIME\_STENCIL\_MECHANICS.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED (definition-phase completion)  
**Scope:** ALM / DASE core kernel temporal structure

---

## **1\. Purpose**

This document defines the **only lawful temporal structure** of the ALM engine.

Time in ALM is **thick**, **bounded**, and **non-predictive**.

The time stencil provides:

* temporal continuity  
* persistence without prediction  
* overwrite safety  
* deterministic cache-bounded evolution

Any deviation introduces hidden control or temporal leakage.

---

## **2\. Canonical Stencil Definition**

### **2.1 Slice Set (Fixed)**

The time stencil consists of **exactly four slices** per cell:

| Index | Name | Role |
| ----- | ----- | ----- |
| 0 | **STABLE** | Long-lived baseline |
| 1 | **RECENT** | Short-term persistence |
| 2 | **NOW** | Active computation target |
| 3 | **FUTURE** | Bias accumulator (non-predictive) |

This count is **fixed** in v0.1.

---

### **2.2 Memory Residency**

All four slices:

* are resident simultaneously  
* are equal in structure  
* contain full payload (R,G,B,I × 32 lanes)

They are stored contiguously in memory and rotate **by index**, not by allocation.

---

## **3\. Rotation Mechanics (Hard Law)**

### **3.1 Rotation Order**

At the end of each kernel step:

STABLE ← RECENT  
RECENT ← NOW  
NOW    ← FUTURE  
FUTURE ← cleared / decayed seed

This rotation is:

* unconditional  
* global  
* identical for scalar and AVX2 paths

No slice may skip rotation.

---

### **3.2 Implementation Rule**

Rotation must be implemented as **index rotation or pointer swap** only.

**Forbidden:**

* copying slice contents elementwise  
* conditional rotation  
* partial rotation

This preserves cache locality and determinism.

---

## **4\. Read / Write Permissions**

### **4.1 Read Permissions**

During a kernel step, the kernel may read:

| Slice | Read Allowed |
| ----- | ----- |
| STABLE | YES |
| RECENT | YES |
| NOW | YES |
| FUTURE | YES (read-only) |

Reading FUTURE is allowed **only as bias**, never as signal truth.

---

### **4.2 Write Permissions**

During a kernel step, the kernel may write:

| Slice | Write Allowed |
| ----- | ----- |
| STABLE | NO |
| RECENT | NO |
| NOW | YES |
| FUTURE | YES (restricted) |

STABLE and RECENT are **read-only snapshots**.

---

## **5\. FUTURE Slice Semantics (Critical)**

### **5.1 What FUTURE Is**

FUTURE is:

* an **accumulator of weak tendencies**  
* a **bias integrator**  
* a **pressure-weighted drift hint**

FUTURE is **not**:

* a prediction  
* a goal  
* a control signal  
* a planner

---

### **5.2 Allowed Writes to FUTURE**

Writes to FUTURE must satisfy:

\[  
FUTURE' \= (1 \- \\lambda\_f),FUTURE \+ \\eta\_f,\\Phi  
\]

Where:

* (\\Phi) is a lawful function of NOW, RECENT, STABLE  
* (\\lambda\_f) is a decay constant  
* (\\eta\_f) is small (≪ NOW update rate)

All writes are:

* continuous  
* symmetric across paired lanes  
* branchless

---

### **5.3 Forbidden FUTURE Behaviors**

The following are **illegal**:

* treating FUTURE as more important than NOW  
* conditional logic based on FUTURE  
* overwriting NOW from FUTURE  
* skipping decay in FUTURE  
* storing pressure directly in FUTURE

Any of the above converts bias into control.

---

## **6\. Overwrite Pressure Interaction**

Overwrite pressure (P\_{\\text{ow}}) interacts with the stencil **only through decay rates**.

### **6.1 Lawful Interaction**

Pressure may:

* increase decay into STABLE  
* accelerate forgetting in RECENT  
* damp FUTURE accumulation

Pressure may **not**:

* change rotation order  
* block rotation  
* select slices  
* redirect writes

---

## **7\. Temporal Consistency Invariants**

The following invariants must always hold:

### **7.1 No Time Travel**

Information may flow only:

STABLE → RECENT → NOW → FUTURE

Never in reverse.

---

### **7.2 Bounded Memory**

No information persists longer than:

* STABLE lifetime \+ decay

There is **no infinite memory channel**.

---

### **7.3 Scalar ↔ AVX2 Equivalence**

Temporal rotation and slice access must be:

* bit-identical  
* order-identical  
* testable

Any divergence is a failure.

---

## **8\. Cache Residency Compliance**

The stencil is dimensioned to preserve the cache proof:

* 4 slices × 100 cells × 512 B ≈ 200 KB

No additional slices may be added without:

* revising CACHE\_RESIDENCY\_PROOF.md  
* bumping version

---

## **9\. Required Tests (Acceptance Gates)**

### **9.1 Rotation Correctness Test**

* Run kernel for N steps  
* Verify slice identity rotates exactly every step

---

### **9.2 No Write-Through Test**

* Modify STABLE/RECENT in test harness  
* Run kernel  
* Verify no changes occurred

---

### **9.3 FUTURE Non-Control Test**

* Populate FUTURE with extreme values  
* Verify NOW evolution remains lawful and continuous

---

## **10\. Relationship to Other Specs**

This document is subordinate to:

* RELATIONAL\_KERNEL\_LAW.md  
* PRESSURE\_AND\_DECAY\_LAWS.md  
* PRESSURE\_SIGNAL\_ORTHOGONALITY.md  
* CACHE\_RESIDENCY\_PROOF.md

If a conflict arises, **those documents override this one**.

---

## **11\. Summary (Non-Negotiable)**

* Time is **four-sliced**  
* Rotation is **mandatory**  
* FUTURE is **bias, not control**  
* No slice may dominate  
* No slice may skip decay  
* No slice may branch execution

**If FUTURE ever “decides,” time has been broken.**

---

## **12\. Status After This Document**

With this document complete:

* ❌ Temporal ambiguity → **RESOLVED**  
* ❌ Hidden prediction → **BLOCKED**  
* ❌ Time-based control → **BLOCKED**  
* ❌ Cache creep via time → **BLOCKED**

---

