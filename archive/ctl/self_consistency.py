"""
Self-consistency evaluation for the emergent cognition pipeline.

Combines symbol, cluster, attractor, and phrase metrics into a weighted score with
simple drift and symmetry checks.
"""

import json
import os
from typing import Dict, List, Tuple

from ctl.attractors import Attractor
from ctl.clusters import Cluster
from ctl.phrase import Phrase
from ctl.symbols import Symbol


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "self_consistency_config.json5")


def load_self_consistency_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _drift(symbols: List[Symbol]) -> float:
    if not symbols:
        return 0.0
    return max(symbol.tone for symbol in symbols) - min(symbol.tone for symbol in symbols)


def _symmetry(symbols: List[Symbol]) -> float:
    if not symbols:
        return 0.0
    midpoint = len(symbols) // 2
    left = sum(s.tone for s in symbols[:midpoint])
    right = sum(s.tone for s in symbols[midpoint:])
    return abs(left - right) / max(1, len(symbols))


def evaluate_consistency(
    symbols: List[Symbol],
    clusters: List[Cluster],
    attractors: List[Attractor],
    phrases: List[Phrase],
    config: Dict | None = None,
) -> Dict:
    cfg = config or load_self_consistency_config()
    weights = cfg["weights"]
    thresholds = cfg["thresholds"]

    symbol_score = 0.0 if len(symbols) < thresholds["min_symbols"] else sum(s.stability for s in symbols) / len(symbols)
    cluster_score = 0.0 if len(clusters) < thresholds["min_clusters"] else sum(c.coherence for c in clusters) / len(clusters)
    attractor_score = 0.0 if not attractors else sum(a.activation for a in attractors) / len(attractors)
    phrase_score = 0.0 if len(phrases) < thresholds["min_phrases"] else sum(p.cadence for p in phrases) / len(phrases)

    drift_penalty = _drift(symbols) / max(1, cfg["evaluation"]["drift_tolerance"])
    symmetry_penalty = _symmetry(symbols) / max(1, cfg["evaluation"]["symmetry_tolerance"])

    weighted = (
        (symbol_score * weights["symbol"])
        + (cluster_score * weights["cluster"])
        + (attractor_score * weights["attractor"])
        + (phrase_score * weights["phrase"])
    )
    score = max(0.0, weighted - drift_penalty - symmetry_penalty)

    return {
        "symbol_score": round(symbol_score, 3),
        "cluster_score": round(cluster_score, 3),
        "attractor_score": round(attractor_score, 3),
        "phrase_score": round(phrase_score, 3),
        "drift_penalty": round(drift_penalty, 3),
        "symmetry_penalty": round(symmetry_penalty, 3),
        "final_score": round(score, 3),
    }


def write_consistency_metrics(metrics: Dict, log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_self_consistency_config()
    log_file = cfg["logging"]["log_file"]
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, log_file)

    header = (
        "symbol_score,cluster_score,attractor_score,phrase_score,drift_penalty,symmetry_penalty,final_score\n"
    )
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{metrics['symbol_score']},{metrics['cluster_score']},{metrics['attractor_score']},{metrics['phrase_score']},{metrics['drift_penalty']},{metrics['symmetry_penalty']},{metrics['final_score']}\n"
        )
    return path


__all__ = [
    "evaluate_consistency",
    "write_consistency_metrics",
    "load_self_consistency_config",
]
