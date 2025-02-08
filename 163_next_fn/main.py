# 163. next and default
#
# next(it) raises StopIteration when done. next(it, default) returns the default instead.
# Useful for optional first items.
#
# Run: python 163_next_fn/main.py

it = iter([10, 20])
print(next(it), next(it), next(it, "empty"))
