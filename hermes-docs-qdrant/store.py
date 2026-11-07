"""Qdrant store for the Hermes docs corpus: schema, ingest, hybrid retrieval.

Kept dependency-light and side-effect-free at import time so a missing Qdrant
or a missing API key disables the tools instead of breaking Hermes startup.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

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
        url = config.get("url") or os.getenv("QDRANT_URL")
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

            self._client = OpenAI(
                base_url=self.base, api_key=os.environ["OPENROUTER_API_KEY"]
            )
        return self._client

    def embed_query(self, text: str) -> list[float]:
        prompt = f"Instruct: {QUERY_INSTRUCTION}\nQuery: {text}"
        resp = self._get_client().embeddings.create(model=self.model, input=[prompt])
        return list(resp.data[0].embedding)


class SparseEmbedder:
    """FastEmbed BM25 sparse vectors; lazily loaded, one model instance."""

    def __init__(self):
        self._model = None
        self._broken = False

    def available(self) -> bool:
        if self._broken:
            return False
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
            out.append((list(emb.indices), list(emb.values)))
        return out

    def embed_one(self, text: str):
        return self.embed([text])[0]


# ----------------------------------------------------------------------- store


class DocsStore:
    """Hybrid retrieval over the Qdrant collection."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self._client = None
        self._dense = QueryEmbedder()
        self._sparse = SparseEmbedder()

    # -- client ---------------------------------------------------------
    def client(self):
        if self._client is None:
            from qdrant_client import QdrantClient
            from qdrant_client.http import models as qm

            self._client = QdrantClient(
                url=self.settings.url,
                api_key=self.settings.api_key,
                path=self.settings.path,
                timeout=10,
            )
            self._qm = qm
        return self._client

    def health(self) -> tuple[bool, str]:
        try:
            client = self.client()
            info = client.get_collection(self.settings.collection)
            return True, f"{info.points_count or 0} points"
        except Exception as exc:  # noqa: BLE001 - surface to the model, never raise
            return False, f"{exc.__class__.__name__}: {str(exc)[:200]}"

    def ensure_collection(self, recreate: bool = False) -> None:
        from qdrant_client.http import models as qm

        client = self.client()
        name = self.settings.collection
        if recreate:
            client.delete_collection(name)
        elif client.collection_exists(name):
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
    ) -> list[dict]:
        from qdrant_client.http import models as qm

        limit = limit or self.settings.top_k
        client = self.client()
        name = self.settings.collection

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

        dense_vec = self._dense.embed_query(query)

        # NOTE: on RRF fusion the top-level query_filter is not applied to the
        # prefetch legs; each leg must carry the filter itself or filtering is
        # silently bypassed (verified against qdrant-client local mode).
        prefetch = [
            qm.Prefetch(
                query=dense_vec,
                using=DENSE_VEC,
                filter=query_filter,
                limit=max(limit * 4, 20),
            )
        ]
        if self._sparse.available():
            try:
                idx, vals = self._sparse.embed_one(query)
                prefetch.append(
                    qm.Prefetch(
                        query=qm.SparseVector(indices=idx, values=vals),
                        using=SPARSE_VEC,
                        filter=query_filter,
                        limit=max(limit * 4, 20),
                    )
                )
            except Exception:  # sparse is an enhancement, never a blocker
                pass

        if len(prefetch) > 1:
            try:
                points = client.query_points(
                    collection_name=name,
                    prefetch=prefetch,
                    query=qm.FusionQuery(fusion=qm.Fusion.RRF),
                    limit=limit,
                    query_filter=query_filter,
                    with_payload=True,
                ).points
            except Exception:
                points = self._dense_only(query_filter, limit, dense_vec)
        else:
            points = self._dense_only(query_filter, limit, dense_vec)

        return [_to_result(p) for p in points if (p.score or 0) >= self.settings.score_floor]

    def _dense_only(self, query_filter, limit: int, vector: list[float]):
        return self.client().query_points(
            collection_name=self.settings.collection,
            query=vector,
            using=DENSE_VEC,
            query_filter=query_filter,
            limit=limit,
            with_payload=True,
        ).points

    # -- reads ----------------------------------------------------------
    def get_doc_chunks(self, doc_id: str, limit: int = 40) -> list[dict]:
        from qdrant_client.http import models as qm

        points, _ = self.client().scroll(
            collection_name=self.settings.collection,
            scroll_filter=qm.Filter(
                must=[qm.FieldCondition(key="doc_id", match=qm.MatchValue(value=doc_id))]
            ),
            limit=limit,
            with_payload=True,
        )
        rows = [_to_result(p) for p in points]
        rows.sort(key=lambda r: r.get("chunk_id", ""))
        return rows

    def list_sections(self) -> list[dict]:
        """Distinct (section, doc_type) counts for discovery."""
        client = self.client()
        counts: dict[tuple[str, str], int] = {}
        offset = None
        while True:
            points, offset = client.scroll(
                collection_name=self.settings.collection,
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


def _to_result(point) -> dict:
    payload = getattr(point, "payload", None) or {}
    score = getattr(point, "score", None)
    return {
        "chunk_id": payload.get("chunk_id", str(getattr(point, "id", ""))),
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
    progress=None,
) -> dict:
    """Embed and upsert chunks.jsonl into Qdrant. Returns a stats dict."""
    from openai import OpenAI
    from qdrant_client.http import models as qm

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

    store = DocsStore(settings)
    store.ensure_collection(recreate=recreate)
    client = store.client()
    name = settings.collection

    embedder = OpenAI(base_url=EMBED_BASE, api_key=key)
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
        dense = [list(d.embedding) for d in sorted(resp.data, key=lambda d: d.index)]
        sparse_vecs = sparse.embed(texts) if use_sparse else [None] * len(batch)

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

        client.upsert(collection_name=name, points=points, wait=True)
        upserted += len(points)
        if progress:
            progress(upserted, len(rows))

    return {
        "upserted": upserted,
        "collection": name,
        "sparse": use_sparse,
        "seconds": round(time.time() - started, 1),
    }
