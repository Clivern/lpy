# 139. Multiple inheritance
#
# A class may list several bases. Mixins are small classes meant to be combined. Keep the
# diamond cooperative with super(), not Parent.__init__(self).
#
# Run: python 139_multiple_inherit/main.py

class JSONMixin:
    def to_json(self):
        return {"name": self.name}

class User(JSONMixin):
    def __init__(self, name):
        self.name = name

print(User("Ada").to_json())
