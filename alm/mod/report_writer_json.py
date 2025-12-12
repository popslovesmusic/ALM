"""ALM Constitutional Engine - JSON Report Writer

Generates machine-readable MGFTS_REPORT.json files.

Output follows the mgfts_report.schema.json5 specification.

Author: ALM Constitutional Engine
Version: 0.1.0
"""

import json
from typing import Any, Dict
from pathlib import Path


def write_json_report(state_dict: Dict[str, Any], output_path: Path) -> None:
    """Write MGFTS compliance report as JSON.

    Parameters
    ----------
    state_dict : dict
        State model dictionary representation
    output_path : Path
        Path to output file

    Notes
    -----
    Output is formatted with:
    - 2-space indentation
    - Sorted keys (for diffing)
    - UTF-8 encoding
    """
    # Ensure stable key ordering for reproducibility
    sorted_state = _sort_dict_recursive(state_dict)

    # Write JSON with formatting
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sorted_state, f, indent=2, ensure_ascii=False)


def _sort_dict_recursive(d: Any) -> Any:
    """Recursively sort dictionary keys.

    Parameters
    ----------
    d : any
        Value to sort (dict, list, or primitive)

    Returns
    -------
    any
        Sorted structure
    """
    if isinstance(d, dict):
        return {k: _sort_dict_recursive(v) for k, v in sorted(d.items())}
    elif isinstance(d, list):
        return [_sort_dict_recursive(item) for item in d]
    else:
        return d


def validate_against_schema(report_dict: Dict[str, Any]) -> bool:
    """Validate report against mgfts_report.schema.json5.

    Parameters
    ----------
    report_dict : dict
        Report to validate

    Returns
    -------
    bool
        True if valid

    Notes
    -----
    This is a stub. Full implementation would use jsonschema library.
    """
    # TODO: Implement schema validation
    # - Load mgfts_report.schema.json5
    # - Use jsonschema validator
    # - Return validation result
    required_keys = [
        "project",
        "timestamp",
        "scores",
        "violations",
        "warnings",
        "coherence_score",
        "concealment_score"
    ]

    for key in required_keys:
        if key not in report_dict:
            return False

    return True


def format_for_diff(report_dict: Dict[str, Any]) -> str:
    """Format report for easy diffing.

    Parameters
    ----------
    report_dict : dict
        Report dictionary

    Returns
    -------
    str
        Formatted JSON string optimized for diff tools
    """
    # One key per line, sorted, trailing commas
    return json.dumps(
        _sort_dict_recursive(report_dict),
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    ) + "\n"
