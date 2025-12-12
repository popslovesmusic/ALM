# MGFTS Tool Developer Guide

## Purpose

This guide explains how to create new analysis tools for the MGFTS Tool Library.

---

## Quick Start

### Step 1: Choose a Template

**Python:**
```bash
cp /tools/templates/python_plugin_template.py /tools/plugins/python/my_tool.py
```

**JavaScript:**
```bash
cp /tools/templates/js_plugin_template.js /tools/plugins/js/my_tool.js
```

### Step 2: Implement `runTool()` Function

Replace the TODO section with your analysis logic:

```python
def run_tool(config: Dict[str, Any]) -> Dict[str, Any]:
    project_path = config["project_path"]

    # Your analysis logic here
    violations = []
    warnings = []
    metrics = {}

    # Example: Check for missing file
    if not os.path.exists(os.path.join(project_path, "AGENTS.md")):
        violations.append({
            "code": "MISSING_AGENTS_MD",
            "message": "Required file AGENTS.md not found",
            "path": "/AGENTS.md",
            "severity": "critical",
            "layer": 2
        })

    return {
        "tool": "my_tool",
        "version": "1.0.0",
        "layer_targets": [2],
        "violations": violations,
        "warnings": warnings,
        "metrics": metrics,
        "score": 1.0 - (len(violations) * 0.1)
    }
```

### Step 3: Register in Manifest

Add entry to `/tools/tool_manifest.json5`:

```json5
{
  name: "my_tool",
  language: "python",
  entry: "plugins/python/my_tool.py",
  version: "1.0.0",
  category: "governance",
  description: "Checks for governance file presence",
  capabilities: ["governance_validation"],
  targets_layers: [2],
  inputs: ["project_path"],
  outputs: ["violations", "warnings", "metrics", "score"],
  deterministic: true,
  config: {}
}
```

### Step 4: Test Your Tool

```bash
echo '{"project_path": "/path/to/test/project"}' | python /tools/plugins/python/my_tool.py
```

---

## Tool Contract Specification

### Input Contract

Tools receive JSON via stdin with at minimum:

```json5
{
  project_path: "/absolute/path/to/project",
  mgfts_root: "/absolute/path/to/mgfts",  // optional
  config: {
    // tool-specific configuration
  }
}
```

### Output Contract

Tools MUST output JSON to stdout with:

**Required Fields:**
- `tool` (string): Tool name
- `version` (string): Semantic version
- `layer_targets` (array of int): MGFTS layers (1-7)
- `violations` (array): Critical issues
- `warnings` (array): Non-critical issues
- `metrics` (object): Numeric measurements

**Optional Fields:**
- `score` (float 0-1): Compliance score

### Violation/Warning Structure

```json5
{
  code: "VIOLATION_CODE",          // SCREAMING_SNAKE_CASE
  message: "Human-readable description",
  path: "/relative/path/from/project/root",
  severity: "critical",            // critical|high|medium|low
  layer: 2                         // MGFTS layer number
}
```

---

## Best Practices

### 1. Determinism

✓ **DO:**
- Read files from `project_path`
- Use fixed algorithms
- Sort output consistently
- Return same results for same input

✗ **DON'T:**
- Use random numbers
- Make network calls
- Depend on system time (except for logging)
- Rely on undefined behavior

### 2. Error Handling

✓ **DO:**
- Validate all inputs
- Handle missing files gracefully
- Return partial results if possible
- Write errors to stderr as JSON

✗ **DON'T:**
- Crash on missing files
- Print stack traces to stdout
- Exit without JSON output
- Swallow errors silently

### 3. Performance

✓ **DO:**
- Process files incrementally
- Use efficient algorithms
- Respect timeout limits
- Cache repeated computations

✗ **DON'T:**
- Load entire project into memory
- Use exponential-time algorithms
- Re-read same files repeatedly
- Block indefinitely

### 4. Output Quality

✓ **DO:**
- Provide specific error messages
- Include file paths and line numbers
- Suggest remediation when possible
- Use consistent severity levels

✗ **DON'T:**
- Report vague errors
- Omit context
- Mix violations with warnings
- Use inconsistent terminology

---

## Severity Levels

Use these consistently:

- **critical**: Prevents MGFTS compliance; must fix
- **high**: Major issue; should fix soon
- **medium**: Moderate issue; fix when convenient
- **low**: Minor issue or style violation

---

## Testing Your Tool

### Manual Testing

```bash
# Create test input
cat > test_config.json <<EOF
{
  "project_path": "/path/to/test/project",
  "config": {}
}
EOF

# Run tool
python /tools/plugins/python/my_tool.py < test_config.json

# Check output is valid JSON
python /tools/plugins/python/my_tool.py < test_config.json | python -m json.tool
```

### Automated Testing

Create test file in `/alm/tests/`:

```python
import json
import subprocess

def test_my_tool():
    config = {"project_path": "/test/fixtures/valid_project"}

    result = subprocess.run(
        ["python", "/tools/plugins/python/my_tool.py"],
        input=json.dumps(config),
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    output = json.loads(result.stdout)

    assert output["tool"] == "my_tool"
    assert "violations" in output
    assert "warnings" in output
```

---

## Common Patterns

### Pattern 1: File Presence Checker

```python
required_files = ["/AGENTS.md", "/agents/PROJECT_RULES.md"]

for file_path in required_files:
    full_path = os.path.join(project_path, file_path.lstrip("/"))
    if not os.path.exists(full_path):
        violations.append({
            "code": "MISSING_FILE",
            "message": f"Required file not found: {file_path}",
            "path": file_path,
            "severity": "critical",
            "layer": 1
        })
```

### Pattern 2: Naming Convention Checker

```python
import re

for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith(".py"):
            if not re.match(r'^[a-z][a-z0-9_]*\.py$', file):
                warnings.append({
                    "code": "NAMING_CONVENTION",
                    "message": f"Python file should use snake_case: {file}",
                    "path": os.path.relpath(os.path.join(root, file), project_path),
                    "severity": "medium",
                    "layer": 1
                })
```

### Pattern 3: JSON5 Schema Validator

```python
import json5

schema_path = os.path.join(project_path, "config.json5")
if os.path.exists(schema_path):
    try:
        with open(schema_path) as f:
            data = json5.load(f)
        # Validate against schema...
    except json5.JSON5DecodeError as e:
        violations.append({
            "code": "INVALID_JSON5",
            "message": f"JSON5 syntax error: {str(e)}",
            "path": "/config.json5",
            "severity": "critical",
            "layer": 3
        })
```

---

## Troubleshooting

### Tool Not Appearing in Registry

1. Check `tool_manifest.json5` syntax
2. Validate against `tool_manifest.schema.json5`
3. Ensure `name` is unique
4. Verify `entry` path exists

### Tool Fails to Execute

1. Check tool has execute permissions
2. Verify JSON input is valid
3. Check tool outputs JSON to stdout
4. Review stderr for error messages

### Inconsistent Results

1. Check for non-deterministic operations
2. Verify sort orders are consistent
3. Remove timestamp dependencies
4. Test with same input multiple times

---

## Tool Manifest Fields Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Unique identifier (snake_case) |
| `language` | string | Yes | python\|javascript\|js\|rust\|cpp\|bash\|other |
| `entry` | string | Yes | Relative path from /tools/ |
| `version` | string | Yes | Semantic version (X.Y.Z) |
| `category` | string | Yes | structural\|content\|semantic\|schema\|meta_schema\|ontological\|utility |
| `description` | string | Yes | Human-readable purpose |
| `capabilities` | array | Yes | List of capability tags |
| `targets_layers` | array | Yes | MGFTS layers 1-7 (empty for utility) |
| `inputs` | array | Yes | Required input parameters |
| `outputs` | array | Yes | Output types produced |
| `deterministic` | boolean | Yes | Must be true |
| `config` | object | Yes | Tool-specific config (can be empty) |
| `dependencies` | array | No | Other required tools |
| `optional` | boolean | No | Whether tool is optional |
| `timeout_ms` | number | No | Max execution time |

---

## Examples

See `/tools/plugins/python/` for example implementations:
- `directory_scanner.py` - File enumeration
- `template_validator.py` - Template validation
- `naming_checker.py` - Naming conventions
- `schema_validator.py` - JSON5 validation
- `concept_linker.py` - Concept analysis

---

**Version:** 1.0.0
**Last Updated:** 2025-01-15
