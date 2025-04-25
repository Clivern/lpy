# 428. loguru
#
# from loguru import logger is a ready logger. add() attaches sinks. bind() adds context.
# It replaces a lot of logging boilerplate.
#
# Run: python 428_loguru_log/main.py

from loguru import logger
import sys
from io import StringIO
buf = StringIO()
logger.remove()
logger.add(buf, format="{level} {message}")
logger.info("hello {name}", name="Ada")
print("hello" in buf.getvalue())
