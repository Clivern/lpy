# 185. os.environ
#
# os.environ is a mapping of environment variables. get avoids KeyError. Changes affect
# the current process and children started after the change.
#
# Run: python 185_os_environ/main.py

import os
print(os.environ.get("PATH", "")[:20], "...")
os.environ["LEARN_PYTHON"] = "1"
print(os.environ["LEARN_PYTHON"])
