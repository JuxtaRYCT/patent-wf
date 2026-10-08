"""Step 1 - Data gathering. Runs every collector family in parallel (different hosts) and
upserts into SQLite. Usage: python -m pipeline.gather [--only papers,patents,news,signals]"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures as cf
import time

from . import store
from .common import dump_json, load_config, log, run_dir
from .sources import news, papers, patents, signals

L = log("gather")


def _signals(cfg):
    items = signals.federal_register(cfg)
    trends = signals.cfpb_issue_trends(cfg)
    dump_json(trends, run_dir() / "cfpb_trends.json")
    return items


FAMILIES = {"papers": papers.collect, "patents": patents.collect, "news": news.collect, "signals": _signals}


def main(only: list[str] | None = None):
    cfg = load_config()
    fams = {k: v for k, v in FAMILIES.items() if not only or k in only}
    t0 = time.time()
    manifest = {}
    with cf.ThreadPoolExecutor(max_workers=len(fams)) as ex:
        futs = {ex.submit(fn, cfg): name for name, fn in fams.items()}
        for f in cf.as_completed(futs):
            name = futs[f]
            try:
                items = f.result()
            except Exception as e:
                L.exception("family %s crashed: %s", name, e)
                continue
            n = store.upsert(items)
            by_src = collections.Counter(i["source"].split(":")[0] for i in items)
            manifest[name] = {"items": n, "by_source": dict(by_src)}
            L.info("== %s done: %d items %s", name, n, dict(by_src))
    manifest["elapsed_s"] = round(time.time() - t0)
    manifest["db_counts"] = store.counts()
    dump_json(manifest, run_dir() / "gather_manifest.json")
    return manifest


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    main([x for x in a.only.split(",") if x] or None)
