# Bootstrap: Python Testing Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on Python or hybrid module testing tasks.

## Apply These Skill Areas

- `skills/testing/`

## Priority Order

1. `skills/testing/test_architecture.md`
2. `skills/testing/unit.md`
3. `skills/testing/integration.md`
4. `skills/testing/system_end_to_end.md`
5. `skills/testing/tdd.md`

## Python-Specific Defaults

- Framework: pytest and pytest ecosystem utilities.
- Avoid `unittest.TestCase` style for new tests.
- Keep unit coverage high and enforce non-regression.
- Mock external collaborators where useful in unit tests.

## Execution Guidance

- Use pytest markers for routing (`unit`, `integration`, `e2e`, `slow`, `hybrid`, `critical_path`).
- Keep unit tests fast and deterministic.
- Route broader suites to nightly/release pipelines.

## Hybrid Module Policy

- Python-side tests cover workflows and user-facing behavior.
- Native-side tests (if applicable) cover ABI-sensitive and low-level failure paths.
- Avoid duplicate assertions across layers; split ownership clearly.
