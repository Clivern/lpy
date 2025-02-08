# 152. Type annotations
#
# name: T and -> T are hints. They do not enforce types at runtime unless a checker or a
# library reads __annotations__. 3.12 can use built-in generics.
#
# Run: python 152_annotations/main.py

def greet(name: str, times: int = 1) -> str:
    return " ".join([f"hi {name}"] * times)

print(greet("Ada", 2))
print(greet.__annotations__)
