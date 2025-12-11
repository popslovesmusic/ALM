"""Coherence feedback layer for Phase 4."""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Sequence

from ctl.meta_symbols import MetaSymbol, summarize_meta_symbols
from ctl.narrative import NarrativeEpisode


@dataclass
class FeedbackSignal:
    posture: str
    adjustments: Dict[str, float]
    confidence: float
    notes: str


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "feedback_config.json5")


def load_feedback_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _clamp(value: float, limit: float) -> float:
    return max(-limit, min(limit, value))


def _mean_salience(episodes: Sequence[NarrativeEpisode]) -> float:
    if not episodes:
        return 0.0
    return sum(ep.salience for ep in episodes) / len(episodes)


def compute_feedback(
    meta_symbols: Sequence[MetaSymbol],
    episodes: Sequence[NarrativeEpisode],
    stability: float,
    config: Dict | None = None,
) -> FeedbackSignal:
    cfg = config or load_feedback_config()
    weights = cfg["weights"]
    thresholds = cfg["thresholds"]

    meta_summary = summarize_meta_symbols(meta_symbols)
    meta_term = meta_summary["mean_weight"] * weights["meta_weight"]
    narrative_term = _mean_salience(episodes) * weights["narrative_weight"]
    stability_term = stability * weights["stability_weight"]

    blended = meta_term + narrative_term + stability_term

    if blended >= thresholds["amplify"]:
        posture = "amplify"
    elif blended <= thresholds["reframe"]:
        posture = "reframe"
    else:
        posture = "stabilize"

    max_delta = cfg["adjustments"]["max_delta"]
    adjustments = {
        "cadence": _clamp(cfg["adjustments"]["cadence_bias"] * (1 if posture == "amplify" else -1 if posture == "reframe" else 0), max_delta),
        "polarity": _clamp(cfg["adjustments"]["polarity_bias"] * (1 if posture == "stabilize" else -1 if posture == "reframe" else 1), max_delta),
        "window": _clamp(float(cfg["adjustments"]["window_bias"]) if posture == "amplify" else -float(cfg["adjustments"]["window_bias"]) if posture == "reframe" else 0.0, max_delta),
    }

    confidence = round(min(1.0, blended), 3)
    notes = f"dominant={meta_summary['dominant_relation']} salience={_mean_salience(episodes):.3f}"

    return FeedbackSignal(
        posture=posture,
        adjustments=adjustments,
        confidence=confidence,
        notes=notes,
    )


def write_feedback_signal(signal: FeedbackSignal, log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_feedback_config()
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, cfg["logging"]["log_file"])

    header = "posture,cadence_delta,polarity_delta,window_delta,confidence,notes\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{signal.posture},{signal.adjustments['cadence']},{signal.adjustments['polarity']},{signal.adjustments['window']},{signal.confidence},{signal.notes}\n"
        )
    return path


__all__ = [
    "FeedbackSignal",
    "compute_feedback",
    "write_feedback_signal",
    "load_feedback_config",
]
