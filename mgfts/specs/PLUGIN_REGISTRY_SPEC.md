# MGFTS Plugin Registry Instructions

## 0. Purpose

This document instructs the agent to define how **plugins (tools)** are registered, discovered, and invoked by the ALM Constitutional Engine.

The Plugin Registry ensures:
- ALM knows what tools exist.
- ALM knows how to run them.
- ALM can reason about tool capabilities and layers.

---

## 1. Concepts in Force

- **Tool Manifest** (already specified)
- **Plugins** (concrete tool implementations)
- **Registry** (ALM's internal view of tools)
- **Deterministic Governance** (no ambiguous tool selection)

---

## 2. Registry Data Model

The agent SHOULD define an internal registry representation matching the manifest, e.g.:

```json5
{
  "tools_by_name": {
    "directory_scanner": {
      "name": "directory_scanner",
      "language": "python",
      "entry": "tools/plugins/python/directory_scanner.py",
      "category": "structural",
      "targets_layers": [1],
      "version": "1.0.0",
      "deterministic": true
    },
    "template_validator": {
      "name": "template_validator",
      ...
    }
  },
  "tools_by_layer": {
    "1": ["directory_scanner", "template_validator", "naming_checker"],
    "2": ["governance_analyzer"],
    ...
  }
}
```

This registry can be built at runtime by loading and validating `tool_manifest.json5`.

---

## 3. Tool Selection Logic

The agent SHOULD define selection rules:

1. **By MGFTS Layer**
   - For each layer (1–7), the registry lists the tools that can analyze that layer.
2. **By Category**
   - Structural issues → structural tools
   - Semantic issues → semantic tools
   - Schema issues → schema tools
   - Utility tasks → utility tools (e.g. spell checker)
3. **By Project State**
   - If required files are missing:
     - Run `directory_scanner` and `template_validator` first.
   - If schemas are present:
     - Run `schema_validator`, `meta_schema_validator`.
   - If concept vault exists:
     - Run `concept_linker`, `ontology_checker`.

ALM SHOULD decide which tools to invoke based on:

- MGFTS rules
- project configuration
- manifest contents.

---

## 4. Execution Contract

Agents implementing the registry MUST ensure:

- Tools are invoked as external processes (or as callable modules) with:
  - JSON config on stdin or argument.
- Outputs are captured as JSON and validated against:
  - A minimal tool-output schema.

If a tool fails:

- Registry should record:
  - failure state
  - error message
  - skip that tool's contribution to scores
- ALM still generates a partial report.

---

## 5. Deliverables for Agent

The agent SHOULD:

1. Define a registry builder module (design only, code optional at this stage), e.g.:
   - `alm/mod/tool_registry.py`
   - which:
     - loads `tool_manifest.json5`
     - validates against `tool_manifest.schema.json5`
     - builds internal registry structures.
2. Document the registry behavior in:
   - `mgfts/specs/Plugin_Registry_Spec.md`

The agent MUST NOT:

- Implement deep ALM logic here (this doc is only about registry behavior).
- Hard-code tool paths instead of reading from manifest.

---

**Version:** 1.0
**Status:** Specification
**Last Updated:** 2025-01-15
