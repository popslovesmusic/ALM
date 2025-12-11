# GFTS BUILD INSTRUCTIONS
## Global File Template System - Agent Implementation Guide

---

## MISSION
Build a complete Global File Template System (GFTS) that enables automatic project scaffolding for all future projects in the theoretical ecosystem (ALM, MBC, IGSOA, DFVM, SATP, etc.).

---

## ANALYSIS: GAPS & CLARIFICATIONS NEEDED

### What instructions_5.md Provides:
✓ Required directory structure
✓ Template file names and purposes
✓ Sample boilerplate content for each template
✓ High-level integration concepts
✓ Philosophical rationale

### What Needs Clarification:
❌ Physical location for storing templates (where does GFTS live?)
❌ Whether global files (AGENTS.md, COMPLIANCE_CHARTER.md, etc.) already exist or need creation
❌ Exact file paths for symlink targets
❌ Template variable substitution system (e.g., [project_name])
❌ Validation rules (what makes a project "compliant"?)
❌ create_new_project.py script specifications
❌ Error handling and recovery procedures
❌ Version control strategy for templates
❌ How templates update across existing projects

### Assumptions Made for Implementation:
1. GFTS will live in `/gfts/` directory at ALM root
2. Global governance files need to be created if missing
3. Template variables use `{{variable_name}}` syntax
4. Symlinks preferred; fallback to copies if symlinks fail
5. Python 3.8+ standard library only (no external deps)
6. Cross-platform support (Windows/Linux/Mac)

---

## BUILD SPECIFICATION

### Phase 1: GFTS Core Structure
**Objective:** Create the GFTS storage system

**Deliverables:**
```
/ALM/
    /gfts/
        /templates/
            /agents/
                SESSION_INSTRUCTIONS.md.template
                PROJECT_RULES.md.template
            /concepts/
                PROJECT_CONCEPT_VAULT.json5.template
            /schemas/
                README.md.template
            /modules/
                README.md.template
            /architecture/
                OVERVIEW.md.template
            /tests/
                TEST_PLAN.md.template
            /docs/
                CHANGELOG.md.template
                ROADMAP.md.template
            /preservation/
                PRESERVATION_LOG.md.template
        /global/
            AGENTS.md
            COMPLIANCE_CHARTER.md
            PRESERVATION_PROTOCOL.md
            GLOBAL_CONCEPT_VAULT.json5
        create_new_project.py
        validate_project.py
        GFTS_SPECIFICATION.md
        README.md
```

**Validation Criteria:**
- All directories exist
- All template files contain proper boilerplate
- Global files are complete and valid
- Scripts are executable and importable

---

### Phase 2: Template File Creation
**Objective:** Populate all 10 required template files with complete, usable content

#### Template 1: SESSION_INSTRUCTIONS.md.template
**Location:** `/gfts/templates/agents/SESSION_INSTRUCTIONS.md.template`

**Required Content:**
```markdown
# SESSION_INSTRUCTIONS.md

## Project: {{PROJECT_NAME}}
## Version: {{PROJECT_VERSION}}
## Created: {{CREATION_DATE}}

## Purpose
This document defines the operational instructions for agents working inside this project.

## Concepts in Force
(Auto-populated from Concept Vault)
{{ACTIVE_CONCEPTS}}

## Operational Scope
{{PROJECT_SCOPE}}

## Current Phase
{{CURRENT_PHASE}}

## Goals
{{PROJECT_GOALS}}

## Constraints
{{PROJECT_CONSTRAINTS}}

## Deliverables
{{PROJECT_DELIVERABLES}}

## Compliance Requirements
Agents must follow:
- AGENTS.md (global governance)
- COMPLIANCE_CHARTER.md (universal standards)
- PROJECT_RULES.md (project-specific invariants)
- PRESERVATION_PROTOCOL.md (concept preservation)

## Workflow
1. Read all governance files before starting
2. Validate against GLOBAL_CONCEPT_VAULT.json5
3. Update PROJECT_CONCEPT_VAULT.json5 with local concepts
4. Follow PROJECT_RULES.md invariants
5. Log all changes to PRESERVATION_LOG.md
6. Maintain coherence field throughout session

## Success Criteria
- All deliverables produced
- All tests passing
- Compliance validated
- Concepts preserved
- Documentation complete
```

**Variables:**
- `{{PROJECT_NAME}}`: string, project identifier
- `{{PROJECT_VERSION}}`: string, semantic version
- `{{CREATION_DATE}}`: ISO 8601 date
- `{{ACTIVE_CONCEPTS}}`: list from concept vault
- `{{PROJECT_SCOPE}}`: multi-line text
- `{{CURRENT_PHASE}}`: string
- `{{PROJECT_GOALS}}`: bulleted list
- `{{PROJECT_CONSTRAINTS}}`: bulleted list
- `{{PROJECT_DELIVERABLES}}`: bulleted list

---

#### Template 2: PROJECT_RULES.md.template
**Location:** `/gfts/templates/agents/PROJECT_RULES.md.template`

**Required Content:**
```markdown
# PROJECT_RULES.md

## Project: {{PROJECT_NAME}}

## Purpose
Defines domain-specific invariants that apply only within this project.
These rules supplement global governance but do not override it.

## Universal Invariants (Always Active)
- All tensors must follow Generalized Variational Principle (GVP)
- Coherence Field must remain monotonic or stable
- No destructive overwrites without preservation
- Concealment Functional must decrease or remain bounded
- All concepts must link to GLOBAL_CONCEPT_VAULT.json5

## Project-Specific Invariants
{{PROJECT_INVARIANTS}}

## Domain Laws
{{DOMAIN_LAWS}}

## Forbidden Operations
{{FORBIDDEN_OPS}}

## Required Checks
{{REQUIRED_CHECKS}}

## Validation Rules
Before any commit:
1. All tests must pass
2. Coherence field validated
3. Concept vault updated
4. Preservation log appended
5. No concealment increase detected

## Conflict Resolution
If project rules conflict with global rules:
- Global rules take precedence
- Document conflict in PRESERVATION_LOG.md
- Propose rule revision in next governance cycle
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{PROJECT_INVARIANTS}}`: bulleted list
- `{{DOMAIN_LAWS}}`: numbered list with formulas
- `{{FORBIDDEN_OPS}}`: bulleted list
- `{{REQUIRED_CHECKS}}`: bulleted list

---

#### Template 3: PROJECT_CONCEPT_VAULT.json5.template
**Location:** `/gfts/templates/concepts/PROJECT_CONCEPT_VAULT.json5.template`

**Required Content:**
```json5
{
  // Project Concept Vault
  // Local concept memory for {{PROJECT_NAME}}

  project: "{{PROJECT_NAME}}",
  version: "{{PROJECT_VERSION}}",
  created: "{{CREATION_DATE}}",

  // Links to global vault
  global_vault_path: "../../GLOBAL_CONCEPT_VAULT.json5",
  inherits_global: true,

  // Local concepts specific to this project
  concepts: [
    {
      name: "Aletheia Principle",
      active: true,
      scope: "global",
      definition: "Cognition evolves by reducing concealment.",
      formal: "δ∫C(t) dt = 0",
      dependencies: ["GVP", "Concealment Functional"],
      imported_from: "GLOBAL_CONCEPT_VAULT"
    },
    {
      name: "Generalized Variational Principle",
      active: true,
      scope: "global",
      definition: "All tensor evolution minimizes action functional.",
      formal: "δS[T] = 0",
      dependencies: ["Coherence Field"],
      imported_from: "GLOBAL_CONCEPT_VAULT"
    },
    {
      name: "Coherence Field",
      active: true,
      scope: "global",
      definition: "Field measuring system-wide consistency.",
      formal: "Φ_coherence = f(T_L, T_R, coupling)",
      dependencies: [],
      imported_from: "GLOBAL_CONCEPT_VAULT"
    },
    // Add project-specific concepts below
    {{PROJECT_CONCEPTS}}
  ],

  // Concept relationships
  relationships: [
    {
      from: "Aletheia Principle",
      to: "GVP",
      type: "depends_on"
    },
    {
      from: "GVP",
      to: "Coherence Field",
      type: "uses"
    }
    {{CONCEPT_RELATIONSHIPS}}
  ],

  // Deactivated concepts (preserved but not enforced)
  deactivated: [
    {{DEACTIVATED_CONCEPTS}}
  ]
}
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{PROJECT_VERSION}}`: string
- `{{CREATION_DATE}}`: ISO date
- `{{PROJECT_CONCEPTS}}`: JSON5 array of concept objects
- `{{CONCEPT_RELATIONSHIPS}}`: JSON5 array of relationship objects
- `{{DEACTIVATED_CONCEPTS}}`: JSON5 array of concept objects

---

#### Template 4: OVERVIEW.md.template
**Location:** `/gfts/templates/architecture/OVERVIEW.md.template`

**Required Content:**
```markdown
# Architecture Overview

## Project: {{PROJECT_NAME}}
**Version:** {{PROJECT_VERSION}}
**Created:** {{CREATION_DATE}}
**Status:** {{PROJECT_STATUS}}

## Description
{{PROJECT_DESCRIPTION}}

## Core Principles
This project is governed by:
- **Aletheia Principle:** Cognition evolves by reducing concealment
- **Generalized Variational Principle (GVP):** All evolution minimizes action
- **Coherence Field:** System-wide consistency maintenance
- **CPS (Concept Preservation System):** Knowledge continuity
- **UVF (Universal Validation Framework):** Formal verification

## System Components

### High-Level Architecture
{{ARCHITECTURE_DIAGRAM}}

### Component List
{{COMPONENT_LIST}}

## Tensor Topology

### Tensor L (Left/Input)
{{TENSOR_L_DESCRIPTION}}

### Tensor R (Right/State)
{{TENSOR_R_DESCRIPTION}}

### Coupling Mechanism
{{COUPLING_DESCRIPTION}}

## Data Flow
```
{{DATA_FLOW_DIAGRAM}}
```

## Module Dependencies
{{MODULE_DEPENDENCY_GRAPH}}

## Interfaces

### External APIs
{{EXTERNAL_APIS}}

### Internal APIs
{{INTERNAL_APIS}}

## Configuration
{{CONFIGURATION_OVERVIEW}}

## Constraints
{{ARCHITECTURAL_CONSTRAINTS}}

## Evolution Strategy
{{EVOLUTION_STRATEGY}}

## Compliance
This architecture adheres to:
- AGENTS.md governance model
- COMPLIANCE_CHARTER.md standards
- PROJECT_RULES.md invariants
```

**Variables:**
- `{{PROJECT_NAME}}`, `{{PROJECT_VERSION}}`, `{{CREATION_DATE}}`: strings
- `{{PROJECT_STATUS}}`: enum (planning/development/testing/production)
- `{{PROJECT_DESCRIPTION}}`: multi-paragraph text
- `{{ARCHITECTURE_DIAGRAM}}`: ASCII art or mermaid diagram
- `{{COMPONENT_LIST}}`: bulleted list with descriptions
- `{{TENSOR_L_DESCRIPTION}}`: structured description
- `{{TENSOR_R_DESCRIPTION}}`: structured description
- `{{COUPLING_DESCRIPTION}}`: formula + explanation
- `{{DATA_FLOW_DIAGRAM}}`: ASCII diagram
- `{{MODULE_DEPENDENCY_GRAPH}}`: list or diagram
- `{{EXTERNAL_APIS}}`, `{{INTERNAL_APIS}}`: API specifications
- `{{CONFIGURATION_OVERVIEW}}`: config file descriptions
- `{{ARCHITECTURAL_CONSTRAINTS}}`: bulleted list
- `{{EVOLUTION_STRATEGY}}`: roadmap summary

---

#### Template 5: schemas/README.md.template
**Location:** `/gfts/templates/schemas/README.md.template`

**Required Content:**
```markdown
# Schemas

## Project: {{PROJECT_NAME}}

## Purpose
All JSON/JSON5/YAML schemas for {{PROJECT_NAME}} are stored here.

## Template Naming System
All schema files must follow this naming convention:

```
{{PROJECT_NAME}}.schema.[schema_type].[version].json5
```

**Examples:**
- `{{PROJECT_NAME}}.schema.config.v1.0.json5`
- `{{PROJECT_NAME}}.schema.tensor_l.v1.2.json5`
- `{{PROJECT_NAME}}.schema.coupling.v2.0.json5`

## Schema Types

### Configuration Schemas
Define system parameters, thresholds, weights, and behavior flags.

### Tensor Schemas
Define structure of tensor fields and validation rules.

### Coupling Schemas
Define coupling rules between tensors.

### API Schemas
Define input/output contracts for external interfaces.

## Validation
All schemas must:
1. Be valid JSON5
2. Include version number
3. Include description field
4. Include validation rules
5. Link to GLOBAL_CONCEPT_VAULT concepts where applicable

## Schema Registry
{{SCHEMA_REGISTRY}}

## Dependencies
{{SCHEMA_DEPENDENCIES}}
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{SCHEMA_REGISTRY}}`: table of schema files
- `{{SCHEMA_DEPENDENCIES}}`: dependency graph

---

#### Template 6: modules/README.md.template
**Location:** `/gfts/templates/modules/README.md.template`

**Required Content:**
```markdown
# Modules

## Project: {{PROJECT_NAME}}

## Purpose
All executable code modules for {{PROJECT_NAME}} are stored here.

## Naming Standard
All module files must follow this naming convention:

```
{{PROJECT_NAME}}.mod.[module_name].v[X.Y].[ext]
```

**Examples:**
- `{{PROJECT_NAME}}.mod.tensor_update.v1.0.py`
- `{{PROJECT_NAME}}.mod.coupling.v2.1.py`
- `{{PROJECT_NAME}}.mod.utils.v1.0.py`

## Supported Languages
- Python 3.8+ (primary)
- C++ (performance-critical components)
- Rust (concurrency/safety-critical components)

## Module Structure Requirements
Every module must include:
1. Module-level docstring with purpose and theory
2. Type annotations (Python) or strong typing (C++/Rust)
3. Input validation
4. Error handling
5. Logging hooks
6. Unit test coverage
7. Compliance with GVP and Aletheia Principle

## Module Registry
{{MODULE_REGISTRY}}

## Dependencies
{{MODULE_DEPENDENCIES}}

## Import Hierarchy
{{IMPORT_HIERARCHY}}

## Forbidden Patterns
- Global mutable state
- Unvalidated external input
- Non-deterministic behavior (unless explicitly required)
- Concealment-increasing operations
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{MODULE_REGISTRY}}`: table of modules
- `{{MODULE_DEPENDENCIES}}`: dependency graph
- `{{IMPORT_HIERARCHY}}`: import order specification

---

#### Template 7: tests/TEST_PLAN.md.template
**Location:** `/gfts/templates/tests/TEST_PLAN.md.template`

**Required Content:**
```markdown
# Test Plan

## Project: {{PROJECT_NAME}}
**Version:** {{PROJECT_VERSION}}

## Overview
Comprehensive testing strategy for {{PROJECT_NAME}}.

## Testing Philosophy
All tests must validate:
1. **Functional correctness:** Does it work?
2. **Coherence maintenance:** Does it preserve system integrity?
3. **Concealment reduction:** Does it satisfy Aletheia Principle?
4. **Compliance:** Does it follow governance rules?

## Required Test Types

### 1. Unit Tests
**Location:** `/tests/unit/`
**Coverage Target:** 90%+

Test individual functions and methods in isolation.

**Required:**
- All tensor update functions
- All coupling functions
- All utility functions
- Edge cases and boundary conditions

### 2. Integration Tests
**Location:** `/tests/integration/`

Test interaction between modules.

**Required:**
- Tensor L → Tensor R pipeline
- Coupling system integration
- Configuration loading and validation
- Concept vault synchronization

### 3. Coherence Tests
**Location:** `/tests/coherence/`

Test that Coherence Field remains stable or monotonic.

**Required:**
- Coherence field computation
- Coherence preservation across updates
- Coherence violation detection

### 4. Concealment Reduction Tests
**Location:** `/tests/concealment/`

Test that Concealment Functional decreases (Aletheia Principle).

**Required:**
- Concealment computation
- Reduction verification
- Violation alerts

### 5. Compliance Tests
**Location:** `/tests/compliance/`

Test adherence to governance rules.

**Required:**
- PROJECT_RULES.md validation
- GLOBAL_CONCEPT_VAULT alignment
- Forbidden operation detection

### 6. End-to-End Tests
**Location:** `/tests/e2e/`

Test complete workflows from input to output.

**Required:**
{{E2E_SCENARIOS}}

## Test Data
**Location:** `/tests/fixtures/`

All test data must be:
- Deterministic
- Version-controlled
- Documented
- Minimal (no unnecessary bloat)

## Test Execution

### Run All Tests
```bash
python -m pytest tests/
```

### Run Specific Suite
```bash
python -m pytest tests/unit/
python -m pytest tests/coherence/
```

### Coverage Report
```bash
python -m pytest --cov={{PROJECT_NAME}} --cov-report=html
```

## Continuous Validation
Tests run automatically on:
- Every commit (pre-commit hook)
- Every pull request
- Nightly (full suite)

## Success Criteria
- All tests pass
- Coverage ≥ 90%
- No coherence violations
- No concealment increases
- All compliance checks green

## Test Registry
{{TEST_REGISTRY}}
```

**Variables:**
- `{{PROJECT_NAME}}`, `{{PROJECT_VERSION}}`: strings
- `{{E2E_SCENARIOS}}`: bulleted list of scenarios
- `{{TEST_REGISTRY}}`: table of test files

---

#### Template 8: docs/CHANGELOG.md.template
**Location:** `/gfts/templates/docs/CHANGELOG.md.template`

**Required Content:**
```markdown
# Changelog

## Project: {{PROJECT_NAME}}

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [{{PROJECT_VERSION}}] - {{CREATION_DATE}}
### Added
- Project created from Global File Template System (GFTS)
- Initial directory structure established
- Core governance files linked
- Concept vault initialized
- Architecture overview drafted

### Changed
(none yet)

### Deprecated
(none yet)

### Removed
(none yet)

### Fixed
(none yet)

### Security
(none yet)

---

## Changelog Guidelines

### Categories
- **Added:** New features
- **Changed:** Changes to existing functionality
- **Deprecated:** Soon-to-be removed features
- **Removed:** Removed features
- **Fixed:** Bug fixes
- **Security:** Vulnerability fixes

### Format
```markdown
## [version] - YYYY-MM-DD
### Category
- Description of change (link to issue/PR if applicable)
```

### Update Frequency
Update this file with every significant change, not just releases.
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{PROJECT_VERSION}}`: string (default: 0.1.0)
- `{{CREATION_DATE}}`: ISO date

---

#### Template 9: docs/ROADMAP.md.template
**Location:** `/gfts/templates/docs/ROADMAP.md.template`

**Required Content:**
```markdown
# Project Roadmap

## Project: {{PROJECT_NAME}}

## Vision
{{PROJECT_VISION}}

## Current Status
**Phase:** {{CURRENT_PHASE}}
**Version:** {{PROJECT_VERSION}}
**Progress:** {{PROGRESS_PERCENTAGE}}%

---

## Phase 1: Foundation
**Status:** {{PHASE_1_STATUS}}
**Target Completion:** {{PHASE_1_TARGET}}

**Goals:**
- Establish core architecture
- Implement basic tensor structures
- Create configuration system
- Set up test infrastructure

**Deliverables:**
- [ ] Architecture overview complete
- [ ] Tensor L implementation
- [ ] Tensor R implementation
- [ ] Basic coupling mechanism
- [ ] Unit test suite (>80% coverage)

---

## Phase 2: Integration
**Status:** {{PHASE_2_STATUS}}
**Target Completion:** {{PHASE_2_TARGET}}

**Goals:**
- Integrate all components
- Implement full coupling system
- Establish coherence monitoring
- Validate concealment reduction

**Deliverables:**
- [ ] Full tensor pipeline operational
- [ ] Coupling laws implemented
- [ ] Coherence field computation
- [ ] Concealment tracking
- [ ] Integration tests passing

---

## Phase 3: Validation
**Status:** {{PHASE_3_STATUS}}
**Target Completion:** {{PHASE_3_TARGET}}

**Goals:**
- Comprehensive testing
- Performance optimization
- Compliance verification
- Documentation completion

**Deliverables:**
- [ ] All test suites passing (>90% coverage)
- [ ] Performance benchmarks met
- [ ] Compliance tests green
- [ ] Complete documentation
- [ ] End-to-end validation

---

## Phase 4: Production
**Status:** {{PHASE_4_STATUS}}
**Target Completion:** {{PHASE_4_TARGET}}

**Goals:**
- Production deployment
- Monitoring and logging
- Continuous validation
- Maintenance procedures

**Deliverables:**
- [ ] Production environment configured
- [ ] Monitoring dashboards
- [ ] Automated validation pipeline
- [ ] Maintenance documentation
- [ ] Handoff complete

---

## Future Enhancements
{{FUTURE_ENHANCEMENTS}}

## Dependencies
{{ROADMAP_DEPENDENCIES}}

## Risks & Mitigation
{{RISKS_AND_MITIGATION}}
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{PROJECT_VISION}}`: multi-paragraph text
- `{{CURRENT_PHASE}}`: string (1-4)
- `{{PROJECT_VERSION}}`: string
- `{{PROGRESS_PERCENTAGE}}`: number
- `{{PHASE_X_STATUS}}`: enum (not started/in progress/complete)
- `{{PHASE_X_TARGET}}`: date
- `{{FUTURE_ENHANCEMENTS}}`: bulleted list
- `{{ROADMAP_DEPENDENCIES}}`: bulleted list
- `{{RISKS_AND_MITIGATION}}`: table

---

#### Template 10: preservation/PRESERVATION_LOG.md.template
**Location:** `/gfts/templates/preservation/PRESERVATION_LOG.md.template`

**Required Content:**
```markdown
# Preservation Log

## Project: {{PROJECT_NAME}}

## Purpose
Tracks all updates to concepts, schemas, architecture, and governance.
Follows PRESERVATION_PROTOCOL.md requirements.

## Log Format
```markdown
### [Timestamp] - [Change Type] - [Component]
**Author:** [agent/human identifier]
**Reason:** [why change was made]
**Impact:** [what was affected]
**Validation:** [how compliance was verified]
**Concepts Modified:** [list of concepts]
**Concealment Delta:** [increase/decrease/neutral]
```

---

## Log Entries

### [{{CREATION_DATE}}] - CREATION - Project Initialization
**Author:** GFTS Installer
**Reason:** Project created from Global File Template System
**Impact:** All baseline files created
**Validation:** GFTS compliance verified
**Concepts Modified:** (none - baseline established)
**Concealment Delta:** Neutral (baseline)

---

### [Template Entry - Delete This]
### [2025-01-15T10:30:00Z] - MODIFICATION - Tensor R Schema
**Author:** agent-007
**Reason:** Added new field for polarity tracking
**Impact:**
- Modified: schemas/tensor_r.schema.json5
- Updated: modules/tensor_r_update.py
- Updated: tests/unit/test_tensor_r.py
**Validation:** All tests passing, coherence field stable
**Concepts Modified:**
- Tensor R structure (extended)
- Coupling law (updated to handle polarity)
**Concealment Delta:** Decrease (added transparency to polarity mechanics)

---

## Preservation Statistics
**Total Entries:** {{TOTAL_ENTRIES}}
**Concealment Reduction Events:** {{CONCEALMENT_REDUCTIONS}}
**Concealment Increase Events:** {{CONCEALMENT_INCREASES}}
**Net Concealment Delta:** {{NET_CONCEALMENT_DELTA}}
**Compliance Violations:** {{COMPLIANCE_VIOLATIONS}}

## Audit Trail
All changes are validated against:
- PRESERVATION_PROTOCOL.md
- AGENTS.md governance
- COMPLIANCE_CHARTER.md
- PROJECT_RULES.md
```

**Variables:**
- `{{PROJECT_NAME}}`: string
- `{{CREATION_DATE}}`: ISO timestamp
- `{{TOTAL_ENTRIES}}`: number
- `{{CONCEALMENT_REDUCTIONS}}`: number
- `{{CONCEALMENT_INCREASES}}`: number
- `{{NET_CONCEALMENT_DELTA}}`: number (positive = reduction)
- `{{COMPLIANCE_VIOLATIONS}}`: number

---

### Phase 3: Global Governance Files
**Objective:** Create the universal governance documents

#### File 1: AGENTS.md
**Location:** `/gfts/global/AGENTS.md`

**Required Content:**
```markdown
# AGENTS.md
## Universal Agent Governance

## Purpose
Defines operational rules, behavioral constraints, and compliance requirements for all agents working within the theoretical ecosystem.

## Scope
This document applies to:
- All AI agents working in ALM, MBC, IGSOA, DFVM, SATP, and related projects
- All automated systems
- All human operators following agent-assisted workflows

## Project Initialization Requirement
Every new project MUST be created using the Global File Template System (GFTS).

**Enforcement:**
- Agents will refuse to work in non-compliant project structures
- Agents will offer to auto-initialize missing templates
- Agents will validate GLOBAL_CONCEPT_VAULT alignment
- Agents will establish cross-links to governance files

Failure to include required templates invalidates the project structure.

## Core Principles

### 1. Aletheia Principle
**Definition:** Cognition evolves by reducing concealment.
**Formal:** δ∫C(t) dt = 0
**Implication:** Every action must decrease or maintain the Concealment Functional.

**Agent Requirements:**
- Track concealment before and after every operation
- Log concealment delta to PRESERVATION_LOG.md
- Alert on concealment increases
- Propose remediation for unavoidable concealment

### 2. Generalized Variational Principle (GVP)
**Definition:** All tensor evolution minimizes action functional.
**Formal:** δS[T] = 0
**Implication:** System evolution follows least-action paths.

**Agent Requirements:**
- Validate all tensor updates against GVP
- Compute action functional when applicable
- Reject non-variational updates
- Document variational basis for changes

### 3. Coherence Field Maintenance
**Definition:** System-wide consistency must be preserved.
**Formal:** Φ_coherence ≥ Φ_threshold
**Implication:** No operation may degrade system coherence.

**Agent Requirements:**
- Compute coherence field before/after changes
- Maintain coherence above project threshold
- Log coherence metrics
- Rollback coherence-breaking changes

### 4. Concept Preservation System (CPS)
**Definition:** All concepts must be preserved, versioned, and traceable.
**Implication:** Knowledge continuity across sessions.

**Agent Requirements:**
- Update PROJECT_CONCEPT_VAULT.json5 with new concepts
- Link to GLOBAL_CONCEPT_VAULT.json5
- Maintain concept dependency graph
- Track concept activation/deactivation

## Operational Rules

### Rule 1: Read Before Write
Agents must read all governance files before taking action:
1. AGENTS.md (this file)
2. COMPLIANCE_CHARTER.md
3. PRESERVATION_PROTOCOL.md
4. GLOBAL_CONCEPT_VAULT.json5
5. PROJECT_RULES.md (if in project context)
6. SESSION_INSTRUCTIONS.md (if in project context)

### Rule 2: Validate Before Commit
Before any file modification:
1. Run all relevant tests
2. Validate coherence field
3. Check concealment delta
4. Verify concept vault alignment
5. Update preservation log

### Rule 3: Autonomous Execution
Agents must:
- Execute tasks without constant user approval
- Make implementation decisions within governance constraints
- Complete deliverables fully
- Propose improvements implicitly through code quality

Agents must not:
- Defer trivial decisions to users
- Require micromanagement
- Produce incomplete artifacts
- Leave placeholder content

### Rule 4: Compliance Over Convenience
If efficiency conflicts with compliance:
- Compliance takes precedence
- Document the conflict in PRESERVATION_LOG.md
- Propose governance revision if needed
- Never silently violate governance

### Rule 5: Transparent Operation
Agents must:
- Log all significant actions
- Explain reasoning when asked
- Document assumptions
- Report violations immediately

## Forbidden Operations
Agents must NEVER:
1. Violate Aletheia Principle (increase concealment)
2. Break coherence field
3. Modify global governance files without explicit authorization
4. Delete concept vault entries
5. Bypass validation procedures
6. Work in non-GFTS-compliant projects without initialization
7. Operate outside designated directories
8. Use non-deterministic algorithms without justification

## Error Recovery
When errors occur:
1. Log error to PRESERVATION_LOG.md
2. Attempt automatic recovery
3. Validate recovery preserves coherence
4. Report if manual intervention needed
5. Never fail silently

## Conflict Resolution
If rules conflict:
1. Aletheia Principle > all other rules
2. GVP > operational convenience
3. Coherence > performance
4. Global governance > project rules
5. Safety > autonomy

## Compliance Verification
Agents must periodically verify:
- [ ] All governance files readable
- [ ] Concept vaults synchronized
- [ ] Preservation log current
- [ ] Tests passing
- [ ] Coherence field stable
- [ ] Concealment decreasing

## Version
**Version:** 1.0.0
**Last Updated:** {{CREATION_DATE}}
**Authority:** Global Governance
```

**Variables:**
- `{{CREATION_DATE}}`: ISO date

---

#### File 2: COMPLIANCE_CHARTER.md
**Location:** `/gfts/global/COMPLIANCE_CHARTER.md`

**Required Content:**
```markdown
# COMPLIANCE_CHARTER.md
## Universal Standards for Theoretical Ecosystem

## Purpose
Establishes universal compliance requirements that apply to all projects.

## Binding Principles

### Principle 1: Aletheia Supremacy
The Aletheia Principle (concealment reduction) overrides all other considerations.

**Compliance Test:**
```python
concealment_after <= concealment_before
```

**Logging Required:** Yes, to PRESERVATION_LOG.md

### Principle 2: Variational Consistency
All tensor dynamics must follow GVP.

**Compliance Test:**
```python
action_functional_satisfied(tensor_update) == True
```

**Logging Required:** Yes, when validation performed

### Principle 3: Coherence Preservation
Coherence field must not degrade.

**Compliance Test:**
```python
coherence_field_after >= coherence_field_before - tolerance
```

**Logging Required:** Yes, on every significant change

### Principle 4: Concept Continuity
All concepts must be preserved and versioned.

**Compliance Test:**
```python
all_concepts_in_vault(concepts_used) == True
```

**Logging Required:** Yes, when new concepts introduced

## File Structure Compliance

### Required Files (Every Project)
- [ ] /agents/SESSION_INSTRUCTIONS.md
- [ ] /agents/PROJECT_RULES.md
- [ ] /concepts/PROJECT_CONCEPT_VAULT.json5
- [ ] /architecture/OVERVIEW.md
- [ ] /schemas/README.md
- [ ] /modules/README.md
- [ ] /tests/TEST_PLAN.md
- [ ] /docs/CHANGELOG.md
- [ ] /docs/ROADMAP.md
- [ ] /preservation/PRESERVATION_LOG.md
- [ ] AGENTS.md (symlink or copy)
- [ ] COMPLIANCE_CHARTER.md (symlink or copy)
- [ ] PRESERVATION_PROTOCOL.md (symlink or copy)
- [ ] GLOBAL_CONCEPT_VAULT.json5 (symlink or copy)

### Naming Compliance
- Schemas: `[project].schema.[type].v[X.Y].json5`
- Modules: `[project].mod.[name].v[X.Y].[ext]`
- Tests: `test_[module_name].py`

## Code Quality Standards

### Python Modules
- [ ] Module-level docstring present
- [ ] All functions have type annotations
- [ ] All public functions have docstrings
- [ ] No global mutable state
- [ ] Input validation on public functions
- [ ] Error handling present
- [ ] Logging hooks present
- [ ] Unit tests exist with >80% coverage

### JSON5 Configs
- [ ] Valid JSON5 syntax
- [ ] Includes version field
- [ ] Includes description/comment
- [ ] All values within valid ranges
- [ ] Links to relevant concepts

### Markdown Docs
- [ ] Proper heading hierarchy
- [ ] No broken links
- [ ] Code blocks properly formatted
- [ ] Version and date present
- [ ] Linked to concept vault where applicable

## Testing Compliance

### Minimum Test Coverage
- Unit tests: 80%+
- Integration tests: required for multi-module interactions
- Coherence tests: required if coherence field used
- Concealment tests: required if Aletheia Principle active
- Compliance tests: required

### Test Execution
All tests must pass before:
- Committing code
- Merging branches
- Releasing versions
- Declaring phase complete

## Documentation Compliance

### Required Documentation
Every project must maintain:
- Architecture overview
- API documentation (if applicable)
- Concept definitions
- Change log
- Roadmap
- Preservation log

### Documentation Quality
- [ ] All concepts linked to vault
- [ ] All formulas properly formatted
- [ ] All code examples valid
- [ ] All diagrams comprehensible
- [ ] All assumptions stated

## Validation Procedures

### Pre-Commit Validation
```bash
1. Run all tests
2. Check code quality (linting)
3. Validate JSON5 configs
4. Check coherence field
5. Compute concealment delta
6. Update preservation log
```

### Pre-Release Validation
```bash
1. All pre-commit checks
2. Run full test suite
3. Validate documentation complete
4. Check concept vault synchronized
5. Verify roadmap current
6. Generate compliance report
```

## Violation Handling

### Severity Levels
- **Critical:** Violates Aletheia Principle
- **High:** Breaks coherence field
- **Medium:** Fails compliance tests
- **Low:** Documentation incomplete

### Response Protocol
1. Log violation to PRESERVATION_LOG.md
2. Alert operator/agent
3. Block commit/release (if critical/high)
4. Propose remediation
5. Track resolution

## Audit Trail
All compliance checks must be logged with:
- Timestamp
- Check performed
- Result (pass/fail)
- Remediation (if failed)

## Version
**Version:** 1.0.0
**Last Updated:** {{CREATION_DATE}}
**Authority:** Global Governance
```

**Variables:**
- `{{CREATION_DATE}}`: ISO date

---

#### File 3: PRESERVATION_PROTOCOL.md
**Location:** `/gfts/global/PRESERVATION_PROTOCOL.md`

**Required Content:**
```markdown
# PRESERVATION_PROTOCOL.md
## Knowledge Continuity Framework

## Purpose
Defines procedures for preserving concepts, decisions, and knowledge across sessions, agents, and projects.

## Core Principle
**Nothing of value is lost.**

All concepts, insights, decisions, and rationale must be captured and made retrievable.

## Preservation Targets

### 1. Concepts
**What:** Theoretical constructs, principles, definitions, formulas
**Where:** GLOBAL_CONCEPT_VAULT.json5, PROJECT_CONCEPT_VAULT.json5
**Format:** JSON5 structured entries

**Required Fields:**
```json5
{
  name: "Concept Name",
  definition: "Clear, concise definition",
  formal: "Mathematical/logical formulation",
  dependencies: ["Other Concept Names"],
  scope: "global|project",
  active: true|false,
  version: "1.0",
  created: "ISO-8601 timestamp",
  modified: "ISO-8601 timestamp"
}
```

### 2. Architectural Decisions
**What:** Design choices, tradeoffs, constraints
**Where:** /architecture/OVERVIEW.md, PRESERVATION_LOG.md
**Format:** Markdown with rationale

**Required Elements:**
- Decision made
- Alternatives considered
- Rationale for choice
- Constraints that influenced decision
- Impact on system

### 3. Changes
**What:** All modifications to code, config, docs
**Where:** PRESERVATION_LOG.md, CHANGELOG.md
**Format:** Structured log entries

**Required Fields:**
- Timestamp
- Component changed
- Nature of change
- Reason for change
- Validation performed
- Concealment delta

### 4. Errors and Failures
**What:** What went wrong and why
**Where:** PRESERVATION_LOG.md
**Format:** Structured error reports

**Required Fields:**
- Timestamp
- Error description
- Root cause
- Resolution attempted
- Outcome
- Prevention strategy

## Preservation Procedures

### Procedure 1: New Concept Introduction
When introducing a new concept:

1. Check if concept exists in GLOBAL_CONCEPT_VAULT.json5
2. If not, add to PROJECT_CONCEPT_VAULT.json5
3. Include full definition and formal representation
4. Link dependencies to existing concepts
5. Log addition to PRESERVATION_LOG.md
6. Propose elevation to global vault if broadly applicable

### Procedure 2: Concept Modification
When modifying an existing concept:

1. Create new version (don't overwrite)
2. Document what changed and why
3. Update dependencies
4. Mark old version as deprecated (if replacing)
5. Log to PRESERVATION_LOG.md
6. Update all references to concept

### Procedure 3: Concept Deactivation
When a concept is no longer applicable:

1. Set `active: false` (don't delete)
2. Document reason for deactivation
3. Preserve all historical information
4. Update dependencies
5. Log to PRESERVATION_LOG.md

### Procedure 4: Code Changes
When modifying code:

1. Document reason in commit message
2. Add entry to PRESERVATION_LOG.md
3. Link to related concepts
4. Compute concealment delta
5. Validate coherence preserved
6. Update CHANGELOG.md

### Procedure 5: Session Handoff
When ending a session:

1. Update PRESERVATION_LOG.md with session summary
2. Update PROJECT_CONCEPT_VAULT.json5 with new concepts
3. Sync changes to CHANGELOG.md
4. Update ROADMAP.md with progress
5. Document any outstanding issues
6. Validate all preservation targets current

## Concealment Tracking

### Computing Concealment Delta
For every change, compute:

```python
concealment_before = measure_concealment(system_state_before)
concealment_after = measure_concealment(system_state_after)
delta = concealment_after - concealment_before
```

**Concealment Metrics:**
- Undefined variables: +1 per variable
- Undocumented functions: +2 per function
- Unexplained design choices: +5 per choice
- Missing concept definitions: +10 per concept
- Broken links/references: +3 per break

**Reduction Metrics:**
- New documentation: -2 per page
- New concept definition: -10 per concept
- Clarified code: -1 per function
- Added type annotations: -0.5 per annotation
- Added tests: -3 per test

### Logging Concealment
Every PRESERVATION_LOG.md entry must include:

```markdown
**Concealment Delta:** -5 (reduction via documentation)
```

## Cross-Project Preservation

### Global Vault Synchronization
Projects must periodically sync with GLOBAL_CONCEPT_VAULT.json5:

1. Check for new global concepts
2. Import relevant concepts to project vault
3. Propose local concepts for global elevation
4. Resolve conflicts (global takes precedence)
5. Log synchronization

### Concept Elevation Criteria
A project concept qualifies for global vault if:
- Used in 2+ projects
- Broadly applicable
- Well-defined and formal
- No conflicts with existing global concepts
- Approved by governance review

## Validation

### Preservation Integrity Check
Periodically verify:
- [ ] All concepts have definitions
- [ ] All dependencies are valid
- [ ] All log entries are complete
- [ ] No orphaned references
- [ ] Concealment is decreasing
- [ ] Vaults are synchronized

### Recovery from Preservation Failure
If preservation fails:
1. Identify what was lost
2. Reconstruct from available sources
3. Document reconstruction in PRESERVATION_LOG.md
4. Implement safeguards against recurrence
5. Validate reconstruction

## Format Standards

### Timestamps
Use ISO 8601 format:
```
2025-01-15T14:30:00Z
```

### Concept Names
- Use Title Case
- Be specific and unambiguous
- Avoid acronyms unless widely known
- Example: "Generalized Variational Principle" not "GVP"

### Log Entries
Follow this template:
```markdown
### [Timestamp] - [Change Type] - [Component]
**Author:** [identifier]
**Reason:** [why]
**Impact:** [what changed]
**Validation:** [how verified]
**Concepts Modified:** [list]
**Concealment Delta:** [number]
```

## Version
**Version:** 1.0.0
**Last Updated:** {{CREATION_DATE}}
**Authority:** Global Governance
```

**Variables:**
- `{{CREATION_DATE}}`: ISO date

---

#### File 4: GLOBAL_CONCEPT_VAULT.json5
**Location:** `/gfts/global/GLOBAL_CONCEPT_VAULT.json5`

**Required Content:**
```json5
{
  // Global Concept Vault
  // Universal concepts applicable across all projects

  vault_name: "Global Concept Vault",
  version: "1.0.0",
  created: "{{CREATION_DATE}}",
  modified: "{{CREATION_DATE}}",
  authority: "Global Governance",

  concepts: [
    {
      name: "Aletheia Principle",
      active: true,
      scope: "global",
      definition: "Cognition evolves by reducing concealment. All cognitive processes must decrease or maintain the Concealment Functional.",
      formal: "δ∫C(t) dt = 0, where C(t) is the Concealment Functional",
      dependencies: ["Concealment Functional", "Generalized Variational Principle"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "All AI agent operations",
        "Documentation requirements",
        "Code clarity standards",
        "Knowledge preservation"
      ],
      validation: "Concealment delta must be ≤ 0"
    },

    {
      name: "Generalized Variational Principle",
      active: true,
      scope: "global",
      definition: "All tensor evolution follows paths that minimize the action functional. System dynamics emerge from variational optimization.",
      formal: "δS[T] = 0, where S is the action functional over tensor space",
      dependencies: ["Action Functional", "Tensor Space"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Tensor update rules",
        "Coupling dynamics",
        "System evolution",
        "Optimization procedures"
      ],
      validation: "All updates must satisfy Euler-Lagrange equations"
    },

    {
      name: "Concealment Functional",
      active: true,
      scope: "global",
      definition: "A measure of hidden, unexplained, or undefined information in a system. Quantifies the degree to which system behavior is opaque.",
      formal: "C = Σ(undefined_vars + undocumented_funcs*w1 + unexplained_decisions*w2)",
      dependencies: [],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Code quality metrics",
        "Documentation completeness",
        "Transparency measurement"
      ],
      validation: "Must be computable from system state"
    },

    {
      name: "Coherence Field",
      active: true,
      scope: "global",
      definition: "A field measuring system-wide consistency and integrity. Quantifies how well different components align with each other and with governing principles.",
      formal: "Φ_coherence = f(T_L, T_R, coupling, concepts, rules)",
      dependencies: ["Tensor Space"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "System validation",
        "Integration testing",
        "Consistency checking"
      ],
      validation: "Must remain ≥ threshold throughout operations"
    },

    {
      name: "Concept Preservation System",
      active: true,
      scope: "global",
      definition: "Framework for maintaining knowledge continuity across sessions, agents, and projects. Ensures no valuable concepts are lost.",
      formal: "CPS = {vaults, protocols, validation, synchronization}",
      dependencies: ["Concealment Functional", "Aletheia Principle"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Concept vault management",
        "Knowledge transfer",
        "Session continuity"
      ],
      validation: "All concepts must be preserved and traceable"
    },

    {
      name: "Tensor Space",
      active: true,
      scope: "global",
      definition: "The mathematical space in which system tensors (L, R, etc.) exist and evolve. Defines the structure and allowable operations on tensors.",
      formal: "T ∈ ℝ^n with defined metric and connection",
      dependencies: [],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Tensor definitions",
        "Update rules",
        "Coupling mechanisms"
      ],
      validation: "All tensor operations must be well-defined in this space"
    },

    {
      name: "Action Functional",
      active: true,
      scope: "global",
      definition: "The functional whose extremization determines system evolution. Integral of Lagrangian over paths in configuration space.",
      formal: "S[T] = ∫L(T, ∂T, t) dt",
      dependencies: ["Generalized Variational Principle"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Deriving update equations",
        "Validating dynamics",
        "Optimization"
      ],
      validation: "Must be finite and differentiable"
    },

    {
      name: "Global File Template System",
      active: true,
      scope: "global",
      definition: "Standardized project scaffolding system ensuring all projects have predictable structure, governance files, and compliance mechanisms.",
      formal: "GFTS = {templates, installer, validator, governance_links}",
      dependencies: ["Concept Preservation System"],
      version: "1.0",
      created: "{{CREATION_DATE}}",
      modified: "{{CREATION_DATE}}",
      applications: [
        "Project initialization",
        "Structure validation",
        "Cross-project interoperability"
      ],
      validation: "All projects must be GFTS-compliant"
    }
  ],

  relationships: [
    {
      from: "Aletheia Principle",
      to: "Concealment Functional",
      type: "uses",
      description: "Aletheia Principle requires minimizing Concealment Functional"
    },
    {
      from: "Aletheia Principle",
      to: "Generalized Variational Principle",
      type: "compatible_with",
      description: "Both govern system evolution through optimization"
    },
    {
      from: "Generalized Variational Principle",
      to: "Action Functional",
      type: "depends_on",
      description: "GVP extremizes Action Functional"
    },
    {
      from: "Generalized Variational Principle",
      to: "Tensor Space",
      type: "operates_in",
      description: "GVP governs evolution within Tensor Space"
    },
    {
      from: "Coherence Field",
      to: "Tensor Space",
      type: "measures",
      description: "Coherence Field measures consistency in Tensor Space"
    },
    {
      from: "Concept Preservation System",
      to: "Aletheia Principle",
      type: "implements",
      description: "CPS reduces concealment by preserving knowledge"
    },
    {
      from: "Global File Template System",
      to: "Concept Preservation System",
      type: "enforces",
      description: "GFTS enforces CPS through required vault files"
    }
  ],

  deactivated: [
    // Concepts that were once active but are no longer enforced
    // Never delete - only deactivate
  ]
}
```

**Variables:**
- `{{CREATION_DATE}}`: ISO date

---

### Phase 4: Installer Script
**Objective:** Create `create_new_project.py` script

**Location:** `/gfts/create_new_project.py`

**Requirements:**
1. Accept project name as argument
2. Accept optional parameters (version, description, etc.)
3. Create directory structure
4. Copy templates with variable substitution
5. Create symlinks to global files (fallback to copies on Windows)
6. Initialize git repository (optional)
7. Generate initial logs
8. Validate created structure
9. Report success/failure

**Function Signature:**
```python
def create_new_project(
    project_name: str,
    target_directory: str = "./",
    version: str = "0.1.0",
    description: str = "",
    author: str = "GFTS",
    init_git: bool = False,
    variables: dict = None
) -> bool:
    """
    Create new GFTS-compliant project.

    Returns True if successful, False otherwise.
    Logs all actions to console and creation log.
    """
```

**Variable Substitution System:**
- Use `{{VARIABLE_NAME}}` syntax in templates
- Replace with actual values during project creation
- Support default values for optional variables
- Validate all required variables present

**Standard Variables:**
```python
{
    "PROJECT_NAME": project_name,
    "PROJECT_VERSION": version,
    "CREATION_DATE": datetime.now().isoformat(),
    "PROJECT_DESCRIPTION": description,
    "AUTHOR": author,
    "PROJECT_SCOPE": "(to be defined)",
    "CURRENT_PHASE": "Phase 1: Foundation",
    "PROJECT_STATUS": "planning",
    # ... all template variables with defaults
}
```

**Validation:**
- Check all required directories created
- Check all required files present
- Validate symlinks or copies successful
- Check JSON5 files valid
- Report any failures

---

### Phase 5: Validator Script
**Objective:** Create `validate_project.py` script

**Location:** `/gfts/validate_project.py`

**Requirements:**
1. Accept project directory as argument
2. Check all required files present
3. Validate file contents (JSON5 syntax, etc.)
4. Check symlinks valid
5. Validate concept vault alignment
6. Check governance file accessibility
7. Generate compliance report
8. Return pass/fail status

**Function Signature:**
```python
def validate_project(
    project_directory: str,
    verbose: bool = True,
    fix_issues: bool = False
) -> dict:
    """
    Validate GFTS compliance of project.

    Returns validation report with:
    - overall_status: "compliant" | "non-compliant"
    - missing_files: list
    - invalid_files: list
    - warnings: list
    - errors: list
    - recommendations: list
    """
```

**Validation Checks:**
```python
[
    "required_directories_exist",
    "required_files_exist",
    "json5_files_valid",
    "markdown_files_valid",
    "symlinks_valid",
    "concept_vault_aligned",
    "governance_files_accessible",
    "naming_conventions_followed",
    "preservation_log_initialized"
]
```

**Auto-Fix Capability:**
If `fix_issues=True`:
- Create missing directories
- Generate missing template files
- Repair broken symlinks
- Initialize missing concept vaults
- Update preservation log

---

### Phase 6: Documentation
**Objective:** Create comprehensive GFTS documentation

#### File 1: GFTS_SPECIFICATION.md
**Location:** `/gfts/GFTS_SPECIFICATION.md`

**Contents:**
- Complete technical specification
- Directory structure requirements
- Template file specifications
- Variable substitution system
- Validation rules
- Installer usage
- Validator usage
- Integration with governance
- Extension guidelines

#### File 2: README.md
**Location:** `/gfts/README.md`

**Contents:**
- Overview of GFTS
- Quick start guide
- Installation instructions
- Usage examples
- Troubleshooting
- FAQ
- Links to detailed docs

---

## IMPLEMENTATION WORKFLOW

### Step-by-Step Execution Order:

**Step 1: Create GFTS Directory Structure**
```bash
/ALM/gfts/
    /templates/
        /agents/
        /concepts/
        /schemas/
        /modules/
        /architecture/
        /tests/
        /docs/
        /preservation/
    /global/
```

**Step 2: Create Template Files (1-10)**
Create all 10 template files with complete boilerplate content as specified above.

**Step 3: Create Global Governance Files**
Create AGENTS.md, COMPLIANCE_CHARTER.md, PRESERVATION_PROTOCOL.md, GLOBAL_CONCEPT_VAULT.json5

**Step 4: Create Installer Script**
Implement create_new_project.py with full functionality

**Step 5: Create Validator Script**
Implement validate_project.py with full validation logic

**Step 6: Create Documentation**
Write GFTS_SPECIFICATION.md and README.md

**Step 7: Test GFTS System**
1. Run create_new_project.py to create test project
2. Run validate_project.py on test project
3. Verify all files present and valid
4. Test variable substitution
5. Test symlink creation
6. Test on Windows/Linux

**Step 8: Validate Against Own Standards**
Use GFTS to validate the GFTS directory itself (meta-validation)

**Step 9: Generate Final Report**
Create GFTS_BUILD_REPORT.md with:
- Build summary
- All files created
- Validation results
- Usage instructions
- Known limitations
- Future enhancements

---

## SUCCESS CRITERIA

The GFTS system is complete when:

- [ ] All 10 template files exist with complete content
- [ ] All 4 global governance files exist with complete content
- [ ] create_new_project.py successfully creates compliant projects
- [ ] validate_project.py correctly validates projects
- [ ] Variable substitution works correctly
- [ ] Symlink creation works (with copy fallback)
- [ ] All JSON5 files are valid
- [ ] All Markdown files are properly formatted
- [ ] Test project created and validated successfully
- [ ] Documentation complete
- [ ] GFTS validates itself (meta-compliance)

---

## DELIVERABLES CHECKLIST

### Templates (10 files):
- [ ] SESSION_INSTRUCTIONS.md.template
- [ ] PROJECT_RULES.md.template
- [ ] PROJECT_CONCEPT_VAULT.json5.template
- [ ] OVERVIEW.md.template
- [ ] schemas/README.md.template
- [ ] modules/README.md.template
- [ ] TEST_PLAN.md.template
- [ ] CHANGELOG.md.template
- [ ] ROADMAP.md.template
- [ ] PRESERVATION_LOG.md.template

### Global Files (4 files):
- [ ] AGENTS.md
- [ ] COMPLIANCE_CHARTER.md
- [ ] PRESERVATION_PROTOCOL.md
- [ ] GLOBAL_CONCEPT_VAULT.json5

### Scripts (2 files):
- [ ] create_new_project.py
- [ ] validate_project.py

### Documentation (2 files):
- [ ] GFTS_SPECIFICATION.md
- [ ] README.md

### Validation:
- [ ] Test project created
- [ ] Test project validated
- [ ] GFTS self-validation passed

---

## NOTES FOR EXECUTING AGENT

### Autonomy Expectations:
- Choose implementation details for scripts
- Design internal data structures
- Choose helper function names
- Improve code clarity
- Handle edge cases
- Add defensive programming
- Create comprehensive error messages

### Do NOT Ask User For:
- Programming language choice (use Python 3.8+)
- Directory structure (specified above)
- File naming (specified above)
- Template content (specified above)
- Variable names (you decide)
- Algorithm choices (you decide)

### DO Ask User If:
- Specification is ambiguous or contradictory
- Required information completely missing
- Cannot proceed without critical decision
- External dependencies needed

### Quality Standards:
- All code must be production-ready
- All templates must be complete and usable
- All documentation must be comprehensive
- All validation must be thorough
- No placeholders or TODOs in deliverables

### Testing:
- Test create_new_project.py with various inputs
- Test validate_project.py on compliant and non-compliant projects
- Test cross-platform compatibility (Windows paths, symlinks)
- Test error handling and recovery
- Test edge cases

---

## END OF BUILD INSTRUCTIONS

**Ready for execution upon user confirmation.**
