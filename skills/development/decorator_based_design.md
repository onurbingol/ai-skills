# Skill: Decorator-Based Design

## Goal

Handle cross-cutting concerns without polluting core logic.

## Techniques

- Input validation
- Logging
- Caching
- Performance tracking

## Rules

- Keep decorators generic and reusable
- Do not embed business logic in decorators
- Stack decorators when needed

## Patterns

- @validate_input
- @log_call
- @cache_result

## Anti-patterns

- Duplicating logic across functions
- Mixing concerns inside core methods
