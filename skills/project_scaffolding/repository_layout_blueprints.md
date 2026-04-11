# Skill: Repository Layout Blueprints

## Goal

Create repository structures that scale from initial delivery to long-term maintenance without layout churn.

## Techniques

- Choose a top-level layout based on language boundaries and deployment model.
- Separate source, tests, docs, scripts, and automation concerns.
- Reserve dedicated folders for generated artifacts and caches.
- Establish explicit ownership boundaries for cross-cutting config.
- Encode module boundaries in folder layout, not only in naming.

## Rules

- Layout must make public API surfaces discoverable.
- Keep build and packaging files close to the components they govern.
- Do not mix runtime source and generated outputs.
- In hybrid modules, isolate native code, bindings, and Python package roots.
- Prefer conventional paths to reduce tooling customization overhead.

## Patterns

- Domain-first structure with feature-level grouping.
- Shared conventions folder for reusable workflow templates.
- Hybrid split pattern: `src/python`, `src/native`, `bindings`, `tests/python`, `tests/native`.
- Layer-preserving layout aligned to architecture boundaries.

## Anti-patterns

- Flat repositories with no ownership cues.
- Deep nesting that hides module intent.
- Co-locating build artifacts with authored source.
- Cross-language coupling through ad hoc relative imports.
- Overfitting layout to one tool's defaults at the expense of clarity.
