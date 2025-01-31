# 121. List comprehensions
#
# [expr for x in it if cond] builds a list. Filters follow the for. Nested fors read left
# to right, like nested loops.
#
# Run: python 121_list_comp/main.py

print([n * n for n in range(6) if n % 2 == 0])
print([f"{a}{b}" for a in "ab" for b in "12"])
