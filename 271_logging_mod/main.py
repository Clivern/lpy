# 271. logging
#
# logging.getLogger(__name__) is the usual logger. basicConfig sets a level and format
# once. debug info warning error critical are the levels.
#
# Run: python 271_logging_mod/main.py

import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("learn")
log.info("hello")
log.debug("hidden")
print("ok")
