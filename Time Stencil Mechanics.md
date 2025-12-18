##  **Time Stencil Mechanics**

**Status:** 🟡 *Previously important / non-blocking* → 🟢 **Ready to finalize**

### **Why it was on the list**

The report identified ambiguity around:

* how many temporal slices exist  
* how rotation occurs  
* how future pressure interacts with overwrite

Without this, Phase-3+ cannot be deterministic.

### **Why it was deferred**

Time stencils depend on:

* pressure & decay laws  
* jitter/focus behavior  
* cache residency constraints

All of those are now fixed.

### **What the document must define (now unambiguous)**

**Document:**  
`TIME_STENCIL_MECHANICS.md`

**Scope:**

* Exact slice count (canonical \= 4\)  
* Rotation order (stable → recent → now → future)  
* Write rules (who may overwrite what)  
* Read rules (what slices kernel can see)  
* Overwrite pressure interaction  
* Future-bias semantics (non-predictive, non-control)

**What it will NOT define**

* learning  
* prediction  
* branching  
* priority  
* control

**Result when written**

* deterministic temporal thickness  
* no “hidden time travel”  
* cache proof remains valid

---

## **2\. Spiral Observables**

**Status:** 🟡 *Previously important / non-blocking* → 🟢 **Ready to finalize**

### **Why it was on the list**

The report flagged that spiral behavior:

* is central to ALM  
* but was only described qualitatively

That is acceptable for theory, not for diagnostics.

### **Why it was deferred**

Spiral observables depend on:

* paired-lane symmetry  
* dual-frequency dynamics  
* invariant enforcement

All are now locked.

### **What the document must define**

**Document:**  
`SPIRAL_OBSERVABLES.md`

**Scope:**

* angular phase integral (θ)  
* radial persistence integral (r)  
* windowing rules  
* noise tolerance  
* interpretation rules

**Hard boundary**

* observables are **read-only**  
* must never feed back  
* must never influence kernel state

**Result when written**

* spiral becomes measurable  
* regression-testable  
* visualizable  
* without becoming a control channel

---

## **3\. AVX2 Coding Rules**

**Status:** 🟡 *Previously important / non-blocking* → 🟢 **Ready to finalize**

### **Why it was on the list**

The report correctly identified that:

SIMD misuse is the \#1 silent ontology violation vector.

### **Why it was deferred**

AVX2 rules must align with:

* lane map  
* coefficient symmetry  
* cache residency  
* scalar↔SIMD equivalence tests

All are now fixed.

### **What the document must define**

**Document:**  
`AVX2_KERNEL_RULES.md`

**Scope:**

* allowed intrinsics  
* forbidden patterns  
* load/store discipline  
* register usage limits  
* alignment rules  
* no-branch guarantees

**Explicitly forbidden**

* lane-dependent branching  
* scalar reductions inside kernel  
* dynamic masks  
* gather/scatter  
* partial vector updates

**Result when written**

* future optimization cannot break ontology  
* reviewers have mechanical enforcement criteria  
* SIMD becomes a *law*, not an implementation detail

---

## **4\. Why These Are Now Safe to Write**

These three documents were **not missing** — they were **sequenced**.

They are now safe because:

| Dependency | Status |
| ----- | ----- |
| Kernel law | ✅ |
| Lane map & coefficients | ✅ |
| Pressure & decay | ✅ |
| Jitter → focus | ✅ |
| Orthogonality | ✅ |
| Invariants | ✅ |
| Cache residency | ✅ |

Nothing circular remains.

---

