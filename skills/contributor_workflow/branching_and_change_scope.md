# Skill: Branching and Change Scope

## Goal

Establish branch and scope discipline so each change set is easy to review, test, and rollback.

## Techniques

- Create one branch per coherent intent with a short, explicit name.
- Define non-goals before coding to avoid scope drift.
- Split large work into stacked or sequenced branches.
- Isolate refactors from behavior changes when both are needed.
- Capture expected verification outcomes up front.

## Rules

- Keep branch scope traceable to one problem statement.
- Avoid mixing bug fixes, refactors, and feature work in one branch.
- Rebase or merge frequently enough to minimize integration surprises.
- If branch lifetime grows, split work into independently mergeable slices.
- For hybrid repositories, separate native ABI-impacting work from Python-only changes unless tightly coupled.

## Patterns

- Branch naming pattern: `type/short-intent`.
- Scope statement pattern: `in-scope`, `out-of-scope`, `validation`.
- Stacked delivery pattern: foundation branch then incremental dependent branches.
- Minimal diff pattern: mechanical edits in one commit, semantic edits in another.

## Anti-patterns

- Long-lived branches with unrelated changes.
- Hidden scope expansion during review.
- Branch names that do not describe intent.
- Mixing generated files and source refactors without clear separation.
- Treating integration conflicts as a final-step activity.
