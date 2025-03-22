# 309. re flags and VERBOSE
#
# re.I ignores case. M makes ^ $ work per line. S lets . match newline. X (VERBOSE) allows
# comments in the pattern. Combine with |.
#
# Run: python 309_re_flags/main.py

import re
pat = re.compile(r"""
    (?P<year>\d{4})
    -
    (?P<month>\d{2})
""", re.VERBOSE)
print(pat.search("2025-03").groupdict())
