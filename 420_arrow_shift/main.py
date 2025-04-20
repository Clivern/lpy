# 420. Arrow shift and span
#
# span("day") is (floor, ceil). floor and ceil snap to a unit. span_range iterates a
# window. These beat hand-rolled timedelta loops.
#
# Run: python 420_arrow_shift/main.py

import arrow
a = arrow.get(2025, 3, 15, 14, 30, tzinfo="UTC")
print(a.floor("hour").datetime.minute)
start, end = a.span("day")
print(start.day, end.hour)
