# 159. Generics
#
# list[int] and dict[str, int] parameterize types. On 3.12, class Box[T] declares a type
# variable. They are hints; the runtime still stores whatever you put in.
#
# Run: python 159_generics/main.py

def first[T](items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]), first(["a", "b"]))
