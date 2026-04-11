# Skill: Interface and Contract Enforcement (Python)

## Goal

Ensure classes strictly follow defined interfaces and contracts.

## Techniques

- Use abc.ABC for abstract base classes
- Use @abstractmethod for required methods
- Use metaclasses for:
  - automatic registration
  - validation at class creation
  - enforcing required attributes
- Use layered abstract hierarchies for responsibility separation
- Use __slots__ for fixed attribute contracts when appropriate

## Patterns

- Interface class defines required behavior
- Concrete classes must implement all methods
- Base -> intermediate -> domain-specific abstract layers

## Rules

- Fail at import time if contract is violated
- Never allow partially implemented classes
- Prefer explicit interfaces over implicit behavior
- Define which layer owns each responsibility

## Anti-patterns

- Duck typing without validation
- Runtime failure due to missing methods
- Single oversized abstract class with mixed concerns
