# Skill: Test Architecture Design

## Goal

Design scalable, maintainable, and policy-driven test suites.

## Techniques

- Mirror production architecture in test layout
- Use a test pyramid with unit-first emphasis
- Keep Python tests pytest-first
- Keep C++ tests CMake/CTest-native with GoogleTest/GoogleMock
- Use labels/markers for suite routing (`unit`, `integration`, `e2e`, `slow`, `native`, `hybrid`)

## Rules

- Define explicit ownership by level: unit vs integration vs end-to-end
- Unit coverage is a tracked and enforced quality gate
- Shared fixtures must be minimal, explicit, and deterministic
- PR pipelines run fast suites first; broader suites run nightly/release
- Hybrid modules must have both Python-facing tests and native boundary tests

## Patterns

- `tests/unit`, `tests/integration`, `tests/system_end_to_end`, `tests/fixtures`
- Decision matrix for when to write unit/integration/e2e tests
- Coverage non-regression policy for unit tests
- CTest labels + pytest markers for selective execution

## Marker and Label Conventions

- Use the same taxonomy in pytest markers and CTest labels when possible
- Required base set: `unit`, `integration`, `e2e`, `slow`, `hybrid`
- Optional compiled-side label: `native`
- Optional release label: `critical_path`
- Each test should have exactly one primary level marker (`unit` or `integration` or `e2e`)
- Add extra markers/labels only for execution traits (`slow`, `critical_path`, `hybrid`, `native`)
- Keep names lowercase and single-token (use underscore only when needed)

## Commands

```bash
# Python test routing by markers
pytest -m unit
pytest -m "integration and not slow"
pytest -m "e2e or critical_path"

# Python coverage gate example
pytest -m unit --cov=. --cov-branch --cov-report=term-missing --cov-fail-under=85

# C++ test routing by CTest labels (after CMake configure/build)
ctest -L unit
ctest -L "integration|hybrid"
ctest --output-on-failure
```

## Anti-patterns

- One giant mixed test folder
- No distinction between behavior, contract, and workflow tests
- CI gates without runtime tiering
- Python-only testing for hybrid modules with native logic
