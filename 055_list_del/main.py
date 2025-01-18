# 055. del on lists
#
# del xs[i] removes by index. del xs[i:j] removes a slice. remove searches by value. pop
# returns the value; del does not.
#
# Run: python 055_list_del/main.py

xs = ["a", "b", "c", "d"]
del xs[1]
print(xs)
del xs[-2:]
print(xs)
