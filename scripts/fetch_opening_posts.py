from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterator

import requests


BASE_URL = "https://discuss.python.org"
POST_CHUNK_SIZE = 20


@dataclass
class PostNode:
    post_number: int
    post_id: int
    username: str
    raw: str | None
    cooked: str
    created_at: str
    reply_to_post_number: int | None
    children: list["PostNode"] = field(default_factory=list)


def chunked(values: list[int], size: int) -> Iterator[list[int]]:
    for start in range(0, len(values), size):
        yield values[start : start + size]


def extract_posts(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Handle the normal Discourse response shape."""
    return payload.get("post_stream", {}).get("posts", [])


def fetch_all_topic_posts(
    topic_id: int,
    *,
    session: requests.Session | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    client = session or requests.Session()
    client.headers.update(
        {
            "Accept": "application/json",
            "User-Agent": "tech-phrase-learning/0.1",
        }
    )

    response = client.get(
        f"{BASE_URL}/t/{topic_id}.json",
        params={"include_raw": "true"},
        timeout=30,
    )
    response.raise_for_status()

    topic = response.json()
    post_stream = topic["post_stream"]

    posts = list(post_stream["posts"])
    all_post_ids: list[int] = post_stream["stream"]

    fetched_ids = {post["id"] for post in posts}
    missing_ids = [
        post_id for post_id in all_post_ids if post_id not in fetched_ids
    ]

    for post_ids in chunked(missing_ids, POST_CHUNK_SIZE):
        params: list[tuple[str, str]] = [
            ("include_raw", "true"),
            *[("post_ids[]", str(post_id)) for post_id in post_ids],
        ]

        response = client.get(
            f"{BASE_URL}/t/{topic_id}/posts.json",
            params=params,
            timeout=30,
        )
        response.raise_for_status()

        posts.extend(extract_posts(response.json()))

    posts.sort(key=lambda post: post["post_number"])
    return topic, posts

def build_conversation_tree(posts: list[dict[str, Any]]) -> PostNode:
    if not posts:
        raise ValueError("The topic contains no visible posts")

    nodes: dict[int, PostNode] = {}

    for post in posts:
        node = PostNode(
            post_number=post["post_number"],
            post_id=post["id"],
            username=post["username"],
            raw=post.get("raw"),
            cooked=post["cooked"],
            created_at=post["created_at"],
            reply_to_post_number=post.get("reply_to_post_number"),
        )
        nodes[node.post_number] = node

    root = nodes[min(nodes)]

    for post_number in sorted(nodes):
        if post_number == root.post_number:
            continue

        node = nodes[post_number]
        explicit_parent = node.reply_to_post_number

        if explicit_parent is not None and explicit_parent in nodes:
            parent = nodes[explicit_parent]
        else:
            # Project normalization:
            # no explicit target means a topic-level response.
            parent = root

        parent.children.append(node)

    return root

def extract_opening_post_record(
    topic: dict[str, Any],
    opening_post: dict[str, Any],
) -> dict[str, Any]:
    topic_id = topic["id"]

    return {
        "topic_id": topic_id,
        "title": topic["title"],
        "url": f"{BASE_URL}/t/{topic['slug']}/{topic_id}",
        "post_number": opening_post["post_number"],
        "username": opening_post["username"],
        "raw": opening_post["raw"],
    }

def fetch_opening_post(
    topic_id: int,
    *,
    session: requests.Session | None = None,
) -> dict[str, Any]:
    client = session or requests.Session()
    client.headers.update(
        {
            "Accept": "application/json",
            "User-Agent": "tech-phrase-learning/0.1",
        }
    )

    response = client.get(
        f"{BASE_URL}/t/{topic_id}.json",
        params={"include_raw": "true"},
        timeout=30,
    )
    response.raise_for_status()

    topic = response.json()
    posts = extract_posts(topic)

    opening_post = next(
        (
            post
            for post in posts
            if post.get("post_number") == 1
        ),
        None,
    )

    if opening_post is None:
        raise ValueError(
            f"Topic {topic_id} has no visible opening post"
        )

    if not opening_post.get("raw"):
        raise ValueError(
            f"Topic {topic_id} opening post has no raw text"
        )

    return extract_opening_post_record(topic, opening_post)

import re


def to_question_candidate_text(raw: str) -> str:
    without_code = re.sub(
        r"```.*?```",
        "[code omitted]",
        raw,
        flags=re.DOTALL,
    )

    paragraphs = [
        paragraph.strip()
        for paragraph in without_code.split("\n\n")
        if paragraph.strip()
    ]

    selected_indexes: set[int] = set()

    for index, paragraph in enumerate(paragraphs):
        if "?" in paragraph:
            selected_indexes.add(index)

            if index > 0:
                selected_indexes.add(index - 1)

    if paragraphs:
        selected_indexes.add(len(paragraphs) - 1)

    selected = [
        paragraphs[index]
        for index in sorted(selected_indexes)
    ]

    return "\n\n".join(selected)

if __name__ == "__main__":
    import json

    TOPIC_IDS = [
        107565,  # standardizing build backend support
        107491,  # PEP 541 uncovered case
        107484,  # new archival distribution format
        107705,  # platform_architecture field proposal
        106702,  # ambiguity in PEP 643
        104839,  # standardizing index error responses
    ]

    for topic_id in TOPIC_IDS:
        try:
            record = fetch_opening_post(topic_id)

            # shorten output
            record = {
                "topic_id": record["topic_id"],
                "title": record["title"],
                "text": to_question_candidate_text(record["raw"])
            }

            print(json.dumps(record, ensure_ascii=False))
        except Exception as exc:
            print(
                json.dumps(
                    {
                        "topic_id": topic_id,
                        "error": str(exc),
                    },
                    ensure_ascii=False,
                )
            )