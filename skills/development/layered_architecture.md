# Skill: Layered System Architecture

## Goal

Separate system into clear layers.

## Techniques

- Core (business logic)
- Services (orchestration)
- Utilities (helpers)
- Integrations (external systems)
- Public facade modules over private implementation modules
- Build boundary: isolate native build orchestration from core domain logic

## Rules

- Core must not depend on outer layers
- Dependencies flow inward
- Keep layers loosely coupled
- Keep public APIs separate from private implementation modules
- Build-system details (CMake, compiler flags, wheel tooling) must stay outside core layers
- Keep packaging metadata (`pyproject.toml`) distinct from tool-specific runtime/lint/type/test configs

## Patterns

- Adapter pattern
- Facade pattern
- Public/private module split (_internal vs public facade)
- CMake-managed native components exposed to Python via scikit-build-core packaging layer
- Dedicated config files per tool to preserve separation of concerns

## Anti-patterns

- Circular dependencies
- Mixing I/O with core logic
- Importing private modules across layer boundaries
- leaking build-system assumptions into business logic modules
- coupling unrelated tool configuration and package metadata into one opaque config surface
