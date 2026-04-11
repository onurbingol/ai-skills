# Skill: Code Review Checklist

## Goal

Provide consistent, risk-aware engineering reviews focused on correctness and regressions across code and delivery artifacts.

## Techniques

- Review in passes: correctness, edge cases, tests, maintainability
- Validate changed behavior against explicit acceptance criteria
- Trace inputs and outputs across modified boundaries
- Inspect error handling, defaults, and backward compatibility
- Verify tests reflect realistic and failure-path scenarios
- Confirm repository hygiene checks (for example `pre-commit`) match changed files
- Review packaging/build/runtime artifacts with the same rigor as source code

## Rules

- Prioritize high-severity findings first
- Require evidence for behavior-changing claims
- Flag missing regression tests for bug fixes
- Distinguish blocking issues from optional improvements
- Keep feedback actionable and tied to concrete code locations
- Require `pre-commit` configuration updates when introducing new lint/format policies
- Review changes in `pyproject.toml`, conda recipes, `CMakeLists.txt`, CPack configs, and Dockerfiles for reproducibility and release impact
- Treat packaging and container misconfiguration risks as blocker-level when they affect build, publish, or runtime safety

## Patterns

- Severity tiers: blocker, major, minor
- Risk matrix: user impact x probability
- Review notes grouped by behavior, safety, and test coverage
- Explicit list of assumptions and open questions
- PR evidence includes `pre-commit run --all-files` output (or equivalent CI status)
- Non-code checklist block for: packaging metadata, dependency pins, build-system flags, CPack outputs, Docker image behavior, and CI workflow contracts

## Anti-patterns

- Cosmetic-only review while logic risk is unassessed
- Vague feedback without reproduction path
- Approving behavior changes without test updates
- Mixing architectural debates into urgent bugfix review
- Treating local hook failures as optional while CI enforces the same checks
- Treating Dockerfiles and build/packaging configs as low-risk "ops-only" changes
