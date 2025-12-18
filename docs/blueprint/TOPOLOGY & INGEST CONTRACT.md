# TOPOLOGY & INGEST CONTRACT

ALM Topology and Ingest Contract v1.0 (Canonical)  
---

## 1\. Purpose

This contract defines the only admissible spatial coupling and external ingest rules for all ALM kernels.  
Its purpose is to eliminate all implementation discretion regarding:

* Neighbor construction  
* Aggregation behavior  
* Ingest timing  
* Ingest structure  
* Authority flow into the kernel

Any implementation that violates this contract is not ALM-compliant.  
---

## 2\. Binding Constraints (Derived)

The following constraints are already enforced elsewhere in ALM and are binding here:

* Pressure channels are orthogonal to state evolution  
* No control, gating, or thresholding is permitted  
* Phase isolation is mandatory  
* Cache residency is bounded  
* Pairwise symmetry must be preserved  
* Observers do not feed back into kernel dynamics

All declarations below satisfy and enforce these constraints.  
---

## 3\. Topology Definition

### 3.1 Cells

An ALM system consists of a finite set of cells.  
All cells are topologically equivalent.  
No geometric embedding is assumed or permitted.  
---

### 3.2 Neighbor Degree (Canonical)

Each cell c maintains a fixed neighbor set N(c) with invariant cardinality:  
mathematica  
Copy code  
|N(c)| \= K \= 12

This value is canonical, global, and immutable.  
---

### 3.3 Neighbor Construction (Canonical)

For each cell c:

* N(c) consists of exactly 12 statically assigned adjacent cells  
* Adjacency is:  
  * symmetric  
  * static for system lifetime  
  * abstract (non-geometric)

Formally:  
r  
Copy code  
cᵢ ∈ N(cⱼ) ⇔ cⱼ ∈ N(cᵢ)

---

### 3.4 Neighbor Weighting (Canonical)

All neighbor contributions are uniformly weighted:  
ini  
Copy code  
w\_i \= 1 / 12

Properties:

* Sum-normalized  
* Symmetry-preserving  
* No authority gradients  
* No implicit control channels

---

### 3.5 Forbidden Topological Behaviors

The following are explicitly forbidden:

* Dynamic rewiring  
* Long-range shortcuts  
* Distance-dependent weighting  
* Learned or adaptive weights  
* Global routing tables  
* Per-lane neighbor specialization

---

## 4\. Ingest Contract

### 4.1 Ingest Lanes

External signals may enter ALM only through designated ingest lanes.  
Ingest lanes:

* Are orthogonal to pressure and persistence channels  
* Do not modify kernel coefficients  
* Do not modify topology  
* Do not carry control or timing metadata

---

### 4.2 Ingest Cadence (Canonical)

Ingest operates at a fixed cadence aligned to the ALM time stencil.  
Rules:

* One ingest frame corresponds to exactly one stencil advancement  
* No mid-step injection is permitted  
* No event-driven or asynchronous callbacks are permitted

---

### 4.3 Valid Ingest Frame (Canonical)

A valid ingest frame consists of:

* One scalar value per declared ingest lane  
* Values aligned to a single stencil step  
* No control, topology, or timing metadata

Frames that violate cadence or bounds are rejected upstream and do not enter ALM state.  
---

### 4.4 Jitter Bounds (Canonical)

Permitted ingest jitter is bounded by:  
Copy code  
|Δt| ≤ 0.25 × Δt\_stencil

Behavior:

* Jitter within bounds is absorbed by the stencil smoothing rule  
* Jitter exceeding bounds invalidates the ingest frame

Jitter does not propagate as state.  
---

## 5\. Phase Boundaries

### Entry Conditions

* Valid ingest frame  
* Stable topology

### Exit Conditions

* Kernel update  
* Observable emission only

No phase may:

* Modify topology  
* Modify ingest rules  
* Influence upstream phases

---

## 6\. Contract Status

This contract is:

* Closed  
* Non-parametric  
* Implementation-binding

Any deviation constitutes a spec violation, not an interpretation difference.

