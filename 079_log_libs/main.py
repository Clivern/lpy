# 079. loguru and structlog
#
# Ready-made and structured logging.
#
# Run: python 079_log_libs/main.py

# --- loguru log ---
from loguru import logger
import sys
from io import StringIO
buf = StringIO()
logger.remove()
logger.add(buf, format="{level} {message}")
logger.info("hello {name}", name="Ada")
print("hello" in buf.getvalue())

# --- structlog bind ---
import structlog
from io import StringIO
import logging
buf = StringIO()
logging.basicConfig(stream=buf, format="%(message)s", level=logging.INFO)
structlog.configure(
    processors=[structlog.processors.KeyValueRenderer()],
    logger_factory=structlog.stdlib.LoggerFactory(),
)
log = structlog.get_logger("learn").bind(n=1)
log.info("hello")
print("hello" in buf.getvalue())
