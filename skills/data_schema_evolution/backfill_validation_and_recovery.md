# Skill: Backfill Validation and Recovery

## Goal

Validate data backfills and provide fast recovery paths when correctness or performance regressions appear.

## Techniques

- Define deterministic success metrics before backfill starts.
- Use sampling plus aggregate parity checks for correctness.
- Track progress with checkpoints and resumable job state.
- Keep recovery artifacts (snapshots, change logs, replay tools) ready.
- Automate post-backfill invariants and anomaly detection.

## Rules

- Backfill completion requires correctness evidence, not only job completion.
- Recovery procedure must be documented, tested, and owned.
- Large backfills should support pause/resume without data duplication.
- Validate both data integrity and query/service performance impact.
- CI should include representative backfill tests or fixture-based validation for critical transformations.

## Patterns

- Dual validation pattern: row-count parity and semantic invariant checks.
- Checkpoint pattern with idempotent retries for partial failures.
- Recovery drill pattern performed before production backfill.
- Audit trail pattern linking transformed records to source lineage.

## Anti-patterns

- Declaring success without post-backfill integrity checks.
- Backfill jobs with no checkpointing or resume behavior.
- Ignoring downstream index, cache, or search consistency impacts.
- Manual recovery steps that are undocumented or untested.
- Deleting source fields before downstream consumers are confirmed updated.
