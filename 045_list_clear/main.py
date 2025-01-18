# 045. list.clear
#
# clear() empties the list in place. xs[:] = [] does the same. Other names that refer to
# the same list see it empty. Rebinding xs = [] does not.
#
# Run: python 045_list_clear/main.py

xs = [1, 2, 3]
alias = xs
xs.clear()
print(xs, alias)
ys = [1, 2]
held = ys
ys = []
print(ys, held)
