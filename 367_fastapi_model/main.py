# 367. FastAPI request body
#
# A Pydantic model as a parameter is the JSON body. Validation errors are 422 with a
# detail list. response_model filters the output.
#
# Run: python 367_fastapi_model/main.py

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
