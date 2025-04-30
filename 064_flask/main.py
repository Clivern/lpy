# 064. Flask
#
# App, routes, JSON, and request.
#
# Run: python 064_flask/main.py

# --- flask hello ---
from flask import Flask
app = Flask(__name__)

@app.get("/")
def index():
    return "hello"

c = app.test_client()
print(c.get("/").data.decode(), c.get("/").status_code)
print(c.get('/').status_code)

# --- flask route ---
from flask import Flask, url_for
app = Flask(__name__)

@app.get("/u/<int:user_id>")
def user(user_id):
    return {"id": user_id}

with app.test_request_context():
    print(url_for("user", user_id=7))
print(app.test_client().get("/u/7").json)

# --- flask json ---
from flask import Flask, request
app = Flask(__name__)

@app.post("/echo")
def echo():
    return {"got": request.get_json()}

c = app.test_client()
r = c.post("/echo", json={"n": 1})
print(r.json, r.status_code)

# --- flask request ---
from flask import Flask, request
app = Flask(__name__)

@app.get("/q")
def q():
    return {"q": request.args.get("q"), "ua": request.headers.get("User-Agent")}

r = app.test_client().get("/q?q=hi", headers={"User-Agent": "learn"})
print(r.json)
