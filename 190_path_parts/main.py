# 190. Path parts and parents
#
# name, stem, suffix, parent, and parents inspect a Path. with_name and with_suffix build
# a sibling path without mutating the original.
#
# Run: python 190_path_parts/main.py

from pathlib import Path
p = Path("/tmp/demo.tar.gz")
print(p.name, p.stem, p.suffix, p.suffixes)
print(p.parent, p.with_suffix(".txt").name)
