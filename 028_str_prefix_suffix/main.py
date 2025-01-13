# 028. removeprefix and removesuffix
#
# removeprefix and removesuffix (3.9+) strip an exact prefix or suffix once. Unlike
# strip("xy"), they do not treat the argument as a set of characters.
#
# Run: python 028_str_prefix_suffix/main.py

print("test_mod.py".removesuffix(".py"))
print("test_mod.py".removeprefix("test_"))
print("xxhello".removeprefix("x"))
print("abba".strip("a"), "abba".removeprefix("a").removesuffix("a"))
