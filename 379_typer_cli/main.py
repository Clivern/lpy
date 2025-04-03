# 379. Typer
#
# Typer builds a Click CLI from type hints. Optional[str] = None is an option. Typer() is
# the app. It is FastAPI's sibling for command lines.
#
# Run: python 379_typer_cli/main.py

import typer
from typer.testing import CliRunner
app = typer.Typer()
@app.command()
def hello(name: str = "world"):
    print(f"hi {name}")
print(CliRunner().invoke(app, ["--name", "Ada"]).output.strip())
