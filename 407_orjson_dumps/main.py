# 407. orjson
#
# orjson.dumps returns bytes, not str. It is fast and supports datetime and numpy with
# option flags. loads parses bytes or str.
#
# Run: python 407_orjson_dumps/main.py

import orjson
from datetime import datetime, timezone
blob = orjson.dumps({"n": 1, "t": datetime(2025, 1, 1, tzinfo=timezone.utc)}, option=orjson.OPT_UTC_Z)
print(orjson.loads(blob)["n"], blob[:1])
