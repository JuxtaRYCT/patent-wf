"""Patent collectors (Approach 1b).

Google Patents has no official API or RSS feed any more; the public `xhr/query` endpoint that
powers patents.google.com returns JSON and is used here with conservative pacing.
USPTO's Open Data Portal (api.uspto.gov) needs a free API key -> used when USPTO_API_KEY is set.
"""
from __future__ import annotations

import os
import re
import urllib.parse as up

from ..common import Http, load_config, log
from .ppubs import PPUBS, to_item

L = log("patents")
_gp = Http(min_interval=6.0, max_retries=2)
_uspto = Http(min_interval=1.0)
_GP_BLOCKED = False   # circuit breaker: Google serves a "Sorry..." 503 page once it flags the IP


def _clean(s: str | None) -> str:
    import html
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def google_patents(q: str = "", num: int = 100, after: str | None = None, assignee: str | None = None,
                   sort_new: bool = False, country: str | None = None, pool: str = "prior_art",
                   page: int = 0) -> tuple[list[dict], int]:
    """Returns (items, total_results). q uses Google Patents syntax."""
    parts = []
    if q:
        parts.append("q=" + up.quote(q))
    if assignee:
        parts.append("assignee=" + up.quote(assignee))
    if after:
        parts.append(f"after=priority:{after}")
    if country:
        parts.append(f"country={country}")
    if sort_new:
        parts.append("sort=new")
    parts.append(f"num={num}")
    if page:
        parts.append(f"page={page}")
    inner = "&".join(parts)
    global _GP_BLOCKED
    if _GP_BLOCKED:
        return [], 0
    r = _gp.get("https://patents.google.com/xhr/query?" + up.urlencode({"url": inner, "exp": ""}))
    if not r:
        _GP_BLOCKED = True
        L.warning("Google Patents throttled -> circuit open for this run")
        return [], 0
    try:
        res = r.json()["results"]
    except Exception:
        return [], 0
    items = []
    for cl in res.get("cluster", []):
        for x in cl.get("result", []):
            p = x["patent"]
            pn = p.get("publication_number")
            if not pn:
                continue
            items.append({
                "id": f"patent:{pn}", "source": "google_patents", "kind": "patent", "pool": pool,
                "title": _clean(p.get("title")), "text": _clean(p.get("snippet")),
                "url": f"https://patents.google.com/patent/{pn}/en", "published": p.get("publication_date"),
                "query": q or f"assignee:{assignee}",
                "meta": {"assignee": _clean(p.get("assignee")), "priority": p.get("priority_date"),
                         "filing": p.get("filing_date"), "inventor": _clean(p.get("inventor")),
                         "lang": p.get("language")}})
    return items, int(res.get("total_num_results") or 0)


def patent_detail(pn: str) -> dict:
    """Fetch abstract + first independent claim from the patent HTML page (for dossiers)."""
    from bs4 import BeautifulSoup
    r = _gp.get(f"https://patents.google.com/patent/{pn}/en")
    if not r:
        return {}
    soup = BeautifulSoup(r.text, "lxml")
    abstract = soup.select_one("section[itemprop=abstract]") or soup.select_one("abstract")
    claims = soup.select("div.claim[id^=CLM]") or soup.select("claim")
    first_claim = claims[0].get_text(" ", strip=True) if claims else ""
    title = soup.select_one("meta[name=DC.title]")
    return {"pn": pn, "title": title["content"].strip() if title else "",
            "abstract": _clean(abstract.get_text(" ", strip=True)) if abstract else "",
            "claim1": _clean(first_claim)[:3000], "n_claims": len(claims)}


def uspto_odp(q: str, rows: int = 50) -> list[dict]:
    key = os.environ.get("USPTO_API_KEY")
    if not key:
        return []
    r = _uspto.get("https://api.uspto.gov/api/v1/patent/applications/search?" + up.urlencode({"q": q, "limit": rows}),
                   headers={"X-API-KEY": key})
    if not r:
        return []
    out = []
    for a in r.json().get("patentFileWrapperDataBag", []):
        md = a.get("applicationMetaData", {})
        out.append({"id": f"uspto:{a.get('applicationNumberText')}", "source": "uspto_odp", "kind": "patent",
                    "pool": "prior_art", "title": md.get("inventionTitle"), "text": md.get("inventionTitle"),
                    "url": None, "published": md.get("filingDate"), "query": q, "meta": md})
    return out


def collect_ppubs(cfg: dict) -> list[dict]:
    """Prior-art knowledge base + competitor tracking from USPTO full text (abstract + claim 1)."""
    p = cfg["ppubs"]
    api = PPUBS()
    since = f"@pd>={p['since']}"
    plan: list[tuple[str, str, str, int]] = []   # (query, pool, label, n)
    plan += [(f"{cpc}.cpc. AND {since}", "prior_art", f"cpc:{cpc}", p["per_cpc"]) for cpc in p["cpc_queries"]]
    plan += [(f"{q} AND {since}", "prior_art", f"kw:{q}", p["per_keyword"]) for q in p["keyword_queries"]]
    plan += [(f"({a}).as. AND {since}", "competitor", f"assignee:{a}", p["per_assignee"]) for a in p["assignees"]]
    seen: dict[str, tuple[str, str]] = {}
    for q, pool, label, n in plan:
        docs, total = api.search(q, n)
        L.info("ppubs %-70s -> %d / %d", label[:70], len(docs), total)
        for d in docs:
            seen.setdefault(d["documentId"], (pool, label))
    from .. import store
    have = {r["meta"].get("doc_id") for r in store.fetch("source='uspto_ppubs'")}
    todo = [d for d in seen if d not in have]
    L.info("ppubs: %d documents found, %d already stored, fetching %d (abstract + claims)",
           len(seen), len(seen) - len(todo), len(todo))
    items = []
    for b in range(0, len(todo), 300):         # save incrementally: a crash never loses more than a chunk
        chunk = [to_item(d, *seen[d["doc_id"]]) for d in api.details(todo[b:b + 300])]
        store.upsert(chunk)
        items += chunk
        L.info("ppubs: stored %d/%d", b + len(chunk), len(todo))
    return items


def collect(cfg: dict | None = None) -> list[dict]:
    cfg = cfg or load_config()
    items = collect_ppubs(cfg)
    g = cfg["google_patents"]      # global coverage (EP/WO/CN/IN/...) when Google is not throttling
    for q in g["topic_queries"]:
        got, total = google_patents(q, num=g["num"], after=g["after_priority"])
        if _GP_BLOCKED:
            break
        L.info("gp topic %-50s -> %d (total %d)", q, len(got), total)
        items += got
    for q in g["topic_queries"][:5]:
        items += uspto_odp(q)
    return items
