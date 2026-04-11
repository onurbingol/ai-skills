# AGENTS for Ollama Routing

Portable routing spec for scripts that call models through Ollama.

## Input Contract

Input is one skill key or a list of skill keys.

Examples:

- python_development
- python_testing
- cpp_documentation
- engineering_review

## Output Contract

Return one or more bootstrap file paths under skills/.

If a key cannot be resolved, return an explicit error with nearest valid keys.

## Canonical Key Rules

- Step 1: Language key pattern:
  - <language>_<area>
  - Supported language values: python, cpp
  - Supported area values: development, documentation, testing

- Step 2: Cross-cutting key pattern:
  - debugging
  - engineering_review
  - delivery_engineering
  - contributor_workflow
  - project_scaffolding
  - data_schema_evolution

## Path Resolution Rule

Primary resolution is direct and deterministic:

- Step 1: Build candidate path from input key:
  - skills/bootstrap_<key>.md

- Step 2: If file exists, return it.

- Step 3: If file does not exist:
  - return: skill_not_found

Examples:

- python_testing -> skills/bootstrap_python_testing.md
- engineering_review -> skills/bootstrap_engineering_review.md
- contributor_workflow -> skills/bootstrap_contributor_workflow.md

## Local Override Loading

Use AGENTS.md as the base configuration source for override semantics.

Resolution order (later overrides earlier):

1. AGENTS.md (base)
2. AGENTS.local.md (optional, gitignored)

If AGENTS.local.md exists, apply it on top of base behavior.

Behavior:

- Local definitions override base definitions when conflicts occur.
- Local overrides must not remove core architectural constraints unless explicitly intended.
- Allow replacement of resolved bootstrap path for an existing key.
- Allow adding new keys from local categories.
- Allow optional local aliases via an `## Aliases` section in AGENTS.local.md.
- Reject absolute paths and path traversal values.

## Suggested Script Flow

1. Normalize input key(s) to lowercase snake_case.
2. Resolve candidate using direct lookup: skills/bootstrap_<key>.md.
3. If unresolved, return skill_not_found.
4. Apply local overrides and aliases from AGENTS.local.md using AGENTS.md override policy.
5. Load bootstrap and its Priority Order skill files.
6. Send only selected skill files as model context.

## Validation Rules

- Resolved bootstrap file must exist.
- Every Priority Order skill file must exist.
- Resolved path must remain under skills/.
