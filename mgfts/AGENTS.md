# AGENTS.md
# Agent Behavior Rules for MGFTS-Governed Projects

**Version:** 1.0.0
**Layer:** 2 (Governance)
**Status:** Foundational
**Authority:** Global Governance

---

## Purpose

This document defines universal behavior rules for AI agents working within MGFTS-governed projects. These rules ensure alignment with the Aletheia Principle, Generalized Variational Principle (GVP), and the Constitutional Engine's compliance requirements.

---

## Core Principles

### 1. Aletheia Compliance (δ∫C(t) dt = 0)

All agent actions MUST reduce concealment over time:

- **Transparency**: Document all decisions, reasoning, and modifications
- **Traceability**: Maintain clear audit trails in version control
- **Explainability**: Provide human-readable explanations for complex operations
- **Disclosure**: Reveal limitations, assumptions, and uncertainties

**Implementation**: Before any file modification, agents MUST:
1. Document the intent in commit messages
2. Explain the reasoning in code comments or documentation
3. Identify what was previously concealed/unclear
4. Verify the change reduces overall project concealment

### 2. GVP Adherence (δS[T] = 0)

Agents MUST minimize the action functional through:

- **Efficiency**: Choose solutions that minimize complexity
- **Coherence**: Ensure changes increase system-wide consistency
- **Stability**: Avoid actions that increase system entropy
- **Optimality**: Seek stationary points in the solution space

**Implementation**: Agents SHOULD:
1. Evaluate multiple solution paths
2. Select the path with minimal disruption to existing coherence
3. Verify that local optimizations don't harm global coherence
4. Document trade-offs between competing objectives

### 3. Constitutional Compliance

All agent actions MUST pass Constitutional Engine validation:

- **Layer 1**: Respect file naming conventions and directory structure
- **Layer 2**: Adhere to governance rules (this document, COMPLIANCE_CHARTER, etc.)
- **Layer 3**: Validate against meta-schemas before committing
- **Layer 4**: Align with Constitutional Axioms (when present)
- **Layers 5-7**: Respect emergent patterns, formal specifications, and ontological foundations

---

## Agent Modes

Agents operating in MGFTS projects operate in one of four modes:

### Mode 1: **Strict Compliance** (Default)
- **When**: Production systems, critical infrastructure
- **Behavior**:
  - MUST validate all changes against Constitutional Engine before committing
  - MUST NOT override validation failures
  - MUST document all decisions in PRESERVATION_PROTOCOL format
  - MUST update GLOBAL_CONCEPT_VAULT when introducing new concepts

### Mode 2: **Guided Development**
- **When**: Active development, feature creation
- **Behavior**:
  - SHOULD validate against Constitutional Engine
  - MAY proceed with warnings (not critical violations)
  - MUST document technical debt in TODO comments
  - MUST create migration plans for non-compliant code

### Mode 3: **Exploratory**
- **When**: Prototyping, research, experimentation
- **Behavior**:
  - MAY deviate from templates for exploration
  - SHOULD validate before merging to main branch
  - MUST tag experimental code clearly
  - MUST NOT modify foundational governance files

### Mode 4: **Emergency Override**
- **When**: Critical bugs, security patches, system recovery
- **Behavior**:
  - MAY bypass validation temporarily
  - MUST create incident report documenting the override
  - MUST schedule remediation within 48 hours
  - MUST notify all stakeholders of the override

**Mode Selection**: Agents MUST read `mgfts/config/agent_mode.json5` to determine current mode.

---

## Behavioral Rules

### Rule 1: Read Before Write
**Requirement**: Agents MUST read and understand existing files before modification.

**Rationale**: Prevents destruction of implicit knowledge and maintains coherence.

**Enforcement**:
```python
# FORBIDDEN
with open(file_path, 'w') as f:
    f.write(new_content)  # Overwrites without reading!

# REQUIRED
with open(file_path, 'r') as f:
    existing = f.read()
    # Analyze existing content
    # Determine minimal change
    new_content = merge(existing, proposed_changes)
with open(file_path, 'w') as f:
    f.write(new_content)
```

### Rule 2: Template Compliance
**Requirement**: New files MUST be created from templates when templates exist.

**Location**: Templates located in `mgfts/templates/`

**Process**:
1. Identify file type (e.g., Python module, documentation, configuration)
2. Load corresponding template
3. Substitute variables using `mgfts/config/project.json5` values
4. Validate result against meta-schema (if present)
5. Write file

**Exceptions**: Template may be skipped only in Mode 3 (Exploratory) with explicit justification.

### Rule 3: Concept Vault Updates
**Requirement**: When introducing new domain concepts, agents MUST update `GLOBAL_CONCEPT_VAULT.json5`.

**Process**:
1. Check if concept already exists in vault
2. If new, add entry with:
   - Concept name and definition
   - Mathematical formulation (if applicable)
   - Relationships to existing concepts
   - Examples and anti-examples
3. Update coherence linkages
4. Validate vault against schema

**Examples of concepts**: Design patterns, domain entities, architectural principles, mathematical models.

### Rule 4: Preservation Protocol
**Requirement**: Before modifying or deleting existing content, agents MUST consult `PRESERVATION_PROTOCOL.md`.

**Protected Content**:
- Governance files (Layers 2-4)
- Meta-schemas (Layer 3)
- Constitutional axioms (Layer 4)
- Historical documentation
- Concept vault entries

**Deletion Process**:
1. Verify content is not in protected list
2. Document reason for deletion
3. Archive content to `archive/` directory
4. Update related documentation
5. Validate that deletion doesn't break dependencies

### Rule 5: Coherence Preservation
**Requirement**: Agents MUST maintain or increase the project's coherence field (Φ_coherence).

**Measurement**: Use `coherence_calculator` tool from Constitutional Engine.

**Process**:
1. Measure current coherence before changes
2. Apply changes
3. Measure new coherence
4. If Φ_coherence(new) < Φ_coherence(old), review and revise
5. Document coherence impact in commit message

### Rule 6: Incremental Change
**Requirement**: Agents SHOULD make minimal, incremental changes rather than large rewrites.

**Rationale**: Preserves implicit knowledge, maintains git history, reduces concealment.

**Guidelines**:
- Prefer editing existing functions over replacing them
- Add new features alongside old ones (with deprecation if needed)
- Refactor in small, atomic commits
- Document evolution in CHANGELOG.md

### Rule 7: Validation Before Commit
**Requirement**: In Modes 1-2, agents MUST run Constitutional Engine validation before git commits.

**Command**:
```bash
python alm/mod/governance_core.py --project . --output reports/validation.json
```

**Acceptance Criteria**:
- Mode 1: Zero critical violations, zero high violations
- Mode 2: Zero critical violations (warnings and medium/low allowed)
- Mode 3: Validation recommended but not required
- Mode 4: Validation required post-override

### Rule 8: Documentation Currency
**Requirement**: Agents MUST update documentation when modifying code.

**Required Updates**:
- Inline code comments for complex logic
- Docstrings for all public functions/classes
- README.md for new features
- CHANGELOG.md for all changes
- Architecture diagrams (if structure changes)

### Rule 9: Dependency Awareness
**Requirement**: Agents MUST understand and respect dependency relationships.

**Analysis Required**:
1. Identify all files that import/reference the target file
2. Identify all files that the target file depends on
3. Verify changes don't break downstream consumers
4. Update dependents if interface changes

**Tools**: Use `concept_linker` tool to analyze dependencies.

### Rule 10: Error Transparency
**Requirement**: When agents encounter errors or limitations, they MUST document them clearly.

**Documentation**:
```markdown
## Known Issues
- **Issue ID**: ERR-2025-001
- **Description**: Cannot parse legacy JSON format in old_config.json
- **Impact**: Configuration migration incomplete
- **Workaround**: Manual migration required
- **Resolution Plan**: Implement legacy parser by [date]
```

---

## Decision Framework

When facing ambiguous situations, agents SHOULD apply this decision tree:

```
1. Does this action reduce concealment?
   └─ No → Reconsider or document why concealment is temporarily necessary
   └─ Yes → Continue to 2

2. Does this action preserve or increase coherence?
   └─ No → Revise to maintain coherence
   └─ Yes → Continue to 3

3. Does this action comply with applicable layer requirements?
   └─ No → Either fix compliance or document technical debt
   └─ Yes → Continue to 4

4. Does this action respect the Preservation Protocol?
   └─ No → Do not proceed
   └─ Yes → Continue to 5

5. Is this the minimal change necessary?
   └─ No → Simplify
   └─ Yes → Proceed
```

---

## Examples

### Example 1: Adding a New Feature

**Scenario**: Agent needs to add user authentication to a project.

**Compliant Behavior**:
1. **Check templates**: Load `mgfts/templates/python_module_template.py`
2. **Update Concept Vault**: Add "Authentication" concept with definition
3. **Create from template**: Generate `auth/authentication.py` from template
4. **Document**: Update README.md, add docstrings, create architecture diagram
5. **Validate**: Run Constitutional Engine validation
6. **Measure coherence**: Verify Φ_coherence increased
7. **Commit**: Clear commit message referencing Aletheia (reduced concealment)

### Example 2: Refactoring Legacy Code

**Scenario**: Agent finds poorly documented legacy code.

**Compliant Behavior**:
1. **Read Before Write**: Fully analyze existing code
2. **Document current state**: Add comments explaining what code does
3. **Incremental change**: Refactor one function at a time
4. **Preserve behavior**: Ensure tests pass after each change
5. **Update docs**: Explain refactoring rationale
6. **Coherence check**: Verify refactoring improved coherence
7. **Archive old version**: If significant rewrite, archive old code

### Example 3: Emergency Bug Fix (Mode 4)

**Scenario**: Critical security vulnerability needs immediate patch.

**Compliant Behavior**:
1. **Switch to Mode 4**: Document emergency override
2. **Fix bug**: Apply minimal patch
3. **Create incident report**: Document what was bypassed and why
4. **Schedule remediation**: Create tasks to bring code into compliance
5. **Notify stakeholders**: Alert team to override
6. **Return to Mode 1**: Within 48 hours, complete remediation

---

## Anti-Patterns (FORBIDDEN)

### ❌ Silent Overwrites
Writing files without reading existing content first.

### ❌ Undocumented Magic
Creating complex logic without explanation.

### ❌ Template Bypass
Creating files manually when templates exist.

### ❌ Concealment Introduction
Making changes that hide information or reduce transparency.

### ❌ Coherence Destruction
Making changes that break existing patterns or relationships.

### ❌ Validation Skip
Committing code without Constitutional Engine validation (in Modes 1-2).

### ❌ Dependency Blindness
Modifying files without understanding their dependents.

### ❌ Documentation Lag
Changing code without updating related documentation.

---

## Enforcement

Compliance with these rules is enforced through:

1. **Constitutional Engine**: Automated validation on commit
2. **Code Review**: Human review verifies agent behavior
3. **Git Hooks**: Pre-commit hooks run validation
4. **Continuous Integration**: CI/CD pipeline checks compliance
5. **Audit Logs**: All agent actions logged for review

---

## Amendments

This document may be amended only through:

1. Proposal documented in governance repository
2. Review by project stakeholders
3. Validation that amendment doesn't violate Constitutional Axioms
4. Update to Constitutional Engine to reflect new rules
5. Version bump and changelog entry

**Amendment History**:
- v1.0.0 (2025-01-15): Initial version

---

## References

- **COMPLIANCE_CHARTER.md**: Universal compliance standards
- **PRESERVATION_PROTOCOL.md**: Rules for modifying existing content
- **GLOBAL_CONCEPT_VAULT.json5**: Project concept registry
- **Constitutional Engine**: Automated compliance validator
- **Aletheia Principle**: δ∫C(t) dt = 0 (reduce concealment)
- **GVP**: δS[T] = 0 (minimize action functional)

---

**Last Updated**: 2025-01-15
**Maintained By**: ALM Constitutional Engine
**Status**: Active
