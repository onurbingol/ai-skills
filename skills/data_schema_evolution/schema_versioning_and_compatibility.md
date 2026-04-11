# Skill: Schema Versioning and Compatibility

## Goal

Define durable schema versioning and compatibility policy for persisted structured data.

## Techniques

- Assign explicit schema versions with documented compatibility contract.
- Classify changes as additive, transitional, or breaking.
- Maintain compatibility test fixtures across version boundaries.
- Use feature flags or capability negotiation for staged adoption.
- Track read and write paths separately during transitions.

## Rules

- Every persisted schema change must declare compatibility impact.
- Breaking changes require migration path and rollback strategy.
- Readers should tolerate known older versions within policy window.
- Version checks must fail clearly when unsupported data is encountered.
- CI should include compatibility tests for current and previous supported versions.

## Patterns

- Semantic schema version policy with explicit support window.
- Compatibility matrix pattern: producer version x consumer version.
- Expand-and-contract pattern for non-breaking rollout.
- Contract tests that load historical serialized fixtures.

## Anti-patterns

- Implicit schema changes with no version increment.
- Breaking serialization format without migration tooling.
- Deleting compatibility code before all deployments are upgraded.
- Assuming backward compatibility without fixture validation.
- Coupling schema policy to one runtime language implementation.
