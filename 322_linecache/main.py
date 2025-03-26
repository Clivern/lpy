# 322. linecache
#
# linecache.getline reads a line from a file by number, with a cache. Tracebacks use it.
# getline(file, 1) is the first line, 1-based.
#
# Run: python 322_linecache/main.py

import linecache, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "x.py"
    p.write_text("a\nb\n", encoding="utf-8")
    print(linecache.getline(str(p), 2).strip())
