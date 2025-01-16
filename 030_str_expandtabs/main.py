# 030. expandtabs
#
# expandtabs replaces \t with spaces so columns line up. tabsize defaults to 8. The next
# tab stop depends on the current column, not a fixed 8 spaces per tab.
#
# Run: python 030_str_expandtabs/main.py

print("a\tb\tc".expandtabs(4))
print("1234\tX".expandtabs(4))
print(len("\t".expandtabs(4)))
