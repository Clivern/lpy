# 205. datetime
#
# datetime.datetime is a date and a time. date and time exist separately. naive objects
# have no tzinfo. aware objects do. utcnow is deprecated; use timezone.utc.
#
# Run: python 205_datetime_mod/main.py

from datetime import datetime, timezone
now = datetime.now(timezone.utc)
print(now.year, now.month, now.tzinfo)
print(datetime(2025, 1, 15, 12, 0).isoformat())
print(now.strftime('%A'))
