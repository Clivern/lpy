# 051. List concatenation
#
# + allocates a new list. += mutates, like extend, when the left side is a list. That
# difference matters if another name aliases the list.
#
# Run: python 051_list_concat/main.py

a = [1, 2]
b = a
a = a + [3]
print(a, b)
c = [1, 2]
d = c
c += [3]
print(c, d)
