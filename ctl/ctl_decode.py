"""
CTL Decoding Module

This module contains the functions responsible for decoding ChromaticCells back into text
through the hue, tone, and phoneme stages. It is part of the Chromatic Transduction Layer (CTL),
a reversible speech–tone–hue–speech mapping that preserves temporal structure,
intensity structure, and polarity structure.
"""

from typing import List, Dict
from .ctl_core import (
    hues_to_tones,
    tones_to_phonemes,
    phonemes_to_text
)


def decode_chromatic_cells_to_text(chromatic_cells: List[Dict]) -> str:
    """
    Complete decoding pipeline: ChromaticCells → Text.

    This function orchestrates stages 5-7 of the CTL pipeline:
    5. ChromaticCells → Tones
    6. Tones → Phonemes
    7. Phonemes → Text

    Args:
        chromatic_cells: List of ChromaticCell dictionaries

    Returns:
        Reconstructed text string
    """
    # Stage 5: ChromaticCells → Tones
    tones = hues_to_tones(chromatic_cells)

    # Stage 6: Tones → Phonemes (uses stored phoneme in cells)
    phonemes = tones_to_phonemes(chromatic_cells)

    # Stage 7: Phonemes → Text
    text = phonemes_to_text(phonemes)

    return text


def decode_chromatic_cells_to_phonemes(chromatic_cells: List[Dict]) -> List[str]:
    """
    Partial decoding: ChromaticCells → Phonemes.

    Stages 5-6 only.

    Args:
        chromatic_cells: List of ChromaticCell dictionaries

    Returns:
        List of phoneme strings
    """
    tones = hues_to_tones(chromatic_cells)
    phonemes = tones_to_phonemes(chromatic_cells)
    return phonemes


def decode_chromatic_cells_to_tones(chromatic_cells: List[Dict]) -> List[int]:
    """
    Partial decoding: ChromaticCells → Tones.

    Stage 5 only.

    Args:
        chromatic_cells: List of ChromaticCell dictionaries

    Returns:
        List of tone indices (0-11)
    """
    tones = hues_to_tones(chromatic_cells)
    return tones
