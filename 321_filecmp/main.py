# 321. filecmp
#
# filecmp.cmp compares two files. dircmp compares directories. shallow=True compares stat
# first. Good enough for tests; hashes are for integrity.
#
# Run: python 321_filecmp/main.py

import filecmp, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    a, b = Path(d) / "a.txt", Path(d) / "b.txt"
    a.write_text("x", encoding="utf-8")
    b.write_text("x", encoding="utf-8")
    print(filecmp.cmp(a, b, shallow=False))
