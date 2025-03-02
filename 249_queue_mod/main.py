# 249. queue
#
# queue.Queue is a thread-safe FIFO. LifoQueue is a stack. PriorityQueue uses a heap.
# get/put optionally block. For async code, use asyncio.Queue.
#
# Run: python 249_queue_mod/main.py

from queue import Queue
q = Queue()
q.put("a")
q.put("b")
print(q.get(), q.get(), q.empty())
