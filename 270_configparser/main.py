# 270. configparser
#
# ConfigParser reads INI files. interpolation expands %(name)s. getboolean understands
# yes/no. Interpolation can surprise; RawConfigParser skips it.
#
# Run: python 270_configparser/main.py

import configparser
from io import StringIO
ini = "[db]\nhost = localhost\nport = 5432\n"
c = configparser.ConfigParser()
c.read_file(StringIO(ini))
print(c["db"]["host"], c.getint("db", "port"))
