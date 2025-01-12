# 025. startswith and endswith
#
# startswith and endswith accept a string or a tuple of strings. start and end bound the
# check. A tuple avoids a chain of or tests.
#
# Run: python 025_str_starts_ends/main.py

s = "notes.tar.gz"
print(s.startswith("notes"), s.endswith(".gz"))
print(s.endswith((".gz", ".zip")))
print(s.startswith("tar", 6))
print(not s.startswith("Notes"))
