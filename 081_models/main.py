# 081. attrs and marshmallow
#
# Class builders and schemas.
#
# Run: python 081_models/main.py

# --- attrs class ---
from attrs import define, field
@define
class User:
    name: str
    tags: list[str] = field(factory=list)
u = User("Ada")
print(u.name, u.tags, u == User("Ada"))

# --- marshmallow schema ---
from marshmallow import Schema, fields
class UserSchema(Schema):
    name = fields.Str(required=True)
    year = fields.Int()
print(UserSchema().load({"name": "Ada", "year": 1815}))
print(UserSchema().dump({"name": "Ada", "year": 1815}))
