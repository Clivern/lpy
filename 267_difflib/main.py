# 267. difflib
#
# difflib compares sequences. unified_diff is the patch format. get_close_matches suggests
# spellings. SequenceMatcher.ratio is a similarity score.
#
# Run: python 267_difflib/main.py

import difflib
a = "hello world".split()
b = "hello there".split()
print("".join(difflib.unified_diff(a, b, lineterm="")))
print(difflib.get_close_matches("appel", ["ape", "apple", "peach"]))
