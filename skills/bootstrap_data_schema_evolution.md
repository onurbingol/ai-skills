# Bootstrap: Cross-Cutting Data and Schema Evolution Skills

Version: 1.0 | Last Updated: 2026-04-14

## Purpose

Use this entry point for projects with persisted structured state that requires versioning, migration, and operational safeguards.

## Apply These Skill Areas

- `skills/data_schema_evolution/`

## Priority Order

1. `skills/data_schema_evolution/schema_versioning_and_compatibility.md`
2. `skills/data_schema_evolution/migration_design_and_rollout.md`
3. `skills/data_schema_evolution/backfill_validation_and_recovery.md`

## Execution Defaults

- Define schema compatibility policy before writing migrations.
- Roll out migration paths incrementally with explicit guardrails.
- Validate post-migration correctness with measurable checks.

## Conditional Use Notes

- Apply this pack only when persistent structured data exists.
- For transient in-memory state, prefer existing development and testing packs.
