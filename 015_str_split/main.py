# 015. str.split and rsplit
#
# split cuts on whitespace by default, or on a separator. maxsplit limits how many cuts.
# rsplit counts from the right, so maxsplit keeps the left part whole.
#
# Run: python 015_str_split/main.py

s = "a,b,c,d"
print(s.split(","))
print(s.split(",", maxsplit=1))
print(s.rsplit(",", maxsplit=1))
print("  a   b\tc  ".split())
print("a/b/c.py".rsplit("/", maxsplit=1))
