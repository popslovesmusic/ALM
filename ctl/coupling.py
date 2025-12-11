"""
Coupling module for aligning Tensor L (perception) with Tensor R (interpretive model).

This module now supports nonlinear disparity penalties, per-step coherence
scores, and contextual thresholds driven by sliding windows. It provides:

* Per-pair disparity evaluation (tone, hue, intensity, polarity).
* Full-sequence processing that returns per-step metrics and summary values.
* Coupling application that blends cells while respecting agreement/coherence.
* Logging helpers that normalize headers and append metrics into /logs/ CSVs.
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


def _nonlinear_scale(value: float, exponent: float) -> float:
    """Apply a gentle nonlinear scaling (value ** exponent)."""
    if value <= 0:
        return 0.0
    return value ** max(1.0, exponent)


def _ensure_log_file(path: str, header: List[str]) -> None:
    """Create CSV with header if missing or normalize header if changed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
        return

    with open(path, "r", newline="") as f:
        rows = [row for row in csv.reader(f) if row]

    if rows and rows[0] == header:
        return

    existing_header = rows[0] if rows else []
    data_rows = rows[1:] if len(rows) > 1 else []

    # Map existing columns into the new header order
    col_index = {name: idx for idx, name in enumerate(existing_header)}
    normalized: List[List[str]] = []
    for row in data_rows:
        normalized_row = []
        for name in header:
            if name in col_index and col_index[name] < len(row):
                normalized_row.append(row[col_index[name]])
            else:
                normalized_row.append("")
        normalized.append(normalized_row)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(normalized)


def load_coupling_config(path: str = None) -> Config:
    """Load coupling configuration from JSON/JSON5 file."""
    cfg_path = path or os.path.join(os.path.dirname(__file__), "coupling_config.json5")
    with open(cfg_path, "r") as f:
        return json.load(f)


def compute_pair_disparity(l_cell: ChromaticCell, r_cell: ChromaticCell, config: Config) -> Dict[str, float]:
    """Compute disparity and coherence metrics for a single L/R pair."""
    tone_gap = _tone_distance(l_cell["tone"], r_cell["tone"])
    hue_gap = _hue_distance(l_cell.get("hue"), r_cell.get("hue"))
    intensity_gap = abs(float(l_cell["intensity"]) - float(r_cell["intensity"]))
    polarity_disagreement = 1.0 if l_cell.get("polarity", 1) != r_cell.get("polarity", 1) else 0.0

    weights = config.get("weights", {})
    nonlinear_cfg = config.get("nonlinear", {})

    tone_w = weights.get("tone_alignment", 0.5)
    hue_w = weights.get("hue_alignment", 0.3)
    int_w = weights.get("intensity_alignment", 0.2)

    tone_exp = nonlinear_cfg.get("tone_exponent", 1.2)
    hue_exp = nonlinear_cfg.get("hue_exponent", 1.1)
    int_exp = nonlinear_cfg.get("intensity_exponent", 1.05)
    polarity_penalty = nonlinear_cfg.get("polarity_penalty", 0.15)

    denom = max(0.001, tone_w + hue_w + int_w)
    normalized = (
        tone_w * _nonlinear_scale(tone_gap / 6.0, tone_exp)
        + hue_w * _nonlinear_scale(hue_gap / 150.0, hue_exp)
        + int_w * _nonlinear_scale(intensity_gap / 3.0, int_exp)
    ) / denom

    coherence_curve = nonlinear_cfg.get("coherence_curve", 1.0)
    agreement = max(0.0, 1.0 - normalized)
    coherence = max(0.0, agreement ** max(1.0, coherence_curve))
    coherence -= polarity_penalty * polarity_disagreement
    coherence = max(0.0, coherence)

    return {
        "tone_disparity": tone_gap,
        "hue_disparity": hue_gap,
        "intensity_disparity": intensity_gap,
        "polarity_disagreement": polarity_disagreement,
        "agreement": agreement,
        "coherence": coherence,
    }


def _window_stats(values: List[float], window: int) -> List[float]:
    """Return rolling means over the provided window size (inclusive)."""
    if window <= 1:
        return values[:]
    rolling: List[float] = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        subset = values[start : i + 1]
        rolling.append(sum(subset) / len(subset))
    return rolling


def compute_coupling_metrics(l_sequence: List[ChromaticCell], r_sequence: List[ChromaticCell], config: Config) -> Dict[str, float]:
    """Compute aggregate disparity, coherence, and agreement metrics."""
    pairs = list(zip(l_sequence, r_sequence))
    if not pairs:
        return {
            "tone_disparity": 0.0,
            "hue_disparity": 0.0,
            "intensity_disparity": 0.0,
            "polarity_disagreement_rate": 0.0,
            "coherence_score": 1.0,
            "agreement": 1.0,
        }

    per_step = [compute_pair_disparity(l, r, config) for l, r in pairs]
    tone_avg = sum(p["tone_disparity"] for p in per_step) / len(per_step)
    hue_avg = sum(p["hue_disparity"] for p in per_step) / len(per_step)
    intensity_avg = sum(p["intensity_disparity"] for p in per_step) / len(per_step)
    polarity_rate = sum(p["polarity_disagreement"] for p in per_step) / len(per_step)
    coherence_score = sum(p["coherence"] for p in per_step) / len(per_step)
    agreement = sum(p["agreement"] for p in per_step) / len(per_step)

    return {
        "tone_disparity": tone_avg,
        "hue_disparity": hue_avg,
        "intensity_disparity": intensity_avg,
        "polarity_disagreement_rate": polarity_rate,
        "coherence_score": coherence_score,
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
    window = thresholds.get("window", 4)

    coherence_cfg = config.get("coherence", {})
    min_coherence = coherence_cfg.get("min_coherence", 0.35)
    boost_on_agree = coherence_cfg.get("boost_on_agreement", 0.08)
    decay = coherence_cfg.get("decay", 0.05)
    window_gain = coherence_cfg.get("window_gain", 0.05)

    polarity_cfg = config.get("polarity", {})
    prefer_consensus = polarity_cfg.get("prefer_consensus", True)
    flip_if_conflict = polarity_cfg.get("flip_if_conflict", True)

    nonlinear_cfg = config.get("nonlinear", {})
    tone_exp = nonlinear_cfg.get("tone_exponent", 1.2)
    hue_exp = nonlinear_cfg.get("hue_exponent", 1.1)
    int_exp = nonlinear_cfg.get("intensity_exponent", 1.05)

    disparities: List[Dict[str, float]] = [compute_pair_disparity(l, r, config) for l, r in pairs]
    tone_window = _window_stats([d["tone_disparity"] for d in disparities], window)
    hue_window = _window_stats([d["hue_disparity"] for d in disparities], window)
    intensity_window = _window_stats([d["intensity_disparity"] for d in disparities], window)

    coupled: List[ChromaticCell] = []

    for idx, (l_cell, r_cell) in enumerate(pairs):
        disparity = disparities[idx]
        tone_gap = disparity["tone_disparity"]
        hue_gap = disparity["hue_disparity"]
        intensity_gap = disparity["intensity_disparity"]

        tone_blend = int(round((1 - tone_w) * r_cell["tone"] + tone_w * l_cell["tone"])) % 12
        hue_blend = [
            int(round((1 - hue_w) * r + hue_w * l))
            for r, l in zip(r_cell.get("hue", [0, 0, 0]), l_cell.get("hue", [0, 0, 0]))
        ]
        intensity_blend = (1 - intensity_w) * float(r_cell["intensity"]) + intensity_w * float(l_cell["intensity"])

        agreement_penalty = (
            _nonlinear_scale(tone_gap / (tone_max + 1e-6), tone_exp)
            + _nonlinear_scale(hue_gap / (hue_max + 1e-6), hue_exp)
            + _nonlinear_scale(intensity_gap / (intens_max + 1e-6), int_exp)
        ) / 3
        agreement_score = max(0.0, 1.0 - agreement_penalty)

        window_penalty = (
            _nonlinear_scale(tone_window[idx] / (tone_max + 1e-6), tone_exp)
            + _nonlinear_scale(hue_window[idx] / (hue_max + 1e-6), hue_exp)
            + _nonlinear_scale(intensity_window[idx] / (intens_max + 1e-6), int_exp)
        ) / 3

        # Coherence update with sliding-window assistance
        coherence = float(r_cell.get("coherence", 1.0))
        coherence = coherence - decay + (boost_on_agree * agreement_score)
        coherence += window_gain * max(0.0, 1.0 - window_penalty)
        coherence = max(min_coherence, min(1.0, coherence))

        # Polarity handling
        polarity = r_cell.get("polarity", 1)
        if prefer_consensus and l_cell.get("polarity", polarity) != polarity:
            polarity = l_cell.get("polarity", polarity)
            if flip_if_conflict and agreement_score < agreement_min:
                polarity *= -1

        constraint_flag = "OK"
        breaches = sum(
            [
                tone_gap > tone_max,
                hue_gap > hue_max,
                intensity_gap > intens_max,
                agreement_score < agreement_min,
            ]
        )
        if window_penalty > 1.0:
            breaches += 1

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
            "tone_disparity": tone_gap,
            "hue_disparity": hue_gap,
            "intensity_disparity": intensity_gap,
        }
        coupled.append(coupled_cell)

    return coupled


def process_coupling_sequence(
    l_sequence: List[ChromaticCell], r_sequence: List[ChromaticCell], config: Config
) -> Dict[str, Any]:
    """Return coupled stream, per-step metrics, and summary values."""
    coupled = apply_coupling(l_sequence, r_sequence, config)
    per_step = [compute_pair_disparity(l, r, config) for l, r in zip(l_sequence, r_sequence)]
    summary = compute_coupling_metrics(l_sequence, r_sequence, config)
    return {"coupled": coupled, "per_step": per_step, "summary": summary}


def log_coupling_metrics(metrics: Dict[str, float], log_dir: str = "logs") -> None:
    """Append coupling metrics to logs/coupling_metrics.csv."""
    path = os.path.join(log_dir, "coupling_metrics.csv")
    header = [
        "tone_disparity",
        "hue_disparity",
        "intensity_disparity",
        "polarity_disagreement_rate",
        "coherence_score",
        "agreement",
    ]
    _ensure_log_file(path, header)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                round(metrics.get("tone_disparity", metrics.get("tone_error", 0.0)), 3),
                round(metrics.get("hue_disparity", metrics.get("hue_error", 0.0)), 3),
                round(metrics.get("intensity_disparity", metrics.get("intensity_gap", 0.0)), 3),
                round(metrics.get("polarity_disagreement_rate", 0.0), 3),
                round(metrics.get("coherence_score", metrics.get("agreement", 0.0)), 3),
                round(metrics.get("agreement", 0.0), 3),
            ]
        )


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
    header = [
        "input_length",
        "agreement",
        "coherence_mean",
        "polarity_disagreements",
        "warnings",
        "violations",
    ]
    _ensure_log_file(path, header)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                summary.get("input_length", 0),
                round(summary.get("agreement", 0.0), 3),
                round(summary.get("coherence_mean", summary.get("agreement", 0.0)), 3),
                summary.get("polarity_disagreements", 0),
                summary.get("warnings", 0),
                summary.get("violations", 0),
            ]
        )


def summarize_coupled_sequence(coupled: List[ChromaticCell]) -> Dict[str, Any]:
    """Return counts and mean agreement for a coupled stream."""
    if not coupled:
        return {
            "input_length": 0,
            "agreement": 0.0,
            "coherence_mean": 0.0,
            "polarity_disagreements": 0,
            "warnings": 0,
            "violations": 0,
        }
    agreements = [float(cell.get("agreement", 0.0)) for cell in coupled]
    warnings = sum(1 for cell in coupled if cell.get("constraint_flag") == "WARN")
    violations = sum(1 for cell in coupled if cell.get("constraint_flag") == "VIOLATION")
    coherence_values = [float(cell.get("coherence", 0.0)) for cell in coupled]
    polarity_disagreements = sum(
        1 for cell in coupled if cell.get("polarity", 1) in (-1, 0) and cell.get("constraint_flag") != "OK"
    )

    return {
        "input_length": len(coupled),
        "agreement": sum(agreements) / len(agreements),
        "coherence_mean": sum(coherence_values) / len(coherence_values),
        "polarity_disagreements": polarity_disagreements,
        "warnings": warnings,
        "violations": violations,
    }


__all__ = [
    "load_coupling_config",
    "compute_coupling_metrics",
    "compute_pair_disparity",
    "apply_coupling",
    "process_coupling_sequence",
    "log_coupling_metrics",
    "log_tensor_r_behavior",
    "log_end_to_end_summary",
    "summarize_coupled_sequence",
]
