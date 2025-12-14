"""
Attractor landscape builder for Phase 3 cognition.

Computes attractor basins from clusters and updates activation energy deterministically.
"""

import json
import os
from dataclasses import dataclass
from typing import Dict, List

from ctl.clusters import Cluster


@dataclass
class Attractor:
    idx: int
    center_tone: float
    center_hue: float
    energy: float
    stability: float
    activation: float


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "attractors_config.json5")


def load_attractors_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _energy_from_cluster(cluster: Cluster, cfg: Dict) -> float:
    gain = cfg["basins"]["energy_gain"]
    coherence_weight = cfg["activation"]["coherence_weight"]
    size_weight = cfg["activation"]["size_weight"]
    size_term = len(cluster.member_indices) / (len(cluster.member_indices) + cfg["basins"]["width"])
    return round(gain * ((cluster.coherence * coherence_weight) + (size_term * size_weight)), 3)


def build_attractors(clusters: List[Cluster], config: Dict | None = None) -> List[Attractor]:
    cfg = config or load_attractors_config()
    attractors: List[Attractor] = []

    for idx, cluster in enumerate(clusters):
        energy = _energy_from_cluster(cluster, cfg)
        stability = max(0.0, min(1.0, cluster.coherence - cfg["basins"]["stability_decay"]))
        activation = energy - cfg["dynamics"]["damping"]
        attractors.append(
            Attractor(
                idx=idx,
                center_tone=cluster.centroid_tone,
                center_hue=sum(cluster.centroid_hue) / 3,
                energy=energy,
                stability=round(stability, 3),
                activation=round(max(0.0, activation), 3),
            )
        )
    return attractors


def update_attractors(attractors: List[Attractor], clusters: List[Cluster], config: Dict | None = None) -> List[Attractor]:
    cfg = config or load_attractors_config()
    updated: List[Attractor] = []
    damping = cfg["dynamics"]["damping"]
    momentum = cfg["dynamics"]["momentum"]

    for attr, cluster in zip(attractors, clusters):
        energy_input = _energy_from_cluster(cluster, cfg)
        blended_energy = (attr.energy * (1 - momentum)) + (energy_input * momentum)
        stability = max(0.0, min(1.0, blended_energy - cfg["basins"]["stability_decay"]))
        activation = max(0.0, blended_energy - damping)
        updated.append(
            Attractor(
                idx=attr.idx,
                center_tone=cluster.centroid_tone,
                center_hue=sum(cluster.centroid_hue) / 3,
                energy=round(blended_energy, 3),
                stability=round(stability, 3),
                activation=round(activation, 3),
            )
        )
    return updated


def summarize_attractors(attractors: List[Attractor]) -> Dict:
    if not attractors:
        return {"count": 0, "mean_activation": 0.0, "mean_stability": 0.0}
    mean_activation = sum(a.activation for a in attractors) / len(attractors)
    mean_stability = sum(a.stability for a in attractors) / len(attractors)
    return {
        "count": len(attractors),
        "mean_activation": round(mean_activation, 3),
        "mean_stability": round(mean_stability, 3),
    }


def write_attractor_metrics(attractors: List[Attractor], log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_attractors_config()
    log_file = cfg["logging"]["log_file"]
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, log_file)

    summary = summarize_attractors(attractors)
    header = "count,mean_activation,mean_stability\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{summary['count']},{summary['mean_activation']},{summary['mean_stability']}\n"
        )
    return path


__all__ = [
    "Attractor",
    "build_attractors",
    "update_attractors",
    "summarize_attractors",
    "write_attractor_metrics",
    "load_attractors_config",
]
