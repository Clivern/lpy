# 304. csv dialects
#
# excel and unix are built-in dialects. delimiter, quotechar, and lineterminator customize
# one. register_dialect names a reusable set.
#
# Run: python 304_csv_writer/main.py

import csv
from io import StringIO
buf = StringIO()
w = csv.writer(buf, delimiter=";", lineterminator="\n")
w.writerow(["a", "b;c"])
print(buf.getvalue())
