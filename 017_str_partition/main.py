# 017. str.partition
#
# partition(sep) returns (head, sep, tail) always as three strings. If sep is missing,
# tail is empty. rpartition searches from the right. Useful when you want one cut, not a
# list.
#
# Run: python 017_str_partition/main.py

print("user@host".partition("@"))
print("a:b:c".partition(":"))
print("a:b:c".rpartition(":"))
print("nocolon".partition(":"))
