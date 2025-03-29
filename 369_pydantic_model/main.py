# 369. Pydantic models
#
# BaseModel validates and coerces. model_dump() is the dict. model_validate parses a dict.
# Extra fields are forbidden if configured.
#
# Run: python 369_pydantic_model/main.py

from pydantic import BaseModel
class User(BaseModel):
    name: str
    year: int
u = User(name="Ada", year="1815")
print(u.year, u.model_dump())
