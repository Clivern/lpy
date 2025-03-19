# 302. Path read and write
#
# write_text and read_text take encoding=. write_bytes and read_bytes skip encoding.
# mkdir(parents=True, exist_ok=True) is the usual directory create.
#
# Run: python 302_pathlib_write/main.py

from pathlib import Path
import tempfile
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "a" / "b.txt"
    p.parent.mkdir(parents=True)
    p.write_text("hi", encoding="utf-8")
    print(p.read_text(encoding="utf-8"))
