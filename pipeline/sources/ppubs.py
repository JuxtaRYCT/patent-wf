"""USPTO Patent Public Search (PPUBS) client - full-text US patents & pre-grant publications.

Discovered 2026-09-30: the PPUBS web app's JSON API works anonymously:
  POST /api/users/me/session            -> x-access-token header
  POST /api/searches/generic            -> {numFound, docs:[{documentId,title,...}]}  (BRS query syntax)
  GET  /api/patents/highlight/{docId}   -> abstractHtml, claimsHtml, descriptionHtml, cpc, applicant
NOTE: USPTO announced PPUBS will require a USPTO.gov login from 2026-11-07; after that set
USPTO_PPUBS_TOKEN (copy the x-access-token of a logged-in browser session) or use the ODP API key.

BRS query cheatsheet: fraud.ab.   jpmorgan.as.   G06Q20/4016.cpc.   @pd>=20250101   money ADJ mule
"""
from __future__ import annotations

import concurrent.futures as cf
import html
import os
import re
import threading
import time

import requests

from ..common import UA, log

L = log("ppubs")
BASE = "https://ppubs.uspto.gov/api"
DBS = [{"databaseName": "US-PGPUB", "countryCodes": []}, {"databaseName": "USPAT", "countryCodes": []}]


def _clean(s: str | None) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s or "")
    return re.sub(r"[ \t]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


class PPUBS:
    SESSION_TTL = 20 * 60        # server-side session timeout is 1800 s; refresh well before it

    def __init__(self, min_interval: float = 0.15):
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": UA, "Content-Type": "application/json"})
        self.token = os.environ.get("USPTO_PPUBS_TOKEN")
        self.min_interval = min_interval
        self._lock = threading.Lock()
        self._last = 0.0
        self._born = time.time()
        if not self.token:
            self._new_session()

    def _new_session(self):
        r = self.s.post(f"{BASE}/users/me/session", data="-1", timeout=30)
        r.raise_for_status()
        self.token = r.headers.get("x-access-token")
        self._born = time.time()

    def _pace(self):
        with self._lock:
            if not os.environ.get("USPTO_PPUBS_TOKEN") and time.time() - self._born > self.SESSION_TTL:
                self._new_session()
            gap = time.time() - self._last
            if gap < self.min_interval:
                time.sleep(self.min_interval - gap)
            self._last = time.time()

    def _req(self, method: str, url: str, **kw):
        for attempt in range(5):
            self._pace()
            try:
                r = self.s.request(method, url, headers={"x-access-token": self.token}, timeout=60, **kw)
            except requests.RequestException as e:
                L.warning("ppubs %s error %s", url[-60:], e)
                time.sleep(2 ** attempt)
                continue
            if r.status_code == 200:
                return r.json()
            if r.status_code in (401, 403, 440):
                with self._lock:
                    self._new_session()
                continue
            if r.status_code in (429, 500, 502, 503, 504):
                L.info("ppubs %s -> %d, retry %d", url[-50:], r.status_code, attempt)
                if attempt >= 1:         # an expired session surfaces as 5xx too: refresh it
                    with self._lock:
                        self._new_session()
                time.sleep(2 ** attempt)
                continue
            L.warning("ppubs %s -> %d %s", url[-80:], r.status_code, r.text[:200])
            return None
        return None

    def search(self, q: str, n: int = 100, sort: str = "date_publ desc") -> tuple[list[dict], int]:
        docs, total, cursor = [], 0, "*"
        while len(docs) < n:
            # deep paging uses Solr cursorMarker (the `start` offset is ignored past page 1)
            body = {"cursorMarker": cursor, "databaseFilters": DBS, "fields": ["documentId", "title", "datePublished"],
                    "op": "AND", "pageSize": min(100, n - len(docs)), "q": q, "searchType": 0, "sort": sort,
                    "start": 0}
            d = self._req("POST", f"{BASE}/searches/generic", json=body)
            if not d:
                break
            total = d.get("numFound", 0)
            page = d.get("docs", [])
            docs += page
            if not page or len(docs) >= total or d.get("cursorMarker") in (None, cursor):
                break
            cursor = d["cursorMarker"]
        return docs, total

    def detail(self, doc_id: str) -> dict | None:
        src = "US-PGPUB" if doc_id.endswith(("-A1", "-A2", "-A9")) else "USPAT"
        d = self._req("GET", f"{BASE}/patents/highlight/{doc_id}",
                      params={"queryId": 1, "source": src, "includeSections": "true", "uniqueId": ""})
        if not d:
            return None
        claims = _clean(d.get("claimsHtml"))
        m = re.search(r"^\s*1\s*\.(.*?)(?=\n\s*2\s*\.|\Z)", claims, re.S)
        return {
            "doc_id": doc_id, "title": _clean(d.get("inventionTitle")), "abstract": _clean(d.get("abstractHtml")),
            "claim1": _clean(m.group(1))[:4000] if m else claims[:4000], "claims": claims[:20000],
            "applicant": ", ".join(d.get("applicantName") or d.get("assigneeName") or []),
            "cpc": d.get("cpcInventiveFlattened"), "filed": d.get("applicationFilingDate"),
            "published": d.get("datePublished"), "description_head": _clean(d.get("descriptionHtml"))[:6000]}

    def details(self, doc_ids: list[str], workers: int = 6) -> list[dict]:
        out = []
        with cf.ThreadPoolExecutor(workers) as ex:
            for n, x in enumerate(ex.map(self.detail, doc_ids), 1):
                if x:
                    out.append(x)
                if n % 250 == 0:
                    L.info("ppubs details %d/%d", n, len(doc_ids))
        return out


def to_item(d: dict, pool: str, query: str) -> dict:
    pn = d["doc_id"]
    gp = pn.replace("-", "")
    return {"id": f"patent:{gp}", "source": "uspto_ppubs", "kind": "patent", "pool": pool,
            "title": d["title"], "text": d["abstract"] + ("\nCLAIM 1: " + d["claim1"] if d["claim1"] else ""),
            "url": f"https://patents.google.com/patent/{gp}/en", "published": (d.get("published") or "")[:10],
            "query": query, "meta": {"applicant": d["applicant"], "cpc": d["cpc"], "filed": d["filed"],
                                     "doc_id": pn}}
