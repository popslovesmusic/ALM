PHASE 4 — HARD CONSTRAINTS
Phase Name: Structural Persistence & Selection Pressure
System: ALM (Analog Latent Model)

These constraints are non-negotiable.
They override convenience, optimization, and future plans.

C0 — Phase Boundary Lock
Phase 3 code is frozen

Phase 3 operator semantics may not be altered

TimeStencil rotation semantics may not be altered

Only read access to Phase-3 outputs is allowed

Bug fixes only, with:

explicit justification

regression tests

C1 — No Semantics (Absolute)
Phase 4 must not introduce:

symbols

tokens

labels

categories

identifiers

pattern names

classifiers

“this represents X” logic

Anything that can be named is out of scope.

C2 — No Discrete Decisions
Forbidden:

thresholds

if/else branching on data

step functions

top-k selection

winner-take-all logic

boolean gates driven by metrics

Allowed:

smooth, continuous functions only

monotonic response curves

linear or gently nonlinear operators

C3 — No Control Loops
Phase 4 must not:

steer the system toward outcomes

stabilize states intentionally

suppress “undesirable” behavior

correct deviations

Selection must emerge only from physical pressure.

C4 — Physical Selection Only
Allowed sources of selection pressure:

finite bandwidth (write pressure)

decay

diffusion

crowding / interference

resource competition

Forbidden:

scoring

ranking

reward functions

penalties

optimization objectives

C5 — Locality Constraint
All Phase-4 effects must be:

local in space (cell / neighborhood)

local in time (adjacent slices only)

Forbidden:

global coordination logic

centralized arbitration

global “mode switches”

A smooth global scalar (e.g., total energy normalization) is allowed only if:

continuous

branchless

non-directive

C6 — Lane-Pair Invariance
All Phase-4 kernels must:

operate on lane pairs

preserve symmetry when input is symmetric

emit paired outputs only

If a symmetric input produces asymmetric output → bug.

C7 — Neutrality Preservation
If:

inputs are flat

or perfectly paired

or fully canceling

Then:

outputs must remain flat

Phase 4 must never generate structure from nothing.

C8 — Observation Without Intervention
Metrics may be:

measured

recorded

logged

Metrics must never:

influence computation

gate execution

alter coefficients

trigger logic

Observation is passive only.

C9 — No Memory Promotion
Phase 4 must not:

declare something “persistent” as a state

promote structures to special storage

freeze or pin patterns

Persistence is measured, not asserted.

C10 — No Cognition Leakage
Forbidden concepts:

intention

representation

meaning

prediction as decision

self-model

goal-directed behavior

Phase 4 remains pre-semantic.

C11 — Hardware Agnosticism
Phase-4 behavior must be invariant under:

scalar execution

AVX2 execution

different SIMD widths

Hardware may change performance, not behavior.

C12 — Failure Is Data
If Phase-4 exhibits:

instability

collapse

dominance

extinction

oscillation

This is valid output, not an error.

Do not “fix” it.

Phase 4 Completion Definition
Phase 4 is complete when:

structures persist or dissolve solely via physical pressure

competition occurs without thresholds or labels

neutrality is preserved

Phase-3 tests still pass

no semantic artifacts appear

Phase-4 AGENTS.md is archived