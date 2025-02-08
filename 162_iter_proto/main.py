# 162. The iterator protocol
#
# iter(x) calls x.__iter__() and returns an iterator. next(it) calls __next__. for uses
# both. A class can be iterable without being an iterator.
#
# Run: python 162_iter_proto/main.py

class Count:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i

print(list(Count(3)))
