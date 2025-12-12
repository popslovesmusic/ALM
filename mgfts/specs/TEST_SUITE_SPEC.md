# ALM-GOV v0.1 Test Suite Instructions

## 0. Purpose

This document instructs the agent to define a **test suite** for the ALM Constitutional Engine (analysis-only mode).

The goal:
- Ensure correctness of:
  - tool registry
  - manifest
  - reporting engine
  - basic MGFTS analysis operations

No enforcement, no autofix — only verification of analysis behavior.

---

## 1. Concepts in Force

- **MGFTS:**
  Provides structural & conceptual expectations.

- **ALM Constitutional Engine:**
  Orchestrates analysis and reporting.

- **Determinism:**
  Tests must be reproducible.

- **Golden Files:**
  Outputs that are known-good and checked into version control for regression detection.

---

## 2. Test Coverage Areas

The test suite SHOULD cover:

1. **Tool Manifest Validation Tests**
   - Ensure `tool_manifest.json5` is:
     - syntactically correct
     - conformant with `tool_manifest.schema.json5`
     - has non-empty, unique tool names

2. **Registry Construction Tests**
   - Given a known manifest:
     - the registry is built correctly
     - tools are mapped to correct layers
     - unknown categories are handled gracefully

3. **Basic Structural Analysis Tests**
   - Use a small sample project with:
     - correct layout
     - intentionally missing required files
   - Verify:
     - structural violations are detected correctly
     - scores reflect the missing pieces

4. **Reporting Engine Tests**
   - With known input state:
     - JSON report matches a golden `MGFTS_REPORT.json`
     - Markdown report matches a golden `MGFTS_REPORT.md`
   - Ensure:
     - required sections exist
     - no broken formatting

5. **Negative / Error Handling Tests**
   - When a tool fails:
     - engine records failure
     - report still builds
   - When manifest is invalid:
     - a clear error is produced
     - test fails with readable diagnostics

---

## 3. Test Layout

The agent SHOULD propose:

```
/alm/tests/
  test_tool_manifest.py
  test_tool_registry.py
  test_reporting_engine.py
  /fixtures/
    /projects/
      minimal_valid_project/
      missing_templates_project/
    mgfts_report_expected.json
    mgfts_report_expected.md
```

Exact structure may vary but MUST be organized and discoverable.

---

## 4. Testing Framework

Python testing is recommended (e.g. `pytest`).

The agent MUST ensure:
- Tests are deterministic.
- No network calls.
- No file system writes outside a temp/fixtures structure.

---

## 5. Deliverables for Agent

The agent SHOULD:

1. Create `alm/tests/TEST_PLAN.md`
   - High-level description of the above areas.

2. Optionally create test skeleton files:
   - `alm/tests/test_tool_manifest.py`
   - `alm/tests/test_tool_registry.py`
   - `alm/tests/test_reporting_engine.py`
   - with docstrings and TODOs.

The agent MUST NOT:
- Implement complete test logic unless explicitly instructed in a later phase.
- Modify existing production code.

---

**Version:** 1.0
**Status:** Specification
**Last Updated:** 2025-01-15
