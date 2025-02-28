# 242. uuid
#
# uuid4 is random. uuid3/5 are name-based. uuid1 includes a MAC and time. str(u) is the
# hyphenated form. Use uuid4 unless you need determinism.
#
# Run: python 242_uuid_mod/main.py

import uuid
u = uuid.uuid4()
print(u, u.version)
print(uuid.uuid5(uuid.NAMESPACE_DNS, "example.com"))
