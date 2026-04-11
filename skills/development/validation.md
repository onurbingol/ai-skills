# Skill: Systematic Validation

## Goal

Ensure correctness at all boundaries.

## Techniques

- Input validation (public APIs)
- Internal validation (state changes)
- Interface validation (class contracts)
- Model validation (object construction and setters)
- Boundary validation (I/O adapters and external payloads)

## Rules

- Validate early
- Fail fast with clear errors
- Never assume correct input
- Define dependency ordering for fields
- Collect validation failures when practical
- Validation policy defines where and how data is validated
- Readiness guards only gate compute execution on already-built objects

## Patterns

- Model and boundary validation kept separate from compute execution
- Aggregated validation errors for faster correction loops

## Anti-patterns

- Silent failures
- Late validation
- Mixing boundary parsing concerns into core compute methods
