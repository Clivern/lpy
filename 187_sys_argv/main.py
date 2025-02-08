# 187. sys.argv
#
# sys.argv[0] is the script name. The rest are arguments. argparse is nicer for real CLIs;
# argv is what every parser starts from.
#
# Run: python 187_sys_argv/main.py

import sys
print(sys.argv[0])
print(sys.argv[1:])
