# Skill: Controlled Attribute Access

## Goal

Protect object state and enforce invariants.

## Techniques

- Use @property for getters
- Use setter methods for validation
- Store internal state as private (_attribute)
- Use lazy properties for computed values
- Reset or invalidate derived state when primary state changes

## Rules

- No direct public attribute mutation
- Validate all inputs in setters
- Keep objects always in a valid state
- Add a private gate method (e.g., _check_readiness()) for compute methods
- Verify required fields before computation starts
- Raise one clear error listing all missing prerequisites

## Patterns

- Computed attributes via properties
- Operation-readiness checks at compute entry points

## Anti-patterns

- Public mutable attributes
- Skipping validation
- Returning stale computed values after setters mutate state
