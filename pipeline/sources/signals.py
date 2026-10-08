"""Opportunity-signal collectors for Approach 2 (AI Opportunity Scanner).

Pain   : CFPB Consumer Complaint Database (public API, ~millions of complaints, with narratives)
Pull   : Federal Register (new/proposed financial regulation = forced demand for new tech)
"""
from __future__ import annotations

import urllib.parse as up

from ..common import Http, days_ago, load_config, log

L = log("signals")
_http = Http(min_interval=1.0)
_http.s.headers["User-Agent"] = "curl/8.7.1"  # CFPB edge blocks browser-like UAs from scripts
CFPB = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"


def cfpb_aggs(date_min: str, date_max: str) -> dict:
    r = _http.get(CFPB + "?" + up.urlencode({"size": 0, "date_received_min": date_min,
                                             "date_received_max": date_max}), timeout=90)
    if not r:
        return {}
    return r.json().get("aggregations", {})


def _bucket_counts(aggs: dict, field: str) -> dict[str, int]:
    """Flatten {field: {field: {buckets: [{key, doc_count, sub_<field>.raw: {buckets}}]}}}.
    Sub-buckets become 'parent > child' keys so sub-issue trends are visible too."""
    node = aggs.get(field, {})
    inner = node.get(field, node)
    out = {}
    for b in inner.get("buckets", []):
        out[b["key"]] = b["doc_count"]
        for k, v in b.items():
            if k.startswith("sub_") and isinstance(v, dict):
                for sb in v.get("buckets", []):
                    out[f"{b['key']} > {sb['key']}"] = sb["doc_count"]
    return out


def cfpb_issue_trends(cfg: dict) -> list[dict]:
    """Compare issue share in recent window vs. baseline year -> growth signal."""
    s = cfg["scanner"]
    recent = cfpb_aggs(days_ago(s["cfpb_window_days"]).isoformat(), days_ago(0).isoformat())
    base = cfpb_aggs(days_ago(s["cfpb_baseline_days"] + s["cfpb_window_days"]).isoformat(),
                     days_ago(s["cfpb_window_days"]).isoformat())
    out = []
    for field in ("product", "issue"):
        rc, bc = _bucket_counts(recent, field), _bucket_counts(base, field)
        rt, bt = max(sum(rc.values()), 1), max(sum(bc.values()), 1)
        for k, v in rc.items():
            share_r, share_b = v / rt, bc.get(k, 0) / bt
            out.append({"field": field, "key": k, "recent": v, "baseline": bc.get(k, 0),
                        "share_recent": share_r, "share_baseline": share_b,
                        "lift": (share_r + 1e-4) / (share_b + 1e-4)})
    L.info("cfpb trends -> %d buckets", len(out))
    return out


# NOTE (verified 2026-09-30): the public API no longer returns consumer narratives
# (`complaint_what_happened` is empty and rejected as a search field), so the scanner
# relies on product / issue / sub-issue trend lifts. Kept for when narratives return.
def cfpb_narratives(issue: str | None = None, product: str | None = None, n: int = 60,
                    days: int = 180) -> list[dict]:
    params = {"size": n, "has_narrative": "true", "sort": "created_date_desc",
              "date_received_min": days_ago(days).isoformat(), "no_aggs": "true"}
    if issue:
        params["issue"] = issue
    if product:
        params["product"] = product
    r = _http.get(CFPB + "?" + up.urlencode(params), timeout=90)
    if not r:
        return []
    out = []
    for h in r.json().get("hits", {}).get("hits", []):
        s = h["_source"]
        text = (s.get("complaint_what_happened") or "").replace("XXXX", "").strip()
        if len(text) < 80:
            continue
        out.append({"id": f"cfpb:{s['complaint_id']}", "source": "cfpb", "kind": "complaint", "pool": "signal",
                    "title": f"{s.get('product')} / {s.get('issue')} / {s.get('sub_issue') or ''}".strip(" /"),
                    "text": text[:3000], "url": f"https://www.consumerfinance.gov/data-research/consumer-complaints/search/detail/{s['complaint_id']}",
                    "published": (s.get("date_received") or "")[:10], "query": issue or product,
                    "meta": {"product": s.get("product"), "sub_product": s.get("sub_product"),
                             "issue": s.get("issue"), "sub_issue": s.get("sub_issue"),
                             "company": s.get("company"), "response": s.get("company_response")}})
    return out


def federal_register(cfg: dict) -> list[dict]:
    s = cfg["scanner"]
    out = []
    since = days_ago(s["federal_register_days"]).isoformat()
    for ag in s["federal_register_agencies"]:
        for page in (1, 2):
            params = [("per_page", 100), ("page", page), ("order", "newest"),
                      ("conditions[agencies][]", ag), ("conditions[publication_date][gte]", since)]
            for t in ("RULE", "PRORULE", "NOTICE"):
                params.append(("conditions[type][]", t))
            r = _http.get("https://www.federalregister.gov/api/v1/documents.json?" + up.urlencode(params))
            if not r:
                break
            res = r.json().get("results", [])
            for d in res:
                if not d.get("abstract"):
                    continue
                out.append({"id": f"fr:{d['document_number']}", "source": "federal_register", "kind": "regulation",
                            "pool": "signal", "title": d["title"], "text": d["abstract"], "url": d["html_url"],
                            "published": d["publication_date"], "query": ag,
                            "meta": {"type": d.get("type"), "agencies": [a.get("name") for a in d.get("agencies", [])]}})
            if len(res) < 100:
                break
    L.info("federal register -> %d", len(out))
    return out
