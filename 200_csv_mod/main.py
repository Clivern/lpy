# 200. csv
#
# csv.reader and writer speak RFC-ish CSV. newline='' on the open is required on Windows.
# quoting controls how commas in fields are escaped.
#
# Run: python 200_csv_mod/main.py

import csv
from io import StringIO
buf = StringIO("name,year\nAda,1815\nAlan,1912\n")
print(list(csv.reader(buf)))
out = StringIO()
w = csv.writer(out)
w.writerow(["name", "year"])
w.writerow(["Ada", 1815])
print(out.getvalue())
