# 376. Click groups
#
# @click.group is a parent with subcommands. @cli.command registers one. pass_context
# shares state. Git-style tools are groups.
#
# Run: python 376_click_group/main.py

import click
from click.testing import CliRunner
@click.group()
def cli():
    pass
@cli.command()
@click.argument("name")
def greet(name):
    click.echo(name)
print(CliRunner().invoke(cli, ["greet", "Ada"]).output.strip())
