# 310. logging levels
#
# DEBUG 10, INFO 20, WARNING 30, ERROR 40, CRITICAL 50. setLevel on the logger.
# isEnabledFor skips expensive debug formatting.
#
# Run: python 310_logging_levels/main.py

import logging
log = logging.getLogger("levels")
log.setLevel(logging.WARNING)
print(log.isEnabledFor(logging.DEBUG), log.isEnabledFor(logging.ERROR))
print(logging.getLevelName(30))
