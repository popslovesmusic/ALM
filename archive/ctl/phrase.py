"""
Chromatic phrase structure builder.

Segments symbols and clusters into temporal phrases and simple chromatic grammar motifs.
"""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Sequence

from ctl.clusters import Cluster
from ctl.symbols import Symbol


@dataclass
class Phrase:
    idx: int
    start: int
    end: int
    motif: str
    cadence: float


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "phrase_config.json5")


def load_phrase_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _tone_slope(symbols: Sequence[Symbol]) -> float:
    if len(symbols) < 2:
        return 0.0
    return (symbols[-1].tone - symbols[0].tone) / max(1, len(symbols) - 1)


def _motif_from_window(symbols: Sequence[Symbol], threshold: float) -> str:
    slope = _tone_slope(symbols)
    if slope > threshold:
        return "ascending"
    if slope < -threshold:
        return "descending"
    polarity_sum = sum(s.polarity for s in symbols)
    if polarity_sum == 0:
        return "balanced"
    return "pulse" if polarity_sum > 0 else "rebound"


def build_phrases(symbols: List[Symbol], clusters: List[Cluster], config: Dict | None = None) -> List[Phrase]:
    cfg = config or load_phrase_config()
    window = cfg["window"]
    motif_len = cfg["motif_length"]
    cadence_threshold = cfg["cadence_threshold"]

    phrases: List[Phrase] = []
    if not symbols:
        return phrases

    for idx in range(0, len(symbols), window):
        window_symbols = symbols[idx : idx + window]
        motif = _motif_from_window(window_symbols[:motif_len], cfg["tone_slope_threshold"])
        cadence = len([s for s in window_symbols if s.role == "peak"]) / max(1, len(window_symbols))
        cadence = round(cadence, 3)
        if cadence < cadence_threshold:
            motif = f"{motif}-soft"
        phrases.append(
            Phrase(
                idx=len(phrases),
                start=window_symbols[0].timestamp,
                end=window_symbols[-1].timestamp,
                motif=motif,
                cadence=cadence,
            )
        )
    return phrases


def summarize_phrases(phrases: List[Phrase]) -> Dict:
    if not phrases:
        return {"count": 0, "mean_cadence": 0.0}
    mean_cadence = sum(p.cadence for p in phrases) / len(phrases)
    motifs = {}
    for phrase in phrases:
        motifs[phrase.motif] = motifs.get(phrase.motif, 0) + 1
    dominant_motif = max(motifs, key=motifs.get)
    return {"count": len(phrases), "mean_cadence": round(mean_cadence, 3), "dominant_motif": dominant_motif}


def write_phrase_metrics(phrases: List[Phrase], log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_phrase_config()
    log_file = cfg["logging"]["log_file"]
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, log_file)

    summary = summarize_phrases(phrases)
    header = "count,mean_cadence,dominant_motif\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{summary['count']},{summary.get('mean_cadence',0)},{summary.get('dominant_motif','none')}\n"
        )
    return path


__all__ = [
    "Phrase",
    "build_phrases",
    "summarize_phrases",
    "write_phrase_metrics",
    "load_phrase_config",
]
