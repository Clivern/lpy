# 301. importlib
#
# importlib.import_module loads a module by name. resources.files (3.9+) reads package
# data. reload is for the interpreter, not production apps.
#
# Run: python 301_importlib/main.py

import importlib
m = importlib.import_module("math")
print(m.sqrt(9))
print(importlib.util.find_spec("json").name)
