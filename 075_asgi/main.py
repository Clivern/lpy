# 075. ASGI and aiohttp
#
# aiohttp client, Starlette, and uvicorn Config.
#
# Run: python 075_asgi/main.py

# --- aiohttp get ---
import asyncio
import aiohttp
async def main():
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get("https://example.com") as resp:
            return resp.status
try:
    print(asyncio.run(main()))
except Exception as e:
    print(type(e).__name__)

# --- starlette app ---
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient
async def ping(request):
    return JSONResponse({"pong": True})
app = Starlette(routes=[Route("/ping", ping)])
print(TestClient(app).get("/ping").json())

# --- uvicorn note ---
from uvicorn.config import Config
from starlette.applications import Starlette
app = Starlette()
cfg = Config(app=app, host="127.0.0.1", port=0, lifespan="off", log_config=None)
print(cfg.host, cfg.app is app)
