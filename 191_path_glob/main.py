# 191. Path.glob
#
# Path.glob matches in one directory. rglob recurses. Patterns use * and **. Results are
# an iterator of Path objects.
#
# Run: python 191_path_glob/main.py

from pathlib import Path
hits = list(Path(".").glob("*.md"))
py = list(Path(".").glob("*.py"))
print(len(hits), "md", len(py), "py")
