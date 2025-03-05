# 266. textwrap
#
# wrap fills a paragraph to a width. fill joins with newlines. dedent removes common
# leading indent from docstrings. indent prefixes each line.
#
# Run: python 266_textwrap/main.py

import textwrap
print(textwrap.wrap("one two three four five", width=10))
print(textwrap.dedent("    line\n    next").strip())
