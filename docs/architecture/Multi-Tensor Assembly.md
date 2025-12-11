# Multi-Tensor Assembly

**Project:** `ALM/`
**Module:** `ctl/multi_tensor.py`
**Role:** Coordinate multiple Tensor R fibers in parallel, aggregate their states, and compare them to Tensor L for coherence-aware alignment.

---

## 1. Motivation
Single Tensor R fibers capture a particular interpretive stream. Running multiple fibers in parallel enables stereo-like relational views, domain-specialized interpretations, and robustness when one fiber drifts. The assembly layer manages these fibers deterministically and exposes aggregated representations for downstream visualization or coupling checks.

---

## 2. Interfaces
* **Input:** Shared Tensor L sequence (list of ChromaticCell dictionaries).
* **Per-fiber config:** Tensor R configs (`tensor_R.json5`-style dicts).
* **Coupling config (optional):** For computing disparity/coherence metrics per fiber.

### Key functions/classes
* `MultiTensorAssembly` — orchestrator holding fiber configs and coupling config.
  * `run_r_fibers(L)` — build Tensor R sequences for each config.
  * `aggregate_states(r_sequences, weights=None)` — weighted merge of parallel R states (tone/intensity/hue/polarity/coherence).
  * `summarize_fibers(L, r_sequences)` — coupling metrics per fiber relative to L (if coupling config provided).
  * `run_full(L, weights=None)` — convenience wrapper returning all R fibers, aggregated stream, and optional coupling summaries.
  * `compare_aggregated_to_l(L, aggregated)` — disparity/coherence between aggregated R and L.
* `run_multi_tensor(L, r_configs, coupling_config=None, weights=None)` — stateless convenience helper.
* `couple_fiber_snapshots(L, r_sequences, coupling_config)` — per-fiber coupled outputs (per-step + summary) for visualization.

---

## 3. Aggregation Strategy
For each time index (truncated to the shortest fiber length):
* Tone: weighted average then modulo 12.
* Hue: channel-wise weighted sums, rounded to integers.
* Intensity: weighted average across fibers.
* Coherence: weighted average, retaining fiber stability signals.
* Polarity: weighted vote; sign determines output polarity.

Weights default to uniform when unspecified; inputs are normalized to sum to 1.0.

---

## 4. Coupling & Monitoring
When a coupling config is provided, each fiber is compared against L using the nonlinear coupling metrics (tone/hue/intensity disparity, polarity disagreement rate, coherence score, agreement). The assembly can also compare the aggregated stream back to L, surfacing whether the fused representation remains faithful.

---

## 5. Logging & Visualization Hooks
The assembly itself remains pure, but its outputs can be passed into `ctl.visualization` helpers to export tone/hue/intensity trajectories, or into `ctl.coupling.log_*` utilities for CSV append-only logging. This keeps Phase 2 visualization and monitoring pipelines consistent across single- and multi-fiber runs.

---

## 6. Extension Ideas
* Add domain tags per fiber and perform tag-weighted aggregation.
* Introduce temporal staggering between fibers for echo-like effects.
* Integrate memory/state sharing primitives for coordinated polarity decisions.
* Provide built-in snapshot exporters for batched experiments.
