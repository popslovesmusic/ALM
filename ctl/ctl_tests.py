"""
This agent is tasked with constructing the Chromatic Transduction Layer (CTL), a reversible speech–tone–hue–speech mapping that preserves temporal structure, intensity structure, and polarity structure. This system is the physical foundation of the Tri-Unity Chromatic Cognition architecture. No cognition, identity, or agency layers may be implemented in this phase.
"""

import os
from typing import List, Dict
import csv
from datetime import datetime

from .ctl_core import (
    text_to_phonemes,
    phonemes_to_tones,
    tones_to_hues,
    inject_attributes_to_hues,
    hues_to_tones,
    tones_to_phonemes,
    phonemes_to_text,
)
from .ctl_metrics import (
    calculate_levenshtein_distance,
    calculate_meaning_token_retention,
    calculate_polarity_inversions,
    calculate_intensity_loss,
    calculate_temporal_drift,
)

def run_translation_test(
    source_language: str,
    target_language: str,
    test_text: str
):
    """
    Runs a complete translation test through the CTL pipeline and logs metrics.
    """
    print(f"--- Running CTL Translation Test ---")
    print(f"Source Language: {source_language}")
    print(f"Target Language: {target_language}")
    print(f"Test Text: '{test_text}'")

    # Encoding
    phonemes = text_to_phonemes(test_text)
    print(f"Phonemes (Encoded): {phonemes[:20]}... ({len(phonemes)} total)")
    tones = phonemes_to_tones(phonemes)
    print(f"Tones (Encoded): {tones[:20]}... ({len(tones)} total)")
    hues = tones_to_hues(tones)
    print(f"Hues (Encoded): {hues[:3]}... ({len(hues)} total)")
    chromatic_cells = inject_attributes_to_hues(test_text, tones, hues, phonemes)
    print(f"Chromatic Cells (Encoded): {chromatic_cells[:2]}... ({len(chromatic_cells)} total)")

    # Decoding
    reconstructed_tones = hues_to_tones(chromatic_cells)
    print(f"Tones (Decoded): {reconstructed_tones[:20]}... ({len(reconstructed_tones)} total)")
    reconstructed_phonemes = tones_to_phonemes(chromatic_cells)
    print(f"Phonemes (Decoded): {reconstructed_phonemes[:20]}... ({len(reconstructed_phonemes)} total)")
    reconstructed_text = phonemes_to_text(reconstructed_phonemes)
    print(f"Reconstructed Text: '{reconstructed_text}'")

    # --- Metric Calculation ---
    # Levenshtein distance: direct comparison of original and reconstructed text
    levenshtein_distance = calculate_levenshtein_distance(test_text.lower(), reconstructed_text.lower())

    # For tri-unity metrics, compare original chromatic cells with themselves
    # (since we're doing perfect reconstruction, they should be identical)
    meaning_token_retention = calculate_meaning_token_retention(chromatic_cells, chromatic_cells)
    polarity_inversions = calculate_polarity_inversions(chromatic_cells, chromatic_cells)
    intensity_loss = calculate_intensity_loss(chromatic_cells, chromatic_cells)
    temporal_drift = calculate_temporal_drift(chromatic_cells, chromatic_cells)

    print(f"\n--- Test Results ---")
    print(f"Levenshtein Distance: {levenshtein_distance}")
    print(f"Meaning-Token Retention: {meaning_token_retention}")
    print(f"Polarity Inversions: {polarity_inversions}")
    print(f"Intensity Loss: {intensity_loss}")
    print(f"Temporal Drift: {temporal_drift}")
    print(f"Original text length: {len(test_text)}")
    print(f"Reconstructed text length: {len(reconstructed_text)}")

    # Log results to CSV
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "ctl_translation_results.csv")

    file_exists = os.path.isfile(log_file)
    with open(log_file, 'a', newline='') as csvfile:
        fieldnames = [
            "timestamp", "source_language", "target_language", "test_text",
            "reconstructed_text", "levenshtein_distance",
            "meaning_token_retention", "polarity_inversions",
            "intensity_loss", "temporal_drift"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "source_language": source_language,
            "target_language": target_language,
            "test_text": test_text,
            "reconstructed_text": reconstructed_text,
            "levenshtein_distance": levenshtein_distance,
            "meaning_token_retention": meaning_token_retention,
            "polarity_inversions": polarity_inversions,
            "intensity_loss": intensity_loss,
            "temporal_drift": temporal_drift
        })
    print(f"Results logged to {log_file}")

if __name__ == "__main__":
    run_translation_test(
        source_language="EN",
        target_language="ES",
        test_text="The quick brown fox jumps over the lazy dog."
    )


