# 325. atexit
#
# atexit.register runs a function when the interpreter exits normally. It does not run on
# os._exit or a crash. Keep handlers small.
#
# Run: python 325_atexit_mod/main.py

import atexit
atexit.register(lambda: None)
print("registered")
