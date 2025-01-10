# 018. str.strip
#
# strip removes leading and trailing characters, whitespace by default. lstrip and rstrip
# do one side. The argument is a set of chars, not a prefix string.
#
# Run: python 018_str_strip/main.py

print("  hi  ".strip())
print("xxhelloxx".strip("x"))
print("abca".strip("a"))
print("  hi  ".lstrip(), "  hi  ".rstrip())
print("---title---".strip("-"))
