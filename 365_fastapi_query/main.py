# 365. FastAPI query params
#
# Function parameters that are not path params become query params. Optional[str] = None
# is optional. Query() adds min_length and description.
#
# Run: python 365_fastapi_query/main.py

from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/search")
def search(q: str, limit: int = 10):
    return {"q": q, "limit": limit}

print(TestClient(app).get("/search", params={"q": "ada"}).json())
