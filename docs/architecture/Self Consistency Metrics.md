# Self Consistency Metrics

## Purpose
Evaluates the coherence of the entire Phase 3 pipeline by combining symbol stability, cluster coherence, attractor activation, and phrase cadence into a single deterministic score. Penalizes excessive drift or asymmetry to maintain interpretable behavior.

## Data Structures
- **Metrics dict**: `{symbol_score, cluster_score, attractor_score, phrase_score, drift_penalty, symmetry_penalty, final_score}`.
- **Config**: `self_consistency_config.json5` weights for each component plus drift and symmetry tolerances.

## Update Rules
1. **Component Scores**: Average stability, coherence, activation, and cadence while enforcing minimum counts for symbols, clusters, and phrases.
2. **Penalty Computation**: Drift = tone range scaled by tolerance; symmetry = tone imbalance between first and second half of symbols.
3. **Weighted Fusion**: Multiply each component by its weight, subtract penalties, and clamp the result to zero or above.

## Examples
A stable sequence with balanced polarity produces high symbol and cluster scores; modest drift results in a small penalty, yielding a final_score near the weighted mean. A highly asymmetric sequence incurs larger penalties, visibly lowering final_score despite strong clusters.

## Integration Points
- **Symbol/Cluster/Attractor/Phrase Modules**: Provide component metrics.
- **Logs**: Persisted to `self_consistency_metrics.csv` for audits and comparisons across runs.
- **Reports**: Feed into `FINAL_REPORT_PHASE3.md` to summarize end-to-end readiness.
