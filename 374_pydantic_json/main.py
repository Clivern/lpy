# 374. Pydantic JSON schema
#
# model_json_schema() is the JSON Schema for OpenAPI. model_validate_json parses a string.
# Round-trip through JSON to see coercions.
#
# Run: python 374_pydantic_json/main.py

from pydantic import BaseModel
class User(BaseModel):
    name: str
    year: int
print(User.model_json_schema()["properties"]["name"]["type"])
print(User.model_validate_json('{"name":"Ada","year":1815}').year)
