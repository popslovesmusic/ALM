"""
CTL Encoding Module

This module contains the functions responsible for encoding text into ChromaticCells through
the phoneme, tone, and hue stages. It is part of the Chromatic Transduction Layer (CTL),
a reversible speech–tone–hue–speech mapping that preserves temporal structure,
intensity structure, and polarity structure.
"""

from typing import List, Dict
from .ctl_core import (
    text_to_phonemes,
    phonemes_to_tones,
    tones_to_hues,
    inject_attributes_to_hues
)


def encode_text_to_chromatic_cells(text: str) -> List[Dict]:
    """
    Complete encoding pipeline: Text → ChromaticCells.

    This function orchestrates stages 1-4 of the CTL pipeline:
    1. Text → Phonemes
    2. Phonemes → Tones
    3. Tones → Hues
    4. Hues + Attributes → ChromaticCells

    Args:
        text: Input text string

    Returns:
        List of ChromaticCell dictionaries containing:
        - tone: int (0-11)
        - rgb: tuple (R, G, B)
        - phoneme: str (original character)
        - intensity: float (0.5-2.0)
        - polarity: int (+1, -1, or 0)
        - timestamp: float (sequential position)
    """
    # Stage 1: Text → Phonemes
    phonemes = text_to_phonemes(text)

    # Stage 2: Phonemes → Tones
    tones = phonemes_to_tones(phonemes)

    # Stage 3: Tones → Hues
    hues = tones_to_hues(tones)

    # Stage 4: Inject T/S/Π attributes → ChromaticCells
    chromatic_cells = inject_attributes_to_hues(text, tones, hues, phonemes)

    return chromatic_cells


def encode_text_to_tones(text: str) -> List[int]:
    """
    Partial encoding: Text → Tones.

    Stages 1-2 only.

    Args:
        text: Input text string

    Returns:
        List of tone indices (0-11)
    """
    phonemes = text_to_phonemes(text)
    tones = phonemes_to_tones(phonemes)
    return tones


def encode_text_to_hues(text: str) -> List[tuple]:
    """
    Partial encoding: Text → Hues.

    Stages 1-3 only.

    Args:
        text: Input text string

    Returns:
        List of RGB tuples
    """
    phonemes = text_to_phonemes(text)
    tones = phonemes_to_tones(phonemes)
    hues = tones_to_hues(tones)
    return hues
