# Skill: Initial Tooling and Configs

## Goal

Establish minimal, high-value tooling defaults for formatting, linting, testing, and static validation.

## Techniques

- Select one formatter and one linter per language.
- Define test entry points with predictable local and CI invocation.
- Centralize configuration where tool ecosystems support it.
- Add pre-commit hooks for fast local quality feedback.
- Pin critical tooling versions for reproducibility.

## Rules

- Tooling must reduce ambiguity, not add overlapping checks.
- Keep defaults strict enough to prevent drift, but practical for iteration speed.
- Document the canonical command set in repository docs.
- In hybrid repositories, define separate Python and native check workflows.
- Validate configuration changes in CI before relying on them as gates.

## Patterns

- Baseline stack pattern: formatter, linter, test runner, type/static checker.
- Single-command onboarding pattern: one command to run core quality checks.
- Config ownership pattern: one file per tool, minimal duplicated settings.
- Hook layering pattern: fast checks locally, exhaustive checks in CI.

## Anti-patterns

- Multiple tools with overlapping responsibilities and conflicting output.
- Undocumented ad hoc scripts as the only way to run checks.
- Enabling heavy checks in pre-commit that make local loop unusable.
- Unpinned toolchain versions that produce non-reproducible lint diffs.
- Native toolchain requirements hidden from contributor documentation.
