"""Embedding provider abstraction with named profiles.

Supported providers
-------------------
openrouter      OpenAI-compatible; NOTE: OpenRouter serves no embedding models
                (verified against /api/v1/models: 0 of 460 are embeddings), so
                this profile only works if that changes. Kept so the requested
                `qwen/qwen3-embedding-4b` route is one config flip away.
deepinfra       Hosts Qwen/Qwen3-Embedding-4B (and `-batch` at half price).
local           sentence-transformers on this machine (needs VRAM/RAM).
openai_compat   Any OpenAI-compatible /embeddings endpoint.

Select a profile with `embed.provider` or the EMBED_PROVIDER env var.
Keys are read from the environment or the plugin data home's .env file.
"""

from __future__ import annotations

import os
import time
from pathlib import Path

from common import load_config

_CACHE: dict = {}
_ENV_LOADED = False


def load_dotenv_once() -> None:
    """Load the plugin data home's .env without overriding real env vars."""
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    _ENV_LOADED = True
    try:
        import paths

        env_path = paths.env_file()
    except Exception:  # noqa: BLE001 - imported outside the pipeline package
        env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return
    try:
        from dotenv import load_dotenv
    except ImportError:  # optional dependency
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
        return
    load_dotenv(env_path, override=False)


API_KEY_HINTS = {
    "openrouter": "OPENROUTER_API_KEY",
    "deepinfra": "DEEPINFRA_API_KEY",
    "openai_compat": "EMBED_API_KEY",
}


class Embedder:
    """Uniform embed_documents()/embed_query() across providers."""

    def __init__(self, cfg: dict | None = None):
        load_dotenv_once()
        full_cfg = load_config()["embed"]
        self.cfg = cfg or full_cfg

        # Provider: explicit arg > env override > config
        self.provider = (
            (self.cfg.get("provider") if cfg else None)
            or os.getenv("EMBED_PROVIDER")
            or full_cfg.get("provider", "local")
        )
        self.normalize = self.cfg.get("normalize", True)
        self.query_instruction = self.cfg.get("query_instruction", "")
        self.batch_size = int(self.cfg.get("batch_size", 32))
        self._local = None
        self.dimension: int | None = None

        profile = (self.cfg.get("profiles", {}) or {}).get(self.provider, {})
        self.model_name = (
            profile.get("model")
            or self.cfg.get("model")
            or self.cfg.get("local_model")
            or "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.api_base = profile.get("api_base") or self.cfg.get("api_base")
        self.api_key_env = profile.get("api_key_env") or API_KEY_HINTS.get(self.provider)

        if self.provider != "local":
            key = os.getenv(self.api_key_env or "")
            if not key:
                raise RuntimeError(
                    f"{self.api_key_env} is not set for provider '{self.provider}'.\n"
                    "  Options:\n"
                    "    - put it in the plugin data home's .env (see .env.example)\n"
                    "    - or EMBED_PROVIDER=local to use the local model"
                )
            from openai import OpenAI

            if not self.api_base:
                raise RuntimeError(f"embed.profiles.{self.provider}.api_base is not configured")
            self._client = OpenAI(base_url=self.api_base, api_key=key)

    # -- public -----------------------------------------------------------
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._embed(texts, is_query=False)

    def embed_query(self, text: str) -> list[float]:
        return self._embed([text], is_query=True)[0]

    @property
    def signature(self) -> str:
        """Identity of the vector space; index and query must match."""
        return f"{self.provider}:{self.model_name}"

    def describe(self) -> str:
        target = self.api_base if self.provider != "local" else "local"
        return f"{self.signature} via {target}"

    # -- internals --------------------------------------------------------
    def _embed(self, texts: list[str], is_query: bool) -> list[list[float]]:
        if not texts:
            return []
        if is_query and self.query_instruction:
            texts = [f"Instruct: {self.query_instruction}\nQuery: {t}" for t in texts]
        vectors = (
            self._embed_remote(texts) if self.provider != "local" else self._embed_local(texts)
        )
        self.dimension = self.dimension or len(vectors[0])
        return vectors

    def _embed_remote(self, texts: list[str]) -> list[list[float]]:
        out: list[list[float]] = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            out.extend(self._request_with_retry(batch))
            if len(texts) > self.batch_size:
                done = min(i + self.batch_size, len(texts))
                print(f"  embedded {done}/{len(texts)}", flush=True)
        return out

    def _request_with_retry(self, batch: list[str], attempts: int = 4) -> list[list[float]]:
        delay = 2.0
        last: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                resp = self._client.embeddings.create(model=self.model_name, input=batch)
                return [list(d.embedding) for d in sorted(resp.data, key=lambda d: d.index)]
            except Exception as exc:
                last = exc
                if attempt == attempts:
                    break
                print(
                    f"  embed batch failed ({exc.__class__.__name__}: {str(exc)[:120]}); "
                    f"retry {attempt}/{attempts - 1} in {delay:.0f}s",
                    flush=True,
                )
                time.sleep(delay)
                delay *= 2
        raise RuntimeError(f"embedding failed after {attempts} attempts: {last}")

    def _embed_local(self, texts: list[str]) -> list[list[float]]:
        from sentence_transformers import SentenceTransformer

        if self._local is None:
            print(f"  loading {self.model_name} locally (first run downloads weights)", flush=True)
            self._local = SentenceTransformer(self.model_name)
        vectors = self._local.encode(
            texts,
            batch_size=self.batch_size,
            normalize_embeddings=self.normalize,
            show_progress_bar=len(texts) > 64,
            convert_to_numpy=True,
        )
        return vectors.tolist()


def get_embedder() -> Embedder:
    if "embedder" not in _CACHE:
        _CACHE["embedder"] = Embedder()
    return _CACHE["embedder"]
