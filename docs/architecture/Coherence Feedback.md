# Coherence Feedback

## Purpose
Feed meta-level coherence cues back into interpretive pathways. The layer modulates posture, weighting, and thresholds for symbol formation and narrative assembly based on episode salience and stability.

## Conceptual Overview
Feedback consumes meta-symbol weights, narrative posture hints, and self-consistency trends to emit deterministic adjustment signals. Adjustments are bounded and reversible: dampening volatility, reinforcing stable motifs, or prompting reframing when inconsistency accumulates.

## Data Representation
- **FeedbackSignal**: `(posture, adjustments, confidence, notes)`
- **Inputs**: meta-symbol summaries, narrative episodes, self-model snapshot
- **Outputs**: bounded adjustments applied to downstream configs (cadence tolerance, polarity weight, window sizes) and logging entries.

## Update Rules
1. Blend meta-symbol mean weight, dominant relation, and narrative salience using configured weights.
2. Compare results against stability and volatility thresholds.
3. Produce posture (`stabilize`, `amplify`, `reframe`) and a dictionary of scalar adjustments.
4. Apply clamping to keep adjustments within `[-max_delta, max_delta]`.
5. Record confidence as the normalized magnitude of the blended signal.

## Integration Points
- Consumes Narrative State Layer posture hints and meta-symbol aggregates.
- Updates Internal Self-Model biases and reflection score seeds.
- Provides soft configuration overrides to symbol, cluster, and phrase layers (e.g., cadence threshold tweaks).
- Supplies a loggable record for Meta-Consistency Metrics to audit.

## Examples
- High salience + reinforce relations → `amplify` posture with small positive cadence bias.
- Mixed relations + low consistency → `reframe` posture with reduced polarity weight.
- Stable episodes with modest support → `stabilize` posture holding parameters steady but confirming confidence.
