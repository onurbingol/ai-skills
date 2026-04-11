# Skill: Risk-Based Review

## Goal

Assess release impact by ranking findings and validating mitigation depth.

## Techniques

- Score findings by severity, blast radius, and recoverability
- Separate safety, correctness, and operability risks
- Map each critical risk to required tests or runtime checks
- Gate merges on unresolved high-risk findings
- Document downgrade path or rollback plan for risky changes

## Rules

- High-risk changes require explicit validation evidence
- Security and data integrity risks are always blocking
- Performance-risk changes require benchmark comparison
- Hybrid boundary risks require dual-layer validation
- Keep risk log concise and decision-focused

## Patterns

- Severity rubric with examples for each tier
- Merge checklist for high-risk PRs
- Release note snippets for known residual risks
- Risk-to-test traceability matrix

## Anti-patterns

- Equal treatment of low and high impact findings
- Approving with unresolved blocker-level risks
- Missing rollback strategy for invasive changes
- Risk discussion without measurable validation criteria
