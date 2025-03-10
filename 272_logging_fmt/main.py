# 272. logging handlers
#
# A Logger can have handlers: StreamHandler, FileHandler. setLevel filters per handler.
# extra= passes fields into the formatter.
#
# Run: python 272_logging_fmt/main.py

import logging
from io import StringIO
buf = StringIO()
log = logging.getLogger("buf")
log.setLevel(logging.DEBUG)
h = logging.StreamHandler(buf)
h.setFormatter(logging.Formatter("%(name)s %(message)s"))
log.addHandler(h)
log.warning("boom")
print(buf.getvalue().strip())
