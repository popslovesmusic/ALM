# Coupling Laws Architecture

**Project:** `cognition/`  
**Module:** `ctl/coupling.py`  
**Role:** Bind Tensor L (perceptual stream) with Tensor R (interpretive stream) into a single coherent chromatic narrative.

Coupling aligns fast sensory updates with slower internal models. It measures disparity, negotiates polarity, and stabilizes tone/hue/intensity so that downstream layers receive a unified chromatic sequence.

---

## 1. Coupling State Definition
At discrete index `i`, a coupled cell `C[i]` is:

```
C[i] = {
  tone        # blended int 0–11 (toward L, respecting R stability)
  hue         # RGB triple blended toward L hue expectation
  intensity   # float, long-horizon salience with bias to R memory
  polarity    # structural polarity negotiated between L and R
  timestamp   # taken from L (or R if L omitted)
  agreement   # [0,1] similarity score across tone/hue/intensity
  coherence   # [0,1] stabilized value after decay + agreement boost
  constraint_flag # "OK" | "WARN" | "VIOLATION" (based on disparity)
}
```

Semantics:
* **tone**: directional blend that respects R’s smoothing while nudging toward L.
* **hue**: linear RGB blend; keeps R palette steady but tracks L drift.
* **intensity**: carries long-horizon salience; avoids spikes by partial adoption.
* **polarity**: prefers consensus; may flip when conflicts persist with low agreement.
* **agreement**: composite similarity measure (tone, hue, intensity).
* **coherence**: internal stability that decays unless supported by agreement.
* **constraint_flag**: signals disparities that exceed allowed thresholds.

---

## 2. Inputs and Configuration

### Inputs
* `L[i]`: perceptual ChromaticCell `{tone, hue, intensity, polarity, timestamp}`.
* `R[i]`: interpretive ChromaticCell `{tone, hue, intensity, polarity, timestamp, coherence}`.

### Configuration (ctl/coupling_config.json5)
* **weights**: `tone_alignment`, `hue_alignment`, `intensity_alignment` (0–1 blends).
* **thresholds**: `tone_error_max`, `hue_error_max`, `intensity_gap_max`, `agreement_min`.
* **coherence**: `min_coherence`, `boost_on_agreement`, `decay`.
* **polarity**: `prefer_consensus`, `flip_if_conflict`.
* **logging**: `enabled`, `log_dir` (append-only CSVs).

---

## 3. Coupling Algorithm
For each `(L[i], R[i])` pair:

1. **Measure Disparity**
   * `tone_gap` = min cyclic distance on 12-tone circle.
   * `hue_gap` = mean RGB channel difference.
   * `intensity_gap` = absolute scalar gap.

2. **Blend Toward Consensus**
   * `tone` = `(1-w_tone) * tone_R + w_tone * tone_L (mod 12)`.
   * `hue` = channel-wise blend using `w_hue`.
   * `intensity` = linear blend using `w_intensity`.

3. **Compute Agreement**
   * Normalize each gap by its threshold and average.
   * `agreement = max(0, 1 - mean_normalized_gap)`.

4. **Update Coherence**
   * Apply decay, then add agreement-driven boost.
   * Clamp to `>= min_coherence`.

5. **Negotiate Polarity**
   * Prefer L polarity when it disagrees with R.
   * If conflict persists and `agreement < agreement_min`, optionally flip polarity.

6. **Constraint Flagging**
   * Count breaches of tone/hue/intensity thresholds or low agreement.
   * `WARN` on single breach, `VIOLATION` on multiple, else `OK`.

7. **Emit Coupled Cell** with updated fields.

---

## 4. Metrics and Logging
* **Coupling metrics**: averages of tone/hue/intensity errors and agreement.
* **Tensor R behavior**: mean tone/intensity/coherence + sequence length.
* **End-to-end summary**: input length, mean agreement, warning/violation counts.

CSV logs (append-only) live in `/logs/`:
* `coupling_metrics.csv`
* `tensor_r_behavior.csv`
* `end_to_end_summary.csv`

---

## 5. Integration Path
1. Generate Tensor L via `ctl_core` (tone/hue/intensity/polarity extraction).
2. Build Tensor R via `tensor_r_update.update_tensor_r_sequence` using `tensor_R.json5`.
3. Load coupling config with `coupling.load_coupling_config()`.
4. Run `coupling.apply_coupling(L, R, config)` to obtain coupled stream.
5. Compute metrics and append logs using provided logging helpers.

This pipeline ensures the inside-out model (R) remains synchronized with the outside-in stream (L) while respecting stability, coherence, and constraint signals.
