# 263. re groups
#
# Parentheses capture. (?P<name>...) names a group. groupdict() maps names. (?:...) is
# non-capturing. Groups are the usual way to pick fields out of text.
#
# Run: python 263_re_groups/main.py

import re
m = re.search(r"(?P<user>\w+)@(?P<host>[\w.]+)", "a@b.com")
print(m.group("user"), m.groupdict())
