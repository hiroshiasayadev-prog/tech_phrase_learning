from __future__ import annotations

import requests
import re

BASE_URL = "https://discuss.python.org"
PACKAGING_CATEGORY_SLUG = "packaging"
PACKAGING_CATEGORY_ID = 14


def fetch_topics(
    *,
    max_pages: int = 3,
    category_slug: str | None = None,
    category_id: int | None = None,
) -> list[dict]:
    if (category_slug is None) != (category_id is None):
        raise ValueError("category_slug and category_id must be provided together")

    if category_slug is not None:
        endpoint = f"{BASE_URL}/c/{category_slug}/{category_id}/l/latest.json"
    else:
        endpoint = f"{BASE_URL}/latest.json"

    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/json",
            "User-Agent": "tech-phrase-learning/0.1",
        }
    )

    topics_by_id: dict[int, dict] = {}

    for page in range(max_pages):
        response = session.get(
            endpoint,
            params={
                "order": "created",
                "page": page,
            },
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()
        topics = data.get("topic_list", {}).get("topics", [])

        if not topics:
            break

        for topic in topics:
            topic_id = topic["id"]

            topics_by_id[topic_id] = {
                "id": topic_id,
                "title": topic["title"],
                "slug": topic["slug"],
                "category_id": topic.get("category_id"),
                "created_at": topic.get("created_at"),
                "url": f"{BASE_URL}/t/{topic['slug']}/{topic_id}",
            }

    return list(topics_by_id.values())

def reject_by_title(title: str) -> str | None:
    normalized = title.casefold()

    if normalized.startswith("announcement:"):
        return "announcement"

    if re.search(r"\b(?:now\s+)?released(?:\s+on\s+pypi)?\b", normalized):
        return "release notice"

    if re.search(r"\b(?:summit|conference|meetup|workshop)\b", normalized):
        return "event notice"

    return None

def main() -> None:
    # First-MVP collection scope: Packaging and its subcategories.
    topics = fetch_topics(
        max_pages=3,
        category_slug=PACKAGING_CATEGORY_SLUG,
        category_id=PACKAGING_CATEGORY_ID,
    )

    candidates = []
    rejected = []
    for topic in topics:
        if reject_by_title(topic['title']) is None:
            candidates.append(topic)
        else:
            rejected.append(topic)

    for kind, filtered_topics in [
        ("CANDIDATES", candidates),
        ("REJECTED", rejected)
    ]:
        print(kind)
        for topic in filtered_topics:
            print(
                f"{topic['id']} [category_id={topic['category_id']}]: "
                f"{topic['title']}"
            )
            # print(f"  {topic['url']}")
        print()


if __name__ == "__main__":
    main()