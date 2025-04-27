# 435. uvicorn
#
# uvicorn is an ASGI server. Config(app=..., lifespan="off") is the object API. In
# production, run the uvicorn command with workers. This lesson only builds a Config.
#
# Run: python 435_uvicorn_note/main.py

from uvicorn.config import Config
from starlette.applications import Starlette
app = Starlette()
cfg = Config(app=app, host="127.0.0.1", port=0, lifespan="off", log_config=None)
print(cfg.host, cfg.app is app)
