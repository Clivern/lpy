# 419. Arrow
#
# arrow.get parses many formats. shift(days=1) moves. to("utc") converts. humanize() is
# relative time. Arrow wraps datetime with a fluent API.
#
# Run: python 419_arrow_dates/main.py

import arrow
a = arrow.get("2025-01-15T12:00:00+00:00")
print(a.shift(days=2).date())
print(a.to("Europe/Berlin").format("YYYY-MM-DD HH:mm"))
