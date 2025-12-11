# Category & Cluster Maps

## Purpose
Organizes symbols into coherent chromatic categories, highlighting local agreements in tone, hue, and polarity. The clustering stage provides centroids and coherence scores that seed attractor basins and guide phrase construction.

## Data Structures
- **Cluster**: dataclass with `idx`, `member_indices`, `centroid_tone`, `centroid_hue`, `polarity`, `coherence`, `label`.
- **Similarity thresholds**: `clusters_config.json5` fields `tone_threshold`, `hue_threshold`, `polarity_consensus`.
- **Coherence weights**: tone/hue/polarity weights plus optional peak bonus for sufficiently large clusters.

## Update Rules
1. **Similarity Checks**: Walk the symbol stream in order; start a new cluster when tone or hue drift exceeds thresholds or polarity diverges (if consensus enforced).
2. **Polarity Consensus**: Track counts of positive and negative members; neutralize polarity when tied.
3. **Coherence Score**: Compute tone spread and hue spread against configured limits, then blend weighted terms with polarity term and optional size bonus. Clip to `[0,1]`.
4. **Centroid Calculation**: Average tone and hue components across members; generate label `C{idx}-T{tone}-P{polarity}`.

## Examples
Two adjacent peaks with tones 1 and 2, aligned hue values, and positive polarity form a single cluster with coherence >0.7. A later polarity flip with tones 6 and 7 spawns a second cluster with negative consensus and its own centroid.

## Integration Points
- **Symbol Formation**: Consumes `Symbol` outputs directly.
- **Attractor Landscape**: Each cluster becomes a candidate basin with energy proportional to coherence and size.
- **Phrase Structure**: Phrase motifs consider cluster boundaries for cadence and motif labeling.
- **Self-Consistency**: Mean coherence feeds the cluster component of the final consistency score.
