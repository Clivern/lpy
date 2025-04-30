# 076. Tooling
#
# dotenv, orjson, tenacity, cachetools, and more-itertools.
#
# Run: python 076_tooling/main.py

# --- dotenv ---
from pathlib import Path
import tempfile
from dotenv import dotenv_values
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / ".env"
    p.write_text("TOKEN=abc\n", encoding="utf-8")
    print(dotenv_values(p)["TOKEN"])

# --- orjson dumps ---
import orjson
from datetime import datetime, timezone
blob = orjson.dumps({"n": 1, "t": datetime(2025, 1, 1, tzinfo=timezone.utc)}, option=orjson.OPT_UTC_Z)
print(orjson.loads(blob)["n"], blob[:1])

# --- orjson numpy ---
import orjson
import numpy as np
blob = orjson.dumps(np.array([1, 2, 3]), option=orjson.OPT_SERIALIZE_NUMPY)
print(orjson.loads(blob))

# --- tenacity retry ---
from tenacity import retry, stop_after_attempt, retry_if_exception_type
box = {"n": 0}
@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(ValueError), reraise=True)
def flaky():
    box["n"] += 1
    if box["n"] < 3:
        raise ValueError("again")
    return "ok"
print(flaky(), box["n"])

# --- tenacity wait ---
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_result
@retry(stop=stop_after_attempt(3), wait=wait_fixed(0), retry=retry_if_result(lambda r: r is None))
def probe():
    probe.i = getattr(probe, "i", 0) + 1
    return "ok" if probe.i >= 2 else None
print(probe())

# --- cachetools ttl ---
from cachetools import TTLCache, cached
cache = TTLCache(maxsize=8, ttl=60)
@cached(cache)
def inc(n):
    inc.calls = getattr(inc, "calls", 0) + 1
    return n + 1
print(inc(1), inc(1), inc.calls)

# --- cachetools lru ---
from cachetools import LRUCache
c = LRUCache(maxsize=2)
c["a"] = 1
c["b"] = 2
c["c"] = 3
print("a" in c, list(c))

# --- more itertools ---
from more_itertools import chunked, first, unique_everseen
print(list(chunked([1, 2, 3, 4, 5], 2)))
print(first([], default=0))
print(list(unique_everseen("ABBA")))

# --- more chunked ---
from more_itertools import windowed, pairwise
print(list(windowed([1, 2, 3, 4], 3)))
print(list(pairwise([1, 2, 3])))
