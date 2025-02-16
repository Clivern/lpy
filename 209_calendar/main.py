# 209. calendar
#
# calendar can print a month and answer weekday questions. monthcalendar returns weeks as
# lists of day numbers, with 0 for padding.
#
# Run: python 209_calendar/main.py

import calendar
print(calendar.month_name[1], calendar.weekday(2025, 1, 1))
print(calendar.monthcalendar(2025, 1)[0])
