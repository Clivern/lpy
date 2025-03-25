# 320. TextIOWrapper
#
# open() returns a TextIOWrapper over a buffered binary file. encoding and newline matter.
# encoding="utf-8" is explicit and portable.
#
# Run: python 320_io_text/main.py

from io import BytesIO, TextIOWrapper
raw = BytesIO()
f = TextIOWrapper(raw, encoding="utf-8", newline="\n")
f.write("café\n")
f.flush()
print(raw.getvalue())
