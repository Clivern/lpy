# 029. maketrans and translate
#
# str.maketrans builds a table for translate. A dict maps characters to strings or None
# (delete). Three-string maketrans maps each char in the first to the second and deletes
# the third.
#
# Run: python 029_str_translate/main.py

table = str.maketrans({"a": "4", "e": "3", "o": None})
print("adobe".translate(table))
table2 = str.maketrans("ae", "43", " ")
print("a e a".translate(table2))
