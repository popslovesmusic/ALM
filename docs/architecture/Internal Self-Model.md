# Internal Self-Model

## Purpose
Maintain a lightweight structural representation of the system’s interpretive posture, stability, and biases. The self-model enables reflective adjustments and provides continuity across episodes.

## Conceptual Overview
The self-model collects posture hints, meta-symbol supports, and meta-consistency signals into a deterministic state object. It tracks stability as a rolling measure, records bias weights applied by feedback, and updates its posture when salience or volatility thresholds are crossed.

## Data Representation
- **SelfModel**: `(posture, stability, biases, recent_scores, reflection)`
- **Inputs**: feedback signals, narrative episodes, meta-consistency ratings
- **Outputs**: updated SelfModel object and snapshot dictionary for logging.

## Update Rules
1. Initialize posture from configuration (`predictive`, `reactive`, or `stable`).
2. Incorporate feedback adjustments by updating bias values (cadence, polarity, window factors).
3. Update stability using exponential smoothing over recent meta-consistency scores.
4. Change posture if salience exceeds the amplify threshold or dips below the stabilize threshold.
5. Emit a reflection score summarizing how closely the current posture matches observed consistency.

## Integration Points
- Consumes output from Coherence Feedback and Meta-Consistency Metrics.
- Provides posture back to feedback for closed-loop adjustment.
- Supplies a stabilized snapshot for logging and downstream analytics.

## Examples
- Sustained high salience raises the stability metric and keeps the posture in `predictive` mode.
- Volatile episodes with low consistency shift posture to `reframe` and reduce cadence bias.
- Stable but low-energy runs settle into `stable` posture with neutral biases and high reflection score.
