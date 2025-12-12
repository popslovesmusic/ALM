# Global File Template System (GFTS) Specification

**Version:** 1.0.0
**Status:** Stable
**Date:** 2025-01-15
**Layer:** Foundation (Layers 1-2)

---

## Executive Summary

The **Global File Template System (GFTS)** is a project scaffolding and governance framework that provides standardized templates, directory structures, and configuration patterns for software projects. GFTS ensures consistency, maintainability, and compliance across projects through template-based file generation and structural validation.

**Meta-GFTS (MGFTS)** extends GFTS with 7 layers of governance, enabling projects to achieve not just structural consistency, but philosophical coherence, formal verification, and ontological grounding.

---

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [GFTS vs MGFTS](#gfts-vs-mgfts)
4. [Layer 1: Structural Templates](#layer-1-structural-templates)
5. [Layer 2: Governance](#layer-2-governance)
6. [Template System](#template-system)
7. [Project Scaffolding](#project-scaffolding)
8. [Validation and Compliance](#validation-and-compliance)
9. [Tool Integration](#tool-integration)
10. [Migration Guide](#migration-guide)
11. [Best Practices](#best-practices)
12. [References](#references)

---

## Overview

### What is GFTS?

GFTS is a **project template system** that provides:

1. **Standardized Templates**: Pre-built file templates for common project artifacts
2. **Directory Structure**: Consistent project organization
3. **Configuration Management**: Unified configuration patterns
4. **Governance Files**: Documentation standards and compliance rules
5. **Scaffolding Tools**: Automated project setup scripts
6. **Validation Framework**: Compliance checking and reporting

### What is MGFTS?

MGFTS (Meta-GFTS) is a **7-layer governance framework** built on GFTS that adds:

1. **Meta-Governance (Layer 3)**: Templates for templates, schemas for schemas
2. **Transcendental Governance (Layer 4)**: Constitutional axioms and paradigm protocols
3. **Ecological Intelligence (Layer 5)**: Pattern recognition and emergent wisdom
4. **Formal Verification (Layer 6)**: Mathematical proofs of correctness
5. **Ontological Foundation (Layer 7)**: Existence criteria and truth semantics

### Why GFTS/MGFTS?

**Problems Solved:**
- ❌ Inconsistent project structures across teams
- ❌ Reinventing boilerplate for every project
- ❌ Lack of compliance checking
- ❌ Knowledge loss during project evolution
- ❌ No systematic approach to governance

**Benefits:**
- ✅ Consistent project structure
- ✅ Rapid project bootstrapping
- ✅ Built-in compliance validation
- ✅ Knowledge preservation protocols
- ✅ Scalable governance from simple to enterprise

---

## Core Concepts

### 1. Template

A **template** is a file with placeholder variables that can be substituted to generate actual project files.

**Example:**
```python
"""{{MODULE_DESCRIPTION}}

Author: {{AUTHOR}}
Version: {{VERSION}}
"""

class {{CLASS_NAME}}:
    def __init__(self):
        self.{{ATTRIBUTE}} = {{DEFAULT_VALUE}}
```

**Substitution:**
```json
{
  "MODULE_DESCRIPTION": "User authentication module",
  "AUTHOR": "Jane Doe",
  "VERSION": "1.0.0",
  "CLASS_NAME": "Authenticator",
  "ATTRIBUTE": "token",
  "DEFAULT_VALUE": "None"
}
```

**Result:**
```python
"""User authentication module

Author: Jane Doe
Version: 1.0.0
"""

class Authenticator:
    def __init__(self):
        self.token = None
```

### 2. Project Structure

A **project structure** is a standardized directory layout:

```
/project_root/
  /src/               # Source code
  /tests/             # Test suites
  /docs/              # Documentation
  /config/            # Configuration files
  /scripts/           # Build and utility scripts
  /mgfts/             # MGFTS governance files
    /templates/       # Project-specific templates
    /meta_schemas/    # Validation schemas
    /config/          # MGFTS configuration
  README.md           # Project overview
  CHANGELOG.md        # Version history
  LICENSE             # License file
```

### 3. Governance File

A **governance file** is a document that defines rules, standards, or protocols:

- `AGENTS.md`: Agent behavior rules
- `COMPLIANCE_CHARTER.md`: Universal compliance standards
- `PRESERVATION_PROTOCOL.md`: Knowledge preservation rules
- `GLOBAL_CONCEPT_VAULT.json5`: Concept registry

### 4. Scaffolding

**Scaffolding** is the automated process of creating a new project from templates:

```bash
python scripts/create_new_project.py my-project --layers 1,2
```

This creates the entire project structure with all necessary files.

### 5. Validation

**Validation** is checking that a project complies with MGFTS requirements:

```bash
python scripts/validate_project.py /path/to/project
```

This reports violations and compliance scores.

---

## GFTS vs MGFTS

| Aspect | GFTS | MGFTS |
|--------|------|-------|
| **Scope** | Structural + Basic Governance | 7-layer full governance |
| **Layers** | 1-2 | 1-7 |
| **Complexity** | Simple, lightweight | Comprehensive, enterprise-grade |
| **Use Case** | Small to medium projects | Large, critical, long-term projects |
| **Learning Curve** | Low | Medium to High |
| **Features** | Templates, structure, basic compliance | + Meta-governance, axioms, formal verification, ontology |

**When to use GFTS:**
- Small projects (< 10k LOC)
- Short-term projects (< 6 months)
- Solo or small team
- No critical compliance requirements

**When to use MGFTS:**
- Large projects (> 10k LOC)
- Multi-year projects
- Multiple teams
- Critical compliance (safety, security, regulatory)
- Need for formal verification or ontological grounding

---

## Layer 1: Structural Templates

### Purpose

Layer 1 provides **structural consistency** through:
- Standardized directory layout
- File naming conventions
- Template-based file generation

### Directory Structure

**Required Directories:**
```
/src/          # Source code
/tests/        # Test suites
/docs/         # Documentation
/mgfts/        # Governance files
```

**Optional Directories:**
```
/config/       # Configuration files
/scripts/      # Build/utility scripts
/tools/        # Development tools
/data/         # Data files (if applicable)
/archive/      # Deprecated content
```

### Naming Conventions

**Python Projects:**
- Modules: `snake_case.py`
- Classes: `PascalCase` (in code, not filename)
- Tests: `test_module_name.py`
- Config: `config.json5` or `CONFIG.yaml`

**JavaScript Projects:**
- Modules: `camelCase.js` or `kebab-case.js`
- Classes: `PascalCase`
- Tests: `module.test.js` or `module.spec.js`
- Config: `config.json5`

**Documentation:**
- Governance: `UPPER_CASE.md` (e.g., `AGENTS.md`)
- Guides: `Title_Case.md` (e.g., `User_Guide.md`)
- API docs: `lowercase.md` (e.g., `api.md`)

### Available Templates

1. **Python Module** (`python_module.py.template`)
2. **Python Test** (`python_test.py.template`)
3. **JavaScript Module** (`javascript_module.js.template`)
4. **Configuration** (`config.json5.template`)
5. **Documentation** (`documentation.md.template`)
6. **API Specification** (`api_spec.yaml.template`)
7. **JSON Schema** (`json_schema.json5.template`)
8. **README** (`README.md.template`)
9. **CHANGELOG** (`CHANGELOG.md.template`)
10. **Domain Class** (`domain_class.py.template`)

### Template Usage

**From Command Line:**
```bash
# Using scaffolding script (creates whole project)
python scripts/create_new_project.py my-project

# Manual template usage (single file)
cat mgfts/templates/python_module.py.template | \
  sed 's/{{MODULE_NAME}}/my_module/g' | \
  sed 's/{{AUTHOR}}/Jane Doe/g' > src/my_module.py
```

**From Code:**
```python
from pathlib import Path

template = Path("mgfts/templates/python_module.py.template").read_text()
substitutions = {
    "MODULE_NAME": "my_module",
    "AUTHOR": "Jane Doe",
    "VERSION": "1.0.0",
}

for key, value in substitutions.items():
    template = template.replace(f"{{{{{key}}}}}", value)

Path("src/my_module.py").write_text(template)
```

---

## Layer 2: Governance

### Purpose

Layer 2 provides **governance and compliance** through:
- Agent behavior rules
- Compliance standards
- Preservation protocols
- Concept management

### Governance Files

#### 1. AGENTS.md

**Purpose**: Define how AI agents should behave when working on the project.

**Key Sections:**
- Core Principles (Aletheia, GVP, Constitutional Compliance)
- Agent Modes (Strict, Guided, Exploratory, Emergency)
- Behavioral Rules (Read Before Write, Template Compliance, etc.)
- Decision Framework

**Example Rule:**
```markdown
### Rule 1: Read Before Write
Agents MUST read and understand existing files before modification.
This prevents destruction of implicit knowledge and maintains coherence.
```

#### 2. COMPLIANCE_CHARTER.md

**Purpose**: Define universal compliance standards across all layers.

**Key Sections:**
- Layer Compliance Requirements (1-7)
- Cross-Cutting Standards (Aletheia, Coherence, Preservation)
- Validation and Enforcement
- Exemptions and Exceptions

**Example Standard:**
```markdown
### Aletheia Compliance
Concealment Score = 0.3·(1-doc) + 0.3·(complexity/max) + 0.2·dead + 0.2·implicit
Target: C < 0.3
```

#### 3. PRESERVATION_PROTOCOL.md

**Purpose**: Rules for modifying existing content without losing knowledge.

**Key Sections:**
- Protected Content Classifications
- Archival Requirements
- Modification Protocols
- Deletion Protocol

**Example Protocol:**
```markdown
### Before Deleting Code
1. Verify code is not called anywhere
2. Archive to /archive/ with ARCHIVAL_CONTEXT.md
3. Document reason for deletion
4. Update references in documentation
5. Commit with meaningful message
```

#### 4. GLOBAL_CONCEPT_VAULT.json5

**Purpose**: Registry of all domain concepts with definitions.

**Example Entry:**
```json5
{
  id: "CORE-001",
  name: "Aletheia Principle",
  definition: "Cognition evolves by reducing concealment over time",
  mathematical_formulation: "δ∫C(t) dt = 0",
  examples: ["Adding documentation reduces concealment"],
  related_concepts: ["CORE-004: Concealment Functional"]
}
```

### Compliance Metrics

**Layer 1 (Structural):**
- Directory structure compliance: 100%
- File naming compliance: > 95%
- Required files present: 100%

**Layer 2 (Governance):**
- Governance files present: 100%
- Documentation coverage: > 80%
- Concealment score: < 0.3
- Coherence score: > 0.7

---

## Template System

### Template Syntax

GFTS uses double-brace syntax for placeholders:

```
{{VARIABLE_NAME}}
```

### Variable Naming Conventions

- `UPPER_SNAKE_CASE` for all placeholders
- Descriptive names (e.g., `MODULE_DESCRIPTION` not `DESC`)
- Consistent across templates

### Common Variables

**Project-level:**
- `PROJECT_NAME`: Name of the project
- `PROJECT_VERSION`: Semantic version
- `AUTHOR`: Project author/team
- `LICENSE`: License type (e.g., "MIT")
- `CREATED_DATE`: ISO date of creation

**Module-level:**
- `MODULE_NAME`: Module identifier
- `MODULE_DESCRIPTION`: One-line description
- `MODULE_PURPOSE`: Detailed purpose
- `MGFTS_LAYER`: Which MGFTS layer this relates to

**Code-level:**
- `CLASS_NAME`: Class identifier
- `FUNCTION_NAME`: Function identifier
- `ATTRIBUTE_NAME`: Attribute identifier
- `TYPE_NAME`: Type annotation

### Template Inheritance

Templates can reference other templates (meta-templates):

```
# Meta-template: template.template
"""{{MODULE_DESCRIPTION}}

{{TEMPLATE_SPECIFIC_CONTENT}}
"""

# Specific template: python_module.py.template
{{INCLUDE:template.template}}
# Where TEMPLATE_SPECIFIC_CONTENT = "class {{CLASS_NAME}}: ..."
```

---

## Project Scaffolding

### Using create_new_project.py

**Basic Usage:**
```bash
python scripts/create_new_project.py my-project
```

**With Options:**
```bash
python scripts/create_new_project.py my-project \
  --layers 1,2,3 \
  --language python \
  --author "Jane Doe" \
  --license MIT
```

**All Layers:**
```bash
python scripts/create_new_project.py enterprise-app --layers all
```

### What Gets Created

1. **Directory Structure**: All required and optional directories
2. **Governance Files**: Copies from MGFTS installation
3. **Templates**: Project-specific templates directory
4. **Configuration**: `mgfts/config/project.json5`
5. **Documentation**: README.md, CHANGELOG.md
6. **Source Structure**: Language-specific source layout
7. **Git Repository**: Initialized with `.gitignore`
8. **Example Code**: Demonstration files from templates

### Customization

**After scaffolding:**

1. Edit `mgfts/config/project.json5` to configure:
   - Enabled layers
   - Validation thresholds
   - Agent mode
   - Custom paths

2. Modify templates in `mgfts/templates/` for project-specific needs

3. Add project-specific concepts to `GLOBAL_CONCEPT_VAULT.json5`

---

## Validation and Compliance

### Using validate_project.py

**Basic Validation:**
```bash
python scripts/validate_project.py /path/to/project
```

**JSON Report:**
```bash
python scripts/validate_project.py . --report json --output report.json
```

**Specific Layers:**
```bash
python scripts/validate_project.py . --layers 1,2,3
```

**Severity Threshold:**
```bash
python scripts/validate_project.py . --severity critical
```

### Violation Severity Levels

1. **CRITICAL**: Blocks commit/merge (e.g., missing governance files)
2. **HIGH**: Requires immediate attention (e.g., test failures)
3. **MEDIUM**: Should be fixed soon (e.g., style violations)
4. **LOW**: Technical debt (e.g., minor naming issues)

### Validation Report

**Text Format:**
```
===============================================================
MGFTS Project Validation Report
===============================================================
Project: /path/to/project
Status: ✅ PASSED
Overall Score: 0.92

Layer Scores:
  Layer 1: 0.95
  Layer 2: 0.90

Violation Counts:
  Critical: 0
  High: 0
  Medium: 2
  Low: 5
===============================================================
```

**JSON Format:**
```json
{
  "project": "/path/to/project",
  "passed": true,
  "scores": {
    "overall": 0.92,
    "layer_1": 0.95,
    "layer_2": 0.90
  },
  "violations": [],
  "warnings": [
    {
      "code": "STRUCT-004",
      "message": "CHANGELOG.md missing",
      "severity": "low",
      "suggestion": "Create CHANGELOG.md from template"
    }
  ]
}
```

---

## Tool Integration

### Constitutional Engine

The **Constitutional Engine** (`alm/mod/governance_core.py`) provides deep validation:

```bash
python alm/mod/governance_core.py --project . --output report.json
```

This generates:
- **JSON Report**: Machine-readable violations and scores
- **Markdown Report**: Human-readable analysis with Aletheia commentary

### CI/CD Integration

**Pre-commit Hook:**
```bash
#!/bin/bash
# .git/hooks/pre-commit

python scripts/validate_project.py . --severity high
if [ $? -ne 0 ]; then
  echo "MGFTS validation failed. Fix violations before committing."
  exit 1
fi
```

**GitHub Actions:**
```yaml
name: MGFTS Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate MGFTS Compliance
        run: python scripts/validate_project.py . --severity high
```

### IDE Integration

**VS Code Settings** (`.vscode/tasks.json`):
```json
{
  "tasks": [
    {
      "label": "Validate MGFTS Compliance",
      "type": "shell",
      "command": "python scripts/validate_project.py .",
      "problemMatcher": []
    }
  ]
}
```

---

## Migration Guide

### Migrating Existing Project to GFTS

1. **Create MGFTS directory:**
   ```bash
   mkdir -p mgfts/templates mgfts/meta_schemas mgfts/config
   ```

2. **Copy governance files:**
   ```bash
   cp /path/to/mgfts/AGENTS.md mgfts/
   cp /path/to/mgfts/COMPLIANCE_CHARTER.md mgfts/
   cp /path/to/mgfts/PRESERVATION_PROTOCOL.md mgfts/
   cp /path/to/mgfts/GLOBAL_CONCEPT_VAULT.json5 mgfts/
   ```

3. **Create configuration:**
   ```bash
   cat > mgfts/config/project.json5 << 'EOF'
   {
     "version": "1.0.0",
     "project": {"name": "my-project"},
     "mgfts": {"enabled": true, "layers": [1, 2]}
   }
   EOF
   ```

4. **Validate:**
   ```bash
   python scripts/validate_project.py .
   ```

5. **Fix violations** reported by validator

6. **Commit:**
   ```bash
   git add mgfts/
   git commit -m "Add MGFTS governance"
   ```

---

## Best Practices

### 1. Start Small

Begin with Layers 1-2, add higher layers as needed.

### 2. Use Templates Consistently

Always generate new files from templates rather than copying/pasting.

### 3. Validate Often

Run validation before every commit (use pre-commit hook).

### 4. Document Concepts

Add new domain concepts to `GLOBAL_CONCEPT_VAULT.json5` immediately.

### 5. Follow Preservation Protocol

Never delete code without archiving and documenting.

### 6. Customize Templates

Adapt templates to project needs, but maintain core structure.

### 7. Automate Compliance

Integrate validation into CI/CD pipeline.

### 8. Review Governance Regularly

Quarterly review of governance files and compliance standards.

---

## References

### Specifications

- **MGFTS_BUILD_INSTRUCTIONS.md**: Complete 7-layer architecture
- **CONSTITUTIONAL_ENGINE_ARCHITECTURE.v0.1.md**: Validation engine spec

### Governance Files

- **AGENTS.md**: Agent behavior rules
- **COMPLIANCE_CHARTER.md**: Compliance standards
- **PRESERVATION_PROTOCOL.md**: Preservation rules
- **GLOBAL_CONCEPT_VAULT.json5**: Concept registry

### Tools

- **create_new_project.py**: Project scaffolding script
- **validate_project.py**: Compliance validation script
- **governance_core.py**: Constitutional Engine (deep validation)

---

**Version:** 1.0.0
**Last Updated:** 2025-01-15
**Maintained By:** ALM MGFTS Team
