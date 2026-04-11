# Skill: Pull Request Hygiene and Review Readiness

## Goal

Prepare pull requests that minimize reviewer friction and maximize decision confidence.

## Techniques

- Provide a concise problem statement and change summary.
- Include explicit validation evidence (tests, lint, build, screenshots where applicable).
- Call out risk areas and rollback considerations.
- Separate mandatory review context from optional background.
- Keep PR size aligned to what reviewers can evaluate safely.

## Rules

- PR description must state expected behavior before and after change.
- Link related issues or design context when available.
- Mark breaking changes, migration requirements, and data impacts explicitly.
- Ensure CI is green or explain known, approved exceptions.
- Author-side readiness ends at a complete, verifiable PR; reviewer-side decisions are handled in `skills/engineering_review/`.

## Patterns

- Description pattern: `problem`, `approach`, `validation`, `risk`, `follow-ups`.
- Evidence pattern: map each claim to test output or observable result.
- Readiness checklist pattern: lint, tests, docs, changelog, migration notes.
- Scope control pattern: split oversized PRs into prerequisite and feature PRs.

## Anti-patterns

- Opening PRs with missing validation evidence.
- Forcing reviewers to infer behavior changes from raw diffs.
- Hiding unresolved TODOs in code without tracking.
- Rewriting PR scope mid-review without clear communication.
- Treating reviewer questions as optional unless formally blocking.
