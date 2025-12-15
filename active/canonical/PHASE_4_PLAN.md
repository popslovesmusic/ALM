# Phase 4 Plan — Structural Persistence & Selection Pressure

## Observables
- Residual energy density per lane pair measured from the current slice.
- Correlation of current residuals with recent and stable slices (persistence_recent, persistence_stable).
- Drift energy between stable and current residuals plus recurrence coherence across rotations.

## Pressure Terms
- **Crowding decay:** smooth reduction of update magnitude scaled by neighbor residual energy; no thresholds or clamps.
- **Diffusion blending:** residuals blend toward neighbor residuals to allow interference without discrete selection.
- **Bandwidth moderation:** global, branchless multiplier `1 / (1 + α * mean_residual_energy)` to keep updates bounded when overall activity rises.

## Explicitly Forbidden
- No tokens, labels, classes, or identifiers; Phase 4 remains pre-semantic.
- No thresholding, top-k selection, or if/else logic driven by metrics.
- No control loops or normalization that steers toward target states.
- No promotion of memory or pinning of structures; persistence is only measured.

## Completion Criteria
- Persistence probe emits continuous observables without influencing computation.
- Selection pressure operates via smooth decay, diffusion, and bandwidth scaling only.
- Phase-4 kernel preserves lane-pair neutrality and writes future slices without introducing asymmetry.
- Competition tests show differential persistence without discrete winners; neutrality tests remain stable.
- Phase-3 behavior stays unchanged and Phase-4 artifacts remain pre-semantic.
