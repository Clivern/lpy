# 216. collections.ChainMap
#
# ChainMap searches several mappings in order. Writes go to the first map. Useful for
# layered config: overrides, then env, then defaults.
#
# Run: python 216_chainmap/main.py

from collections import ChainMap
defaults = {"host": "localhost", "port": 80}
env = {"port": 8080}
print(ChainMap(env, defaults)["host"], ChainMap(env, defaults)["port"])
