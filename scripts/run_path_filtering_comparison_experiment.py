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
DEFAULT_GPT_MODEL = "gpt-oss:20b"
DEFAULT_QWEN_MODEL = "qwen3.6-27b:q4_k_m-tools"
DEFAULT_SOURCE_RUN = Path(
    "product/fixture/experiments/gpt-oss-20b/"
    "conversation-path-selection/runs/topic-107565-v3"
)
EXPERIMENT_DIR = Path(
    "product/fixture/experiments/path-filtering-model-comparison"
)

MODEL_DEFAULTS = {
    "gpt": {"think": "medium"},
    "qwen": {"think": "high"},
}

TECHNICAL_TERMS_BY_POST = {
    1: ["pyproject.toml", "build_wheel", "build_sdist"],
    2: ["pip", "build_wheel", "build_sdist"],
    4: ["uv", "hatch", "pdm"],
    6: ["PEP 517", ".app", ".pex"],
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


def model_slug(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-")


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
                    "Act as an absolute quiz-path validity filter. Judge only the "
                    "supplied path. Never reject it merely because another path could "
                    "be better. Return only schema-valid JSON."
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
    if not isinstance(content, str) or not content.strip():
        raise ValueError("Ollama response has no non-empty message.content")
    parsed = json.loads(content)
    if not isinstance(parsed, dict):
        raise ValueError("Ollama structured output is not an object")
    write_json(output_prefix.with_suffix(".parsed.json"), parsed)
    return parsed


def build_post_maps(
    tree: dict[str, Any],
    summaries_doc: dict[str, Any],
) -> tuple[dict[int, dict[str, Any]], dict[int, dict[str, Any]]]:
    nodes = {
        node["post_number"]: node
        for node in tree.get("nodes", [])
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
    return nodes, summaries


def transform_phrases(
    post_number: int,
    original: Any,
    transform: str,
) -> list[dict[str, Any]]:
    if transform == "remove_phrase_candidates":
        return []
    if transform == "technical_terms_only":
        return [
            {
                "text": term,
                "function": "technical term only",
                "source_verified": True,
            }
            for term in TECHNICAL_TERMS_BY_POST.get(post_number, [])
        ]
    if not isinstance(original, list):
        raise ValueError(f"Post #{post_number} has no phrase candidate list")
    result: list[dict[str, Any]] = []
    for item in original:
        if not isinstance(item, dict):
            continue
        text = item.get("text")
        function = item.get("function")
        if isinstance(text, str) and isinstance(function, str):
            result.append(
                {
                    "text": text,
                    "function": function,
                    "source_verified": True,
                }
            )
    return result


def build_case_input(
    case: dict[str, Any],
    nodes: dict[int, dict[str, Any]],
    summaries: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    case_id = case.get("case_id")
    path = case.get("path")
    transform = case.get("transform")
    mechanically_valid = case.get("mechanically_valid")
    if not isinstance(case_id, str):
        raise ValueError("Case has no case_id")
    if not isinstance(path, list) or not all(isinstance(x, int) for x in path):
        raise ValueError(f"Case {case_id} has invalid path")
    if not isinstance(transform, str):
        raise ValueError(f"Case {case_id} has no transform")
    if not isinstance(mechanically_valid, bool):
        raise ValueError(f"Case {case_id} has no mechanically_valid flag")

    posts: list[dict[str, Any]] = []
    for number in path:
        if number not in nodes or number not in summaries:
            raise ValueError(f"Case {case_id} references unknown post #{number}")
        summary = summaries[number]
        posts.append(
            {
                "post_number": number,
                "username": nodes[number].get("username"),
                "summary": summary.get("summary"),
                "conversational_intent": summary.get("conversational_intent"),
                "stance": summary.get("stance"),
                "technical_burden": summary.get("technical_burden"),
                "phrase_candidates": transform_phrases(
                    number,
                    summary.get("phrase_candidates"),
                    transform,
                ),
            }
        )

    return {
        "case_id": case_id,
        "path": path,
        "post_count": len(path),
        "mechanically_valid": mechanically_valid,
        "posts": posts,
    }


def all_phrase_texts(case_input: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for post in case_input.get("posts", []):
        if not isinstance(post, dict):
            continue
        for phrase in post.get("phrase_candidates", []):
            if isinstance(phrase, dict) and isinstance(phrase.get("text"), str):
                result.add(phrase["text"])
    return result


def validate_filter_result(
    result: dict[str, Any],
    case_input: dict[str, Any],
) -> dict[str, Any]:
    errors: list[str] = []
    case_id = case_input["case_id"]
    if result.get("case_id") != case_id:
        errors.append(
            f"case_id mismatch: expected {case_id!r}, got {result.get('case_id')!r}"
        )

    valid = result.get("valid_for_quiz")
    decision = result.get("decision")
    if not isinstance(valid, bool):
        errors.append("valid_for_quiz is not boolean")
    if decision not in {"accept", "reject"}:
        errors.append("decision is not accept or reject")
    if isinstance(valid, bool):
        expected_decision = "accept" if valid else "reject"
        if decision != expected_decision:
            errors.append(
                f"decision must be {expected_decision!r} when valid_for_quiz={valid}"
            )

    focuses = result.get("learning_focus")
    evidence = result.get("reusable_phrase_evidence")
    reasons = result.get("exclusion_reasons")
    if not isinstance(focuses, list) or not all(isinstance(x, str) for x in focuses):
        errors.append("learning_focus is not a string list")
        focuses = []
    if not isinstance(evidence, list) or not all(isinstance(x, str) for x in evidence):
        errors.append("reusable_phrase_evidence is not a string list")
        evidence = []
    if not isinstance(reasons, list) or not all(isinstance(x, str) for x in reasons):
        errors.append("exclusion_reasons is not a string list")
        reasons = []

    available = all_phrase_texts(case_input)
    unknown_evidence = [text for text in evidence if text not in available]
    if unknown_evidence:
        errors.append(f"Phrase evidence was not supplied: {unknown_evidence}")

    if valid is True:
        if not focuses:
            errors.append("Accepted path has no learning focus")
        if not evidence:
            errors.append("Accepted path has no reusable phrase evidence")
        if reasons:
            errors.append("Accepted path has exclusion reasons")
    elif valid is False:
        if not reasons:
            errors.append("Rejected path has no exclusion reason")

    return {
        "passed": not errors,
        "errors": errors,
        "available_phrase_count": len(available),
    }


def run_case(
    *,
    session: requests.Session,
    base_url: str,
    model: str,
    initial_think: str | None,
    retries: int,
    temperature: float,
    keep_alive: str,
    timeout: float,
    max_output_tokens: int,
    prompt: str,
    schema: dict[str, Any],
    case_input: dict[str, Any],
    output_dir: Path,
) -> tuple[dict[str, Any], dict[str, Any], int]:
    result: dict[str, Any] | None = None
    validation: dict[str, Any] = {
        "passed": False,
        "errors": ["Filter was not run"],
    }
    attempt_think = initial_think

    for attempt in range(1, retries + 2):
        retry_instruction = ""
        if attempt > 1:
            retry_instruction = (
                "\n\nThe previous response failed deterministic validation. "
                "Regenerate the complete JSON object without changing the supplied "
                "case. Use only supplied phrase candidates as evidence.\n"
                "Validation errors:\n"
                + json.dumps(validation.get("errors", []), ensure_ascii=False, indent=2)
            )
        prefix = output_dir / f"attempt-{attempt:02d}"
        try:
            result = call_ollama(
                session,
                base_url=base_url,
                model=model,
                think=attempt_think,
                temperature=temperature,
                keep_alive=keep_alive,
                timeout=timeout,
                max_output_tokens=max_output_tokens,
                prompt=prompt + retry_instruction,
                schema=schema,
                output_prefix=prefix,
            )
            validation = validate_filter_result(result, case_input)
            validation["reasoning_effort"] = attempt_think or "off"
            validation["timed_out"] = False
        except requests.exceptions.ReadTimeout as exc:
            validation = {
                "passed": False,
                "errors": [f"Read timeout after {timeout} seconds: {exc}"],
                "reasoning_effort": attempt_think or "off",
                "timed_out": True,
            }
            result = None
        except (requests.RequestException, RuntimeError, json.JSONDecodeError, ValueError) as exc:
            validation = {
                "passed": False,
                "errors": [f"Unusable model response: {exc}"],
                "reasoning_effort": attempt_think or "off",
                "timed_out": False,
            }
            result = None

        write_json(prefix.with_suffix(".validation.json"), validation)
        if validation["passed"] and result is not None:
            write_json(
                output_dir / "accepted.json",
                {"accepted_attempt": attempt, "result": result},
            )
            return result, validation, attempt
        attempt_think = lower_reasoning_effort(attempt_think)

    raise ValueError(
        f"Filtering failed for {case_input['case_id']} after {retries + 1} attempts: "
        f"{validation.get('errors')}"
    )


def calculate_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(records)
    correct = sum(1 for item in records if item["correct"])
    valid_records = [item for item in records if item["expected_valid"]]
    invalid_records = [item for item in records if not item["expected_valid"]]
    valid_accepted = sum(1 for item in valid_records if item["actual_valid"])
    invalid_rejected = sum(1 for item in invalid_records if not item["actual_valid"])
    valid_recall = valid_accepted / len(valid_records) if valid_records else 0.0
    invalid_rejection_rate = (
        invalid_rejected / len(invalid_records) if invalid_records else 0.0
    )
    return {
        "total_cases": total,
        "correct_cases": correct,
        "accuracy": correct / total if total else 0.0,
        "real_valid_cases": len(valid_records),
        "real_valid_accepted": valid_accepted,
        "valid_path_recall": valid_recall,
        "invalid_controls": len(invalid_records),
        "invalid_controls_rejected": invalid_rejected,
        "invalid_control_rejection_rate": invalid_rejection_rate,
        "false_rejections": [
            item["case_id"]
            for item in valid_records
            if not item["actual_valid"]
        ],
        "false_acceptances": [
            item["case_id"]
            for item in invalid_records
            if item["actual_valid"]
        ],
        "acceptance_target_met": (
            valid_recall == 1.0 and invalid_rejection_rate == 1.0
        ),
    }


def build_report(
    model_results: dict[str, dict[str, Any]],
    agreement: dict[str, Any],
) -> str:
    lines = [
        "# Path-filtering model comparison",
        "",
        "Each case was judged independently. Expected labels were not sent to either model.",
        "",
        "## Summary",
        "",
        "| model | accuracy | valid recall | invalid rejection | target met |",
        "|---|---:|---:|---:|---|",
    ]
    for key, value in model_results.items():
        metrics = value["metrics"]
        lines.append(
            "| {model} | {accuracy:.3f} | {valid_recall:.3f} | "
            "{invalid_rejection:.3f} | {target} |".format(
                model=value["model"],
                accuracy=metrics["accuracy"],
                valid_recall=metrics["valid_path_recall"],
                invalid_rejection=metrics["invalid_control_rejection_rate"],
                target=metrics["acceptance_target_met"],
            )
        )

    lines += [
        "",
        "## Case decisions",
        "",
        "| case | expected | class | "
        + " | ".join(value["model"] for value in model_results.values())
        + " |",
        "|---|---|---|"
        + "---|" * len(model_results),
    ]
    case_ids = [item["case_id"] for item in next(iter(model_results.values()))["records"]]
    records_by_model = {
        key: {item["case_id"]: item for item in value["records"]}
        for key, value in model_results.items()
    }
    first_records = records_by_model[next(iter(records_by_model))]
    for case_id in case_ids:
        first = first_records[case_id]
        decisions = []
        for key in model_results:
            record = records_by_model[key][case_id]
            marker = "accept" if record["actual_valid"] else "reject"
            if not record["correct"]:
                marker += " ⚠"
            decisions.append(marker)
        lines.append(
            f"| {case_id} | {'accept' if first['expected_valid'] else 'reject'} | "
            f"{first['control_class']} | " + " | ".join(decisions) + " |"
        )

    lines += [
        "",
        "## Agreement",
        "",
        f"- Cases compared: `{agreement['case_count']}`",
        f"- Same decision: `{agreement['same_decision_count']}`",
        f"- Agreement rate: `{agreement['agreement_rate']:.3f}`",
        f"- Disagreements: `{agreement['disagreement_case_ids']}`",
        "",
    ]
    for key, value in model_results.items():
        lines += [
            f"## {value['model']}",
            "",
            f"- False rejections: `{value['metrics']['false_rejections']}`",
            f"- False acceptances: `{value['metrics']['false_acceptances']}`",
            "",
        ]
        for record in value["records"]:
            lines += [
                f"### {record['case_id']} — {'accept' if record['actual_valid'] else 'reject'}",
                "",
                f"Expected: `{'accept' if record['expected_valid'] else 'reject'}`",
                "",
                f"Learning focus: `{record['result'].get('learning_focus')}`",
                "",
                f"Evidence: `{record['result'].get('reusable_phrase_evidence')}`",
                "",
                f"Exclusion reasons: `{record['result'].get('exclusion_reasons')}`",
                "",
                str(record["result"].get("explanation", "")),
                "",
            ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare GPT-OSS and Qwen as independent absolute filters over quiz-path "
            "candidates and invalid controls."
        )
    )
    parser.add_argument("--source-run", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--base-url",
        default=os.environ.get("OLLAMA_BASE_URL", DEFAULT_BASE_URL),
    )
    parser.add_argument("--gpt-model", default=DEFAULT_GPT_MODEL)
    parser.add_argument("--qwen-model", default=DEFAULT_QWEN_MODEL)
    parser.add_argument(
        "--models",
        nargs="+",
        choices=["gpt", "qwen"],
        default=["gpt", "qwen"],
    )
    parser.add_argument("--gpt-think", choices=["none", "low", "medium", "high"], default="medium")
    parser.add_argument("--qwen-think", choices=["none", "low", "medium", "high"], default="high")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--keep-alive", default="30m")
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument("--max-output-tokens", type=int, default=4096)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parent.parent
    source_run = (args.source_run or repo / DEFAULT_SOURCE_RUN).resolve()
    output = (
        args.output_dir
        or repo / ".tmp/path-filtering-comparison/topic-107565-v1"
    ).resolve()
    if args.max_output_tokens < 256:
        raise ValueError("--max-output-tokens must be at least 256")
    if args.retries < 0:
        raise ValueError("--retries must be zero or greater")
    if output.exists() and any(output.iterdir()):
        if not args.force:
            raise FileExistsError(f"{output} is not empty; use --force")
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    tree_path = source_run / "coarse-tree.json"
    summaries_path = source_run / "post-summaries.json"
    prompt_path = repo / EXPERIMENT_DIR / "path-filter-prompt-v1.md"
    schema_path = repo / EXPERIMENT_DIR / "path-filter-v1.schema.json"
    cases_path = repo / EXPERIMENT_DIR / "filter-cases-v1.json"
    for path in (tree_path, summaries_path, prompt_path, schema_path, cases_path):
        if not path.exists():
            raise FileNotFoundError(path)

    tree = read_json(tree_path)
    summaries_doc = read_json(summaries_path)
    schema = read_json(schema_path)
    cases_doc = read_json(cases_path)
    nodes, summaries = build_post_maps(tree, summaries_doc)
    case_defs = cases_doc.get("cases")
    if not isinstance(case_defs, list):
        raise ValueError("filter-cases-v1.json has no cases list")

    case_inputs: dict[str, dict[str, Any]] = {}
    gold: dict[str, dict[str, Any]] = {}
    for case in case_defs:
        if not isinstance(case, dict):
            raise ValueError("Case definition is not an object")
        case_input = build_case_input(case, nodes, summaries)
        case_id = case_input["case_id"]
        case_inputs[case_id] = case_input
        gold[case_id] = {
            "expected_valid": case.get("expected_valid"),
            "control_class": case.get("control_class"),
        }
        write_json(output / "cases" / f"{case_id}.input.json", case_input)

    write_json(output / "case-gold.json", gold)
    write_json(output / "case-set.json", {"cases": list(case_inputs.values())})

    base_url = args.base_url.rstrip("/")
    model_requests = {
        "gpt": {
            "requested_model": args.gpt_model,
            "think": None if args.gpt_think == "none" else args.gpt_think,
        },
        "qwen": {
            "requested_model": args.qwen_model,
            "think": None if args.qwen_think == "none" else args.qwen_think,
        },
    }
    session = requests.Session()
    resolved_models: dict[str, dict[str, Any]] = {}
    installed: list[str] = []
    if not args.prepare_only:
        for key in args.models:
            resolved, installed = resolve_model(
                session,
                base_url,
                model_requests[key]["requested_model"],
            )
            resolved_models[key] = {
                **model_requests[key],
                "resolved_model": resolved,
            }
    else:
        for key in args.models:
            resolved_models[key] = {
                **model_requests[key],
                "resolved_model": model_requests[key]["requested_model"],
            }

    manifest = {
        "started_at": now(),
        "source_run": str(source_run),
        "source_hashes": {
            "coarse-tree.json": sha256(tree_path),
            "post-summaries.json": sha256(summaries_path),
        },
        "fixture_hashes": {
            prompt_path.name: sha256(prompt_path),
            schema_path.name: sha256(schema_path),
            cases_path.name: sha256(cases_path),
        },
        "base_url": base_url,
        "models": resolved_models,
        "installed_models": installed,
        "temperature": args.temperature,
        "keep_alive": args.keep_alive,
        "timeout": args.timeout,
        "max_output_tokens": args.max_output_tokens,
        "retries": args.retries,
        "blind_evaluation": {
            "expected_labels_not_sent": True,
            "cases_judged_independently": True,
            "alternative_paths_not_sent": True,
        },
        "prepare_only": args.prepare_only,
    }
    write_json(output / "run-manifest.json", manifest)

    if args.prepare_only:
        print(f"Prepared {len(case_inputs)} cases for models {args.models}: {output}")
        return 0

    model_results: dict[str, dict[str, Any]] = {}
    for key in args.models:
        config = resolved_models[key]
        model = config["resolved_model"]
        model_dir = output / "models" / model_slug(model)
        records: list[dict[str, Any]] = []
        for case_id, case_input in case_inputs.items():
            prompt = fill_prompt(
                prompt_path,
                "{{FILTER_INPUT_JSON}}",
                case_input,
            )
            case_dir = model_dir / case_id
            result, validation, accepted_attempt = run_case(
                session=session,
                base_url=base_url,
                model=model,
                initial_think=config["think"],
                retries=args.retries,
                temperature=args.temperature,
                keep_alive=args.keep_alive,
                timeout=args.timeout,
                max_output_tokens=args.max_output_tokens,
                prompt=prompt,
                schema=schema,
                case_input=case_input,
                output_dir=case_dir,
            )
            expected_valid = gold[case_id]["expected_valid"]
            actual_valid = result["valid_for_quiz"]
            record = {
                "case_id": case_id,
                "control_class": gold[case_id]["control_class"],
                "expected_valid": expected_valid,
                "actual_valid": actual_valid,
                "correct": actual_valid == expected_valid,
                "accepted_attempt": accepted_attempt,
                "validation": validation,
                "result": result,
            }
            records.append(record)
            write_json(case_dir / "evaluation.json", record)

        metrics = calculate_metrics(records)
        model_results[key] = {
            "model": model,
            "records": records,
            "metrics": metrics,
        }
        write_json(model_dir / "summary.json", model_results[key])

    agreement = {
        "case_count": 0,
        "same_decision_count": 0,
        "agreement_rate": 0.0,
        "disagreement_case_ids": [],
    }
    if len(model_results) >= 2:
        keys = list(model_results)
        left = {
            item["case_id"]: item["actual_valid"]
            for item in model_results[keys[0]]["records"]
        }
        right = {
            item["case_id"]: item["actual_valid"]
            for item in model_results[keys[1]]["records"]
        }
        shared = sorted(set(left) & set(right))
        disagreements = [case_id for case_id in shared if left[case_id] != right[case_id]]
        agreement = {
            "case_count": len(shared),
            "same_decision_count": len(shared) - len(disagreements),
            "agreement_rate": (
                (len(shared) - len(disagreements)) / len(shared)
                if shared
                else 0.0
            ),
            "disagreement_case_ids": disagreements,
        }

    write_json(
        output / "comparison.json",
        {"models": model_results, "agreement": agreement},
    )
    write_text(
        output / "report.md",
        build_report(model_results, agreement) + "\n",
    )

    manifest.update(
        {
            "completed_at": now(),
            "model_metrics": {
                key: value["metrics"] for key, value in model_results.items()
            },
            "agreement": agreement,
        }
    )
    write_json(output / "run-manifest.json", manifest)

    print(f"Experiment completed: {output}")
    for value in model_results.values():
        metrics = value["metrics"]
        print(
            f"{value['model']}: accuracy={metrics['accuracy']:.3f}, "
            f"valid_recall={metrics['valid_path_recall']:.3f}, "
            f"invalid_rejection={metrics['invalid_control_rejection_rate']:.3f}, "
            f"target={metrics['acceptance_target_met']}"
        )
    if len(model_results) >= 2:
        print(f"Agreement: {agreement['agreement_rate']:.3f}")
    print(f"Report: {output / 'report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
