# 370. Pydantic validators
#
# Field(ge=0) constrains numbers. field_validator runs custom checks.
# ValidationError.errors() lists failures. Use this at API boundaries.
#
# Run: python 370_pydantic_valid/main.py

from pydantic import BaseModel, Field, ValidationError
class Item(BaseModel):
    n: int = Field(ge=0, le=100)
try:
    Item(n=-1)
except ValidationError as e:
    print(e.errors()[0]["type"])
print(Item(n=3).n)
