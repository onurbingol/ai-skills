# Bootstrap: Cross-Cutting Debugging Skills

Version: 1.0 | Last Updated: 2026-04-11

## Purpose

Use this entry point for defect investigation, triage, and regression-proof fixes across Python, C++, and hybrid modules.

## Apply These Skill Areas

- `skills/debugging/`

## Priority Order

1. `skills/debugging/hybrid_debugging_workflow.md`
2. `skills/debugging/python_debugging_workflow.md`
3. `skills/debugging/cpp_debugging_workflow.md`

## Execution Defaults

- Start from reproducible failing scenario before code edits.
- Use evidence-first triage (stack traces, logs, sanitizer output).
- Add regression tests as part of the fix.

## Hybrid Boundary Notes

- Attribute failures by layer first (Python, binding, native).
- Validate from both sides of the boundary before closing.
