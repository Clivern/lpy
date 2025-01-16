# 032. Multiline strings
#
# Triple quotes hold newlines. A leading newline after """ is part of the string unless
# you escape it. textwrap.dedent strips shared indent from code-shaped text.
#
# Run: python 032_str_multiline/main.py

block = """line one
line two
"""
print(repr(block))
print("""one
two""".splitlines())
