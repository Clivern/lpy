# 378. Click echo and style
#
# click.echo is print with pager and color awareness. style() adds color when the tty
# supports it. secho is echo plus style.
#
# Run: python 378_click_echo/main.py

import click
from click.testing import CliRunner
@click.command()
def run():
    click.secho("ok", fg="green")
print("ok" in CliRunner().invoke(run).output)
