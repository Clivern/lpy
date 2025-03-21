# 305. strftime and strptime
#
# strftime formats a datetime. strptime parses a string. %Y %m %d %H %M %S are the usual
# pieces. fromisoformat handles the ISO form on recent Pythons.
#
# Run: python 305_datetime_fmt/main.py

from datetime import datetime
d = datetime(2025, 3, 14, 15, 9, 26)
print(d.strftime("%Y-%m-%d %H:%M"))
print(datetime.strptime("2025-01-02", "%Y-%m-%d").date())
print(datetime.fromisoformat("2025-01-02T03:04:05"))
