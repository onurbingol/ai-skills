# Skill: Extensible Design via Composition

## Goal

Allow flexible extension without modifying core code.

## Techniques

- Composition over inheritance
- Strategy pattern
- Plugin systems
- Snapshot-based algorithm contracts
- Prefer dataclasses for stable internal snapshots
- Use frozen dataclasses to avoid accidental mutation
- Use __post_init__ for lightweight cross-field checks

## Rules

- Inject dependencies
- Avoid hardcoding behavior
- Allow user-defined extensions
- Pass a state snapshot (dict or dataclass) to strategy components
- Do not pass full host objects when a smaller contract is enough
- Keep strategy components stateless when possible

## Patterns

- interchangeable components
- pluggable backends
- typed component injection via property setters

## Anti-patterns

- Deep inheritance chains
- Hardcoded logic
- Strategies tightly coupled to host class internals
