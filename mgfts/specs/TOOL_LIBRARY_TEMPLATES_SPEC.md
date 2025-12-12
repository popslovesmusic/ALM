# MGFTS Tool Library Templates — Agent Instructions

## 0. Purpose

This document instructs the agent to create **file and code templates** for tools in the MGFTS Tool Library.

These templates define:
- directory structure
- base Python plugin
- base JS plugin
- standard IO format
- metadata headers

The goal is to standardize new tool creation.

---

## 1. Concepts in Force

- **Tool Library:**
  A collection of small analysis programs.

- **Plugins:**
  Tools that conform to common interface rules.

- **ALM Constitutional Engine:**
  Orchestrates tools and consumes their JSON outputs.

- **Determinism:**
  Tools must be deterministic when used in constitutional analysis.

---

## 2. Directory Layout for Tools

The agent SHOULD define:

```
/tools/
  /plugins/
    /python/
      directory_scanner.py
      template_validator.py
      ...
    /js/
      spell_checker.js
      classifier.js
      ...
  tool_manifest.json5
  /docs/
    TOOL_LIBRARY_OVERVIEW.md
    TOOL_DEVELOPER_GUIDE.md
```

This layout is a recommendation and may be adjusted as needed, but `/tools/plugins/` SHOULD exist as the default plugin directory.

---

## 3. Python Plugin Template

The agent SHOULD create a Python template at:

`/tools/templates/python_plugin_template.py`

Example content:

```python
"""MGFTS Tool Plugin Template (Python)

This file serves as a template for MGFTS-compatible analysis tools.

Requirements:
- Deterministic behavior given the same inputs.
- Read configuration and parameters from JSON-like input.
- Write results to stdout or a specified file in JSON-like format.

"""

import json
import sys
from typing import Any, Dict


def run_tool(config: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the tool's logic.

    Parameters
    ----------
    config : dict
        Configuration including at least:
        - project_path: str
        - any tool-specific options

    Returns
    -------
    dict
        Standard MGFTS tool output, e.g.:
        {
            "tool": "example_tool",
            "version": "1.0.0",
            "layer_targets": [1],
            "violations": [],
            "warnings": [],
            "metrics": {},
            "score": 1.0
        }
    """
    # TODO: Implement actual logic in derived tools.
    result = {
        "tool": "example_tool",
        "version": "1.0.0",
        "layer_targets": [],
        "violations": [],
        "warnings": [],
        "metrics": {},
        "score": 1.0,
    }
    return result


def main() -> None:
    # Read JSON config from stdin
    config_text = sys.stdin.read()
    config = json.loads(config_text)

    result = run_tool(config)

    print(json.dumps(result))


if __name__ == "__main__":
    main()
```

Agents generating real tools SHOULD copy this template and customize `run_tool`.

---

## 4. JS Plugin Template (Optional for Now)

If Node/JS tools are desired, the agent SHOULD create:

`/tools/templates/js_plugin_template.js`

With equivalent semantics:

- read JSON from stdin
- output JSON to stdout
- implement `runTool(config)`.

---

## 5. Developer Docs Templates

The agent SHOULD prepare:

1. `/tools/docs/TOOL_LIBRARY_OVERVIEW.md`
   - Explains:
     - how tools are discovered (via manifest)
     - how tools are invoked by ALM
     - IO format
     - deterministic requirements
2. `/tools/docs/TOOL_DEVELOPER_GUIDE.md`
   - Explains:
     - how to create a new tool
     - how to register it in the manifest
     - how to test it
     - how to ensure determinism

---

## 6. Deliverables for Agent

The agent SHOULD produce:

1. `/tools/templates/python_plugin_template.py`
2. (Optional) `/tools/templates/js_plugin_template.js`
3. `/tools/docs/TOOL_LIBRARY_OVERVIEW.md`
4. `/tools/docs/TOOL_DEVELOPER_GUIDE.md`
5. Ensure `tool_manifest.json5` references at least one tool that could be implemented from the Python template.

The agent MUST NOT:

- Write functional tool logic here (stubs and templates only).
- Modify real project files.

---

**Version:** 1.0
**Status:** Specification
**Last Updated:** 2025-01-15
