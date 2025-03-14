# 289. zipfile
#
# ZipFile reads and writes zip archives. writestr puts bytes at a name. infolist lists
# members. Use with to close the file.
#
# Run: python 289_zipfile/main.py

import zipfile
from io import BytesIO
buf = BytesIO()
with zipfile.ZipFile(buf, "w") as z:
    z.writestr("hello.txt", "hi")
buf.seek(0)
with zipfile.ZipFile(buf) as z:
    print(z.read("hello.txt"), z.namelist())
