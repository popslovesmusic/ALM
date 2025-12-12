# ALM Constitutional Engine Test Plan

## Purpose

Define comprehensive testing strategy for ALM-GOV v0.1 (analysis-only mode).

---

## Test Objectives

1. **Correctness**: Ensure analysis is accurate
2. **Determinism**: Same input → same output
3. **Completeness**: All components tested
4. **Regression**: Prevent regressions via golden files
5. **Coverage**: Achieve >90% code coverage

---

## Test Categories

### 1. Tool Manifest Validation Tests

**Module:** `test_tool_manifest.py`

**Purpose:** Ensure tool manifest is valid and complete

**Tests:**
- `test_manifest_syntax`: JSON5 syntax is valid
- `test_manifest_schema`: Conforms to `tool_manifest.schema.json5`
- `test_tool_uniqueness`: All tool names are unique
- `test_required_fields`: All tools have required fields
- `test_determinism_flag`: All tools are deterministic
- `test_layer_ranges`: Layer targets are 1-7
- `test_category_validity`: Categories are from approved list

**Fixtures:**
- Valid manifest
- Invalid manifests (various error types)

---

### 2. Registry Construction Tests

**Module:** `test_tool_registry.py`

**Purpose:** Validate tool registry behavior

**Tests:**
- `test_registry_loading`: Registry loads manifest correctly
- `test_tools_by_name`: Tool lookup by name works
- `test_tools_by_layer`: Tool lookup by layer works
- `test_tools_by_category`: Tool lookup by category works
- `test_tool_selection`: Correct tools selected for project state
- `test_missing_manifest`: Handles missing manifest gracefully
- `test_invalid_manifest`: Handles invalid manifest gracefully
- `test_tool_execution`: Can execute a simple tool
- `test_tool_timeout`: Respects timeout limits

**Fixtures:**
- Test manifest with known tools
- Mock project states
- Dummy test tool

---

### 3. State Model Tests

**Module:** `test_state_model.py`

**Purpose:** Verify state aggregation logic

**Tests:**
- `test_state_initialization`: State initializes correctly
- `test_add_tool_result`: Tool results aggregate properly
- `test_violation_grouping`: Violations group by severity/layer
- `test_score_computation`: Overall score computes correctly
- `test_coherence_update`: Coherence score updates
- `test_concealment_update`: Concealment score updates
- `test_concept_tracking`: Concept lists maintained
- `test_to_dict`: State serializes correctly

**Fixtures:**
- Mock tool results
- Known state configurations

---

### 4. Reporting Engine Tests

**Module:** `test_reporting_engine.py`

**Purpose:** Validate report generation

**Tests:**
- `test_json_report_structure`: JSON report has required fields
- `test_json_schema_compliance`: JSON matches schema
- `test_markdown_sections`: Markdown has all sections
- `test_aletheia_commentary`: Commentary is present
- `test_summary_table`: Table formats correctly
- `test_golden_json`: JSON matches golden file
- `test_golden_markdown`: Markdown matches golden file (structure)

**Fixtures:**
- Known state
- Golden report files

---

### 5. Basic Structural Analysis Tests

**Module:** `test_structural_analysis.py`

**Purpose:** Test end-to-end structural validation

**Tests:**
- `test_valid_project`: Compliant project scores well
- `test_missing_files`: Missing files detected
- `test_invalid_naming`: Naming violations detected
- `test_empty_project`: Empty project handled correctly

**Fixtures:**
- `fixtures/projects/minimal_valid_project/`
- `fixtures/projects/missing_templates_project/`
- `fixtures/projects/empty_project/`

---

### 6. Error Handling Tests

**Module:** `test_error_handling.py`

**Purpose:** Verify graceful failure handling

**Tests:**
- `test_tool_failure`: Failed tool doesn't crash engine
- `test_tool_timeout`: Timeout handled gracefully
- `test_invalid_json_output`: Invalid tool output handled
- `test_missing_tool`: Missing tool reported
- `test_partial_analysis`: Partial results still generate report

**Fixtures:**
- Broken tools
- Malformed outputs

---

### 7. Integration Tests

**Module:** `test_integration.py`

**Purpose:** Test complete workflows

**Tests:**
- `test_full_analysis_pipeline`: Complete analysis runs
- `test_report_generation`: Reports generated correctly
- `test_multiple_projects`: Can analyze multiple projects
- `test_layer_filtering`: Can analyze specific layers only

**Fixtures:**
- Full test projects
- Expected outputs

---

## Test Data Structure

```
/alm/tests/
  test_tool_manifest.py
  test_tool_registry.py
  test_state_model.py
  test_reporting_engine.py
  test_structural_analysis.py
  test_error_handling.py
  test_integration.py

  /fixtures/
    /manifests/
      valid_manifest.json5
      invalid_manifest_missing_field.json5
      invalid_manifest_bad_syntax.json5

    /projects/
      /minimal_valid_project/
        AGENTS.md
        /agents/
          SESSION_INSTRUCTIONS.md
          PROJECT_RULES.md
        /concepts/
          PROJECT_CONCEPT_VAULT.json5

      /missing_templates_project/
        # Intentionally incomplete

      /empty_project/
        # Empty directory

    /golden/
      mgfts_report_expected.json
      mgfts_report_expected.md

    /tools/
      dummy_tool.py
      failing_tool.py
      timeout_tool.py
```

---

## Testing Framework

**Framework:** pytest

**Installation:**
```bash
pip install pytest pytest-cov
```

**Running Tests:**
```bash
# All tests
pytest alm/tests/

# Specific module
pytest alm/tests/test_tool_manifest.py

# With coverage
pytest --cov=alm --cov-report=html alm/tests/

# Verbose
pytest -v alm/tests/
```

---

## Coverage Requirements

**Minimum Coverage:** 90%

**Modules:**
- `alm/mod/governance_core.py`: 85%+
- `alm/mod/state_model.py`: 95%+
- `alm/mod/tool_registry.py`: 90%+
- `alm/mod/report_builder.py`: 85%+
- `alm/mod/report_writer_json.py`: 95%+
- `alm/mod/report_writer_md.py`: 90%+

---

## Golden File Management

**Golden files** are known-good outputs for regression testing.

**Location:** `/alm/tests/fixtures/golden/`

**Usage:**
1. Generate output with known-good implementation
2. Manually verify correctness
3. Save as golden file
4. Compare future outputs to golden file

**Updating:**
- Only update when behavior intentionally changes
- Document reason for update
- Review diff carefully

---

## Determinism Verification

All tests must be deterministic:

✓ **Allowed:**
- Fixed inputs
- Sorted outputs
- Consistent ordering

✗ **Forbidden:**
- Random data
- Timestamps in assertions
- File system order dependence
- Network calls

---

## Continuous Integration

Tests run automatically on:
- Every commit (via pre-commit hook)
- Every pull request
- Nightly (full suite + coverage)

**CI Configuration:**
- GitHub Actions / GitLab CI
- Run on Python 3.8, 3.9, 3.10, 3.11
- Fail on coverage < 90%
- Fail on any test failure

---

## Test Development Guidelines

1. **One assertion per test** (when possible)
2. **Descriptive test names** (`test_should_reject_invalid_severity`)
3. **Use fixtures** for common data
4. **Mock external dependencies** (file system when appropriate)
5. **Test error paths** not just happy paths
6. **Document complex tests** with docstrings

---

**Version:** 1.0.0
**Last Updated:** 2025-01-15
