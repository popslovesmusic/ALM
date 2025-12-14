"""Meta-symbol construction for Phase 4."""

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

from ctl.clusters import Cluster
from ctl.phrase import Phrase
from ctl.symbols import Symbol


@dataclass
class MetaSymbol:
    idx: int
    anchor: str
    target: str
    relation: str
    span: Tuple[int, int]
    support: int
    weight: float
    coherence: float


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "meta_symbols_config.json5")


def load_meta_symbols_config() -> Dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _nearest_cluster(timestamp: int, clusters: Sequence[Cluster]) -> Cluster | None:
    if not clusters:
        return None
    best = min(clusters, key=lambda c: min(abs(timestamp - idx) for idx in c.member_indices))
    return best


def _polarity_balance(symbols: Sequence[Symbol], start: int, end: int) -> float:
    window = [s.polarity for s in symbols if start <= s.timestamp <= end]
    if not window:
        return 0.0
    return sum(window) / len(window)


def _relation(anchor: Phrase, target: Phrase | None, cadence_cfg: Dict) -> str:
    if target is None:
        return "sustain"
    cadence_delta = target.cadence - anchor.cadence
    if anchor.motif == target.motif and cadence_delta >= 0:
        return "reinforce"
    if cadence_delta > cadence_cfg["anticipate_threshold"]:
        return "anticipate"
    if cadence_delta < cadence_cfg["resolve_threshold"]:
        return "resolve"
    return "contrast" if anchor.motif != target.motif else "link"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def derive_meta_symbols(
    symbols: Sequence[Symbol],
    clusters: Sequence[Cluster],
    phrases: Sequence[Phrase],
    config: Dict | None = None,
) -> List[MetaSymbol]:
    cfg = config or load_meta_symbols_config()
    meta_symbols: List[MetaSymbol] = []
    if not phrases:
        return meta_symbols

    for idx, phrase in enumerate(phrases):
        target_phrase = phrases[idx + 1] if idx + 1 < len(phrases) else None
        relation = _relation(phrase, target_phrase, cfg["cadence"])

        anchor_cluster = _nearest_cluster(phrase.start, clusters)
        coherence = anchor_cluster.coherence if anchor_cluster else 0.0

        span_end = target_phrase.end if target_phrase else phrase.end
        anchor_pol = _polarity_balance(symbols, phrase.start, phrase.end)
        target_pol = _polarity_balance(symbols, target_phrase.start, target_phrase.end) if target_phrase else anchor_pol
        polarity_alignment = 1 - abs(anchor_pol - target_pol) / 2

        motif_weight = cfg["relation_weights"]["motif_match"] if target_phrase and phrase.motif == target_phrase.motif else cfg["relation_weights"]["contrast"]
        weight = motif_weight
        weight += coherence * cfg["relation_weights"]["coherence"]
        weight += polarity_alignment * cfg["relation_weights"]["polarity"]
        weight = _clamp(weight)

        support = max(cfg["support"]["min_support"], len([s for s in symbols if phrase.start <= s.timestamp <= span_end]))

        meta_symbol = MetaSymbol(
            idx=len(meta_symbols),
            anchor=phrase.motif,
            target=target_phrase.motif if target_phrase else phrase.motif,
            relation=relation,
            span=(phrase.start, span_end),
            support=support,
            weight=round(weight, 3),
            coherence=round(coherence, 3),
        )

        if meta_symbols:
            last = meta_symbols[-1]
            if (
                last.relation == meta_symbol.relation
                and meta_symbol.span[0] - last.span[1] <= cfg["support"]["merge_window"]
            ):
                updated_support = last.support + meta_symbol.support
                averaged_weight = round((last.weight + meta_symbol.weight) / 2, 3)
                meta_symbols[-1] = MetaSymbol(
                    idx=last.idx,
                    anchor=last.anchor,
                    target=meta_symbol.target,
                    relation=last.relation,
                    span=(last.span[0], meta_symbol.span[1]),
                    support=updated_support,
                    weight=averaged_weight,
                    coherence=round(max(last.coherence, meta_symbol.coherence), 3),
                )
                continue

        meta_symbols.append(meta_symbol)

    return meta_symbols


def summarize_meta_symbols(meta_symbols: Sequence[MetaSymbol]) -> Dict:
    if not meta_symbols:
        return {
            "count": 0,
            "mean_weight": 0.0,
            "dominant_relation": "none",
            "mean_support": 0.0,
        }
    relation_counts: Dict[str, int] = {}
    for meta in meta_symbols:
        relation_counts[meta.relation] = relation_counts.get(meta.relation, 0) + 1
    dominant_relation = max(relation_counts, key=relation_counts.get)
    mean_weight = sum(m.weight for m in meta_symbols) / len(meta_symbols)
    mean_support = sum(m.support for m in meta_symbols) / len(meta_symbols)
    return {
        "count": len(meta_symbols),
        "mean_weight": round(mean_weight, 3),
        "dominant_relation": dominant_relation,
        "mean_support": round(mean_support, 3),
    }


def write_meta_symbol_metrics(meta_symbols: Sequence[MetaSymbol], log_dir: str | None = None, config: Dict | None = None) -> str:
    cfg = config or load_meta_symbols_config()
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, cfg["logging"]["log_file"])

    summary = summarize_meta_symbols(meta_symbols)
    header = "count,mean_weight,mean_support,dominant_relation\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{summary['count']},{summary['mean_weight']},{summary['mean_support']},{summary['dominant_relation']}\n"
        )
    return path


__all__ = [
    "MetaSymbol",
    "derive_meta_symbols",
    "summarize_meta_symbols",
    "write_meta_symbol_metrics",
    "load_meta_symbols_config",
]
