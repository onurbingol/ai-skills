# Bootstrap: Python Development Skills

Version: 1.0 | Last Updated: 2026-04-10

## Purpose

Use this entry point when working on Python implementation tasks.

## Apply These Skill Areas

- `skills/development/`

## Priority Order

1. `skills/development/layered_architecture.md`
2. `skills/development/solid_principles.md`
3. `skills/development/hybrid_module_development.md`
4. `skills/development/extendible_design_by_composition.md`
5. `skills/development/validation.md`
6. `skills/development/dependency_minimization.md`
7. `skills/development/api_design.md`
8. `skills/development/controlled_attribute_access.md`
9. `skills/development/decorator_based_design.md`
10. `skills/development/python_dunder_protocol.md`
11. `skills/development/object_lifecycle_and_state_management.md`
12. `skills/development/algorithm_injection_pattern.md`
13. `skills/development/module_api_surface_management.md`

## Python-Specific Defaults

- Use `pyproject.toml` as mandatory package/build metadata entry point.
- Keep tool configs separate by default (`pytest.ini`, `mypy.ini`, `.ruff.toml`).
- Prefer dataclasses for structured internal models before adding heavy dependencies.
- Keep public APIs explicit and stable.

## Hybrid Build Notes

- If native modules exist, prefer CMake + scikit-build-core as the canonical bridge.
- Keep build/tooling concerns outside business logic modules.

## Hybrid Binding Policy (Python Side)

- Default choice for C++-first hybrid modules: pybind11.
- Use Cython when the module is Python-first and benefits from typed Python syntax,
  or when an existing Cython codebase is already established.
- Do not enforce one binding tool universally; choose one per module and document
  the rationale.
- Avoid mixing pybind11 and Cython in the same extension module unless there is a
  clear, documented need.
