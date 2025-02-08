# 195. tempfile
#
# TemporaryDirectory and NamedTemporaryFile create files that vanish. mkstemp is the low-
# level pair of fd and path. Always use the context manager form.
#
# Run: python 195_tempfile/main.py

import tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "note.txt"
    p.write_text("hello", encoding="utf-8")
    print(p.read_text(encoding="utf-8"), p.exists())
print("gone")
