from pathlib import Path
import re


def test_seed_config_literals_and_salts():
    config_header = Path("alm/core/include/alm/config.hpp").read_text(encoding="utf-8")
    assert "SeedConfig" in config_header
    assert "LaneSeed" in config_header
    assert "kDefaultSeed" in config_header

    salts_block = re.search(r"register_salts\{([^}]*)\}", config_header, re.MULTILINE | re.DOTALL)
    assert salts_block, "register salts must be defined for deterministic seeding"
    salts = re.findall(r"0x[0-9A-Fa-f]+ULL", salts_block.group(1))
    assert len(salts) == 4, "expected four register salts to cover each register lane"


def test_initialization_clears_padding_and_uses_seed_mapping():
    init_header = Path("alm/core/include/alm/initialization.hpp").read_text(encoding="utf-8")
    assert "SeedToUnitFloat" in init_header, "seed normalization must be available"
    assert "ClearPadding" in init_header, "padding lanes must be zeroed deterministically"
    assert "InitializeFrame" in init_header, "frames must be initialized deterministically"
    assert "IsPaddingLane" in init_header, "initialization must respect padding lanes"


def test_default_seed_literal_is_present():
    constants_header = Path("alm/core/include/alm/constants.hpp").read_text(encoding="utf-8")
    assert "kDefaultSeed" in constants_header
    assert "0xA1B2C3D4u" in constants_header
