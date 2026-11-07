#!/usr/bin/env python3
"""Scrape all doc URLs from Hermes llms.txt via Crawl4AI and save as markdown."""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import httpx
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.async_dispatcher import SemaphoreDispatcher

LLMS_URL = "https://hermes-agent.nousresearch.com/docs/llms.txt"
DOCS_PREFIX = "https://hermes-agent.nousresearch.com/docs/"
LINK_RE = re.compile(r"\[([^\]]+)\]\((https://hermes-agent\.nousresearch\.com/docs/[^)]+)\)")


@dataclass(frozen=True)
class DocLink:
    title: str
    url: str


def parse_llms_text(text: str) -> list[DocLink]:
    seen: set[str] = set()
    links: list[DocLink] = []
    for title, url in LINK_RE.findall(text):
        url = url.rstrip("/")
        if url in seen:
            continue
        seen.add(url)
        links.append(DocLink(title=title.strip(), url=url))
    return links


def url_to_output_path(url: str, out_dir: Path) -> Path:
    parsed = urlparse(url)
    rel = parsed.path.removeprefix("/docs/").strip("/")
    if not rel:
        rel = "index"
    return out_dir / f"{rel}.md"


def markdown_body(result) -> str:
    md = result.markdown
    if md is None:
        return ""
    if hasattr(md, "raw_markdown") and md.raw_markdown:
        return md.raw_markdown
    if isinstance(md, str):
        return md
    return str(md)


def write_page(path: Path, link: DocLink, body: str, result) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    front = [
        "---",
        f'title: "{link.title.replace(chr(34), chr(39))}"',
        f"source: {link.url}",
        f"scraped_at: {datetime.now(timezone.utc).isoformat()}",
        f"success: {result.success}",
    ]
    if result.status_code is not None:
        front.append(f"status_code: {result.status_code}")
    if result.error_message:
        front.append(f'error: "{result.error_message[:200]}"')
    front.append("---")
    path.write_text("\n".join(front) + "\n\n" + body, encoding="utf-8")


async def fetch_llms(url: str) -> str:
    async with httpx.AsyncClient(follow_redirects=True, timeout=60) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.text


def resolve_link(url_by_link: dict[str, DocLink], result_url: str) -> DocLink:
    key = result_url.rstrip("/")
    if key in url_by_link:
        return url_by_link[key]
    for k, v in url_by_link.items():
        if key == k.rstrip("/"):
            return v
    return DocLink(title=result_url, url=result_url)


def record_result(
    out_dir: Path,
    url_by_link: dict[str, DocLink],
    result,
    stats: dict,
) -> None:
    link = resolve_link(url_by_link, result.url)
    out_path = url_to_output_path(link.url, out_dir)
    body = markdown_body(result)
    if not result.success and not body:
        body = f"# Failed to scrape\n\n{result.error_message or 'Unknown error'}\n"
        stats["failed"] += 1
        stats["errors"].append({"url": link.url, "error": result.error_message})
    else:
        stats["ok"] += 1
    write_page(out_path, link, body, result)
    print(f"[{'OK' if result.success else 'FAIL'}] {out_path.relative_to(out_dir)}")


async def scrape(
    links: list[DocLink],
    out_dir: Path,
    concurrency: int,
    skip_existing: bool,
    batch_size: int,
) -> dict:
    url_by_link = {link.url.rstrip("/"): link for link in links}
    urls = [link.url for link in links]
    if skip_existing:
        urls = [u for u in urls if not url_to_output_path(u, out_dir).exists()]

    stats = {"total": len(links), "queued": len(urls), "ok": 0, "failed": 0, "errors": []}

    if not urls:
        return stats

    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
    dispatcher = SemaphoreDispatcher(semaphore_count=concurrency)

    async with AsyncWebCrawler() as crawler:
        for i in range(0, len(urls), batch_size):
            batch = urls[i : i + batch_size]
            print(f"Batch {i // batch_size + 1}: {len(batch)} URLs")
            results = await crawler.arun_many(batch, config=config, dispatcher=dispatcher)
            for result in results:
                record_result(out_dir, url_by_link, result, stats)

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--llms-url", default=LLMS_URL)
    parser.add_argument("--llms-file", type=Path, help="Local llms.txt instead of downloading")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "docs",
    )
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--skip-existing", action="store_true", default=True)
    parser.add_argument("--no-skip-existing", action="store_false", dest="skip_existing")
    args = parser.parse_args()

    out_dir = args.output_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.llms_file:
        llms_text = args.llms_file.read_text(encoding="utf-8")
    else:
        llms_text = asyncio.run(fetch_llms(args.llms_url))

    (out_dir.parent / "llms.txt").write_text(llms_text, encoding="utf-8")
    links = parse_llms_text(llms_text)
    print(f"Found {len(links)} unique doc links")

    stats = asyncio.run(
        scrape(links, out_dir, args.concurrency, args.skip_existing, args.batch_size)
    )
    manifest = out_dir.parent / "scrape_manifest.json"
    manifest.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(f"Done: {stats['ok']} ok, {stats['failed']} failed -> {out_dir}")
    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
