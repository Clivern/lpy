# 068. In-place set operators
#
# intersection_update (&=), difference_update (-=), and symmetric_difference_update (^=)
# mutate. They return None. Useful when the left set is the accumulator.
#
# Run: python 068_set_in_place/main.py

a = {1, 2, 3, 4}
a.intersection_update([2, 3, 9])
print(a)
a.difference_update([3])
print(a)
a.symmetric_difference_update({2, 8})
print(a)
