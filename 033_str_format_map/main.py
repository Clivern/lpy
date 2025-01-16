# 033. format_map
#
# format_map interpolates from a mapping without copying into kwargs. Useful with
# defaultdict so missing keys can yield a default instead of KeyError.
#
# Run: python 033_str_format_map/main.py

from collections import defaultdict
print("{name} {year}".format_map({"name": "Ada", "year": 1815}))
m = defaultdict(lambda: "?", {"name": "Alan"})
print("{name} {city}".format_map(m))
