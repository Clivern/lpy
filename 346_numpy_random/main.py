# 346. numpy.random
#
# default_rng() is the modern Generator. integers, random, normal, and choice are the
# usual draws. A seed makes tests repeatable.
#
# Run: python 346_numpy_random/main.py

import numpy as np
rng = np.random.default_rng(0)
print(rng.integers(0, 10, size=3))
print(rng.normal(0, 1, size=2).shape)
