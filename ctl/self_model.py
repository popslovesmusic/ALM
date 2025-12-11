"""Internal self-model for Phase 4."""

import json
import os
from dataclasses import dataclass, replace
from typing import Dict, List

from ctl.feedback import FeedbackSignal


@dataclass
class SelfModel:
    posture: str
    stability: float
    biases: Dict[str, float]
    recent_scores: List[float]
    reflection: float


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "self_model_config.json5")


def load_self_model_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def initialize_self_model(config: Dict | None = None) -> SelfModel:
    cfg = config or load_self_model_config()
    return SelfModel(
        posture=cfg["posture"],
        stability=1.0,
        biases={"cadence": cfg["biases"]["cadence"], "polarity": cfg["biases"]["polarity"], "window": cfg["biases"]["window"]},
        recent_scores=[],
        reflection=1.0,
    )


def _clamp_bias(value: float, limit: float = 0.5) -> float:
    return max(-limit, min(limit, value))


def update_self_model(
    self_model: SelfModel,
    feedback: FeedbackSignal,
    meta_consistency: float,
    config: Dict | None = None,
) -> SelfModel:
    cfg = config or load_self_model_config()
    smoothing = cfg["smoothing"]

    updated_biases = {
        key: _clamp_bias(self_model.biases.get(key, 0.0) + feedback.adjustments.get(key, 0.0))
        for key in set(self_model.biases) | set(feedback.adjustments)
    }

    stability = (self_model.stability * smoothing) + ((1 - smoothing) * meta_consistency)
    stability = round(_clamp_bias(stability, 1.0), 3)

    posture = self_model.posture
    if feedback.posture == "amplify" and meta_consistency >= cfg["posture_thresholds"]["amplify"]:
        posture = "predictive"
    elif feedback.posture == "reframe" and meta_consistency <= cfg["posture_thresholds"]["stabilize"]:
        posture = "reactive"
    elif feedback.posture == "stabilize":
        posture = "stable"

    recent_scores = (self_model.recent_scores + [meta_consistency])[-5:]
    reflection = round((stability + (sum(recent_scores) / len(recent_scores))) / 2 if recent_scores else stability, 3)

    return replace(
        self_model,
        posture=posture,
        stability=stability,
        biases=updated_biases,
        recent_scores=recent_scores,
        reflection=reflection,
    )


def snapshot_self_model(self_model: SelfModel) -> Dict:
    return {
        "posture": self_model.posture,
        "stability": self_model.stability,
        "biases": self_model.biases,
        "recent_scores": list(self_model.recent_scores),
        "reflection": self_model.reflection,
    }


def write_self_model_snapshot(self_model: SelfModel, log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_self_model_config()
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, cfg["logging"]["log_file"])

    snapshot = snapshot_self_model(self_model)
    header = "posture,stability,cadence_bias,polarity_bias,window_bias,reflection\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{snapshot['posture']},{snapshot['stability']},{snapshot['biases'].get('cadence',0)},{snapshot['biases'].get('polarity',0)},{snapshot['biases'].get('window',0)},{snapshot['reflection']}\n"
        )
    return path


__all__ = [
    "SelfModel",
    "initialize_self_model",
    "update_self_model",
    "snapshot_self_model",
    "write_self_model_snapshot",
    "load_self_model_config",
]
