# 284. subprocess
#
# subprocess.run is the modern API. capture_output and text=True give strings. check=True
# raises on non-zero. Never pass shell=True with untrusted strings.
#
# Run: python 284_subprocess/main.py

import subprocess, sys
r = subprocess.run([sys.executable, "-c", "print(1+1)"], capture_output=True, text=True, check=True)
print(r.stdout.strip(), r.returncode)
