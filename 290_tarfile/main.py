# 290. tarfile
#
# tarfile reads tar archives, optionally gzipped. addfile and getmembers are the API.
# Never extract untrusted tars without filtering; path traversal is a classic bug.
#
# Run: python 290_tarfile/main.py

import tarfile, io, time
buf = io.BytesIO()
with tarfile.open(fileobj=buf, mode="w") as t:
    data = b"hello"
    info = tarfile.TarInfo("a.txt")
    info.size = len(data)
    info.mtime = time.time()
    t.addfile(info, io.BytesIO(data))
print(buf.tell() > 0)
