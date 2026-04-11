# Skill: Migration Design and Rollout

## Goal

Design and execute schema migrations safely across environments with controlled risk.

## Techniques

- Choose offline, online, or dual-write migration based on scale and availability needs.
- Break migration into preparation, execution, and cleanup phases.
- Add observability for migration throughput, error rate, and lag.
- Gate rollout by environment and tenant or shard cohorts.
- Rehearse migrations on production-like snapshots before rollout.

## Rules

- Migration must be idempotent or explicitly checkpointed.
- Define abort criteria and rollback behavior before execution.
- Separate DDL changes from data backfill when operationally safer.
- For high-volume systems, enforce rate limiting to protect primary workloads.
- CI should verify migration scripts apply cleanly and support expected downgrade strategy when applicable.

## Patterns

- Two-step rollout: deploy compatibility code, then run migration.
- Shadow validation pattern: compare pre/post read models during rollout.
- Cohort rollout pattern with automatic pause on error threshold.
- Runbook pattern: prerequisites, commands, monitors, rollback actions.

## Anti-patterns

- One-shot migrations without dry-run evidence.
- Running irreversible transformations without backup snapshot.
- Coupling app deploy and full data rewrite in one risky window.
- Missing ownership and on-call coverage during critical rollout.
- Treating migration completion as success without correctness checks.
