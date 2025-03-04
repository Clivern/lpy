# 260. urllib.parse
#
# urlparse splits a URL. urlencode builds a query string. quote escapes a path segment.
# quote_plus is for form bodies.
#
# Run: python 260_urllib_parse/main.py

from urllib.parse import urlparse, urlencode, quote
u = urlparse("https://example.com:443/a?x=1#f")
print(u.scheme, u.hostname, u.path, u.query)
print(urlencode({"q": "a b"}))
print(quote("a/b c"))
