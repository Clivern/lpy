# 432. freezegun
#
# @freeze_time("2025-01-15") pins datetime.now. tick() advances. Use it so tests do not
# depend on the wall clock. asyncio and time.time are also patched.
#
# Run: python 432_freezegun_time/main.py

from datetime import datetime, timezone
from freezegun import freeze_time
with freeze_time("2025-01-15 12:00:00", tz_offset=0):
    print(datetime.now(timezone.utc).date())
