# PRESERVATION_PROTOCOL.md
# Knowledge Preservation Rules for MGFTS-Governed Projects

**Version:** 1.0.0
**Layer:** 2 (Governance)
**Status:** Foundational
**Authority:** Global Governance

---

## Purpose

This protocol ensures that knowledge is preserved during project evolution. It implements the Concept Preservation System (CPS) and provides concrete rules for modifying, refactoring, or deleting existing content without losing institutional knowledge.

**Core Principle**: Information is never truly deleted, only transformed or archived.

---

## I. Philosophy

### 1.1 The Knowledge Loss Problem

Software projects accumulate implicit knowledge:
- **Why** decisions were made
- **What** alternatives were considered
- **How** edge cases are handled
- **Context** that makes code comprehensible

Traditional development practices often destroy this knowledge through:
- Undocumented refactoring
- Silent deletions
- Overwriting without reading
- Replacing code without understanding it

**This protocol prevents knowledge loss.**

### 1.2 Preservation vs. Stagnation

Preservation does NOT mean:
- Never deleting anything
- Never refactoring
- Never changing old code
- Keeping all historical versions inline

Preservation DOES mean:
- Documenting before deleting
- Understanding before refactoring
- Archiving before removing
- Explaining changes

**Evolution is encouraged; amnesia is forbidden.**

---

## II. Protected Content Classifications

### 2.1 Class A: Immutable Content

**Definition**: Content that MUST NOT be modified (only versioned).

**Examples**:
- Constitutional Axioms (`CONSTITUTIONAL_AXIOMS.md`)
- Versioned API contracts
- Cryptographic constants
- Historical records

**Modification Process**:
1. Create new version with incremented version number
2. Document relationship to previous version
3. Maintain previous version(s) for reference
4. Update version registry

**Deletion**: FORBIDDEN (archive only)

### 2.2 Class B: Governance Content

**Definition**: Foundational governance files requiring review for modification.

**Examples**:
- `AGENTS.md`
- `COMPLIANCE_CHARTER.md`
- `PRESERVATION_PROTOCOL.md` (this document)
- `GLOBAL_CONCEPT_VAULT.json5`
- Meta-schemas

**Modification Process**:
1. Propose change with detailed rationale
2. Minimum 1-week review period
3. Requires approval from governance authority
4. Document change in amendment section
5. Increment version number
6. Announce to all stakeholders

**Deletion**: Requires exceptional justification and approval

### 2.3 Class C: Structural Content

**Definition**: Code and configuration that implements system behavior.

**Examples**:
- Source code
- Configuration files
- Build scripts
- Database schemas

**Modification Process**:
1. Read and understand existing content
2. Document intent and reasoning
3. Make minimal, incremental changes
4. Preserve behavioral equivalence (or document breaking changes)
5. Update tests
6. Update documentation

**Deletion**: Requires archival (see Section III)

### 2.4 Class D: Documentation

**Definition**: Human-readable explanatory content.

**Examples**:
- README.md
- User guides
- API documentation
- Code comments

**Modification Process**:
1. Verify documentation is outdated/incorrect
2. Update to reflect current state
3. Document what changed in commit message
4. If major rewrite, archive previous version

**Deletion**: Allowed if content is obsolete and no longer relevant

### 2.5 Class E: Transient Content

**Definition**: Temporary content with no long-term preservation requirement.

**Examples**:
- Build artifacts
- Temporary files
- Cache files
- Log files (after retention period)

**Modification Process**: No restrictions

**Deletion**: Allowed without archival

---

## III. Archival Requirements

### 3.1 When Archival is Required

Archival is REQUIRED before:
- Deleting Class A, B, or C content
- Significant rewrites (>50% content change)
- Removing deprecated features
- Changing architectural patterns
- Removing legacy code

### 3.2 Archive Location

**Standard Location**: `/archive/`

**Structure**:
```
/archive/
  /YYYY-MM-DD-HH-MM/         # Timestamp of archival
    /original_path/           # Mirrors original directory structure
      archived_file.ext
      ARCHIVAL_CONTEXT.md     # Required metadata
```

### 3.3 Archival Metadata

Every archival MUST include `ARCHIVAL_CONTEXT.md`:

```markdown
# Archival Context

**Archived Date**: 2025-01-15T14:30:00Z
**Archived By**: developer@example.com
**Original Path**: src/legacy/old_parser.py
**Last Modified**: 2024-12-01T10:00:00Z
**Git Commit**: abc123def456

## Reason for Archival
This parser was replaced by the new unified parser in src/parser/unified_parser.py
due to performance issues and lack of support for modern formats.

## What This Code Did
- Parsed legacy CSV format (pre-2020)
- Handled special cases for customer X's data format
- Implemented custom error recovery logic

## Why It Was Removed
- Performance: O(n²) parsing algorithm
- Maintenance: No tests, poorly documented
- Obsolescence: Format no longer in use

## Replacement
New implementation: src/parser/unified_parser.py
Migration guide: docs/migration/legacy_parser_migration.md

## Dependencies
- Required: pandas < 1.0
- Called by: src/importers/csv_importer.py (now updated)
- Called: None (standalone utility)

## Known Issues
- Bug #123: Crashes on files > 100MB
- Bug #456: Incorrect handling of UTF-8 BOM

## References
- Original PR: #789
- Deprecation RFC: #890
- Replacement PR: #901
```

### 3.4 Archival Process

**Steps**:
1. Create timestamp directory in `/archive/`
2. Copy content to archive location (preserving structure)
3. Create `ARCHIVAL_CONTEXT.md` with complete metadata
4. Commit archive to version control
5. Delete original content
6. Update references in documentation
7. Add entry to `CHANGELOG.md`

**Command Template**:
```bash
# Example archival script
TIMESTAMP=$(date +%Y-%m-%d-%H-%M)
ARCHIVE_DIR="archive/$TIMESTAMP"
ORIGINAL_PATH="src/legacy/old_parser.py"

mkdir -p "$ARCHIVE_DIR/$(dirname $ORIGINAL_PATH)"
cp "$ORIGINAL_PATH" "$ARCHIVE_DIR/$ORIGINAL_PATH"
# Create ARCHIVAL_CONTEXT.md
echo "# Archival Context..." > "$ARCHIVE_DIR/$ORIGINAL_PATH/../ARCHIVAL_CONTEXT.md"
git add "$ARCHIVE_DIR"
git commit -m "archive: preserve old_parser.py before deletion"
git rm "$ORIGINAL_PATH"
git commit -m "remove: old_parser.py (archived to $ARCHIVE_DIR)"
```

---

## IV. Modification Protocols

### 4.1 Before Modifying Any File

**Mandatory Steps**:

1. **Read and Understand**:
   ```python
   # REQUIRED: Read existing file first
   with open(file_path, 'r') as f:
       existing_content = f.read()

   # Analyze:
   # - What does this do?
   # - Why was it written this way?
   # - What are the edge cases?
   # - What might break if I change this?
   ```

2. **Check Dependencies**:
   ```bash
   # Find who imports this
   grep -r "from $(basename $file_path)" .
   grep -r "import $(basename $file_path)" .
   ```

3. **Verify Tests Exist**:
   ```bash
   # Check for corresponding test file
   find tests/ -name "test_$(basename $file_path)"
   ```

4. **Document Intent**:
   ```python
   # Add comment explaining the change
   # MODIFICATION(2025-01-15): Refactored to improve performance
   # Previous implementation: O(n²), new: O(n log n)
   # Preserving edge case handling for empty inputs
   ```

### 4.2 Incremental Modification Pattern

**Prefer Small Steps**:

❌ **ANTI-PATTERN**: Large rewrite
```python
# Delete entire function and rewrite
def complex_function(data):
    # 200 lines of completely new code
    ...
```

✅ **CORRECT**: Incremental refactoring
```python
# Step 1: Add new implementation alongside old
def complex_function_v2(data):
    # New implementation
    ...

# Step 2: Add feature flag
def complex_function(data):
    if USE_NEW_IMPLEMENTATION:
        return complex_function_v2(data)
    else:
        # Old implementation (to be removed in v2.0)
        ...

# Step 3 (later): Remove old implementation after validation
```

**Benefits**:
- Preserves git blame information
- Allows easy rollback
- Maintains test coverage
- Reduces risk

### 4.3 Refactoring Protocol

**Steps**:

1. **Ensure Tests Pass**:
   ```bash
   pytest tests/test_target_module.py  # Must be green
   ```

2. **Refactor Incrementally**:
   - Extract function
   - Rename variable
   - Move to better location
   - Simplify logic
   - (One transformation at a time)

3. **Verify Tests Still Pass**:
   ```bash
   pytest tests/test_target_module.py  # Must still be green
   ```

4. **Update Documentation**:
   - Code comments
   - Docstrings
   - README (if public interface changed)

5. **Commit with Explanation**:
   ```
   refactor(parser): extract validation logic to separate function

   Extracted input validation from parse() to validate_input()
   to improve testability and separation of concerns.
   No behavior change; all tests pass.
   ```

### 4.4 Breaking Change Protocol

**When Changing Public APIs**:

1. **Deprecation First** (when possible):
   ```python
   import warnings

   def old_function(x):
       warnings.warn(
           "old_function is deprecated, use new_function instead",
           DeprecationWarning,
           stacklevel=2
       )
       return new_function(x)

   def new_function(x):
       # New implementation
       ...
   ```

2. **Migration Guide**:
   - Create `docs/migration/v1_to_v2.md`
   - Document all breaking changes
   - Provide example migrations
   - Include timeline for deprecation

3. **Version Bump**:
   - Major version bump (1.x → 2.0) for breaking changes
   - Update CHANGELOG.md
   - Tag release

4. **Announcement**:
   - Notify all users
   - Provide migration timeline
   - Offer support during migration

---

## V. Deletion Protocol

### 5.1 Before Deleting Code

**Verification Checklist**:

- [ ] Verify code is not called anywhere (grep search)
- [ ] Verify code is not referenced in documentation
- [ ] Verify code is not exposed in public API
- [ ] Verify tests can be deleted (or updated to use replacement)
- [ ] Archive if Class A, B, or C content
- [ ] Document reason for deletion

### 5.2 Safe Deletion Process

**Steps**:

1. **Mark as Deprecated**:
   ```python
   @deprecated(version='2.0', reason='Use new_implementation instead')
   def old_function():
       ...
   ```

2. **Wait One Version Cycle**:
   - Allow users to migrate
   - Warn in release notes

3. **Archive**:
   - Follow archival process (Section III)

4. **Delete**:
   - Remove code
   - Remove tests
   - Update documentation
   - Remove from imports

5. **Commit**:
   ```
   remove: old_function deprecated in v1.5, removed in v2.0

   Archived to archive/2025-01-15-14-30/src/old_function.py
   See ARCHIVAL_CONTEXT.md for historical context.
   Migration guide: docs/migration/v1_to_v2.md
   ```

### 5.3 Emergency Deletion

**When Immediate Deletion Required** (security vulnerability, legal requirement):

1. **Delete Immediately**:
   ```bash
   git rm vulnerable_file.py
   git commit -m "security: remove vulnerable_file.py (CVE-2025-0001)"
   ```

2. **Archive Separately** (if safe):
   - Archive to secure location (not public repository)
   - Document in separate security incident report

3. **Notification**:
   - Notify all users immediately
   - Provide remediation steps
   - Document in security advisory

---

## VI. Documentation Preservation

### 6.1 Inline Documentation

**Code Comments**:
- MUST explain "why", not "what"
- MUST be updated when code changes
- SHOULD reference issue numbers or RFCs
- MAY include historical context

**Example**:
```python
# HISTORICAL NOTE: We use a custom hash function here instead of
# Python's built-in hash() because of a collision issue discovered
# in production (Bug #456). The custom function provides better
# distribution for our specific data patterns.
# See: docs/architecture/hash_function_analysis.md
def custom_hash(value):
    ...
```

### 6.2 Commit Message Preservation

**Commit Message Format**:
```
<type>(<scope>): <short summary>

<detailed description>

<metadata>
```

**Example**:
```
fix(auth): prevent timing attack in password comparison

Replaced string comparison with constant-time comparison function
to prevent timing-based password discovery. This vulnerability
was discovered during security audit (Audit-2025-Q1).

Refs: #789
Security: CVE-2025-0001
```

**Preservation**: Git history preserves all commit messages; never rewrite history on main branch.

### 6.3 Decision Records

**When Required**:
- Significant architectural decisions
- Technology selection
- Major refactorings
- Breaking changes

**Format**: Architecture Decision Records (ADRs)

**Location**: `/docs/decisions/`

**Template**:
```markdown
# ADR-001: Use PostgreSQL for Primary Database

**Status**: Accepted
**Date**: 2025-01-15
**Deciders**: @alice, @bob, @charlie

## Context
We need to select a database for our multi-tenant SaaS application...

## Decision
We will use PostgreSQL 14+ as our primary database.

## Consequences
**Positive**:
- Mature, stable, well-documented
- Strong ACID guarantees
- Excellent JSON support
- Row-level security for multi-tenancy

**Negative**:
- Requires more ops expertise than managed NoSQL
- Scaling requires careful planning

## Alternatives Considered
- MongoDB: Ruled out due to lack of strong consistency
- MySQL: Ruled out due to weaker JSON support
- DynamoDB: Ruled out due to vendor lock-in
```

---

## VII. Concept Preservation

### 7.1 Global Concept Vault

**Purpose**: Preserve definitions of core project concepts.

**Location**: `GLOBAL_CONCEPT_VAULT.json5`

**Required Updates**:
- When introducing new domain concepts
- When modifying existing concept definitions
- When deprecating concepts

### 7.2 Concept Lifecycle

**Stages**:

1. **Introduction**:
   ```json5
   {
     concept: "User Session",
     status: "active",
     introduced: "2025-01-15",
     definition: "A temporary authenticated context...",
     examples: ["..."],
     related_concepts: ["User", "Authentication"]
   }
   ```

2. **Evolution**:
   ```json5
   {
     concept: "User Session",
     status: "active",
     introduced: "2025-01-15",
     last_modified: "2025-06-01",
     definition: "An authenticated context with refresh tokens...",
     // Keep changelog
     evolution: [
       {
         date: "2025-06-01",
         change: "Added refresh token support",
         reason: "To improve UX and reduce re-authentication"
       }
     ]
   }
   ```

3. **Deprecation**:
   ```json5
   {
     concept: "User Session",
     status: "deprecated",
     deprecated_date: "2026-01-01",
     reason: "Replaced by stateless JWT authentication",
     replacement: "JWT Token",
     migration_guide: "docs/migration/sessions_to_jwt.md"
   }
   ```

4. **Archival**:
   - Move to `ARCHIVED_CONCEPTS.json5`
   - Preserve full history
   - Reference from current vault

---

## VIII. Enforcement

### 8.1 Automated Checks

**Pre-commit Hooks**:
```bash
#!/bin/bash
# Check for deleted files without archival

deleted_files=$(git diff --cached --name-status | grep "^D" | awk '{print $2}')

for file in $deleted_files; do
  # Check if file is Class A, B, or C
  if [[ $file == mgfts/* ]] || [[ $file == src/* ]]; then
    # Verify archival exists
    if ! git diff --cached | grep -q "archive/.*$file"; then
      echo "ERROR: File $file deleted without archival"
      echo "See PRESERVATION_PROTOCOL.md Section III"
      exit 1
    fi
  fi
done
```

### 8.2 Constitutional Engine Integration

**Validation Rules**:
- Check for archival metadata when files deleted
- Verify commit messages explain modifications
- Ensure documentation updated with code
- Validate concept vault updates

### 8.3 Code Review Checklist

**Reviewers MUST Verify**:
- [ ] Large changes preserve existing behavior (or document breaking changes)
- [ ] Deletions include archival (if required)
- [ ] Commit messages explain reasoning
- [ ] Documentation updated
- [ ] Tests maintained
- [ ] No implicit knowledge lost

---

## IX. Exceptions

### 9.1 Experimental Code

**Branches**: `experiment/*`

**Rules**: Preservation protocol relaxed for experimental branches:
- No archival required for deletions
- Less stringent documentation requirements
- Faster iteration encouraged

**Condition**: Must pass full protocol when merging to main.

### 9.2 Generated Code

**Examples**: Protobuf generated files, API client code

**Rules**:
- No archival required (can be regenerated)
- Document generation command in README
- Version control generation inputs, not outputs (when feasible)

### 9.3 Third-Party Code

**Location**: `/vendor/`

**Rules**:
- Follow upstream's versioning
- Document modifications separately
- Consider upstreaming changes

---

## X. Benefits

Adherence to this protocol provides:

1. **Knowledge Continuity**: Future developers understand "why" decisions were made
2. **Risk Reduction**: Can recover from mistakes using archives
3. **Compliance**: Audit trails for regulated industries
4. **Onboarding**: New team members learn from history
5. **Debugging**: Historical context helps diagnose issues
6. **Archaeology**: Can understand project evolution

---

## XI. Amendments

**Version History**:
- v1.0.0 (2025-01-15): Initial version

**Amendment Process**: See COMPLIANCE_CHARTER.md Article VI.

---

## References

- **AGENTS.md**: Agent behavior rules (Read Before Write rule)
- **COMPLIANCE_CHARTER.md**: Compliance standards
- **GLOBAL_CONCEPT_VAULT.json5**: Concept definitions
- **Aletheia Principle**: Reduce concealment through preservation

---

**Last Updated**: 2025-01-15
**Maintained By**: ALM Constitutional Engine
**Status**: Active
