# Skill: Behavior-Oriented API Design

## Goal

Design APIs around actions, not data.

## Techniques

- Methods represent meaningful operations
- Avoid exposing raw data structures
- Prefer verb-based names: compute(), evaluate(), transform()
- Avoid generic names: process(), handle()
- Use explicit module boundaries for public vs internal APIs
- Use keyword-based constructors for forward compatibility

## Rules

- Keep APIs intuitive
- Hide implementation details
- Maintain consistency
- Separate public modules from internal modules (e.g., _internal.py)
- Keep internal symbols out of default imports
- Prefer explicit export lists for stable APIs
- Document accepted keyword arguments
- Keep optional behaviors opt-in via named parameters

## Patterns

- Behavior-oriented public methods over raw data access
- Stable facade modules over internal implementations

## Anti-patterns

- Getter/setter-only classes
- Data dumping APIs
- Leaking private modules as public contract
