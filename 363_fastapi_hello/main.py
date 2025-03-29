# 363. FastAPI hello
#
# FastAPI() is an ASGI app. TestClient from starlette/fastapi wraps it. Type hints become
# OpenAPI. Return a dict and it becomes JSON.
#
# Run: python 363_fastapi_hello/main.py

from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

print(TestClient(app).get("/health").json())
