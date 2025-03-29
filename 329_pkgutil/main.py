# 329. pkgutil
#
# pkgutil.iter_modules lists submodules. resolve_name (3.9+) imports from a dotted string.
# Plugin loaders use this to discover packages.
#
# Run: python 329_pkgutil/main.py

import pkgutil
names = [m.name for m in pkgutil.iter_modules() if m.name.startswith("json")]
print("json" in {m.name for m in pkgutil.iter_modules()})
print(len(names) >= 0)
