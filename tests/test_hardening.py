from pathlib import Path


CHECKLIST_SECTIONS = [
    "Topology (Must Be Instantiable)",
    "Ingest (Must Be Mechanically Checkable)",
    "Coefficients (Must Be Generatable)",
    "Time / Rotation (Must Be Numeric)",
    "Residual Ambiguities Are Labeled Correctly",
]


def test_blueprint_checklist_sections_present():
    checklist_text = Path("docs/blueprint/Blueprint checklist.md").read_text(encoding="utf-8")

    for section in CHECKLIST_SECTIONS:
        assert section in checklist_text, f"missing checklist section: {section}"
