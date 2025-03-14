# 285. subprocess pipes
#
# input= feeds stdin. stderr can be STDOUT to merge streams. CompletedProcess has args,
# returncode, stdout, stderr.
#
# Run: python 285_subprocess_pipe/main.py

import subprocess, sys
r = subprocess.run(
    [sys.executable, "-c", "import sys; print(sys.stdin.read().upper())"],
    input="hi",
    capture_output=True,
    text=True,
    check=True,
)
print(r.stdout.strip())
