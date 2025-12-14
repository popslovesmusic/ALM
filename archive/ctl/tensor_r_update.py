"""
tensor_r_update.py

Discrete Tensor R update model for the Chromatic Interpretive Fiber.

This module assumes:
- Tensor L cells are dicts with keys: "tone", "hue", "intensity", "polarity", "timestamp"
- Tensor R cells are dicts with keys: "tone", "hue", "intensity", "polarity",
  "timestamp", "coherence", "constraint_flag"

Config is expected to be a Python dict with the same structure as tensor_R.json5.
"""

from typing import Dict, List, Any
import math
import copy

from ctl import memory


ChromaticCell = Dict[str, Any]
Config = Dict[str, Any]


# --------- Utility functions --------- #

def _blend_tone(prev: int, curr: int, lam: float) -> int:
    """
    Blend tones on a 12-tone circle using weighted average + modulo.
    """
    # Simple linear blend, then round and mod 12
    blended = lam * prev + (1.0 - lam) * curr
    tone = int(round(blended)) % 12
    return tone


def _tone_trend(prev_l: int, curr_l: int) -> int:
    """
    Compute a simple discrete trend between two L tones.
    No sophisticated cyclic handling yet; can be extended later.
    """
    return curr_l - prev_l


def _apply_trend(tone: int, trend: int, alpha: float) -> int:
    """
    Apply a fraction of the trend to a tone, modulo 12.
    """
    updated = tone + alpha * trend
    return int(round(updated)) % 12


def _blend_hue(prev: List[int], curr: List[int], weight: float) -> List[int]:
    """
    Linear interpolation between two RGB hues.
    prev, curr: [R, G, B] with 0-255.
    weight: fraction of curr to blend in each step.
    """
    if prev is None:
        return curr[:]  # fallback
    blended = []
    for p, c in zip(prev, curr):
        val = (1.0 - weight) * p + weight * c
        blended.append(max(0, min(255, int(round(val)))))
    return blended


def _exp_smooth(prev: float, curr: float, beta: float) -> float:
    """
    Exponential smoothing for scalar values.
    """
    return beta * prev + (1.0 - beta) * curr


# Memory hooks (stubs for now)

def _resolve_memory_config(memory_config: Config | None) -> Config:
    """Return provided memory config or load default."""
    if memory_config is not None:
        return memory_config
    try:
        return memory.load_memory_config()
    except FileNotFoundError:
        return {}


# --------- Initialization --------- #

def init_tensor_r_cell(l_cell: ChromaticCell, config: Config) -> ChromaticCell:
    """
    Initialize R[0] from L[0].
    """
    coherence_enabled = config.get("behaviors", {}).get("coherence_field", {}).get("enabled", True)
    default_coherence = config.get("behaviors", {}).get("coherence_field", {}).get("default_value", 1.0)

    r_cell: ChromaticCell = {
        "tone": l_cell["tone"],
        "hue": l_cell["hue"][:],
        "intensity": 1.0,
        "polarity": 1,
        "timestamp": l_cell.get("timestamp", 0.0),
        "coherence": default_coherence if coherence_enabled else 0.0,
        "constraint_flag": "OK",
    }
    return r_cell


# --------- Per-step update --------- #

def update_tensor_r_cell(
    prev_r: ChromaticCell,
    l_prev: ChromaticCell,
    l_curr: ChromaticCell,
    config: Config,
    flip_history: List[int] = None,
    memory_state: Dict[str, Any] | None = None,
    memory_config: Config | None = None,
) -> ChromaticCell:
    """
    Compute R[i] given:
    - previous R[i-1] = prev_r
    - L[i-1] = l_prev
    - L[i]   = l_curr
    - config: Tensor R config dict (from tensor_R.json5)
    - flip_history: list of past polarity_R values (for over-oscillation detection)
    - memory_state: optional mutable memory accumulator from ctl.memory
    - memory_config: optional memory config dict (defaults to ctl/memory_config.json5)

    Returns a new R[i] cell.
    """
    behaviors = config.get("behaviors", {})
    smoothing_cfg = behaviors.get("smoothing", {})
    prediction_cfg = behaviors.get("prediction", {})
    hue_cfg = behaviors.get("hue_expectation", {})
    intensity_cfg = behaviors.get("intensity_integration", {})
    polarity_cfg = behaviors.get("polarity_integration", {})
    mem_cfg = behaviors.get("memory_integration", {})
    tone_constr_cfg = behaviors.get("tone_constraints", {})
    intens_constr_cfg = behaviors.get("intensity_constraints", {})
    coherence_cfg = behaviors.get("coherence_field", {})

    lam = smoothing_cfg.get("lambda", 0.7)
    alpha = prediction_cfg.get("alpha", 0.2)
    hue_weight = hue_cfg.get("weight", 0.2)
    beta = intensity_cfg.get("beta", 0.85)
    intensity_max = intensity_cfg.get("max_value", 3.0)
    flip_on_input_change = polarity_cfg.get("flip_on_input_change", True)
    max_flips_per_window = polarity_cfg.get("max_flips_per_window", 4)
    flip_window = polarity_cfg.get("flip_window", 16)
    coherence_gain = mem_cfg.get("coherence_gain", 0.2)
    intensity_gain = mem_cfg.get("intensity_gain", 0.1)
    max_tone_jump = tone_constr_cfg.get("max_jump", 5)
    saturation_factor = intens_constr_cfg.get("saturation_factor", 0.5)
    coherence_enabled = coherence_cfg.get("enabled", True)
    mem_state: Dict[str, Any] | None = memory_state if mem_cfg.get("enabled", True) else None
    mem_cfg_resolved = _resolve_memory_config(memory_config) if mem_state is not None else {}

    r = copy.deepcopy(prev_r)
    r["constraint_flag"] = "OK"  # reset by default

    # --- Tone smoothing ---
    if smoothing_cfg.get("enabled", True):
        tone_smoothed = _blend_tone(prev_r["tone"], l_curr["tone"], lam)
    else:
        tone_smoothed = prev_r["tone"]

    # --- Tone prediction ---
    if prediction_cfg.get("enabled", True):
        trend = _tone_trend(l_prev["tone"], l_curr["tone"])
        tone_pred = _apply_trend(tone_smoothed, trend, alpha)
    else:
        tone_pred = tone_smoothed

    r["tone"] = tone_pred

    # --- Hue expectation ---
    if hue_cfg.get("enabled", True):
        r["hue"] = _blend_hue(prev_r["hue"], l_curr["hue"], hue_weight)
    else:
        r["hue"] = prev_r["hue"][:]

    # --- Intensity integration ---
    if intensity_cfg.get("enabled", True):
        r["intensity"] = _exp_smooth(prev_r["intensity"], l_curr["intensity"], beta)
    else:
        r["intensity"] = prev_r["intensity"]

    # --- Polarity integration ---
    if polarity_cfg.get("enabled", True):
        if flip_on_input_change and (l_curr["polarity"] != l_prev["polarity"]):
            r["polarity"] = -prev_r["polarity"]
        else:
            r["polarity"] = prev_r["polarity"]
    else:
        r["polarity"] = prev_r["polarity"]

    # --- Timestamp (keep simple: align with L for now) ---
    r["timestamp"] = l_curr.get("timestamp", prev_r.get("timestamp", 0.0) + 1.0)

    # --- Coherence / memory integration ---
    if coherence_enabled:
        coherence = prev_r.get("coherence", 1.0)

        if mem_state is not None and memory.match_to_memory_profile(l_curr, mem_state, mem_cfg_resolved):
            coherence += coherence_gain

        coherence = max(0.0, min(1.0, coherence))
        r["coherence"] = coherence
        r["intensity"] += coherence * intensity_gain

    # --- Snap to memory peaks (tone/hue) ---
    if mem_state is not None:
        r["tone"] = memory.snap_to_nearest_memory_tone(r["tone"], mem_state, mem_cfg_resolved)
        r["hue"] = memory.snap_to_nearest_memory_hue(r["hue"], mem_state, mem_cfg_resolved)

    # --- Tone constraint (max jump) ---
    if tone_constr_cfg.get("enabled", True):
        tone_jump = abs(r["tone"] - prev_r["tone"])
        if tone_jump > max_tone_jump:
            r["constraint_flag"] = "WARN"
            r["tone"] = prev_r["tone"]

    # --- Intensity saturation constraint ---
    if intens_constr_cfg.get("enabled", True):
        if r["intensity"] > intensity_max:
            r["constraint_flag"] = "WARN"
            r["intensity"] *= saturation_factor

    # --- Polarity over-oscillation constraint ---
    if polarity_cfg.get("enabled", True) and flip_history is not None:
        # Flip history is a list of past polarity_R values (e.g., last N)
        recent = flip_history[-flip_window:]
        flips = 0
        for a, b in zip(recent, recent[1:]):
            if a != b:
                flips += 1
        if flips > max_flips_per_window:
            r["constraint_flag"] = "VIOLATION"
            r["polarity"] = 1  # reset structural polarity

    # --- Memory reinforcement update ---
    if mem_state is not None:
        updated_mem = memory.update_memory_state(mem_state, l_curr, mem_cfg_resolved, r.get("coherence", 1.0))
        mem_state.clear()
        mem_state.update(updated_mem)

    return r


# --------- Sequence-level helper --------- #

def update_tensor_r_sequence(
    l_sequence: List[ChromaticCell],
    config: Config,
    memory_config: Config | None = None,
) -> List[ChromaticCell]:
    """
    Convenience function:
    Given a full L sequence, build an R sequence by:
    - Initializing R[0] from L[0]
    - Iteratively updating R[i] using L[i-1], L[i]

    Returns list of R cells.
    """
    if not l_sequence:
        return []

    r_sequence: List[ChromaticCell] = []
    flip_history: List[int] = []
    mem_state = memory.init_memory_state() if config.get("behaviors", {}).get("memory_integration", {}).get("enabled", True) else None

    # Initialize R[0]
    r0 = init_tensor_r_cell(l_sequence[0], config)
    r_sequence.append(r0)
    flip_history.append(r0["polarity"])

    # Iterate
    for i in range(1, len(l_sequence)):
        prev_r = r_sequence[-1]
        l_prev = l_sequence[i - 1]
        l_curr = l_sequence[i]
        r_i = update_tensor_r_cell(
            prev_r,
            l_prev,
            l_curr,
            config,
            flip_history,
            memory_state=mem_state,
            memory_config=memory_config,
        )
        r_sequence.append(r_i)
        flip_history.append(r_i["polarity"])

    return r_sequence
