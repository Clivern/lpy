# 361. Flask JSON
#
# Returning a dict makes a JSON response. request.get_json() reads the body. jsonify is
# explicit. 404 is abort(404) or a tuple (body, status).
#
# Run: python 361_flask_json/main.py

from flask import Flask, request
app = Flask(__name__)

@app.post("/echo")
def echo():
    return {"got": request.get_json()}

c = app.test_client()
r = c.post("/echo", json={"n": 1})
print(r.json, r.status_code)
