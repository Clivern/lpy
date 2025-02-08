# 142. __eq__ and __hash__
#
# __eq__ defines ==. Objects that compare equal should have the same hash if they are
# hashable. Mutable objects should set __hash__ = None.
#
# Run: python 142_eq_hash/main.py

class User:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

print(User(1) == User(1), len({User(1), User(1), User(2)}))
