"""
Lightweight visualization helpers for chromatic sequences.

Functions here generate structured summaries (tone trajectories, hue maps,
intensity envelopes) and export them to JSON or CSV so that external plotting
tools can render the data. No GUI dependencies are introduced.
"""
from __future__ import annotations

import csv
import json
import os
from typing import Any, Dict, Iterable, List, Sequence

ChromaticCell = Dict[str, Any]


def tone_trajectory(sequence: Sequence[ChromaticCell]) -> List[Dict[str, Any]]:
    """Return timestamped tone trajectory for plotting."""
    return [
        {"timestamp": cell.get("timestamp", idx), "tone": cell.get("tone", 0)}
        for idx, cell in enumerate(sequence)
    ]


def hue_map(sequence: Sequence[ChromaticCell]) -> List[Dict[str, Any]]:
    """Return RGB channel trajectories keyed by timestamp."""
    mapped: List[Dict[str, Any]] = []
    for idx, cell in enumerate(sequence):
        hue = cell.get("hue", [0, 0, 0])
        mapped.append(
            {
                "timestamp": cell.get("timestamp", idx),
                "r": int(hue[0]) if len(hue) > 0 else 0,
                "g": int(hue[1]) if len(hue) > 1 else 0,
                "b": int(hue[2]) if len(hue) > 2 else 0,
            }
        )
    return mapped


def intensity_envelope(sequence: Sequence[ChromaticCell]) -> List[Dict[str, Any]]:
    """Return timestamped intensity envelope."""
    return [
        {"timestamp": cell.get("timestamp", idx), "intensity": float(cell.get("intensity", 0.0))}
        for idx, cell in enumerate(sequence)
    ]


def export_json_snapshot(name: str, data: Any, log_dir: str = "logs") -> str:
    """Persist structured visualization data to a JSON file."""
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


def export_csv_snapshot(name: str, rows: Iterable[Dict[str, Any]], log_dir: str = "logs") -> str:
    """Persist tabular visualization rows to CSV."""
    os.makedirs(log_dir, exist_ok=True)
    rows_list = list(rows)
    path = os.path.join(log_dir, f"{name}.csv")
    if not rows_list:
        with open(path, "w", newline="") as f:
            f.write("")
        return path

    header = list(rows_list[0].keys())
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows_list)
    return path


def bundle_visualizations(sequence: Sequence[ChromaticCell]) -> Dict[str, Any]:
    """Return a combined visualization bundle for convenience."""
    return {
        "tone": tone_trajectory(sequence),
        "hue": hue_map(sequence),
        "intensity": intensity_envelope(sequence),
    }


__all__ = [
    "tone_trajectory",
    "hue_map",
    "intensity_envelope",
    "bundle_visualizations",
    "export_json_snapshot",
    "export_csv_snapshot",
]
