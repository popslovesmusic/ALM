# Meta-Global File Template System (MGFTS)

**Version:** 1.0.0
**Status:** Production Ready
**License:** MIT

> "Governance is not a constraint—it's a foundation for transcendent software evolution."

---

## What is MGFTS?

MGFTS is a **7-layer governance framework** for software projects that ensures:

- **Structural Consistency** (Layer 1): Standardized file structure and naming
- **Governance Compliance** (Layer 2): Agent behavior rules and compliance standards
- **Meta-Governance** (Layer 3): Self-regulating, self-validating governance
- **Transcendental Governance** (Layer 4): Constitutional axioms that govern the governors
- **Ecological Intelligence** (Layer 5): Emergent wisdom from pattern recognition
- **Formal Verification** (Layer 6): Mathematical proofs of correctness
- **Ontological Foundation** (Layer 7): Existence criteria and truth semantics

MGFTS combines **template-based project scaffolding** with **automated compliance validation** to create projects that are not just well-structured, but philosophically coherent and formally sound.

---

## Quick Start

### 1. Create a New Project

```bash
python scripts/create_new_project.py my-awesome-project
```

This creates a complete project with:
- ✅ Standardized directory structure
- ✅ Governance files (AGENTS.md, COMPLIANCE_CHARTER.md, etc.)
- ✅ Templates for all common file types
- ✅ Configuration files
- ✅ Git repository initialized

### 2. Develop with Compliance

Your project now has built-in governance:

```python
# All files created from templates automatically
# comply with MGFTS standards

# Example: Create new module from template
from pathlib import Path

template = Path("mgfts/templates/python_module.py.template").read_text()
# Substitute variables and create file
```

### 3. Validate Compliance

```bash
python scripts/validate_project.py .
```

**Output:**
```
✅ PASSED
Overall Score: 0.95
Layer 1: 1.0
Layer 2: 0.92

Warnings:
  [LOW] STRUCT-004: CHANGELOG.md could be more detailed
```

### 4. Commit with Confidence

Pre-commit hooks automatically validate compliance:

```bash
git add .
git commit -m "feat: add user authentication"
# ✅ MGFTS validation passed
```

---

## The 7 Layers

### Layer 1: Structural Templates 📁

**What:** Standardized file structure and templates

**Example:**
```
/project/
  /src/          # Source code
  /tests/        # Tests
  /docs/         # Documentation
  /mgfts/        # Governance files
```

**Benefits:**
- Instant familiarity for new team members
- Consistency across projects
- Automated file generation

---

### Layer 2: Governance 📋

**What:** Rules for agents and developers

**Files:**
- `AGENTS.md`: Agent behavior rules
- `COMPLIANCE_CHARTER.md`: Compliance standards
- `PRESERVATION_PROTOCOL.md`: Knowledge preservation
- `GLOBAL_CONCEPT_VAULT.json5`: Concept registry

**Benefits:**
- AI agents know how to behave
- Clear compliance criteria
- Knowledge never lost

---

### Layer 3: Meta-Governance 🔄

**What:** Governance for governance (self-regulation)

**Features:**
- Templates for templates
- Schemas for schemas
- Validation for validators

**Benefits:**
- System can evolve its own governance
- Consistency at meta-level
- Self-validation

---

### Layer 4: Transcendental Governance 🎯

**What:** Constitutional axioms (immutable principles)

**Example:**
```markdown
## Constitutional Axiom #1
No user data shall be logged unencrypted.

## Axiom #2
System shall degrade gracefully under load.
```

**Benefits:**
- Foundational principles never violated
- All rules derive from axioms
- Clear decision framework

---

### Layer 5: Ecological Intelligence 🌿

**What:** Pattern recognition and emergent wisdom

**Features:**
- Automatic pattern detection
- Collective learning
- Ecosystem health metrics

**Benefits:**
- System learns from itself
- Patterns emerge naturally
- Organic evolution

---

### Layer 6: Formal Verification ✓

**What:** Mathematical proofs of correctness

**Example:**
```
Specification: sort(list) returns sorted list
Proof: ∀ lists L, ∀ i,j where i<j: result[i] ≤ result[j]
Verified: ✓ (via Coq/Isabelle)
```

**Benefits:**
- Correctness guaranteed
- Critical systems verified
- Trust through proof

---

### Layer 7: Ontological Foundation 🏛️

**What:** Existence criteria and truth semantics

**Example:**
```json5
{
  concept: "User",
  exists_when: [
    "has_unique_identifier",
    "has_authentication_method",
    "has_permission_set"
  ]
}
```

**Benefits:**
- Concepts well-defined
- No ambiguity
- Ontological grounding

---

## Core Principles

### Aletheia Principle: δ∫C(t) dt = 0

**"Reduce concealment over time"**

Concealment (C) is hidden/implicit information. The Aletheia Principle states that systems should continuously reduce concealment.

**How:**
- Document undocumented code
- Explain complex logic
- Make assumptions explicit
- Add comments to magic numbers

**Measurement:**
```
C = 0.3·(1-doc_coverage) + 0.3·(complexity/max) + 0.2·dead_code + 0.2·implicit_deps
Target: C < 0.3
```

---

### GVP (Generalized Variational Principle): δS[T] = 0

**"Systems seek coherence"**

Just as light takes the path of least time, software naturally evolves toward maximum coherence.

**How:**
- Consistent naming conventions
- Uniform design patterns
- Minimal coupling
- Architectural alignment

**Measurement:**
```
Φ = 0.25·naming + 0.25·patterns + 0.25·(1-coupling) + 0.25·architecture
Target: Φ > 0.7
```

---

### Preservation Protocol

**"Knowledge is never lost, only transformed"**

Before deleting or modifying code:
1. Read and understand it
2. Archive with context
3. Document reason for change
4. Update related documentation

---

## Usage Examples

### Example 1: Create Python Project

```bash
python scripts/create_new_project.py my-python-app \
  --language python \
  --layers 1,2,3 \
  --author "Your Name"

cd my-python-app
tree
```

**Output:**
```
my-python-app/
├── src/
│   ├── __init__.py
│   └── example.py
├── tests/
│   └── test_example.py
├── docs/
│   └── initial_validation.json
├── mgfts/
│   ├── AGENTS.md
│   ├── COMPLIANCE_CHARTER.md
│   ├── PRESERVATION_PROTOCOL.md
│   ├── GLOBAL_CONCEPT_VAULT.json5
│   ├── templates/
│   └── config/
│       └── project.json5
├── README.md
├── CHANGELOG.md
└── .gitignore
```

### Example 2: Add New Module from Template

```python
# add_module.py
from pathlib import Path
import json

# Load template
template_path = Path("mgfts/templates/python_module.py.template")
template = template_path.read_text()

# Define substitutions
substitutions = {
    "MODULE_DESCRIPTION": "User authentication module",
    "MODULE_PURPOSE": "Handle user login and session management",
    "AUTHOR": "Jane Doe",
    "VERSION": "1.0.0",
    "CLASS_NAME": "Authenticator",
    "MGFTS_LAYER": "1",
    "DEPENDENCIES": "cryptography, jwt",
}

# Substitute variables
result = template
for key, value in substitutions.items():
    result = result.replace(f"{{{{{key}}}}}", value)

# Write new module
output_path = Path("src/auth.py")
output_path.write_text(result)

print(f"✅ Created {output_path}")
```

### Example 3: Validate Before Commit

```bash
# .git/hooks/pre-commit
#!/bin/bash

echo "Running MGFTS validation..."
python scripts/validate_project.py . --severity high

if [ $? -ne 0 ]; then
  echo "❌ MGFTS validation failed"
  echo "Fix violations before committing"
  echo "Run: python scripts/validate_project.py ."
  exit 1
fi

echo "✅ MGFTS validation passed"
```

---

## Documentation

### Specifications
- **[GFTS_SPECIFICATION.md](GFTS_SPECIFICATION.md)**: Complete GFTS/MGFTS specification
- **[MGFTS_BUILD_INSTRUCTIONS.md](../MGFTS_BUILD_INSTRUCTIONS.md)**: 7-layer architecture details
- **[CONSTITUTIONAL_ENGINE_ARCHITECTURE.v0.1.md](specs/CONSTITUTIONAL_ENGINE_ARCHITECTURE.v0.1.md)**: Validation engine

### Governance Files
- **[AGENTS.md](AGENTS.md)**: Agent behavior rules
- **[COMPLIANCE_CHARTER.md](COMPLIANCE_CHARTER.md)**: Compliance standards
- **[PRESERVATION_PROTOCOL.md](PRESERVATION_PROTOCOL.md)**: Preservation rules
- **[GLOBAL_CONCEPT_VAULT.json5](GLOBAL_CONCEPT_VAULT.json5)**: Concept registry

### Tools
- **[create_new_project.py](../scripts/create_new_project.py)**: Project scaffolding
- **[validate_project.py](../scripts/validate_project.py)**: Compliance validation
- **[governance_core.py](../alm/mod/governance_core.py)**: Constitutional Engine

---

## Templates

MGFTS provides 10 comprehensive templates:

1. **Python Module** (`python_module.py.template`) - Full-featured Python module
2. **Python Test** (`python_test.py.template`) - Pytest test suite
3. **JavaScript Module** (`javascript_module.js.template`) - Node.js module
4. **Configuration** (`config.json5.template`) - JSON5 configuration
5. **Documentation** (`documentation.md.template`) - Comprehensive docs
6. **API Specification** (`api_spec.yaml.template`) - OpenAPI/Swagger spec
7. **JSON Schema** (`json_schema.json5.template`) - JSON Schema definition
8. **README** (`README.md.template`) - Project README
9. **CHANGELOG** (`CHANGELOG.md.template`) - Version history
10. **Domain Class** (`domain_class.py.template`) - Domain-driven design class

All templates include:
- Comprehensive documentation
- Type annotations
- Error handling
- Examples
- Best practices

---

## Validation

### Automatic Validation

```bash
python scripts/validate_project.py /path/to/project
```

**Checks:**
- ✅ Directory structure compliance
- ✅ Required files present
- ✅ Naming conventions
- ✅ Governance files valid
- ✅ Configuration correct
- ✅ Templates used properly

### Constitutional Engine (Deep Validation)

```bash
python alm/mod/governance_core.py --project . --output report.json
```

**Generates:**
- **JSON Report**: Machine-readable violations
- **Markdown Report**: Human-readable analysis with Aletheia commentary

**Measures:**
- Concealment score
- Coherence score
- Layer-specific compliance
- Overall project health

---

## Integration

### CI/CD (GitHub Actions)

```yaml
name: MGFTS Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Validate
        run: python scripts/validate_project.py . --severity high
```

### Pre-commit Hooks

```bash
# Install pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
python scripts/validate_project.py . --severity high || exit 1
EOF

chmod +x .git/hooks/pre-commit
```

---

## FAQ

### Q: Do I need all 7 layers?

**A:** No! Start with Layers 1-2 (structural + governance). Add higher layers as needed:
- Small projects: Layers 1-2
- Medium projects: Layers 1-3
- Enterprise/Critical: Layers 1-6 or all 7

### Q: Can I customize templates?

**A:** Yes! Templates in `mgfts/templates/` are yours to customize. Just maintain the core structure.

### Q: What if validation fails?

**A:** Fix the reported violations, or add exceptions to `.mgfts-exceptions.json5` with justification.

### Q: Is MGFTS language-agnostic?

**A:** Mostly. Layers 1-2 work with any language. Templates are provided for Python and JavaScript. Add templates for other languages.

### Q: How does this compare to other frameworks?

**A:** MGFTS is unique in combining:
- **Scaffolding** (like Yeoman, Cookiecutter)
- **Governance** (like RFC processes)
- **Validation** (like linters/formatters)
- **Philosophy** (like Domain-Driven Design)
- **Formal Methods** (like TLA+, Coq)

---

## Roadmap

### Version 1.1 (Q2 2025)
- [ ] Additional language templates (Go, Rust, TypeScript)
- [ ] Web UI for validation reports
- [ ] IDE plugins (VS Code, IntelliJ)
- [ ] Layer 5 implementation (pattern recognition)

### Version 2.0 (Q4 2025)
- [ ] Layer 6 implementation (formal verification)
- [ ] Layer 7 implementation (ontology)
- [ ] Machine learning-based pattern detection
- [ ] Multi-project governance (monorepo support)

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

**Areas we need help:**
- Additional language templates
- IDE integrations
- Documentation improvements
- Bug fixes and testing

---

## License

MIT License - see [LICENSE](../LICENSE) for details.

---

## Contact

- **Documentation**: [GFTS_SPECIFICATION.md](GFTS_SPECIFICATION.md)
- **Issues**: [GitHub Issues](https://github.com/alm-project/mgfts/issues)
- **Discussions**: [GitHub Discussions](https://github.com/alm-project/mgfts/discussions)

---

<div align="center">

**Built with ❤️ by the ALM Team**

*"From structure to transcendence, one layer at a time."*

</div>
