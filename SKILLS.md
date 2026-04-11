# SKILLS

Guide for creating and maintaining skill packs in this repository.

## Contributor Quickstart

If you are adding a new skill and want the shortest path:

1. Pick the right domain folder under `skills/`.
2. Create one markdown file using the required template sections.
3. Add it to the relevant `bootstrap_*.md` priority list.
4. If you introduced a new category, add routing in `AGENTS.md`.
5. Run quick checks (search for stale paths, list bootstraps, inspect inventory).

This guide is written to be clear, practical, and easy to scan for anyone extending the skill system.

## Purpose

Use this document when adding, updating, or reviewing skills so all packs stay consistent, routable, and useful.

## Skill Design Principles

- Keep each skill focused on one clear concern.
- Prefer actionable rules over abstract advice.
- Include language and hybrid notes only when they affect behavior.
- Keep overlap explicit: define which skill owns which decision.

## Required Skill Template

Every skill file must include these sections in order:

- Goal
- Techniques
- Rules
- Patterns
- Anti-patterns

## Definition of Done (For Any New Skill/Pack)

- Follows the shared template (Goal, Techniques, Rules, Patterns, Anti-patterns)
- Includes language-specific defaults where relevant
- Includes hybrid module notes where boundaries matter
- Includes CI/validation guidance when operational impact exists
- Added to appropriate bootstrap priority order
- Routed through `AGENTS.md` when category-level discovery is required

## Authoring Workflow

- Step 1: Choose domain and ownership.
  - Decide where the skill belongs (language-specific or cross-cutting).
  - Avoid adding new top-level domains unless current ones are insufficient.

- Step 2: Create the skill file.
  - Place it under the appropriate folder in skills.
  - Use concise, policy-oriented bullets.
  - Add concrete operational defaults where needed.

- Step 3: Integrate with routing.
  - Add the skill to the correct bootstrap file priority order.
  - Update AGENTS.md if a new bootstrap category is introduced.

- Step 4: Validate consistency.
  - Confirm naming follows current conventions.
  - Confirm section order and wording style match existing skills.
  - Confirm no stale path references after renames.

- Step 5: Review for operational readiness.
  - Ensure CI and validation guidance exists where relevant.
  - Ensure risk-heavy changes include blocker-level criteria.
  - Ensure hybrid boundaries are explicit when Python/C++ interfaces are involved.

## Naming Conventions

- Domain folders: snake_case, short, explicit.
- Skill files: descriptive snake_case names.
- Bootstrap files: bootstrap_<domain>.md.
- Keep terms stable once routed in AGENTS.md.

## Bootstrap Rules

- Bootstrap purpose should define when to use the pack.
- Priority order should go from strategic to tactical.
- Keep list focused; avoid excessive low-value entries.
- Refresh Last Updated when meaningful routing changes occur.

## AGENTS Routing Rules

- AGENTS.md should expose only stable entry points.
- Cross-cutting categories should use explicit names.
- If local overrides are needed, use AGENTS.local.md.

## Suggested Review Checklist for New Skills

- Template complete (Goal/Techniques/Rules/Patterns/Anti-patterns).
- Scope is clear and non-duplicative.
- Language-specific defaults are included where needed.
- Hybrid notes are present where boundaries matter.
- CI validation guidance exists for operational concerns.
- Skill is wired into bootstrap priority.
- AGENTS mapping is updated when applicable.

## Common Mistakes

- Adding a skill file without bootstrap integration.
- Creating broad "catch-all" skills with unclear ownership.
- Mixing policy and implementation details without boundary.
- Renaming folders/files without updating AGENTS and bootstrap paths.
- Treating packaging/build/container changes as non-critical review areas.

## Optional: Lightweight Validation Command Set

Run these checks before finalizing major skill edits:

```bash
# find legacy names or stale references
rg "old_name|deprecated_path" .

# list current bootstrap files
ls skills/bootstrap_*.md

# inspect domain inventory
find skills -maxdepth 2 -type f | sort
```

## Change Management

- Keep edits incremental and reviewable.
- Prefer one domain migration per change set.
- Record major taxonomy changes in .plans when useful.
