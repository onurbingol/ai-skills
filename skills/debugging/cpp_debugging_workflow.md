# Skill: C++ Debugging Workflow

## Goal

Diagnose and fix C++ defects with symbol-aware and sanitizer-first triage.

## Techniques

- Build with debug symbols and reproducible compiler flags
- Start with sanitizer runs (ASan/UBSan/TSan as applicable)
- Use stack traces, breakpoints, and watch expressions for state transitions
- Isolate undefined behavior and lifetime issues before logic tweaks
- Validate with focused tests and CTest label reruns

## Rules

- Keep a reproducible failing command and seed when possible
- Prefer sanitizer evidence over speculative pointer reasoning
- Treat data races and UB as release blockers
- Verify behavior across debug and release-like builds
- Add regression tests for every fixed crash or UB path

## Patterns

- Configure dedicated debug preset with symbols and sanitizers
- Capture minimal crashing input and preserve it in fixtures
- Narrow fault domain by toggling modules/features progressively
- Use CTest labels to rerun affected unit/integration subsets

## Anti-patterns

- Debugging optimized builds without symbols
- Ignoring sanitizer warnings after a passing test run
- Touching unrelated ownership models during triage
- Accepting flaky reproduction as resolved
