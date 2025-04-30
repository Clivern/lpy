# 074. Date libraries
#
# dateutil, Arrow, and Pendulum.
#
# Run: python 074_dates/main.py

# --- dateutil parse ---
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
print(parse("15 Jan 2025").date())
print(datetime(2025, 1, 31) + relativedelta(months=1))

# --- arrow dates ---
import arrow
a = arrow.get("2025-01-15T12:00:00+00:00")
print(a.shift(days=2).date())
print(a.to("Europe/Berlin").format("YYYY-MM-DD HH:mm"))

# --- arrow shift ---
import arrow
a = arrow.get(2025, 3, 15, 14, 30, tzinfo="UTC")
print(a.floor("hour").datetime.minute)
start, end = a.span("day")
print(start.day, end.hour)

# --- pendulum tz ---
import pendulum
d = pendulum.parse("2025-01-31T00:00:00+00:00")
print(d.add(months=1).to_date_string())
print(pendulum.duration(hours=2).in_seconds())

# --- pendulum period ---
import pendulum
start = pendulum.datetime(2025, 1, 1, tz="UTC")
end = start.add(days=3)
print([d.to_date_string() for d in pendulum.period(start, end).range("days")])
