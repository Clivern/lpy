# 144. Context managers
#
# __enter__ and __exit__ implement with. __exit__ receives exception info and may suppress
# it by returning True. Files and locks use this.
#
# Run: python 144_context_mgr/main.py

class Tag:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"<{self.name}>")
        return self

    def __exit__(self, *exc):
        print(f"</{self.name}>")
        return False

with Tag("p"):
    print("hello")
