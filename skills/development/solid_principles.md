# Skill: SOLID Principles in Python

## Goal

Design maintainable and extensible systems.

## Techniques

- One class = one reason to change
- Extend via new classes, not modification
- Prefer algorithm injection points for extensibility
- Subclasses must behave like base classes
- Many small interfaces > one large interface
- Depend on abstractions, not implementations

## Rules

- Avoid god classes
- Keep methods small and focused
- Keep host classes closed by delegating variable behavior to abstractions

## Patterns

- OCP via algorithm injection
- Host object defines an abstract strategy contract
- New behavior is added by implementing new strategy classes
- Host code remains unchanged

## Anti-patterns

- God classes with many unrelated reasons to change
- Extending behavior by editing stable host classes repeatedly
- Large implicit interfaces with unclear contracts
- Concrete implementations wired directly into high-level policy code
