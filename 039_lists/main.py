# 039. Lists
#
# list is a mutable sequence. append, extend, insert, pop, and indexing mutate or read. *
# repeats. A slice copy is shallow.
#
# Run: python 039_lists/main.py

xs = [1, 2, 3]
xs.append(4)
xs.extend([5, 6])
print(xs[0], xs[-1], xs[1:3])
print(xs.pop(), xs)
print([0] * 3)
