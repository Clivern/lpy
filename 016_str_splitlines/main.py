# 016. str.splitlines
#
# splitlines splits on \n, \r\n, and other unicode line breaks. keepends=True retains the
# break. split("\n") misses \r\n as a single break.
#
# Run: python 016_str_splitlines/main.py

text = "a\nb\r\nc\n"
print(text.splitlines())
print(text.splitlines(keepends=True))
print("a\n".splitlines())
