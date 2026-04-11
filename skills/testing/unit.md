# Skill: Unit Testing (Isolation-First)

## Goal

Validate individual components in fast, deterministic isolation.

## Techniques

- Use pytest function-style tests and fixtures
- Use Arrange -> Act -> Assert structure
- Mock external collaborators where useful
- Use parameterized tests for input matrix coverage
- Use fixture fakes over heavy global patching

## Rules

- One behavioral intent per test case
- No real DB/network/filesystem unless explicitly faked
- Do not mock the unit under test
- Tests must run independently and in any order
- Unit coverage is a primary metric and should trend non-regressive

## Patterns

- `@pytest.mark.parametrize` for behavior variants
- `pytest-mock` or `monkeypatch` for collaborator seams
- Determinism checklist: fixed seeds, controlled time, no hidden global state
- Clear naming: `test_<behavior>_<condition>_<expectation>`

## Commands

```bash
# Run only unit tests
pytest -m unit

# Run a focused module/test
pytest tests/unit/test_module.py -k "edge_case"

# Unit coverage with branch coverage
pytest -m unit --cov=. --cov-branch --cov-report=term-missing

# Fast feedback mode
pytest -m unit -x --maxfail=1
```

## Anti-patterns

- Overly broad tests with multiple unrelated assertions
- Real infrastructure calls in unit suites
- Mocking internals instead of boundaries
- Slow unit tests that block rapid feedback
