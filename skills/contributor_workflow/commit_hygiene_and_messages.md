# Skill: Commit Hygiene and Messages

## Goal

Produce commit history that is auditable, review-friendly, and operationally safe to revert.

## Techniques

- Use small, logically complete commits.
- Write imperative, intent-focused subject lines.
- Add body context for risk, rationale, and migration notes when needed.
- Stage selectively to avoid unrelated noise.
- Run relevant lint and tests before commit.

## Rules

- Every commit should compile or pass relevant checks in isolation where practical.
- Commit message subject should describe what changed and why at a high level.
- Include operational notes when change affects CI, release, or persisted data.
- Avoid empty phrasing such as "misc fixes" or "update".
- In hybrid repositories, mention layer impact explicitly (Python, binding, native).

## Patterns

- Subject pattern: `area: action with intent`.
- Body pattern: `context`, `change`, `validation`, `risk`.
- Safety pattern: run pre-commit hooks before finalizing.
- Revertability pattern: keep commits scoped so rollback does not drop unrelated work.

## Anti-patterns

- Squashing unrelated work into one large commit.
- Commit messages that only restate file names.
- Fixup chains merged without cleanup.
- Committing generated or lockfile churn without explanation.
- Skipping validation for changes that modify quality gates.
