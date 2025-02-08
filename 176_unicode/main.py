# 176. Unicode
#
# str holds Unicode code points. ord and chr convert. NFC/NFD normalization changes
# combining marks. len counts code points, not graphemes or bytes.
#
# Run: python 176_unicode/main.py

print(ord("A"), chr(65), "café")
print(len("é"), "é".encode("utf-8"))
print("a\u0301", len("a\u0301"))
