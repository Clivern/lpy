# 251. Locks and RLock
#
# Lock is a mutex. RLock can be acquired again by the same thread. with lock: is the safe
# form. Condition and Event wait for signals.
#
# Run: python 251_locks/main.py

import threading
lock = threading.Lock()
n = 0
def bump():
    global n
    with lock:
        n += 1
ts = [threading.Thread(target=bump) for _ in range(8)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(n)
