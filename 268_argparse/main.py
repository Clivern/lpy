# 268. argparse
#
# ArgumentParser is the stdlib CLI. add_argument declares flags. parse_args(argv) is
# testable. help= becomes --help text.
#
# Run: python 268_argparse/main.py

import argparse
p = argparse.ArgumentParser(prog="demo")
p.add_argument("name")
p.add_argument("-n", "--times", type=int, default=1)
ns = p.parse_args(["Ada", "-n", "3"])
print(ns.name, ns.times)
