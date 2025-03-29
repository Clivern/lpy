# 373. Pydantic aliases
#
# Field(alias="userName") maps JSON keys that are not valid Python names. populate_by_name
# allows both. serialization_alias can differ from validation.
#
# Run: python 373_pydantic_alias/main.py

from pydantic import BaseModel, Field
class User(BaseModel):
    name: str = Field(alias="userName")
    model_config = {"populate_by_name": True}
print(User.model_validate({"userName": "Ada"}).name)
print(User(name="Alan").model_dump(by_alias=True))
