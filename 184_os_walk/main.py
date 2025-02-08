# 184. os.walk
#
# os.walk yields (dirpath, dirnames, filenames) as it traverses a tree. Mutating dirnames
# in place prunes the walk. pathlib.rglob is an alternative.
#
# Run: python 184_os_walk/main.py

import os
n = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in {".git", ".venv", "__pycache__", ".gen"}]
    n += len(files)
    if n > 20:
        break
print("saw at least", n, "files")
