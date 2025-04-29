# 436. packaging.version
#
# Version parses PEP 440. v1 < v2 compares. specifier.SpecifierSet(">=1.2") contains
# versions. pip and build tools share this library.
#
# Run: python 436_packaging_version/main.py

from packaging.version import Version
from packaging.specifiers import SpecifierSet
print(Version("1.2.3") < Version("1.10.0"))
print(Version("1.3") in SpecifierSet(">=1.2,<2"))
