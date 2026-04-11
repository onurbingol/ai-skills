# Skill: Hybrid Module Development (Python + C++)

## Goal

Design maintainable, testable, and packaging-friendly hybrid modules across Python and native C++ layers.

## Techniques

- Define explicit ownership boundaries between Python and C++ layers
- [Python] Keep orchestration, workflow composition, and user-facing API behavior in Python
- [C++] Keep performance-critical kernels and low-level algorithms in native code
- [Boundary] Keep binding glue thin and separate from domain logic
- [Build] Use CMake + scikit-build-core as the canonical native build bridge
- [Binding] Prefer pybind11 for C++-first modules; allow Cython for justified Python-first flows
- [Boundary] Keep type conversion paths explicit and measurable

## Rules

- Choose one primary binding approach per extension module and document rationale
- [Python] Do not encode ABI/compiler assumptions in Python business logic
- [C++] Keep public native interfaces stable and compatibility policy explicit
- [Boundary] Keep exception and error mapping explicit across language boundaries
- [Boundary] Document ownership and lifetime for cross-language objects
- [Build] Keep one native build path only; avoid parallel ad hoc pipelines

## Patterns

- Thin binding layer over stable native service interfaces
- Clear split: Python orchestrates workflows; C++ handles performance-critical kernels
- Dedicated adapter modules for conversion and boundary validation
- Build metadata in pyproject, tool configs separate by default
- Native tests for boundary/ABI-sensitive paths plus Python tests for workflows

## Anti-patterns

- Mixing pybind11 and Cython in one extension without documented necessity
- Embedding business rules inside binding glue code
- Implicit conversion behavior with hidden ownership semantics
- Python-only tests for modules with non-trivial native behavior
- Multiple competing native build paths in one project
