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

def print_tree(node: PostNode, depth: int = 0) -> None:
    indentation = "  " * depth
    preview = (node.raw or "").replace("\n", " ")#[:80]

    print(
        f"{indentation}#{node.post_number} "
        f"@{node.username}: {preview}"
    )

    for child in node.children:
        print_tree(child, depth + 1)


def display_tree(topic_id) -> None:

    topic, posts = fetch_all_topic_posts(topic_id)
    tree = build_conversation_tree(posts)

    print(topic["title"])
    print_tree(tree)

    print()

def main() -> None:
    TOPIC_IDS = [107565]
    
    for topic_id in TOPIC_IDS:
        display_tree(topic_id)

if __name__ == "__main__":
    main()