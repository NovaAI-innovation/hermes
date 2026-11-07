---
title: "Changelog"
source: https://modelcontextprotocol.io/specification/draft/changelog.md
scraped_at: 2026-11-07T19:29:38.553996+00:00
success: True
raw_markdown: True
---

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

Changes since the most recent release will accumulate here.

## Other schema changes

1. Restore the optional `_meta` field on `CreateMessageRequestParams`, `ElicitRequestFormParams`, `ElicitRequestURLParams`, `ElicitResult`, and `ListRootsResult`. It was unintentionally dropped in 2026-07-28 when these types stopped extending `TaskAugmentedRequestParams` and `Result`, leaving `ListRootsRequest` as the only input request that could carry `_meta` ([#3468](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3468)).
