# MGFTS Tool Manifest Specification

## 0. Purpose

This document instructs the agent to define a **Tool Manifest Specification** for the MGFTS ecosystem.

The Tool Manifest describes all tools available to the ALM Constitutional Engine, including:
- structural analyzers
- semantic analyzers
- schema validators
- spell checkers
- parsers
- classifiers
- other utility tools

---

## 1. Concepts in Force

- **MGFTS:**
  Global multi-layer file, schema, and concept governance system.

- **ALM Constitutional Engine:**
  The orchestrator that reasons about which tools to run.

- **Tool Library:**
  A collection of small, focused programs that:
  - perform analysis
  - output structured JSON
  - do not decide policies

- **Determinism:**
  Tools MUST produce the same output given the same input and configuration.

---

## 2. High-Level Requirements

The Tool Manifest MUST:

1. Enumerate all available tools.
2. Describe each tool's:
   - name
   - version
   - language (python/js/other)
   - entry point path
   - capabilities (what it analyzes)
   - input requirements
   - output contract
   - target MGFTS layers
3. Be machine-readable (JSON5 recommended).
4. Be human-readable enough to audit.
5. Be easy to extend with new tools over time.

---

## 3. Tool Manifest Structure

The agent SHOULD define a manifest file like:

`/tools/tool_manifest.json5`

Suggested structure:

```json5
{
  "version": "1.0",
  "tools": [
    {
      "name": "directory_scanner",
      "language": "python",
      "entry": "plugins/directory_scanner.py",
      "version": "1.0.0",
      "description": "Scans project directories and enumerates files, directories, sizes, and timestamps.",
      "capabilities": ["structure_scan"],
      "targets_layers": [1],
      "inputs": ["project_path"],
      "outputs": ["file_index", "dir_index", "metrics"],
      "deterministic": true,
      "config": {
        "follow_symlinks": false
      }
    },
    {
      "name": "template_validator",
      "language": "python",
      "entry": "plugins/template_validator.py",
      "version": "1.0.0",
      "description": "Validates that required templates exist and match template/meta-template definitions.",
      "capabilities": ["template_validation"],
      "targets_layers": [1, 3],
      "inputs": ["project_path", "template_dir"],
      "outputs": ["violations", "metrics", "score"],
      "deterministic": true,
      "config": {}
    }
    // additional tools...
  ]
}
```

---

## 4. Tool Categories

The agent SHOULD support categorizing tools as:

- structural
- content
- semantic
- schema
- meta_schema
- ontological
- utility (e.g. spell checker, parser, classifier)

Each tool SHOULD include a category field:

```json5
"category": "structural"
```

---

## 5. Tool IO Contract (Reinforced)

All non-trivial tools MUST:

- Accept configuration via JSON-like input.
- Write results in a standard JSON-like structure.

Minimal output fields:

```json5
{
  "tool": "name",
  "version": "1.0.0",
  "layer_targets": [1, 2],
  "violations": [ ... ],
  "warnings": [ ... ],
  "metrics": { "metric_name": value },
  "score": 0.0
}
```

---

## 6. Manifest Validation

The agent SHOULD:

1. Define a JSON5 schema for `tool_manifest.json5`, e.g.:
   `mgfts/meta_schemas/tool_manifest.schema.json5`
2. Ensure:
   - All tools have unique name.
   - Each tool declares language, entry, category.
   - `deterministic: true` is required for tools used by the Constitutional Engine.
   - `targets_layers` is non-empty, and all values are between 1 and 7.

---

## 7. Deliverables for Agent

The agent SHOULD produce:

1. `mgfts/specs/Tool_Manifest_Specification.md`
   - A cleaned-up, finalized spec derived from this document.
2. `tools/tool_manifest.json5` (initial version)
   - With at least stub entries for:
     - directory_scanner
     - template_validator
     - naming_checker
     - schema_validator
     - spell_checker
     - concept_linker
3. `mgfts/meta_schemas/tool_manifest.schema.json5`
   - A schema for validating the manifest itself.

The agent MUST NOT:

- Implement tool logic itself in this pass.
- Modify existing project code.

---

**Version:** 1.0
**Status:** Specification
**Last Updated:** 2025-01-15
