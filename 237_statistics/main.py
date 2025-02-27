# 237. statistics
#
# statistics computes mean, median, mode, pstdev, and quantiles on Python data. For large
# arrays use numpy; this module is for lists of numbers.
#
# Run: python 237_statistics/main.py

import statistics
xs = [1, 2, 2, 3, 8]
print(statistics.mean(xs), statistics.median(xs), statistics.mode(xs))
print(statistics.pstdev(xs))
