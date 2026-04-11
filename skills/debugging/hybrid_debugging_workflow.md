# Skill: Hybrid Boundary Debugging Workflow

## Goal

Isolate faults in Python/C++ hybrid modules by separating boundary failures from layer-internal failures.

## Techniques

- Reproduce in Python-facing test and native-facing test independently
- Trace data marshaling at boundary (types, ownership, shape, encoding)
- Validate native contract assumptions with focused C++ tests
- Validate Python API contract with focused pytest tests
- Use boundary-level logging to align Python call context with native execution

## Rules

- Identify failing layer first: Python surface, binding layer, or native core
- Keep ownership and lifetime assumptions explicit during triage
- Avoid duplicate assertions across layers; assign one owner per check
- Confirm fix from both directions (Python caller and C++ boundary tests)
- Record boundary contract change when behavior changes

## Patterns

- Paired repros: one pytest case plus one native unit case
- Boundary checklist: nullability, shape/size, encoding, ownership, exception mapping
- Golden error mapping tests for native-to-Python exceptions
- Regression tests at boundary and behavior layers

## Anti-patterns

- Treating boundary crashes as pure Python bugs
- Fixing only one side of a dual-surface contract
- Silent coercion that hides contract mismatches
- Debugging without a clear layer attribution
