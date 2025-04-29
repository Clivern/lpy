# 437. packaging specifiers
#
# InvalidVersion is raised for junk. .major .minor .micro split a release. pre and local
# handle rc and +local. Keep comparisons on Version, not on strings.
#
# Run: python 437_packaging_spec/main.py

from packaging.version import Version, InvalidVersion
v = Version("2.0.0rc1")
print(v.major, v.is_prerelease)
try:
    Version("not-a-version")
except InvalidVersion:
    print("bad")
