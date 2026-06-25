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
DEFAULT_MODEL = "qwen3.6-27b:q4_k_m-tools"
EXPERIMENT_DIR = Path(
    "product/fixture/experiments/qwen3.6-27b/path-ranking"
)
DEFAULT_SOURCE_RUN = Path(
    "product/fixture/experiments/gpt-oss-20b/"
    "conversation-path-selection/runs/topic-107565-v3"
)

SCORE_WEIGHTS = {
    "conversation_coherence": 0.25,
    "reusable_phrase_value": 0.35,
    "cognitive_lightness": 0.15,
    "technical_detail_control": 0.10,
    "conversational_function_variety": 0.15,
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def fill_prompt(path: Path, placeholder: str, value: Any) -> str:
    template = path.read_text(encoding="utf-8")
    if placeholder not in template:
        raise ValueError(f"{path} does not contain {placeholder}")
    return template.replace(
        placeholder,
        json.dumps(value, ensure_ascii=False, indent=2),
    )


def model_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower().removesuffix(":latest"))


def lower_reasoning_effort(value: str | None) -> str | None:
    if value == "high":
        return "medium"
    if value == "medium":
        return "low"
    if value == "low":
        return None
    return None


def resolve_model(
    session: requests.Session,
    base_url: str,
    requested: str,
) -> tuple[str, list[str]]:
    response = session.get(f"{base_url}/api/tags", timeout=15)
    response.raise_for_status()
    names = [
        item["name"]
        for item in response.json().get("models", [])
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    ]
    if requested in names:
        return requested, names

    expected = model_key(requested)
    matches = [name for name in names if model_key(name) == expected]
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
    max_output_tokens: int,
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
                    "Act as an independent learning-path ranker. "
                    "Prioritize reusable conversational English over technical depth. "
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
        "options": {
            "temperature": temperature,
            "num_predict": max_output_tokens,
        },
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


def enumerate_paths(
    tree: dict[str, Any],
    min_posts: int,
    max_posts: int,
) -> list[list[int]]:
    root = tree.get("root_post_number")
    nodes = tree.get("nodes")
    if not isinstance(root, int) or not isinstance(nodes, list):
        raise ValueError("Invalid coarse tree")

    known = {
        node["post_number"]
        for node in nodes
        if isinstance(node, dict) and isinstance(node.get("post_number"), int)
    }
    if root not in known:
        raise ValueError("Coarse-tree root is missing from nodes")

    children: dict[int, list[int]] = {}
    for node in nodes:
        if not isinstance(node, dict):
            continue
        number = node.get("post_number")
        parent = node.get("projected_parent")
        if isinstance(number, int) and isinstance(parent, int):
            children.setdefault(parent, []).append(number)
    for values in children.values():
        values.sort()

    paths: list[list[int]] = []

    def visit(number: int, path: list[int]) -> None:
        if min_posts <= len(path) <= max_posts:
            paths.append(path.copy())
        if len(path) >= max_posts:
            return
        for child in children.get(number, []):
            if child in path:
                raise ValueError(f"Cycle detected at post #{child}")
            visit(child, [*path, child])

    visit(root, [root])
    paths.sort(key=lambda path: tuple(path))
    if not paths:
        raise ValueError("No candidate paths were enumerated")
    return paths


def path_text(path: list[int]) -> str:
    return " -> ".join(f"#{number}" for number in path)


def build_candidates(
    tree: dict[str, Any],
    summaries_doc: dict[str, Any],
    min_posts: int,
    max_posts: int,
    required_prefix: list[int] | None = None,
    required_post_count: int | None = None,
) -> list[dict[str, Any]]:
    nodes = {
        node["post_number"]: node
        for node in tree["nodes"]
        if isinstance(node, dict) and isinstance(node.get("post_number"), int)
    }
    summaries = {
        item["post_number"]: item
        for item in summaries_doc.get("summaries", [])
        if isinstance(item, dict) and isinstance(item.get("post_number"), int)
    }
    missing = sorted(set(nodes) - set(summaries))
    if missing:
        raise ValueError(f"Missing summaries for posts: {missing}")

    paths = enumerate_paths(tree, min_posts, max_posts)
    if required_prefix is not None:
        paths = [
            path
            for path in paths
            if path[: len(required_prefix)] == required_prefix
        ]
    if required_post_count is not None:
        paths = [path for path in paths if len(path) == required_post_count]
    if not paths:
        raise ValueError(
            "Candidate filters removed every path; check --required-prefix and "
            "--required-post-count"
        )

    candidates: list[dict[str, Any]] = []
    for index, path in enumerate(paths, start=1):
        posts = []
        functions: list[str] = []
        for number in path:
            summary = summaries[number]
            phrase_candidates = summary.get("phrase_candidates")
            if not isinstance(phrase_candidates, list):
                raise ValueError(f"Post #{number} has no phrase_candidates list")
            for phrase in phrase_candidates:
                if isinstance(phrase, dict) and isinstance(phrase.get("function"), str):
                    functions.append(phrase["function"])
            posts.append(
                {
                    "post_number": number,
                    "username": nodes[number].get("username"),
                    "summary": summary.get("summary"),
                    "conversational_intent": summary.get("conversational_intent"),
                    "stance": summary.get("stance"),
                    "technical_burden": summary.get("technical_burden"),
                    "phrase_learning_potential": summary.get(
                        "phrase_learning_potential"
                    ),
                    "phrase_candidates": phrase_candidates,
                }
            )

        candidates.append(
            {
                "candidate_id": f"P{index:03d}",
                "path": path,
                "path_text": path_text(path),
                "post_count": len(path),
                "distinct_phrase_functions": sorted(set(functions)),
                "posts": posts,
            }
        )
    return candidates


def weighted_score(scores: dict[str, Any]) -> float | None:
    values: list[float] = []
    for field, weight in SCORE_WEIGHTS.items():
        value = scores.get(field)
        if not isinstance(value, int) or not 1 <= value <= 5:
            return None
        values.append(value * weight)
    return round(sum(values), 3)


def validate_ranking(
    result: dict[str, Any],
    candidates: list[dict[str, Any]],
) -> dict[str, Any]:
    expected_ids = [candidate["candidate_id"] for candidate in candidates]
    expected_set = set(expected_ids)
    errors: list[str] = []

    ranked = result.get("ranked_candidates")
    if not isinstance(ranked, list):
        return {
            "passed": False,
            "errors": ["ranked_candidates is not a list"],
            "expected_candidate_ids": expected_ids,
            "returned_candidate_ids": [],
        }

    returned_ids: list[str] = []
    returned_ranks: list[int] = []
    derived_scores: dict[str, float | None] = {}
    for index, item in enumerate(ranked, start=1):
        if not isinstance(item, dict):
            errors.append(f"Ranking item {index} is not an object")
            continue
        candidate_id = item.get("candidate_id")
        rank = item.get("rank")
        if not isinstance(candidate_id, str):
            errors.append(f"Ranking item {index} has no candidate_id")
        else:
            returned_ids.append(candidate_id)
        if not isinstance(rank, int):
            errors.append(f"Ranking item {index} has no integer rank")
        else:
            returned_ranks.append(rank)
        scores = item.get("scores")
        if isinstance(candidate_id, str) and isinstance(scores, dict):
            derived_scores[candidate_id] = weighted_score(scores)
        elif isinstance(candidate_id, str):
            derived_scores[candidate_id] = None

    if len(ranked) != len(candidates):
        errors.append(
            f"Expected {len(candidates)} ranking items, got {len(ranked)}"
        )
    if set(returned_ids) != expected_set:
        errors.append(
            f"Candidate coverage mismatch: expected {expected_ids}, got {returned_ids}"
        )
    if len(returned_ids) != len(set(returned_ids)):
        errors.append("Candidate IDs are duplicated")

    expected_ranks = list(range(1, len(candidates) + 1))
    if sorted(returned_ranks) != expected_ranks:
        errors.append(
            f"Ranks must be exactly {expected_ranks}, got {returned_ranks}"
        )
    if len(returned_ranks) != len(set(returned_ranks)):
        errors.append("Ranks are duplicated")

    top_id = result.get("top_candidate_id")
    rank_one_ids = [
        item.get("candidate_id")
        for item in ranked
        if isinstance(item, dict) and item.get("rank") == 1
    ]
    if top_id not in expected_set:
        errors.append(f"Unknown top_candidate_id: {top_id!r}")
    if rank_one_ids != [top_id]:
        errors.append(
            f"top_candidate_id must equal the sole rank-1 candidate: {rank_one_ids}"
        )

    return {
        "passed": not errors,
        "errors": errors,
        "expected_candidate_ids": expected_ids,
        "returned_candidate_ids": returned_ids,
        "returned_ranks": returned_ranks,
        "derived_weighted_scores": derived_scores,
    }


def find_candidate_id(
    candidates: list[dict[str, Any]],
    path: list[int] | None,
) -> str | None:
    if path is None:
        return None
    for candidate in candidates:
        if candidate["path"] == path:
            return candidate["candidate_id"]
    return None


def ranking_position(result: dict[str, Any], candidate_id: str | None) -> int | None:
    if candidate_id is None:
        return None
    for item in result.get("ranked_candidates", []):
        if isinstance(item, dict) and item.get("candidate_id") == candidate_id:
            rank = item.get("rank")
            return rank if isinstance(rank, int) else None
    return None


def build_comparison(
    result: dict[str, Any],
    candidates: list[dict[str, Any]],
    expected_path: list[int] | None,
    gpt_oss_path: list[int] | None,
) -> dict[str, Any]:
    by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
    top_id = result.get("top_candidate_id")
    top_path = by_id.get(top_id, {}).get("path")
    expected_id = find_candidate_id(candidates, expected_path)
    gpt_oss_id = find_candidate_id(candidates, gpt_oss_path)
    return {
        "qwen_top_candidate_id": top_id,
        "qwen_top_path": top_path,
        "expected_path": expected_path,
        "expected_candidate_id": expected_id,
        "expected_rank": ranking_position(result, expected_id),
        "qwen_top_matches_expected": top_path == expected_path,
        "gpt_oss_path": gpt_oss_path,
        "gpt_oss_candidate_id": gpt_oss_id,
        "gpt_oss_rank": ranking_position(result, gpt_oss_id),
        "qwen_top_matches_gpt_oss": top_path == gpt_oss_path,
    }


def make_report(
    *,
    model: str,
    source_run: Path,
    candidates: list[dict[str, Any]],
    result: dict[str, Any],
    validation: dict[str, Any],
    comparison: dict[str, Any],
) -> str:
    candidate_by_id = {
        candidate["candidate_id"]: candidate for candidate in candidates
    }
    ranked = sorted(
        (
            item
            for item in result.get("ranked_candidates", [])
            if isinstance(item, dict)
        ),
        key=lambda item: item.get("rank", 10_000),
    )
    weighted = validation.get("derived_weighted_scores", {})

    lines = [
        "# Qwen path-ranking experiment",
        "",
        f"- Judge model: `{model}`",
        f"- Fixed upstream run: `{source_run}`",
        f"- Candidate count: `{len(candidates)}`",
        f"- Ranking validation: `{validation.get('passed')}`",
        f"- Qwen top path: `{path_text(comparison['qwen_top_path']) if comparison.get('qwen_top_path') else None}`",
        f"- Reviewed reference path: `{path_text(comparison['expected_path']) if comparison.get('expected_path') else None}`",
        f"- Reference rank: `{comparison.get('expected_rank')}`",
        f"- GPT-OSS path: `{path_text(comparison['gpt_oss_path']) if comparison.get('gpt_oss_path') else None}`",
        f"- GPT-OSS path rank: `{comparison.get('gpt_oss_rank')}`",
        "",
        "## Ranking",
        "",
        "| rank | candidate | path | phrase | coherence | lightness | detail control | function variety | weighted |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for item in ranked:
        candidate_id = item.get("candidate_id")
        candidate = candidate_by_id.get(candidate_id, {})
        scores = item.get("scores", {})
        lines.append(
            "| {rank} | {candidate_id} | {path} | {phrase} | {coherence} | "
            "{lightness} | {detail} | {variety} | {weighted_score} |".format(
                rank=item.get("rank"),
                candidate_id=candidate_id,
                path=candidate.get("path_text"),
                phrase=scores.get("reusable_phrase_value"),
                coherence=scores.get("conversation_coherence"),
                lightness=scores.get("cognitive_lightness"),
                detail=scores.get("technical_detail_control"),
                variety=scores.get("conversational_function_variety"),
                weighted_score=weighted.get(candidate_id),
            )
        )

    lines += [
        "",
        "## Top-choice reason",
        "",
        str(result.get("top_choice_reason", "")),
        "",
        "## Candidate notes",
        "",
    ]
    for item in ranked:
        candidate_id = item.get("candidate_id")
        candidate = candidate_by_id.get(candidate_id, {})
        lines += [
            f"### Rank {item.get('rank')}: {candidate_id} — {candidate.get('path_text')}",
            "",
            str(item.get("reason", "")),
            "",
            "Strengths:",
            *[f"- {value}" for value in item.get("strengths", [])],
            "",
            "Weaknesses:",
            *[f"- {value}" for value in item.get("weaknesses", [])],
            "",
        ]

    lines += [
        "## Interpretation boundary",
        "",
        "The ranking is an independent model judgment over fixed upstream summaries and phrase candidates. It does not replace human acceptance of the final learning path.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Enumerate valid paths from a fixed conversation-tree run and ask "
            "Qwen to rank them for English phrase learning."
        )
    )
    parser.add_argument("--source-run", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--base-url",
        default=os.environ.get("OLLAMA_BASE_URL", DEFAULT_BASE_URL),
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("QWEN_RANKER_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument(
        "--think",
        choices=["none", "low", "medium", "high"],
        default="high",
    )
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--keep-alive", default="30m")
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=8192,
        help="Maximum combined reasoning and answer tokens requested from Ollama.",
    )
    parser.add_argument("--min-posts", type=int, default=2)
    parser.add_argument("--max-posts", type=int, default=6)
    parser.add_argument(
        "--required-prefix",
        type=int,
        nargs="+",
        help="Keep only candidates that start with this exact post-number prefix.",
    )
    parser.add_argument(
        "--required-post-count",
        type=int,
        help="Keep only candidates with exactly this many posts.",
    )
    parser.add_argument("--ranking-retries", type=int, default=2)
    parser.add_argument("--expected-path", type=int, nargs="+")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parent.parent
    source_run = (args.source_run or repo / DEFAULT_SOURCE_RUN).resolve()
    output = (
        args.output_dir
        or repo / ".tmp/qwen-path-ranking/topic-107565-v1"
    ).resolve()

    if args.min_posts < 2:
        raise ValueError("--min-posts must be at least 2")
    if args.max_posts < args.min_posts:
        raise ValueError("--max-posts must be at least --min-posts")
    if args.ranking_retries < 0:
        raise ValueError("--ranking-retries must be zero or greater")
    if args.max_output_tokens < 256:
        raise ValueError("--max-output-tokens must be at least 256")
    if args.required_post_count is not None and args.required_post_count < 2:
        raise ValueError("--required-post-count must be at least 2")

    if output.exists() and any(output.iterdir()):
        if not args.force:
            raise FileExistsError(f"{output} is not empty; use --force")
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    tree_path = source_run / "coarse-tree.json"
    summaries_path = source_run / "post-summaries.json"
    source_manifest_path = source_run / "run-manifest.json"
    gpt_oss_result_path = (
        source_run / "path-selection/path-selection.parsed.json"
    )
    for path in (
        tree_path,
        summaries_path,
        source_manifest_path,
        gpt_oss_result_path,
    ):
        if not path.exists():
            raise FileNotFoundError(path)

    prompt_path = repo / EXPERIMENT_DIR / "path-ranking-prompt-v1.md"
    schema_path = repo / EXPERIMENT_DIR / "path-ranking-v1.schema.json"
    tree = read_json(tree_path)
    summaries_doc = read_json(summaries_path)
    source_manifest = read_json(source_manifest_path)
    gpt_oss_result = read_json(gpt_oss_result_path)
    schema = read_json(schema_path)

    candidates = build_candidates(
        tree,
        summaries_doc,
        args.min_posts,
        args.max_posts,
        required_prefix=args.required_prefix,
        required_post_count=args.required_post_count,
    )
    expected_path = args.expected_path or source_manifest.get("expected_path")
    if expected_path is not None and not all(
        isinstance(number, int) for number in expected_path
    ):
        raise ValueError("Expected path must contain only integers")
    gpt_oss_path = gpt_oss_result.get("selected_path")
    if gpt_oss_path is not None and not all(
        isinstance(number, int) for number in gpt_oss_path
    ):
        raise ValueError("GPT-OSS selected path is invalid")

    ranking_input = {
        "topic_id": source_manifest.get("topic_id"),
        "objective": (
            "Rank mechanically valid paths for lightweight English phrase learning."
        ),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    write_json(output / "ranking-candidates.json", {"candidates": candidates})
    write_json(output / "ranking-input.json", ranking_input)

    session = requests.Session()
    base_url = args.base_url.rstrip("/")
    model = args.model
    installed: list[str] = []
    if not args.prepare_only:
        model, installed = resolve_model(session, base_url, model)

    manifest = {
        "started_at": now(),
        "source_run": str(source_run),
        "source_hashes": {
            "coarse-tree.json": sha256(tree_path),
            "post-summaries.json": sha256(summaries_path),
            "run-manifest.json": sha256(source_manifest_path),
            "path-selection.parsed.json": sha256(gpt_oss_result_path),
        },
        "judge": {
            "base_url": base_url,
            "requested_model": args.model,
            "resolved_model": model,
            "installed_models": installed,
            "think": None if args.think == "none" else args.think,
            "temperature": args.temperature,
            "keep_alive": args.keep_alive,
            "ranking_retries": args.ranking_retries,
            "request_timeout_seconds": args.timeout,
            "max_output_tokens": args.max_output_tokens,
        },
        "candidate_policy": {
            "min_posts": args.min_posts,
            "max_posts": args.max_posts,
            "include_non_leaf_prefixes": True,
            "required_prefix": args.required_prefix,
            "required_post_count": args.required_post_count,
            "candidate_count": len(candidates),
        },
        "blind_inputs": {
            "expected_path_not_sent_to_judge": True,
            "gpt_oss_path_not_sent_to_judge": True,
        },
        "artifact_hashes": {
            prompt_path.name: sha256(prompt_path),
            schema_path.name: sha256(schema_path),
        },
        "prepare_only": args.prepare_only,
    }
    write_json(output / "run-manifest.json", manifest)

    if args.prepare_only:
        print(f"Prepared {len(candidates)} candidate paths: {output}")
        return 0

    base_prompt = fill_prompt(
        prompt_path,
        "{{RANKING_INPUT_JSON}}",
        ranking_input,
    )
    result: dict[str, Any] | None = None
    validation: dict[str, Any] = {
        "passed": False,
        "errors": ["Ranking was not run"],
    }
    accepted_attempt = 0
    attempt_think = None if args.think == "none" else args.think

    for attempt in range(1, args.ranking_retries + 2):
        retry_instruction = ""
        if validation.get("errors") and attempt > 1:
            retry_instruction = (
                "\n\nThe previous response failed deterministic validation. "
                "Regenerate the complete ranking. Include every supplied candidate "
                "exactly once, assign unique consecutive ranks from 1 through the "
                f"candidate count, and make top_candidate_id equal rank 1.\n"
                "Validation errors:\n"
                + json.dumps(validation["errors"], ensure_ascii=False, indent=2)
            )
        prefix = output / f"ranking-attempt-{attempt:02d}"
        try:
            result = call_ollama(
                session,
                base_url=base_url,
                model=model,
                think=attempt_think,
                temperature=args.temperature,
                keep_alive=args.keep_alive,
                timeout=args.timeout,
                max_output_tokens=args.max_output_tokens,
                prompt=base_prompt + retry_instruction,
                schema=schema,
                output_prefix=prefix,
            )
            validation = validate_ranking(result, candidates)
            validation["reasoning_effort"] = attempt_think or "off"
            validation["timed_out"] = False
        except requests.exceptions.ReadTimeout as exc:
            validation = {
                "passed": False,
                "errors": [
                    f"Ollama read timeout after {args.timeout} seconds: {exc}"
                ],
                "reasoning_effort": attempt_think or "off",
                "timed_out": True,
            }
            result = None
            session.close()
            session = requests.Session()
        except (json.JSONDecodeError, ValueError) as exc:
            validation = {
                "passed": False,
                "errors": [f"Ollama returned unusable structured output: {exc}"],
                "reasoning_effort": attempt_think or "off",
                "timed_out": False,
            }
            result = None

        write_json(prefix.with_suffix(".validation.json"), validation)
        if validation["passed"]:
            accepted_attempt = attempt
            break
        attempt_think = lower_reasoning_effort(attempt_think)

    if result is None or not validation["passed"]:
        raise ValueError(
            f"Qwen ranking failed after {args.ranking_retries + 1} attempts: "
            f"{validation.get('errors')}"
        )

    write_json(
        output / "ranking.accepted.json",
        {"accepted_attempt": accepted_attempt, "result": result},
    )
    write_json(output / "ranking-validation.json", validation)

    comparison = build_comparison(
        result,
        candidates,
        expected_path,
        gpt_oss_path,
    )
    write_json(output / "ranking-comparison.json", comparison)
    write_text(
        output / "report.md",
        make_report(
            model=model,
            source_run=source_run,
            candidates=candidates,
            result=result,
            validation=validation,
            comparison=comparison,
        )
        + "\n",
    )

    manifest.update(
        {
            "completed_at": now(),
            "accepted_attempt": accepted_attempt,
            "ranking_validation_passed": validation["passed"],
            "qwen_top_candidate_id": result.get("top_candidate_id"),
            "qwen_top_path": comparison.get("qwen_top_path"),
            "expected_rank": comparison.get("expected_rank"),
            "gpt_oss_rank": comparison.get("gpt_oss_rank"),
        }
    )
    write_json(output / "run-manifest.json", manifest)

    print(f"Experiment completed: {output}")
    print(f"Qwen top path: {comparison.get('qwen_top_path')}")
    print(f"Reviewed reference rank: {comparison.get('expected_rank')}")
    print(f"GPT-OSS path rank: {comparison.get('gpt_oss_rank')}")
    print(f"Report: {output / 'report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
