# AGENTS

Use these bootstrap entry points under `skills/`.

---

## Configuration Resolution

This project supports local overrides via `AGENTS.local.md`.

Resolution order (later overrides earlier):

1. This file (`AGENTS.md`) — base configuration
2. `AGENTS.local.md` — optional local overrides (gitignored)

Rules:

- If `AGENTS.local.md` exists, it is applied on top of this file
- Local definitions override base definitions when conflicts occur
- Local overrides must not remove core architectural constraints unless explicitly intended

---

## Bootstrap Routing

See `skills/bootstrap.md` for canonical bootstrap entry mappings.

### Stable Cross-Cutting Categories

- Contributor Workflow -> `skills/bootstrap_contributor_workflow.md`
- Project Scaffolding -> `skills/bootstrap_project_scaffolding.md`
- Data and Schema Evolution -> `skills/bootstrap_data_schema_evolution.md`

---

## Extension Mechanism

`AGENTS.local.md` may:

- Override existing skill mappings
- Add new languages or categories
- Adjust priorities or workflows

Example overrides:

- Replace Python documentation style
- Add experimental testing strategies
- Introduce project-specific skills

---

## Notes

- Keep this file stable and shared across the repository
- Use `AGENTS.local.md` for personal or environment-specific customization
- See `SKILLS.md` for skill authoring and validation workflow
