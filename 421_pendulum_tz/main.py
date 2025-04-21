# 421. Pendulum
#
# pendulum.parse is timezone-aware by default. now() takes a tz. add(months=1) handles
# month ends. duration. in_words is English.
#
# Run: python 421_pendulum_tz/main.py

import pendulum
d = pendulum.parse("2025-01-31T00:00:00+00:00")
print(d.add(months=1).to_date_string())
print(pendulum.duration(hours=2).in_seconds())
