"""
Symbol formation layer for Phase 3 cognitive emergence.

Transforms ChromaticCell-like inputs (tone, hue, polarity, intensity, timestamp)
into stabilized Symbol objects with roles and labels suitable for higher-level
processing. All functions are deterministic and rely only on local calculations
and JSON5 configuration values.
"""

import json
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass
class Symbol:
    """Lightweight representation of a chromatic symbol."""

    idx: int
    tone: int
    hue: Tuple[int, int, int]
    polarity: int
    intensity: float
    timestamp: int
    role: str
    stability: float
    label: str


_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_MODULE_DIR, "symbols_config.json5")


def load_symbols_config() -> Dict:
    """Load configuration for the symbol formation layer."""

    with open(_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _moving_average(values: List[float], window: int) -> List[float]:
    window = max(1, window)
    averaged = []
    for i, _ in enumerate(values):
        start = max(0, i - window + 1)
        segment = values[start : i + 1]
        averaged.append(sum(segment) / len(segment))
    return averaged


def _role_for_index(intensities: List[float], index: int, threshold: float) -> str:
    current = intensities[index]
    prev_val = intensities[index - 1] if index > 0 else current
    next_val = intensities[index + 1] if index < len(intensities) - 1 else current

    if current >= threshold and current >= prev_val and current >= next_val:
        return "peak"
    if current < prev_val and current <= next_val:
        return "bridge"
    if current >= prev_val:
        return "onset"
    return "decay"


def form_symbols(cells: Iterable[Dict], config: Dict | None = None) -> List[Symbol]:
    """
    Build symbols from a sequence of chromatic cells.

    Args:
        cells: Iterable of dicts containing tone, hue (tuple), polarity, intensity, timestamp.
        config: Optional configuration override.

    Returns:
        List of Symbol objects.
    """

    cfg = config or load_symbols_config()
    agg_cfg = cfg["aggregation"]
    stability_cfg = cfg["stability"]
    label_cfg = cfg["labeling"]

    tones: List[int] = []
    hues: List[Tuple[int, int, int]] = []
    polarities: List[int] = []
    intensities: List[float] = []
    timestamps: List[int] = []
    for cell in cells:
        tones.append(int(cell["tone"]))
        hue = tuple(int(v) for v in cell["hue"])
        hues.append(hue)
        polarities.append(int(cell.get("polarity", 1)))
        intensities.append(float(cell.get("intensity", 1.0)))
        timestamps.append(int(cell.get("timestamp", len(timestamps))))

    smoothed = _moving_average(intensities, agg_cfg["window"])
    symbols: List[Symbol] = []

    for idx, (tone, hue, polarity, intensity, ts, smoothed_intensity) in enumerate(
        zip(tones, hues, polarities, intensities, timestamps, smoothed)
    ):
        role = _role_for_index(smoothed, idx, agg_cfg["intensity_threshold"])
        stability = (smoothed_intensity * (1 - stability_cfg["decay"])) + (
            abs(polarity) * agg_cfg["polarity_weight"]
        )
        if role == "peak":
            stability += stability_cfg["role_bonus"]
        tone_band = tone // max(1, label_cfg["tone_band"])
        hue_band = sum(hue) // (3 * max(1, label_cfg["hue_band"]))
        label = f"T{tone_band}-H{hue_band}-P{polarity:+d}"
        symbols.append(
            Symbol(
                idx=idx,
                tone=tone,
                hue=hue,
                polarity=polarity,
                intensity=intensity,
                timestamp=ts,
                role=role,
                stability=round(stability, 3),
                label=label,
            )
        )

    return symbols


def summarize_symbols(symbols: List[Symbol]) -> Dict:
    """Summarize symbol set into aggregate metrics."""

    if not symbols:
        return {
            "count": 0,
            "mean_tone": 0,
            "mean_intensity": 0,
            "stability": 0,
            "peak_ratio": 0,
        }

    mean_tone = sum(sym.tone for sym in symbols) / len(symbols)
    mean_intensity = sum(sym.intensity for sym in symbols) / len(symbols)
    stability = sum(sym.stability for sym in symbols) / len(symbols)
    peak_ratio = len([s for s in symbols if s.role == "peak"]) / len(symbols)

    return {
        "count": len(symbols),
        "mean_tone": round(mean_tone, 3),
        "mean_intensity": round(mean_intensity, 3),
        "stability": round(stability, 3),
        "peak_ratio": round(peak_ratio, 3),
    }


def write_symbol_metrics(symbols: List[Symbol], log_dir: str | None = None, config: Dict | None = None) -> str:
    """Write symbol metrics to CSV and return the path."""

    cfg = config or load_symbols_config()
    log_file = cfg["logging"]["log_file"]
    target_dir = log_dir or os.path.abspath(os.path.join(_MODULE_DIR, "..", "logs"))
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, log_file)

    metrics = summarize_symbols(symbols)
    header = "count,mean_tone,mean_intensity,stability,peak_ratio\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(header)
        handle.write(
            f"{metrics['count']},{metrics['mean_tone']},{metrics['mean_intensity']},{metrics['stability']},{metrics['peak_ratio']}\n"
        )
    return path


__all__ = ["Symbol", "form_symbols", "summarize_symbols", "write_symbol_metrics", "load_symbols_config"]
