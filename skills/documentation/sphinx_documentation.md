# Skill: Sphinx Documentation Tooling

## Goal

Implement narrative and API documentation effectively using Sphinx.

## Techniques

- Map tool-agnostic narrative docs into Sphinx structure and navigation
- Use autodoc as reference support, not as complete documentation strategy
- Use `toctree` and cross-references for navigation clarity
- Use Graphviz diagrams for workflow/state/process visualization
- Use inheritance diagrams for non-trivial class hierarchies
- Add module landing pages that summarize purpose, key APIs, and navigation

## Rules

- Keep Sphinx structure aligned with narrative ownership and module boundaries
- Enforce docs build and link checks in CI
- Apply docs versioning/deprecation notes on release-impacting changes
- Treat documentation updates as part of feature/change completion criteria
- Diagrams must be source-controlled text (Graphviz) and built in CI
- Use diagrams where they reduce cognitive load; avoid decorative/low-value diagrams
- Keep landing pages concise and task-oriented; avoid duplicate API dump content

## Patterns

- `docs/index.rst`, `docs/architecture/`, `docs/tutorials/`, `docs/examples/`, `docs/api/`
- "Why this exists" section for non-obvious components
- PR checks: changed-doc build + internal link validation
- Nightly/release checks: full build + external links + example validation
- `sphinx.ext.graphviz` for workflow/process graphs
- `sphinx.ext.inheritance_diagram` for hierarchy visualization
- One landing page per major module/domain with links to tutorials, diagrams, and API

## Anti-patterns

- API dump pages with no narrative path
- Autodoc-only strategy for user onboarding
- Design decisions undocumented in architecture/tutorial layers
- Doc lifecycle unmanaged across versions
- Diagram proliferation with no maintenance owner
- Landing pages that repeat full API reference instead of guiding navigation
