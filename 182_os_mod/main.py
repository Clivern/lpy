# 182. os
#
# os talks to the operating system. getcwd, listdir, name, and sep are the usual first
# calls. Prefer pathlib for new path work; os still owns env and process helpers.
#
# Run: python 182_os_mod/main.py

import os
print(os.name, os.sep)
print(os.getcwd())
print(len(os.listdir(".")))
