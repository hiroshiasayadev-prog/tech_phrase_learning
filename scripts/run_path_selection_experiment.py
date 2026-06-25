from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


DEFAULT_BASE_URL = "http://192.168.11.22:11434"
DEFAULT_MODEL = "gpt-oss:20b"
DEFAULT_PATH = [1, 2, 4, 7]
EXPERIMENT_DIR = Path(
    "product/fixture/experiments/gpt-oss-20b/conversation-path-selection"
)
QUOTE_RE = re.compile(r"\[quote=.*?\bpost:(\d+)\b.*?\]", re.IGNORECASE)
QUOTE_BLOCK_RE = re.compile(
    r"\[quote=.*?\].*?\[/quote\]",
    re.IGNORECASE | re.DOTALL,
)


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_posts(topic: dict[str, Any]) -> list[dict[str, Any]]:
    stream = topic.get("post_stream", {})
    posts = stream.get("posts")
    ids = stream.get("stream")
    if not isinstance(posts, list) or not isinstance(ids, list):
        raise ValueError("Invalid post_stream")

    by_id = {
        post["id"]: post
        for post in posts
        if isinstance(post, dict) and isinstance(post.get("id"), int)
    }
    missing = [post_id for post_id in ids if post_id not in by_id]
    if missing:
        raise ValueError(f"Incomplete snapshot; missing post IDs: {missing}")
    return sorted((by_id[post_id] for post_id in ids), key=lambda x: x["post_number"])


def quote_targets(raw: str) -> list[int]:
    result: list[int] = []
    for value in QUOTE_RE.findall(raw):
        number = int(value)
        if number not in result:
            result.append(number)
    return result


def authored_text(raw: str) -> tuple[str, bool]:
    without_quotes, count = QUOTE_BLOCK_RE.subn("", raw)
    return without_quotes.strip(), count > 0


def build_tree(posts: list[dict[str, Any]]) -> dict[str, Any]:
    numbers = {int(post["post_number"]) for post in posts}
    root = 1 if 1 in numbers else min(numbers)
    nodes = []

    for post in posts:
        number = int(post["post_number"])
        reply = post.get("reply_to_post_number")
        reply = reply if isinstance(reply, int) else None
        if number == root:
            parent, reason = None, "opening_post"
        elif reply in numbers:
            parent, reason = reply, "explicit_reply"
        elif reply is None:
            parent, reason = root, "topic_level_projection"
        else:
            parent, reason = root, "missing_reply_target_projection"

        raw = post.get("raw")
        if not isinstance(raw, str):
            raise ValueError(f"Post #{number} has no raw text")
        nodes.append(
            {
                "post_number": number,
                "username": post.get("username"),
                "explicit_reply_to": reply,
                "quote_targets": quote_targets(raw),
                "projected_parent": parent,
                "projection_reason": reason,
            }
        )
    return {"root_post_number": root, "nodes": nodes}


def render_tree(
    tree: dict[str, Any],
    summaries: dict[int, dict[str, Any]] | None = None,
) -> str:
    nodes = {node["post_number"]: node for node in tree["nodes"]}
    children: dict[int, list[int]] = {}
    for node in tree["nodes"]:
        parent = node["projected_parent"]
        if parent is not None:
            children.setdefault(parent, []).append(node["post_number"])
    for values in children.values():
        values.sort()

    lines: list[str] = []

    def visit(number: int, prefix: str, last: bool, root: bool = False) -> None:
        connector = "" if root else ("└─ " if last else "├─ ")
        label = f"#{number} @{nodes[number]['username']}"
        if summaries:
            label += f" — {summaries[number]['summary']}"
        lines.append(prefix + connector + label)
        next_prefix = prefix if root else prefix + ("   " if last else "│  ")
        values = children.get(number, [])
        for index, child in enumerate(values):
            visit(child, next_prefix, index == len(values) - 1)

    visit(tree["root_post_number"], "", True, True)
    return "\n".join(lines)


def reduce_source(raw: str, limit: int) -> tuple[str, bool]:
    if len(raw) <= limit:
        return raw, False
    head = int(limit * 0.7)
    return (
        raw[:head]
        + "\n\n[... middle omitted by experiment script ...]\n\n"
        + raw[-(limit - head) :],
        True,
    )


def fill_prompt(path: Path, placeholder: str, value: Any) -> str:
    template = path.read_text(encoding="utf-8")
    if placeholder not in template:
        raise ValueError(f"{path} does not contain {placeholder}")
    return template.replace(
        placeholder,
        json.dumps(value, ensure_ascii=False, indent=2),
    )


def resolve_model(session: requests.Session, base_url: str, requested: str) -> tuple[str, list[str]]:
    response = session.get(f"{base_url}/api/tags", timeout=15)
    response.raise_for_status()
    names = [
        item["name"]
        for item in response.json().get("models", [])
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    ]
    if requested in names:
        return requested, names

    key = re.sub(r"[^a-z0-9]", "", requested.lower())
    matches = [
        name
        for name in names
        if re.sub(r"[^a-z0-9]", "", name.lower()) == key
        or (
            "gptoss" in re.sub(r"[^a-z0-9]", "", name.lower())
            and "20b" in re.sub(r"[^a-z0-9]", "", name.lower())
            and "gptoss" in key
            and "20b" in key
        )
    ]
    if len(matches) == 1:
        return matches[0], names
    raise ValueError(f"Model {requested!r} not found. Installed models: {names}")


def call_ollama(
    session: requests.Session,
    *,
    base_url: str,
    model: str,
    think: str | None,
    temperature: float,
    keep_alive: str,
    timeout: float,
    prompt: str,
    schema: dict[str, Any],
    output_prefix: Path,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Preserve source stance and uncertainty. "
                    "Return only schema-valid JSON."
                ),
            },
            {
                "role": "user",
                "content": (
                    prompt
                    + "\n\nReturn JSON matching this schema:\n"
                    + json.dumps(schema, ensure_ascii=False, indent=2)
                ),
            },
        ],
        "stream": False,
        "format": schema,
        "options": {"temperature": temperature},
        "keep_alive": keep_alive,
    }
    if think:
        payload["think"] = think

    write_json(output_prefix.with_suffix(".request.json"), payload)
    response = session.post(
        f"{base_url}/api/chat",
        json=payload,
        timeout=timeout,
    )
    if not response.ok:
        write_text(output_prefix.with_suffix(".response.txt"), response.text)
        raise RuntimeError(
            f"Ollama HTTP {response.status_code}: {response.text[:500]}"
        )

    body = response.json()
    write_json(output_prefix.with_suffix(".response.json"), body)
    content = body.get("message", {}).get("content")
    if not isinstance(content, str):
        raise ValueError("Ollama response has no message.content")

    parsed = json.loads(content)
    if not isinstance(parsed, dict):
        raise ValueError("Ollama structured output is not an object")
    write_json(output_prefix.with_suffix(".parsed.json"), parsed)
    return parsed


def validate_path(
    path: Any,
    tree: dict[str, Any],
    rejected_alternatives: Any,
) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(path, list) or not all(isinstance(x, int) for x in path):
        return {"passed": False, "errors": ["Path is not an integer list"]}

    parents = {
        node["post_number"]: node["projected_parent"]
        for node in tree["nodes"]
    }
    known_posts = set(parents)
    if not 2 <= len(path) <= 6:
        errors.append("Path length must be 2 to 6")
    if not path or path[0] != tree["root_post_number"]:
        errors.append("Path does not start at the opening post")
    if len(path) != len(set(path)):
        errors.append("Path contains duplicate posts")
    for parent, child in zip(path, path[1:]):
        if parents.get(child) != parent:
            errors.append(f"#{parent} -> #{child} is not a coarse-tree edge")

    if not isinstance(rejected_alternatives, list):
        errors.append("rejected_alternatives is not a list")
        rejected_numbers: list[int] = []
    else:
        rejected_numbers = [
            item.get("post_number")
            for item in rejected_alternatives
            if isinstance(item, dict) and isinstance(item.get("post_number"), int)
        ]
        if len(rejected_numbers) != len(rejected_alternatives):
            errors.append("A rejected alternative has no integer post_number")

    overlap = sorted(set(path) & set(rejected_numbers))
    if overlap:
        errors.append(f"Selected posts also appear as rejected: {overlap}")
    unknown = sorted(set(rejected_numbers) - known_posts)
    if unknown:
        errors.append(f"Rejected alternatives are not in the tree: {unknown}")
    if len(rejected_numbers) != len(set(rejected_numbers)):
        errors.append("rejected_alternatives contains duplicate posts")

    return {
        "passed": not errors,
        "errors": errors,
        "path": path,
        "rejected_post_numbers": rejected_numbers,
    }


def compare_paths(selected: list[int], expected: list[int]) -> dict[str, Any]:
    prefix = 0
    for left, right in zip(selected, expected):
        if left != right:
            break
        prefix += 1
    return {
        "selected_path": selected,
        "expected_path": expected,
        "exact_match": selected == expected,
        "common_prefix_length": prefix,
        "shared_posts": [x for x in selected if x in expected],
        "selected_only": [x for x in selected if x not in expected],
        "expected_only": [x for x in expected if x not in selected],
    }


def validate_summary_result(
    result: dict[str, Any],
    post_number: int,
    source_text: str,
) -> list[str]:
    errors: list[str] = []
    if result.get("post_number") != post_number:
        errors.append(
            f"post_number must be {post_number}, got {result.get('post_number')!r}"
        )

    summary = result.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        errors.append("summary must be a non-empty string")

    candidates = result.get("phrase_candidates")
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= 3:
        errors.append("phrase_candidates must contain 1 to 3 items")
        return errors

    for index, candidate in enumerate(candidates, start=1):
        if not isinstance(candidate, dict):
            errors.append(f"phrase candidate {index} is not an object")
            continue
        text = candidate.get("text")
        function = candidate.get("function")
        if not isinstance(text, str) or not text:
            errors.append(f"phrase candidate {index} has empty text")
        elif text not in source_text:
            errors.append(
                f"phrase candidate {index} is not an exact authored-text substring: {text!r}"
            )
        if not isinstance(function, str) or not function.strip():
            errors.append(f"phrase candidate {index} has empty function")

    return errors


def validate_evaluation_coverage(
    evaluation: dict[str, Any],
    expected_posts: list[int],
) -> dict[str, Any]:
    reviews = evaluation.get("summary_reviews")
    if not isinstance(reviews, list):
        return {
            "passed": False,
            "errors": ["summary_reviews is not a list"],
            "reviewed_post_numbers": [],
            "expected_post_numbers": expected_posts,
        }

    reviewed = [
        item.get("post_number")
        for item in reviews
        if isinstance(item, dict) and isinstance(item.get("post_number"), int)
    ]
    errors: list[str] = []
    if len(reviewed) != len(reviews):
        errors.append("A summary review has no integer post_number")
    if reviewed != expected_posts:
        errors.append(
            f"Review coverage/order mismatch: expected {expected_posts}, got {reviewed}"
        )
    if len(reviewed) != len(set(reviewed)):
        errors.append("summary_reviews contains duplicate post numbers")

    return {
        "passed": not errors,
        "errors": errors,
        "reviewed_post_numbers": reviewed,
        "expected_post_numbers": expected_posts,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize a Discourse topic and select one learning path."
    )
    parser.add_argument("--source", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--base-url",
        default=os.environ.get("OLLAMA_BASE_URL", DEFAULT_BASE_URL),
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OLLAMA_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument(
        "--think",
        choices=["none", "low", "medium", "high"],
        default="medium",
    )
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--keep-alive", default="30m")
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument("--max-post-chars", type=int, default=20_000)
    parser.add_argument(
        "--summary-retries",
        type=int,
        default=2,
        help="Retry a post summary after deterministic validation failure.",
    )
    parser.add_argument("--expected-path", type=int, nargs="+", default=DEFAULT_PATH)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parent.parent
    source = (
        args.source
        or repo / "product/fixture/golden/topic-107565/source-topic.raw.json"
    ).resolve()
    topic = read_json(source)
    post_list = load_posts(topic)
    posts = {int(post["post_number"]): post for post in post_list}
    tree = build_tree(post_list)
    nodes = {node["post_number"]: node for node in tree["nodes"]}

    output = (
        args.output_dir
        or repo / ".tmp/conversation-path-selection" / f"topic-{topic['id']}"
    ).resolve()
    if args.summary_retries < 0:
        raise ValueError("--summary-retries must be zero or greater")

    if output.exists() and any(output.iterdir()):
        if not args.force:
            raise FileExistsError(f"{output} is not empty; use --force")
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    prompt_dir = repo / EXPERIMENT_DIR
    summary_prompt = prompt_dir / "post-summary-prompt-v3-authored-text.md"
    path_prompt = prompt_dir / "path-selection-prompt-v3-authored-phrase-evidence.md"
    evaluation_prompt = prompt_dir / "automated-evaluation-prompt-v3-complete-coverage.md"
    summary_schema = read_json(prompt_dir / "post-summary-v3.schema.json")
    path_schema = read_json(prompt_dir / "path-selection-v3.schema.json")
    evaluation_schema = read_json(prompt_dir / "automated-evaluation-v3.schema.json")

    write_json(output / "coarse-tree.json", tree)
    write_text(output / "coarse-tree.md", render_tree(tree) + "\n")

    session = requests.Session()
    base_url = args.base_url.rstrip("/")
    model = args.model
    installed: list[str] = []
    if not args.prepare_only:
        model, installed = resolve_model(session, base_url, model)

    manifest = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "topic_id": topic["id"],
        "source": str(source),
        "source_sha256": sha256(source),
        "expected_path": args.expected_path,
        "ollama": {
            "base_url": base_url,
            "requested_model": args.model,
            "resolved_model": model,
            "installed_models": installed,
            "think": None if args.think == "none" else args.think,
            "temperature": args.temperature,
            "keep_alive": args.keep_alive,
            "summary_retries": args.summary_retries,
        },
        "prompt_sha256": {
            path.name: sha256(path)
            for path in (
                summary_prompt,
                path_prompt,
                evaluation_prompt,
                prompt_dir / "post-summary-v3.schema.json",
                prompt_dir / "path-selection-v3.schema.json",
                prompt_dir / "automated-evaluation-v3.schema.json",
            )
        },
        "prepare_only": args.prepare_only,
    }
    write_json(output / "run-manifest.json", manifest)

    summaries: dict[int, dict[str, Any]] = {}
    warnings: list[str] = []
    for number in sorted(posts):
        own_text, quotes_removed = authored_text(posts[number]["raw"])
        if not own_text:
            raise ValueError(f"Post #{number} has no authored text after quote removal")
        reduced_text, truncated = reduce_source(own_text, args.max_post_chars)
        parent = nodes[number]["projected_parent"]
        summary_input = {
            "topic": {"id": topic["id"], "title": topic["title"]},
            "post": {
                **nodes[number],
                "authored_text": reduced_text,
                "authored_text_truncated": truncated,
                "quoted_blocks_removed": quotes_removed,
            },
            "context": {
                "projected_parent_summary": summaries.get(parent),
                "quote_target_summaries": [
                    summaries[target]
                    for target in nodes[number]["quote_targets"]
                    if target in summaries
                ],
            },
        }
        prefix = output / "summaries" / f"post-{number:03d}"
        write_json(prefix.with_suffix(".input.json"), summary_input)
        if args.prepare_only:
            continue

        base_summary_prompt = fill_prompt(
            summary_prompt,
            "{{POST_INPUT_JSON}}",
            summary_input,
        )
        result: dict[str, Any] | None = None
        validation_errors: list[str] = []
        accepted_attempt = 0

        for attempt in range(1, args.summary_retries + 2):
            retry_instruction = ""
            if validation_errors:
                retry_instruction = (
                    "\n\nThe previous output failed deterministic validation. "
                    "Regenerate the entire JSON object. Use shorter phrase candidates "
                    "copied character-for-character from authored_text. Do not shorten "
                    "or rewrite Markdown links, punctuation, emphasis markers, or code spans. "
                    "Prefer a different phrase without a Markdown link when practical.\n"
                    "Validation errors:\n"
                    + json.dumps(validation_errors, ensure_ascii=False, indent=2)
                )

            attempt_prefix = (
                output
                / "summaries"
                / f"post-{number:03d}-attempt-{attempt:02d}"
            )
            result = call_ollama(
                session,
                base_url=base_url,
                model=model,
                think=None if args.think == "none" else args.think,
                temperature=args.temperature,
                keep_alive=args.keep_alive,
                timeout=args.timeout,
                prompt=base_summary_prompt + retry_instruction,
                schema=summary_schema,
                output_prefix=attempt_prefix,
            )
            validation_errors = validate_summary_result(
                result,
                number,
                own_text,
            )
            write_json(
                attempt_prefix.with_suffix(".validation.json"),
                {
                    "passed": not validation_errors,
                    "errors": validation_errors,
                },
            )
            if not validation_errors:
                accepted_attempt = attempt
                break

        if result is None or validation_errors:
            raise ValueError(
                f"Summary for #{number} failed after "
                f"{args.summary_retries + 1} attempts: {validation_errors}"
            )

        write_json(
            prefix.with_suffix(".accepted.json"),
            {
                "accepted_attempt": accepted_attempt,
                "result": result,
            },
        )
        if len(str(result.get("summary", "")).split()) > 55:
            warnings.append(f"Summary for #{number} exceeds 55 words")

        summaries[number] = result

    if args.prepare_only:
        print(f"Prepared coarse tree and summary inputs: {output}")
        return 0

    write_json(
        output / "post-summaries.json",
        {
            "model": model,
            "summaries": [summaries[x] for x in sorted(summaries)],
            "warnings": warnings,
        },
    )
    summarized_tree = render_tree(tree, summaries)
    write_text(output / "summarized-tree.md", summarized_tree + "\n")

    path_input = {
        "topic": {"id": topic["id"], "title": topic["title"]},
        "root_post_number": tree["root_post_number"],
        "coarse_tree": summarized_tree,
        "posts": [
            {**nodes[number], **summaries[number]}
            for number in sorted(summaries)
        ],
    }
    write_json(output / "path-selection.input.json", path_input)
    path_result = call_ollama(
        session,
        base_url=base_url,
        model=model,
        think=None if args.think == "none" else args.think,
        temperature=args.temperature,
        keep_alive=args.keep_alive,
        timeout=args.timeout,
        prompt=fill_prompt(path_prompt, "{{TREE_INPUT_JSON}}", path_input),
        schema=path_schema,
        output_prefix=output / "path-selection" / "path-selection",
    )

    selected = path_result.get("selected_path")
    check = validate_path(
        selected,
        tree,
        path_result.get("rejected_alternatives"),
    )
    write_json(output / "path-validation.json", check)
    if not isinstance(selected, list) or not all(isinstance(x, int) for x in selected):
        raise ValueError("selected_path is not an integer list")

    comparison = compare_paths(selected, args.expected_path)
    write_json(output / "path-comparison.json", comparison)

    evaluation = None
    evaluation_check = {
        "passed": False,
        "errors": ["Automated evaluation was not run"],
        "reviewed_post_numbers": [],
        "expected_post_numbers": sorted(posts),
    }
    if check["passed"]:
        all_posts = []
        for number in sorted(posts):
            own_text, quotes_removed = authored_text(posts[number]["raw"])
            reduced_text, truncated = reduce_source(own_text, args.max_post_chars)
            all_posts.append(
                {
                    "post_number": number,
                    "selected": number in selected,
                    "username": posts[number]["username"],
                    "authored_text": reduced_text,
                    "authored_text_truncated": truncated,
                    "quoted_blocks_removed": quotes_removed,
                    "quote_targets": nodes[number]["quote_targets"],
                    "generated_summary": summaries[number],
                }
            )
        evaluation_input = {
            "topic": {"id": topic["id"], "title": topic["title"]},
            "selected_path": selected,
            "all_posts": all_posts,
        }
        write_json(output / "automated-evaluation.input.json", evaluation_input)
        evaluation = call_ollama(
            session,
            base_url=base_url,
            model=model,
            think=None if args.think == "none" else args.think,
            temperature=args.temperature,
            keep_alive=args.keep_alive,
            timeout=args.timeout,
            prompt=fill_prompt(
                evaluation_prompt,
                "{{EVALUATION_INPUT_JSON}}",
                evaluation_input,
            ),
            schema=evaluation_schema,
            output_prefix=output
            / "automated-evaluation"
            / "automated-evaluation",
        )
        evaluation_check = validate_evaluation_coverage(
            evaluation,
            sorted(posts),
        )
    write_json(output / "automated-evaluation-validation.json", evaluation_check)
    write_json(
        output / "automated-evaluation-summary.json",
        {
            "evaluation": evaluation,
            "coverage_validation": evaluation_check,
            "human_review_required": True,
        },
    )

    report = [
        f"# Path-selection experiment: topic {topic['id']}",
        "",
        f"- Topic: {topic['title']}",
        f"- Model: `{model}`",
        f"- Selected path: `{' -> '.join(f'#{x}' for x in selected)}`",
        f"- Valid coarse-tree path: `{check['passed']}`",
        f"- Complete automated-review coverage: `{evaluation_check['passed']}`",
        f"- Reference exact match: `{comparison['exact_match']}`",
        "",
        "## Summarized tree",
        "",
        "```text",
        summarized_tree,
        "```",
        "",
        "## Path rationale",
        "",
        str(path_result.get("path_summary", "")),
        "",
        "## Automated evaluation",
        "",
        "```json",
        json.dumps(evaluation, ensure_ascii=False, indent=2),
        "```",
        "",
        "This evaluation is model-generated. Human review remains required.",
        "",
    ]
    write_text(output / "report.md", "\n".join(report))

    manifest.update(
        {
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "selected_path": selected,
            "path_validation_passed": check["passed"],
            "evaluation_coverage_passed": evaluation_check["passed"],
            "reference_path_exact_match": comparison["exact_match"],
        }
    )
    write_json(output / "run-manifest.json", manifest)

    print(f"Experiment completed: {output}")
    print(f"Selected path: {selected}")
    print(f"Reference exact match: {comparison['exact_match']}")
    print(f"Report: {output / 'report.md'}")
    return 0 if check["passed"] and evaluation_check["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
