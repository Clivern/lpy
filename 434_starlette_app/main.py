# 434. Starlette
#
# Starlette is the ASGI toolkit under FastAPI. Route and TestClient are enough for a tiny
# app. Middleware is a stack of wrap calls.
#
# Run: python 434_starlette_app/main.py

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient
async def ping(request):
    return JSONResponse({"pong": True})
app = Starlette(routes=[Route("/ping", ping)])
print(TestClient(app).get("/ping").json())
