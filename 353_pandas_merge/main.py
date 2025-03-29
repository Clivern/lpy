# 353. pandas merge
#
# merge is join. how= is inner, left, right, outer. on= names the key. concat stacks on
# axis 0 or 1. Overlapping names get suffixes.
#
# Run: python 353_pandas_merge/main.py

import pandas as pd
left = pd.DataFrame({"id": [1, 2], "name": ["Ada", "Alan"]})
right = pd.DataFrame({"id": [1, 3], "city": ["London", "Paris"]})
print(left.merge(right, on="id", how="left"))
