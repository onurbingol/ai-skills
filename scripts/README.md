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

`execute_skill.py` defaults to Ollama’s native chat API at `http://localhost:11434/api/chat`. Optional overrides when running on the host:

```bash
export OLLAMA_MODEL="qwen3.5:0.8b"
# Only if you use an OpenAI-compatible URL (for example some proxies or toolchains):
# export OLLAMA_API_URL="http://localhost:11434/v1/chat/completions"
```

Environment variables used by `scripts/docker-compose.yml` for the `skill-review` service:

- OLLAMA_API_URL: Default `http://ollama:11434/api/chat` (Ollama native); override if you need another base URL or an OpenAI-compatible path.
- OLLAMA_TIMEOUT: HTTP request timeout in seconds (default `600` = 10 minutes).
- OLLAMA_MODEL: Model name passed to the API.
- SKILL_KEY: Default skill key for compose-based review runs.
- REVIEW_PROMPT: Default review task prompt for compose-based review runs.
- TARGET_FILE: Optional target file path; when set, compose includes `--file <TARGET_FILE>`.

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
