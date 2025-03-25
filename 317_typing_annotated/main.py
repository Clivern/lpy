# 317. Annotated
#
# Annotated[T, meta] attaches extra data for libraries (FastAPI, Pydantic). get_type_hints
# with include_extras keeps it. The first item is the real type.
#
# Run: python 317_typing_annotated/main.py

from typing import Annotated, get_args
Port = Annotated[int, "tcp port"]
print(get_args(Port))
