# hermes-docs-qdrant

Self-contained documentation corpus plugin for Hermes Agent. It scrapes one or
more `llms.txt` sources, normalizes and chunks them into a single corpus,
embeds with `qwen/qwen3-embedding-4b`, and serves hybrid retrieval as agent
tools.

- **Sources:** any number, declared in `sources.yaml` (Hermes, llms.txt spec, Portkey, …).
- **Vectors:** dense `qwen/qwen3-embedding-4b` (2,560-dim, via OpenRouter) + sparse `Qdrant/bm25` (FastEmbed), fused with RRF.
- **Tools:** `docs_search`, `docs_read`, `docs_outline`.

## Where data lives

**Nothing generated is written into the plugin directory.** Hermes replaces the
install tree on `hermes plugins update` and deletes it on `remove`, so corpus and
vector data live in the plugin data home instead (`pipeline/paths.py`):

| Priority | Location | When |
|---|---|---|
| 1 | `$HERMES_DOCS_HOME` | explicit override |
| 2 | `$HERMES_HOME/plugin-data/hermes-docs-qdrant/` | installed in Hermes |
| 3 | `<plugin>/.data/` | standalone git checkout |

Layout under that home:

```
<home>/sources.yaml          user-editable registry (seeded from default_sources.yaml)
<home>/sources/<name>/       llms.txt, docs/, clean/
<home>/corpus/               documents.jsonl, chunks.jsonl, parents.jsonl
<home>/qdrant/               embedded Qdrant store
<home>/.env                  optional, standalone
```

The packaged `default_sources.yaml` is copied to the home on first use and never
overwritten, so upgrades keep your edits.

## Install

```powershell
hermes plugins install ./hermes-docs-qdrant
hermes plugins enable hermes-docs-qdrant
```

Then, once, to build the corpus and vector store:

```powershell
cd $env:HERMES_HOME\plugin-data\hermes-docs-qdrant
python -m hermes_docs_qdrant.cli fetch --recreate
```

Or from a checkout, `python cli.py fetch --recreate` — the CLI resolves the same
home either way. Restart Hermes after enabling; tools appear in the
`hermes_docs` toolset and hide themselves (`check_fn`) when Qdrant is
unreachable.

## CLI

| Command | Purpose |
|---|---|
| `python cli.py init` | create the data home, seed `sources.yaml`, print paths |
| `python cli.py sources` | list registered sources and their directories |
| `python cli.py scrape [--source X] [--refresh]` | llms.txt → `sources/<name>/docs/` |
| `python cli.py build` | normalize → enrich → chunk |
| `python cli.py index [--recreate]` | embed `chunks.jsonl` into Qdrant |
| `python cli.py fetch` | scrape + build + index |
| `python cli.py status` | data home, per-source counts, collection health |
| `python cli.py search "query"` | retrieval smoke test |

## Adding a source

Edit `<home>/sources.yaml`:

```yaml
sources:
  - name: mysource
    title: My Docs
    llms_txt: https://example.com/llms.txt
    doc_host: docs.example.com   # only when links point at another host
```

Then `python cli.py scrape --source mysource && python cli.py build && python cli.py index`.

## Configuration

Environment variables or the plugin's `config.yaml` namespace:

| Setting | Env | Default |
|---|---|---|
| Data home | `HERMES_DOCS_HOME` | Hermes `plugin-data` dir, else `<plugin>/.data` |
| Qdrant URL | `QDRANT_URL` | — (embedded store under the home) |
| Qdrant API key | `QDRANT_API_KEY` | — |
| Collection | `HERMES_DOCS_COLLECTION` | `hermes_docs` |
| Embedding model | `HERMES_DOCS_EMBED_MODEL` | `qwen/qwen3-embedding-4b` |
| Embedding endpoint | `HERMES_DOCS_EMBED_BASE` | `https://openrouter.ai/api/v1` |
| Result count | `HERMES_DOCS_TOP_K` | `6` |

Requires `OPENROUTER_API_KEY` (declared in `plugin.yaml` so the host prompts for it).

## Tools

| Tool | Purpose |
|---|---|
| `docs_search` | Hybrid search; filters on `doc_type`, `section`, `source`. Returns ranked passages + `source_url`. |
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
- Ingest retries 429/5xx with exponential backoff; a full rebuild is thousands of batches.
