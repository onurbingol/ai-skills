# Skill: Testability-Driven Design

## Goal

Design production code that is inherently easy to test.

## Techniques

- Dependency Injection over hard dependencies
- Pure functions where possible
- Explicit inputs and outputs
- Avoid hidden state
- Follow red-green-refactor loops with small increments
- Default to unit tests first (pytest-style) for new behavior

## Rules

- Every class must be mockable or replaceable
- Side effects must be isolated
- Business logic must be independent of infrastructure
- Write the smallest failing test first, then implement minimally
- Refactor only after tests pass and keep behavior unchanged
- Escalate to integration/e2e only when boundary/workflow risk requires it

## Patterns

- Red -> Green -> Refactor with atomic commits
- Pytest fixtures to keep tests readable and reusable
- Constructor injection for collaborators to enable mocking
- Explicit trigger map: unit by default, integration for boundary contracts, e2e for user workflows

## Commands

```bash
# Red phase: run only the new failing test
pytest tests/unit/test_feature.py::test_new_behavior -q

# Green phase: run target file or marker
pytest tests/unit/test_feature.py
pytest -m unit -q

# Refactor safety run
pytest -m "unit or integration" --maxfail=1
```

## Anti-patterns

- Writing tests AFTER design decisions are fixed
- Designing without considering test structure
- Coupling tests to implementation details during refactor
