# 193. glob
#
# glob.glob returns matching path strings. glob.iglob is lazy. recursive=True enables **.
# pathlib glob is often enough; this module still appears in older code.
#
# Run: python 193_glob_mod/main.py

import glob
print(glob.glob("*.md"))
print(len(list(glob.iglob("**/*.py", recursive=True) )) >= 0)
