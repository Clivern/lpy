# 269. argparse subcommands
#
# add_subparsers() builds git-style verbs. set_defaults(func=...) dispatches. dest names
# the chosen verb.
#
# Run: python 269_argparse_sub/main.py

import argparse
p = argparse.ArgumentParser()
sub = p.add_subparsers(dest="cmd", required=True)
g = sub.add_parser("greet")
g.add_argument("name")
ns = p.parse_args(["greet", "Ada"])
print(ns.cmd, ns.name)
