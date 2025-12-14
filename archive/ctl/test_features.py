"""Quick feature test for CTL intensity and polarity logic"""

from ctl.ctl_encode import encode_text_to_chromatic_cells
from ctl.ctl_decode import decode_chromatic_cells_to_text

# Test 1: Intensity from capitals
print("=== Test 1: Intensity Calculation ===")
test_cases = [
    "hello",           # Base: 1.0 (length 5)
    "HELLO",           # +0.3 for caps = 1.3
    "world!",          # +0.2 for ! = 1.2
    "WONDERFUL!",      # +0.3 caps, +0.2 !, +0.1 length>7 = 1.6
    "hi",              # -0.1 length<=3 = 0.9
]

for text in test_cases:
    cells = encode_text_to_chromatic_cells(text)
    # Get intensity of first character (representative of word)
    if cells:
        first_intensity = cells[0]['intensity']
        print(f"'{text}' -> Intensity: {first_intensity}")

# Test 2: Polarity from NOT-words
print("\n=== Test 2: Polarity Calculation ===")
polarity_tests = [
    "I am happy",                  # All +1
    "I am not happy",              # "am"=+1, "not"=+1, "happy"=-1 (negated)
    "no way",                      # "no"=+1, "way"=-1 (negated)
    "never ever again",            # "never"=+1, "ever"=-1, "again"=-1 (window=3)
    "Is this good?",               # "good?"=0 (question mark)
]

for text in polarity_tests:
    cells = encode_text_to_chromatic_cells(text)
    words = text.split()
    print(f"\nText: '{text}'")

    # Map cells to words
    word_idx = 0
    for cell in cells:
        if cell['phoneme'] == ' ':
            word_idx += 1
        else:
            if word_idx < len(words):
                print(f"  {cell['phoneme']} (word: {words[word_idx]}) -> polarity={cell['polarity']}")

# Test 3: Round-trip reconstruction
print("\n=== Test 3: Round-trip Reconstruction ===")
round_trip_tests = [
    "The quick brown fox",
    "HELLO WORLD!",
    "I do not like this",
    "What is your name?",
]

for text in round_trip_tests:
    cells = encode_text_to_chromatic_cells(text)
    reconstructed = decode_chromatic_cells_to_text(cells)
    match = "[PASS]" if text.lower() == reconstructed.lower() else "[FAIL]"
    print(f"{match} '{text}' -> '{reconstructed}'")

print("\n=== All Tests Complete ===")
