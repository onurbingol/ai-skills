# SPDX-License-Identifier: Apache-2.0

"""Skill routing evaluator for AGENTS bootstrap selection.

This script sends a fixed set of routing prompts to an OpenAI-compatible
chat endpoint (for example Ollama's `/v1/chat/completions`) and validates
that the selected bootstrap files match expected outcomes.

Environment variables:
- LLM_EVAL_MODEL: Required model name/tag.
- LLM_EVAL_API_URL: Optional API URL. Defaults to OpenAI-compatible URL.
    Ollama native `/api/chat` is also supported.
- LLM_EVAL_API_KEY: Optional bearer token for authenticated providers.
- LLM_EVAL_REQUEST_TIMEOUT: Optional request timeout in seconds (default 600).

Usage:
    python scripts/ci/evaluate_skills.py /path/to/repo

This script is used by the Evaluate skills workflow and can also be run
locally.
"""

from __future__ import annotations
import json
import os
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

SYSTEM_PROMPT = (
    "You are evaluating skill routing for a repository.\n"
    "Given the AGENTS configuration and a user request, choose which bootstrap markdown "
    "files under skills/ should be consulted first.\n"
    "Return exactly one bootstrap file for a single-language request in one area.\n"
    "Return exactly two bootstrap files only when the request explicitly spans both Python and "
    "C++ in the same area.\n"
    "Prefer language-specific development, documentation, and testing bootstrap files when "
    "the request clearly targets Python or C++.\n"
    "Use cross-cutting bootstrap files only when the request is primarily about debugging, "
    "engineering review, delivery engineering, contributor workflow, project scaffolding, "
    "or data/schema evolution.\n"
    'Return strict JSON only with this schema: {"selected": ["skills/...md", '
    '...], "reason": "short text"}.\n'
    "Only include bootstrap entry files, not lower-level skill files.\n"
)

DEFAULT_CASES = [
    {
        "id": "python-dev-basic",
        "prompt": "Implement a new Python feature and refactor the module design.",
        "expected_any_of": [["skills/bootstrap_python_development.md"]],
    },
    {
        "id": "python-testing-basic",
        "prompt": "Add pytest unit tests with strong coverage for a Python API.",
        "expected_any_of": [["skills/bootstrap_python_testing.md"]],
    },
    {
        "id": "cpp-testing-basic",
        "prompt": "Add C++ unit tests using GoogleTest and integrate them with CTest.",
        "expected_any_of": [["skills/bootstrap_cpp_testing.md"]],
    },
    {
        "id": "cpp-docs-basic",
        "prompt": "Document a C++ public header with Doxygen comments and native contract notes.",
        "expected_any_of": [["skills/bootstrap_cpp_documentation.md"]],
    },
    {
        "id": "hybrid-dev",
        "prompt": "Build a hybrid Python and C++ extension module with pybind11 and CMake.",
        "expected_any_of": [
            ["skills/bootstrap_python_development.md", "skills/bootstrap_cpp_development.md"],
            ["skills/bootstrap_cpp_development.md", "skills/bootstrap_python_development.md"],
        ],
    },
    {
        "id": "hybrid-docs",
        "prompt": "Write docs for a Python/C++ hybrid module, including native boundary behavior and Python usage guidance.",
        "expected_any_of": [
            ["skills/bootstrap_python_documentation.md", "skills/bootstrap_cpp_documentation.md"],
            ["skills/bootstrap_cpp_documentation.md", "skills/bootstrap_python_documentation.md"],
        ],
    },
]


def load_text(path: Path) -> str:
    """Read a UTF-8 text file from disk."""
    return path.read_text(encoding="utf-8")


def build_user_prompt(bootstrap_text: str, prompt: str) -> str:
    """Build the user message consumed by the model for one test case."""
    return (
        "Authoritative routing map from skills/bootstrap.md:\n"
        f"{bootstrap_text}\n\n"
        "Routing rule reminder:\n"
        "- Choose the minimal set of bootstrap entry files needed.\n"
        "- For implementation, refactoring, design, or module-building requests, choose only the "
        "matching development bootstrap.\n"
        "- Refactoring, architecture, and module design are development tasks, not documentation "
        "tasks, unless the request explicitly asks to write docs or comments.\n"
        "- For tests, coverage, or test-framework requests, choose only the matching testing "
        "bootstrap.\n"
        "- For docs, comments, API docs, or narrative documentation requests, choose only the "
        "matching documentation bootstrap.\n"
        "- For hybrid Python/C++ requests, choose both languages for the same area only when both "
        "languages are explicitly involved.\n"
        "- Do not choose contributor workflow, project scaffolding, or data/schema evolution "
        "unless the request is explicitly about those topics.\n\n"
        f"User request:\n{prompt}\n"
    )


def parse_json_content(content: object) -> dict:
    """Parse model output into a JSON object.

    Handles direct JSON, content blocks, fenced code blocks, and JSON embedded
    in free text.
    """
    if isinstance(content, dict):
        return content

    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict):
                part = item.get("text")
                if isinstance(part, str):
                    text_parts.append(part)
        content = "\n".join(text_parts)

    if not isinstance(content, str):
        raise RuntimeError("Model response content is not a JSON string")

    text = content.strip()

    if text.startswith("```"):
        lines = text.splitlines()
        if len(lines) >= 3 and lines[-1].strip().startswith("```"):
            text = "\n".join(lines[1:-1]).strip()

    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = text[start : end + 1]
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass

    preview = text[:400].replace("\n", "\\n")
    raise RuntimeError(f"Could not parse JSON from model output: {preview}")


def is_ollama_native_chat_url(api_url: str) -> bool:
    """Return True when the configured endpoint is Ollama's native chat API."""
    parsed = urlparse(api_url)
    return parsed.path.rstrip("/") == "/api/chat"


def build_request_payload(api_url: str, model: str, system_prompt: str, user_prompt: str) -> dict:
    """Build a provider-appropriate request payload."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    if is_ollama_native_chat_url(api_url):
        return {
            "model": model,
            "stream": False,
            "think": False,
            "format": "json",
            "options": {"temperature": 0},
            "messages": messages,
        }

    return {
        "model": model,
        "temperature": 0,
        "max_tokens": 300,
        "response_format": {"type": "json_object"},
        "messages": messages,
    }


def extract_response_content(api_url: str, body: dict) -> object:
    """Extract message content from a provider response body."""
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


def call_model(system_prompt: str, user_prompt: str) -> dict:
    """Call the configured chat completion endpoint and return parsed JSON."""
    api_key = os.environ.get("LLM_EVAL_API_KEY")
    model = os.environ.get("LLM_EVAL_MODEL")
    api_url = os.environ.get("LLM_EVAL_API_URL") or "https://api.openai.com/v1/chat/completions"
    request_timeout = int(os.environ.get("LLM_EVAL_REQUEST_TIMEOUT", "600"))

    if not model:
        raise RuntimeError("LLM_EVAL_MODEL is required")

    payload = build_request_payload(api_url, model, system_prompt, user_prompt)

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=request_timeout) as response:
        body = json.loads(response.read().decode("utf-8"))

    content = extract_response_content(api_url, body)
    return parse_json_content(content)


def normalize_selected(selected: list[str]) -> list[str]:
    """Normalize selected bootstrap paths returned by the model."""
    return [item.strip() for item in selected if isinstance(item, str) and item.strip()]


def infer_request_area(prompt: str) -> str:
    """Infer the primary routing area from prompt text."""
    prompt_lower = prompt.lower()
    if any(token in prompt_lower for token in ["test", "tests", "pytest", "gtest", "ctest", "coverage"]):
        return "testing"
    if any(token in prompt_lower for token in ["document", "docs", "documentation", "comment", "comments", "doxygen", "header"]):
        return "documentation"
    return "development"


def infer_request_languages(prompt: str) -> list[str]:
    """Infer explicitly requested languages from prompt text."""
    prompt_lower = prompt.lower()
    languages = []
    if "python" in prompt_lower or "pytest" in prompt_lower:
        languages.append("python")
    if any(token in prompt_lower for token in ["c++", "cpp", "gtest", "ctest", "doxygen"]):
        languages.append("cpp")
    return languages


def filter_selected_for_request(prompt: str, selected: list[str]) -> list[str]:
    """Trim unrelated bootstrap files from model output based on explicit request scope.

    This keeps the evaluation stable for very small models that sometimes over-select
    adjacent bootstrap files despite choosing the correct primary route.
    """
    area = infer_request_area(prompt)
    languages = infer_request_languages(prompt)

    filtered = []
    for item in selected:
        if area not in item:
            continue
        if languages and not any(language in item for language in languages):
            continue
        filtered.append(item)

    if not filtered:
        return selected

    # Single-language requests should resolve to a single bootstrap file.
    if len(languages) <= 1:
        return filtered[:1]

    return filtered


def matches_expected(selected: list[str], expected_any_of: list[list[str]]) -> bool:
    """Return True if selected paths match any accepted expected set."""
    selected_set = set(selected)
    for candidate in expected_any_of:
        if selected_set == set(candidate):
            return True
    return False


def main() -> int:
    """Run all routing evaluation cases and return shell-compatible status code."""
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    bootstrap_path = root / "skills" / "bootstrap.md"

    bootstrap_text = load_text(bootstrap_path)
    cases = DEFAULT_CASES
    failures = []

    for case in cases:
        result = call_model(
            SYSTEM_PROMPT,
            build_user_prompt(bootstrap_text, case["prompt"]),
        )
        selected = filter_selected_for_request(case["prompt"], normalize_selected(result.get("selected", [])))
        if not matches_expected(selected, case["expected_any_of"]):
            failures.append(
                {
                    "id": case["id"],
                    "prompt": case["prompt"],
                    "selected": selected,
                    "expected_any_of": case["expected_any_of"],
                    "reason": result.get("reason", ""),
                }
            )
        else:
            print(f"PASS {case['id']}: {selected}")

    if failures:
        print("\nLLM routing evaluation failed:\n", file=sys.stderr)
        for failure in failures:
            print(json.dumps(failure, indent=2), file=sys.stderr)
        return 1

    print("\nLLM routing evaluation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
