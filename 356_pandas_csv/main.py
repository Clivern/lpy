# 356. pandas CSV
#
# read_csv and to_csv are the usual I/O. parse_dates parses columns. index_col sets the
# index. usecols limits memory. Always pass encoding when the file is not UTF-8.
#
# Run: python 356_pandas_csv/main.py

import pandas as pd
from io import StringIO
text = "name,year\nAda,1815\nAlan,1912\n"
df = pd.read_csv(StringIO(text))
print(df.to_csv(index=False).strip())
print(df.year.dtype)
