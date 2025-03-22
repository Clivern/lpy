# 311. argparse types
#
# type=int converts. choices= restricts. nargs='+' gathers a list. metavar names the help
# placeholder. required=True on optionals is allowed but unusual.
#
# Run: python 311_argparse_types/main.py

import argparse
p = argparse.ArgumentParser()
p.add_argument("--port", type=int, default=8000)
p.add_argument("--mode", choices=["dev", "prod"], default="dev")
p.add_argument("files", nargs="*")
ns = p.parse_args(["--port", "9", "a.py"])
print(ns.port, ns.mode, ns.files)
