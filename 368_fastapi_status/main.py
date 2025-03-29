# 368. FastAPI status codes
#
# status_code= on the decorator sets the default. JSONResponse and HTTPException set it
# per call. 204 must not include a body.
#
# Run: python 368_fastapi_status/main.py

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/gone")
def gone():
    raise HTTPException(status_code=410, detail="gone")

print(TestClient(app).get("/gone").status_code)
