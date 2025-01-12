# 024. isspace, isidentifier, isascii
#
# isspace is True for Unicode whitespace. isidentifier matches a valid name (not a keyword
# check). isprintable and isascii catch control chars and non-ASCII.
#
# Run: python 024_str_is_space/main.py

print(" \t\n".isspace(), " a ".isspace())
print("name_1".isidentifier(), "1name".isidentifier(), "class".isidentifier())
print("hi".isprintable(), "\n".isprintable())
print("café".isascii(), "cafe".isascii())
