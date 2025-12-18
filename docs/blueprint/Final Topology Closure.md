# A. Final Topology Closure

### A.1 Neighbor Degree

Declaration (Constitutional):  
r  
Copy code  
|N(c)| \= 12

Justification (Derived, not stylistic):

* ALM is mod-12 lane structured  
* Pairwise symmetry is already mod-6  
* Degree-12 preserves:  
  * rotational symmetry  
  * lane–neighbor homology  
  * cache-regular adjacency  
* Any other K introduces:  
  * lane/neighbor mismatch  
  * additional normalization rules  
  * unnecessary freedom

This choice collapses topology degrees of freedom to zero.  
---

### A.2 Neighbor Weighting

Declaration (Canonical):  
All neighbor contributions are uniformly weighted:  
ini  
Copy code  
w\_i \= 1 / K \= 1 / 12

Properties:

* Sum-normalized  
* Symmetry-preserving  
* No authority gradients  
* No hidden control channels

Forbidden:

* Learned weights  
* Distance-based weights  
* Adaptive scaling  
* Per-lane weighting

Aggregation is now fully specified.  
---

# B. Final Coefficient Closure

### B.1 Base Sequence

Declaration (Canonical):  
All coefficient families (α, β, Γ) are generated from the same base mod-12 signed sequence:  
ini  
Copy code  
S \= \[+1, 0, −1, 0, \+1, 0, −1, 0, \+1, 0, −1, 0\]

Properties:

* Mod-12 periodic  
* Zero-sum  
* Even/odd antisymmetric  
* Compatible with ⊕6 inversion  
* Minimal non-trivial sequence

No empirical meaning is attached.  
This is a structural seed, not data.  
---

### B.2 Normalization Constant

Declaration (Immutable):  
ini  
Copy code  
C \= 1

All coefficient tables are normalized such that:  
Copy code  
‖α‖₂ ≤ 1  
‖β‖₂ ≤ 1  
‖Γ‖₂ ≤ 1

with equality allowed only for α.  
Why this is safe:

* Unit normalization is scale-free  
* All dynamics already assume boundedness  
* Scaling later would be constitutional amendment, not tuning

---

### B.3 Family Differentiation Rule

Derived Rule (No New Freedom):

* α uses S directly  
* β uses S rotated by \+3  
* Γ uses S rotated by \+6 (sign-inverted pair)

This:

* Preserves orthogonality  
* Avoids identical dynamics across families  
* Introduces no new parameters

---

## 3\. Effect on the Readiness Verdict

With only the above declarations added:

### Blocking Issues Resolution

| Issue | Status |
| :---- | :---- |
| Neighbor degree undefined | CLOSED |
| Neighbor weighting undefined | CLOSED |
| Normalization constant missing | CLOSED |
| Coefficient instantiation ambiguous | CLOSED |

