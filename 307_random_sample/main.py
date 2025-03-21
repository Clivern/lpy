# 307. random distributions
#
# gauss, expovariate, and uniform draw from distributions. triangular is a simple bounded
# bell. seed first in tests. numpy has vectorized versions.
#
# Run: python 307_random_sample/main.py

import random
random.seed(1)
print(round(random.uniform(0, 1), 3))
print(round(random.gauss(0, 1), 3))
print(random.randrange(0, 10, 2) % 2 == 0)
