# 119. Walrus operator
#
# := assigns inside an expression. Useful in while, if, and comprehensions so you do not
# compute twice. Keep the expression readable.
#
# Run: python 119_walrus/main.py

import re
text = "id=42"
if m := re.search(r"id=(\d+)", text):
    print(m.group(1))
print(n := 3, n + 1)
