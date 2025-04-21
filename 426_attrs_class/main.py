# 426. attrs
#
# @define is the modern attrs class. frozen=True, slots=True are the usual pair.
# field(factory=list) is default_factory. Pydantic is for validation; attrs is for
# classes.
#
# Run: python 426_attrs_class/main.py

from attrs import define, field
@define
class User:
    name: str
    tags: list[str] = field(factory=list)
u = User("Ada")
print(u.name, u.tags, u == User("Ada"))
