# Chromatic Phrase Structure

## Purpose
Defines temporal grammar over symbol streams by segmenting sequences into phrases and detecting motifs based on tone slope, polarity balance, and peak cadence. The structure encodes emergent rhythmic patterns required for Phase 3 cognition.

## Data Structures
- **Phrase**: dataclass with `idx`, `start`, `end`, `motif`, `cadence`.
- **Config**: `phrase_config.json5` fields for phrase window, motif_length, tone_slope_threshold, and cadence_threshold.

## Update Rules
1. **Windowing**: Slide through symbols in fixed windows to ensure deterministic segmentation.
2. **Motif Detection**: Compute tone slope across the motif_length subset; classify as ascending, descending, balanced, pulse, or rebound. Append `-soft` if cadence falls below threshold.
3. **Cadence Calculation**: Ratio of peak-role symbols within the phrase window; clamp to three decimals.
4. **Boundary Tracking**: Use timestamps of first and last symbols in the window to preserve temporal alignment.

## Examples
A five-symbol sequence with rising tones produces an `ascending-soft` motif when cadence is sparse; denser peaks lift cadence above threshold, yielding `ascending` without suffix. Mixed polarity with flat slope becomes `pulse` or `rebound` motifs.

## Integration Points
- **Symbol Formation**: Requires peak roles and timestamps to measure cadence accurately.
- **Cluster Maps**: Boundaries can align with coherence changes to mark phrase transitions.
- **Attractor Landscape**: Persistent activations encourage longer phrases and affect motif classification.
- **Self-Consistency**: Phrase cadence contributes to the final score and supports drift/symmetry checks.
