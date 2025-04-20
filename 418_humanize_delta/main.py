# 418. humanize deltas
#
# naturaldelta and precisedelta format timedeltas. naturalday talks about a date relative
# to today. Clocks in UIs use these.
#
# Run: python 418_humanize_delta/main.py

import humanize
from datetime import timedelta
print(humanize.naturaldelta(timedelta(days=2, hours=3)))
print(humanize.precisedelta(timedelta(seconds=90), minimum_unit="seconds"))
