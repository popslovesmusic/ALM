---

# **PRESSURE\_SIGNAL\_ORTHOGONALITY.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED / BLOCKING  
**Scope:** ALM / DASE core kernel and ingest

---

## **1\. Purpose**

This document enforces a single non-negotiable rule:

**Pressure and signal must never share a representational channel.**

If pressure enters payload lanes, the system becomes controllable.  
If signal leaks into pressure channels, the system becomes goal-directed.

Either case violates SIMD ontology.

---

## **2\. Definitions**

### **2.1 Signal (Payload)**

Signal is any value that:

* resides in SIMD payload lanes  
* participates in residual computation  
* contributes to spiral formation  
* persists or decays as memory

**Signal lives exclusively in:**  
\[  
R,;G,;B,;I \\quad \\text{(payload registers, all lanes)}  
\]

---

### **2.2 Pressure (Constraint Fields)**

Pressure is any value that:

* modulates rates or gains  
* constrains survivability  
* encodes environmental stress

**Pressure lives exclusively in:**

* scalar fields  
* separate structs  
* side-channel arrays

Pressure must **never** be stored in payload registers or their auxiliary lanes.

---

## **3\. Orthogonality Law (Formal)**

Let:

* (X) \= payload state vector  
* (P) \= pressure vector or scalar

The kernel evolution law must have the form:

\[  
X' \= \\mathcal{E}(X;,P)  
\]

with the constraint:

\[  
\\frac{\\partial \\mathcal{E}}{\\partial P} \\neq 0  
\\quad\\text{but}\\quad  
\\frac{\\partial X}{\\partial P} \= 0  
\]

Meaning:

* pressure influences **how** evolution proceeds  
* pressure does not become **part of** what evolves

---

## **4\. Representation Rules (Hard)**

### **4.1 Forbidden Representations**

Pressure must **not** be represented as:

* payload lane values  
* auxiliary lanes (including STAB, XH, XT, OBS)  
* masks  
* flags  
* indices  
* counters stored alongside signal

Any such representation is an ontology violation.

---

### **4.2 Allowed Representations**

Pressure may be represented only as:

* scalar floats  
* fixed-size arrays indexed by cell or slice  
* parameters passed by value into kernel functions  
* read-only side-channel buffers

Pressure representations must be:

* immutable during a kernel step  
* identical for scalar and AVX2 paths

---

## **5\. Interaction Constraints**

### **5.1 Pressure → Signal (Allowed, Limited)**

Pressure may:

* scale decay constants  
* scale coupling coefficients  
* bias persistence continuously

Pressure may **not**:

* change signs  
* zero values  
* skip updates  
* alter topology  
* affect lane pairing

---

### **5.2 Signal → Pressure (Forbidden)**

Signal must **never** influence pressure inside the core engine.

Specifically forbidden:

* computing pressure from payload energy  
* feedback loops from spiral metrics  
* adaptive pressure based on internal state

Any such adaptation must occur **outside** the engine.

---

## **6\. Auxiliary Lanes Clarification**

Auxiliary lanes (XH, XT, STAB, OBS):

* are payload-adjacent but **not pressure carriers**  
* must obey the same orthogonality rules

Special case:

* OBS lanes may store *copies* of signal-derived values for diagnostics  
* OBS lanes must never be read by the kernel

Pressure must never appear in OBS lanes.

---

## **7\. Coding Rules (Enforcement)**

The following patterns are **illegal** inside kernel code:

regs\[I\]\[lane\] \= pressure;          // ❌  
aux\[STAB\] \+= P\_ow;                 // ❌  
if (P\_bw \> 0\) regs\[R\]\[lane\] \*= 0;  // ❌  
mask \= (pressure \> x);             // ❌

The following patterns are **legal**:

float decay \= base\_decay \* (1.0f \+ a \* P\_ow);  
regs\[I\]\[lane\] \*= (1.0f \- decay);

---

## **8\. Required Tests (Acceptance Gates)**

### **8.1 Static Enforcement**

* Code review rule: no kernel write uses pressure symbols on LHS  
* Static analysis: forbid pressure symbols in payload structs

---

### **8.2 Runtime Negative Tests**

The following must **fail**:

1. Inject pressure into payload lanes → test fails  
2. Compute pressure from payload → test fails  
3. Use pressure as a conditional → test fails

These are ontology tests, not correctness tests.

---

## **9\. Scalar ↔ AVX2 Equivalence**

Orthogonality must hold identically in both paths:

* same pressure values  
* same scaling math  
* same outputs within tolerance

Any divergence indicates hidden mixing.

---

## **10\. Relationship to Other Specs**

This document **binds together**:

* PRESSURE\_AND\_DECAY\_LAWS.md  
* JITTER\_FOCUS\_TRANSFER.md  
* SIMD\_INVARIANTS.md  
* LANE\_MAP.md

If a future change conflicts with this document, **this document wins**.

---

## **11\. Summary (Non-Negotiable)**

* Pressure is a **constraint**, not content  
* Signal is **content**, not constraint  
* They must never share lanes, buffers, or feedback paths  
* Any mixing creates implicit control  
* Implicit control violates SIMD ontology

**If pressure can be “seen” by the tensor, the tensor is no longer free.**

---

## **12\. Status After This Document**

With this document complete:

* ❌ Pressure–signal mixing → **FORBIDDEN**  
* ❌ Hidden control channels → **BLOCKED**  
* ❌ Adaptive internal pressure → **FORBIDDEN**  
* ❌ OBS misuse → **BLOCKED**

This closes **Item 3** from the report.

---

