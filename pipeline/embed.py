"""Vector embeddings for every item (cached in SQLite, computed once per item)."""
from __future__ import annotations

import functools

import numpy as np

from . import store
from .common import load_config, log

L = log("embed")


@functools.lru_cache(maxsize=1)
def model():
    import torch
    from sentence_transformers import SentenceTransformer
    name = load_config()["embedding"]["model"]
    dev = "mps" if torch.backends.mps.is_available() else "cpu"
    L.info("loading %s on %s", name, dev)
    return SentenceTransformer(name, device=dev)


def model_name() -> str:
    return load_config()["embedding"]["model"]


def doc_text(it: dict, limit: int = 1800) -> str:
    return f"{it.get('title') or ''}. {(it.get('text') or '')[:limit]}"


def encode(texts: list[str], query: bool = False) -> np.ndarray:
    """L2-normalised embeddings. bge models want an instruction prefix on short queries."""
    if query and "bge" in model_name():
        texts = ["Represent this sentence for searching relevant passages: " + t for t in texts]
    bs = load_config()["embedding"]["batch_size"]
    return model().encode(texts, batch_size=bs, normalize_embeddings=True, show_progress_bar=len(texts) > 500,
                          convert_to_numpy=True).astype(np.float32)


def ensure(items: list[dict]) -> np.ndarray:
    """Return matrix aligned with `items`, computing and caching any missing vectors."""
    name = model_name()
    have = store.load_vectors([i["id"] for i in items], name)
    missing = [i for i in items if i["id"] not in have]
    if missing:
        L.info("embedding %d new items (%d cached)", len(missing), len(have))
        vecs = encode([doc_text(i) for i in missing])
        store.save_vectors([i["id"] for i in missing], vecs, name)
        have.update({i["id"]: v for i, v in zip(missing, vecs)})
    return np.stack([have[i["id"]] for i in items]) if items else np.zeros((0, 768), np.float32)
