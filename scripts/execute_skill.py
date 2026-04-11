# SPDX-License-Identifier: Apache-2.0

"""Run skill-routed review prompts through an Ollama-compatible endpoint.

This utility resolves skill keys to bootstrap files, loads each bootstrap's
priority skill files, builds a single prompt, and sends it to a chat API.
It supports both OpenAI-compatible chat completions and Ollama's native
`/api/chat` endpoint.

Usage:
        python scripts/execute_skill.py /path/to/repo \
            --skill python_testing \
            --prompt "Review this module for test quality" \
            --file path/to/target.py
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


def snake_case(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_local_config(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    overrides: dict[str, str] = {}
    aliases: dict[str, str] = {}
    if not path.exists():
        return overrides, aliases

    current_section = ""
    for line in load_text(path).splitlines():
        heading = re.match(r"^##\s+(.+)$", line.strip())
        if heading:
            current_section = snake_case(heading.group(1))
            continue

        item = re.match(r"^-\s*([^:]+):\s*(.+)$", line.strip())
        if not item or not current_section:
            continue

        category = snake_case(item.group(1))
        target = item.group(2).strip()

        if current_section == "aliases":
            aliases[category] = snake_case(target)
            continue

        if current_section in {"cross_cutting", "crosscutting"}:
            key = category
        else:
            key = f"{current_section}_{category}"

        overrides[key] = target

    return overrides, aliases


def available_bootstrap_keys(root: Path) -> list[str]:
    keys = []
    for path in sorted((root / "skills").glob("bootstrap_*.md")):
        if path.name == "bootstrap.md":
            continue
        keys.append(path.stem.replace("bootstrap_", "", 1))
    return keys


def resolve_bootstrap_path(root: Path, key: str) -> Path:
    normalized = snake_case(key)
    local_overrides, local_aliases = parse_local_config(root / "AGENTS.local.md")

    if normalized in local_aliases:
        normalized = local_aliases[normalized]

    resolved: Path | None = None
    default_candidate = root / "skills" / f"bootstrap_{normalized}.md"
    if default_candidate.exists():
        resolved = default_candidate

    if normalized in local_overrides:
        override_candidate = (root / local_overrides[normalized]).resolve()
        try:
            override_candidate.relative_to(root.resolve())
        except ValueError as exc:
            raise RuntimeError(f"Invalid local override path for '{normalized}': {override_candidate}") from exc
        if not override_candidate.exists():
            raise RuntimeError(f"Local override target does not exist for '{normalized}': {override_candidate}")
        resolved = override_candidate

    if resolved is not None:
        return resolved

    candidates = sorted(set(available_bootstrap_keys(root) + list(local_overrides.keys()) + list(local_aliases.keys())))
    hints = difflib.get_close_matches(normalized, candidates, n=5)
    hint_text = ", ".join(hints) if hints else "none"
    raise RuntimeError(f"skill_not_found: {normalized}. nearest_valid_keys: {hint_text}")


def parse_priority_files(bootstrap_text: str) -> list[str]:
    results: list[str] = []
    for line in bootstrap_text.splitlines():
        m = re.match(r"^\d+\.\s+`([^`]+\.md)`\s*$", line.strip())
        if m:
            results.append(m.group(1))
    return results


def load_skill_context(root: Path, bootstrap_path: Path) -> tuple[str, list[tuple[str, str]]]:
    bootstrap_text = load_text(bootstrap_path)
    skill_paths = parse_priority_files(bootstrap_text)
    loaded: list[tuple[str, str]] = []

    for rel in skill_paths:
        candidate = (root / rel).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError as exc:
            raise RuntimeError(f"Invalid priority skill path: {rel}") from exc
        if not candidate.exists():
            raise RuntimeError(f"Priority skill file missing: {rel}")
        loaded.append((rel, load_text(candidate)))

    return bootstrap_text, loaded


def parse_model_content(content: object) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
        return "\n".join(parts)
    return str(content)


def is_ollama_native_chat_url(api_url: str) -> bool:
    """Return True when the configured endpoint is Ollama's native chat API."""
    parsed = urlparse(api_url)
    return parsed.path.rstrip("/") == "/api/chat"


def build_request_payload(api_url: str, model: str, prompt: str) -> dict:
    """Build a provider-appropriate request payload."""
    messages = [
        {
            "role": "system",
            "content": "You are a software reviewer. Follow the provided skill policies strictly and output findings ordered by severity.",
        },
        {"role": "user", "content": prompt},
    ]

    if is_ollama_native_chat_url(api_url):
        return {
            "model": model,
            "stream": False,
            "think": False,
            "options": {"temperature": 0},
            "messages": messages,
        }

    return {
        "model": model,
        "temperature": 0,
        "messages": messages,
    }


def extract_response_content(api_url: str, body: dict) -> object:
    """Extract response content from a provider response body."""
    if is_ollama_native_chat_url(api_url):
        return body.get("message", {}).get("content", "")

    choice = body["choices"][0]
    message = choice["message"]
    content = message.get("content", "")
    if content:
        return content

    finish_reason = choice.get("finish_reason", "")
    reasoning_preview = str(message.get("reasoning", ""))[:400].replace("\n", "\\n")
    raise RuntimeError(f"Model returned empty content (finish_reason={finish_reason!r}, reasoning_preview={reasoning_preview!r})")


def call_ollama(api_url: str, model: str, prompt: str, timeout: int) -> str:
    payload = build_request_payload(api_url, model, prompt)

    headers = {"Content-Type": "application/json"}
    api_key = os.environ.get("LLM_EVAL_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))

    content = extract_response_content(api_url, body)
    return parse_model_content(content)


def build_prompt(
    task: str,
    agents_specs: list[tuple[Path, str]],
    selected_bootstraps: list[Path],
    contexts: list[tuple[Path, str, list[tuple[str, str]]]],
    target_files: list[Path],
) -> str:
    lines: list[str] = []
    lines.append("Task:")
    lines.append(task)
    lines.append("")

    lines.append("Selected bootstrap files:")
    for path in selected_bootstraps:
        lines.append(f"- {path.as_posix()}")
    lines.append("")

    if agents_specs:
        lines.append("Routing specifications:")
        for spec_path, _ in agents_specs:
            lines.append(f"- {spec_path.as_posix()}")
        lines.append("")

        for spec_path, spec_text in agents_specs:
            lines.append(f"Routing spec: {spec_path.as_posix()}")
            lines.append(spec_text)
            lines.append("")

    for bootstrap_path, bootstrap_text, skills in contexts:
        lines.append(f"Bootstrap: {bootstrap_path.as_posix()}")
        lines.append(bootstrap_text)
        lines.append("")
        for rel, content in skills:
            lines.append(f"Skill: {rel}")
            lines.append(content)
            lines.append("")

    if target_files:
        lines.append("Target files:")
        for path in target_files:
            lines.append(f"- {path.as_posix()}")
        lines.append("")

        for path in target_files:
            lines.append(f"File content: {path.as_posix()}")
            lines.append(load_text(path))
            lines.append("")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """Parse CLI flags for skill selection, prompt, and target files."""
    parser = argparse.ArgumentParser(description="Run skill-routed review prompt through Ollama")
    parser.add_argument("root", nargs="?", default=".", help="Repository root path")
    parser.add_argument("--skill", action="append", required=True, help="Skill key. Repeatable.")
    parser.add_argument("--prompt", required=True, help="Review prompt/task")
    parser.add_argument(
        "--file",
        action="append",
        default=[],
        help=("Target file path(s) relative to repo. If omitted, the selected bootstrap files from --skill are used as target files."),
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OLLAMA_MODEL", "qwen3.5:0.8b"),
        help="Model name",
    )
    parser.add_argument(
        "--api-url",
        default=os.environ.get("OLLAMA_API_URL", "http://localhost:11434/api/chat"),
        help="Chat API URL. Supports Ollama native /api/chat and OpenAI-compatible endpoints.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("OLLAMA_TIMEOUT", "600")),
        help="Request timeout in seconds",
    )
    return parser.parse_args()


def main() -> int:
    """Resolve selected skills, call model API, and print review output."""
    args = parse_args()
    root = Path(args.root).resolve()

    agents_specs: list[tuple[Path, str]] = []
    for rel in ["AGENTS.ollama.md", "AGENTS.md"]:
        candidate = (root / rel).resolve()
        if candidate.exists() and candidate.is_file():
            agents_specs.append((candidate.relative_to(root), load_text(candidate)))

    skill_keys: list[str] = []
    for raw in args.skill:
        for part in raw.split(","):
            cleaned = snake_case(part)
            if cleaned:
                skill_keys.append(cleaned)

    if not skill_keys:
        raise RuntimeError("At least one --skill value is required")

    selected_bootstraps: list[Path] = []
    contexts: list[tuple[Path, str, list[tuple[str, str]]]] = []

    for key in skill_keys:
        bootstrap_path = resolve_bootstrap_path(root, key)
        bootstrap_text, skills = load_skill_context(root, bootstrap_path)
        selected_bootstraps.append(bootstrap_path.relative_to(root))
        contexts.append((bootstrap_path.relative_to(root), bootstrap_text, skills))

    target_files: list[Path] = []
    if args.file:
        for rel in args.file:
            candidate = (root / rel).resolve()
            try:
                candidate.relative_to(root)
            except ValueError as exc:
                raise RuntimeError(f"Invalid target file path: {rel}") from exc
            if not candidate.exists() or candidate.is_dir():
                raise RuntimeError(f"Target file does not exist: {rel}")
            target_files.append(candidate.relative_to(root))
    else:
        # Default to bootstrap files resolved from --skill when no target file is provided.
        target_files = list(dict.fromkeys(selected_bootstraps))

    prompt = build_prompt(args.prompt, agents_specs, selected_bootstraps, contexts, target_files)
    response = call_ollama(args.api_url, args.model, prompt, args.timeout)
    print(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
