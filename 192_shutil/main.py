# 192. shutil
#
# shutil copies files and trees. copy2 keeps metadata. which finds an executable on PATH.
# disk_usage reports free space.
#
# Run: python 192_shutil/main.py

import shutil
from pathlib import Path
print(shutil.which("python3") or shutil.which("python"))
u = shutil.disk_usage(Path.cwd())
print(u.total > u.free)
