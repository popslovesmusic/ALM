# PART I — TOPOLOGY & INGEST CONTRACT

ALM Topology and Ingest Contract v1.0 (Proposed Canonical)  
---

## 1\. Purpose

This contract defines the only admissible spatial coupling and external ingest rules for ALM kernels.  
Its role is to eliminate implementation discretion regarding:

* Neighbor definition  
* Signal entry  
* Temporal alignment  
* Authority flow

---

## 2\. Derived Constraints (Non-Negotiable)

The following are already enforced elsewhere in ALM and therefore constrain topology and ingest:

* Pressure channels must remain orthogonal to state evolution  
* No control, gating, or thresholding is permitted  
* Phase isolation is mandatory  
* Cache residency is bounded  
* Pairwise symmetry must be preserved  
* No observer feedback into kernel dynamics

These constraints are binding on all declarations below.  
---

## 3\. Topology Definition

### 3.1 Cell and Neighbor Set

Definition (Derived):  
Each ALM cell c maintains a fixed, finite neighbor set N(c) such that:

* |N(c)| \= K, where K is constant across all cells  
* Neighbor relationships are symmetric:  
* r  
* Copy code

cᵢ ∈ N(cⱼ) ⇔ cⱼ ∈ N(cᵢ)

*   
* Neighbor identity is static for the lifetime of the system

Forbidden (Derived):

* Dynamic rewiring  
* Distance-dependent weighting  
* Long-range shortcuts  
* Global routing tables

Rationale: dynamic or asymmetric topology introduces implicit authority flow and violates pressure orthogonality.  
---

### 3.2 Topological Regularity

Declaration (Constitutional Choice):  
Topology is locally regular and degree-bounded, but geometry is abstract.

* No embedding in physical space is assumed  
* Topology is defined purely by adjacency  
* All cells are topologically equivalent

This preserves symmetry while avoiding geometric bias.  
---

## 4\. Ingest Contract

### 4.1 External Signal Entry

Definition (Derived):  
External signals enter ALM only through designated ingest lanes, which:

* Are orthogonal to pressure and persistence channels  
* Do not modify kernel coefficients  
* Do not alter neighbor topology

---

### 4.2 Temporal Alignment

Definition (Derived):  
Ingest operates at a fixed cadence aligned to the ALM time stencil.

* Each ingest sample maps to exactly one stencil advancement  
* No mid-step injection is permitted

Forbidden:

* Event-driven injection  
* Asynchronous callbacks  
* Observer-triggered updates

---

### 4.3 Jitter Handling

Declaration (Minimal Sufficiency):

* Bounded jitter is absorbed into the existing time stencil smoothing rules  
* Jitter does not propagate as a state variable  
* Excess jitter beyond declared bounds is rejected upstream

This avoids introducing hidden state or adaptive timing control.  
---

## 5\. Entry / Exit Conditions

* Entry: Valid ingest frame \+ stable neighbor topology  
* Exit: Kernel update \+ observable emission only

No phase may:

* Modify ingest rules  
* Modify topology  
* Influence upstream phases

---

## 6\. Contract Status

This contract is:

* Authoritative  
* Non-parametric  
* Implementation-binding

Any code violating this contract is non-ALM.

