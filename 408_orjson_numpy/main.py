# 408. orjson numpy option
#
# OPT_SERIALIZE_NUMPY encodes ndarrays. OPT_INDENT_2 pretty-prints. OPT_SORT_KEYS is for
# stable diffs. Combine flags with |.
#
# Run: python 408_orjson_numpy/main.py

import orjson
import numpy as np
blob = orjson.dumps(np.array([1, 2, 3]), option=orjson.OPT_SERIALIZE_NUMPY)
print(orjson.loads(blob))
