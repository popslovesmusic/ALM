"""Synthetic ChromaticCell generators for CTL tests."""
from typing import Any, Dict, List

ChromaticCell = Dict[str, Any]


def make_l_cell(tone: int, hue: List[int], intensity: float, polarity: int, timestamp: float) -> ChromaticCell:
    return {
        "tone": tone % 12,
        "hue": [int(x) for x in hue],
        "intensity": float(intensity),
        "polarity": int(polarity),
        "timestamp": float(timestamp),
    }


def generate_l_sequence(length: int = 6, start_tone: int = 0, tone_step: int = 1) -> List[ChromaticCell]:
    """Create a monotonic L stream with gentle hue drift and alternating polarity."""
    seq: List[ChromaticCell] = []
    for i in range(length):
        tone = (start_tone + tone_step * i) % 12
        hue = [min(255, 30 + 10 * i), min(255, 60 + 5 * i), min(255, 90 + 3 * i)]
        intensity = 1.0 + 0.1 * i
        polarity = 1 if i % 3 else -1  # occasional flips
        seq.append(make_l_cell(tone, hue, intensity, polarity, i))
    return seq


def generate_contrasting_l_sequence(length: int = 5) -> List[ChromaticCell]:
    """Sequence with abrupt tone jumps and polarity oscillations for constraint tests."""
    seq: List[ChromaticCell] = []
    tones = [0, 7, 2, 9, 3][:length]
    polarities = [1, -1, 1, -1, 1][:length]
    for i, (tone, pol) in enumerate(zip(tones, polarities)):
        hue = [200 - 15 * i, 80 + 10 * i, 50 + 5 * i]
        intensity = 0.8 + 0.2 * i
        seq.append(make_l_cell(tone, hue, intensity, pol, i))
    return seq
