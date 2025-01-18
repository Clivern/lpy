# 053. Nested lists
#
# A list of lists is a matrix by convention. Index row then column. Rows can have
# different lengths. deepcopy is needed to copy the inner lists.
#
# Run: python 053_list_nested/main.py

m = [[1, 2, 3], [4, 5, 6]]
print(m[1][0], [row[1] for row in m])
print([n for row in m for n in row])
