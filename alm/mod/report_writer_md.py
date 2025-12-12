"""ALM Constitutional Engine - Markdown Report Writer

Generates human-readable MGFTS_REPORT.md files.

Includes:
- Summary table with layer scores
- Key findings (violations/warnings)
- Layer-by-layer analysis
- Concept view (missing/unused)
- Aletheia & Coherence commentary

Author: ALM Constitutional Engine
Version: 0.1.0
"""

from typing import Any, Dict, List
from pathlib import Path
from datetime import datetime


def write_markdown_report(state_dict: Dict[str, Any], output_path: Path) -> None:
    """Write MGFTS compliance report as Markdown.

    Parameters
    ----------
    state_dict : dict
        State model dictionary representation
    output_path : Path
        Path to output file
    """
    sections = []

    # 1. Header
    sections.append(_generate_header(state_dict))

    # 2. Summary Table
    sections.append(_generate_summary_table(state_dict))

    # 3. Key Findings
    sections.append(_generate_key_findings(state_dict))

    # 4. Layer-by-Layer Analysis
    sections.append(_generate_layer_analysis(state_dict))

    # 5. Concept View
    sections.append(_generate_concept_view(state_dict))

    # 6. Aletheia & Coherence Commentary
    sections.append(_generate_aletheia_commentary(state_dict))

    # Write to file
    content = "\n\n---\n\n".join(sections)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def _generate_header(state: Dict[str, Any]) -> str:
    """Generate report header with metadata.

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown header
    """
    project = state.get("project", "Unknown")
    timestamp = state.get("timestamp", datetime.utcnow().isoformat())
    overall_score = state.get("scores", {}).get("overall", 0.0)

    # Determine status badge
    if overall_score >= 0.9:
        status = "✅ EXCELLENT"
    elif overall_score >= 0.75:
        status = "✓ GOOD"
    elif overall_score >= 0.5:
        status = "⚠ NEEDS IMPROVEMENT"
    else:
        status = "❌ CRITICAL"

    return f"""# MGFTS Compliance Report

**Project:** `{project}`
**Scan Time:** {timestamp}
**MGFTS Version:** 1.0.0
**Engine Version:** ALM-GOV v0.1

**Overall Score:** {overall_score:.2f} / 1.00
**Status:** {status}
"""


def _generate_summary_table(state: Dict[str, Any]) -> str:
    """Generate summary table with per-layer scores.

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown table
    """
    scores = state.get("scores", {})
    coherence = state.get("coherence_score", 0.0)
    concealment = state.get("concealment_score", 0.0)

    # Layer names
    layer_names = [
        "Layer 1: Structural",
        "Layer 2: Governance",
        "Layer 3: Meta-Schema",
        "Layer 4: Semantic",
        "Layer 5: Ecological",
        "Layer 6: Formal",
        "Layer 7: Ontological"
    ]

    # Build table
    table = "## Summary\n\n"
    table += "| Layer | Score | Status |\n"
    table += "|-------|-------|--------|\n"

    for i, name in enumerate(layer_names, 1):
        score_key = f"layer_{i}_" + name.split(":")[1].strip().lower().replace("-", "_")
        score = scores.get(score_key, 0.0)

        # Status indicator
        if score >= 0.9:
            status_icon = "✅"
        elif score >= 0.75:
            status_icon = "✓"
        elif score >= 0.5:
            status_icon = "⚠"
        else:
            status_icon = "❌"

        table += f"| {name} | {score:.2f} | {status_icon} |\n"

    # Add coherence and concealment
    table += f"| **Coherence Field** | {coherence:.2f} | {'✅' if coherence >= 0.7 else '⚠'} |\n"
    table += f"| **Concealment** | {concealment:.2f} | {'✅' if concealment <= 0.3 else '⚠'} |\n"

    # Overall
    overall = scores.get("overall", 0.0)
    table += f"| **OVERALL** | **{overall:.2f}** | **{'✅' if overall >= 0.75 else '⚠'}** |\n"

    return table


def _generate_key_findings(state: Dict[str, Any]) -> str:
    """Generate key findings section.

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown section
    """
    violations = state.get("violations", [])
    warnings = state.get("warnings", [])
    concepts_missing = state.get("concepts_missing", [])

    section = "## Key Findings\n\n"

    # Critical violations
    critical_violations = [v for v in violations if v.get("severity") == "critical"]
    if critical_violations:
        section += f"### 🚨 Critical Issues ({len(critical_violations)})\n\n"
        for v in critical_violations[:5]:  # Top 5
            section += f"- **[{v.get('code')}]** {v.get('message')}\n"
            section += f"  - File: `{v.get('path')}`\n"
            if v.get("layer"):
                section += f"  - Layer: {v.get('layer')}\n"
        if len(critical_violations) > 5:
            section += f"\n*...and {len(critical_violations) - 5} more critical issues*\n"
        section += "\n"

    # Missing concepts
    if concepts_missing:
        section += f"### 📚 Missing Concepts ({len(concepts_missing)})\n\n"
        for concept in concepts_missing[:10]:
            section += f"- {concept}\n"
        if len(concepts_missing) > 10:
            section += f"\n*...and {len(concepts_missing) - 10} more*\n"
        section += "\n"

    # Warnings summary
    if warnings:
        section += f"### ⚠ Warnings: {len(warnings)} total\n\n"

    if not violations and not warnings and not concepts_missing:
        section += "✅ No critical issues found.\n"

    return section


def _generate_layer_analysis(state: Dict[str, Any]) -> str:
    """Generate layer-by-layer analysis.

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown section
    """
    section = "## Layer-by-Layer Analysis\n\n"

    # TODO: Implement detailed layer analysis
    # For each layer:
    # - Show score
    # - List violations for that layer
    # - Provide interpretation
    # - Suggest improvements

    section += "*Detailed layer analysis not yet implemented.*\n"

    return section


def _generate_concept_view(state: Dict[str, Any]) -> str:
    """Generate concept view section.

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown section
    """
    concepts_missing = state.get("concepts_missing", [])
    concepts_unused = state.get("concepts_unused", [])

    section = "## Concept Analysis\n\n"

    # Missing concepts (referenced but undefined)
    if concepts_missing:
        section += "### Missing Concepts\n"
        section += "*Referenced but not defined in concept vault:*\n\n"
        for concept in concepts_missing:
            section += f"- {concept}\n"
        section += "\n"

    # Unused concepts (defined but never referenced)
    if concepts_unused:
        section += "### Unused Concepts\n"
        section += "*Defined but never referenced:*\n\n"
        for concept in concepts_unused:
            section += f"- {concept}\n"
        section += "\n"

    if not concepts_missing and not concepts_unused:
        section += "✅ All concepts properly defined and used.\n"

    return section


def _generate_aletheia_commentary(state: Dict[str, Any]) -> str:
    """Generate Aletheia & Coherence commentary.

    This section focuses on:
    - Where concealment is concentrated
    - How coherence could be increased
    - Guidance toward compliance (non-prescriptive)

    Parameters
    ----------
    state : dict
        State dictionary

    Returns
    -------
    str
        Markdown section
    """
    concealment = state.get("concealment_score", 0.0)
    coherence = state.get("coherence_score", 0.0)
    violations = state.get("violations", [])

    section = "## Aletheia & Coherence Commentary\n\n"

    # Concealment analysis
    section += "### Concealment Analysis\n\n"
    if concealment < 0.3:
        section += "✅ **Low concealment.** The system is relatively transparent and well-documented.\n\n"
    elif concealment < 0.6:
        section += "⚠ **Moderate concealment.** Some areas lack clarity:\n\n"
    else:
        section += "❌ **High concealment.** Significant opacity detected:\n\n"

    # Identify concealment sources
    if violations:
        section += "**Primary sources of concealment:**\n"
        missing_file_count = len([v for v in violations if "MISSING" in v.get("code", "")])
        undefined_count = len([v for v in violations if "UNDEFINED" in v.get("code", "")])

        if missing_file_count > 0:
            section += f"- {missing_file_count} missing required files\n"
        if undefined_count > 0:
            section += f"- {undefined_count} undefined references\n"

        section += "\n"

    # Coherence analysis
    section += "### Coherence Analysis\n\n"
    if coherence >= 0.8:
        section += "✅ **High coherence.** System components are well-aligned.\n\n"
    elif coherence >= 0.6:
        section += "✓ **Adequate coherence.** Minor alignment issues present.\n\n"
    else:
        section += "⚠ **Low coherence.** Significant inconsistencies detected.\n\n"

    # Guidance (non-prescriptive)
    section += "### Path Forward\n\n"
    section += "To reduce concealment and increase coherence:\n\n"

    if violations:
        section += "1. Address critical violations first\n"
    section += "2. Define missing concepts in concept vault\n"
    section += "3. Ensure all required files are present\n"
    section += "4. Maintain consistent naming conventions\n"
    section += "5. Document design decisions\n"

    section += "\n*This analysis is descriptive, not prescriptive. The engine does not modify files.*\n"

    return section
