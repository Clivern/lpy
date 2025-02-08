# 183. os.path
#
# os.path.join builds a path for the current OS. split, splitext, exists, and isdir
# inspect it. pathlib.Path is the newer object API for the same jobs.
#
# Run: python 183_os_path/main.py

import os
p = os.path.join("a", "b", "c.py")
print(p, os.path.split(p), os.path.splitext(p))
print(os.path.exists("."), os.path.isdir("."))
