# 194. fnmatch
#
# fnmatch matches a name against a glob pattern. filter applies it to a list. It does not
# touch the filesystem; glob does that.
#
# Run: python 194_fnmatch/main.py

import fnmatch
names = ["main.py", "test_main.py", "README.md"]
print(fnmatch.filter(names, "*.py"))
print(fnmatch.fnmatch("Foo.PY", "*.py"))
