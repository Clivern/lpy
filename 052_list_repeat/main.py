# 052. List repetition
#
# [x] * n repeats references to the same x. For mutable x that is a trap: all rows of
# [[0]*3]*2 are one row. Use a comprehension for independent rows.
#
# Run: python 052_list_repeat/main.py

print([0] * 3)
row = [0] * 3
grid = [row, row]
grid[0][0] = 1
print(grid)
print([[0] * 3 for _ in range(2)])

# Each row must be a new list, not a repeated reference.
