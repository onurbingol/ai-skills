# Bootstrap: Python Documentation Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on Python documentation tasks.

## Apply These Skill Areas

- `skills/documentation/`

## Priority Order

1. `skills/documentation/python_inline_documentation.md`
2. `skills/documentation/cross_layer_documentation_consistency.md`
3. `skills/documentation/narrative_documentation.md`
4. `skills/documentation/sphinx_documentation.md`
5. `skills/documentation/doxygen_documentation.md`

## Python-Specific Defaults

- Keep docstrings complete for public APIs (parameters, returns, raises, examples).
- Keep architecture and API docs consistent with current module boundaries.
- Prefer executable examples where practical.
- Prefer Graphviz-based workflow diagrams in Sphinx (`sphinx.ext.graphviz`).
- Use inheritance diagrams for meaningful class hierarchies.
- Create module landing pages for navigation and quick orientation.

## Hybrid Module Notes

- Document both Python-facing behavior and native boundary constraints.
- Call out conversion costs, ownership/lifetime assumptions, and error semantics.
