"""MGFTS Tool Plugin Template (Python)

This file serves as a template for MGFTS-compatible analysis tools.

Requirements:
- Deterministic behavior given the same inputs.
- Read configuration and parameters from JSON-like input.
- Write results to stdout or a specified file in JSON-like format.

Tool Output Contract:
- tool: string (name of this tool)
- version: string (semantic version)
- layer_targets: [int] (MGFTS layers analyzed: 1-7)
- violations: [{code, message, path, severity, layer}]
- warnings: [{code, message, path, severity, layer}]
- metrics: {metric_name: value, ...}
- score: float (0-1, optional)

Usage:
  echo '{"project_path": "/path/to/project"}' | python tool_name.py
  python tool_name.py < config.json

Author: MGFTS Constitutional Engine
Version: 1.0.0
"""

import json
import sys
from typing import Any, Dict, List


def run_tool(config: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the tool's logic.

    This is the main entry point for tool implementation.
    Override this function in derived tools with actual analysis logic.

    Parameters
    ----------
    config : dict
        Configuration including at least:
        - project_path: str (required)
        - Any tool-specific options

    Returns
    -------
    dict
        Standard MGFTS tool output with keys:
        - tool: str
        - version: str
        - layer_targets: List[int]
        - violations: List[Dict]
        - warnings: List[Dict]
        - metrics: Dict[str, Any]
        - score: float (0-1, optional)

    Example
    -------
    >>> config = {"project_path": "/path/to/project"}
    >>> result = run_tool(config)
    >>> assert "tool" in result
    >>> assert "violations" in result
    """
    # TODO: Implement actual logic in derived tools.
    # This template provides a minimal valid response.

    project_path = config.get("project_path", ".")

    # Example structure - replace with real analysis
    result = {
        "tool": "example_tool",  # CHANGE THIS to actual tool name
        "version": "1.0.0",
        "layer_targets": [],  # e.g., [1, 3] for layers 1 and 3
        "violations": [
            # Example violation structure:
            # {
            #     "code": "MISSING_FILE",
            #     "message": "Required file not found: AGENTS.md",
            #     "path": "/AGENTS.md",
            #     "severity": "critical",  # critical|high|medium|low
            #     "layer": 2
            # }
        ],
        "warnings": [
            # Example warning structure:
            # {
            #     "code": "NAMING_CONVENTION",
            #     "message": "File should use snake_case naming",
            #     "path": "/ctl/MyModule.py",
            #     "severity": "medium",
            #     "layer": 1
            # }
        ],
        "metrics": {
            # Example metrics:
            # "files_scanned": 42,
            # "total_violations": 0,
            # "total_warnings": 0
        },
        "score": 1.0,  # Optional: 0-1 compliance score
    }

    return result


def validate_config(config: Dict[str, Any]) -> bool:
    """Validate that config contains required fields.

    Parameters
    ----------
    config : dict
        Configuration to validate

    Returns
    -------
    bool
        True if valid, False otherwise
    """
    required_fields = ["project_path"]

    for field in required_fields:
        if field not in config:
            print(
                json.dumps({
                    "error": f"Missing required config field: {field}",
                    "tool": "unknown",
                    "version": "1.0.0"
                }),
                file=sys.stderr
            )
            return False

    return True


def main() -> None:
    """Main entry point.

    Reads JSON config from stdin, runs tool, outputs JSON result to stdout.
    """
    try:
        # Read JSON config from stdin
        config_text = sys.stdin.read()

        if not config_text.strip():
            print(
                json.dumps({
                    "error": "No input provided. Expected JSON config on stdin.",
                    "tool": "unknown",
                    "version": "1.0.0"
                }),
                file=sys.stderr
            )
            sys.exit(1)

        config = json.loads(config_text)

        # Validate config
        if not validate_config(config):
            sys.exit(1)

        # Run tool
        result = run_tool(config)

        # Output result as JSON
        print(json.dumps(result, indent=2))

    except json.JSONDecodeError as e:
        print(
            json.dumps({
                "error": f"Invalid JSON input: {str(e)}",
                "tool": "unknown",
                "version": "1.0.0"
            }),
            file=sys.stderr
        )
        sys.exit(1)

    except Exception as e:
        print(
            json.dumps({
                "error": f"Tool execution failed: {str(e)}",
                "tool": "unknown",
                "version": "1.0.0"
            }),
            file=sys.stderr
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
