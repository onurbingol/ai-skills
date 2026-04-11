# Skill: Python Inline Documentation (Google Style)

## Goal

Produce clear, structured, and complete docstrings for all public Python APIs.

## Techniques

- Use Google-style docstrings for public classes, functions, methods, and non-trivial properties
- Keep summary lines imperative and behavior-focused
- Document args, returns, raises, and examples with semantic meaning
- Prefer runnable examples for non-trivial behavior
- Keep Python-facing semantics explicit for hybrid modules

## Rules

- Document all public API parameters, including kwargs semantics
- Describe meaning and constraints, not only type information
- Document intentional exceptions and triggering conditions
- If behavior changes, update docstrings in the same PR
- Validate examples in CI (doctest/snippet policy)

## Patterns

- Standard Google sections: `Args`, `Returns`, `Raises`, `Example`
- Summary line starts with a verb (for example: Compute, Evaluate, Return)
- Complex return structures include shape/schema notes
- Hybrid modules: Python docstrings define usage semantics and user-facing behavior

## Anti-patterns

- Missing `Args`/`Returns` for public APIs
- Repeating signatures without semantic explanation
- Vague descriptions (for example: "Gets value")
- Stale examples that do not run
