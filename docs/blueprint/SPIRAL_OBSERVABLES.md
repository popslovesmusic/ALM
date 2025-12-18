---

# **SPIRAL\_OBSERVABLES.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED (definition-phase completion)  
**Scope:** ALM / DASE diagnostics & validation only

---

## **1\. Purpose**

This document defines **spiral observables** as **read-only diagnostics** derived from lawful state evolution.

Spirals are **evidence** of coherence, not mechanisms of control.

Spiral observables:

* must never influence kernel evolution  
* must never modulate coefficients  
* must never feed pressure, focus, or decay  
* must never branch execution

They exist to:

* verify ontology  
* detect coherence regimes  
* support visualization and debugging  
* provide regression targets

---

## **2\. Conceptual Basis (Non-Operational)**

Spirals arise from:

* paired-lane symmetry  
* dual-frequency (fast/slow) dynamics  
* bounded decay  
* local neighbor coupling

They are **emergent**, not imposed.

This document defines **how to measure**, not **how to cause**.

---

## **3\. Observable Domains**

Spiral observables are computed **per cell** and **per window**.

They are defined in a **polar decomposition** of lawful state evolution:

* **Angular component** → phase coherence  
* **Radial component** → persistence / memory depth

No additional state is introduced.

---

## **4\. Signal Sources (Allowed)**

Spiral observables may be computed from:

* payload registers: R, G, B, I  
* paired lanes (ℓ, \\bar{ℓ})  
* fast and slow components  
* time stencil slices (read-only)

They must not read:

* pressure fields  
* jitter or focus values  
* auxiliary OBS lanes (except to write results)

---

## **5\. Angular Observable (θ)**

### **5.1 Definition**

For a given register (k), cell (c), and lane pair ((\\ell, \\bar{\\ell})):

Define a phase proxy using the fast component:

# **\[**

# **\\theta\_{k,c,\\ell}(t)**

\\operatorname{atan2}\!\\left(  
x\_{k,f}(c,\\ell),  
x\_{k,f}(c,\\bar{\\ell})  
\\right)  
\]

This yields:  
\[  
\\theta \\in (-\\pi, \\pi\]  
\]

---

### **5.2 Aggregate Angular Velocity**

Over a window of (W) steps:

# **\[**

# **\\omega\_{k,c}**

\\frac{1}{W-1}  
\\sum\_{i=1}^{W-1}  
\\operatorname{unwrap}\!\\left(  
\\theta\_{k,c}(t\_i) \- \\theta\_{k,c}(t\_{i-1})  
\\right)  
\]

Properties:

* continuous  
* insensitive to amplitude scaling  
* invariant under uniform decay

---

### **5.3 Interpretation (Non-Causal)**

* (|\\omega| \\approx 0): static or incoherent regime  
* sustained (|\\omega| \> 0): spiral motion present  
* sign indicates handedness only (no semantics)

---

## **6\. Radial Observable (r)**

### **6.1 Definition**

Radial magnitude is derived from the **slow component**:

# **\[**

# **r\_{k,c}(t)**

\\sqrt{  
\\sum\_{\\ell \\in \\text{paired lanes}}  
x\_{k,s}(c,\\ell)^2  
}  
\]

This measures:

* accumulated persistence  
* memory depth  
* resistance to decay

---

### **6.2 Radial Drift**

Over window (W):

# **\[**

# **\\dot{r}\_{k,c}**

\\frac{r\_{k,c}(t\_W) \- r\_{k,c}(t\_0)}{W}  
\]

Properties:

* continuous  
* monotone under sustained input  
* bounded by decay law

---

## **7\. Spiral Coherence Index (Optional, Derived)**

A single scalar diagnostic may be computed:

# **\[**

# **S\_{k,c}**

|\\omega\_{k,c}| \\cdot r\_{k,c}  
\]

This is:

* **not** an objective  
* **not** a reward  
* **not** a trigger

It exists solely for **visualization and logging**.

---

## **8\. Windowing Rules**

* Window size (W) must be fixed at compile time or initialization  
* Default: (W \= 8\)  
* Overlapping windows allowed  
* No adaptive window sizing permitted

---

## **9\. Numerical Stability Constraints**

To ensure observables remain diagnostic only:

* All functions must be smooth  
* No division by instantaneous amplitudes  
* No thresholding  
* No clipping  
* No branching on observable values

---

## **10\. Storage & Access Rules**

### **10.1 Storage**

Spiral observables may be stored in:

* external diagnostic buffers  
* logging structures  
* visualization layers

They must **not** be stored in:

* payload registers  
* auxiliary lanes (except OBS as write-only mirrors)  
* pressure or focus structures

---

### **10.2 Access**

Kernel code must:

* never read spiral observables  
* never branch on spiral observables  
* never scale coefficients using spiral observables

---

## **11\. Required Tests (Acceptance Gates)**

### **11.1 Non-Interference Test**

* Run kernel with observables enabled  
* Run kernel with observables disabled  
* Outputs must be identical within tolerance

---

### **11.2 Decay Invariance Test**

* Uniformly scale decay rates  
* Spiral angular velocity unchanged  
* Radial magnitude scales smoothly

---

### **11.3 Symmetry Test**

* Paired-lane antisymmetry preserved  
* Spiral observables invariant under lane permutation

---

## **12\. Forbidden Uses (Explicit)**

The following are **illegal**:

* using spiral metrics to modulate pressure  
* using spiral metrics to change focus  
* using spiral metrics as a loss  
* using spiral metrics to select neighbors  
* using spiral metrics to trigger events

Any such usage violates **Pressure–Signal Orthogonality**.

---

## **13\. Relationship to Other Specs**

This document is subordinate to:

* RELATIONAL\_KERNEL\_LAW.md  
* TIME\_STENCIL\_MECHANICS.md  
* PRESSURE\_SIGNAL\_ORTHOGONALITY.md  
* INVARIANT\_REGRESSION\_TESTS.md

If conflict arises, **those documents override this one**.

---

## **14\. Summary (Non-Negotiable)**

* Spirals are **measured**, not enforced  
* Spiral metrics are **read-only**  
* Spiral metrics are **non-causal**  
* Spiral metrics exist for **evidence and diagnostics only**  
* Any feedback path from spiral → kernel is forbidden

**If a spiral can influence the engine, it is no longer a spiral — it is a controller.**

---

## **15\. Status After This Document**

With this document complete:

* ❌ Spiral ambiguity → **RESOLVED**  
* ❌ Hidden feedback loops → **BLOCKED**  
* ❌ Diagnostic misuse → **BLOCKED**  
* ❌ Ontology contamination → **BLOCKED**

---

