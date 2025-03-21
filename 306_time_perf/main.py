# 306. time.perf_counter
#
# perf_counter is the clock for benchmarks: high resolution, monotonic. process_time is
# CPU time. time.time() is wall clock and can jump.
#
# Run: python 306_time_perf/main.py

import time
t0 = time.perf_counter()
sum(range(10000))
dt = time.perf_counter() - t0
print(dt >= 0, time.process_time() >= 0)
