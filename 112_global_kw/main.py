# 112. global
#
# global name tells the function that assignment should rebind a module-level name. Read-
# only use of a global does not need the keyword.
#
# Run: python 112_global_kw/main.py

count = 0

def bump():
    global count
    count += 1

bump()
bump()
print(count)
