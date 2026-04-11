# Skill: Review Comment Response Workflow

## Goal

Resolve review feedback clearly with traceable changes and minimal churn.

## Techniques

- Triage comments into accept, clarify, or defer
- Batch related fixes into coherent commits
- Link each addressed comment to concrete code change
- Provide rationale when retaining existing implementation
- Re-run affected tests and summarize outcomes

## Rules

- Respond to every substantive comment
- Keep thread resolution tied to a verifiable change
- Avoid partial fixes without explicit follow-up issue
- Preserve reviewer context when force-pushing updates
- Close threads only after validation is complete

## Patterns

- Comment response template: concern, change, validation
- Mapping table: comment -> file -> test evidence
- Follow-up issue creation for deferred non-blockers
- Changelog note for externally visible behavior shifts

## Anti-patterns

- Marking threads resolved without code or rationale
- Bundling unrelated refactors into review fix commits
- Ignoring requested tests or validation details
- Repeating identical clarifications across multiple threads
