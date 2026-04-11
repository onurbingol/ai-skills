# Skill: Narrative Documentation (Tool-Agnostic)

## Goal

Create conceptual documentation that explains architecture, usage, and reasoning independent of any specific doc tool.

## Techniques

- Organize docs by conceptual layers (architecture, tutorials, examples, API orientation)
- Introduce concepts before code snippets
- Explain design intent, trade-offs, and boundaries
- Use diagrams when they reduce cognitive load
- Add module landing pages for fast navigation and onboarding
- [Python] Emphasize usage semantics, workflows, and integration patterns
- [C++] Emphasize contracts, constraints, ownership, and performance context

## Rules

- Every major module needs concept explanation plus at least one realistic usage path
- Narrative docs must stay aligned with current module boundaries and behavior
- Architecture/design changes require narrative updates in the same PR
- Keep docs concise and task-oriented; avoid API-dump pages
- [Python] User-facing workflows and examples should be runnable where practical
- [C++] Native behavior, constraints, and trade-offs must be explicit in prose

## Patterns

- `architecture/`, `tutorials/`, `examples/`, `module landing pages`
- "Why this exists" section for non-obvious components
- Cross-language sections for hybrid boundaries and behavior mapping
- Diagram sections for workflows, state transitions, and high-level component flow

## Anti-patterns

- Tool-generated pages presented as complete narrative docs
- No onboarding path for new contributors/users
- Design decisions undocumented outside code comments
- Narrative pages that duplicate full API references without guidance
