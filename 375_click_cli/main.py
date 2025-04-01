# 375. Click CLI
#
# @click.command and @click.option build a CLI. CliRunner invokes it in tests. echo writes
# to stdout. types convert strings.
#
# Run: python 375_click_cli/main.py

import click
from click.testing import CliRunner
@click.command()
@click.option("--name", default="world")
def hello(name):
    click.echo(f"hi {name}")
print(CliRunner().invoke(hello, ["--name", "Ada"]).output.strip())
