# Skill: CI Pipeline Design

## Goal

Design tiered CI pipelines that balance fast feedback with deep validation.

## Techniques

- Split execution into PR, nightly, and release tiers
- Keep PR tier focused on deterministic fast checks
- Route broader integration/e2e/perf checks to scheduled tiers
- Use directory-based workflow routing where repository boundaries are clear
- Run `pre-commit` hooks as a fast PR-tier quality gate
- Use explicit pipeline contracts for pass/fail criteria
- Capture pipeline timings and adjust tier boundaries iteratively

## Rules

- PR pipeline must finish within an agreed latency budget
- Nightly pipeline must cover broad cross-layer scenarios
- Release pipeline must enforce full gating for publish readiness
- Critical-path suites run in both PR and release tiers
- Every gate must map to a documented quality risk
- Apply path filters only when ownership and dependency boundaries are explicit
- Keep a fallback full-repo validation path (nightly or manual) to catch cross-directory coupling
- Keep `pre-commit` hook execution consistent between local developer workflow and CI

## Patterns

- PR: lint + unit + focused integration
- Nightly: full integration + e2e + extended compatibility
- Release: full matrix + packaging + publish checks
- Reusable job templates with shared setup actions
- Directory-scoped workflow triggers (for example docs-only, Python-only, native-only paths)
- Changed-files routing to activate only relevant jobs in monorepo-style layouts
- CI step: `pre-commit run --all-files` or path-scoped hooks for fast feedback

## Anti-patterns

- Running every suite on every PR without prioritization
- Undefined pass criteria for release gates
- Flaky suites in required PR checks without quarantine strategy
- Pipeline drift from repository test taxonomy
- Path filters that skip required validation for shared dependencies
- Directory-only routing without periodic full-graph test coverage
- Different hook definitions between `.pre-commit-config.yaml` and CI execution scripts
