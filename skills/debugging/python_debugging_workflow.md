# Skill: Python Debugging Workflow

## Goal

Resolve Python defects quickly with a reproducible, evidence-first workflow.

## Techniques

- Reproduce failures with the smallest deterministic scenario
- Isolate scope by reducing inputs, fixtures, and side effects
- Inspect runtime state with debugger, logging, and targeted assertions
- Apply minimal fix first, then refactor only when behavior is stable
- Add regression tests before closing the issue

## Rules

- Never debug from production traces alone; recreate locally first
- Keep one hypothesis active at a time and prove/disprove it with data
- Preserve failing artifacts (input, stack trace, environment metadata)
- Confirm fix with targeted test and nearest broader suite
- Capture root cause and prevention note in PR summary

## Patterns

- Repro script under tests fixtures for recurring defects
- Binary-search style isolation across call chain
- Temporary high-signal logging around suspected boundary
- Red test first, then green fix, then cleanup

## Anti-patterns

- Fixing by intuition without a stable repro
- Broad refactors while root cause is unknown
- Removing assertions/logs before regression test exists
- Closing bug after one passing run
