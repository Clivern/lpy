# 316. Literal and Final
#
# Literal["a", "b"] restricts a value to those options for checkers. Final marks a name as
# not reassigned. Runtime still stores whatever you put in.
#
# Run: python 316_typing_literal/main.py

from typing import Final, Literal
MODE: Final[Literal["dev", "prod"]] = "dev"
def run(mode: Literal["dev", "prod"]) -> str:
    return mode
print(run(MODE))
