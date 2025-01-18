# 043. list.pop
#
# pop() removes and returns the last item, O(1). pop(i) removes index i and is O(n). An
# empty list raises IndexError. Use it as a stack.
#
# Run: python 043_list_pop/main.py

xs = [1, 2, 3, 4]
print(xs.pop(), xs)
print(xs.pop(0), xs)
try:
    [].pop()
except IndexError as e:
    print(type(e).__name__)
