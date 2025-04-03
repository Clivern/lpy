# 377. Click flags
#
# is_flag=True is a boolean switch. multiple=True gathers repeats. envvar= reads an
# environment variable. required=True fails without a value.
#
# Run: python 377_click_option/main.py

import click
from click.testing import CliRunner
@click.command()
@click.option("--verbose", is_flag=True)
@click.option("--tag", multiple=True)
def run(verbose, tag):
    click.echo(f"{verbose} {','.join(tag)}")
print(CliRunner().invoke(run, ["--verbose", "--tag", "a", "--tag", "b"]).output.strip())
