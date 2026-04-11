# Bootstrap: Cross-Cutting Project Scaffolding Skills

Version: 1.0 | Last Updated: 2026-04-14

## Purpose

Use this entry point when creating a new repository or standardizing layout, tooling, and first-pipeline defaults.

## Apply These Skill Areas

- `skills/project_scaffolding/`

## Priority Order

1. `skills/project_scaffolding/repository_layout_blueprints.md`
2. `skills/project_scaffolding/initial_tooling_and_configs.md`
3. `skills/project_scaffolding/bootstrap_tasks_and_first_ci.md`

## Execution Defaults

- Start with a minimal, explicit repository topology.
- Add tooling only when ownership and operational value are clear.
- Land a first CI pass that proves install, lint, and test loops.

## Hybrid Boundary Notes

- For Python + C++ repositories, separate native and Python surfaces early.
- Keep packaging, build, and test concerns distinct from domain logic.
