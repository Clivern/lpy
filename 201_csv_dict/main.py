# 201. csv.DictReader
#
# DictReader uses the header row as keys. DictWriter writes from mappings.
# extrasaction='ignore' drops unknown keys on write.
#
# Run: python 201_csv_dict/main.py

import csv
from io import StringIO
text = "name,year\nAda,1815\n"
rows = list(csv.DictReader(StringIO(text)))
print(rows[0]["name"], rows[0]["year"])
