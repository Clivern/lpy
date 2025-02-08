# 188. sys.path
#
# sys.path is the list of directories import searches. The script's directory and the
# site-packages go here. Inserting 0 puts a local folder first. Do not ship that hack.
#
# Run: python 188_sys_path/main.py

import sys
print(sys.path[0])
print(any("site-packages" in p for p in sys.path))
