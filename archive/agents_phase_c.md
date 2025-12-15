Phase-3 Objective (Non-Interpretive)
Implement ALM’s first true compute layer, whose sole responsibility is:

Evolving interaction-generated residuals across time slices using physically plausible operators.

Phase-3 does not:

decide meaning

select symbols

correct errors

stabilize outcomes

perform cognition

Phase-3 only evolves structure already present.

2. Fundamental Operating Principle
ALM computation is governed by this invariant:

Only deviations that survive paired cancellation and persist across time slices are allowed to influence future state.

This is enforced mechanically, not logically.

3. Data Model (Locked)
The agent must not modify:

TensorCluster layout

SIMD lane count

TimeStencil rotation semantics

Free-running ingest / compute separation

Phase-3 operates on top of Phase-2 infrastructure.

4. Lane Pairing Rule (New, Mandatory)
Definition
Each effective ALM signal is represented as a paired lane:

Copy code
LanePair(i) = (lane[2i], lane[2i+1])
Residual(i) = lane[2i] − lane[2i+1]
Enforcement
Operators must consume pairs

Operators must emit paired output

Single-lane reads or writes are forbidden

5. Phase-3 Operator Class (Allowed)
Agents may implement only operators from this class:

A. Residual Extraction
Computes paired differences

No thresholds

No conditionals

B. Envelope / Accumulation
Integrates residual magnitude over:

time slices

neighboring cells

Uses FMA-friendly accumulation

C. Decay
Monotonic

Local

Parameterized but fixed during execution

D. Diffusion
Spatial only

No teleportation

No nonlocal jumps

6. Operator Execution Model
Each compute tick:

Read i_now slice only

Operate on paired lanes

Write results exclusively to i_future

Do not zero or normalize

Allow overwrite if pressure exists

Important:
Phase-3 kernels must be branchless.

7. SIMD Requirements
Use AVX2 (or detected SIMD width)

Paired lanes must map cleanly to vector lanes

All operators must vectorize cleanly

Scalar fallbacks only if SIMD unavailable

Runtime SIMD detection is allowed
Operator semantics must not change

8. Phase-3 Metrics (Collection Only)
The agent must collect, not act on:

Residual energy per tick

Residual persistence across slices

Pair symmetry violations

Operator output variance

Diffusion spread rate

Metrics are:

Observational

Logged

Non-interfering

9. Forbidden Actions (Hard Stop)
The agent must not:

Introduce thresholds

Introduce conditionals based on values

Clamp outputs

Normalize tensors

Inject constants

Create control loops

Modify TimeStencil logic

“Fix” instability

If instability appears, it is data.

10. Deliverables (Phase-3 Completion)
The agent must produce:

One minimal Phase-3 operator kernel

One SIMD-vectorized implementation

One correctness test (symmetry preservation)

One stress test (pressure + overwrite)

Metrics log output

No documentation expansion required yet.