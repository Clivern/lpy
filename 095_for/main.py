# 095. for loops
#
# for name in iterable binds name to each item. It works on any iterable, not just ranges.
# The loop variable leaks into the enclosing scope.
#
# Run: python 095_for/main.py

for ch in "py":
    print(ch)
for i, name in [(0, "Ada"), (1, "Alan")]:
    print(i, name)
