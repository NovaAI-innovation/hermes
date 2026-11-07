"""Qdrant store for the Hermes docs corpus: schema, ingest, hybrid retrieval.

Kept dependency-light and side-effect-free at import time so a missing Qdrant
or a missing API key disables the tools instead of breaking Hermes startup.
"""

from __future__ import annotations

import json
import logging
import os
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import wraps
from pathlib import Path
from threading import RLock
from typing import Any
from uuid import uuid4

logger = logging.getLogger(__name__)

DEFAULT_COLLECTION = "hermes_docs"
PLUGIN_ROOT = Path(__file__).resolve().parent
EMBED_MODEL = os.getenv("HERMES_DOCS_EMBED_MODEL", "qwen/qwen3-embedding-4b")
EMBED_BASE = os.getenv("HERMES_DOCS_EMBED_BASE", "https://openrouter.ai/api/v1")
EMBED_DIM = int(os.getenv("HERMES_DOCS_EMBED_DIM", "2560"))
DENSE_VEC = "dense"
SPARSE_VEC = "bm25"
QUERY_INSTRUCTION = (
    "Given a web search query, retrieve relevant passages that answer the query"
)


# --------------------------------------------------------------------- config


@dataclass
class Settings:
    """Resolved connection settings.

    Precedence: explicit config dict > environment > local-mode path.
    """

    url: str | None = None
    api_key: str | None = None
    path: str | None = None
    collection: str = DEFAULT_COLLECTION
    corpus_dir: str | None = None
    top_k: int = 6
    score_floor: float = 0.0
    extras: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def resolve(cls, config: dict | None = None) -> "Settings":
        config = config or {}
        url = config.get("url") or (None if config.get("path") else os.getenv("QDRANT_URL"))
        api_key = config.get("api_key") or os.getenv("QDRANT_API_KEY")
        path = config.get("path") or os.getenv("QDRANT_PATH")
        if not url and not path:
            # Default to an embedded store inside the plugin's data dir so the
            # plugin works with zero infrastructure, then can be repointed.
            path = str(_default_local_path())
        return cls(
            url=url,
            api_key=api_key,
            path=path if not url else None,
            collection=config.get("collection") or os.getenv(
                "HERMES_DOCS_COLLECTION", DEFAULT_COLLECTION
            ),
            corpus_dir=config.get("corpus_dir") or os.getenv("HERMES_DOCS_CORPUS"),
            top_k=int(config.get("top_k") or os.getenv("HERMES_DOCS_TOP_K", 6)),
            score_floor=float(config.get("score_floor", 0.0)),
            extras=config,
        )


def _default_local_path() -> Path:
    """Embedded store under the plugin data home, never the install tree."""
    try:
        from .pipeline import paths  # type: ignore
    except Exception:  # noqa: BLE001 - imported as a top-level script
        try:
            from pipeline import paths  # type: ignore
        except Exception:  # noqa: BLE001
            paths = None
    if paths is not None:
        return paths.qdrant_dir()
    base = os.getenv("HERMES_DOCS_DATA")
    if base:
        return Path(base) / "qdrant"
    return PLUGIN_ROOT / ".data" / "qdrant"


# -------------------------------------------------------------------- embedder


class QueryEmbedder:
    """Embeds queries only; documents are embedded at ingest time."""

    def __init__(self, model: str = EMBED_MODEL, base: str = EMBED_BASE):
        self.model = model
        self.base = base
        self._client = None

    def available(self) -> bool:
        try:
            import openai  # noqa: F401
        except ImportError:
            return False
        return bool(os.getenv("OPENROUTER_API_KEY"))

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI

            key = os.getenv("OPENROUTER_API_KEY")
            if not key:
                # A bare KeyError here reached the agent as "KeyError:
                # 'OPENROUTER_API_KEY'" with no hint about which credential or
                # how to set it. Name the fix instead.
                raise RuntimeError(
                    "OPENROUTER_API_KEY is not set, so queries cannot be "
                    "embedded. Add it to $HERMES_HOME/.env (or the plugin's "
                    "environment) and restart the gateway. "
                    "Call docs_diagnostics to confirm."
                )
            self._client = OpenAI(base_url=self.base, api_key=key, timeout=15, max_retries=1)
        return self._client

    def embed_query(self, text: str) -> list[float]:
        prompt = f"Instruct: {QUERY_INSTRUCTION}\nQuery: {text}"
        resp = self._get_client().embeddings.create(model=self.model, input=[prompt])
        return list(resp.data[0].embedding)


class SparseEmbedder:
    """FastEmbed BM25 sparse vectors; lazily loaded, one model instance."""

    def __init__(self):
        self._model = None

    def available(self) -> bool:
        try:
            import fastembed  # noqa: F401
        except ImportError:
            return False
        return True

    def _get_model(self):
        if self._model is None:
            from fastembed import SparseTextEmbedding

            self._model = SparseTextEmbedding(model_name="Qdrant/bm25")
        return self._model

    def embed(self, texts: list[str]) -> list[tuple[list[int], list[float]]]:
        out = []
        for emb in self._get_model().embed(texts):
            out.append(([int(i) for i in emb.indices], [float(v) for v in emb.values]))
        return out

    def embed_one(self, text: str):
        return self.embed([text])[0]


# ----------------------------------------------------------------------- store


def _locked(method):
    @wraps(method)
    def call(self, *args, **kwargs):
        with self._db_lock:
            return method(self, *args, **kwargs)

    return call


class DocsStore:
    """Hybrid retrieval over the Qdrant collection."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self._db_lock = RLock()
        self._embed_lock = RLock()
        self._client = None
        self._dense = QueryEmbedder()
        self._sparse = SparseEmbedder()

    # -- client ---------------------------------------------------------
    @_locked
    def client(self):
        if self._client is None:
            from qdrant_client import QdrantClient
            # Local (embedded) mode passes path; server mode passes url.
            # Passing both makes qdrant-client prefer the remote and silently
            # ignore the embedded store, so the kwargs are exclusive here.
            if self.settings.url:
                self._client = QdrantClient(
                    url=self.settings.url,
                    api_key=self.settings.api_key,
                    timeout=10,
                )
            else:
                self._client = QdrantClient(
                    path=self.settings.path, timeout=10, force_disable_check_same_thread=True
                )
        return self._client

    @_locked
    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None

    @property
    def active_alias(self) -> str:
        return f"{self.settings.collection}__active"

    @_locked
    def active_collection(self) -> str:
        return self._alias_target() or self.settings.collection

    def _alias_target(self) -> str | None:
        for alias in self.client().get_aliases().aliases:
            if alias.alias_name == self.active_alias:
                return alias.collection_name
        return None

    @_locked
    def publish_collection(self, name: str) -> str | None:
        from qdrant_client.http import models as qm

        client = self.client()
        current = self._alias_target()
        previous = current or self.settings.collection
        actions = []
        if current:
            actions.append(qm.DeleteAliasOperation(delete_alias=qm.DeleteAlias(alias_name=self.active_alias)))
        actions.append(qm.CreateAliasOperation(
            create_alias=qm.CreateAlias(collection_name=name, alias_name=self.active_alias)
        ))
        existed = client.collection_exists(previous)
        if not client.update_collection_aliases(actions):
            raise RuntimeError("Qdrant did not confirm the collection switch")
        return previous if existed else None

    @_locked
    def health(self, collection: str | None = None) -> tuple[bool, str]:
        try:
            client = self.client()
            info = client.get_collection(collection or self.active_collection())
            return True, f"{info.points_count or 0} points"
        except Exception as exc:  # noqa: BLE001 - surface to the model, never raise
            return False, f"{exc.__class__.__name__}: {str(exc)[:200]}"

    def diagnosis(self) -> dict[str, Any]:
        """Full diagnostic snapshot; used by docs_diagnostics and cli.py doctor."""
        from . import compat

        env = compat.check_environment()
        ok, detail = self.health()
        return {
            "dependencies": env,
            "collection": self.settings.collection,
            "reachable": ok,
            "detail": detail,
            "target": self.settings.url or self.settings.path,
            "local_mode": not bool(self.settings.url),
        }


    @_locked
    def ensure_collection(self, name: str) -> None:
        from qdrant_client.http import models as qm

        client = self.client()
        if client.collection_exists(name):
            return

        client.create_collection(
            collection_name=name,
            vectors_config={
                DENSE_VEC: qm.VectorParams(size=EMBED_DIM, distance=qm.Distance.COSINE)
            },
            sparse_vectors_config={
                SPARSE_VEC: qm.SparseVectorParams(modifier=qm.Modifier.IDF)
            },
        )
        # Payload indexes only exist on server-mode Qdrant; local mode ignores them.
        if self.settings.url:
            for field_name in ("doc_type", "section", "doc_id", "source"):
                client.create_payload_index(name, field_name, field_schema="keyword")

    # -- search ---------------------------------------------------------
    def search(
        self,
        query: str,
        limit: int | None = None,
        doc_type: str | None = None,
        section: str | None = None,
        source: str | None = None,
        details: dict | None = None,
    ) -> list[dict]:
        from qdrant_client.http import models as qm

        limit = limit or self.settings.top_k
        conditions = []
        if doc_type:
            conditions.append(
                qm.FieldCondition(key="doc_type", match=qm.MatchValue(value=doc_type))
            )
        if section:
            conditions.append(
                qm.FieldCondition(key="section", match=qm.MatchValue(value=section))
            )
        if source:
            conditions.append(
                qm.FieldCondition(key="source", match=qm.MatchValue(value=source))
            )
        query_filter = qm.Filter(must=conditions) if conditions else None

        vectors = {}
        warnings = []
        with self._embed_lock:
            try:
                vectors[DENSE_VEC] = self._dense.embed_query(query)
            except Exception as exc:
                reason = "OPENROUTER_API_KEY is missing" if not os.getenv("OPENROUTER_API_KEY") else type(exc).__name__
                warnings.append(f"Dense embeddings unavailable ({reason})")
            try:
                if self._sparse.available():
                    indices, values = self._sparse.embed_one(query)
                    if indices:
                        vectors[SPARSE_VEC] = qm.SparseVector(indices=indices, values=values)
                else:
                    warnings.append("BM25 embeddings unavailable (FastEmbed is missing)")
            except Exception as exc:
                warnings.append(f"BM25 embeddings unavailable ({type(exc).__name__})")

        if not vectors:
            raise RuntimeError(f"{' '.join(warnings)} No search vectors available. Call docs_diagnostics.")

        with self._db_lock:
            client = self.client()
            name = self.active_collection()
            options = {
                "collection_name": name,
                "limit": limit,
                "query_filter": query_filter,
                "with_payload": True,
            }
            points = None
            if len(vectors) == 2:
                try:
                    # Each prefetch leg needs its own filter for RRF.
                    points = client.query_points(
                        **options,
                        prefetch=[
                            qm.Prefetch(query=vector, using=kind, filter=query_filter, limit=max(limit * 4, 20))
                            for kind, vector in vectors.items()
                        ],
                        query=qm.FusionQuery(fusion=qm.Fusion.RRF),
                    ).points
                    mode = "hybrid"
                except Exception as exc:
                    warnings.append(f"Hybrid search unavailable ({type(exc).__name__})")
            if points is None:
                for mode, vector in vectors.items():
                    try:
                        points = client.query_points(**options, query=vector, using=mode).points
                        break
                    except Exception as exc:
                        warnings.append(f"{mode} search unavailable ({type(exc).__name__})")
                if points is None:
                    raise RuntimeError(f"{' '.join(warnings)} Call docs_diagnostics.")

        if details is not None:
            details.update(mode=mode)
            if warnings:
                details["warnings"] = warnings
        return [_to_result(p) for p in points if (p.score or 0) >= self.settings.score_floor]

    # -- reads ----------------------------------------------------------
    @_locked
    def get_doc_chunks(self, doc_id: str, limit: int | None = 40) -> list[dict]:
        from qdrant_client.http import models as qm

        client = self.client()
        name = self.active_collection()
        query_filter = qm.Filter(must=[qm.FieldCondition(key="doc_id", match=qm.MatchValue(value=doc_id))])
        rows = []
        offset = None
        while True:
            points, offset = client.scroll(
                collection_name=name, scroll_filter=query_filter, offset=offset,
                limit=256, with_payload=True,
            )
            rows.extend(_to_result(p) for p in points)
            if offset is None:
                break
        rows.sort(key=_chunk_order)
        return rows[:limit]

    @_locked
    def list_sections(self) -> list[dict]:
        """Distinct (section, doc_type) counts for discovery."""
        client = self.client()
        name = self.active_collection()
        counts: dict[tuple[str, str], int] = {}
        offset = None
        while True:
            points, offset = client.scroll(
                collection_name=name,
                limit=512,
                offset=offset,
                with_payload=["section", "doc_type"],
            )
            for p in points:
                payload = p.payload or {}
                key = (payload.get("section", ""), payload.get("doc_type", ""))
                counts[key] = counts.get(key, 0) + 1
            if offset is None:
                break
        return [
            {"section": s, "doc_type": d, "chunks": n}
            for (s, d), n in sorted(counts.items(), key=lambda kv: -kv[1])
        ]

    def search_many(
        self,
        queries: list[str],
        limit: int | None = None,
        doc_type: str | None = None,
        section: str | None = None,
        source: str | None = None,
        errors: dict[str, str] | None = None,
        details: dict[str, dict] | None = None,
    ) -> dict[str, list[dict]]:
        """Run several queries, keeping results separated by query.

        A single query answers "what does the corpus say about X"; several
        compare sub-questions in one call, e.g. ["rerank", "guardrails"].
        """
        out: dict[str, list[dict]] = {}
        for q in dict.fromkeys(query.strip() for query in queries):
            if not q:
                continue
            try:
                query_details = {} if details is not None else None
                out[q] = self.search(
                    q, limit=limit, doc_type=doc_type, section=section, source=source, details=query_details,
                )
                if details is not None:
                    details[q] = query_details
            except Exception as exc:
                if errors is None:
                    raise
                errors[q] = str(exc)
                out[q] = []
        return out

    @_locked
    def list_documents(
        self,
        source: str | None = None,
        doc_type: str | None = None,
        prefix: str | None = None,
        limit: int = 200,
    ) -> list[dict]:
        """Catalog of distinct documents, ordered by doc_id.

        Scrolls chunk payloads and deduplicates; cheaper than scanning the
        corpus JSONL and reflects exactly what the collection holds.
        """
        from qdrant_client.http import models as qm

        conditions = []
        if source:
            conditions.append(
                qm.FieldCondition(key="source", match=qm.MatchValue(value=source))
            )
        if doc_type:
            conditions.append(
                qm.FieldCondition(key="doc_type", match=qm.MatchValue(value=doc_type))
            )

        docs: dict[str, dict] = {}
        offset = None
        client = self.client()
        name = self.active_collection()
        while len(docs) < limit:
            points, offset = client.scroll(
                collection_name=name,
                scroll_filter=qm.Filter(must=conditions) if conditions else None,
                limit=512,
                offset=offset,
                with_payload=["doc_id", "title", "doc_type", "source", "source_url", "section"],
            )
            for p in points:
                payload = p.payload or {}
                doc_id = payload.get("doc_id", "")
                if not doc_id or doc_id in docs:
                    continue
                if prefix and not doc_id.startswith(prefix):
                    continue
                docs[doc_id] = {
                    "doc_id": doc_id,
                    "title": payload.get("title", ""),
                    "doc_type": payload.get("doc_type", ""),
                    "source": payload.get("source", ""),
                    "source_url": payload.get("source_url", ""),
                    "section": payload.get("section", ""),
                }
                if len(docs) >= limit:
                    break
            if offset is None:
                break
        return [docs[k] for k in sorted(docs)]

    @_locked
    def corpus_stats(self) -> dict[str, Any]:
        """Per-source document and chunk counts, plus collection size."""
        counts: dict[str, dict[str, Any]] = {}
        seen_docs: set[str] = set()
        offset = None
        client = self.client()
        name = self.active_collection()
        while True:
            points, offset = client.scroll(
                collection_name=name,
                limit=512,
                offset=offset,
                with_payload=["doc_id", "source", "doc_type"],
            )
            for p in points:
                payload = p.payload or {}
                src = payload.get("source", "") or "unknown"
                bucket = counts.setdefault(
                    src, {"source": src, "chunks": 0, "documents": 0, "doc_types": {}}
                )
                bucket["chunks"] += 1
                doc_id = payload.get("doc_id", "")
                if doc_id and doc_id not in seen_docs:
                    seen_docs.add(doc_id)
                    bucket["documents"] += 1
                dt = payload.get("doc_type", "") or "default"
                bucket["doc_types"][dt] = bucket["doc_types"].get(dt, 0) + 1
            if offset is None:
                break

        ok, detail = self.health(name)
        return {
            "collection": self.settings.collection,
            "active_collection": name,
            "reachable": ok,
            "detail": detail,
            "total_documents": len(seen_docs),
            "total_chunks": sum(b["chunks"] for b in counts.values()),
            "by_source": sorted(counts.values(), key=lambda b: -b["chunks"]),
        }

    def collection_manifest(self, active_collection: str | None = None) -> dict[str, Any] | None:
        """The corpus manifest written at build time, if present."""
        try:
            from .pipeline import paths  # type: ignore
        except Exception:  # noqa: BLE001
            try:
                from pipeline import paths  # type: ignore
            except Exception:  # noqa: BLE001
                return None
        path = Path(self.settings.corpus_dir or paths.corpus_dir()) / "manifest.json"
        if not path.exists():
            return None
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(manifest, dict) or manifest.get("indexed") is False:
                return None
            if active_collection and manifest.get("active_collection", active_collection) != active_collection:
                return None
            return manifest
        except Exception:  # noqa: BLE001
            return None


def _to_result(point) -> dict:
    payload = getattr(point, "payload", None) or {}
    score = getattr(point, "score", None)
    return {
        "chunk_id": payload.get("chunk_id", str(getattr(point, "id", ""))),
        "chunk_index": payload.get("chunk_index"),
        "doc_id": payload.get("doc_id", ""),
        "title": payload.get("title", ""),
        "heading": payload.get("heading", ""),
        "text": payload.get("text", ""),
        "source_url": payload.get("source_url", ""),
        "breadcrumb": payload.get("breadcrumb", []),
        "doc_type": payload.get("doc_type", ""),
        "section": payload.get("section", ""),
        "source": payload.get("source", ""),
        "score": round(float(score or 0.0), 4),
    }


def _chunk_order(row: dict) -> tuple:
    index = row.get("chunk_index")
    if isinstance(index, int):
        return 0, index
    stem, _, suffix = row["chunk_id"].rpartition("~")
    return (1, stem, int(suffix)) if suffix.isdecimal() else (1, row["chunk_id"], 0)


# ---------------------------------------------------------------------- ingest


def chunk_point_id(chunk_id: str) -> int:
    """Stable positive 63-bit id from the chunk id string."""
    import hashlib

    digest = hashlib.blake2b(chunk_id.encode("utf-8"), digest_size=8).digest()
    return int.from_bytes(digest, "big") >> 1


def ingest(
    chunks_path: Path,
    settings: Settings,
    recreate: bool = False,
    batch_size: int = 32,
    limit: int | None = None,
    progress: Callable[[int, int], None] | None = None,
    *,
    store: DocsStore | None = None,
) -> dict:
    """Embed and upsert chunks.jsonl into Qdrant. Returns a stats dict."""
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is required to embed documents")

    rows = [
        json.loads(line)
        for line in chunks_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if limit:
        rows = rows[:limit]
    if not rows:
        raise ValueError("No chunks to index. Check the configured sources and scrape output.")
    if len({row["chunk_id"] for row in rows}) != len(rows):
        raise ValueError("Duplicate chunk IDs in the corpus")

    owns_store = store is None
    store = store or DocsStore(settings)
    try:
        name = f"{settings.collection}__build_{uuid4().hex}" if recreate else store.active_collection()
        try:
            store.ensure_collection(name)
            result = _ingest_rows(rows, store, name, key, batch_size, progress)
            if recreate:
                with store._db_lock:
                    if store.client().count(name, exact=True).count != len(rows):
                        raise RuntimeError("Indexed point count does not match the corpus")
        except Exception:
            if recreate:
                try:
                    with store._db_lock:
                        client = store.client()
                        client.delete_collection(name)
                        if os.name == "nt" and not settings.url:
                            # Embedded Qdrant drops the collection before its SQLite
                            # connection is collected. Windows still locks the files.
                            from gc import collect

                            collect()
                            client.delete_collection(name)
                except Exception:
                    logger.warning("Could not discard staged collection %s", name)
            raise
        # If a server times out during the alias update, it might have committed.
        # Keep the staged collection in that case.
        if recreate:
            result["previous_collection"] = store.publish_collection(name)
        return {**result, "collection": settings.collection, "active_collection": name}
    finally:
        if owns_store:
            store.close()


def _ingest_rows(rows, store, name, key, batch_size, progress) -> dict:
    from openai import OpenAI
    from qdrant_client.http import models as qm

    embedder = OpenAI(base_url=EMBED_BASE, api_key=key, timeout=60, max_retries=0)
    sparse = SparseEmbedder()
    use_sparse = sparse.available()

    started = time.time()
    upserted = 0

    def embed_with_retry(texts: list[str], attempts: int = 6):
        """Embed one batch, backing off on 429/5xx.

        OpenRouter answers `engine_overloaded` under sustained load; a full
        corpus rebuild is thousands of batches, so a single 429 must not abort
        an ingest that is already ~20% done.
        """
        delay = 3.0
        for attempt in range(1, attempts + 1):
            try:
                return embedder.embeddings.create(model=EMBED_MODEL, input=texts)
            except Exception as exc:  # noqa: BLE001
                status = getattr(exc, "status_code", None)
                if attempt == attempts or (status is not None and status not in (429, 500, 502, 503, 504)):
                    raise
                print(
                    f"  retry {attempt}/{attempts - 1} after {delay:.0f}s ({status or exc.__class__.__name__})",
                    flush=True,
                )
                time.sleep(delay)
                delay = min(delay * 2, 60.0)

    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        texts = [r.get("embed_text") or r["text"] for r in batch]
        resp = embed_with_retry(texts)
        ordered = sorted(resp.data, key=lambda item: item.index)
        if [item.index for item in ordered] != list(range(len(batch))):
            raise RuntimeError("Embedding provider returned an incomplete batch")
        dense = [list(item.embedding) for item in ordered]
        sparse_vecs = sparse.embed(texts) if use_sparse else [None] * len(batch)
        if len(sparse_vecs) != len(batch):
            raise RuntimeError("Sparse embedder returned an incomplete batch")

        points = []
        for row, dvec, svec in zip(batch, dense, sparse_vecs):
            vector: dict[str, Any] = {DENSE_VEC: dvec}
            if svec is not None:
                vector[SPARSE_VEC] = qm.SparseVector(indices=svec[0], values=svec[1])
            points.append(
                qm.PointStruct(
                    id=chunk_point_id(row["chunk_id"]),
                    vector=vector,
                    payload={
                        "chunk_id": row["chunk_id"],
                        "chunk_index": row.get("chunk_index"),
                        "doc_id": row["doc_id"],
                        "title": row.get("title", ""),
                        "heading": row.get("heading", ""),
                        "text": row["text"],
                        "source_url": row.get("source_url", ""),
                        "breadcrumb": row.get("breadcrumb", []),
                        "doc_type": row.get("doc_type", ""),
                        "section": row.get("section", ""),
                        "source": row.get("corpus_source", ""),
                        "doc_summary": row.get("doc_summary", ""),
                    },
                )
            )

        with store._db_lock:
            store.client().upsert(collection_name=name, points=points, wait=True)
        upserted += len(points)
        if progress:
            progress(upserted, len(rows))

    return {
        "upserted": upserted,
        "sparse": use_sparse,
        "seconds": round(time.time() - started, 1),
    }
