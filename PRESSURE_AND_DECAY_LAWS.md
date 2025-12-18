---

# **PRESSURE\_AND\_DECAY\_LAWS.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED / BLOCKING  
**Scope:** ALM / DASE core kernel only

---

## **1\. Purpose**

This document defines the **only lawful role of pressure** in ALM:

Pressure modulates *rates*, never *structure*.

Pressure may:

* scale decay  
* scale coupling strength  
* bias survivability continuously

Pressure may **never**:

* select lanes  
* gate execution  
* flip signs  
* introduce thresholds  
* branch control flow  
* override kernel laws

Violation of any rule in this document constitutes an **ontology break**.

---

## **2\. Definitions**

### **2.1 Payload State (Protected)**

Payload state consists exclusively of SIMD lane vectors belonging to:  
\[  
R,;G,;B,;I  
\]

These lanes:

* carry semantic content  
* participate in residual computation  
* evolve under invariant kernel laws

Pressure must **never** be stored in these lanes.

---

### **2.2 Pressure Fields (Orthogonal)**

Pressure exists only as **external scalar or vector fields**, denoted:

* Overwrite pressure: (P\_{\\text{ow}}(c) \\ge 0\)  
* Bandwidth pressure: (P\_{\\text{bw}}(c) \\ge 0\)

Pressure may be:

* per-cell  
* per-slice  
* per-update

Pressure may **not** be:

* per-lane selectors  
* discrete states  
* boolean flags

---

### **2.3 Baseline Decay Constants**

Each register (k \\in {R,G,B,I}) has a baseline decay constant:  
\[  
\\lambda\_k \\in (0,1)  
\]

This is the decay rate **in the absence of pressure**.

---

## **3\. Law 1 — Pressure Is Rate Modulation Only**

Pressure modifies decay and coupling **multiplicatively**, never additively and never conditionally.

### **3.1 Effective Decay Law**

For each cell (c) and register (k):

# **\[**

# **\\lambda\_k^{\\text{eff}}(c)**

\\lambda\_k \\cdot  
\\left(  
1  
\+  
a\_{\\text{ow}},P\_{\\text{ow}}(c)  
\+  
a\_{\\text{bw}},P\_{\\text{bw}}(c)  
\\right)  
\]

Where:

* (a\_{\\text{ow}}, a\_{\\text{bw}} \\ge 0\) are fixed constants  
* Mapping is **continuous and monotone**

**Hard constraint:**  
\[  
\\lambda\_k^{\\text{eff}}(c) \< 1  
\]  
This must be enforced by coefficient choice, **not by clamping or branching**.

---

### **3.2 Slow-State Update (Canonical)**

For slow/persistence component (k\_s):

# **\[**

# **k\_s'(c)**

\\bigl(1 \- \\lambda\_k^{\\text{eff}}(c)\\bigr),k\_s(c)  
\+  
\\eta\_s,\\rho\!\\left(k\_f(c)\\right)  
\]

Where:

* (k\_f) is the fast component  
* (\\rho(\\cdot)) is an **even, smooth, branchless** function  
  (default: (\\rho(x)=x^2))

---

## **4\. Law 2 — Pressure May Bias Coupling Strength, Not Topology**

Pressure may scale how strongly a cell responds, but not *what* it responds to.

### **4.1 Effective Neighbor Coupling**

Given baseline neighbor coupling coefficient (\\beta\_k):

# **\[**

# **\\beta\_k^{\\text{eff}}(c)**

\\beta\_k \\cdot \\bigl(1 \+ b\_{\\text{bw}},P\_{\\text{bw}}(c)\\bigr)  
\]

Where:

* (b\_{\\text{bw}} \\ge 0\)  
* No neighbor inclusion/exclusion is permitted

**Forbidden:**

* pressure-dependent neighbor masks  
* pressure-dependent topology  
* pressure-dependent lane routing

---

## **5\. Law 3 — Pressure Must Never Gate Execution**

The kernel **must execute identically** regardless of pressure values.

### **5.1 Explicitly Forbidden Forms**

The following are **illegal**:

if (P\_ow \> threshold) { ... }  
if (P\_bw \== 0\) skip\_update();  
if (pressure\_flag) disable\_lane();

As well as:

* max/min clipping  
* ReLU-style dead zones  
* piecewise functions  
* step functions  
* sigmoid-as-gate usage

Pressure must appear **only as a multiplier inside arithmetic expressions**.

---

## **6\. Law 4 — Pressure Cannot Flip Polarity**

Pressure must not change sign relationships.

Formally, if paired lanes satisfy antisymmetry:  
\[  
x\[\\bar{\\ell}\] \= \-x\[\\ell\]  
\]

Then after pressure-modulated update:  
\[  
x'\[\\bar{\\ell}\] \= \-x'\[\\ell\]  
\]

This is guaranteed if:

* pressure scalars are non-negative  
* pressure is applied identically to paired lanes  
* no conditional logic exists

---

## **7\. Law 5 — Pressure Is Not an Objective**

Pressure must **never** be interpreted as:

* a goal  
* a reward  
* a loss  
* a score  
* a selector

Pressure has **no semantic meaning** inside the engine.  
It is a *physical constraint*, not a preference.

---

## **8\. Interaction With Other Subsystems**

### **8.1 With Jitter / Focus**

Pressure and jitter may interact **only through shared scaling**:

* jitter may modulate coefficients (a\_{\\text{ow}},a\_{\\text{bw}})  
* jitter may not enable/disable pressure paths

### **8.2 With Observability**

Pressure values may be logged, but:

* must not be written into OBS lanes  
* must not influence metrics except indirectly via state evolution

---

## **9\. Required Tests (Acceptance Gates)**

The following tests are **mandatory**:

1. **Continuity test**  
   Small changes in (P\_{\\text{ow}},P\_{\\text{bw}}) produce small changes in output.  
2. **Zero-pressure neutrality test**  
   Setting all pressures to zero yields baseline decay behavior.  
3. **Symmetry preservation test**  
   Antisymmetric initial state remains antisymmetric under pressure.  
4. **Scalar ↔ AVX2 equivalence under pressure**  
   Already partially satisfied by existing harness; must be retained.

Failure of any test \= violation of this spec.

---

## **10\. Summary (Non-Negotiable)**

* Pressure is **rate modulation**, not control  
* Pressure is **continuous**, not discrete  
* Pressure is **orthogonal** to payload  
* Pressure cannot branch, gate, or select  
* Pressure cannot encode intent

**If pressure ever “decides” something, the system is no longer ALM.**

---

## **11\. Status After This Document**

With this document complete:

* ❌ Pressure ambiguity → **RESOLVED**  
* ❌ Hidden control channels → **BLOCKED**  
* ❌ Threshold creep → **FORBIDDEN**  
* ❌ Objective leakage → **FORBIDDEN**

