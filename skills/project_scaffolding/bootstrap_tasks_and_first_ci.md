# Skill: Bootstrap Tasks and First CI

## Goal

Define initial automation tasks and a first CI pipeline that proves repository health on every change.

## Techniques

- Start from install, lint, and test as baseline CI stages.
- Create explicit task labels for local parity with CI steps.
- Fail fast on syntax and formatting before expensive jobs.
- Publish test and lint artifacts for debugging failed runs.
- Expand matrix coverage only after baseline reliability is stable.

## Rules

- CI should validate the same commands contributors run locally.
- Keep the first pipeline simple, deterministic, and well documented.
- Add cache strategy only after correctness is proven without cache.
- In hybrid repos, run language-specific jobs and a boundary integration job.
- Treat flaky jobs as incidents; do not normalize rerun-only success.

## Patterns

- Three-stage baseline: `setup`, `quality`, `tests`.
- Task parity pattern: Make targets or script aliases mapped 1:1 to CI steps.
- Artifact pattern: upload logs and coverage summaries for failed jobs.
- Progressive hardening pattern: add type checks, sanitizer jobs, and nightly depth over time.

## Anti-patterns

- Shipping with no CI gate on pull requests.
- CI workflows that diverge from local contributor commands.
- Adding many optional jobs before stabilizing core checks.
- Silent test failures from ignored exit codes or swallowed output.
- Relying on a single broad job that hides failure source.
