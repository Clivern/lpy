# 261. urllib.request
#
# urlopen performs HTTP. It is in the stdlib and has no session cookies helper like
# requests. For real clients, prefer requests or httpx. Here we parse a file URL.
#
# Run: python 261_urllib_request/main.py

from urllib.request import url2pathname
from urllib.parse import urlparse
print(urlparse("https://example.com/x").netloc)
print(url2pathname("/tmp/x"))
