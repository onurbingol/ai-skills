# Bootstrap: C++ Testing Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on C++ or hybrid native testing tasks.

## Apply These Skill Areas

- `skills/testing/`

## Priority Order

1. `skills/testing/test_architecture.md`
2. `skills/testing/unit.md`
3. `skills/testing/integration.md`
4. `skills/testing/system_end_to_end.md`
5. `skills/testing/tdd.md`

## C++-Specific Defaults

- Framework: GoogleTest; use GoogleMock where useful.
- Execution: CMake + CTest as canonical test runner path.
- Label suites by level and execution traits (`unit`, `integration`, `slow`, `hybrid`, `native`).
- Keep unit tests fast and deterministic.

## Hybrid Module Policy

- Python-side tests cover user-facing behavior and workflows.
- Native-side tests cover boundary, ABI-sensitive logic, and low-level failure modes.
- Avoid duplicate assertions across layers; split ownership explicitly.
