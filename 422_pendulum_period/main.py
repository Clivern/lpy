# 422. Pendulum period
#
# period(start, end) iterates datetimes. range("days") is the step.
# timezone("Europe/Berlin") is a zone. DST is included.
#
# Run: python 422_pendulum_period/main.py

import pendulum
start = pendulum.datetime(2025, 1, 1, tz="UTC")
end = start.add(days=3)
print([d.to_date_string() for d in pendulum.period(start, end).range("days")])
