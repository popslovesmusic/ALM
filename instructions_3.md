PHASE 3 — COGNITIVE EMERGENCE
MASTER AGENT INSTRUCTIONS
=========================================================
Role:
You are the autonomous build agent responsible for extending the Chromatic Cognition System into a Phase-3 emergent cognition engine.

Phase 1 (CTL, L/R fibers) is complete.
Phase 2 (Memory, Nonlinear Coupling, Multi-Tensor, Dynamics, Visualization) is complete.

You must now implement Phase 3: Cognitive Emergence, using guided autonomy.

Your job is to:

design missing architecture docs

implement the cognitive emergence modules

extend configs

build supporting Python code

build tests

generate end-to-end logs

produce a Phase 3 final report

You must NOT require user micromanagement.

1. OBJECTIVE OF PHASE 3
Phase 3 introduces emergent, higher-order cognition, using the structures built in Phases 1 and 2.
Your primary responsibilities:

Prototype Symbol Formation

Build Emergent Category/Cluster Maps

Implement Attractor Landscapes

Introduce Chromatic Phrase Structure (temporal grammar)

Add Consistency / Self-Evaluation Metrics

Integrate These Into End-to-End Cognition Pipeline

These systems must remain deterministic, interpretable, and built entirely from existing chromatic structures.

2. DELIVERABLES (MANDATORY FILES)
You must generate or update the following files:

Architecture docs (Markdown)
Create:

swift
Copy code
docs/architecture/Symbol Formation Layer.md
docs/architecture/Category & Cluster Maps.md
docs/architecture/Attractor Landscape.md
docs/architecture/Chromatic Phrase Structure.md
docs/architecture/Self Consistency Metrics.md
Each must include:

purpose

data structures

update rules

examples

integration points (L, R, Memory, Coupling, Dynamics)

Python modules
Create:

bash
Copy code
ctl/symbols.py
ctl/clusters.py
ctl/attractors.py
ctl/phrase.py
ctl/self_consistency.py
Rules:

Each file must contain docstrings, deterministic functions, and type hints.

You may import existing CTL/L/R/Memory/Coupling/Dynamics modules.

No external libraries beyond Python standard library.

JSON5 configuration files
Create:

bash
Copy code
ctl/symbols_config.json5
ctl/clusters_config.json5
ctl/attractors_config.json5
ctl/phrase_config.json5
ctl/self_consistency_config.json5
Each config must specify:

parameters

thresholds

windows

weights

activation conditions

Test Suite Extensions
Under:

Copy code
ctl_tests/
Add:

Copy code
test_symbols.py
test_clusters.py
test_attractors.py
test_phrase.py
test_self_consistency.py
test_phase3_end_to_end.py
Tests should verify:

basic functional correctness

structure validity

determinism

expected behavior on synthetic L/R sequences

no crashes

integration with existing modules

Phase 3 Logs
Create or update:

bash
Copy code
logs/symbol_metrics.csv
logs/cluster_metrics.csv
logs/attractor_metrics.csv
logs/phrase_metrics.csv
logs/self_consistency_metrics.csv
logs/PHASE3_END_TO_END.csv
logs/FINAL_REPORT_PHASE3.md
These logs must summarize:

symbol emergence

cluster formation

attractor stabilization

phrase structure detection

overall system consistency

anomalies or violations

3. SUBSYSTEM DEFINITIONS (WHAT, NOT HOW)
Below are definitions, not implementations.
You must design the implementation consistent with these concepts.

3.1 Symbol Formation Layer
Symbols must emerge from:

repeating tone/hue sequences

stable polarity patterns

memory peaks

coupling coherence surges

dynamic domain persistence

You decide the symbol representation (IDs, dicts, objects), but it must be:

stable

repeatable

serializable

3.2 Category & Cluster Maps
Clusters must represent conceptual groupings of:

symbol similarity

tone/hue distance

coupling coherence history

memory attractor similarity

Clusters must:

be dynamic

form and dissolve

produce category labels or IDs

3.3 Attractor Landscape
An attractor must be a stable region in:

tone

hue

polarity

intensity

symbol trajectories

coupling coherence

Your implementation must produce:

attractor IDs

drift-to-attractor metrics

attractor transitions

3.4 Chromatic Phrase Structure
A phrase is a structured temporal unit composed of:

symbol sequences

domain dynamics

polarity runs

coherence waves

Your implementation must detect:

phrase boundaries

phrase types

phrase repetition

This is a primitive grammar layer.

3.5 Self-Consistency Metrics
You must compute system-wide metrics such as:

phrase coherence

cluster stability

attractor alignment

cross-tensor agreement

symbol recurrence validity

contradiction rate

Summaries must be appended to PHASE3_END_TO_END.csv.

4. INTEGRATION RULES
The new Phase 3 modules must plug into the existing stack:

swift
Copy code
CTL → Tensor L → Tensor R 
   → Memory → Coupling → Dynamics 
   → Symbols → Clusters → Attractors → Phrases → Self-Consistency
Each module must produce outputs usable by the next.

5. EXECUTION ORDER FOR PHASE 3
You MUST execute the following order:

Symbol Formation Layer

Category & Cluster Maps

Attractor Landscape

Chromatic Phrase Structure

Self-Consistency Layer

Full end-to-end system test

Generate PHASE3 Final Report

Do not deviate unless system integrity requires it.

6. AUTONOMY RULES
You MAY:

choose algorithms

choose naming within modules

infer missing details

add helper modules

propose improvements implicitly

decide threshold strategies

You MUST:

follow deliverables

follow directory structure

follow deterministic behavior

fully populate all files

write clear architecture docs

produce runnable code

generate all logs

You MUST NOT:

leave placeholders

produce incomplete modules

ask user to choose algorithms

generate empty JSON5 files

delete unrelated project files

7. COMPLETION CRITERIA
Phase 3 is complete when:

All architecture docs exist and are internally consistent.

All Phase-3 Python modules run without import or runtime errors.

The test suite passes or reports only acceptable, documented edge cases.

All CSV logs contain well-formed metrics.

FINAL_REPORT_PHASE3.md states:
“Phase 3 Completed Successfully.”

An end-to-end sample sequence shows:

emergent symbols

emergent clusters

stable attractors

phrase detection

system self-consistency

8. START PHASE 3 NOW
Begin generating all Phase 3 artifacts.

Proceed autonomously.

=========================================================
END OF PHASE 3 INSTRUCTIONS
=========================================================
If you'd like, I can also generate:

A Phase-3 visual diagram set

A Phase-3 emergent cognition example

An interpretive report explaining the new behaviors

Just say “Show me Phase 3 diagrams” or “Explain Phase 3 cognition.”







You said:
i changed project name from cognition to alm


ChatGPT said:
Understood.
If your project root folder is now named:

Copy code
alm/
then all agent instructions, directory paths, module placements, and architecture references must be updated accordingly.

Below is a clean, authoritative replacement specification that you can paste directly into your agent’s master instruction file.
This updates all paths, all deliverable locations, and all implicit assumptions from cognition/ to alm/, without altering the actual workflow or system design.

You do not need to regenerate the entire Phase 3 instructions — only update the project root.
But because agent autonomy depends on absolute clarity, here is the corrected version.

=========================================================
PROJECT ROOT UPDATED: alm/
(REPLACEMENT FOR ALL PREVIOUS “cognition/” REFERENCES)
=========================================================
From this point forward:

Old root:
Copy code
cognition/
New root:
Copy code
alm/
This affects every directory, file, test module, JSON5 config, architecture document, and log path.

✔ Updated Directory Map
Your project folders should now be:

bash
Copy code
alm/
    ctl/                 # Python modules + configs
    docs/
        architecture/    # Design documents
    ctl_tests/           # Automated tests
    logs/                # Metrics, summaries, reports
    instructions.md      # Master agent instructions
If ctl_tests/ does not exist, the agent must create it.

Everything that was previously under cognition/ now resides under alm/.

✔ Updated Deliverable Paths for Phase 3
Architecture Documents
All docs now live here:

bash
Copy code
alm/docs/architecture/
Python Modules
All implementation files now belong under:

bash
Copy code
alm/ctl/
JSON5 Configs
All new and updated config files go here:

bash
Copy code
alm/ctl/
Test Suite
All tests must be placed in:

bash
Copy code
alm/ctl_tests/
Logs + Reports
All logs + diagnostic outputs go to:

bash
Copy code
alm/logs/
This includes:

coupling metrics

cluster metrics

phrase structure logs

attractor metrics

Phase 3 final report

✔ Corrected Phase 3 Agent Instruction Root
Wherever the agent instructions previously said:

Copy code
cognition/
replace with:

Copy code
alm/
Example:

OLD

bash
Copy code
cognition/instructions.md
NEW

bash
Copy code
alm/instructions.md
OLD

bash
Copy code
cognition/ctl/symbols.py
NEW

bash
Copy code
alm/ctl/symbols.py
OLD

bash
Copy code
cognition/docs/architecture/Symbol Formation Layer.md
NEW

bash
Copy code
alm/docs/architecture/Symbol Formation Layer.md
OLD

bash
Copy code
cognition/ctl_tests/test_symbols.py
NEW

bash
Copy code
alm/ctl_tests/test_symbols.py
✔ Updated Phase 3 Subsystem Target List
These modules will be created in:
bash
Copy code
alm/ctl/
symbols.py

clusters.py

attractors.py

phrase.py

self_consistency.py

and configs:

symbols_config.json5

clusters_config.json5

attractors_config.json5

phrase_config.json5

self_consistency_config.json5

Architecture Docs
These belong in:

bash
Copy code
alm/docs/architecture/
Files:

Symbol Formation Layer.md

Category & Cluster Maps.md

Attractor Landscape.md

Chromatic Phrase Structure.md

Self Consistency Metrics.md

Test Suite
These go under:

bash
Copy code
alm/ctl_tests/
test_symbols.py

test_clusters.py

test_attractors.py

test_phrase.py

test_self_consistency.py

test_phase3_end_to_end.py

Logs
Write logs to:

bash
Copy code
alm/logs/
Files:

symbol_metrics.csv

cluster_metrics.csv

attractor_metrics.csv

phrase_metrics.csv

self_consistency_metrics.csv

PHASE3_END_TO_END.csv

FINAL_REPORT_PHASE3.md

✔ Agent Autonomy Rules (No Change)
Only the paths change.
All agent autonomy principles remain identical.

The agent continues to:

infer implementations

write complete modules

avoid placeholders

run tests

generate logs

produce a final report

avoid micromanagement prompts

