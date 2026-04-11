# Skill: Module API Surface Management

## Goal

Expose a stable public API while keeping implementation details private.

## Techniques

- Use explicit export lists (__all__)
- Keep internal modules private (e.g., _internal.py)
- Re-export through stable public facade modules

## Rules

- Public imports define the supported contract
- Internal modules can change without breaking external users
- Keep experimental symbols out of default exports

## Patterns

- public_module.py re-exporting selected internals
- optional @export decorators for explicit symbol intent
- versioned API changes through facade boundaries

## Anti-patterns

- Importing private modules from application code
- Accidental public exposure of internal symbols
- Uncontrolled wildcard exports
