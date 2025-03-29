# 359. Flask hello
#
# Flask(__name__) is the app. @app.get("/") registers a route. test_client() is the in-
# process client. Debug reloader stays off in tests.
#
# Run: python 359_flask_hello/main.py

from flask import Flask
app = Flask(__name__)

@app.get("/")
def index():
    return "hello"

c = app.test_client()
print(c.get("/").data.decode(), c.get("/").status_code)
print(c.get('/').status_code)
