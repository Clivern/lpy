# 019. str.find and index
#
# find returns the first index or -1. index is the same but raises ValueError. rfind and
# rindex search from the right. start and end bound the search like a slice.
#
# Run: python 019_str_find/main.py

s = "abracadabra"
print(s.find("bra"), s.find("z"), s.rfind("bra"))
print(s.index("cad"), s.find("a", 3, 8))
try:
    s.index("z")
except ValueError as e:
    print(type(e).__name__)
