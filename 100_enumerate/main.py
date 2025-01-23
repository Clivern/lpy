# 100. enumerate
#
# enumerate(iterable, start=0) yields (index, item) pairs. Use it instead of
# range(len(xs)) when you need both index and value.
#
# Run: python 100_enumerate/main.py

for i, ch in enumerate("abc", start=1):
    print(i, ch)
