"""Industry news, newsletters, Hacker News and GitHub collectors (Approach 1c).

Feedly / Inoreader APIs are paid wrappers around the same RSS feeds; the pipeline reads the
feeds directly (and Google News RSS searches), which needs no account. Set FEEDLY_TOKEN to
additionally pull a Feedly board (see integrations/README).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import re
import urllib.parse as up

import feedparser

from ..common import Http, days_ago, github_token, load_config, log

L = log("news")
_http = Http(min_interval=0.8)


def _clean(s: str | None) -> str:
    import html
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def _date(e) -> str:
    for k in ("published_parsed", "updated_parsed"):
        if e.get(k):
            return dt.date(*e[k][:3]).isoformat()
    return ""


def rss(name: str, url: str, since: dt.date, pool: str = "finance") -> list[dict]:
    r = _http.get(url, allow_redirects=True)
    if not r:
        return []
    feed = feedparser.parse(r.content)
    out = []
    for e in feed.entries:
        d = _date(e)
        if d and d < since.isoformat():
            continue
        link = e.get("link") or ""
        uid = hashlib.sha1((link or e.get("title", "")).encode()).hexdigest()[:16]
        out.append({"id": f"news:{uid}", "source": f"rss:{name}", "kind": "news", "pool": pool,
                    "title": _clean(e.get("title")), "text": _clean(e.get("summary"))[:2000],
                    "url": link, "published": d, "query": name, "meta": {}})
    L.info("rss %-28s -> %d", name, len(out))
    return out


def google_news(q: str, since: dt.date) -> list[dict]:
    url = "https://news.google.com/rss/search?" + up.urlencode({"q": f"{q} when:30d", "hl": "en-US", "gl": "US",
                                                                "ceid": "US:en"})
    return rss(f"gnews:{q}", url, since)


def hackernews(cfg: dict) -> list[dict]:
    h = cfg["hackernews"]
    since = int((dt.datetime.now() - dt.timedelta(days=cfg["run"]["lookback_days"])).timestamp())
    out = []
    for q in h["queries"]:
        r = _http.get("https://hn.algolia.com/api/v1/search?" + up.urlencode({
            "query": q, "tags": "(story,ask_hn)", "hitsPerPage": h["per_query"],
            "numericFilters": f"created_at_i>{since},points>20"}))
        if not r:
            continue
        for x in r.json().get("hits", []):
            out.append({"id": f"hn:{x['objectID']}", "source": "hackernews", "kind": "post", "pool": "finance",
                        "title": _clean(x.get("title")), "text": _clean(x.get("story_text") or x.get("title"))[:2000],
                        "url": x.get("url") or f"https://news.ycombinator.com/item?id={x['objectID']}",
                        "published": (x.get("created_at") or "")[:10], "query": q,
                        "meta": {"points": x.get("points"), "comments": x.get("num_comments")}})
    L.info("hackernews -> %d", len(out))
    return out


def github(cfg: dict) -> list[dict]:
    g = cfg["github"]
    tok = github_token()
    headers = {"Accept": "application/vnd.github+json"}
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    since = days_ago(g["created_after_days"]).isoformat()
    out = []
    for t in g["topics"]:
        r = _http.get("https://api.github.com/search/repositories?" + up.urlencode({
            "q": f"topic:{t} created:>{since}", "sort": "stars", "order": "desc", "per_page": g["per_topic"]}),
            headers=headers)
        if not r:
            continue
        for x in r.json().get("items", []):
            out.append({"id": f"gh:{x['full_name']}", "source": "github", "kind": "repo", "pool": "finance",
                        "title": x["full_name"], "text": _clean(x.get("description") or "") + " | topics: " +
                        ", ".join(x.get("topics") or []), "url": x["html_url"], "published": x["created_at"][:10],
                        "query": t, "meta": {"stars": x.get("stargazers_count"), "lang": x.get("language")}})
    # daily trending page (all languages) for general tech momentum
    r = _http.get("https://github.com/trending?since=weekly")
    if r:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "lxml")
        for art in soup.select("article.Box-row"):
            a = art.select_one("h2 a")
            if not a:
                continue
            name = a["href"].strip("/")
            desc = art.select_one("p")
            out.append({"id": f"gh:{name}", "source": "github_trending", "kind": "repo", "pool": "crossdomain",
                        "title": name, "text": _clean(desc.get_text() if desc else ""),
                        "url": f"https://github.com/{name}", "published": dt.date.today().isoformat(),
                        "query": "trending", "meta": {}})
    L.info("github -> %d", len(out))
    return out


def collect(cfg: dict | None = None) -> list[dict]:
    cfg = cfg or load_config()
    since = days_ago(cfg["run"]["lookback_days"])
    items = []
    for name, url in cfg["rss"]["feeds"].items():
        try:
            items += rss(name, url, since)
        except Exception as e:
            L.warning("rss %s failed: %s", name, e)
    for q in cfg["rss"]["google_news_queries"]:
        items += google_news(q, since)
    for fn in (hackernews, github):
        try:
            items += fn(cfg)
        except Exception as e:
            L.exception("%s failed: %s", fn.__name__, e)
    return items
