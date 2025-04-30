# 065. FastAPI
#
# Path, query, Depends, request models, and status codes.
#
# Run: python 065_fastapi/main.py

# --- fastapi hello ---
from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

print(TestClient(app).get("/health").json())
print(TestClient(app).get('/health').status_code)

# --- fastapi path ---
from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/users/{user_id}")
def show(user_id: int):
    return {"id": user_id}

c = TestClient(app)
print(c.get("/users/3").json())
print(c.get("/users/x").status_code)

# --- fastapi query ---
from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/search")
def search(q: str, limit: int = 10):
    return {"q": q, "limit": limit}

print(TestClient(app).get("/search", params={"q": "ada"}).json())

# --- fastapi depends ---
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

def user():
    return {"name": "Ada"}

@app.get("/me")
def me(u=Depends(user)):
    return u

print(TestClient(app).get("/me").json())

# --- fastapi model ---
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    n: int = 1

@app.post("/items")
def create(item: Item):
    return item

c = TestClient(app)
print(c.post("/items", json={"name": "x"}).json())
print(c.post("/items", json={}).status_code)

# --- fastapi status ---
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/gone")
def gone():
    raise HTTPException(status_code=410, detail="gone")

print(TestClient(app).get("/gone").status_code)
