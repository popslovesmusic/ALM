"""
Coupling module for aligning Tensor L (perception) with Tensor R (interpretive model).

This module computes disparity metrics, adjusts Tensor R cells toward Tensor L
when appropriate, and emits coupled cells that encode agreement and stability.
It also provides lightweight logging helpers that append rows to CSV files in
/logs/ without overwriting existing results.
"""
from __future__ import annotations

import csv
import json
import os
from typing import Any, Dict, List

ChromaticCell = Dict[str, Any]
Config = Dict[str, Any]


def _tone_distance(a: int, b: int) -> int:
    """Return the minimum cyclic distance on a 12-tone circle."""
    diff = abs(a - b) % 12
    return min(diff, 12 - diff)


def _hue_distance(a: List[int], b: List[int]) -> float:
    """Average channel difference for RGB hues."""
    if a is None or b is None:
        return 0.0
    distances = [abs(int(x) - int(y)) for x, y in zip(a, b)]
    return sum(distances) / max(1, len(distances))


def _ensure_log_file(path: str, header: List[str]) -> None:
    """Create CSV with header if missing."""
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)


def load_coupling_config(path: str = None) -> Config:
    """Load coupling configuration from JSON/JSON5 file."""
    cfg_path = path or os.path.join(os.path.dirname(__file__), "coupling_config.json5")
    with open(cfg_path, "r") as f:
        return json.load(f)


def compute_coupling_metrics(l_sequence: List[ChromaticCell], r_sequence: List[ChromaticCell], config: Config) -> Dict[str, float]:
    """
    Compute aggregate disparity metrics between L and R sequences.
    Returns a dict with average tone/hue/intensity errors and agreement score.
    """
    pairs = list(zip(l_sequence, r_sequence))
    if not pairs:
        return {"tone_error": 0.0, "hue_error": 0.0, "intensity_gap": 0.0, "agreement": 1.0}

    tone_errors = []
    hue_errors = []
    intensity_gaps = []

    for l_cell, r_cell in pairs:
        tone_errors.append(_tone_distance(l_cell["tone"], r_cell["tone"]))
        hue_errors.append(_hue_distance(l_cell.get("hue"), r_cell.get("hue")))
        intensity_gaps.append(abs(float(l_cell["intensity"]) - float(r_cell["intensity"])) )

    tone_err = sum(tone_errors) / len(tone_errors)
    hue_err = sum(hue_errors) / len(hue_errors)
    intensity_gap = sum(intensity_gaps) / len(intensity_gaps)

    weights = config.get("weights", {})
    tone_w = weights.get("tone_alignment", 0.5)
    hue_w = weights.get("hue_alignment", 0.3)
    int_w = weights.get("intensity_alignment", 0.2)

    denom = max(0.001, tone_w + hue_w + int_w)
    agreement = max(0.0, 1.0 - (tone_w * (tone_err / 6.0) + hue_w * (hue_err / 100.0) + int_w * (intensity_gap / 3.0)) / denom)

    return {
        "tone_error": tone_err,
        "hue_error": hue_err,
        "intensity_gap": intensity_gap,
        "agreement": agreement,
    }


def apply_coupling(l_sequence: List[ChromaticCell], r_sequence: List[ChromaticCell], config: Config) -> List[ChromaticCell]:
    """
    Bind Tensor L and Tensor R into coupled cells.

    Strategy:
    - Blend tone/intensity values toward L using weights
    - Keep hue from R but bias toward L based on hue alignment weight
    - Update coherence based on per-cell agreement and config thresholds
    - Enforce polarity consensus when conflicts arise
    """
    pairs = list(zip(l_sequence, r_sequence))
    if not pairs:
        return []

    weights = config.get("weights", {})
    tone_w = weights.get("tone_alignment", 0.55)
    hue_w = weights.get("hue_alignment", 0.25)
    intensity_w = weights.get("intensity_alignment", 0.2)

    thresholds = config.get("thresholds", {})
    tone_max = thresholds.get("tone_error_max", 4)
    hue_max = thresholds.get("hue_error_max", 50)
    intens_max = thresholds.get("intensity_gap_max", 1.5)
    agreement_min = thresholds.get("agreement_min", 0.4)

    coherence_cfg = config.get("coherence", {})
    min_coherence = coherence_cfg.get("min_coherence", 0.35)
    boost_on_agree = coherence_cfg.get("boost_on_agreement", 0.08)
    decay = coherence_cfg.get("decay", 0.05)

    polarity_cfg = config.get("polarity", {})
    prefer_consensus = polarity_cfg.get("prefer_consensus", True)
    flip_if_conflict = polarity_cfg.get("flip_if_conflict", True)

    coupled: List[ChromaticCell] = []

    for l_cell, r_cell in pairs:
        tone_gap = _tone_distance(l_cell["tone"], r_cell["tone"])
        hue_gap = _hue_distance(l_cell.get("hue"), r_cell.get("hue"))
        intensity_gap = abs(float(l_cell["intensity"]) - float(r_cell["intensity"]))

        tone_blend = int(round((1 - tone_w) * r_cell["tone"] + tone_w * l_cell["tone"])) % 12
        hue_blend = [
            int(round((1 - hue_w) * r + hue_w * l))
            for r, l in zip(r_cell.get("hue", [0, 0, 0]), l_cell.get("hue", [0, 0, 0]))
        ]
        intensity_blend = (1 - intensity_w) * float(r_cell["intensity"]) + intensity_w * float(l_cell["intensity"])

        agreement_penalty = (tone_gap / (tone_max + 1e-6) + hue_gap / (hue_max + 1e-6) + intensity_gap / (intens_max + 1e-6)) / 3
        agreement_score = max(0.0, 1.0 - agreement_penalty)

        # Coherence update
        coherence = float(r_cell.get("coherence", 1.0))
        coherence = max(min_coherence, coherence - decay + (boost_on_agree * agreement_score))

        # Polarity handling
        polarity = r_cell.get("polarity", 1)
        if prefer_consensus and l_cell.get("polarity", polarity) != polarity:
            polarity = l_cell.get("polarity", polarity)
            if flip_if_conflict and agreement_score < agreement_min:
                polarity *= -1

        constraint_flag = "OK"
        breaches = sum([
            tone_gap > tone_max,
            hue_gap > hue_max,
            intensity_gap > intens_max,
            agreement_score < agreement_min,
        ])
        if breaches == 1:
            constraint_flag = "WARN"
        elif breaches > 1:
            constraint_flag = "VIOLATION"

        coupled_cell: ChromaticCell = {
            "tone": tone_blend,
            "hue": hue_blend,
            "intensity": intensity_blend,
            "polarity": polarity,
            "timestamp": l_cell.get("timestamp", r_cell.get("timestamp", 0.0)),
            "agreement": agreement_score,
            "coherence": coherence,
            "constraint_flag": constraint_flag,
        }
        coupled.append(coupled_cell)

    return coupled


def log_coupling_metrics(metrics: Dict[str, float], log_dir: str = "logs") -> None:
    """Append coupling metrics to logs/coupling_metrics.csv."""
    path = os.path.join(log_dir, "coupling_metrics.csv")
    _ensure_log_file(path, ["tone_error", "hue_error", "intensity_gap", "agreement"])
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            round(metrics.get("tone_error", 0.0), 3),
            round(metrics.get("hue_error", 0.0), 3),
            round(metrics.get("intensity_gap", 0.0), 3),
            round(metrics.get("agreement", 0.0), 3),
        ])


def log_tensor_r_behavior(r_sequence: List[ChromaticCell], log_dir: str = "logs") -> None:
    """Append simple statistics about a Tensor R sequence."""
    if not r_sequence:
        return
    tones = [cell["tone"] for cell in r_sequence]
    intensities = [float(cell["intensity"]) for cell in r_sequence]
    coherences = [float(cell.get("coherence", 1.0)) for cell in r_sequence]

    mean_tone = sum(tones) / len(tones)
    mean_intensity = sum(intensities) / len(intensities)
    mean_coherence = sum(coherences) / len(coherences)

    path = os.path.join(log_dir, "tensor_r_behavior.csv")
    _ensure_log_file(path, ["mean_tone", "mean_intensity", "mean_coherence", "length"])
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            round(mean_tone, 3),
            round(mean_intensity, 3),
            round(mean_coherence, 3),
            len(r_sequence),
        ])


def log_end_to_end_summary(summary: Dict[str, Any], log_dir: str = "logs") -> None:
    """Append a short end-to-end summary row."""
    path = os.path.join(log_dir, "end_to_end_summary.csv")
    _ensure_log_file(path, ["input_length", "agreement", "warnings", "violations"])
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            summary.get("input_length", 0),
            round(summary.get("agreement", 0.0), 3),
            summary.get("warnings", 0),
            summary.get("violations", 0),
        ])


def summarize_coupled_sequence(coupled: List[ChromaticCell]) -> Dict[str, Any]:
    """Return counts and mean agreement for a coupled stream."""
    if not coupled:
        return {"input_length": 0, "agreement": 0.0, "warnings": 0, "violations": 0}
    agreements = [float(cell.get("agreement", 0.0)) for cell in coupled]
    warnings = sum(1 for cell in coupled if cell.get("constraint_flag") == "WARN")
    violations = sum(1 for cell in coupled if cell.get("constraint_flag") == "VIOLATION")
    return {
        "input_length": len(coupled),
        "agreement": sum(agreements) / len(agreements),
        "warnings": warnings,
        "violations": violations,
    }


__all__ = [
    "load_coupling_config",
    "compute_coupling_metrics",
    "apply_coupling",
    "log_coupling_metrics",
    "log_tensor_r_behavior",
    "log_end_to_end_summary",
    "summarize_coupled_sequence",
]
