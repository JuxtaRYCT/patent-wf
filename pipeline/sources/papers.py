"""Academic paper collectors: arXiv, Semantic Scholar, PubMed, Crossref, OpenAlex (Approach 1a)."""
from __future__ import annotations

import re
import urllib.parse as up
import xml.etree.ElementTree as ET

import feedparser

from ..common import Http, days_ago, load_config, log

L = log("papers")
_http = Http(min_interval=3.1)        # arXiv asks for >=3s between calls
_s2 = Http(min_interval=1.2)
_ncbi = Http(min_interval=0.4)
_misc = Http(min_interval=1.0)


def _clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()


# ------------------------------------------------------------------ arXiv
def arxiv_query(q: str, max_results: int, pool: str, since=None) -> list[dict]:
    out, start, page = [], 0, 100
    while start < max_results:
        url = ("https://export.arxiv.org/api/query?" + up.urlencode({
            "search_query": q, "start": start, "max_results": min(page, max_results - start),
            "sortBy": "submittedDate", "sortOrder": "descending"}))
        r = _http.get(url)
        if not r:
            break
        feed = feedparser.parse(r.text)
        if not feed.entries:
            break
        stop = False
        for e in feed.entries:
            pub = e.get("published", "")[:10]
            if since and pub and pub < since.isoformat():
                stop = True
                break
            aid = e.id.rsplit("/abs/", 1)[-1]
            aid_nov = re.sub(r"v\d+$", "", aid)
            out.append({
                "id": f"arxiv:{aid_nov}", "source": "arxiv", "kind": "paper", "pool": pool,
                "title": _clean(e.title), "text": _clean(e.summary), "url": f"https://arxiv.org/abs/{aid_nov}",
                "published": pub, "query": q,
                "meta": {"categories": [t["term"] for t in e.get("tags", [])],
                         "authors": [a.name for a in e.get("authors", [])][:8]}})
        if stop:
            break
        start += page
    L.info("arxiv %-60s -> %d", q[:60], len(out))
    return out


def arxiv_all(cfg: dict) -> list[dict]:
    a = cfg["arxiv"]
    since = days_ago(cfg["run"]["lookback_days"])
    items = []
    for q in a["finance_queries"]:
        items += arxiv_query(q, a["max_per_query"], "finance", since)
    for cat in a["crossdomain_categories"]:
        items += arxiv_query(f"cat:{cat}", a["crossdomain_per_category"], "crossdomain")
    return items


# ------------------------------------------------------------------ Semantic Scholar
def semantic_scholar(cfg: dict) -> list[dict]:
    s = cfg["semantic_scholar"]
    year = f"{days_ago(730).year}-"
    items = []
    for q in s["queries"]:
        url = ("https://api.semanticscholar.org/graph/v1/paper/search/bulk?" + up.urlencode({
            "query": q, "year": year, "sort": "publicationDate:desc",
            "fields": "title,abstract,year,publicationDate,venue,externalIds,citationCount,url"}))
        r = _s2.get(url)
        if not r:
            continue
        n = 0
        for p in r.json().get("data", []):
            if not p.get("abstract") or n >= s["per_query"]:
                continue
            n += 1
            ext = p.get("externalIds") or {}
            pid = f"arxiv:{ext['ArXiv']}" if ext.get("ArXiv") else f"s2:{p['paperId']}"
            items.append({
                "id": pid, "source": "semantic_scholar", "kind": "paper", "pool": "finance",
                "title": p["title"], "text": _clean(p["abstract"]), "url": p.get("url"),
                "published": p.get("publicationDate") or str(p.get("year") or ""), "query": q,
                "meta": {"venue": p.get("venue"), "citations": p.get("citationCount"), "doi": ext.get("DOI")}})
        L.info("s2 %-40s -> %d", q, n)
    return items


# ------------------------------------------------------------------ PubMed (bio mechanisms)
def pubmed(cfg: dict) -> list[dict]:
    p = cfg["pubmed"]
    email = cfg["run"].get("contact_email") or ""
    items = []
    for q in p["queries"]:
        r = _ncbi.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + up.urlencode({
            "db": "pubmed", "term": q, "retmax": p["per_query"], "sort": "pub_date",
            "retmode": "json", "email": email, "tool": "patents-wf"}))
        if not r:
            continue
        ids = r.json()["esearchresult"].get("idlist", [])
        if not ids:
            continue
        r = _ncbi.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + up.urlencode({
            "db": "pubmed", "id": ",".join(ids), "retmode": "xml", "email": email, "tool": "patents-wf"}))
        if not r:
            continue
        root = ET.fromstring(r.content)
        n = 0
        for art in root.iter("PubmedArticle"):
            pmid = art.findtext(".//PMID")
            title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
            abstract = " ".join("".join(t.itertext()) for t in art.iter("AbstractText"))
            if not abstract:
                continue
            y = art.findtext(".//PubDate/Year") or art.findtext(".//ArticleDate/Year") or ""
            m = art.findtext(".//ArticleDate/Month") or "01"
            items.append({
                "id": f"pubmed:{pmid}", "source": "pubmed", "kind": "paper", "pool": "crossdomain",
                "title": _clean(title), "text": _clean(abstract), "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "published": f"{y}-{m}" if y else "", "query": q, "meta": {}})
            n += 1
        L.info("pubmed %-45s -> %d", q, n)
    return items


# ------------------------------------------------------------------ Crossref (journals)
def crossref(cfg: dict) -> list[dict]:
    c = cfg["crossref"]
    items = []
    since = days_ago(365).isoformat()
    for q in c["queries"]:
        r = _misc.get("https://api.crossref.org/works?" + up.urlencode({
            "query": q, "rows": c["rows"], "filter": f"from-pub-date:{since},has-abstract:true",
            "select": "DOI,title,abstract,issued,container-title", "mailto": cfg["run"].get("contact_email") or ""}))
        if not r:
            continue
        n = 0
        for w in r.json()["message"]["items"]:
            if not w.get("title"):
                continue
            parts = (w.get("issued") or {}).get("date-parts", [[None]])[0]
            items.append({
                "id": f"doi:{w['DOI'].lower()}", "source": "crossref", "kind": "paper", "pool": "finance",
                "title": _clean(w["title"][0]), "text": _clean(w.get("abstract")),
                "url": f"https://doi.org/{w['DOI']}", "published": "-".join(str(x) for x in parts if x),
                "query": q, "meta": {"journal": (w.get("container-title") or [""])[0]}})
            n += 1
        L.info("crossref %-40s -> %d", q, n)
    return items


def openalex_search(q: str, n: int = 25, api_key: str | None = None) -> list[dict]:
    """Used by prior-art checks. OpenAlex throttles anonymous search since 2025; key optional."""
    params = {"search": q, "per-page": n, "select": "id,title,abstract_inverted_index,publication_date,doi"}
    if api_key:
        params["api_key"] = api_key
    r = _misc.get("https://api.openalex.org/works?" + up.urlencode(params))
    if not r:
        return []
    out = []
    for w in r.json().get("results", []):
        inv = w.get("abstract_inverted_index") or {}
        pos = sorted((p, t) for t, ps in inv.items() for p in ps)
        out.append({"id": w["id"], "title": w.get("title"), "text": " ".join(t for _, t in pos),
                    "published": w.get("publication_date"), "url": w.get("doi") or w["id"]})
    return out


_s2_fast = Http(min_interval=1.5, max_retries=1)
_S2_FAILS = [0]


def s2_search(q: str, n: int = 20) -> list[dict]:
    """Relevance-ranked paper search used by prior-art checks. Anonymous S2 is heavily throttled, so this
    uses a single attempt and a circuit breaker (3 consecutive failures -> skipped for the rest of the run)."""
    if _S2_FAILS[0] >= 3:
        return []
    r = _s2_fast.get("https://api.semanticscholar.org/graph/v1/paper/search?" + up.urlencode({
        "query": q, "limit": n, "fields": "title,abstract,year,url,externalIds"}))
    if not r:
        _S2_FAILS[0] += 1
        return []
    _S2_FAILS[0] = 0
    return [{"id": f"s2:{p['paperId']}", "title": p.get("title"), "text": _clean(p.get("abstract")),
             "published": str(p.get("year") or ""), "url": p.get("url")} for p in r.json().get("data", [])]


def arxiv_search(terms: list[str], n: int = 15) -> list[dict]:
    """Relevance-ranked arXiv search on distinctive terms (prior-art checks)."""
    q = " AND ".join(f'all:"{t}"' if " " in t else f"all:{t}" for t in terms[:3])
    r = _http.get("https://export.arxiv.org/api/query?" + up.urlencode({
        "search_query": q, "start": 0, "max_results": n, "sortBy": "relevance"}))
    if not r:
        return []
    out = []
    for e in feedparser.parse(r.text).entries:
        aid = re.sub(r"v\d+$", "", e.id.rsplit("/abs/", 1)[-1])
        out.append({"id": f"arxiv:{aid}", "title": _clean(e.title), "text": _clean(e.summary),
                    "published": e.get("published", "")[:10], "url": f"https://arxiv.org/abs/{aid}"})
    return out


def collect(cfg: dict | None = None) -> list[dict]:
    cfg = cfg or load_config()
    items = []
    for fn in (arxiv_all, semantic_scholar, pubmed, crossref):
        try:
            items += fn(cfg)
        except Exception as e:  # one source failing must not kill the daily run
            L.exception("%s failed: %s", fn.__name__, e)
    return items
