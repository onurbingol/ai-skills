# Skill: System / End-to-End Testing

## Goal

Validate full system behavior from entry point to output.

## Techniques

- Test critical user workflows as black-box scenarios
- Use production-like configuration and runtime setup
- Validate observable outcomes, not implementation internals
- Keep mocks minimal and limited to unavoidable external infrastructure
- Use markers for release gating (`e2e`, `critical_path`, `slow`)

## Rules

- Tests should reflect real user behavior
- Prioritize critical paths first, then add high-risk edge workflows
- Keep environment parity and test-account lifecycle explicit
- For hybrid modules, treat Python e2e as workflow coverage, not native correctness coverage

## Patterns

- CLI/API/workflow journey tests with clear pass/fail outcomes
- Critical-path suite for release gates
- Flaky-test triage with explicit ownership and stabilization deadlines
- Environment bootstrapping via reproducible fixtures/config

## Commands

```bash
# End-to-end suites
pytest -m e2e

# Release-critical workflow checks
pytest -m critical_path

# Nightly broad workflow validation
pytest -m "e2e or critical_path" --maxfail=1
```

## Anti-patterns

- Testing implementation details
- Overly granular assertions
- Debugging-level test complexity
- Expanding e2e scope to duplicate unit/integration verification
