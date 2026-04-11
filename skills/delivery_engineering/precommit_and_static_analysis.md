# Skill: Pre-commit and Static Analysis Integration

## Goal

Establish a consistent pre-commit and static-analysis baseline that runs locally and in CI with the same behavior.

## Techniques

- Start with default pre-commit hygiene hooks as baseline policy
- Add `ruff` for Python linting and formatting through pre-commit
- Add language/file analyzers by file type (Dockerfile, shell, YAML, Markdown, GitHub Actions)
- Keep hook versions pinned and update on a scheduled cadence
- Run pre-commit in both changed-files mode (local) and all-files mode (CI)

## Rules

- Keep `.pre-commit-config.yaml` as the single source of hook truth
- Prefer built-in/default hook sets before adding custom scripts
- Python default lint/format path: `ruff` and `ruff-format`
- Dockerfile linting must be enabled when Dockerfiles exist (prefer `hadolint`)
- Add analyzers only where file types are present in the repository

## Patterns

- Baseline hooks: whitespace, EOF fixer, merge-conflict checks, YAML/JSON/TOML validity
- Python hooks: `ruff`, `ruff-format`
- Docker hooks: `hadolint`
- Additional optional hooks: `shellcheck`, `yamllint`, `markdownlint`, `actionlint`
- CI step: `pre-commit run --all-files` with cached hook environments

## Anti-patterns

- Different hook sets between developer machines and CI
- Unpinned hook revisions causing non-reproducible lint behavior
- Python lint policy split across incompatible tools without rationale
- Ignoring Dockerfile linting while building/publishing container images
