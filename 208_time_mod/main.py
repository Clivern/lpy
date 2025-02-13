# 208. time
#
# time.time() is seconds since the Unix epoch. sleep pauses. monotonic() is for measuring
# intervals because it does not jump when the clock is set.
#
# Run: python 208_time_mod/main.py

import time
t0 = time.monotonic()
time.sleep(0.01)
print(round(time.monotonic() - t0, 3) >= 0.01)
print(int(time.time()) > 1_700_000_000)
