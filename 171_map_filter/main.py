# 171. map and filter
#
# map(fn, it) applies fn lazily. filter(pred, it) keeps true items. Comprehensions are
# usually clearer; map still shows up in APIs.
#
# Run: python 171_map_filter/main.py

print(list(map(str.upper, ["a", "b"])))
print(list(filter(lambda n: n % 2 == 0, range(6))))
