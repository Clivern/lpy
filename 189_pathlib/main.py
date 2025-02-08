# 189. pathlib.Path
#
# Path is an object for filesystem paths. / joins. read_text and write_text handle UTF-8.
# Path.cwd() and Path.home() are the usual starts.
#
# Run: python 189_pathlib/main.py

from pathlib import Path
p = Path.cwd() / "README.md"
print(p.name, p.suffix, p.exists())
print(Path("a/b/c.py").parts)
