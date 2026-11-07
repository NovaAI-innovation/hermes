# hermes-docs-qdrant

Self-contained documentation corpus plugin for Hermes Agent. It scrapes one or
more `llms.txt` sources, normalizes and chunks them into a single corpus,
embeds with `qwen/qwen3-embedding-4b`, and serves hybrid retrieval as agent
tools.

- **Sources:** any number, declared in `sources.yaml` (Hermes, llms.txt spec, Portkey, …).
- **Vectors:** dense `qwen/qwen3-embedding-4b` (2,560-dim, via OpenRouter) + sparse `Qdrant/bm25` (FastEmbed), fused with RRF.
- **Tools:** 8 — retrieval (`docs_search`, `docs_search_many`, `docs_read`), discovery (`docs_outline`, `docs_list`, `docs_stats`), diagnosis (`docs_diagnostics`), and lifecycle (`docs_rebuild`).

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

## Two dependency sets

The plugin ships with **runtime-only** dependencies (`plugin.yaml`): `qdrant-client`, `fastembed`, `openai`, `httpx`, `pyyaml`. It deliberately does **not** depend on the corpus toolchain.

`crawl4ai` pins `snowballstemmer<3`, and Hermes core requires
`snowballstemmer==3.1.1` on Python 3.14 — declaring it made `hermes plugins
enable` refuse the plugin as unsatisfiable. Since `crawl4ai` is only needed to
*crawl HTML pages*, it lives in the build step instead:

```powershell
# Build env (yours, not Hermes's) — full toolchain
python install.py --with-build       # creates .venv-build, installs requirements-build.txt

# Hermes env — runtime only, resolved from plugin.yaml
hermes plugins install ./hermes-docs-qdrant
```

`requirements.txt` at the repo root is the **runtime** set and is safe to
install into the Hermes environment; `requirements-build.txt` is the corpus
toolchain and must not be. `cli.py scrape` imports `crawl4ai` lazily and raises
a clear message naming the missing package if HTML sources are queued without
it. Raw-markdown `llms.txt` sources need only `httpx` and work either way.

## Install

**One command**, from the plugin directory:

```powershell
python install.py                 # verify + install runtime deps + doctor
python install.py --check         # verify only, change nothing
python install.py --with-build    # also create .venv-build for scraping
python install.py --restart       # restart the gateway afterwards
```

Then in Hermes:

```powershell
hermes plugins install ./hermes-docs-qdrant
hermes plugins enable hermes-docs-qdrant
hermes gateway restart            # a running process never switches envs
```

Then, once, to build the corpus and vector store:

```powershell
python cli.py fetch --recreate
```

`install.py` exists because the failure mode is silent. `hermes plugins install`
resolves `plugin.yaml` and the tools register, but the **running** Hermes
interpreter is a separate environment: if it cannot import `qdrant_client`, every
`check_fn` returns False and the whole toolset disappears with no error. The
installer installs into the interpreter that is actually running, then proves it
with three tests and a `doctor` report.

## Why the dependency floor is 1.10.0

`store.py` drives `client.query_points()`, `qm.Prefetch` and `qm.FusionQuery`
for dense+BM25 RRF fusion. None of those exist before `qdrant-client 1.10.0`.
The manifest previously said `>=1.9.0`, which let a resolver install a client
the code could not drive — tools registered, then hid themselves.

The floor is now stated in three places that `test_contract.py` keeps in sync:

| File | Role |
|---|---|
| `plugin.yaml` | what Hermes resolves when installing the plugin |
| `requirements-runtime.txt` | what `install.py` / a manual repair installs |
| `compat.py` | what the tools check and report at runtime |

`compat.py` also asserts the three APIs are present on the installed client, so
a floor that is wrong in the future fails loudly instead of silently.

## When the tools are missing

Call `docs_diagnostics` — it is registered with `check_fn=None`, so it answers
in exactly the state that hides every other tool. It reports each dependency,
its installed and required version, whether it is hard or soft, the collection
target, reachability, and the remediation command.

The rule the plugin now follows:

- **Hard** dependency missing or too old (`qdrant-client`, `openai`) → tools are
  disabled, and an `ERROR` naming the package is logged at registration.
- **Soft** dependency missing (`fastembed`, `pyyaml`, `httpx`) → tools stay
  available, the feature degrades (sparse fusion or the CLI), and a `WARNING` is
  logged. A missing optional package must never hide retrieval.

```powershell
python cli.py doctor   # python, every dependency, collection health, next step
```

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
| `python cli.py doctor` | dependency contract + collection health, with the fix |
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

Requires `OPENROUTER_API_KEY` (declared in `plugin.yaml` so the host prompts for it). Without it, the tools register and the corpus is readable, but `docs_search` cannot embed the query; `docs_diagnostics` reports the missing credential rather than the search failing with a bare `KeyError`.

## Tools

| Tool | Purpose |
|---|---|
| `docs_search` | Hybrid (dense + BM25, RRF) search with filters on `source`, `doc_type`, `section`. Returns ranked passages + `source_url`. |
| `docs_search_many` | Several queries in one call, results grouped per query. For comparing sub-questions. |
| `docs_read` | Full page by source-qualified `doc_id`, reassembled in chunk order. |
| `docs_outline` | Corpus overview (sources, doc types, sections, counts) or one page's headings. |
| `docs_list` | Document catalog filtered by `source`, `doc_type`, or `doc_id` prefix. |
| `docs_stats` | Collection health and size, with a per-source breakdown. |
| `docs_diagnostics` | Dependency contract, versions, collection target, reachability, remediation. Ungated — call it when other tools are missing. |
| `docs_rebuild` | Rebuild the corpus from `sources.yaml`: optional re-scrape, then normalize → enrich → chunk → re-index. |

All handlers return JSON and never raise. Retrieval tools hide themselves
(`check_fn`) only on a **hard** dependency failure or an unreachable
collection. `docs_diagnostics` and `docs_rebuild` stay callable precisely so
they can explain and repair that state.

## Verify without credentials

```powershell
python test_contract.py      # manifest / requirements / compat.py bounds agree
python test_availability.py  # hard failure hides + reports; soft failure does not
python test_registration.py  # 8 tools register; search returns cited passages
python test_offline.py       # stub embedder; ingest, hybrid query, filters, reads
```

## Notes

- Dependency bounds live in `plugin.yaml`, `requirements-runtime.txt` and `compat.py`. Edit all three; `test_contract.py` fails if they drift.
- Payload indexes are created only in server mode; the embedded store ignores them.
- On RRF fusion the filter must be attached to each `Prefetch` leg — a top-level `query_filter` is silently bypassed. `store.py` does this; keep it that way if you edit the query.
- Point ids are a stable `blake2b` hash of `chunk_id`, so re-ingesting the same corpus is idempotent.
- Ingest retries 429/5xx with exponential backoff; a full rebuild is thousands of batches.
