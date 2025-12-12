# COMPLIANCE_CHARTER.md
# Universal Compliance Standards for MGFTS-Governed Projects

**Version:** 1.0.0
**Layer:** 2 (Governance)
**Status:** Foundational
**Authority:** Global Governance

---

## Preamble

This Charter establishes the universal compliance standards for all projects governed by the Meta-Global File Template System (MGFTS). These standards derive from the Aletheia Principle, the Generalized Variational Principle (GVP), and the seven-layer architecture of MGFTS.

**Purpose**: To ensure all project artifacts maintain:
- **Transparency** (Aletheia)
- **Coherence** (GVP)
- **Traceability** (Preservation)
- **Validity** (Formal Correctness)
- **Meaning** (Ontological Grounding)

---

## Article I: Layer Compliance Requirements

### Section 1.1: Layer 1 (Structural Compliance)

**Requirement**: All projects MUST maintain a coherent directory structure.

**Standards**:

1. **Directory Structure**:
   ```
   /project_root/
     /src/               # Source code
     /docs/              # Documentation
     /tests/             # Test suites
     /config/            # Configuration files
     /scripts/           # Automation scripts
     /mgfts/             # MGFTS governance files
       /templates/       # Project templates
       /meta_schemas/    # Validation schemas
       /config/          # MGFTS configuration
     /archive/           # Deprecated/archived content
   ```

2. **File Naming Conventions**:
   - Source files: `snake_case.ext` or `kebab-case.ext`
   - Classes: `PascalCase` in filename (e.g., `UserAuthentication.py`)
   - Configuration: `SCREAMING_SNAKE_CASE.ext` or `lowercase.ext`
   - Documentation: `UPPER_CASE.md` for governance, `Title_Case.md` for guides
   - Tests: `test_*.py` or `*.test.js`

3. **File Headers**:
   All source files MUST include:
   ```python
   """Module description.

   Purpose: [What this module does]
   Layer: [MGFTS layer(s) this relates to]
   Dependencies: [Key dependencies]

   Author: [Author/Team]
   Version: [Semantic version]
   """
   ```

4. **Validation**:
   - Tool: `directory_scanner` and `naming_checker`
   - Frequency: On every commit
   - Acceptance: Zero critical structural violations

### Section 1.2: Layer 2 (Governance Compliance)

**Requirement**: All projects MUST include foundational governance files.

**Required Files**:
1. `mgfts/AGENTS.md` - Agent behavior rules
2. `mgfts/COMPLIANCE_CHARTER.md` - This document
3. `mgfts/PRESERVATION_PROTOCOL.md` - Content modification rules
4. `mgfts/GLOBAL_CONCEPT_VAULT.json5` - Concept registry
5. `README.md` - Project overview
6. `CHANGELOG.md` - Change history
7. `LICENSE` - Legal terms (if applicable)

**Standards**:
- All governance files MUST be version-controlled
- Changes to governance files MUST be reviewed by at least one human
- Governance files MUST pass `template_validator`
- Governance files MUST NOT be deleted without archival

**Validation**:
- Tool: `governance_analyzer`
- Frequency: On governance file modification
- Acceptance: All required files present and valid

### Section 1.3: Layer 3 (Meta-Governance Compliance)

**Requirement**: Projects with schemas MUST provide meta-schemas.

**When Required**: If project includes:
- JSON/YAML configuration files
- API specifications
- Database schemas
- Data validation rules

**Standards**:
1. Every schema MUST have a corresponding meta-schema
2. Meta-schemas MUST be in JSON Schema format (or equivalent)
3. All instances MUST validate against their schemas
4. Schema versioning MUST follow semantic versioning
5. Breaking changes MUST be documented in migration guides

**Example**:
```
/config/database_config.json5     → instance
/mgfts/meta_schemas/database_config.schema.json5  → meta-schema
```

**Validation**:
- Tool: `schema_validator` and `meta_validator`
- Frequency: On configuration file modification
- Acceptance: All instances validate against schemas

### Section 1.4: Layer 4 (Transcendental Compliance)

**Requirement**: Projects MAY define Constitutional Axioms that govern all other layers.

**When Required**: Recommended for:
- Critical infrastructure
- Multi-year projects
- Projects with >5 contributors
- Projects with compliance requirements (legal, safety, etc.)

**Standards**:
1. Axioms MUST be immutable (versioned, never edited)
2. Axioms MUST be documented in `mgfts/CONSTITUTIONAL_AXIOMS.md`
3. All lower-layer rules MUST derive from axioms
4. Axiom violations MUST halt all operations
5. Axiom changes MUST trigger project-wide review

**Example Axioms**:
- "No user data shall be logged unencrypted"
- "All financial calculations shall use decimal arithmetic"
- "System shall degrade gracefully under load"

**Validation**:
- Tool: `axiom_checker` (when Layer 4 implemented)
- Frequency: On every commit
- Acceptance: Zero axiom violations

### Section 1.5: Layer 5 (Ecological Intelligence Compliance)

**Requirement**: Projects MAY implement emergent pattern recognition.

**When Beneficial**:
- Large codebases (>10k LOC)
- Projects with evolving patterns
- Multi-paradigm projects

**Standards**:
1. Pattern emergence MUST be documented
2. Emergent conventions MUST NOT contradict lower layers
3. Pattern changes MUST be gradual, not abrupt
4. Ecosystem health metrics MUST be tracked

**Validation**:
- Tool: `pattern_recognizer`, `ecosystem_health`
- Frequency: Weekly or on major changes
- Acceptance: Ecosystem coherence > 0.7

### Section 1.6: Layer 6 (Formal Verification Compliance)

**Requirement**: Critical projects SHOULD provide formal specifications.

**When Required**:
- Safety-critical systems
- Cryptographic implementations
- Distributed consensus algorithms
- Financial transaction systems

**Standards**:
1. Formal specs MUST use a recognized specification language
2. Invariants MUST be stated explicitly
3. Proofs MUST be machine-checkable where possible
4. Verification results MUST be documented

**Example Specification Languages**:
- TLA+, Alloy, Coq, Isabelle, Z notation

**Validation**:
- Tool: `theorem_prover_integration`, `invariant_verifier`
- Frequency: On algorithm modification
- Acceptance: All stated invariants proven

### Section 1.7: Layer 7 (Ontological Compliance)

**Requirement**: Projects SHOULD define existence criteria for core concepts.

**When Beneficial**:
- Domain-driven design projects
- Knowledge management systems
- Semantic web applications
- AI/ML systems with concept learning

**Standards**:
1. Core concepts MUST be defined in GLOBAL_CONCEPT_VAULT
2. Concept definitions MUST include existence criteria
3. Concept relationships MUST be explicit (is-a, has-a, part-of, etc.)
4. Concept evolution MUST be traceable

**Example Existence Criteria**:
```json5
{
  concept: "User",
  exists_when: [
    "has_unique_identifier",
    "has_authentication_method",
    "has_permission_set"
  ],
  ceases_when: [
    "account_deleted AND retention_period_expired"
  ]
}
```

**Validation**:
- Tool: `ontology_validator`, `concept_coherence_checker`
- Frequency: On concept vault modification
- Acceptance: All concepts well-defined

---

## Article II: Cross-Cutting Compliance Standards

### Section 2.1: Aletheia Compliance (Concealment Reduction)

**Principle**: δ∫C(t) dt = 0 - Concealment must decrease over time.

**Requirements**:

1. **Documentation Completeness**:
   - Every public API MUST be documented
   - Every complex algorithm MUST have explanatory comments
   - Every configuration option MUST be explained
   - Every assumption MUST be stated explicitly

2. **Traceability**:
   - All decisions MUST be traceable to requirements or rationale
   - All changes MUST have meaningful commit messages
   - All bugs MUST have linked issue tickets
   - All technical debt MUST be documented

3. **Transparency Metrics**:
   - Documentation coverage MUST be > 80%
   - Code complexity MUST be measured and bounded
   - Dead code MUST be removed or archived
   - Hidden dependencies MUST be made explicit

**Measurement**:
```
Concealment Score =
  0.3 * (1 - doc_coverage) +
  0.3 * (cyclomatic_complexity / max_allowed) +
  0.2 * (dead_code_ratio) +
  0.2 * (implicit_dependency_ratio)

Target: Concealment Score < 0.3
```

**Validation**:
- Tool: `concealment_calculator`
- Frequency: On every commit
- Acceptance: Concealment score decreasing or stable at low value

### Section 2.2: Coherence Compliance (GVP)

**Principle**: δS[T] = 0 - System seeks minimal action functional.

**Requirements**:

1. **Consistency**:
   - Naming conventions MUST be uniform across project
   - Error handling MUST follow consistent patterns
   - Logging MUST use consistent formats
   - Testing MUST follow consistent structure

2. **Coupling Minimization**:
   - Modules SHOULD have minimal dependencies
   - Circular dependencies MUST NOT exist
   - Interface contracts MUST be stable
   - Side effects MUST be minimized and documented

3. **Coherence Metrics**:
   - Coupling metrics MUST be tracked
   - Pattern consistency MUST be measured
   - Naming coherence MUST be validated
   - Architectural coherence MUST be maintained

**Measurement**:
```
Coherence Score =
  0.25 * naming_coherence +
  0.25 * pattern_coherence +
  0.25 * (1 - coupling_factor) +
  0.25 * architectural_alignment

Target: Coherence Score > 0.7
```

**Validation**:
- Tool: `coherence_calculator`
- Frequency: On every commit
- Acceptance: Coherence score stable or increasing

### Section 2.3: Preservation Compliance

**Requirement**: Knowledge MUST NOT be lost during evolution.

**Standards**:

1. **Before Deletion**:
   - Verify content is not referenced elsewhere
   - Archive deleted content to `/archive/` with context
   - Document reason for deletion
   - Update related documentation

2. **Before Modification**:
   - Read and understand existing content
   - Preserve implicit knowledge through comments
   - Make incremental changes, not rewrites
   - Document what changed and why

3. **Before Refactoring**:
   - Ensure tests exist for current behavior
   - Verify tests pass before and after refactoring
   - Maintain behavioral equivalence
   - Document any intentional behavior changes

**Enforcement**: See `PRESERVATION_PROTOCOL.md`

### Section 2.4: Version Control Compliance

**Requirements**:

1. **Commit Messages**:
   - MUST follow format: `<type>(<scope>): <description>`
   - Types: feat, fix, docs, refactor, test, chore
   - MUST reference issue numbers when applicable
   - MUST explain "why", not just "what"

   Example:
   ```
   feat(auth): add OAuth2 support for enterprise SSO

   Implements OAuth2 flow to enable enterprise customers to use
   their existing identity providers. Reduces concealment by
   documenting the authentication flow in docs/auth.md.

   Refs: #123
   ```

2. **Branching**:
   - `main`: production-ready code
   - `develop`: integration branch
   - `feature/*`: new features
   - `fix/*`: bug fixes
   - `hotfix/*`: emergency production fixes

3. **Pull Requests**:
   - MUST pass all CI checks
   - MUST pass Constitutional Engine validation
   - MUST include tests for new functionality
   - MUST update documentation
   - SHOULD be reviewed by at least one human

### Section 2.5: Testing Compliance

**Requirements**:

1. **Coverage**:
   - Unit test coverage MUST be > 80%
   - Critical paths MUST be > 95%
   - Integration tests MUST cover main workflows
   - Regression tests MUST exist for all bugs

2. **Test Quality**:
   - Tests MUST be deterministic
   - Tests MUST be independent
   - Tests MUST be fast (<1s per unit test)
   - Tests MUST have clear names describing what they test

3. **Test Organization**:
   - Tests MUST mirror source structure
   - Test fixtures MUST be in `/tests/fixtures/`
   - Test utilities MUST be in `/tests/utils/`
   - Golden files MUST be in `/tests/fixtures/golden/`

### Section 2.6: Security Compliance

**Requirements**:

1. **Secrets Management**:
   - Secrets MUST NOT be committed to version control
   - Secrets MUST be stored in secure vaults or environment variables
   - Secret scanning MUST run on every commit
   - Leaked secrets MUST be rotated immediately

2. **Dependencies**:
   - Dependencies MUST be pinned to specific versions
   - Dependencies MUST be scanned for vulnerabilities
   - Vulnerable dependencies MUST be updated within 7 days (critical) or 30 days (high)
   - Dependency licenses MUST be compatible with project license

3. **Input Validation**:
   - All external input MUST be validated
   - All user input MUST be sanitized
   - All database queries MUST use parameterization
   - All file paths MUST be validated

---

## Article III: Validation and Enforcement

### Section 3.1: Automated Validation

**Constitutional Engine**:
- MUST run on every commit (Modes 1-2)
- MUST validate against all applicable layers
- MUST produce JSON report with violations
- MUST produce Markdown report with remediation guidance

**Continuous Integration**:
- MUST run all tests
- MUST check code coverage
- MUST run security scans
- MUST validate documentation builds

### Section 3.2: Manual Review

**Required For**:
- Governance file changes
- Axiom additions/modifications
- Security-critical code
- Breaking API changes

**Review Criteria**:
- Aletheia compliance (reduces concealment)
- Coherence preservation (maintains consistency)
- Preservation protocol adherence
- Layer-specific requirements met

### Section 3.3: Violation Severity

**Critical**: Blocks commit/merge
- Axiom violations
- Security vulnerabilities (CVSS > 7.0)
- Data loss potential
- Breaking changes without migration path

**High**: Requires immediate attention
- Governance violations
- Test failures
- Coherence degradation
- Missing documentation for public APIs

**Medium**: Should be fixed soon
- Style guide violations
- Incomplete test coverage
- Minor coherence issues
- Outdated documentation

**Low**: Technical debt
- Code duplication
- Minor naming inconsistencies
- Missing optional documentation
- Non-critical TODO items

### Section 3.4: Remediation

**Violation Response**:
1. Automated validation reports violation
2. Agent or developer reviews violation
3. If valid violation:
   - Fix immediately (Critical, High)
   - Schedule fix (Medium - within 1 week)
   - Document as technical debt (Low)
4. If false positive:
   - Document exception in `.mgfts-exceptions.json5`
   - Submit issue to Constitutional Engine project
5. Update validation rules if needed

---

## Article IV: Exemptions and Exceptions

### Section 4.1: Temporary Exceptions

**When Allowed**:
- Emergency Mode (Mode 4) operations
- Prototype/experimental code (Mode 3)
- Third-party code integration (documented in `.mgfts-exceptions.json5`)

**Requirements**:
- MUST be documented with justification
- MUST have expiration date
- MUST have remediation plan
- MUST be reviewed periodically

**Format** (`.mgfts-exceptions.json5`):
```json5
{
  exceptions: [
    {
      id: "EXC-2025-001",
      file: "legacy/old_parser.py",
      violation: "Missing documentation",
      severity: "medium",
      reason: "Legacy code scheduled for replacement",
      expires: "2025-06-01",
      remediation: "Replace with new parser module by expiration",
      approved_by: "tech-lead@example.com"
    }
  ]
}
```

### Section 4.2: Permanent Exceptions

**Rarely Granted For**:
- Generated code (clearly marked)
- Binary assets
- Third-party code (in `/vendor/`)
- Test fixtures/data

**Requirements**:
- MUST be approved by project governance committee
- MUST be documented in this charter (amendment)
- MUST be re-evaluated annually

---

## Article V: Compliance Reporting

### Section 5.1: Compliance Dashboard

**Required Metrics**:
- Overall compliance score (weighted by layer)
- Concealment score trend
- Coherence score trend
- Violation counts by severity
- Test coverage percentage
- Documentation coverage percentage

**Frequency**: Updated on every commit

### Section 5.2: Periodic Reviews

**Quarterly Review**:
- Review all medium/low violations
- Review all exceptions
- Update remediation plans
- Assess overall health trends

**Annual Review**:
- Review compliance charter for updates
- Review Constitutional Axioms (if present)
- Assess Layer 5-7 needs
- Update validation tools

---

## Article VI: Amendments

### Section 6.1: Amendment Process

1. **Proposal**: Document proposed change with rationale
2. **Review**: Stakeholder review (minimum 1 week)
3. **Validation**: Verify no Constitutional Axiom conflicts
4. **Approval**: Requires consensus or designated authority
5. **Implementation**: Update charter, tools, and training
6. **Announcement**: Notify all contributors

### Section 6.2: Amendment History

**Version 1.0.0** (2025-01-15):
- Initial version
- Defines compliance for Layers 1-7
- Establishes Aletheia, GVP, and Preservation requirements

---

## Article VII: Interpretation

In case of ambiguity or conflict:

1. **Constitutional Axioms** (Layer 4) take precedence over all other rules
2. **Aletheia Principle** guides interpretation (choose transparency)
3. **GVP** guides implementation (choose coherence)
4. **Preservation Protocol** guides modification (preserve knowledge)
5. **Common sense** applies when rules don't cover a situation

**Escalation**: Unresolved conflicts escalate to governance committee or project lead.

---

## References

- **AGENTS.md**: Agent behavior rules
- **PRESERVATION_PROTOCOL.md**: Content modification rules
- **GLOBAL_CONCEPT_VAULT.json5**: Concept definitions
- **Constitutional Engine**: Automated validation tool
- **MGFTS Specification**: Seven-layer architecture
- **Aletheia Principle**: δ∫C(t) dt = 0
- **GVP**: δS[T] = 0

---

## Appendix A: Compliance Checklist

Quick reference for developers:

- [ ] File structure follows Layer 1 conventions
- [ ] All required governance files present (Layer 2)
- [ ] Schemas validated against meta-schemas (Layer 3)
- [ ] No Constitutional Axiom violations (Layer 4)
- [ ] Code documented (Aletheia)
- [ ] Tests written and passing
- [ ] Commit message follows format
- [ ] Constitutional Engine validation passed
- [ ] Pull request approved
- [ ] CHANGELOG.md updated
- [ ] Concealment score stable or decreasing
- [ ] Coherence score stable or increasing

---

**Last Updated**: 2025-01-15
**Maintained By**: ALM Constitutional Engine
**Status**: Active
**Binding**: All MGFTS-governed projects
