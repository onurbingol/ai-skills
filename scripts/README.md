# Scripts

Very brief usage notes for script-based workflows in this repository.

## Skill Review With Ollama

Run from repository root:

```bash
python scripts/execute_skill.py . \
  --skill python_testing \
  --prompt "Review this file for test quality"
```

Default behavior:

- Includes AGENTS.ollama.md and AGENTS.md (if present) in prompt context.
- If --file is omitted, uses bootstrap file(s) resolved from --skill as target file(s).
- You can still pass one or more --file values for specific files to review.

If Ollama is running elsewhere or you want a different model, set:

```bash
export OLLAMA_API_URL="http://localhost:11434/v1/chat/completions"
export OLLAMA_MODEL="qwen3.5:0.8b"
```

Environment variables used by scripts/docker-compose.yml:

- OLLAMA_API_URL: OpenAI-compatible Ollama endpoint used by the review script.
- OLLAMA_MODEL: Model name passed to the API.
- SKILL_KEY: Default skill key for compose-based review runs.
- REVIEW_PROMPT: Default review task prompt for compose-based review runs.
- TARGET_FILE: Optional target file path; when set, compose includes --file <TARGET_FILE>.

You can also run via Docker Compose:

```bash
docker compose -f scripts/docker-compose.yml run --rm skill-review
```

Inline env-var one-liner examples:

```bash
OLLAMA_MODEL="gpt-oss:latest" docker compose -f scripts/docker-compose.yml run --rm skill-review
```

```bash
SKILL_KEY="engineering_review" REVIEW_PROMPT="Review architecture risks" docker compose -f scripts/docker-compose.yml run --rm skill-review
```

```bash
SKILL_KEY="python_testing" TARGET_FILE="README.md" docker compose -f scripts/docker-compose.yml run --rm skill-review
```

Alternatives without setting environment variables:

```bash
docker compose -f scripts/docker-compose.yml run --rm skill-review \
  python scripts/execute_skill.py /workspace \
  --skill python_testing \
  --prompt "Review this file for test quality" \
  --file README.md
```

```bash
docker compose -f scripts/docker-compose.yml run --rm \
  --entrypoint python skill-review \
  scripts/execute_skill.py /workspace \
  --skill engineering_review \
  --prompt "Review this file for architecture and maintainability"
```
