# 206. timedelta
#
# timedelta is a duration. Adding it to a datetime shifts the clock. total_seconds() is
# the length as a float. There is no months field; calendars are messy.
#
# Run: python 206_timedelta/main.py

from datetime import datetime, timedelta
start = datetime(2025, 1, 1)
print(start + timedelta(days=10, hours=5))
print(timedelta(hours=2).total_seconds())
