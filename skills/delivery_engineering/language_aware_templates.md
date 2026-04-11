# Skill: Language-Aware CI Templates

## Goal

Generate CI templates that respect Python, C++, and hybrid build/test realities.

## Techniques

- Use Python-specific jobs for packaging, linting, typing, and testing
- Use C++-specific jobs for CMake configure/build/test with CTest labels
- Add hybrid jobs for binding build, boundary tests, and wheel artifacts
- Use Docker multi-target builds to map job purpose (development/test/runtime)
- Include `pre-commit` jobs for cross-language formatting, lint, and policy hooks
- Keep shared setup modular and reusable across jobs
- Align CI commands with local developer commands

## Rules

- Python jobs use project-defined environment and test markers
- C++ jobs use explicit CMake presets/toolchains and deterministic flags
- Hybrid jobs validate both Python-facing and native-facing behavior
- Avoid hidden side effects between language-specific jobs
- Keep artifact naming consistent across matrix variants
- Prefer one Dockerfile per component with multiple targets over many near-duplicate Dockerfiles
- Hooks in `.pre-commit-config.yaml` must be executable in both local and CI environments
- Default Python pre-commit policy should use `ruff` (lint) and `ruff-format` (format)
- If Dockerfiles are present, include Dockerfile analysis in hook/CI policy (prefer `hadolint`)

## Patterns

- Matrix dimensions for OS, Python version, and compiler where required
- Separate smoke job for rapid PR feedback
- Dedicated native test job with sanitizer variant in nightly tier
- Hybrid packaging job using CMake + scikit-build-core when applicable
- CI jobs selecting Docker targets explicitly (for example `--target test` for validation jobs)
- Devcontainer using the same Dockerfile with `build.target=development` for local parity
- Dedicated `pre-commit` job reused across Python/C++/hybrid repositories
- Baseline pre-commit hooks from default rule sets (whitespace, EOF, merge-conflict, config-file validity)

## Anti-patterns

- One monolithic job for all languages and concerns
- Inconsistent commands between local and CI paths
- Missing native validation in hybrid modules
- Cross-job coupling through undocumented cache assumptions
- CI using `runtime` image for builds/tests when dedicated `test` target exists
- Defining hooks that only run in CI but are skipped locally
