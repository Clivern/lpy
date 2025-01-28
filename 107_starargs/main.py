# 107. *args and unpacking calls
#
# *args collects extra positional arguments into a tuple. *seq in a call unpacks a
# sequence into positional arguments.
#
# Run: python 107_starargs/main.py

def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))
print(total(*range(5)))
