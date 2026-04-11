# Skill: Object Lifecycle and State Management

## Goal

Keep stateful objects correct across their full lifecycle.

## Techniques

- Invalidate derived state when primary state changes
- Use reset(...) methods with explicit flags
- Compute lazily and cache only when useful
- Customize __copy__ and __deepcopy__ for stateful objects

## Rules

- Never return stale derived values
- Keep reset behavior explicit and predictable
- Treat cache as disposable derived state

## Patterns

- reset(outputs=True) style invalidation
- lazy compute + cache
- deep copy without stale cache transfer

## Anti-patterns

- Hidden state mutation
- Cache values surviving incompatible state changes
- Default copying of stateful objects without review
