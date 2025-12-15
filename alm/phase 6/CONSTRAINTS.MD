PHASE_6_CONSTRAINTS.md
Scope: Phase 6 Only
Authority: Hard / Non-Negotiable
Deletion Effect: Phase 6 Ceases to Exist

1. Core Safety Doctrine (Binding)
Phase 6 may change what can be seen,
but must never change what happens.

Any violation of this doctrine invalidates Phase 6.

2. Causal Isolation (CRITICAL)
The Phase-6 agent SHALL NOT:

write to any structure used by Phases 1–5

alter buffers, ring sizes, decay rates, or coefficients

modify scheduling, execution order, or timing

introduce locks, waits, synchronization, or blocking calls

alter random seeds, jitter sources, or entropy streams

change memory allocation patterns observable upstream

If Phase 6 can affect execution timing or memory layout, it is causal and therefore forbidden.

3. Detachability Requirement (MANDATORY)
The system must satisfy the following invariant:

Removing Phase 6 entirely produces identical Phase-1–5 behavior
(bitwise identical within floating-point tolerance).

This includes:

state tensors

event traces

decay behavior

diagnostics

halt/continue decisions

If this cannot be demonstrated by test, Phase 6 is invalid.

4. Input Restrictions (Strict)
Phase 6 may read only:

Phase-5 event traces containing:

opaque event ID

timestamp

spatial index

continuous intensity

unnamed feature vector

Phase 6 may not read:

Phase-4 internal fields

diagnostics state

governance state

decay parameters

tool-orchestration state

5. Allowed Operations (Whitelist Only)
5.1 Relational Construction
Permitted relations (continuous only):

temporal adjacency (smooth decay with Δt)

spatial proximity (distance-weighted)

feature similarity (dot, cosine, diffusion distance)

co-occurrence statistics

No thresholds. No gates. No booleans.

5.2 Structural Transforms (Permitted Classes)
The agent may compute:

weighted graphs

graph Laplacians

spectral embeddings

diffusion maps

recurrence measures

continuous transition matrices

These are coordinate transforms, not interpretations.

5.3 Invariant Extraction
Permitted outputs include:

eigenvalue spectra

low-dimensional embeddings

stability / recurrence metrics

tolerance-aware structural signatures

No ranking. No pruning. No selection.

6. Explicitly Forbidden Operations
The Phase-6 agent SHALL NOT:

assign names, labels, or meanings

classify or cluster with semantic intent

define importance, salience, or relevance

introduce thresholds or boolean decisions

feed results back into ALM

trigger storage or retrieval autonomously

learn or adapt parameters over time

run continuously or in the background

Phase 6 is stateless unless explicitly handed state.

7. Output Contract (Read-Only Artifacts)
7.1 AtlasFrame
May contain:

event IDs

relational coordinates

density / recurrence values

transition strengths

No labels. No explanations. No authority.

7.2 AtlasSignature
deterministic within tolerance

derived solely from invariants

suitable for comparison

never treated as truth

7.3 Optional Match Report
Only if explicitly requested:

similarity scores

opaque prior identifiers

alignment distances

No autonomous retrieval.

8. Disk Discipline
Phase 6 SHALL NOT:

write to disk without explicit command

read from disk without explicit command

perform background indexing

Storage is append-only and inert.

9. Determinism Requirement
Given identical inputs, Phase-6 outputs must be identical within floating tolerance.

Non-determinism beyond tolerance is a failure.

10. Required Tests (Blocking)
10.1 Detachment Test
Run Phases 1–5 alone → record outputs

Enable Phase 6 (unused outputs)

Re-run identically

Assert no upstream differences

Any difference = failure.

10.2 Read-Only Audit
Verify:

no upstream writes

no timing drift

no allocation drift

10.3 Threshold Audit
Scan Phase-6 code for:

if / else gates

comparisons against constants

boolean logic

Any occurrence = failure.

11. Completion Definition
Phase 6 is complete only when:

all blocking tests pass

detachment is proven

outputs are structurally useful

no semantics exist anywhere in the layer

At that point, Phase 6 is a tool, not a dependency.

End of PHASE_6_CONSTRAINTS.md

