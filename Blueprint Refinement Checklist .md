## Blueprint Refinement Checklist (Concise)

### 1\. Structure & Order

* Lead with NOT / IS analysis  
* Follow with core invariants  
* Present mechanics before philosophy  
* Move metaphors, analogies, and narrative to appendices  
* End with observables and test criteria

---

### 2\. Language Hardening

* Replace “learning” → co-evolution / resonance  
* Replace “error” → dissipation / mismatch  
* Replace “prediction” → future drift (non-authoritative)  
* Replace “memory” → persistence / circulation  
* Avoid agentic verbs (decide, choose, know, want)

---

### 3\. Ontology Enforcement

* Explicitly list non-negotiable invariants  
* Explicitly list forbidden constructs  
* Mark all tunable values as parameters, not logic  
* State that violation of invariants invalidates the system

---

### 4\. Mechanics Clarity

* Define one canonical core loop  
* Specify fast vs slow dynamics formally  
* State decay and coupling as laws, not heuristics  
* Make SIMD uniformity a hard requirement  
* Make cache locality a functional constraint

---

### 5\. Observability Discipline

* Define observables as read-only  
* Prohibit observables feeding back into evolution  
* Distinguish internal state vs diagnostic views  
* Define meaning only as a measured property, never computed

---

### 6\. Filtering & Loops

* Frame filtering as resonance \+ dissipation  
* Explicitly forbid thresholding and selection  
* Describe loops as oscillators, not feedback controllers  
* Prohibit corrective or regulatory semantics

---

### 7\. Time Semantics

* Clarify that FUTURE slice is non-predictive  
* State that no information travels backward in time  
* Emphasize local causality and present conditioning

---

### 8\. Implementation Guardrails

* Require scalar ↔ SIMD equivalence tests  
* Require branch-free kernel execution  
* Require invariant regression tests  
* Require failure on ontology violation

---

### 9\. Scope Control

* Explicitly state what the system does not attempt  
* Avoid comparisons to ML or AI in core sections  
* Defer extensions to separate documents  
* Freeze core concepts before coding begins

---

### 10\. Build Readiness

* Include one minimal reference instantiation  
* Include expected failure modes  
* Include acceptance criteria for “correct implementation”  
* Declare spec freeze point

