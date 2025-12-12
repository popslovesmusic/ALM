# MGFTS Tool Library Overview

## Purpose

The MGFTS Tool Library is a collection of small, focused analysis programs that work together to validate projects against MGFTS (Meta-Global File Template System) compliance requirements.

Each tool is:
- **Focused**: Does one thing well
- **Deterministic**: Same input → same output
- **Composable**: Works with other tools
- **Standardized**: Follows the MGFTS tool contract

---

## Architecture

```
ALM Constitutional Engine (Orchestrator)
    ↓
Tool Registry (Manifest-based discovery)
    ↓
Tool Library (Analysis execution)
    ├── Structural Tools (Layer 1)
    ├── Governance Tools (Layer 2)
    ├── Schema Tools (Layer 3)
    ├── Semantic Tools (Layer 4)
    ├── Ecological Tools (Layer 5)
    ├── Formal Tools (Layer 6)
    ├── Ontological Tools (Layer 7)
    └── Utility Tools (Cross-cutting)
```

---

## Tool Discovery

Tools are discovered via the **Tool Manifest** (`/tools/tool_manifest.json5`):

1. Constitutional Engine loads the manifest
2. Parses tool definitions
3. Builds internal registry (tools by name, by layer, by category)
4. Selects appropriate tools based on project state and analysis requirements

---

## Tool Invocation

### Input (stdin):
```json
{
  "project_path": "/path/to/project",
  "mgfts_root": "/path/to/mgfts",
  "config": {
    "tool_specific": "options"
  }
}
```

### Output (stdout):
```json
{
  "tool": "tool_name",
  "version": "1.0.0",
  "layer_targets": [1, 3],
  "violations": [
    {
      "code": "VIOLATION_CODE",
      "message": "Description",
      "path": "/relative/path",
      "severity": "critical",
      "layer": 1
    }
  ],
  "warnings": [...],
  "metrics": {
    "files_scanned": 42,
    "issues_found": 3
  },
  "score": 0.95
}
```

---

## Tool Categories

### Structural Tools
**Layer:** 1 (Structural)
**Purpose:** Validate file/directory structure, naming conventions, file presence

**Examples:**
- `directory_scanner`: Enumerates project structure
- `template_validator`: Checks required templates exist
- `naming_checker`: Validates naming conventions

### Governance Tools
**Layer:** 2 (Governance)
**Purpose:** Validate governance files (AGENTS.md, rules, compliance)

**Examples:**
- `governance_analyzer`: Checks governance file completeness

### Schema Tools
**Layer:** 3 (Meta-Schema)
**Purpose:** Validate JSON5/schema files against meta-schemas

**Examples:**
- `schema_validator`: Validates JSON5 syntax and schema conformance
- `template_validator`: Validates templates against meta-templates

### Semantic Tools
**Layer:** 4 (Semantic)
**Purpose:** Analyze concepts, references, definitions

**Examples:**
- `concept_linker`: Finds missing/unused concepts

### Utility Tools
**Layer:** N/A (cross-cutting)
**Purpose:** Supporting functions (spell check, formatting)

**Examples:**
- `spell_checker`: Checks documentation spelling

### Meta-Schema Tools
**Purpose:** Compute aggregate metrics

**Examples:**
- `coherence_calculator`: Computes Coherence Field score
- `concealment_calculator`: Computes Concealment Functional

---

## Determinism Requirements

All tools MUST be deterministic:

✓ **Allowed:**
- File reading
- String parsing
- Mathematical computations
- Pattern matching
- Schema validation

✗ **Forbidden:**
- Random number generation
- Network calls
- Timestamp dependencies (except for logging)
- Non-deterministic algorithms

---

## Tool Lifecycle

1. **Registration**: Tool added to `tool_manifest.json5`
2. **Validation**: Manifest validated against `tool_manifest.schema.json5`
3. **Discovery**: Constitutional Engine loads manifest
4. **Selection**: Engine determines which tools to run
5. **Execution**: Tools run with JSON input
6. **Collection**: Engine collects JSON output
7. **Aggregation**: Results merged into global state
8. **Reporting**: Final report generated

---

## Available Tools (v1.0)

| Tool | Language | Layer | Purpose |
|------|----------|-------|---------|
| `directory_scanner` | Python | 1 | Scan project structure |
| `template_validator` | Python | 1, 3 | Validate templates |
| `naming_checker` | Python | 1 | Check naming conventions |
| `schema_validator` | Python | 3 | Validate JSON5 schemas |
| `concept_linker` | Python | 4 | Analyze concept usage |
| `spell_checker` | Python | - | Check spelling |
| `governance_analyzer` | Python | 2 | Check governance files |
| `coherence_calculator` | Python | 2-4 | Compute coherence |
| `concealment_calculator` | Python | 1-4 | Compute concealment |

---

## Adding New Tools

See [TOOL_DEVELOPER_GUIDE.md](TOOL_DEVELOPER_GUIDE.md) for detailed instructions on creating and registering new tools.

---

**Version:** 1.0.0
**Last Updated:** 2025-01-15
