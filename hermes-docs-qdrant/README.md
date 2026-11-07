# hermes-docs-qdrant

Hermes Agent plugin exposing the scraped Hermes documentation as Qdrant-backed agent tools.

- **Corpus:** 249 pages → ~4.6k chunks, each carrying `doc_id`, `heading`, `source_url`, `doc_type`, `section`, `breadcrumb`.
- **Vectors:** dense `qwen/qwen3-embedding-4b` (2,560-dim, via OpenRouter) + sparse `Qdrant/bm25` (FastEmbed), fused with RRF.
- **Tools:** `docs_search`, `docs_read`, `docs_outline`.

## Install

```powershell
# 1. Ingest the corpus into Qdrant (server, or embedded local store)
cd hermes-docs-qdrant
python ingest.py --url http://localhost:6333 --recreate

# 2. Install into Hermes
hermes plugins install ./hermes-docs-qdrant
hermes plugins doctor ./hermes-docs-qdrant
hermes plugins enable hermes-docs-qdrant
```

Restart Hermes after enabling. Tools appear in the `hermes_docs` toolset and hide themselves (`check_fn`) when Qdrant is unreachable.

## Configuration

Set via `config.yaml` under the plugin's namespace, or environment variables:

| Setting | Env | Default |
|---|---|---|
| Qdrant URL | `QDRANT_URL` | — (embedded store) |
| Qdrant API key | `QDRANT_API_KEY` | — |
| Embedded store path | `QDRANT_PATH` | `<plugin>/.data/qdrant` |
| Collection | `HERMES_DOCS_COLLECTION` | `hermes_docs` |
| Embedding model | `HERMES_DOCS_EMBED_MODEL` | `qwen/qwen3-embedding-4b` |
| Embedding endpoint | `HERMES_DOCS_EMBED_BASE` | `https://openrouter.ai/api/v1` |
| Result count | `HERMES_DOCS_TOP_K` | `6` |

Requires `OPENROUTER_API_KEY` (also used by the Host's install prompt via `requires_env`).

## Tools

| Tool | Purpose |
|---|---|
| `docs_search` | Hybrid search with optional `doc_type` / `section` filters. Returns ranked passages + `source_url`. |
| `docs_read` | Full page by `doc_id` (concatenated chunks, truncatable). |
| `docs_outline` | Corpus outline (sections + counts) or one page's headings. |

All handlers return JSON and never raise.

## Verify without credentials

```powershell
python test_offline.py   # stub embedder; proves schema, ingest, hybrid query, filters, reads
```

## Notes

- Payload indexes are created only in server mode; the embedded store ignores them.
- On RRF fusion the filter must be attached to each `Prefetch` leg — a top-level `query_filter` is silently bypassed. `store.py` does this; keep it that way if you edit the query.
- Point ids are a stable `blake2b` hash of `chunk_id`, so re-ingesting the same corpus is idempotent.
