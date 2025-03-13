# 283. platform
#
# platform.system, machine, python_version, and platform() describe the host. Useful in
# bug reports. os.uname is POSIX-only; this module is portable.
#
# Run: python 283_platform_mod/main.py

import platform
print(platform.system(), platform.machine())
print(platform.python_version())
