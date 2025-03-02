# 252. Event and Barrier
#
# Event is a flag: wait blocks until set. Barrier waits until N parties arrive. Both are
# in threading. Timeouts return False instead of raising.
#
# Run: python 252_events/main.py

import threading
ev = threading.Event()
def go():
    ev.wait(timeout=1)
    print("released")
t = threading.Thread(target=go)
t.start()
ev.set()
t.join()
