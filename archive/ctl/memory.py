"""Chromatic Memory System utilities for CTL.

This module stores and retrieves tone/hue attractors that reinforce over time
from L-stream observations. The goal is to provide stable peaks that Tensor R
can snap to and to expose quick similarity checks for coherence boosting.
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Tuple

ChromaticCell = Dict[str, Any]
Config = Dict[str, Any]
MemoryState = Dict[str, Any]


def load_memory_config(path: str | None = None) -> Config:
    """Load memory configuration from JSON/JSON5 file."""
    cfg_path = path or os.path.join(os.path.dirname(__file__), "memory_config.json5")
    with open(cfg_path, "r") as f:
        return json.load(f)


def init_memory_state() -> MemoryState:
    """Return an empty memory state container."""
    return {
        "tone_peaks": [],
        "hue_peaks": [],
        "updates": 0,
    }


# --- distance helpers ---

def _tone_distance(a: int, b: int) -> int:
    diff = abs(a - b) % 12
    return min(diff, 12 - diff)


def _hue_distance(a: List[int], b: List[int]) -> float:
    if a is None or b is None:
        return 0.0
    gaps = [abs(int(x) - int(y)) for x, y in zip(a, b)]
    return sum(gaps) / max(1, len(gaps))


# --- peak maintenance ---

def _decay_peaks(peaks: List[Dict[str, Any]], decay: float, min_strength: float) -> List[Dict[str, Any]]:
    decayed: List[Dict[str, Any]] = []
    for peak in peaks:
        new_strength = peak["strength"] * max(0.0, 1.0 - decay)
        if new_strength >= min_strength:
            updated = dict(peak)
            updated["strength"] = new_strength
            decayed.append(updated)
    return decayed


def _nearest_tone_peak(peaks: List[Dict[str, Any]], tone: int) -> Tuple[Dict[str, Any] | None, int]:
    if not peaks:
        return None, 12
    distances = [(_tone_distance(p["tone"], tone), p) for p in peaks]
    distance, peak = min(distances, key=lambda t: t[0])
    return peak, distance


def _nearest_hue_peak(peaks: List[Dict[str, Any]], hue: List[int]) -> Tuple[Dict[str, Any] | None, float]:
    if not peaks:
        return None, 255.0
    distances = [(_hue_distance(p["hue"], hue), p) for p in peaks]
    distance, peak = min(distances, key=lambda t: t[0])
    return peak, distance


def _reinforce_tone_peak(peaks: List[Dict[str, Any]], tone: int, strength: float, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    min_sep = cfg.get("min_separation", 2)
    max_peaks = cfg.get("max_peaks", 12)

    existing, distance = _nearest_tone_peak(peaks, tone)
    if existing and distance <= min_sep:
        existing = dict(existing)
        existing["strength"] += strength
        peaks = [existing if p is existing else p for p in peaks]
    elif len(peaks) < max_peaks:
        peaks.append({"tone": tone % 12, "strength": strength})
    return peaks


def _reinforce_hue_peak(peaks: List[Dict[str, Any]], hue: List[int], strength: float, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    min_dist = cfg.get("min_distance", 15.0)
    max_peaks = cfg.get("max_peaks", 8)

    existing, distance = _nearest_hue_peak(peaks, hue)
    if existing and distance <= min_dist:
        existing = dict(existing)
        existing["strength"] += strength
        peaks = [existing if p is existing else p for p in peaks]
    elif len(peaks) < max_peaks:
        peaks.append({"hue": [int(x) for x in hue], "strength": strength})
    return peaks


# --- public API ---

def update_memory_state(
    memory_state: MemoryState,
    l_cell: ChromaticCell,
    config: Config,
    coherence: float = 1.0,
) -> MemoryState:
    """
    Apply decay and reinforcement using the incoming L cell.

    Strength is biased by intensity and coherence to favor salient events.
    Returns a new memory state dictionary (input is not mutated).
    """
    peaks_cfg = config.get("peaks", {})
    tone_cfg = peaks_cfg.get("tone", {})
    hue_cfg = peaks_cfg.get("hue", {})
    matching_cfg = config.get("matching", {})

    intensity_weight = matching_cfg.get("intensity_weight", 0.2)
    coherence_bias = matching_cfg.get("coherence_bias", 0.1)

    tone_peaks = _decay_peaks(memory_state.get("tone_peaks", []), tone_cfg.get("decay", 0.02), tone_cfg.get("min_strength", 0.05))
    hue_peaks = _decay_peaks(memory_state.get("hue_peaks", []), hue_cfg.get("decay", 0.02), hue_cfg.get("min_strength", 0.05))

    boost = 1.0 + intensity_weight * float(l_cell.get("intensity", 1.0)) + coherence_bias * float(coherence)

    tone_peaks = _reinforce_tone_peak(tone_peaks, int(l_cell.get("tone", 0)), boost * tone_cfg.get("reinforce_gain", 0.25), tone_cfg)
    hue_peaks = _reinforce_hue_peak(hue_peaks, l_cell.get("hue", [0, 0, 0]), boost * hue_cfg.get("reinforce_gain", 0.2), hue_cfg)

    return {
        "tone_peaks": tone_peaks,
        "hue_peaks": hue_peaks,
        "updates": int(memory_state.get("updates", 0)) + 1,
    }


def match_to_memory_profile(l_cell: ChromaticCell, memory_state: MemoryState, config: Config) -> bool:
    """Return True when tone+hue fall within tolerance of strong peaks."""
    matching_cfg = config.get("matching", {})
    tone_tol = matching_cfg.get("tone_tolerance", 2)
    hue_tol = matching_cfg.get("hue_tolerance", 25.0)
    min_strength = matching_cfg.get("min_match_strength", 0.12)

    tone_peak, tone_gap = _nearest_tone_peak(memory_state.get("tone_peaks", []), int(l_cell.get("tone", 0)))
    hue_peak, hue_gap = _nearest_hue_peak(memory_state.get("hue_peaks", []), l_cell.get("hue", [0, 0, 0]))

    tone_match = tone_peak and tone_gap <= tone_tol and tone_peak.get("strength", 0.0) >= min_strength
    hue_match = hue_peak and hue_gap <= hue_tol and hue_peak.get("strength", 0.0) >= min_strength

    if not tone_match and not hue_match:
        return False

    score = 0.0
    if tone_match:
        score += tone_peak["strength"] * max(0.0, 1 - tone_gap / max(1.0, tone_tol))
    if hue_match:
        score += hue_peak["strength"] * max(0.0, 1 - hue_gap / max(1.0, hue_tol))

    return score >= min_strength


def snap_to_nearest_memory_tone(tone: int, memory_state: MemoryState, config: Config) -> int:
    """Snap tone to strongest nearby peak when available."""
    matching_cfg = config.get("matching", {})
    tone_tol = matching_cfg.get("tone_tolerance", 2)
    min_strength = matching_cfg.get("min_match_strength", 0.12)

    peak, distance = _nearest_tone_peak(memory_state.get("tone_peaks", []), tone)
    if peak and distance <= tone_tol and peak.get("strength", 0.0) >= min_strength:
        return int(peak["tone"]) % 12
    return tone % 12


def snap_to_nearest_memory_hue(hue: List[int], memory_state: MemoryState, config: Config) -> List[int]:
    """Snap hue to nearest stable hue peak when found."""
    matching_cfg = config.get("matching", {})
    hue_tol = matching_cfg.get("hue_tolerance", 25.0)
    min_strength = matching_cfg.get("min_match_strength", 0.12)

    peak, distance = _nearest_hue_peak(memory_state.get("hue_peaks", []), hue)
    if peak and distance <= hue_tol and peak.get("strength", 0.0) >= min_strength:
        return [int(x) for x in peak["hue"]]
    return [int(x) for x in hue]


__all__ = [
    "init_memory_state",
    "load_memory_config",
    "update_memory_state",
    "match_to_memory_profile",
    "snap_to_nearest_memory_tone",
    "snap_to_nearest_memory_hue",
]
