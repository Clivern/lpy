# 333. requests POST
#
# data= sends a form body. json= sends application/json. params= is the query string. The
# prepared request is r.request.
#
# Run: python 333_requests_post/main.py

import requests
req = requests.Request("POST", "https://httpbin.org/post", json={"n": 1}, params={"q": "x"})
prep = req.prepare()
print(prep.method, prep.url.split("?")[1] if prep.url else "")
print(prep.headers.get("Content-Type"))
