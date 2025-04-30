# 082. packaging
#
# PEP 440 versions and specifiers.
#
# Run: python 082_packaging/main.py

# --- packaging version ---
from packaging.version import Version
from packaging.specifiers import SpecifierSet
print(Version("1.2.3") < Version("1.10.0"))
print(Version("1.3") in SpecifierSet(">=1.2,<2"))
print(Version("1.0.0") < Version("1.0.1"))

# --- packaging spec ---
from packaging.version import Version, InvalidVersion
v = Version("2.0.0rc1")
print(v.major, v.is_prerelease)
try:
    Version("not-a-version")
except InvalidVersion:
    print("bad")
