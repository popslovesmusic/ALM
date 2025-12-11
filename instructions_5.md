A Global File Template System (GFTS)
A set of required, standardized file templates that every new project must include so that all agents always have a predictable, stable environment.

This is exactly the right move for a multi-project ecosystem like ALM, MBC, IGSOA, DFVM, SATP, etc.

We are creating:

a minimum viable project skeleton,

required governance files,

required agent instruction files,

required conceptual anchors,

required schema/test directories,

AND real, reusable file content templates.

This is similar to how professional frameworks (Django, Rust Cargo, ROS, Unreal Engine, etc.) enforce a project structure — but tailored to your theoretical ecosystem.

Let me define the full system.

GLOBAL FILE TEMPLATE SYSTEM (GFTS)
Mandatory project scaffolding for all future projects.
Every new project MUST include a set of required directories and required template files, each initialized with specific boilerplate content.

This ensures that agents always know:

where to find governance rules

where to write new modules

where to store concepts

how to remain compliant with Aletheia, CPS, UVF

how to report progress

how to maintain coherence

how to integrate with AGENTS.md

This creates universal project interoperability.

1. Required Directory Tree (Global Standard)
Every project must begin with this structure:

swift
Copy code
/[project_name]/
    /agents/
        SESSION_INSTRUCTIONS.md
        PROJECT_RULES.md
    /concepts/
        PROJECT_CONCEPT_VAULT.json5
    /schemas/
        README.md
    /modules/
        README.md
    /architecture/
        OVERVIEW.md
    /tests/
        TEST_PLAN.md
    /docs/
        CHANGELOG.md
        ROADMAP.md
    /preservation/
        PRESERVATION_LOG.md

AGENTS.md (symlink or direct copy)
COMPLIANCE_CHARTER.md (symlink or direct copy)
PRESERVATION_PROTOCOL.md (symlink or direct copy)
GLOBAL_CONCEPT_VAULT.json5 (symlink or direct copy)
Every project must include these.

2. Required Template Files (with real boilerplate content)
Now the part you were actually asking for:

Templates. Actual file content.
Every project MUST include:

TEMPLATE 1 — SESSION_INSTRUCTIONS.md
Purpose: Directives for local agent execution.

shell
Copy code
# SESSION_INSTRUCTIONS.md

## Purpose
This document defines the operational instructions for agents working inside this project.

## Concepts in Force
(autopopulated from Concept Vault)
- Aletheia Principle
- Generalized Variational Principle
- Concealment Functional
- Coherence Field
- CPS Propagation Rule

## Operational Scope
Describe the phase, goals, and constraints.

## Deliverables
List required outputs for this session.

## Compliance
Agents must follow:
- AGENTS.md
- COMPLIANCE_CHARTER.md
- PROJECT_RULES.md
TEMPLATE 2 — PROJECT_RULES.md
Purpose: Domain-specific invariants.

shell
Copy code
# PROJECT_RULES.md

## Purpose
Defines domain constraints that apply only within this project.

## Invariants
- All tensors must follow GVP
- Coherence Field must remain monotonic
- No destructive overwrites

## Project-Specific Laws
(add your rules here)
TEMPLATE 3 — PROJECT_CONCEPT_VAULT.json5
Purpose: Local concept memory for the project.

json
Copy code
{
  "project": "NAME",
  "version": "1.0",
  "concepts": [
    {
      "name": "Aletheia Principle",
      "active": true,
      "definition": "Cognition evolves by reducing concealment.",
      "formal": "δ∫C(t) dt = 0",
      "dependencies": ["GVP", "Concealment Functional"]
    }
  ]
}
TEMPLATE 4 — OVERVIEW.md
Purpose: Project architecture description.

markdown
Copy code
# Architecture Overview

## Project Name
DESCRIPTION

## Core Principles
- Aletheia
- GVP
- Coherence Field
- CPS

## System Components
List high-level architecture parts.

## Tensor Topology
Define tensors used here.
TEMPLATE 5 — SCHEMA README
pgsql
Copy code
# SCHEMAS

Place all JSON/JSON5 schemas here.

All schemas must follow the Template Naming System.
TEMPLATE 6 — MODULE README
less
Copy code
# MODULES

All Python/C++/Rust modules belong here.

Naming standard:
[project].mod.[name].vX.Y.ext
TEMPLATE 7 — TEST_PLAN.md
markdown
Copy code
# Test Plan

## Overview
Testing strategy for this project.

## Required Test Types
- unit tests
- coherence tests
- concealment reduction tests

## Compliance Tests
Ensure Aletheia Principle is upheld.
TEMPLATE 8 — CHANGELOG.md
csharp
Copy code
# Changelog

## v0.1
- project created from global scaffolding
TEMPLATE 9 — ROADMAP.md
markdown
Copy code
# Project Roadmap

- Phase 1:
- Phase 2:
- Phase 3:
TEMPLATE 10 — PRESERVATION_LOG.md
pgsql
Copy code
# Preservation Log

Tracks updates to concepts, schemas, and architecture.

Follows PRESERVATION_PROTOCOL.md.
3. Global Template Installer
We can create a script:

create_new_project.py

It will auto-generate all these directories and templates for ANY project name you give it.

Agents can use it directly.

4. Integration with AGENTS.md
AGENTS.md will include:

pgsql
Copy code
## Project Initialization Requirement
Every new project MUST be created using the Global File Template System (GFTS).
Failure to include required templates invalidates the project structure.
Agents will be required to:

refuse to work in a non-compliant folder

offer to auto-initialize missing templates

update missing Concept Vault entries

establish cross-links

This guarantees ecosystem integrity.