# Skill: Doxygen Documentation

## Goal

Provide precise, contract-focused documentation for C++ APIs and native boundaries.

## Techniques

- Document public APIs at declaration sites (headers)
- Use Doxygen tags consistently (`@brief`, `@param`, `@return`, `@throws`)
- Describe ownership, lifetime, mutability, and side effects explicitly
- Include constraints, units, and valid ranges where relevant
- Keep native contract details explicit for hybrid modules
- Use Doxygen Graphviz (`dot`) integration for structural diagrams

## Rules

- All public interfaces must be documented
- Prefer intent and constraints over mechanical restatement of signatures
- Document exception/error behavior with conditions
- If native interface behavior changes, update Doxygen in the same PR
- Keep one canonical contract description per API surface
- Enable and validate `dot`-based diagram generation in docs CI where diagrams are used

## Patterns

- Header-level API contracts with concise `@brief` + detailed behavior block
- Ownership/lifetime notes for pointers, references, and transferred resources
- Performance notes only when behavior is non-obvious or cost-sensitive
- Hybrid modules: Doxygen defines native contracts; Python docs define usage semantics
- Doxygen config with `HAVE_DOT = YES` and scoped graph toggles (for example inheritance/call graphs)

## Anti-patterns

- Placeholder or trivial comments
- Signature duplication without semantic value
- Missing ownership/lifetime notes for boundary objects
- Public API changes without documentation updates
