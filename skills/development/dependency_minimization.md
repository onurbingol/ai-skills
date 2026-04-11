# Skill: Dependency Minimization

## Goal

Keep core system lightweight and portable.

## Techniques

- Prefer type hints + explicit checks first
- Use dataclasses + __post_init__ for lightweight model validation
- Use pydantic only at external I/O boundaries when richer parsing is required
- Isolate optional integrations behind adapters
- Use `pyproject.toml` as the canonical build metadata entry point for pure Python projects
- For Python projects with native code, prefer CMake + scikit-build-core as the build bridge
- For C++ hybrid bindings, default to pybind11; allow Cython by explicit module-level rationale

## Rules

- Avoid unnecessary external libraries
- Isolate optional dependencies
- Use standard library when possible
- Treat `pyproject.toml` as mandatory for modern Python packaging/build configuration
- Keep tool configurations in dedicated files by default (for example `.ruff.toml`, `mypy.ini`, `pytest.ini`)
- Only place tool config in `pyproject.toml` when a separate file is not supported or causes clear operational friction
- Keep build tooling centralized: avoid multiple competing native build paths
- Avoid dual binding stacks in a single extension module unless technically required and documented

## Patterns

- optional imports
- adapter wrappers
- dataclass-first core models
- boundary adapters for optional validation frameworks
- `pyproject.toml` for build-system and package metadata
- separate tool config files for linting, typing, formatting, and test runners
- pyproject-based native builds through scikit-build-core
- pybind11-based C++ bindings for C++-first modules
- Cython-based bindings for Python-first typed wrapper flows
- CTest-compatible native test execution when C++ components exist

## Anti-patterns

- heavy framework coupling
- hidden dependencies
- core domain logic tightly coupled to optional validation libraries
- storing all tool settings in one oversized `pyproject.toml` without clear justification
- mixing setuptools custom build glue and ad hoc CMake scripts without one canonical path
