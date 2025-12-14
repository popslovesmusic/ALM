"""Narrative state layer for Phase 4."""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Sequence

from ctl.meta_symbols import MetaSymbol
from ctl.phrase import Phrase


@dataclass
class NarrativeEpisode:
    idx: int
    start: int
    end: int
    theme: str
    salience: float
    meta_count: int
    consistency: float
    posture_hint: str


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "narrative_config.json5")


def load_narrative_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _motif_diversity(phrases: Sequence[Phrase]) -> float:
    motifs = {p.motif for p in phrases}
    if not phrases:
        return 0.0
    return (len(motifs) - 1) / max(1, len(phrases))


def _theme_for_chunk(meta_symbols: Sequence[MetaSymbol], phrases: Sequence[Phrase]) -> str:
    if meta_symbols:
        relation_counts: Dict[str, int] = {}
        for meta in meta_symbols:
            relation_counts[meta.relation] = relation_counts.get(meta.relation, 0) + 1
        dominant_relation = max(relation_counts, key=relation_counts.get)
    else:
        dominant_relation = "none"
    dominant_motif = phrases[0].motif if phrases else "none"
    return f"{dominant_relation}-{dominant_motif}"


def build_narrative(
    meta_symbols: Sequence[MetaSymbol],
    phrases: Sequence[Phrase],
    config: Dict | None = None,
) -> List[NarrativeEpisode]:
    cfg = config or load_narrative_config()
    episodes: List[NarrativeEpisode] = []
    if not phrases:
        return episodes

    window = max(1, cfg["window"])
    thresholds = cfg["thresholds"]

    for i in range(0, len(phrases), window):
        chunk_phrases = phrases[i : i + window]
        start, end = chunk_phrases[0].start, chunk_phrases[-1].end
        chunk_metas = [m for m in meta_symbols if start <= m.span[0] <= end]
        theme = _theme_for_chunk(chunk_metas, chunk_phrases)

        if chunk_metas:
            mean_weight = sum(m.weight for m in chunk_metas) / len(chunk_metas)
            mean_support = sum(m.support for m in chunk_metas) / len(chunk_metas)
        else:
            mean_weight = 0.0
            mean_support = 0.0

        cadence_mean = sum(p.cadence for p in chunk_phrases) / len(chunk_phrases)
        diversity = _motif_diversity(chunk_phrases)
        salience = mean_weight + (cadence_mean * cfg["cadence_bias"]) - (diversity * cfg["drift_penalty"])
        salience = round(max(0.0, salience), 3)

        consistency = 1 - min(1.0, diversity + (0.1 if mean_support < thresholds["consistency_low"] else 0))
        consistency = round(max(0.0, consistency), 3)

        if salience >= thresholds["salience_high"] and consistency >= thresholds["consistency_high"]:
            posture_hint = "amplify"
        elif salience <= thresholds["salience_low"] or consistency <= thresholds["consistency_low"]:
            posture_hint = "reframe"
        else:
            posture_hint = "stabilize"

        episodes.append(
            NarrativeEpisode(
                idx=len(episodes),
                start=start,
                end=end,
                theme=theme,
                salience=salience,
                meta_count=len(chunk_metas),
                consistency=consistency,
                posture_hint=posture_hint,
            )
        )
    return episodes


def summarize_episodes(episodes: Sequence[NarrativeEpisode]) -> Dict:
    if not episodes:
        return {"count": 0, "mean_salience": 0.0, "dominant_theme": "none"}
    mean_salience = sum(e.salience for e in episodes) / len(episodes)
    theme_counts: Dict[str, int] = {}
    for ep in episodes:
        theme_counts[ep.theme] = theme_counts.get(ep.theme, 0) + 1
    dominant_theme = max(theme_counts, key=theme_counts.get)
    return {
        "count": len(episodes),
        "mean_salience": round(mean_salience, 3),
        "dominant_theme": dominant_theme,
    }


def write_narrative_metrics(episodes: Sequence[NarrativeEpisode], log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_narrative_config()
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, cfg["logging"]["log_file"])

    summary = summarize_episodes(episodes)
    header = "count,mean_salience,dominant_theme\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(f"{summary['count']},{summary['mean_salience']},{summary['dominant_theme']}\n")
    return path


__all__ = [
    "NarrativeEpisode",
    "build_narrative",
    "summarize_episodes",
    "write_narrative_metrics",
    "load_narrative_config",
]
