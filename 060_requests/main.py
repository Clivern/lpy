# 060. requests
#
# GET, POST, JSON, headers, and Session.
#
# Run: python 060_requests/main.py

# --- requests get ---
import requests
try:
    r = requests.get("https://example.com", timeout=5)
    print(r.status_code, "text/html" in r.headers.get("content-type", ""))
except requests.RequestException as e:
    print(type(e).__name__)

# Always pass timeout= on real requests.

# --- requests post ---
import requests
req = requests.Request("POST", "https://httpbin.org/post", json={"n": 1}, params={"q": "x"})
prep = req.prepare()
print(prep.method, prep.url.split("?")[1] if prep.url else "")
print(prep.headers.get("Content-Type"))

# --- requests json ---
import requests
try:
    r = requests.get("https://httpbin.org/json", timeout=5)
    r.raise_for_status()
    print("slideshow" in r.json() or "author" in str(r.json()))
except requests.RequestException as e:
    print(type(e).__name__)

# --- requests headers ---
import requests
s = requests.Session()
s.headers.update({"User-Agent": "learn-python/0.1"})
print(s.headers["User-Agent"])
print("user-agent" in s.headers)

# --- requests session ---
import requests
with requests.Session() as s:
    s.cookies.set("n", "1")
    print(s.cookies.get("n"))
    print(s.get("https://example.com", timeout=5).status_code if False else "lazy")
