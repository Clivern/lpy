# 066. Pydantic
#
# BaseModel, validators, nested models, settings, aliases, and JSON schema.
#
# Run: python 066_pydantic/main.py

# --- pydantic model ---
from pydantic import BaseModel
class User(BaseModel):
    name: str
    year: int
u = User(name="Ada", year="1815")
print(u.year, u.model_dump())
print(list(u.model_fields))

# --- pydantic valid ---
from pydantic import BaseModel, Field, ValidationError
class Item(BaseModel):
    n: int = Field(ge=0, le=100)
try:
    Item(n=-1)
except ValidationError as e:
    print(e.errors()[0]["type"])
print(Item(n=3).n)

# --- pydantic nested ---
from pydantic import BaseModel
class User(BaseModel):
    name: str
class Team(BaseModel):
    users: list[User]
t = Team.model_validate({"users": [{"name": "Ada"}, {"name": "Alan"}]})
print(len(t.users), t.users[0].name)

# --- pydantic settings ---
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LEARN_")
    debug: bool = False
s = Settings(_env_file=None)
print(s.debug, Settings(debug=True).debug)

# --- pydantic alias ---
from pydantic import BaseModel, Field
class User(BaseModel):
    name: str = Field(alias="userName")
    model_config = {"populate_by_name": True}
print(User.model_validate({"userName": "Ada"}).name)
print(User(name="Alan").model_dump(by_alias=True))

# --- pydantic json ---
from pydantic import BaseModel
class User(BaseModel):
    name: str
    year: int
print(User.model_json_schema()["properties"]["name"]["type"])
print(User.model_validate_json('{"name":"Ada","year":1815}').year)
