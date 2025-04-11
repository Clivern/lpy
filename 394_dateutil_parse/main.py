# 394. python-dateutil
#
# dateutil.parser.parse is a fuzzy datetime parser. relativedelta adds months correctly.
# tz.gettz loads a named zone. Prefer datetime.fromisoformat when the format is known.
#
# Run: python 394_dateutil_parse/main.py

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
print(parse("15 Jan 2025").date())
print(datetime(2025, 1, 31) + relativedelta(months=1))
