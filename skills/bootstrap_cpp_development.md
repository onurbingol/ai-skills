# Bootstrap: C++ Development Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on C++ implementation tasks.

## Apply These Skill Areas

- `skills/development/`

## Priority Order

1. `skills/development/layered_architecture.md`
2. `skills/development/solid_principles.md`
3. `skills/development/hybrid_module_development.md`
4. `skills/development/interface_contact_enforcement.md`
5. `skills/development/extendible_design_by_composition.md`
6. `skills/development/validation.md`
7. `skills/development/dependency_minimization.md`
8. `skills/development/api_design.md`
9. `skills/development/controlled_attribute_access.md`
10. `skills/development/algorithm_injection_pattern.md`
11. `skills/development/module_api_surface_management.md`

## C++-Specific Defaults

- Prefer modern C++ style and explicit interfaces.
- Keep public headers minimal and stable; hide implementation details.
- Prefer composition over deep inheritance.
- Keep build-system concerns outside core logic.
- For Python bindings or hybrid modules, keep native boundaries explicit.

## Build and Tooling Guidance

- Prefer CMake as canonical build system.
- Keep one native build path only.
- Use clear module boundaries and avoid leaking compiler/build assumptions into core code.

## Python Binding Policy (C++ Side)

- Prefer pybind11 as the default binding layer for C++ hybrid modules.
- Pair pybind11 with CMake + scikit-build-core for build consistency.
- Allow Cython when integration constraints justify it (existing Cython surface,
  Python-first typed wrappers, or migration phases).
- Enforce consistency per module: one primary binding approach per extension.
