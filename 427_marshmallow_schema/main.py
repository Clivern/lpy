# 427. marshmallow
#
# Schema.load validates a dict. dump serializes an object. fields.Int and fields.Str
# declare types. Pydantic v2 covers much of this space now.
#
# Run: python 427_marshmallow_schema/main.py

from marshmallow import Schema, fields
class UserSchema(Schema):
    name = fields.Str(required=True)
    year = fields.Int()
print(UserSchema().load({"name": "Ada", "year": 1815}))
print(UserSchema().dump({"name": "Ada", "year": 1815}))
