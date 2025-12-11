# Symbol Formation Layer

## Purpose
Transforms ChromaticCell outputs from the CTL core into stable, labeled symbols that capture tone, hue, polarity, and intensity patterns. The layer smooths temporal fluctuations, assigns semantic roles (onset/peak/bridge/decay), and prepares downstream clustering, attractor, and phrase modules with deterministic feature encodings.

## Data Structures
- **ChromaticCell**: `{tone: int, hue: (r,g,b), polarity: int, intensity: float, timestamp: int}`
- **Symbol**: dataclass with fields `idx`, `tone`, `hue`, `polarity`, `intensity`, `timestamp`, `role`, `stability`, `label`.
- **Config**: `symbols_config.json5` providing aggregation window, intensity threshold, polarity weight, role bonuses, and labeling bands.

## Update Rules
1. **Smoothing**: Moving average over intensity with configurable window to stabilize noisy frames.
2. **Role Detection**: Evaluate each smoothed intensity relative to neighbors; identify `peak`, `bridge`, `onset`, or `decay` based on threshold crossings and local slopes.
3. **Stability Score**: Combine smoothed intensity with polarity weight and optional peak bonus; apply decay factor to prevent runaway values.
4. **Labeling**: Bucket tone and hue into discrete bands (tone_band, hue_band) and combine with polarity sign to form deterministic symbol labels.

## Examples
Given four ChromaticCells with increasing tone and mixed polarity, the layer produces symbols such as `T0-H0-P+1` (onset) and `T1-H0-P-1` (peak). Stability values rise on peaks and fall on bridges/decays, while timestamps remain aligned to input order.

## Integration Points
- **L/R Tensors**: Consumes tone/hue/polarity from CTL tensor outputs.
- **Memory**: Stability values can seed memory persistence scores.
- **Coupling**: Labels and polarity guide coupling coherence checks.
- **Dynamics**: Roles influence dynamic visualizations and intensity evolution plots.
- **Downstream Modules**: Feeds clusters.py for grouping, attractors.py for basin energy, phrase.py for motif detection, and self_consistency.py for scoring.
