# 207. timezone
#
# datetime.timezone.utc is UTC. timezone(timedelta(hours=2)) is a fixed offset. Zone names
# like Europe/Berlin live in zoneinfo, not here.
#
# Run: python 207_timezone/main.py

from datetime import datetime, timezone, timedelta
cet = timezone(timedelta(hours=1), name="CET")
print(datetime(2025, 1, 1, tzinfo=timezone.utc).astimezone(cet))
