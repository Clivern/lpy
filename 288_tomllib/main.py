# 288. tomllib
#
# tomllib reads TOML (3.11+). It only loads; writing is left to third-party tomli-w or
# tomlkit. pyproject.toml is the usual input.
#
# Run: python 288_tomllib/main.py

import tomllib
data = tomllib.loads("name = \"learn\"\nversion = \"0.1.0\"\n")
print(data["name"], data["version"])
