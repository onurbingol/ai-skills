# Skill: CI Caching, Artifacts, and Failure Triage

## Goal

Improve CI reliability and speed with safe caching, useful artifacts, and rapid failure diagnosis.

## Techniques

- Cache dependency and build layers with explicit cache keys
- Emit artifacts for failed runs (logs, reports, test outputs)
- Separate cache invalidation strategy by language/toolchain
- Add failure summary section to aid first-response triage
- Track flaky tests and isolate them with quarantine process

## Rules

- Cache keys must include lockfiles/toolchain signatures
- Never cache mutable runtime outputs without versioned keys
- Failed jobs must publish enough artifacts for offline diagnosis
- Keep artifact retention aligned with debugging needs and cost
- Treat repeated flaky failures as backlog items with ownership

## Patterns

- Python cache keyed by lockfile and Python version
- C++ cache keyed by compiler, flags, and dependency versions
- Upload failing test XML/log bundle for quick inspection
- Failure labels for infra issue vs code regression vs flaky test

## Anti-patterns

- Broad cache keys that mask dependency changes
- No artifacts for intermittent failures
- Re-running pipelines without first-pass triage evidence
- Ignoring recurring flaky failures in required gates
