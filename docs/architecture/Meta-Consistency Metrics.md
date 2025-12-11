# Meta-Consistency Metrics

## Purpose
Assess whether the system maintains coherent self-interpretation across time. Metrics evaluate alignment between narrative episodes, stability of the self-model, and recurrence of meta-symbol patterns.

## Conceptual Overview
Meta-consistency extends self-consistency by incorporating episode continuity and self-model reflection. Deterministic scoring blends cross-episode drift, posture stability, and relation recurrence into a single reflection stability score while exposing interpretable sub-metrics.

## Data Representation
- **Meta-Consistency Report**: `{reflection_stability, episode_alignment, posture_stability, recurrence, drift_penalty}`
- **Inputs**: meta-symbol list, narrative episodes, self-model snapshot
- **Outputs**: numeric metrics and optional CSV log for audits.

## Update Rules
1. Measure episode alignment by comparing themes between adjacent Narrative episodes.
2. Compute posture stability from the variance of the self-model posture history.
3. Track recurrence by counting dominant relations over a sliding meta-symbol window.
4. Apply drift penalties when episode salience or support falls below thresholds.
5. Combine components using configured weights to form `reflection_stability` in `[0, 1]`.

## Integration Points
- Consumes outputs from Narrative State Layer, Meta-Symbolics, and Internal Self-Model.
- Provides reflection score back to the Self-Model for smoothing.
- Supplies a final scalar for Phase 4 completion and logging.

## Examples
- Consistent themes and stable posture produce high reflection stability.
- Alternating themes with low support increase drift penalties and lower the final score.
- Recurring `reinforce` relations across windows raise the recurrence metric even when salience is modest.
