# Narrative State Layer

## Purpose
Aggregate meta-symbols and phrase spans into episodic narratives that capture how interpretations evolve. The layer introduces temporal arcs, episode coherence, and salience that guide downstream feedback and self-modeling.

## Conceptual Overview
Narratives are constructed by sliding a configurable window across phrases and their meta-symbol relations. Each episode bundles motifs, relations, and coherence scores into a compact record. Deterministic heuristics assign themes (dominant relation + motif), compute salience from cadence and weights, and maintain an episode-level consistency value.

## Data Representation
- **NarrativeEpisode**: `(idx, start, end, theme, salience, meta_count, consistency, posture_hint)`
- **Inputs**: ordered meta-symbols, phrases, optional attractor/cluster summaries
- **Outputs**: list of NarrativeEpisode objects and aggregate statistics (mean salience, dominant theme, window coverage).

## Update Rules
1. Chunk phrases using the configured `window` size; align meta-symbols that overlap each chunk.
2. Derive a theme using the most frequent relation and phrase motif within the chunk.
3. Compute salience = mean(meta-symbol weight) + cadence_bias − drift_penalty.
4. Evaluate consistency by comparing motif spread, polarity stability, and meta-symbol support counts.
5. Emit posture hints (`stabilize`, `amplify`, `reframe`) based on salience and consistency thresholds.

## Integration Points
- Consumes Meta-Symbolics output and original phrase boundaries.
- Provides posture hints to Coherence Feedback.
- Supplies episode summaries to the Internal Self-Model.
- Offers time-aligned windows for Meta-Consistency Metrics.

## Examples
- A run of `reinforce` relations with stable cadence yields a "reinforce-ascending" episode with high salience.
- Mixed motifs but rising cadence produce a "reframe" posture hint encouraging the feedback layer to dampen volatility.
- Sparse meta-symbols with low support form a low-salience episode that can be deprioritized downstream.
