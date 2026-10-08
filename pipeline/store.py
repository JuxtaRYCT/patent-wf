"""SQLite store for every gathered item, its embedding, and pipeline annotations.

Schema
------
items(id PK, source, kind, pool, title, text, url, published, fetched, query, meta JSON)
    kind : paper | patent | news | repo | post | complaint | regulation | idea
    pool : finance | crossdomain | prior_art | signal | idea  (role in the pipeline)
vectors(id PK, model, dim, vec BLOB)
scores(id, run, stage, key, value)   -- novelty and LLM scores per run
"""
from __future__ import annotations

import datetime as dt
import json
import sqlite3
from typing import Iterable

import numpy as np

from .common import DB_PATH, today

SCHEMA = """
CREATE TABLE IF NOT EXISTS items(
  id TEXT PRIMARY KEY, source TEXT, kind TEXT, pool TEXT, title TEXT, text TEXT,
  url TEXT, published TEXT, fetched TEXT, query TEXT, meta TEXT);
CREATE INDEX IF NOT EXISTS items_kind ON items(kind);
CREATE INDEX IF NOT EXISTS items_pool ON items(pool);
CREATE TABLE IF NOT EXISTS vectors(id TEXT PRIMARY KEY, model TEXT, dim INT, vec BLOB);
CREATE TABLE IF NOT EXISTS scores(id TEXT, run TEXT, stage TEXT, key TEXT, value REAL,
  PRIMARY KEY(id, run, stage, key));
"""


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    cols = {r[1] for r in con.execute("PRAGMA table_info(items)")}
    if "seen_day" not in cols:   # migration: day the item entered the knowledge base
        con.execute("ALTER TABLE items ADD COLUMN seen_day TEXT")
        con.execute("UPDATE items SET seen_day = substr(fetched, 1, 10)")
        con.execute("CREATE INDEX IF NOT EXISTS items_seen ON items(seen_day)")
        con.commit()
    return con


def upsert(items: Iterable[dict]) -> int:
    """Insert items; keeps the first-seen `fetched` date so novelty 'newness' is stable."""
    con = connect()
    now = dt.datetime.utcnow().isoformat(timespec="seconds")
    n = 0
    for it in items:
        if not it.get("id") or not (it.get("title") or it.get("text")):
            continue
        con.execute(
            """INSERT INTO items(id,source,kind,pool,title,text,url,published,fetched,query,meta,seen_day)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET text=excluded.text, meta=excluded.meta,
                 title=excluded.title, url=excluded.url""",
            (it["id"], it.get("source"), it.get("kind"), it.get("pool"), (it.get("title") or "").strip(),
             (it.get("text") or "").strip(), it.get("url"), it.get("published"), now,
             it.get("query"), json.dumps(it.get("meta") or {}, default=str),
             it.get("seen_day") or today()))
        n += 1
    con.commit()
    con.close()
    return n


def fetch(where: str = "1=1", params: tuple = (), as_of: bool = True) -> list[dict]:
    """Items matching `where`. With as_of (default) only items already seen by the run date are visible,
    so a backfilled day never learns from data that arrived on later days."""
    con = connect()
    if as_of:
        where, params = f"({where}) AND (seen_day IS NULL OR seen_day <= ?)", (*params, today())
    rows = [dict(r) for r in con.execute(f"SELECT * FROM items WHERE {where}", params)]
    con.close()
    for r in rows:
        r["meta"] = json.loads(r["meta"] or "{}")
    return rows


def save_vectors(ids: list[str], vecs: np.ndarray, model: str):
    con = connect()
    con.executemany("INSERT OR REPLACE INTO vectors(id,model,dim,vec) VALUES(?,?,?,?)",
                    [(i, model, vecs.shape[1], v.astype(np.float32).tobytes()) for i, v in zip(ids, vecs)])
    con.commit()
    con.close()


def load_vectors(ids: list[str], model: str) -> dict[str, np.ndarray]:
    con = connect()
    out = {}
    for chunk in range(0, len(ids), 900):
        part = ids[chunk:chunk + 900]
        q = f"SELECT id, vec FROM vectors WHERE model=? AND id IN ({','.join('?' * len(part))})"
        for r in con.execute(q, (model, *part)):
            out[r["id"]] = np.frombuffer(r["vec"], dtype=np.float32)
    con.close()
    return out


def save_scores(rows: Iterable[tuple]):
    """rows: (id, run, stage, key, value)"""
    con = connect()
    con.executemany("INSERT OR REPLACE INTO scores VALUES(?,?,?,?,?)", list(rows))
    con.commit()
    con.close()


def counts() -> list[tuple]:
    con = connect()
    r = list(con.execute("SELECT source, kind, pool, COUNT(*) FROM items GROUP BY 1,2,3 ORDER BY 4 DESC"))
    con.close()
    return [tuple(x) for x in r]
