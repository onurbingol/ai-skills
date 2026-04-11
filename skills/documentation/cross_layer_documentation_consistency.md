# Skill: Cross-Layer Documentation Consistency

## Goal

Keep terminology, contracts, and behavior descriptions consistent across inline, narrative, and native docs.

## Techniques

- Maintain a canonical terminology set across Python docstrings, Sphinx pages, and Doxygen
- Map each concept to a primary documentation owner and secondary references
- Define explicit contract mapping for Python-facing vs native-facing behavior
- Use change checklists to detect and prevent documentation drift

## Rules

- Terminology for the same concept must be identical across layers
- Behavioral and contract changes require same-PR updates to all impacted docs
- Sphinx conceptual claims must match inline and native contract documentation
- Hybrid modules must document conversion, ownership, error mapping, and performance caveats consistently

## Patterns

- Ownership map: Sphinx -> architecture and reasoning (why); Python inline docs -> usage semantics (what/how); Doxygen -> native contracts and constraints
- Hybrid contract checklist applied on mixed-language changes
- Drift checklist in PR review for API/behavior-altering commits

## Anti-patterns

- Different names for same concept
- Docs drifting from implementation
- Sphinx saying one thing, code doing another
- Boundary behavior documented differently in Python and C++ layers
