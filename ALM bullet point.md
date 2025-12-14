# ALM v0.2 — Complete System Plan (Bullet Form)

---

## 0\. Governing Principles (Non-Negotiable)

* SIMD is Ontology  
  * SIMD lanes represent relations, not objects or tensors.  
  * All differentiation is parametric (coefficients), never control flow.  
* Time is Finite and Rotational  
  * Only a small stencil of time slices exists.  
  * No “before-before” or “after-after” states are addressable.  
* Depth Comes from Relations, Not Time  
  * Memory depth is achieved through lane stacking, not extra time slices.  
* L2 Cache Residency is Law  
  * Entire active cognitive state must fit in \< 256 KB L2 per tick.  
* Jitter is Proprioception  
  * Ingest/compute drift is harvested as a control signal, not suppressed.

---

## 1\. Target Platform

* System: Dell R730  
* CPU: Xeon E5-26xx v3/v4  
* Vector ISA: AVX2 \+ FMA  
* Cache Topology:  
  * L1: private  
  * L2: private 256 KB (primary design constraint)  
  * L3: avoided in steady-state

---

## 2\. Physics Clock & Ingestion

* Sampling Rate:  
  * Nominal: 215 kHz (stress regime)  
  * Adjustable downward to increase L2 safety margin  
* Frame Size:  
  * 256 samples per ingest frame  
* Ingest Ring:  
  * 8 ingest frames (power-of-2 mask)  
  * Single stream (no duplication)  
  * Free-running, asynchronous  
* Threads:  
  * Sensor (write) thread  
  * Brain (compute) thread  
  * No synchronization barriers  
* Allowed Behavior:  
  * Read/write tearing  
  * Partial frame overwrite  
  * Sample loss (harvested, not corrected)

---

## 3\. Jitter / Proprioception Engine

* Heads:  
  * WriteHead (sensor)  
  * ReadHead (brain)  
* Bulldozer Rule:  
  * If WriteHead overtakes ReadHead:  
    * ReadHead is forcibly advanced  
    * Advancement is bounded (never beyond required future window)  
* Distance Metric:  
  * distance \= (WriteHead − ReadHead) & mask  
* Focus Mapping:  
  * Small distance → reflex / fast kernel  
  * Large distance → deep / predictive kernel  
* Output:  
  * Global scalar or vector focus\_intensity  
  * Passed into relational kernel each tick

---

## 4\. Cognitive State Geometry (“Brain Gem”)

* Spatial Substrate:  
  * 10 × 10 grid \= 100 cells  
  * Chosen for cache safety, not chromatic meaning  
* Registers per Cell:  
  * 4 registers: R, G, B, I  
* Time Stencil:  
  * 4 slices:  
    * Stable History  
    * Recent Past  
    * Now  
    * Staged Future  
* Time Semantics:  
  * Slices rotate by pointer permutation  
  * No copying, no clearing  
  * Time outside stencil does not exist

---

## 5\. Relational Depth (SIMD Lane Space)

* Lane Count:  
  * 32 lanes (128-byte aligned)  
  * 22 active relational tensors  
  * 10 padding / auxiliary / safety lanes  
* Lane Meaning:  
  * Lanes encode relations, not states  
  * Examples:  
    * One-way coupling  
    * Interstate mediation  
    * Redirect / split  
    * Inertial / stabilizing modes  
* Chromatic Structure:  
  * 12 hues × 12 tones implemented in lane algebra  
  * Mod-12 periodicity in coefficients  
  * Chromaticity is relational, not spatial

---

## 6\. Memory Layout (Strict L2 Fit)

* Alignment:  
  * alignas(128) (2 cache lines)  
* Layout Order:  
* css  
* Copy code

\[TimeSlice\]\[Cell\]\[Register\]\[Lane\]

*   
* Total Size:  
  * 100 × 4 × 4 × 32 × 4 bytes  
  * ≈ 204,800 bytes (\~200 KB)  
* Headroom:  
  * \~56 KB for:  
    * instruction footprint  
    * stack  
    * loop temporaries

---

## 7\. Relational Kernel (AVX2)

* Execution Model:  
  * One kernel per tick  
  * Straight-line, branch-free  
* Instruction Core:  
  * \_mm256\_fmadd\_ps  
* Rules:  
  * Pointer hoisting only  
  * No address math inside inner loops  
  * No memset  
  * Future slice is written destructively  
* Lane Differentiation:  
  * Via coefficient vectors only  
  * Lane identity invariant across ticks

---

## 8\. 10×10 ALM Math Solver Role

* Grid Role:  
  * Numerical substrate  
  * Not a chromatic basis  
* Solver Type:  
  * Iterated nonlinear dynamics (PDE-like)  
  * Optional fixed-point or energy descent interpretation  
* Neighborhood Coupling:  
  * Local stencil (4- or 8-neighbor)  
  * Toroidal wrap preferred (no edges)  
* Update Form:  
* ini  
* Copy code

future \= Φ(now, recent, neighborhood, lane\_params, focus)

* 

---

## 9\. Sample Rate vs L2 Safety

* Higher Sample Rate:  
  * More ticks/sec  
  * Less time per tick  
  * More L2 pressure  
  * More jitter events  
* Lower Sample Rate:  
  * Fewer ticks/sec  
  * More compute slack  
  * Greater effective L2 safety  
  * Deeper cognitive modes  
* Interpretation:  
  * Sample rate is a stress control knob, not a memory knob

---

## 10\. Accepted Design Trade-offs

* Non-determinism:  
  * Bit-exact replay not guaranteed  
  * State loss is intentional  
* AVX2 Downclocking:  
  * Accepted  
  * Mitigated by L2 residency and linear access  
* No Infinite History:  
  * Persistence emerges from dynamics, not storage

---

## 11\. Implementation Sequence

1. Define and verify TensorCluster size and alignment  
2. Implement ingest ring \+ bulldozer logic  
3. Implement AVX2 relational kernel  
4. Map jitter distance → focus intensity  
5. Profile:  
   * L2 miss rate  
   * AVX2 frequency behavior  
   * bulldozer event distribution

---

## 12\. One-Sentence System Summary

ALM v0.2 is a cache-resident, free-running, relational field engine where time is finite, depth is relational, SIMD lanes are ontological, and jitter is sensed rather than suppressed.

