# Skill: Python Dunder Protocol Design

## Goal

Use Python protocol methods to create predictable, composable objects.

## Techniques

- __str__ / __repr__ for readable identity
- __eq__ / __ne__ for structural comparison
- __iter__ / __next__ for iteration behavior
- __len__ / __getitem__ for collection-like semantics

## Rules

- Keep protocol semantics consistent with object meaning
- Prefer explicit structural equality over identity checks for domain objects
- Handle floating-point comparisons with tolerance when needed

## Patterns

- __repr__ = __str__ when both should match
- single-object iterable behavior for polymorphic loops
- value-based equality for deterministic tests

## Anti-patterns

- Inconsistent __eq__ behavior across subclasses
- Protocol methods that hide expensive side effects
- Iteration behavior that changes unexpectedly by state
