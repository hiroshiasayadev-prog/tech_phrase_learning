from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import requests


BASE_URL = "https://discuss.python.org"
POST_CHUNK_SIZE = 20
USER_AGENT = "tech-phrase-learning/0.1"
MAX_DIFF_LINES = 120


def chunked(values: list[int], size: int) -> Iterable[list[int]]:
    for start in range(0, len(values), size):
        yield values[start : start + size]


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def write_bytes(path: Path, content: bytes, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite {path}. Re-run with --force to replace it."
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def write_text(path: Path, content: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite {path}. Re-run with --force to replace it."
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def decode_json_body(response: requests.Response) -> dict[str, Any]:
    try:
        payload = response.json()
    except requests.JSONDecodeError as exc:
        raise ValueError(f"Response from {response.url} was not valid JSON") from exc

    if not isinstance(payload, dict):
        raise ValueError(f"Response from {response.url} was not a JSON object")

    return payload


def fetch_response(
    session: requests.Session,
    url: str,
    *,
    params: list[tuple[str, str]] | dict[str, str],
) -> tuple[requests.Response, dict[str, Any]]:
    response = session.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response, decode_json_body(response)


def extract_posts(payload: dict[str, Any]) -> list[dict[str, Any]]:
    posts = payload.get("post_stream", {}).get("posts", [])
    if not isinstance(posts, list):
        raise ValueError("Discourse response contains an invalid post_stream.posts value")
    return posts


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def first_mismatch(left: str, right: str) -> int | None:
    for index, (left_char, right_char) in enumerate(zip(left, right)):
        if left_char != right_char:
            return index

    if len(left) != len(right):
        return min(len(left), len(right))

    return None


def bounded_unified_diff(
    current: str,
    captured: str,
    *,
    max_lines: int = MAX_DIFF_LINES,
) -> str:
    lines = list(
        difflib.unified_diff(
            current.splitlines(),
            captured.splitlines(),
            fromfile="reviewed fixture",
            tofile="captured API raw",
            lineterm="",
        )
    )

    if len(lines) <= max_lines:
        return "\n".join(lines)

    omitted = len(lines) - max_lines
    return "\n".join(
        [*lines[:max_lines], f"... {omitted} additional diff lines omitted ..."]
    )


def build_selected_source(
    topic: dict[str, Any],
    posts: list[dict[str, Any]],
    selected_post_numbers: list[int],
) -> dict[str, Any]:
    posts_by_number = {post["post_number"]: post for post in posts}
    missing = [
        post_number
        for post_number in selected_post_numbers
        if post_number not in posts_by_number
    ]
    if missing:
        raise ValueError(f"Selected posts are missing from the topic: {missing}")

    selected_posts = []
    for post_number in selected_post_numbers:
        post = posts_by_number[post_number]
        raw = post.get("raw")
        if not isinstance(raw, str):
            raise ValueError(f"Post #{post_number} has no raw source text")

        selected_posts.append(
            {
                "post_number": post_number,
                "post_id": post["id"],
                "username": post["username"],
                "created_at": post.get("created_at"),
                "reply_to_post_number": post.get("reply_to_post_number"),
                "raw": raw,
                "cooked": post.get("cooked"),
            }
        )

    topic_id = topic["id"]
    return {
        "topic_id": topic_id,
        "title": topic["title"],
        "slug": topic["slug"],
        "source_url": f"{BASE_URL}/t/{topic['slug']}/{topic_id}",
        "selected_post_numbers": selected_post_numbers,
        "posts": selected_posts,
    }


def load_json_object(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return payload


def source_phrase_checks(
    output_dir: Path,
    captured_posts: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    for filename in ("question-interaction.json", "reply-interaction.json"):
        path = output_dir / filename
        interaction = load_json_object(path)
        if interaction is None:
            continue

        source_phrase = interaction.get("source_phrase", {})
        phrase = source_phrase.get("text") if isinstance(source_phrase, dict) else None
        if not isinstance(phrase, str) or not phrase:
            checks.append(
                {
                    "file": filename,
                    "phrase": None,
                    "matching_posts": [],
                    "passed": False,
                }
            )
            continue

        matching_posts = [
            post["post_number"]
            for post in captured_posts
            if phrase in post["raw"]
        ]
        checks.append(
            {
                "file": filename,
                "phrase": phrase,
                "matching_posts": matching_posts,
                "passed": bool(matching_posts),
            }
        )

    return checks


def build_comparison_report(
    reviewed: dict[str, Any] | None,
    captured: dict[str, Any],
    phrase_checks: list[dict[str, Any]],
) -> str:
    lines = [
        "# Source capture comparison",
        "",
        "This report compares the reviewed fixture with a fresh Discourse API capture.",
        "The capture script does not overwrite `source-posts.json`.",
        "",
    ]

    if reviewed is None:
        lines.extend(
            [
                "## Reviewed fixture",
                "",
                "No existing `source-posts.json` was found.",
                "",
            ]
        )
    else:
        reviewed_posts = {
            post["post_number"]: post
            for post in reviewed.get("posts", [])
            if isinstance(post, dict) and "post_number" in post
        }
        captured_posts = {
            post["post_number"]: post for post in captured["posts"]
        }

        lines.extend(
            [
                "## Post comparison",
                "",
                "| post | username | reply target | raw exact | whitespace-normalized |",
                "|---|---|---|---|---|",
            ]
        )

        mismatches: list[tuple[int, str, str]] = []
        for post_number in captured["selected_post_numbers"]:
            api_post = captured_posts[post_number]
            reviewed_post = reviewed_posts.get(post_number)

            if reviewed_post is None:
                lines.append(
                    f"| `#{post_number}` | missing | missing | no | no |"
                )
                continue

            username_match = reviewed_post.get("username") == api_post.get("username")
            reply_match = (
                reviewed_post.get("reply_to_post_number")
                == api_post.get("reply_to_post_number")
            )
            reviewed_raw = reviewed_post.get("raw", "")
            api_raw = api_post["raw"]
            raw_exact = reviewed_raw == api_raw
            whitespace_match = (
                normalize_whitespace(reviewed_raw)
                == normalize_whitespace(api_raw)
            )

            lines.append(
                "| "
                f"`#{post_number}` | "
                f"{'yes' if username_match else 'no'} | "
                f"{'yes' if reply_match else 'no'} | "
                f"{'yes' if raw_exact else 'no'} | "
                f"{'yes' if whitespace_match else 'no'} |"
            )

            if not raw_exact:
                mismatches.append((post_number, reviewed_raw, api_raw))

        lines.append("")

        if mismatches:
            lines.extend(["## Raw-text differences", ""])
            for post_number, reviewed_raw, api_raw in mismatches:
                mismatch_index = first_mismatch(reviewed_raw, api_raw)
                lines.extend(
                    [
                        f"### Post #{post_number}",
                        "",
                        f"- Reviewed characters: `{len(reviewed_raw)}`",
                        f"- Captured characters: `{len(api_raw)}`",
                        f"- First mismatch offset: `{mismatch_index}`",
                        "- Whitespace-normalized match: "
                        f"`{normalize_whitespace(reviewed_raw) == normalize_whitespace(api_raw)}`",
                        "",
                        "```diff",
                        bounded_unified_diff(reviewed_raw, api_raw),
                        "```",
                        "",
                    ]
                )
        else:
            lines.extend(
                [
                    "## Raw-text differences",
                    "",
                    "No raw-text differences were found.",
                    "",
                ]
            )

    lines.extend(
        [
            "## Source phrase checks",
            "",
            "| interaction | exact phrase found | matching posts |",
            "|---|---|---|",
        ]
    )

    if phrase_checks:
        for check in phrase_checks:
            matching_posts = ", ".join(
                f"`#{post_number}`" for post_number in check["matching_posts"]
            ) or "none"
            lines.append(
                f"| `{check['file']}` | "
                f"{'yes' if check['passed'] else 'no'} | "
                f"{matching_posts} |"
            )
    else:
        lines.append("| no interaction files found | n/a | n/a |")

    lines.append("")
    return "\n".join(lines)


def capture_topic(
    topic_id: int,
    selected_post_numbers: list[int],
    output_dir: Path,
    *,
    force: bool,
) -> int:
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        }
    )

    captured_at = datetime.now(timezone.utc).isoformat()
    requests_manifest: list[dict[str, Any]] = []

    topic_url = f"{BASE_URL}/t/{topic_id}.json"
    topic_response, topic = fetch_response(
        session,
        topic_url,
        params={"include_raw": "true"},
    )
    topic_raw_path = output_dir / "source-topic.raw.json"
    write_bytes(topic_raw_path, topic_response.content, force=force)
    requests_manifest.append(
        {
            "url": topic_response.url,
            "output": topic_raw_path.name,
            "status_code": topic_response.status_code,
            "content_type": topic_response.headers.get("Content-Type"),
            "etag": topic_response.headers.get("ETag"),
            "last_modified": topic_response.headers.get("Last-Modified"),
            "sha256": sha256_bytes(topic_response.content),
        }
    )

    post_stream = topic.get("post_stream")
    if not isinstance(post_stream, dict):
        raise ValueError("Topic response has no valid post_stream")

    posts = list(extract_posts(topic))
    stream = post_stream.get("stream", [])
    if not isinstance(stream, list):
        raise ValueError("Topic response has no valid post_stream.stream")

    fetched_ids = {post["id"] for post in posts}
    missing_ids = [post_id for post_id in stream if post_id not in fetched_ids]

    for chunk_index, post_ids in enumerate(
        chunked(missing_ids, POST_CHUNK_SIZE),
        start=1,
    ):
        params: list[tuple[str, str]] = [
            ("include_raw", "true"),
            *[("post_ids[]", str(post_id)) for post_id in post_ids],
        ]
        chunk_response, chunk_payload = fetch_response(
            session,
            f"{BASE_URL}/t/{topic_id}/posts.json",
            params=params,
        )
        chunk_path = output_dir / f"source-posts-chunk-{chunk_index:02d}.raw.json"
        write_bytes(chunk_path, chunk_response.content, force=force)
        requests_manifest.append(
            {
                "url": chunk_response.url,
                "output": chunk_path.name,
                "status_code": chunk_response.status_code,
                "content_type": chunk_response.headers.get("Content-Type"),
                "etag": chunk_response.headers.get("ETag"),
                "last_modified": chunk_response.headers.get("Last-Modified"),
                "sha256": sha256_bytes(chunk_response.content),
            }
        )
        posts.extend(extract_posts(chunk_payload))

    posts.sort(key=lambda post: post["post_number"])
    captured = build_selected_source(topic, posts, selected_post_numbers)

    derived_path = output_dir / "source-posts.from-api.json"
    write_text(
        derived_path,
        json.dumps(captured, ensure_ascii=False, indent=2) + "\n",
        force=force,
    )

    phrase_checks = source_phrase_checks(output_dir, captured["posts"])
    reviewed = load_json_object(output_dir / "source-posts.json")
    report = build_comparison_report(reviewed, captured, phrase_checks)
    report_path = output_dir / "source-comparison.md"
    write_text(report_path, report, force=force)

    manifest = {
        "topic_id": topic_id,
        "captured_at": captured_at,
        "selected_post_numbers": selected_post_numbers,
        "requests": requests_manifest,
        "derived_output": derived_path.name,
        "comparison_report": report_path.name,
        "source_phrase_checks": phrase_checks,
    }
    manifest_path = output_dir / "source-capture.json"
    write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        force=force,
    )

    failed_phrase_checks = [
        check for check in phrase_checks if not check["passed"]
    ]
    if failed_phrase_checks:
        print(f"Captured topic {topic_id}, but one or more source phrases were missing.")
        print(f"Review: {report_path}")
        return 2

    print(f"Captured topic {topic_id} into {output_dir}")
    print(f"Raw topic payload: {topic_raw_path}")
    print(f"Derived selected posts: {derived_path}")
    print(f"Comparison report: {report_path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Capture a Discourse topic as raw API evidence, derive selected posts, "
            "and compare them with an existing golden fixture."
        )
    )
    parser.add_argument("topic_id", type=int)
    parser.add_argument(
        "--posts",
        type=int,
        nargs="+",
        required=True,
        help="Selected post numbers in branch order, for example: 1 2 4 7",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help=(
            "Fixture directory. Defaults to "
            "product/fixture/golden/topic-<topic-id> under the repository root."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files previously produced by this script.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = args.output_dir or (
        repo_root / "product" / "fixture" / "golden" / f"topic-{args.topic_id}"
    )

    if len(set(args.posts)) != len(args.posts):
        raise ValueError("--posts must not contain duplicate post numbers")

    return capture_topic(
        topic_id=args.topic_id,
        selected_post_numbers=args.posts,
        output_dir=output_dir.resolve(),
        force=args.force,
    )


if __name__ == "__main__":
    raise SystemExit(main())
