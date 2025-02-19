# 213. collections.deque
#
# deque is a double-ended queue. appendleft and popleft are O(1). maxlen makes a bounded
# ring. It is the right structure for BFS and rolling windows.
#
# Run: python 213_deque/main.py

from collections import deque
q = deque([1, 2, 3], maxlen=5)
q.appendleft(0)
q.append(4)
print(q, q.popleft())
