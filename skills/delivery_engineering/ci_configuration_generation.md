# Skill: CI Configuration Generation

## Goal

Generate maintainable CI workflow configurations with clear triggers, secure defaults, and predictable execution.

## Techniques

- Define workflow structure by intent (validate, build, release, maintenance)
- Use explicit trigger policies (`pull_request`, `push`, `workflow_dispatch`, `schedule`)
- Configure path-based execution where ownership boundaries are clear
- Use reusable workflows and composite actions for repeated job logic
- Prefer containerized job execution when host setup is brittle or commands are complex

## Rules

- Keep workflow permissions least-privilege by default
- Pin action versions and avoid mutable references
- Document required checks and branch protection alignment
- Use concurrency controls to cancel stale runs where appropriate
- When using full-container CI mode, ensure build/test/release commands are encapsulated in versioned images or targets

## Patterns

- One workflow per concern with shared reusable building blocks
- PR workflow: fast gates, deterministic checks, path-aware job routing
- Release workflow: full matrix plus packaging/publish checks
- Manual workflow (`workflow_dispatch`) for on-demand heavy or diagnostic runs
- Full-container CI mode: `job.container` or `docker compose run` for all major steps

## Anti-patterns

- Monolithic workflow with mixed responsibilities and unclear ownership
- Broad triggers that waste CI capacity without better risk coverage
- Unpinned third-party actions in required gates
- Host-dependent scripts when containerized equivalents already exist
