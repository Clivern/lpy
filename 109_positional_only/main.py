# 109. Positional-only parameters
#
# Parameters before / cannot be passed by name. Builtins like len use this. It leaves the
# name free to change later.
#
# Run: python 109_positional_only/main.py

def dist(x, y, /):
    return (x ** 2 + y ** 2) ** 0.5

print(dist(3, 4))
