"""
This agent is tasked with constructing the Chromatic Transduction Layer (CTL),
a reversible speech–tone–hue–speech mapping that preserves temporal structure,
intensity structure, and polarity structure. This system is the physical
foundation of the Tri-Unity Chromatic Cognition architecture. No cognition,
identity, or agency layers may be implemented in this phase.
"""

from typing import List, Dict


def calculate_levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.
    This is a basic implementation for character-by-character comparison.
    """
    if len(s1) < len(s2):
        return calculate_levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def calculate_meaning_token_retention(original_cells: List[Dict], reconstructed_cells: List[Dict]) -> float:
    """
    Calculates the meaning-token retention as the ratio of matching phonemes.

    For Phase 1, this compares the phoneme sequences to measure how well
    the text structure was preserved.

    Returns:
        Float between 0.0 and 1.0, where 1.0 = perfect retention
    """
    if not original_cells or not reconstructed_cells:
        return 0.0

    # Extract phonemes from cells
    original_phonemes = [cell.get('phoneme', '') for cell in original_cells]
    reconstructed_phonemes = [cell.get('phoneme', '') for cell in reconstructed_cells]

    # Count matching positions
    min_len = min(len(original_phonemes), len(reconstructed_phonemes))
    matches = sum(1 for i in range(min_len) if original_phonemes[i] == reconstructed_phonemes[i])

    # Calculate retention ratio
    max_len = max(len(original_phonemes), len(reconstructed_phonemes))
    if max_len == 0:
        return 1.0

    return matches / max_len


def calculate_polarity_inversions(original_cells: List[Dict], reconstructed_cells: List[Dict]) -> int:
    """
    Calculates the number of polarity inversions (sign flips).

    Counts how many chromatic cells have different polarity values
    between original and reconstructed versions.

    Returns:
        Integer count of polarity mismatches
    """
    if not original_cells or not reconstructed_cells:
        return 0

    # Compare polarities at matching positions
    min_len = min(len(original_cells), len(reconstructed_cells))
    inversions = 0

    for i in range(min_len):
        orig_polarity = original_cells[i].get('polarity', 1)
        recon_polarity = reconstructed_cells[i].get('polarity', 1)

        # Check if polarity has flipped (sign changed)
        if orig_polarity * recon_polarity < 0:  # Different signs
            inversions += 1
        elif orig_polarity != recon_polarity:  # Different values (e.g., 1 vs 0)
            inversions += 1

    # Add inversions for length mismatch
    inversions += abs(len(original_cells) - len(reconstructed_cells))

    return inversions


def calculate_intensity_loss(original_cells: List[Dict], reconstructed_cells: List[Dict]) -> float:
    """
    Calculates the average intensity loss (absolute difference).

    Measures how much the intensity values have drifted during
    the encoding/decoding process.

    Returns:
        Float representing average absolute intensity difference
    """
    if not original_cells or not reconstructed_cells:
        return 0.0

    min_len = min(len(original_cells), len(reconstructed_cells))
    if min_len == 0:
        return 0.0

    total_loss = 0.0
    for i in range(min_len):
        orig_intensity = original_cells[i].get('intensity', 1.0)
        recon_intensity = reconstructed_cells[i].get('intensity', 1.0)
        total_loss += abs(orig_intensity - recon_intensity)

    # Add penalty for length mismatch (assume default intensity 1.0 for missing)
    length_diff = abs(len(original_cells) - len(reconstructed_cells))
    total_loss += length_diff * 1.0

    # Return average loss
    max_len = max(len(original_cells), len(reconstructed_cells))
    return total_loss / max_len if max_len > 0 else 0.0


def calculate_temporal_drift(original_cells: List[Dict], reconstructed_cells: List[Dict]) -> float:
    """
    Calculates the average temporal drift (timestamp differences).

    Measures how much the temporal ordering has shifted during
    the encoding/decoding process.

    Returns:
        Float representing average absolute timestamp difference
    """
    if not original_cells or not reconstructed_cells:
        return 0.0

    min_len = min(len(original_cells), len(reconstructed_cells))
    if min_len == 0:
        return 0.0

    total_drift = 0.0
    for i in range(min_len):
        orig_time = original_cells[i].get('timestamp', 0.0)
        recon_time = reconstructed_cells[i].get('timestamp', 0.0)
        total_drift += abs(orig_time - recon_time)

    # Return average drift
    return total_drift / min_len if min_len > 0 else 0.0
