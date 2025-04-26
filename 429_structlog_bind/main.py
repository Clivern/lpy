# 429. structlog
#
# structlog.get_logger() is a structured logger. bind() adds fields. configure() sets
# processors. JSONRenderer is for log ships.
#
# Run: python 429_structlog_bind/main.py

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
