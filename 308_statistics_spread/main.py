# 308. statistics spread
#
# variance, stdev, quantiles, and correlation (3.10+) describe a sample. pstdev is
# population. quantiles n=4 are quartiles.
#
# Run: python 308_statistics_spread/main.py

import statistics
xs = [1.0, 2.0, 2.0, 3.0, 8.0]
ys = [1.0, 2.0, 2.1, 2.9, 9.0]
print(statistics.stdev(xs))
print(statistics.quantiles(xs, n=4))
print(statistics.correlation(xs, ys))
