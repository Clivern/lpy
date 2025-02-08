# 186. sys
#
# sys holds interpreter state: version, platform, path, argv, stdin/stdout/stderr, and
# exit. version_info is a tuple you can compare.
#
# Run: python 186_sys_mod/main.py

import sys
print(sys.version_info[:3], sys.platform)
print(sys.executable)
print(len(sys.path))
