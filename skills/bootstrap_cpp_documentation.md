# Bootstrap: C++ Documentation Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on C++ documentation tasks.

## Apply These Skill Areas

- `skills/documentation/`

## Priority Order

1. `skills/documentation/doxygen_documentation.md`
2. `skills/documentation/cross_layer_documentation_consistency.md`
3. `skills/documentation/narrative_documentation.md`

## C++-Specific Defaults

- Prefer Doxygen-compatible comments for public headers and APIs.
- Document ownership, lifetime, and exception/error behavior.
- Keep docs aligned with architectural boundaries.
- Ensure examples compile or map directly to real signatures.
- Prefer Doxygen as the primary C++ documentation system.
- Use Doxygen Graphviz (`dot`) support for call/caller, include, and inheritance graphs.
- Use inheritance diagrams for non-trivial class structures.
- Create module landing pages to connect architecture, usage, and API docs.

## Hybrid Module Notes

- Document both native API behavior and bound-language behavior.
- Call out boundary-specific constraints (types, conversion, performance caveats).
