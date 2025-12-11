"""Meta-consistency metrics for Phase 4."""

import json
import os
from typing import Dict, Sequence

from ctl.meta_symbols import MetaSymbol
from ctl.narrative import NarrativeEpisode
from ctl.self_model import SelfModel

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "meta_consistency_config.json5")


def load_meta_consistency_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _alignment_score(episodes: Sequence[NarrativeEpisode]) -> float:
    if len(episodes) < 2:
        return 1.0 if episodes else 0.0
    matches = 0
    for prev, curr in zip(episodes, episodes[1:]):
        if prev.theme == curr.theme:
            matches += 1
    return matches / (len(episodes) - 1)


def _recurrence_score(meta_symbols: Sequence[MetaSymbol], window: int) -> float:
    if not meta_symbols:
        return 0.0
    window = max(1, window)
    relations = [m.relation for m in meta_symbols]
    counts: Dict[str, int] = {}
    for rel in relations[-window:]:
        counts[rel] = counts.get(rel, 0) + 1
    return max(counts.values()) / window


def _drift_penalty(episodes: Sequence[NarrativeEpisode], salience_floor: float) -> float:
    if not episodes:
        return 0.0
    below = len([e for e in episodes if e.salience < salience_floor])
    return below / len(episodes)


def evaluate_meta_consistency(
    meta_symbols: Sequence[MetaSymbol],
    episodes: Sequence[NarrativeEpisode],
    self_model: SelfModel,
    config: Dict | None = None,
) -> Dict:
    cfg = config or load_meta_consistency_config()
    weights = cfg["weights"]
    thresholds = cfg["thresholds"]

    alignment = _alignment_score(episodes)
    posture_stability = max(0.0, min(1.0, self_model.stability))
    recurrence = _recurrence_score(meta_symbols, cfg["recurrence"]["window"])
    drift = _drift_penalty(episodes, thresholds["salience_floor"])

    reflection_stability = (
        (alignment * weights["alignment"])
        + (posture_stability * weights["posture"])
        + (recurrence * weights["recurrence"])
        - (drift * weights["drift"])
    )
    reflection_stability = max(0.0, min(1.0, reflection_stability))

    return {
        "alignment": round(alignment, 3),
        "posture_stability": round(posture_stability, 3),
        "recurrence": round(recurrence, 3),
        "drift_penalty": round(drift, 3),
        "reflection_stability": round(reflection_stability, 3),
    }


def write_meta_consistency_metrics(metrics: Dict, log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_meta_consistency_config()
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, cfg["logging"]["log_file"])

    header = "alignment,posture_stability,recurrence,drift_penalty,reflection_stability\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{metrics['alignment']},{metrics['posture_stability']},{metrics['recurrence']},{metrics['drift_penalty']},{metrics['reflection_stability']}\n"
        )
    return path


__all__ = [
    "evaluate_meta_consistency",
    "write_meta_consistency_metrics",
    "load_meta_consistency_config",
]
