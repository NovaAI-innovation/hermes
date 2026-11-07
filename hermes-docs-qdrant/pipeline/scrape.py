#!/usr/bin/env python3
"""Scrape every llms.txt in sources.yaml into sources/<name>/docs/.

    python scrape.py                    # all sources
    python scrape.py --source hermes    # one source
    python scrape.py --list             # show registry
    python scrape.py --refresh          # re-scrape existing pages
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urldefrag, urlparse

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent))

import paths  # noqa: E402
from common import parse_front_matter  # noqa: E402
from sources import Source, load_sources  # noqa: E402

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


@dataclass(frozen=True)
class DocLink:
    title: str
    url: str


def parse_llms_text(text: str, source: Source) -> list[DocLink]:
    seen: set[str] = set()
    links: list[DocLink] = []
    for title, url in LINK_RE.findall(text):
        url = urldefrag(url).url.rstrip("/")
        if url in seen or not source.allows(url):
            continue
        seen.add(url)
        links.append(DocLink(title=title.strip(), url=url))
    return links


def primary_host(source: Source) -> str:
    return source.doc_host or urlparse(source.llms_txt).netloc


def url_to_output_path(url: str, out_dir: Path, source: Source | None = None) -> Path:
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if any(part in {".", ".."} or "\\" in part or ":" in part for part in parts):
        raise ValueError(f"Unsafe documentation path: {parsed.path}")
    # Drop a leading 'docs' segment so paths stay short and stable.
    if parts and parts[0] in {"docs", "documentation"}:
        parts = parts[1:]
    rel = "/".join(parts) or "index"
    # llms.txt files often link straight to .md/.mdx/.html — normalize the stub.
    rel = re.sub(r"\.(md|mdx|markdown|html?)$", "", rel, flags=re.IGNORECASE)
    # Only scope by host when the URL leaves the source's own site; otherwise
    # every file would land under a redundant _host/ directory.
    own_host = primary_host(source) if source else ""
    if parsed.netloc and parsed.netloc != own_host:
        host_dir = parsed.netloc.replace(":", "_")
        rel = f"_{host_dir}/{rel}"
    target = out_dir / f"{rel}.md"
    if not target.resolve().is_relative_to(out_dir.resolve()):
        raise ValueError(f"Documentation path escapes its source: {parsed.path}")
    return target


RAW_MARKDOWN_RE = re.compile(r"\.(md|mdx|markdown)$", re.IGNORECASE)


async def fetch_raw_markdown(client: httpx.AsyncClient, url: str) -> str | None:
    """llms.txt commonly points at raw .md files; fetch those directly.

    Returns None when the URL is not raw markdown so the caller can crawl it.
    """
    if not RAW_MARKDOWN_RE.search(urlparse(url).path):
        return None
    resp = await client.get(url)
    resp.raise_for_status()
    if "html" in resp.headers.get("content-type", ""):
        return None  # a rendered page, not raw source
    if not resp.text.strip():
        raise ValueError("Empty Markdown response")
    return resp.text


# --------------------------------------------------------------- crawl4ai


async def fetch_llms(url: str, local: Path | None = None) -> str:
    if local is not None:
        return local.read_text(encoding="utf-8")
    async with httpx.AsyncClient(follow_redirects=True, timeout=60) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.text


def markdown_body(result) -> str:
    md = result.markdown
    if md is None:
        return ""
    if hasattr(md, "raw_markdown"):
        return md.raw_markdown or ""
    return md if isinstance(md, str) else str(md)


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


async def scrape_source(
    source: Source,
    links: list[DocLink],
    out_dir: Path,
    concurrency: int,
    batch_size: int,
    skip_existing: bool,
) -> dict:
    # crawl4ai is imported lazily below; it is scrape-time only.
    url_to_link = {link.url: link for link in links}
    urls = [link.url for link in links]
    if skip_existing:
        pending = []
        for url in urls:
            page = url_to_output_path(url, out_dir, source)
            if page.is_file():
                try:
                    meta, body = parse_front_matter(page.read_text(encoding="utf-8"))
                except UnicodeError:
                    pending.append(url)
                    continue
                if meta.get("success", "true").lower() != "false" and meta.get("source", url) == url and body.strip():
                    continue
            pending.append(url)
        urls = pending

    stats = {
        "source": source.name,
        "total": len(links),
        "queued": len(urls),
        "ok": 0,
        "failed": 0,
        "raw_markdown": 0,
        "errors": [],
    }
    if not urls:
        return stats

    # llms.txt files that point at raw .md are copied verbatim: no browser, no
    # chrome to strip, and the source is already clean markdown.
    crawl_urls: list[str] = []
    async with httpx.AsyncClient(follow_redirects=True, timeout=45) as client:
        for url in urls:
            try:
                raw = await fetch_raw_markdown(client, url)
            except (httpx.HTTPError, ValueError) as exc:
                stats["failed"] += 1
                stats["errors"].append({"url": url, "error": str(exc)})
                continue
            if raw is None:
                crawl_urls.append(url)
                continue

            link = url_to_link[url]
            out_path = url_to_output_path(link.url, out_dir, source)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            front = [
                "---",
                f'title: "{link.title.replace(chr(34), chr(39))}"',
                f"source: {link.url}",
                f"scraped_at: {datetime.now(timezone.utc).isoformat()}",
                "success: True",
                "raw_markdown: True",
                "---",
            ]
            out_path.write_text("\n".join(front) + "\n\n" + raw, encoding="utf-8")
            stats["raw_markdown"] += 1
            stats["ok"] += 1

    if not crawl_urls:
        return stats

    # crawl4ai is scrape-time only and is intentionally NOT a plugin
    # dependency: it pins snowballstemmer<3, which conflicts with Hermes core's
    # snowballstemmer==3.1.1 on Python >= 3.14. Without it, raw-markdown
    # sources still work; only HTML crawling needs it.
    try:
        from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
        from crawl4ai.async_dispatcher import SemaphoreDispatcher
    except ImportError as exc:  # noqa: BLE001
        raise RuntimeError(
            f"{len(crawl_urls)} URL(s) need HTML crawling but crawl4ai is not "
            "installed.\n"
            "  pip install 'crawl4ai>=0.8.6'  (use a build env: it conflicts "
            "with Hermes core on Python 3.14)"
        ) from exc

    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
    dispatcher = SemaphoreDispatcher(semaphore_count=concurrency)

    async with AsyncWebCrawler() as crawler:
        for i in range(0, len(crawl_urls), batch_size):
            batch = crawl_urls[i : i + batch_size]
            print(f"  [{source.name}] batch {i // batch_size + 1}: {len(batch)} URLs", flush=True)
            results = await crawler.arun_many(batch, config=config, dispatcher=dispatcher)
            completed = set()
            for result in results:
                url = result.url.rstrip("/")
                if url not in batch or url in completed:
                    continue
                completed.add(url)
                link = url_to_link[url]
                out_path = url_to_output_path(link.url, out_dir, source)
                body = markdown_body(result)
                if not result.success or (result.status_code or 0) >= 400 or not body.strip():
                    stats["failed"] += 1
                    reason = result.error_message or f"No usable Markdown (HTTP {result.status_code})"
                    stats["errors"].append({"url": link.url, "error": reason})
                    continue
                stats["ok"] += 1
                write_page(out_path, link, body, result)
            for missing in set(batch) - completed:
                stats["failed"] += 1
                stats["errors"].append({"url": missing, "error": "No crawl result"})
    return stats


# ------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", help="limit to named source(s)")
    parser.add_argument("--list", action="store_true", help="show the registry and exit")
    parser.add_argument("--registry", type=Path, default=None, help="alternate sources.yaml")
    parser.add_argument("--refresh", action="store_true", help="re-scrape existing pages")
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--batch-size", type=int, default=25)
    args = parser.parse_args()

    sources = load_sources(args.registry)
    if args.source:
        wanted = set(args.source)
        unknown = wanted - {s.name for s in sources}
        if unknown:
            print(f"unknown source(s): {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2
        sources = [s for s in sources if s.name in wanted]

    if args.list:
        for src in sources:
            print(f"{src.name:20} {src.title}")
            print(f"{'':20} {src.llms_txt}")
        return 0

    all_stats = []
    for source in sources:
        print(f"\n=== {source.name} ({source.title}) ===", flush=True)
        source.dir.mkdir(parents=True, exist_ok=True)
        local = None if source.is_remote else Path(source.llms_txt)
        try:
            text = asyncio.run(fetch_llms(source.llms_txt, local))
        except Exception as exc:  # noqa: BLE001
            print(f"  failed to fetch llms.txt: {exc}", file=sys.stderr)
            all_stats.append({"source": source.name, "error": str(exc)})
            continue

        links = parse_llms_text(text, source)
        print(f"  {len(links)} links after include/exclude filters")

        pruned = source.prune_versions(links)
        if len(pruned) != len(links):
            print(
                f"  {len(pruned)} links after keeping only the newest version tree "
                f"({len(links) - len(pruned)} older-version pages dropped)"
            )
        links = pruned

        if not links:
            error = "No documentation links matched the configured source"
            print(f"  {source.name}: {error}", file=sys.stderr)
            all_stats.append({"source": source.name, "error": error})
            continue

        # A page may be advertised both as HTML and as Markdown. Prefer Markdown.
        by_path = {}
        for link in links:
            output = url_to_output_path(link.url, source.docs_dir, source)
            if output not in by_path or RAW_MARKDOWN_RE.search(urlparse(link.url).path):
                by_path[output] = link

        try:
            stats = asyncio.run(scrape_source(
                source, list(by_path.values()), source.docs_dir,
                args.concurrency, args.batch_size, skip_existing=not args.refresh,
            ))
        except Exception as exc:
            print(f"  {source.name}: {exc}", file=sys.stderr)
            all_stats.append({"source": source.name, "error": str(exc)})
            continue
        if not stats["failed"]:
            source.llms_path.write_text(text, encoding="utf-8")
            (source.dir / "pages.json").write_text(json.dumps(sorted(
                output.relative_to(source.docs_dir).as_posix() for output in by_path
            )), encoding="utf-8")
        all_stats.append(stats)
        for error in stats["errors"][:3]:
            print(f"  {source.name}: {error['url']}: {error['error']}", file=sys.stderr)
        print(
            f"  ok={stats['ok']} failed={stats['failed']} queued={stats['queued']}"
            f" raw_md={stats.get('raw_markdown', 0)}"
        )

    manifest = paths.ensure_home() / "scrape_manifest.json"
    manifest.write_text(json.dumps(all_stats, indent=2), encoding="utf-8")

    total_ok = sum(s.get("ok", 0) for s in all_stats)
    total_fail = sum(s.get("failed", 0) + int("error" in s) for s in all_stats)
    print(f"\nDone: {total_ok} ok, {total_fail} failed across {len(all_stats)} source(s)")
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main())
