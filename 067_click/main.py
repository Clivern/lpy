# 067. Click and Typer
#
# Commands, groups, flags, echo, and Typer type-hint CLIs.
#
# Run: python 067_click/main.py

# --- click cli ---
import click
from click.testing import CliRunner
@click.command()
@click.option("--name", default="world")
def hello(name):
    click.echo(f"hi {name}")
print(CliRunner().invoke(hello, ["--name", "Ada"]).output.strip())
print(CliRunner().invoke(hello, []).output.strip())

# --- click group ---
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

# --- click option ---
import click
from click.testing import CliRunner
@click.command()
@click.option("--verbose", is_flag=True)
@click.option("--tag", multiple=True)
def run(verbose, tag):
    click.echo(f"{verbose} {','.join(tag)}")
print(CliRunner().invoke(run, ["--verbose", "--tag", "a", "--tag", "b"]).output.strip())

# --- click echo ---
import click
from click.testing import CliRunner
@click.command()
def run():
    click.secho("ok", fg="green")
print("ok" in CliRunner().invoke(run).output)

# --- typer cli ---
import typer
from typer.testing import CliRunner
app = typer.Typer()
@app.command()
def hello(name: str = "world"):
    print(f"hi {name}")
print(CliRunner().invoke(app, ["--name", "Ada"]).output.strip())
