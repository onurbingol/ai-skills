# Skill: Algorithm Injection Pattern

## Goal

Extend behavior by injecting algorithms instead of modifying host classes.

## Techniques

- Host object owns state and orchestration
- Snapshot contract (dict or dataclass) carries algorithm inputs
- Algorithm object performs computation through an abstract interface
- Inject sub-algorithms (callables) for inner variation points

## Rules

- Prefer stateless algorithms
- Pass minimal snapshot contracts, not full host objects
- Keep algorithm interfaces explicit and stable
- Prefer dataclass snapshots in core code
- Keep richer validation frameworks optional and boundary-scoped

## Patterns

- Unit test algorithms with synthetic snapshots
- Unit test hosts with mocked algorithm implementations
- Keep snapshot contracts documented and versionable

## Anti-patterns

- Host classes hardcoding algorithm details
- Algorithms mutating host object internals
- Snapshot contracts with undocumented keys/fields
