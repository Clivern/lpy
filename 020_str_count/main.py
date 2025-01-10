# 020. str.count
#
# count returns non-overlapping occurrences. Optional start and end limit the range.
# Overlapping patterns are not double-counted: "aaa".count("aa") is 1.
#
# Run: python 020_str_count/main.py

s = "banana"
print(s.count("a"), s.count("ana"), s.count("na"))
print("aaa".count("aa"))
print("abcabc".count("a", 1, 5))
