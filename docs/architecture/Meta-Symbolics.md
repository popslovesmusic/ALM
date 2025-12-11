# Meta-Symbolics

## Purpose
Define relationships between lower-level chromatic symbols, clusters, attractors, and phrase motifs to capture how interpretations influence each other over time. Meta-symbols expose reinforcement, contrast, anticipation, and resolution patterns that the higher layers can reason over.

## Conceptual Overview
Meta-symbols link pairs of phrases and their supporting clusters into interpretable relational tokens. Each meta-symbol carries a relation label, support count, and weight derived from cadence, cluster coherence, and polarity alignment. The layer stays deterministic by deriving everything from prior outputs without randomness.

## Data Representation
- **MetaSymbol**: `(idx, anchor_label, target_label, relation, span, support, weight, coherence)`
- **Inputs**: symbols, clusters, phrases (and optionally attractor activations for coherence bias)
- **Outputs**: ordered list of MetaSymbol objects plus summary metrics for logging.

## Update Rules
1. Slide through phrases in temporal order.
2. Determine a relation type based on motif continuity (`reinforce`), motif shifts (`contrast`), cadence increases (`anticipate`), or cadence drops (`resolve`).
3. Locate nearest clusters to anchor and target boundaries; compute polarity balance from symbols in-span.
4. Compute weight = motif_weight + coherence_bias + polarity_alignment, then clamp to `[0, 1]`.
5. Increment support when relation persists within the configured window; otherwise start a fresh meta-symbol.
6. Emit summaries (count, mean weight, dominant relation) for downstream logging.

## Integration Points
- Consumes symbols, clusters, and phrases produced by earlier layers.
- Feeds Narrative State Layer with relational tokens and their spans.
- Provides weights to Coherence Feedback for posture adjustments.
- Supplies support counts for Internal Self-Model stability tracking.

## Examples
- Consecutive "ascending" motifs with high cadence yield a `reinforce` meta-symbol spanning both phrases.
- A sharp cadence jump following a polarity flip yields an `anticipate` relation with modest weight.
- Divergent motifs with low coherence clusters trigger `contrast` relations and reduce downstream confidence.
