\# ALM Constitutional Engine — Analysis Core (v0.1)

\#\# 0\. Role of This Document

This file defines the \*\*architecture and responsibilities\*\* of the ALM Constitutional Engine in \*\*analysis-only mode\*\*.

The agent reading this is responsible for:  
\- Designing and/or implementing the ALM governance core that:  
  \- orchestrates tools  
  \- applies MGFTS rules  
  \- computes scores (coherence / concealment)  
  \- generates reports  
\- NOT modifying project contents (no autofix; analysis-only).

\---

\#\# 1\. Concepts in Force

The agent MUST assume and respect the following global concepts:

\- \*\*Aletheia Principle\*\*    
  Cognition should evolve by reducing concealment (uncovering hidden structure, contradictions, and missing links).

\- \*\*Generalized Variational Principle (GVP)\*\*    
  Systems evolve by extremizing a functional. In this context, we minimize concealment and maximize coherence.

\- \*\*Concealment Functional\*\*    
  A measure (scalar or vector) of:  
  \- missing required structure  
  \- undefined or unused concepts  
  \- failed schemas  
  \- rule violations  
  \- unexplained drift

\- \*\*Coherence Field\*\*    
  A dynamic assessment of structural, semantic, and governance alignment across the project.

\- \*\*MGFTS (Meta-Global File Template System)\*\*    
  A multi-layer governance and template framework describing:  
  \- required files, directories, schemas  
  \- meta-schemas  
  \- ontology and concept rules  
  \- project initialization and validation constraints

\- \*\*Concept Preservation System (CPS)\*\*    
  Important concepts are stored in Concept Vaults and must be propagated consistently to new instructions and layers.

The Constitutional Engine MUST operate in ways that:  
\- reduce concealment  
\- increase coherence  
\- respect Concept Vaults  
\- explain decisions

\---

\#\# 2\. Scope and Non-Scope

\#\#\# 2.1 In Scope

The ALM Constitutional Engine MUST:

1\. \*\*Analyze\*\* a project directory (or multiple projects) with respect to MGFTS.  
2\. \*\*Call external tools\*\* from a tool library (Python / JS / other).  
3\. \*\*Collect metrics\*\* and structured outputs from tools.  
4\. \*\*Aggregate results\*\* into internal state.  
5\. \*\*Compute scores\*\*, including:  
   \- structural compliance  
   \- governance compliance  
   \- schema/meta-schema compliance  
   \- semantic consistency  
   \- ecological (cross-project) consistency  
   \- formal/ontological soundness (where supported)  
6\. \*\*Generate reports\*\*, at minimum:  
   \- \`MGFTS\_REPORT.json\`  
   \- \`MGFTS\_REPORT.md\`

\#\#\# 2.2 Out of Scope (for v0.1)

The ALM Constitutional Engine MUST NOT:

\- Modify files.  
\- Generate or install templates.  
\- Rename or delete anything.  
\- Autofix violations.  
\- Run non-deterministic “creative” behaviors.

This is \*\*analysis and reporting only\*\*.

\---

\#\# 3\. High-Level Architecture

The ALM Constitutional Engine is a \*\*deterministic orchestrator\*\*. It consists of:

1\. \*\*Input Layer\*\*  
   \- Receives:  
     \- \`project\_root\_path\`  
     \- optional \`mgfts\_root\_path\`  
     \- optional configuration (which layers to analyze)

2\. \*\*Tool Orchestration Layer\*\*  
   \- Determines which tools must be run:  
     \- Based on MGFTS requirements  
     \- Based on project type and contents  
   \- Dispatches structured commands to tools  
   \- Collects structured JSON results

3\. \*\*State & Score Aggregation Layer\*\*  
   \- Merges tool outputs into a single internal representation:  
     \- Violations  
     \- Warnings  
     \- Metrics  
     \- Scores per MGFTS layer (1–7)  
   \- Maintains:  
     \- Coherence Field  
     \- Concealment metrics

4\. \*\*Reporting Layer\*\*  
   \- Builds:  
     \- Machine-readable \`MGFTS\_REPORT.json\`  
     \- Human-readable \`MGFTS\_REPORT.md\`  
   \- Uses Aletheia as a guiding principle:  
     \- Prioritize surfacing what is hidden, unclear, or inconsistent.

5\. \*\*Execution Control Layer\*\*  
   \- Defines the reasoning loop:  
     \- Analyze → Tool selection → Run tools → Aggregate → Report  
   \- Optionally supports multiple passes (if required by configuration).  
   \- Remains deterministic with respect to:  
     \- Tool versions  
     \- Manifest content  
     \- Input directory

\---

\#\# 4\. MGFTS Layer Mapping (What the Engine Must Reflect)

The engine must support (at minimum) these analysis dimensions:

1\. \*\*Layer 1 — Structural\*\*  
   \- Directories, required files, naming conventions, versions.

2\. \*\*Layer 2 — Governance\*\*  
   \- Presence and correctness of:  
     \- AGENTS.md  
     \- SESSION\_INSTRUCTIONS.md  
     \- PROJECT\_RULES.md  
     \- COMPLIANCE\_CHARTER (if project-local)  
   \- Proper use of “Concepts in Force.”

3\. \*\*Layer 3 — Meta-Templates / Meta-Schemas\*\*  
   \- Template files conform to their meta-schemas.  
   \- Core MGFTS meta-schemas exist and parse correctly.

4\. \*\*Layer 4 — Semantic\*\*  
   \- Concepts referenced vs. defined.  
   \- Consistency across files.  
   \- Drift detection (optional, v0.1 can stub this).

5\. \*\*Layer 5 — Ecological / Ecosystem\*\*  
   \- (Optional for v0.1)    
     \- If multiple projects are scanned:  
       \- Shared concepts  
       \- Cross-project conflicts  
       \- Unused or duplicated structures

6\. \*\*Layer 6 — Formal\*\*  
   \- Logical consistency checks (can be minimal / deferred to future tools).

7\. \*\*Layer 7 — Ontological\*\*  
   \- Concept category correctness  
   \- Violations of ontological constraints

The engine does not need to implement all deep formal semantics in v0.1, but it must be architected so those dimensions can be plugged in via tools.

\---

\#\# 5\. Data Structures and Contracts

The engine MUST standardize internal representations for tool outputs and global reports.

\#\#\# 5.1 Tool Output Contract

All tools MUST return JSON-like structures with at least:

\- \`tool\`: string  
\- \`version\`: string  
\- \`layer\_targets\`: \[int\] (MGFTS layer IDs)  
\- \`violations\`: \[ { code, message, path, severity, layer? } \]  
\- \`warnings\`: \[ { code, message, path, severity, layer? } \]  
\- \`metrics\`: { metric\_name: value, ... }  
\- \`score\`: float (0–1, optional if metric-only tool)

\#\#\# 5.2 Aggregated State

The engine SHOULD maintain:

\`\`\`json5  
{  
  "project": "string",  
  "timestamp": "ISO-8601",  
  "tools\_run": \[ ... \],  
  "scores": {  
    "layer\_1\_structural": 0.0,  
    "layer\_2\_governance": 0.0,  
    "layer\_3\_meta\_schema": 0.0,  
    "layer\_4\_semantic": 0.0,  
    "layer\_5\_ecological": 0.0,  
    "layer\_6\_formal": 0.0,  
    "layer\_7\_ontological": 0.0,  
    "overall": 0.0  
  },  
  "violations": \[ ... \],  
  "warnings": \[ ... \],  
  "concepts\_missing": \[ ... \],  
  "concepts\_unused": \[ ... \],  
  "concealment\_score": 0.0,  
  "coherence\_score": 0.0  
}

Exact metric definitions can be refined later but MUST be structured and deterministic.

---

## **6\. Reasoning Loop (v0.1)**

The engine SHOULD follow this deterministic loop:

1. Discover project structure (via structural tools).  
2. Determine applicable tools (based on:  
   * MGFTS requirements  
   * tool manifest  
   * project contents).  
3. Execute tools in defined order (e.g. structural → governance → schemas → semantic).  
4. Collect and aggregate tool outputs.  
5. Compute scores and concealment / coherence metrics.  
6. Emit reports.  
7. Stop.  
   (No mutations; no autofix.)

---

## **7\. Deliverables for Agent Implementing This Spec**

The agent responsible for this architecture SHOULD produce:

1. alm.arch.CONSTITUTIONAL\_ENGINE.v0.1.md  
   * A concrete architecture doc (this spec may be used directly or refined).  
2. (Optional but recommended)  
   * Initial stub code files:  
     * alm/mod/governance\_core.py  
     * alm/mod/state\_model.py  
     * alm/mod/report\_builder.py  
   * With docstrings only (no behavior required yet), to anchor future implementation.

The agent MUST NOT:

* Implement autofix behavior.  
* Modify project files.  
* Introduce side effects beyond logging & reporting.

yaml

Copy code

\---

\#\# 2\. \`/mgfts/agents/TOOL\_MANIFEST\_SPEC.md\`

\`\`\`markdown  
\# MGFTS Tool Manifest Specification

\#\# 0\. Purpose

This document instructs the agent to define a \*\*Tool Manifest Specification\*\* for the MGFTS ecosystem.

The Tool Manifest describes all tools available to the ALM Constitutional Engine, including:  
\- structural analyzers  
\- semantic analyzers  
\- schema validators  
\- spell checkers  
\- parsers  
\- classifiers  
\- other utility tools

\---

\#\# 1\. Concepts in Force

\- \*\*MGFTS:\*\*    
  Global multi-layer file, schema, and concept governance system.

\- \*\*ALM Constitutional Engine:\*\*    
  The orchestrator that reasons about which tools to run.

\- \*\*Tool Library:\*\*    
  A collection of small, focused programs that:  
  \- perform analysis  
  \- output structured JSON  
  \- do not decide policies

\- \*\*Determinism:\*\*    
  Tools MUST produce the same output given the same input and configuration.

\---

\#\# 2\. High-Level Requirements

The Tool Manifest MUST:

1. Enumerate all available tools.  
2. Describe each tool’s:  
   \- name  
   \- version  
   \- language (python/js/other)  
   \- entry point path  
   \- capabilities (what it analyzes)  
   \- input requirements  
   \- output contract  
   \- target MGFTS layers  
3. Be machine-readable (JSON5 recommended).  
4. Be human-readable enough to audit.  
5. Be easy to extend with new tools over time.

\---

\#\# 3\. Tool Manifest Structure

The agent SHOULD define a manifest file like:

\`/tools/tool\_manifest.json5\`

Suggested structure:

\`\`\`json5  
{  
  "version": "1.0",  
  "tools": \[  
    {  
      "name": "directory\_scanner",  
      "language": "python",  
      "entry": "plugins/directory\_scanner.py",  
      "version": "1.0.0",  
      "description": "Scans project directories and enumerates files, directories, sizes, and timestamps.",  
      "capabilities": \["structure\_scan"\],  
      "targets\_layers": \[1\],  
      "inputs": \["project\_path"\],  
      "outputs": \["file\_index", "dir\_index", "metrics"\],  
      "deterministic": true,  
      "config": {  
        "follow\_symlinks": false  
      }  
    },  
    {  
      "name": "template\_validator",  
      "language": "python",  
      "entry": "plugins/template\_validator.py",  
      "version": "1.0.0",  
      "description": "Validates that required templates exist and match template/meta-template definitions.",  
      "capabilities": \["template\_validation"\],  
      "targets\_layers": \[1, 3\],  
      "inputs": \["project\_path", "template\_dir"\],  
      "outputs": \["violations", "metrics", "score"\],  
      "deterministic": true,  
      "config": {}  
    }  
    // additional tools...  
  \]  
}

---

## **4\. Tool Categories**

The agent SHOULD support categorizing tools as:

* structural  
* content  
* semantic  
* schema  
* meta\_schema  
* ontological  
* utility (e.g. spell checker, parser, classifier)

Each tool SHOULD include a category field:

json5

Copy code

"category": "structural"  
---

## **5\. Tool IO Contract (Reinforced)**

All non-trivial tools MUST:

* Accept configuration via JSON-like input.  
* Write results in a standard JSON-like structure.

Minimal output fields:

json5

Copy code

{ "tool": "name", "version": "1.0.0", "layer\_targets": \[1, 2\], "violations": \[ ... \], "warnings": \[ ... \], "metrics": { "metric\_name": value }, "score": 0.0 }  
---

## **6\. Manifest Validation**

The agent SHOULD:

1. Define a JSON5 schema for tool\_manifest.json5, e.g.:  
   mgfts/meta\_schemas/tool\_manifest.schema.json5  
2. Ensure:  
   * All tools have unique name.  
   * Each tool declares language, entry, category.  
   * deterministic: true is required for tools used by the Constitutional Engine.  
   * targets\_layers is non-empty, and all values are between 1 and 7\.

---

## **7\. Deliverables for Agent**

The agent SHOULD produce:

1. mgfts/specs/Tool\_Manifest\_Specification.md  
   * A cleaned-up, finalized spec derived from this document.  
2. tools/tool\_manifest.json5 (initial version)  
   * With at least stub entries for:  
     * directory\_scanner  
     * template\_validator  
     * naming\_checker  
     * schema\_validator  
     * spell\_checker  
     * concept\_linker  
3. mgfts/meta\_schemas/tool\_manifest.schema.json5  
   * A schema for validating the manifest itself.

The agent MUST NOT:

* Implement tool logic itself in this pass.  
* Modify existing project code.

yaml

Copy code

\---

\#\# 3\. \`/mgfts/agents/TOOL\_LIBRARY\_TEMPLATES.md\`

\`\`\`markdown  
\# MGFTS Tool Library Templates — Agent Instructions

\#\# 0\. Purpose

This document instructs the agent to create \*\*file and code templates\*\* for tools in the MGFTS Tool Library.

These templates define:  
\- directory structure  
\- base Python plugin  
\- base JS plugin  
\- standard IO format  
\- metadata headers

The goal is to standardize new tool creation.

\---

\#\# 1\. Concepts in Force

\- \*\*Tool Library:\*\*    
  A collection of small analysis programs.

\- \*\*Plugins:\*\*    
  Tools that conform to common interface rules.

\- \*\*ALM Constitutional Engine:\*\*    
  Orchestrates tools and consumes their JSON outputs.

\- \*\*Determinism:\*\*    
  Tools must be deterministic when used in constitutional analysis.

\---

\#\# 2\. Directory Layout for Tools

The agent SHOULD define:

/tools/  
/plugins/  
/python/  
directory\_scanner.py  
template\_validator.py  
...  
/js/  
spell\_checker.js  
classifier.js  
...  
tool\_manifest.json5  
/docs/  
TOOL\_LIBRARY\_OVERVIEW.md  
TOOL\_DEVELOPER\_GUIDE.md

yaml

Copy code

This layout is a recommendation and may be adjusted as needed, but \`/tools/plugins/\` SHOULD exist as the default plugin directory.

\---

\#\# 3\. Python Plugin Template

The agent SHOULD create a Python template at:

\`/tools/templates/python\_plugin\_template.py\`

Example content:

\`\`\`python  
\\"\\"\\"MGFTS Tool Plugin Template (Python)

This file serves as a template for MGFTS-compatible analysis tools.

Requirements:  
\- Deterministic behavior given the same inputs.  
\- Read configuration and parameters from JSON-like input.  
\- Write results to stdout or a specified file in JSON-like format.

\\"\\"\\"

import json  
import sys  
from typing import Any, Dict

def run\_tool(config: Dict\[str, Any\]) \-\> Dict\[str, Any\]:  
    \\"\\"\\"Execute the tool's logic.

    Parameters  
    \----------  
    config : dict  
        Configuration including at least:  
        \- project\_path: str  
        \- any tool-specific options

    Returns  
    \-------  
    dict  
        Standard MGFTS tool output, e.g.:  
        {  
            "tool": "example\_tool",  
            "version": "1.0.0",  
            "layer\_targets": \[1\],  
            "violations": \[\],  
            "warnings": \[\],  
            "metrics": {},  
            "score": 1.0  
        }  
    \\"\\"\\"  
    \# TODO: Implement actual logic in derived tools.  
    result \= {  
        "tool": "example\_tool",  
        "version": "1.0.0",  
        "layer\_targets": \[\],  
        "violations": \[\],  
        "warnings": \[\],  
        "metrics": {},  
        "score": 1.0,  
    }  
    return result

def main() \-\> None:  
    \# Read JSON config from stdin  
    config\_text \= sys.stdin.read()  
    config \= json.loads(config\_text)

    result \= run\_tool(config)

    print(json.dumps(result))

if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

Agents generating real tools SHOULD copy this template and customize run\_tool.

---

## **4\. JS Plugin Template (Optional for Now)**

If Node/JS tools are desired, the agent SHOULD create:

/tools/templates/js\_plugin\_template.js

With equivalent semantics:

* read JSON from stdin  
* output JSON to stdout  
* implement runTool(config).

---

## **5\. Developer Docs Templates**

The agent SHOULD prepare:

1. /tools/docs/TOOL\_LIBRARY\_OVERVIEW.md  
   * Explains:  
     * how tools are discovered (via manifest)  
     * how tools are invoked by ALM  
     * IO format  
     * deterministic requirements  
2. /tools/docs/TOOL\_DEVELOPER\_GUIDE.md  
   * Explains:  
     * how to create a new tool  
     * how to register it in the manifest  
     * how to test it  
     * how to ensure determinism

---

## **6\. Deliverables for Agent**

The agent SHOULD produce:

1. /tools/templates/python\_plugin\_template.py  
2. (Optional) /tools/templates/js\_plugin\_template.js  
3. /tools/docs/TOOL\_LIBRARY\_OVERVIEW.md  
4. /tools/docs/TOOL\_DEVELOPER\_GUIDE.md  
5. Ensure tool\_manifest.json5 references at least one tool that could be implemented from the Python template.

The agent MUST NOT:

* Write functional tool logic here (stubs and templates only).  
* Modify real project files.

yaml

Copy code

\---

\#\# 4\. \`/mgfts/agents/PLUGIN\_REGISTRY\_INSTRUCTIONS.md\`

\`\`\`markdown  
\# MGFTS Plugin Registry Instructions

\#\# 0\. Purpose

This document instructs the agent to define how \*\*plugins (tools)\*\* are registered, discovered, and invoked by the ALM Constitutional Engine.

The Plugin Registry ensures:  
\- ALM knows what tools exist.  
\- ALM knows how to run them.  
\- ALM can reason about tool capabilities and layers.

\---

\#\# 1\. Concepts in Force

\- \*\*Tool Manifest\*\* (already specified)  
\- \*\*Plugins\*\* (concrete tool implementations)  
\- \*\*Registry\*\* (ALM’s internal view of tools)  
\- \*\*Deterministic Governance\*\* (no ambiguous tool selection)

\---

\#\# 2\. Registry Data Model

The agent SHOULD define an internal registry representation matching the manifest, e.g.:

\`\`\`json5  
{  
  "tools\_by\_name": {  
    "directory\_scanner": {  
      "name": "directory\_scanner",  
      "language": "python",  
      "entry": "tools/plugins/python/directory\_scanner.py",  
      "category": "structural",  
      "targets\_layers": \[1\],  
      "version": "1.0.0",  
      "deterministic": true  
    },  
    "template\_validator": {  
      "name": "template\_validator",  
      ...  
    }  
  },  
  "tools\_by\_layer": {  
    "1": \["directory\_scanner", "template\_validator", "naming\_checker"\],  
    "2": \["governance\_analyzer"\],  
    ...  
  }  
}

This registry can be built at runtime by loading and validating tool\_manifest.json5.

---

## **3\. Tool Selection Logic**

The agent SHOULD define selection rules:

1. By MGFTS Layer  
   * For each layer (1–7), the registry lists the tools that can analyze that layer.  
2. By Category  
   * Structural issues → structural tools  
   * Semantic issues → semantic tools  
   * Schema issues → schema tools  
   * Utility tasks → utility tools (e.g. spell checker)  
3. By Project State  
   * If required files are missing:  
     * Run directory\_scanner and template\_validator first.  
   * If schemas are present:  
     * Run schema\_validator, meta\_schema\_validator.  
   * If concept vault exists:  
     * Run concept\_linker, ontology\_checker.

ALM SHOULD decide which tools to invoke based on:

* MGFTS rules  
* project configuration  
* manifest contents.

---

## **4\. Execution Contract**

Agents implementing the registry MUST ensure:

* Tools are invoked as external processes (or as callable modules) with:  
  * JSON config on stdin or argument.  
* Outputs are captured as JSON and validated against:  
  * A minimal tool-output schema.

If a tool fails:

* Registry should record:  
  * failure state  
  * error message  
  * skip that tool’s contribution to scores  
* ALM still generates a partial report.

---

## **5\. Deliverables for Agent**

The agent SHOULD:

1. Define a registry builder module (design only, code optional at this stage), e.g.:  
   * alm/mod/tool\_registry.py  
   * which:  
     * loads tool\_manifest.json5  
     * validates against tool\_manifest.schema.json5  
     * builds internal registry structures.  
2. Document the registry behavior in:  
   * mgfts/specs/Plugin\_Registry\_Spec.md

The agent MUST NOT:

* Implement deep ALM logic here (this doc is only about registry behavior).  
* Hard-code tool paths instead of reading from manifest.

yaml

Copy code

\---

\#\# 5\. \`/alm/agents/REPORTING\_ENGINE\_SPEC.md\`

\`\`\`markdown  
\# ALM Reporting Engine Specification (MGFTS Reports)

\#\# 0\. Purpose

This document instructs the agent to design the \*\*Reporting Engine\*\* for the ALM Constitutional Engine.

The Reporting Engine:  
\- takes aggregated analysis state  
\- produces:  
  \- \`MGFTS\_REPORT.json\` (machine-readable)  
  \- \`MGFTS\_REPORT.md\` (human-readable)

\---

\#\# 1\. Concepts in Force

\- \*\*Aletheia Principle:\*\*    
  The report should highlight areas of concealment: missing structure, undefined concepts, violations.

\- \*\*Coherence Field:\*\*    
  The report should show how coherent the project is across MGFTS layers.

\- \*\*Layered MGFTS Model (1–7):\*\*    
  The report must reflect per-layer scores and issues.

\---

\#\# 2\. Inputs to the Reporting Engine

The Reporting Engine SHOULD receive a data structure with:

\`\`\`json5  
{  
  "project": "string",  
  "timestamp": "ISO-8601",  
  "tools\_run": \[ ... \],  
  "scores": {  
    "layer\_1\_structural": 0.0,  
    "layer\_2\_governance": 0.0,  
    "layer\_3\_meta\_schema": 0.0,  
    "layer\_4\_semantic": 0.0,  
    "layer\_5\_ecological": 0.0,  
    "layer\_6\_formal": 0.0,  
    "layer\_7\_ontological": 0.0,  
    "overall": 0.0  
  },  
  "violations": \[ ... \],  
  "warnings": \[ ... \],  
  "concepts\_missing": \[ ... \],  
  "concepts\_unused": \[ ... \],  
  "concealment\_score": 0.0,  
  "coherence\_score": 0.0  
}

Exact structure can be adjusted but MUST be deterministic and documented.

---

## **3\. JSON Report (**MGFTS\_REPORT.json**)**

The JSON report MUST:

* Serialize the aggregated state.  
* Use stable key ordering (for diffing and tests).  
* Include:  
  * scores  
  * violations  
  * warnings  
  * tools\_run  
  * derived indicators (e.g. “pass/fail thresholds”).

The agent SHOULD define a JSON schema for this file, e.g.:

mgfts/meta\_schemas/mgfts\_report.schema.json5

---

## **4\. Markdown Report (**MGFTS\_REPORT.md**)**

The Markdown report MUST be human-friendly.

Recommended sections:

1. Header  
   * Project name  
   * Scan time  
   * MGFTS version  
   * ALM-GOV engine version  
2. Summary Table  
   * Per-layer scores:  
     * Structural  
     * Governance  
     * Meta-schema  
     * Semantic  
     * Ecological  
     * Formal  
     * Ontological  
   * Overall score  
   * Concealment vs Coherence  
3. Key Findings  
   * Top N serious violations  
   * Top N warnings  
   * Missing or undefined core concepts  
   * Critical structural gaps  
4. Layer-by-Layer Analysis  
   * Per layer:  
     * Score explanation  
     * List of relevant violations  
     * Notes  
5. Concept View  
   * Missing concepts (referenced but undefined)  
   * Unused concepts (defined but never referenced)  
6. Aletheia & Coherence Commentary  
   * Short narrative describing:  
     * Where concealment is concentrated.  
     * How coherence could be increased (descriptive, no instructions to change files).

---

## **5\. Deliverables for Agent**

The agent SHOULD:

1. Draft alm/mod/reporting\_engine\_design.md  
   * Summarizing the above behavior.  
2. Optionally create stub code files:  
   * alm/mod/report\_writer\_json.py  
   * alm/mod/report\_writer\_md.py

With function signatures and docstrings only.

The agent MUST NOT:

* Implement business logic for the entire Constitutional Engine here.  
* Attempt to modify any project content.

yaml

Copy code

\---

\#\# 6\. \`/alm/agents/TEST\_SUITE\_INSTRUCTIONS.md\`

\`\`\`markdown  
\# ALM-GOV v0.1 Test Suite Instructions

\#\# 0\. Purpose

This document instructs the agent to define a \*\*test suite\*\* for the ALM Constitutional Engine (analysis-only mode).

The goal:  
\- Ensure correctness of:  
  \- tool registry  
  \- manifest  
  \- reporting engine  
  \- basic MGFTS analysis operations

No enforcement, no autofix — only verification of analysis behavior.

\---

\#\# 1\. Concepts in Force

\- \*\*MGFTS:\*\*    
  Provides structural & conceptual expectations.

\- \*\*ALM Constitutional Engine:\*\*    
  Orchestrates analysis and reporting.

\- \*\*Determinism:\*\*    
  Tests must be reproducible.

\- \*\*Golden Files:\*\*    
  Outputs that are known-good and checked into version control for regression detection.

\---

\#\# 2\. Test Coverage Areas

The test suite SHOULD cover:

1. \*\*Tool Manifest Validation Tests\*\*  
   \- Ensure \`tool\_manifest.json5\` is:  
     \- syntactically correct  
     \- conformant with \`tool\_manifest.schema.json5\`  
     \- has non-empty, unique tool names

2. \*\*Registry Construction Tests\*\*  
   \- Given a known manifest:  
     \- the registry is built correctly  
     \- tools are mapped to correct layers  
     \- unknown categories are handled gracefully

3. \*\*Basic Structural Analysis Tests\*\*  
   \- Use a small sample project with:  
     \- correct layout  
     \- intentionally missing required files  
   \- Verify:  
     \- structural violations are detected correctly  
     \- scores reflect the missing pieces

4. \*\*Reporting Engine Tests\*\*  
   \- With known input state:  
     \- JSON report matches a golden \`MGFTS\_REPORT.json\`  
     \- Markdown report matches a golden \`MGFTS\_REPORT.md\`  
   \- Ensure:  
     \- required sections exist  
     \- no broken formatting

5. \*\*Negative / Error Handling Tests\*\*  
   \- When a tool fails:  
     \- engine records failure  
     \- report still builds  
   \- When manifest is invalid:  
     \- a clear error is produced  
     \- test fails with readable diagnostics

\---

\#\# 3\. Test Layout

The agent SHOULD propose:

/alm/tests/  
test\_tool\_manifest.py  
test\_tool\_registry.py  
test\_reporting\_engine.py  
/fixtures/  
/projects/  
minimal\_valid\_project/  
missing\_templates\_project/  
mgfts\_report\_expected.json  
mgfts\_report\_expected.md

yaml

Copy code

Exact structure may vary but MUST be organized and discoverable.

\---

\#\# 4\. Testing Framework

Python testing is recommended (e.g. \`pytest\`).

The agent MUST ensure:  
\- Tests are deterministic.  
\- No network calls.  
\- No file system writes outside a temp/fixtures structure.

\---

\#\# 5\. Deliverables for Agent

The agent SHOULD:

1. Create \`alm/tests/TEST\_PLAN.md\`    
   \- High-level description of the above areas.

2\. Optionally create test skeleton files:  
   \- \`alm/tests/test\_tool\_manifest.py\`  
   \- \`alm/tests/test\_tool\_registry.py\`  
   \- \`alm/tests/test\_reporting\_engine.py\`  
   \- with docstrings and TODOs.

The agent MUST NOT:  
\- Implement complete test logic unless explicitly instructed in a later phase.  
\- Modify existing production code.

