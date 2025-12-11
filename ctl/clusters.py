"""
Category and cluster mapping module for Phase 3 cognition.

Groups symbols into coherent clusters using tone, hue, and polarity consensus.
Clusters expose centroids, coherence scores, and labels for attractor formation.
"""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

from ctl.symbols import Symbol


@dataclass
class Cluster:
    """Aggregation of nearby symbols."""

    idx: int
    member_indices: List[int]
    centroid_tone: float
    centroid_hue: Tuple[float, float, float]
    polarity: int
    coherence: float
    label: str


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "clusters_config.json5")


def load_clusters_config() -> Dict:
    """Load configuration for cluster formation."""

    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _tone_distance(a: int, b: int) -> int:
    return abs(a - b)


def _hue_distance(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> float:
    return sum(abs(x - y) for x, y in zip(a, b)) / 3


def _polarity_agree(values: Sequence[int]) -> int:
    positive = len([v for v in values if v > 0])
    negative = len([v for v in values if v < 0])
    if positive == negative:
        return 0
    return 1 if positive > negative else -1


def _coherence_score(tones: List[int], hues: List[Tuple[int, int, int]], polarity: int, cfg: Dict) -> float:
    if not tones:
        return 0.0
    tone_spread = max(tones) - min(tones)
    hue_spread = max(sum(h) for h in hues) - min(sum(h) for h in hues)
    hue_spread = hue_spread / 3

    tone_term = max(0.0, 1 - (tone_spread / max(cfg["coherence"]["tone_spread_limit"], 1)))
    hue_term = max(0.0, 1 - (hue_spread / max(cfg["coherence"]["hue_spread_limit"], 1)))
    polarity_term = 1.0 if polarity >= 0 else 0.85

    coherence = (
        tone_term * cfg["weights"]["tone"]
        + hue_term * cfg["weights"]["hue"]
        + polarity_term * cfg["weights"]["polarity"]
    )
    if len(tones) >= cfg["coherence"]["min_size"]:
        coherence += cfg["coherence"].get("bonus_for_peak", 0)
    return round(min(coherence, 1.0), 3)


def cluster_symbols(symbols: Sequence[Symbol], config: Dict | None = None) -> List[Cluster]:
    """Group adjacent symbols into clusters based on similarity thresholds."""

    cfg = config or load_clusters_config()
    sim_cfg = cfg["similarity"]

    clusters: List[Cluster] = []
    if not symbols:
        return clusters

    current_members: List[Symbol] = [symbols[0]]
    for current in symbols[1:]:
        last = current_members[-1]
        tone_close = _tone_distance(current.tone, last.tone) <= sim_cfg["tone_threshold"]
        hue_close = _hue_distance(current.hue, last.hue) <= sim_cfg["hue_threshold"]
        polarity_close = (not sim_cfg["polarity_consensus"]) or (current.polarity == last.polarity)
        if tone_close and hue_close and polarity_close:
            current_members.append(current)
        else:
            clusters.append(_finalize_cluster(len(clusters), current_members, cfg))
            current_members = [current]

    clusters.append(_finalize_cluster(len(clusters), current_members, cfg))
    return clusters


def _finalize_cluster(idx: int, members: List[Symbol], cfg: Dict) -> Cluster:
    tones = [m.tone for m in members]
    hues = [m.hue for m in members]
    polarity = _polarity_agree([m.polarity for m in members])
    coherence = _coherence_score(tones, hues, polarity, cfg)
    centroid_tone = sum(tones) / len(tones)
    centroid_hue = tuple(sum(values) / len(values) for values in zip(*hues))
    label = f"C{idx}-T{round(centroid_tone,1)}-P{polarity:+d}"
    return Cluster(
        idx=idx,
        member_indices=[m.idx for m in members],
        centroid_tone=round(centroid_tone, 3),
        centroid_hue=tuple(round(v, 3) for v in centroid_hue),
        polarity=polarity,
        coherence=coherence,
        label=label,
    )


def summarize_clusters(clusters: List[Cluster]) -> Dict:
    if not clusters:
        return {"count": 0, "mean_coherence": 0.0, "dominant_polarity": 0}

    mean_coherence = sum(c.coherence for c in clusters) / len(clusters)
    polarity_sum = sum(c.polarity for c in clusters)
    dominant_polarity = 0 if polarity_sum == 0 else (1 if polarity_sum > 0 else -1)
    return {
        "count": len(clusters),
        "mean_coherence": round(mean_coherence, 3),
        "dominant_polarity": dominant_polarity,
    }


def write_cluster_metrics(clusters: List[Cluster], log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_clusters_config()
    log_file = cfg["logging"]["log_file"]
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, log_file)

    summary = summarize_clusters(clusters)
    header = "count,mean_coherence,dominant_polarity\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{summary['count']},{summary['mean_coherence']},{summary['dominant_polarity']}\n"
        )
    return path


__all__ = [
    "Cluster",
    "cluster_symbols",
    "summarize_clusters",
    "write_cluster_metrics",
    "load_clusters_config",
]
