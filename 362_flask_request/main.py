# 362. Flask request
#
# request.args is the query string. request.headers is case-insensitive. request.method is
# the verb. The local is valid only during a request.
#
# Run: python 362_flask_request/main.py

from flask import Flask, request
app = Flask(__name__)

@app.get("/q")
def q():
    return {"q": request.args.get("q"), "ua": request.headers.get("User-Agent")}

r = app.test_client().get("/q?q=hi", headers={"User-Agent": "learn"})
print(r.json)
