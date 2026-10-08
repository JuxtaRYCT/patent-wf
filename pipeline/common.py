"""Shared helpers: paths, config, HTTP session with polite retry/backoff, logging."""
from __future__ import annotations

import datetime as dt
import json
import logging
import os
import subprocess
import time
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RUNS = ROOT / "runs"
IDEAS = ROOT / "ideas"
EXPORTS = ROOT / "exports"
DB_PATH = DATA / "patents_wf.sqlite"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36 patents-wf/1.0")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")


def log(name: str) -> logging.Logger:
    return logging.getLogger(name)


def load_config() -> dict:
    with open(ROOT / "config" / "config.yaml") as f:
        return yaml.safe_load(f)


def today() -> str:
    return dt.date.today().isoformat()


def days_ago(n: int) -> dt.date:
    return dt.date.today() - dt.timedelta(days=n)


def run_dir(date: str | None = None) -> Path:
    d = RUNS / (date or today())
    d.mkdir(parents=True, exist_ok=True)
    return d


def github_token() -> str | None:
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        return tok
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True,
                              timeout=10).stdout.strip() or None
    except Exception:
        return None


class Http:
    """requests.Session wrapper: per-host minimum interval + retry on 429/5xx with Retry-After."""

    def __init__(self, min_interval: float = 1.0, max_retries: int = 6):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.min_interval = min_interval
        self.max_retries = max_retries
        self._last: dict[str, float] = {}
        self.log = log("http")

    def _wait(self, host: str):
        last = self._last.get(host, 0.0)
        gap = time.time() - last
        if gap < self.min_interval:
            time.sleep(self.min_interval - gap)
        self._last[host] = time.time()

    def get(self, url: str, **kw) -> requests.Response | None:
        host = requests.utils.urlparse(url).netloc
        kw.setdefault("timeout", 40)
        delay = 2.0
        for attempt in range(self.max_retries):
            self._wait(host)
            try:
                r = self.s.get(url, **kw)
            except requests.RequestException as e:
                self.log.warning("GET %s failed (%s), retry %d", url[:120], e, attempt)
                time.sleep(delay)
                delay *= 2
                continue
            if r.status_code == 200:
                return r
            if r.status_code in (429, 500, 502, 503, 504):
                ra = r.headers.get("Retry-After")
                try:
                    body = r.json()
                    ra = ra or body.get("retryAfter")
                except Exception:
                    pass
                wait = float(ra) if ra and str(ra).replace(".", "").isdigit() else delay
                wait = min(wait, 90)
                self.log.info("%s -> %d, sleeping %.0fs", host, r.status_code, wait)
                time.sleep(wait)
                delay = min(delay * 2, 60)
                continue
            self.log.warning("GET %s -> %d", url[:160], r.status_code)
            return None
        self.log.warning("GET %s gave up after %d retries", url[:160], self.max_retries)
        return None


def dump_json(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, default=str)


def load_json(path: Path):
    with open(path) as f:
        return json.load(f)
