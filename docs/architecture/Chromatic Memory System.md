# Chromatic Memory System

**Project:** `cognition/`
**Module:** `ctl/memory.py`
**Role:** Capture stable tone and hue attractors from the L stream so Tensor R can snap toward familiar structures and boost coherence when recognitions occur.

---

## 1. Memory State
A lightweight dictionary maintains sparse peaks:
- `tone_peaks`: list of `{tone, strength}` on the 12-tone circle.
- `hue_peaks`: list of `{hue, strength}` in RGB space.
- `updates`: count of reinforcement steps applied.

Strength encodes how salient or repeatedly observed a peak is after decay and reinforcement.

---

## 2. Configuration (ctl/memory_config.json5)
* **peaks.tone**: `decay`, `max_peaks`, `reinforce_gain`, `min_separation`, `min_strength`.
* **peaks.hue**: `decay`, `max_peaks`, `reinforce_gain`, `min_distance`, `min_strength`.
* **matching**: `tone_tolerance`, `hue_tolerance`, `intensity_weight`, `coherence_bias`, `min_match_strength`.

Decay prunes weak peaks, reinforcement grows salient ones, and matching thresholds control when a cell counts as a recognition.

---

## 3. Update Cycle
For each incoming L cell:
1. **Decay** existing tone/hue peaks by their configured rate; drop values under `min_strength`.
2. **Compute boost** = `1 + intensity_weight * intensity + coherence_bias * coherence`.
3. **Reinforce tone peak** at the nearest neighbor within `min_separation` or append a new peak while under `max_peaks`.
4. **Reinforce hue peak** at the closest hue within `min_distance` or add a new peak while under `max_peaks`.
5. **Persist** updated `tone_peaks`, `hue_peaks`, and `updates`.

---

## 4. Recognition and Snapping
* **match_to_memory_profile**: returns `True` when tone and/or hue fall within tolerance of a sufficiently strong peak (using `tone_tolerance`, `hue_tolerance`, and `min_match_strength`).
* **snap_to_nearest_memory_tone**: if a strong tone peak is within tolerance, snap the tone directly to that peak.
* **snap_to_nearest_memory_hue**: if a strong hue peak is within tolerance, snap hue to the stored RGB values.

These functions allow Tensor R to stabilize around familiar attractors while rejecting weak or noisy peaks.

---

## 5. Integration Path
1. Load config via `memory.load_memory_config()` and create `memory_state = memory.init_memory_state()`.
2. During Tensor R updates, call `memory.match_to_memory_profile` to gate coherence boosts.
3. Apply `snap_to_nearest_memory_tone/hue` after smoothing and prediction to enforce attractors.
4. Call `memory.update_memory_state` each step to decay stale peaks and reinforce new observations.

This loop yields adaptive long-horizon memory that gradually shapes Tensor R’s tone and hue expectations.
