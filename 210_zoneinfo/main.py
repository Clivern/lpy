# 210. zoneinfo
#
# ZoneInfo("Europe/Berlin") is a tz database zone. DST is applied for you. Combine with
# datetime.replace(tzinfo=...) or datetime(..., tzinfo=zone).
#
# Run: python 210_zoneinfo/main.py

from datetime import datetime
from zoneinfo import ZoneInfo
winter = datetime(2025, 1, 15, 12, 0, tzinfo=ZoneInfo("Europe/Berlin"))
summer = datetime(2025, 7, 15, 12, 0, tzinfo=ZoneInfo("Europe/Berlin"))
print(winter.strftime("%z"), summer.strftime("%z"))
