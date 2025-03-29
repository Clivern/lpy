# 360. Flask path params
#
# <int:id> converts a path segment. url_for builds a URL from the endpoint name. Methods
# default to GET for @app.get and both for @app.route.
#
# Run: python 360_flask_route/main.py

from flask import Flask, url_for
app = Flask(__name__)

@app.get("/u/<int:user_id>")
def user(user_id):
    return {"id": user_id}

with app.test_request_context():
    print(url_for("user", user_id=7))
print(app.test_client().get("/u/7").json)
