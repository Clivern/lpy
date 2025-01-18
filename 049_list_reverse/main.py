# 049. list.reverse
#
# reverse() reverses in place and returns None. reversed(xs) is a lazy iterator and does
# not mutate. xs[::-1] copies a reversed list.
#
# Run: python 049_list_reverse/main.py

xs = [1, 2, 3]
print(xs.reverse(), xs)
print(list(reversed([1, 2, 3])))
print([1, 2, 3][::-1])
