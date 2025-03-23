# 313. dataclasses.field
#
# field(default_factory=list) gives each instance its own list. compare=False skips a
# field in ==. metadata holds extra info for libraries.
#
# Run: python 313_dataclasses_field/main.py

from dataclasses import dataclass, field
@dataclass
class Bag:
    items: list[int] = field(default_factory=list)
    note: str = field(default="", compare=False)
print(Bag() is not Bag())
print(Bag([1], "a") == Bag([1], "b"))
