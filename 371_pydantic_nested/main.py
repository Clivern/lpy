# 371. Nested Pydantic models
#
# A field of type User nests validation. list[User] validates each element.
# model_dump(mode="json") produces JSON-ready types.
#
# Run: python 371_pydantic_nested/main.py

from pydantic import BaseModel
class User(BaseModel):
    name: str
class Team(BaseModel):
    users: list[User]
t = Team.model_validate({"users": [{"name": "Ada"}, {"name": "Alan"}]})
print(len(t.users), t.users[0].name)
