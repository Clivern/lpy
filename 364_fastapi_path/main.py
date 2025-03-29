# 364. FastAPI path params
#
# def show(user_id: int) with /users/{user_id} parses and validates. A non-int path
# returns 422. Response models live in the decorator.
#
# Run: python 364_fastapi_path/main.py

from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/users/{user_id}")
def show(user_id: int):
    return {"id": user_id}

c = TestClient(app)
print(c.get("/users/3").json())
print(c.get("/users/x").status_code)
