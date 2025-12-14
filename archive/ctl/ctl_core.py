"""
This agent is tasked with constructing the Chromatic Transduction Layer (CTL),
a reversible speech–tone–hue–speech mapping that preserves temporal structure,
intensity structure, and polarity structure. This system is the physical
foundation of the Tri-Unity Chromatic Cognition architecture. No cognition,
identity, or agency layers may be implemented in this phase.
"""

import json
import os
from typing import List, Dict, Tuple

# Load JSON mappings at module level
_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_MODULE_DIR, 'phoneme_map.json'), 'r') as f:
    PHONEME_TO_TONE = json.load(f)

with open(os.path.join(_MODULE_DIR, 'tone_map.json'), 'r') as f:
    TONE_NAMES = json.load(f)

with open(os.path.join(_MODULE_DIR, 'hue_map.json'), 'r') as f:
    TONE_TO_HUE = {int(k): v for k, v in json.load(f).items()}

with open(os.path.join(_MODULE_DIR, 'polarity_rules.json'), 'r') as f:
    POLARITY_RULES = json.load(f)

# Create reverse mapping: tone -> list of phonemes
TONE_TO_PHONEMES = {}
for phoneme, tone in PHONEME_TO_TONE.items():
    if tone not in TONE_TO_PHONEMES:
        TONE_TO_PHONEMES[tone] = []
    TONE_TO_PHONEMES[tone].append(phoneme)


def calculate_word_intensity(word: str) -> float:
    """
    Calculate intensity for a word based on textual features.

    Rules:
    - Base intensity = 1.0
    - +0.3 if contains any capital letter
    - +0.2 if ends with !
    - +0.1 if length > 7
    - -0.1 if length <= 3
    - Clip to [0.5, 2.0]
    """
    intensity = 1.0

    if any(c.isupper() for c in word):
        intensity += 0.3

    if word.endswith('!'):
        intensity += 0.2

    if len(word) > 7:
        intensity += 0.1

    if len(word) <= 3:
        intensity -= 0.1

    # Clip to valid range
    return max(0.5, min(2.0, intensity))


def calculate_word_polarities(words: List[str]) -> List[int]:
    """
    Calculate polarity for each word using NOT-word logic.

    Rules:
    - Default polarity = +1
    - If word is in NOT-words list, flip polarity for next 1-3 tokens
    - If sentence ends with ?, mark final token with polarity 0
    """
    not_words = set(POLARITY_RULES['not_words'])
    negation_window = POLARITY_RULES['negation_window']
    default_polarity = POLARITY_RULES['default_polarity']
    question_polarity = POLARITY_RULES['question_polarity']

    polarities = []
    negation_counter = 0

    for i, word in enumerate(words):
        # Check if this is a NOT-word
        word_lower = word.lower().rstrip('.,!?')
        is_not_word = word_lower in not_words or word_lower.endswith("n't")

        # Determine polarity
        if negation_counter > 0:
            polarity = -default_polarity
            negation_counter -= 1
        else:
            polarity = default_polarity

        # Handle question marks (optional: mark as neutral)
        if word.endswith('?') and i == len(words) - 1:
            polarity = question_polarity

        polarities.append(polarity)

        # If this is a NOT-word, set negation window
        if is_not_word:
            negation_counter = negation_window

    return polarities


def text_to_phonemes(text: str) -> List[str]:
    """
    Converts input text into a list of phonemes.
    For Phase 1, uses character-level tokenization that preserves structure.
    Preserves spaces, punctuation, and capitalization information.
    """
    # Simply return list of characters, preserving everything
    return list(text.lower())


def phonemes_to_tones(phonemes: List[str]) -> List[int]:
    """
    Converts a list of phonemes into a list of tone indices (0-11).
    Uses phoneme_map.json for deterministic mapping.
    """
    tones = []
    for phoneme in phonemes:
        if phoneme in PHONEME_TO_TONE:
            tones.append(PHONEME_TO_TONE[phoneme])
        else:
            # Fallback: use modulo for unknown characters
            tones.append(ord(phoneme) % 12)
    return tones


def tones_to_hues(tones: List[int]) -> List[Tuple[int, int, int]]:
    """
    Converts a list of tone indices to a list of RGB hue values.
    Uses hue_map.json for fixed color wheel mapping.
    """
    return [tuple(TONE_TO_HUE[tone % 12]) for tone in tones]


def inject_attributes_to_hues(
    text: str,
    tones: List[int],
    hues: List[Tuple[int, int, int]],
    phonemes: List[str]
) -> List[Dict]:
    """
    Injects intensity, polarity, and timestamp into each hue, creating ChromaticCell objects.

    Intensity derived from word-level textual features.
    Polarity derived from NOT-word logic.
    Timestamp is sequential position.
    """
    # Split text into words for intensity/polarity calculation
    words = text.split()

    # Calculate intensity and polarity per word
    word_intensities = [calculate_word_intensity(w) for w in words]
    word_polarities = calculate_word_polarities(words)

    # Map word-level attributes to character-level
    char_intensities = []
    char_polarities = []
    word_idx = 0
    in_word = False

    for char in text.lower():
        if char == ' ':
            char_intensities.append(1.0)  # Neutral for spaces
            char_polarities.append(1)
            in_word = False
        else:
            if not in_word:
                in_word = True
                if word_idx >= len(words):
                    # Shouldn't happen, but handle gracefully
                    char_intensities.append(1.0)
                    char_polarities.append(1)
                else:
                    char_intensities.append(word_intensities[word_idx])
                    char_polarities.append(word_polarities[word_idx])
            else:
                # Continue with same word's attributes
                char_intensities.append(word_intensities[word_idx] if word_idx < len(word_intensities) else 1.0)
                char_polarities.append(word_polarities[word_idx] if word_idx < len(word_polarities) else 1)

        # Check if we're at the end of a word
        if in_word and (len(char_intensities) >= len(text.lower()) or
                        (len(char_intensities) < len(text.lower()) and text.lower()[len(char_intensities)] == ' ')):
            word_idx += 1

    # Create ChromaticCell objects
    chromatic_cells = []
    for i, (tone, hue, phoneme) in enumerate(zip(tones, hues, phonemes)):
        chromatic_cells.append({
            "tone": tone,
            "rgb": hue,
            "phoneme": phoneme,  # Store original phoneme for reconstruction
            "intensity": char_intensities[i] if i < len(char_intensities) else 1.0,
            "polarity": char_polarities[i] if i < len(char_polarities) else 1,
            "timestamp": float(i)
        })

    return chromatic_cells


def hues_to_tones(chromatic_cells: List[Dict]) -> List[int]:
    """
    Reconstructs a list of tone indices from a list of ChromaticCell objects.
    """
    return [cell["tone"] for cell in chromatic_cells]


def tones_to_phonemes(chromatic_cells: List[Dict]) -> List[str]:
    """
    Converts a list of ChromaticCell objects back into phonemes.
    Uses the stored phoneme in each cell for perfect reconstruction.
    """
    # Use stored phonemes from chromatic cells
    if chromatic_cells and "phoneme" in chromatic_cells[0]:
        return [cell["phoneme"] for cell in chromatic_cells]

    # Fallback: use tone-to-phoneme reverse mapping (lossy)
    tones = [cell["tone"] if isinstance(cell, dict) else cell for cell in chromatic_cells]
    phonemes = []
    for tone in tones:
        if tone in TONE_TO_PHONEMES:
            # Pick first phoneme mapping (arbitrary but deterministic)
            phonemes.append(TONE_TO_PHONEMES[tone][0])
        else:
            phonemes.append('?')  # Unknown
    return phonemes


def phonemes_to_text(phonemes: List[str]) -> str:
    """
    Converts a list of phonemes back into a string.
    For Phase 1, simply joins the characters.
    """
    return "".join(phonemes)
