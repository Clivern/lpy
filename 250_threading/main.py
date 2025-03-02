# 250. threading
#
# Thread(target=fn) runs fn in another OS thread. join waits. The GIL means threads help
# I/O more than CPU. Pass args= as a tuple.
#
# Run: python 250_threading/main.py

import threading
box = []
def work(n):
    box.append(n)
t = threading.Thread(target=work, args=(7,))
t.start()
t.join()
print(box)
