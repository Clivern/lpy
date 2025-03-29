# 366. FastAPI Depends
#
# Depends(fn) injects the result of fn. Nested depends share a cache per request. Use it
# for auth, db sessions, and settings.
#
# Run: python 366_fastapi_depends/main.py

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

def user():
    return {"name": "Ada"}

@app.get("/me")
def me(u=Depends(user)):
    return u

print(TestClient(app).get("/me").json())
