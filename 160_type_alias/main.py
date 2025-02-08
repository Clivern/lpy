# 160. Type aliases
#
# type Json = dict[str, object] (3.12) names a type. Older code uses Alias = dict[str,
# object] or TypeAlias. Aliases keep signatures short.
#
# Run: python 160_type_alias/main.py

type UserId = int
type JSON = dict[str, object]

def find(user: UserId) -> JSON:
    return {"id": user}

print(find(7))
