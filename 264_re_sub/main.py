# 264. re.sub and split
#
# sub replaces matches. The replacement can be a function. split cuts on a pattern.
# flags=re.I ignores case. DOTALL lets . match newlines.
#
# Run: python 264_re_sub/main.py

import re
print(re.sub(r"\s+", " ", "a   b\tc"))
print(re.split(r"[,;]", "a,b;c"))
print(re.findall(r"ada", "ADA", flags=re.I))
