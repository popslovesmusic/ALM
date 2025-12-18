## Blueprint Revision — What Must Be Reflected (No More, No Less)

When you revise the blueprint, ensure the following are explicitly present and unambiguous. This is not a rewrite request—this is a verification checklist.

### 1\. Topology (Must Be Instantiable)

Confirm the blueprint now states, verbatim or equivalently:

* Neighbor degree is fixed: K \= 12  
* Neighbor sets are:  
  * static  
  * symmetric  
  * abstract (non-geometric)  
* Aggregation weights are uniform: 1/12  
* No rewiring, no adaptive weights, no topology mutation

If any of these are only implied, the agent layer will reopen them.  
---

### 2\. Ingest (Must Be Mechanically Checkable)

Ensure the blueprint includes:

* Fixed ingest cadence \= one frame per stencil step  
* Definition of a valid ingest frame:  
  * scalar-only  
  * no control/timing metadata  
* Explicit jitter bound:  
  * |Δt| ≤ 0.25 × Δt\_stencil  
* Explicit rejection behavior for violations

Avoid phrases like “typically,” “may,” or “expected to.”  
---

### 3\. Coefficients (Must Be Generatable)

The blueprint must now contain:

* The base sequence S explicitly  
* The family differentiation rules (α, β, Γ)  
* The normalization constant C \= 1  
* A clear statement that coefficients are:  
  * generated, not stored  
  * immutable at runtime

If the blueprint still says “see coefficient tables” without the generation rule, the closure is incomplete.  
---

### 4\. Time / Rotation (Must Be Numeric)

Confirm that:

* Rotation order is fixed  
* Rotation scalar ω is explicitly numeric (e.g., ω \= 1.0)  
* No free temporal scaling remains at runtime

---

### 5\. Residual Ambiguities Are Labeled Correctly

Items like:

* diagnostic storage retention  
* Φ realization

should be explicitly marked as non-kernel, non-blocking, so future agents do not attempt to “resolve” them.  
