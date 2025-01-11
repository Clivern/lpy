# 021. str.replace
#
# replace(old, new) returns a new string. count= limits how many replacements from the
# left. An empty old inserts new between every character and at the ends.
#
# Run: python 021_str_replace/main.py

print("aa-aa-aa".replace("aa", "b"))
print("aa-aa-aa".replace("aa", "b", 1))
print("x".replace("x", "yz"))
print("ab".replace("", "-"))
