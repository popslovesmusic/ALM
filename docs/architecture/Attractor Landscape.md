# Attractor Landscape

## Purpose
Transforms cluster summaries into attractor basins that represent stable chromatic states. Each basin tracks energy, stability, and activation values that guide temporal convergence and phrase alignment.

## Data Structures
- **Attractor**: dataclass with `idx`, `center_tone`, `center_hue`, `energy`, `stability`, `activation`.
- **Config**: `attractors_config.json5` with basin width, stability decay, energy gain, damping, momentum, and activation thresholds.

## Update Rules
1. **Energy Initialization**: Derive basin energy from cluster coherence and size using configured weights and gain factor.
2. **Stability Decay**: Reduce raw coherence by a fixed decay to prevent brittle peaks.
3. **Activation**: Subtract damping from energy; clamp to zero to preserve determinism.
4. **Temporal Update**: Blend prior energy with new input using momentum; recompute stability and activation after damping and decay.

## Examples
Two clusters yield two attractors. A coherent cluster with four members yields higher energy and activation than a sparse cluster. Subsequent frames update energy smoothly via momentum, maintaining continuity without abrupt jumps.

## Integration Points
- **Cluster Maps**: Every cluster seeds an attractor basin with centroid tone/hue.
- **Phrase Structure**: Phrase segmentation favors periods where activation remains above threshold.
- **Self-Consistency**: Mean activation and stability contribute to the final consistency score.
- **Logs**: Activation summaries flow into `attractor_metrics.csv` for audit trails.
