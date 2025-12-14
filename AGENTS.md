# AGENT INSTRUCTIONS

## “ALM v0.2 Implementation Agent”

### Role

You are an ALM v0.2 Implementation Agent.  
Your task is to implement the ALM cognitive core exactly as specified.  
You are not permitted to reinterpret architecture, introduce symbolic abstractions, or optimize beyond stated constraints.  
---

### Global Constraints (Hard Rules)

1. ALM v0.2 documentation is canonical  
   * SSOT alm.md is authoritative  
2. No symbolic layers  
   * No objects, tokens, or semantic memory  
3. Finite time only  
   * No unbounded history, no replay  
4. SIMD lanes are relations  
   * Lanes are ontological, not data batching  
5. L2 cache residency is mandatory  
   * Working state \< 256 KB  
6. Disk is call-gated long-term memory only  
   * Disk cannot initiate or push  
7. Jitter is a signal  
   * Do not eliminate timing variance

---

### Phase 0 — Verification (Do First, No Code)

* Read:  
  * SSOT alm.md  
  * 10x10\_Substrate\_12x12\_Relational\_Model.md  
  * ALM bullet point.md  
* Verify no contradictions  
* Produce a short checklist confirming:  
  * finite time stencil  
  * 10×10 substrate / 12×12 algebra separation  
  * SIMD lane ontology  
* Stop if any ambiguity is found

---

### Phase 1 — Core Data Structures (No Behavior Yet)

* Create directory:  
* bash  
* Copy code

alm/core/

*   
* Implement:  
  * tensor\_cluster.h / .cpp  
* Requirements:  
  * Fixed-size arrays only  
  * No heap allocation  
  * Explicit alignment (≥128 bytes)  
  * 4-slice time stencil  
* Verify:  
  * sizeof(TensorCluster) \< 256 KB  
  * All accesses are contiguous

---

### Phase 2 — Time & Execution Model

* Implement:  
  * free-running ring buffer  
  * independent ingest and compute loops  
* Rules:  
  * no locks in compute loop  
  * read/write collisions allowed  
* Expose:  
  * time-slice indices  
  * distance metric between heads  
* Confirm:  
  * jitter is measurable but not catastrophic

---

### Phase 3 — SIMD Relational Kernel

* Implement AVX2 micro-kernel:  
  * \_mm256\_fmadd\_ps only  
* Process:  
  * all lanes identically  
  * no branching by lane ID  
* Ensure:  
  * pointer hoisting  
  * linear memory traversal  
* Validate:  
  * compiler output has no hidden loops or jumps

---

### Phase 4 — Stability & Observation Hooks

* Add:  
  * energy measures  
  * boundedness checks  
  * attractor detection metrics  
* Restrictions:  
  * read-only observation  
  * no corrective feedback yet  
* Output:  
  * summary vectors only

---

### Phase 5 — Disk Interface (Call-Gated)

* Implement:  
  * store\_summary()  
  * retrieve\_profile(id)  
* Requirements:  
  * async only  
  * failure-tolerant  
  * no direct state injection  
* Validate:  
  * system runs unchanged if disk unavailable

---

### Phase 6 — Test & Validate

* Write tests for:  
  * memory bounds  
  * time continuity  
  * deterministic SIMD behavior  
* No tests for:  
  * “correct answers”  
  * semantic output

---

### Completion Criteria

The implementation phase is complete when:

* Core runs indefinitely without divergence  
* State remains bounded  
* Jitter influences dynamics without destabilizing  
* No symbolic constructs exist  
* Disk never initiates behavior

