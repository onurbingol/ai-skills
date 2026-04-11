# Skill: Container Images and Devcontainers

## Goal

Use container images and devcontainers to standardize build, test, and developer environments when environment drift is a real risk.

## Techniques

- Create minimal, reproducible Docker images for CI build and test jobs
- Use multi-stage Docker builds to separate build-time and runtime layers
- Define explicit Docker build targets (for example `base`, `development`, `test`, `runtime`)
- Add devcontainer definitions for onboarding and local parity with CI
- Configure devcontainers to use a dedicated development build target when available
- Pin base image families and critical tool versions
- Reuse the same task commands across CI and devcontainer workflows
- Offer a full-container CI execution mode for complex build/test/release command stacks

## Rules

- Introduce containers only where they reduce measurable setup or drift problems
- Keep images deterministic with explicit dependency sources and versions
- Keep Docker contexts small and scoped to required files
- Run security scanning and vulnerability checks for maintained images
- Ensure devcontainer configuration matches CI-critical toolchain expectations
- Keep development-target tooling out of runtime images unless explicitly required
- Reuse shared base stages to avoid drift between development/test/runtime targets
- In full-container CI mode, keep host-run setup minimal and execute primary steps inside containers

## Patterns

- Multi-stage Dockerfile with build, test, and runtime targets
- Add a `development` target with debugging and interactive tooling for local/devcontainer use
- Set devcontainer `build.target` to the Dockerfile development target
- Language-specific base images with project overlays
- Devcontainer setup with post-create command for project bootstrap
- Directory-scoped image builds in mono-repo or multi-package layouts
- CI full-container option using `job.container` or `docker compose run` for build/test/publish stages

## Anti-patterns

- Single oversized image for unrelated pipelines
- Floating dependency behavior without lockfiles or pins
- Devcontainer configs that diverge from CI build assumptions
- Rebuilding images on every run without cache strategy
- Separate Dockerfiles for CI and devcontainer with duplicated dependency logic
- Mixing host and container execution arbitrarily in the same job without explicit boundary rationale
