# Skill: Integration Testing

## Goal

Validate interaction between multiple components or layers.

## Techniques

- Exercise service and layer boundaries with realistic setup
- Use real implementations for internal components where practical
- Mock only true externals when needed for stability/cost
- Validate contracts, data flow, and failure propagation across boundaries
- Use fixtures for ephemeral resources and controlled teardown

## Rules

- Test realistic usage scenarios
- Focus on behavior, not implementation details
- Keep setup minimal but realistic
- Keep isolation/cleanup explicit for databases and stateful services
- Label suites for CI routing (`integration`, `slow`, `hybrid`)

## Patterns

- API <-> business logic contract checks
- DB transaction isolation and cleanup strategy
- Service boundary error handling scenarios
- CTest labels for compiled integration tests in mixed-language repos

## Commands

```bash
# Python integration suites
pytest -m integration
pytest -m "integration and not slow"

# C++ integration suites via CTest labels
ctest -L integration --output-on-failure

# Hybrid integration slice
pytest -m hybrid
ctest -L hybrid --output-on-failure
```

## Anti-patterns

- Over-mocking internal components
- Treating integration tests like unit tests
- Testing trivial flows that duplicate unit tests
- Shared mutable environment across tests
